import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Dict, List, Optional, Tuple


class DualModelHateDetector:
    CATEGORIES = {
        'IHC': ['vanilla', 'incitement', 'inferiority', 'irony', 'other', 'stereotypical', 'threatening', 'white_grievance'],
        'SBIC': ['vanilla', 'body', 'culture', 'disabled', 'gender', 'race', 'social', 'victim']
    }

    def __init__(self, model_path: str, dataset: str = 'IHC', device: Optional[str] = None):
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        self.dataset = dataset
        self.categories = self.CATEGORIES.get(dataset, self.CATEGORIES['IHC'])
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
    parser.add_argument('--model_path', type=str, required=True)
    parser.add_argument('--data_file', type=str, required=True)
    parser.add_argument('--output_file', type=str, default=None)
    parser.add_argument('--dataset', type=str, default='IHC')
    parser.add_argument('--exp_name', type=str, default=None)
    args = parser.parse_args()

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    exp_name = args.exp_name or f"{args.dataset}_inference"
    output_file = args.output_file or f"results/{exp_name}_{timestamp}.json"

    detector = DualModelHateDetector(args.model_path, dataset=args.dataset)
    data = load_data(args.data_file)

    posts = [d['post'] for d in data]
    references = [d['label'] for d in data]

    predictions = []
    for i, post in enumerate(posts):
        if i % 100 == 0:
            print(f"Processing {i}/{len(posts)}...")
        result = detector.infer(post)
        predictions.append(result['label'])

    metrics = evaluate(predictions, references)
    print(f"\nResults:")
    for k, v in metrics.items():
        print(f"  {k}: {v:.4f}")

    import os
    os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump({
            'predictions': predictions,
            'metrics': metrics,
            'exp_name': exp_name,
            'timestamp': timestamp
        }, f, indent=2)


if __name__ == '__main__':
    main()