import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from torch import nn
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import os


@dataclass
class TrainingConfig:
    mode: str = "separate"
    backbone_mode: str = "independent"
    batch_size: int = 8
    learning_rate: float = 1e-5
    epochs: int = 3
    warmup_steps: int = 100


class DualModelHateDetector:
    CATEGORIES = {
        'IHC': ['vanilla', 'incitement', 'inferiority', 'irony', 'other', 'stereotypical', 'threatening', 'white_grievance'],
        'SBIC': ['vanilla', 'body', 'culture', 'disabled', 'gender', 'race', 'social', 'victim']
    }

    def __init__(self, model_path: str, dataset: str = 'IHC', device: Optional[str] = None):
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.dataset = dataset
        self.categories = self.CATEGORIES.get(dataset, self.CATEGORIES['IHC'])
        self.cat2id = {c: i for i, c in enumerate(self.categories)}
        self.id2cat = {i: c for c, i in self.cat2id.items()}

        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            trust_remote_code=True,
            torch_dtype=torch.bfloat16 if self.device == 'cuda' else torch.float32
        ).to(self.device)
        self.model.eval()

    def build_model1_prompt(self, post: str) -> str:
        cat_list = ', '.join(self.categories)
        return f"""Given the following post, predict its category and target.
Category must be one of: {cat_list}.

Post: {post}

Category:"""

    def build_model2_prompt(self, post: str, category: str, target: str) -> str:
        return f"Post: {post}\nCategory: {category}\nTarget: {target}\n\nIs this post toxic? Answer only 'toxic' or 'not_toxic'."

    def parse_model1_output(self, output: str) -> Tuple[str, str]:
        category = 'vanilla'
        target = 'unspecified'
        output_lower = output.lower()

        if 'category:' in output_lower:
            try:
                cat_part = output_lower.split('category:')[1].split(',')[0].strip()
                for cat in self.categories:
                    if cat in cat_part or cat_part in cat:
                        category = cat
                        break
            except:
                pass

        if 'target:' in output_lower:
            try:
                tgt_part = output_lower.split('target:')[1].strip()
                tgt_clean = tgt_part.split('\n')[0].strip().strip('"\'')
                if tgt_clean and tgt_clean != 'unspecified':
                    target = tgt_clean
            except:
                pass

        return category, target

    def predict_model1(self, post: str) -> Tuple[str, str]:
        prompt = self.build_model1_prompt(post)
        inputs = self.tokenizer(prompt, return_tensors='pt').to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=128,
                temperature=0.1,
                do_sample=False
            )

        response = self.tokenizer.decode(
            outputs[0][inputs['input_ids'].shape[1]:],
            skip_special_tokens=True
        )
        return self.parse_model1_output(response)

    def predict_model2(self, post: str, category: str, target: str) -> str:
        prompt = self.build_model2_prompt(post, category, target)
        inputs = self.tokenizer(prompt, return_tensors='pt').to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=32,
                temperature=0.1,
                do_sample=False
            )

        response = self.tokenizer.decode(
            outputs[0][inputs['input_ids'].shape[1]:],
            skip_special_tokens=True
        ).lower().strip()

        if 'toxic' in response and 'not_toxic' not in response:
            return 'toxic'
        elif 'not_toxic' in response:
            return 'not_toxic'
        else:
            return 'toxic' if len(response) < 10 else 'not_toxic'

    def infer(self, post: str) -> Dict:
        category, target = self.predict_model1(post)
        label = self.predict_model2(post, category, target)
        return {
            'post': post,
            'category': category,
            'target': target,
            'label': label
        }

    def batch_infer(self, posts: List[str]) -> List[Dict]:
        return [self.infer(post) for post in posts]


class DualModelTrainer:
    def __init__(
        self,
        model1_path: str,
        model2_path: str,
        dataset: str,
        config: TrainingConfig
    ):
        self.config = config
        self.dataset = dataset
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        self.model1 = DualModelHateDetector(model1_path, dataset, self.device)
        self.model2 = DualModelHateDetector(model2_path, dataset, self.device)

        self.categories = self.model1.categories
        self.cat2id = self.model1.cat2id

    def train_model1_separate(self, train_data: List[Dict], valid_data: List[Dict]):
        print("Training Model 1 (separate mode)...")

        optimizer = torch.optim.AdamW(
            list(self.model1.model.parameters()),
            lr=self.config.learning_rate
        )

        for epoch in range(self.config.epochs):
            self.model1.model.train()
            total_loss = 0

            for i in range(0, len(train_data), self.config.batch_size):
                batch = train_data[i:i + self.config.batch_size]

                prompts = [self.model1.build_model1_prompt(d['post']) for d in batch]
                category_labels = [self.cat2id.get(d['category'], 0) for d in batch]

                inputs = self.model1.tokenizer(
                    prompts,
                    return_tensors='pt',
                    padding=True,
                    truncation=True,
                    max_length=512
                ).to(self.device)

                with torch.no_grad():
                    targets_input = self.model1.tokenizer(
                        [f"Category: {d['category']}\nTarget: {d['target']}" for d in batch],
                        return_tensors='pt',
                        padding=True,
                        truncation=True,
                        max_length=128
                    ).to(self.device)

                outputs = self.model1.model(
                    input_ids=inputs['input_ids'],
                    attention_mask=inputs['attention_mask'],
                    labels=targets_input['input_ids']
                )

                loss = outputs.loss
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                total_loss += loss.item()

                if (i // self.config.batch_size) % 50 == 0:
                    print(f"  Epoch {epoch+1}, Step {i//self.config.batch_size}, Loss: {loss.item():.4f}")

            avg_loss = total_loss / (len(train_data) // self.config.batch_size)
            print(f"  Epoch {epoch+1} completed, Avg Loss: {avg_loss:.4f}")

    def train_model2_separate(self, train_data: List[Dict], valid_data: List[Dict]):
        print("Training Model 2 (separate mode)...")

        optimizer = torch.optim.AdamW(
            list(self.model2.model.parameters()),
            lr=self.config.learning_rate
        )

        for epoch in range(self.config.epochs):
            self.model2.model.train()
            total_loss = 0

            for i in range(0, len(train_data), self.config.batch_size):
                batch = train_data[i:i + self.config.batch_size]

                prompts = [self.model2.build_model2_prompt(d['post'], d['category'], d['target']) for d in batch]
                labels = [1 if d['label'] == 'toxic' else 0 for d in batch]

                inputs = self.model2.tokenizer(
                    prompts,
                    return_tensors='pt',
                    padding=True,
                    truncation=True,
                    max_length=512
                ).to(self.device)

                with torch.no_grad():
                    targets_input = self.model2.tokenizer(
                        [d['label'] for d in batch],
                        return_tensors='pt',
                        padding=True,
                        truncation=True,
                        max_length=32
                    ).to(self.device)

                outputs = self.model2.model(
                    input_ids=inputs['input_ids'],
                    attention_mask=inputs['attention_mask'],
                    labels=targets_input['input_ids']
                )

                loss = outputs.loss
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                total_loss += loss.item()

                if (i // self.config.batch_size) % 50 == 0:
                    print(f"  Epoch {epoch+1}, Step {i//self.config.batch_size}, Loss: {loss.item():.4f}")

            avg_loss = total_loss / (len(train_data) // self.config.batch_size)
            print(f"  Epoch {epoch+1} completed, Avg Loss: {avg_loss:.4f}")

    def train_joint(self, train_data: List[Dict], valid_data: List[Dict]):
        print("Training Jointly (mode=joint, backbone_mode=independent)...")
        print("  Model1 and Model2 have independent backbones")
        print("  Joint loss: L = L_label + L_category + L_target")

        optimizer = torch.optim.AdamW(
            list(self.model1.model.parameters()) + list(self.model2.model.parameters()),
            lr=self.config.learning_rate
        )

        for epoch in range(self.config.epochs):
            self.model1.model.train()
            self.model2.model.train()
            total_loss = 0

            for i in range(0, len(train_data), self.config.batch_size):
                batch = train_data[i:i + self.config.batch_size]

                prompts1 = [self.model1.build_model1_prompt(d['post']) for d in batch]
                inputs1 = self.model1.tokenizer(
                    prompts1,
                    return_tensors='pt',
                    padding=True,
                    truncation=True,
                    max_length=512
                ).to(self.device)

                cat_labels = [self.cat2id.get(d['category'], 0) for d in batch]
                tgt_labels = [d['target'] for d in batch]

                outputs1 = self.model1.model(
                    input_ids=inputs1['input_ids'],
                    attention_mask=inputs1['attention_mask']
                )

                cat_logits = outputs1.logits[:, 0]
                loss_cat = nn.CrossEntropyLoss()(cat_logits, torch.tensor(cat_labels).to(self.device))

                prompts2 = [self.model2.build_model2_prompt(d['post'], d['category'], d['target']) for d in batch]
                inputs2 = self.model2.tokenizer(
                    prompts2,
                    return_tensors='pt',
                    padding=True,
                    truncation=True,
                    max_length=512
                ).to(self.device)

                labels = [1 if d['label'] == 'toxic' else 0 for d in batch]

                outputs2 = self.model2.model(
                    input_ids=inputs2['input_ids'],
                    attention_mask=inputs2['attention_mask']
                )

                label_logits = outputs2.logits[:, 0]
                loss_label = nn.CrossEntropyLoss()(label_logits, torch.tensor(labels).to(self.device))

                loss = loss_cat + loss_label

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                total_loss += loss.item()

                if (i // self.config.batch_size) % 50 == 0:
                    print(f"  Epoch {epoch+1}, Step {i//self.config.batch_size}, Loss: {loss.item():.4f}")

            avg_loss = total_loss / (len(train_data) // self.config.batch_size)
            print(f"  Epoch {epoch+1} completed, Avg Loss: {avg_loss:.4f}")

    def train(self, train_data: List[Dict], valid_data: List[Dict]):
        if self.config.mode == "separate":
            self.train_model1_separate(train_data, valid_data)
            self.train_model2_separate(train_data, valid_data)
        elif self.config.mode == "joint":
            self.train_joint(train_data, valid_data)

    def save_models(self, save_dir: str):
        os.makedirs(save_dir, exist_ok=True)
        self.model1.model.save_pretrained(os.path.join(save_dir, "model1"))
        self.model1.tokenizer.save_pretrained(os.path.join(save_dir, "model1"))
        self.model2.model.save_pretrained(os.path.join(save_dir, "model2"))
        self.model2.tokenizer.save_pretrained(os.path.join(save_dir, "model2"))
        print(f"Models saved to {save_dir}")

    def load_models(self, save_dir: str):
        self.model1.model.from_pretrained(os.path.join(save_dir, "model1"))
        self.model2.model.from_pretrained(os.path.join(save_dir, "model2"))
        print(f"Models loaded from {save_dir}")


def load_data(file_path: str) -> List[Dict]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def evaluate(predictions: List[str], references: List[str]) -> Dict:
    tp = sum(1 for p, r in zip(predictions, references) if p == 'toxic' and r == 'toxic')
    tn = sum(1 for p, r in zip(predictions, references) if p == 'not_toxic' and r == 'not_toxic')
    fp = sum(1 for p, r in zip(predictions, references) if p == 'toxic' and r == 'not_toxic')
    fn = sum(1 for p, r in zip(predictions, references) if p == 'not_toxic' and r == 'toxic')

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else 0

    return {
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'accuracy': accuracy
    }


def main():
    import argparse
    from datetime import datetime
    parser = argparse.ArgumentParser()
    parser.add_argument('--model1_path', type=str, required=True)
    parser.add_argument('--model2_path', type=str, required=True)
    parser.add_argument('--data_file', type=str, required=True)
    parser.add_argument('--mode', type=str, choices=['separate', 'joint'], default='separate')
    parser.add_argument('--backbone_mode', type=str, choices=['shared', 'independent'], default='independent')
    parser.add_argument('--save_dir', type=str, default=None)
    parser.add_argument('--dataset', type=str, default='IHC')
    args = parser.parse_args()

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    exp_name = f"{args.dataset}_{args.mode}_{timestamp}"
    save_dir = args.save_dir or f"checkpoints/{exp_name}"

    config = TrainingConfig(mode=args.mode, backbone_mode=args.backbone_mode)
    trainer = DualModelTrainer(args.model1_path, args.model2_path, args.dataset, config)

    train_data = load_data(args.data_file)
    print(f"Loaded {len(train_data)} training samples")
    print(f"Experiment: {exp_name}")

    trainer.train(train_data, [])
    trainer.save_models(save_dir)


if __name__ == '__main__':
    main()