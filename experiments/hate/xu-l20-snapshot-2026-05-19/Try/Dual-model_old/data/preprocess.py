import json
import os
from typing import Dict, List, Any


def process_sample(sample: Dict, is_training: bool = True) -> Dict:
    result = {
        'id': sample.get('id', ''),
        'post': sample['post'],
        'label': sample['class']
    }

    if is_training:
        if sample['class'] == 'toxic' and sample.get('hate_class') and sample['hate_class'] != ['none']:
            result['category'] = sample['hate_class'][0]
            result['target'] = sample['target'][0] if sample['target'] and sample['target'] != ['none'] else 'unspecified'
        else:
            result['category'] = 'vanilla'
            result['target'] = 'unspecified'
    else:
        result['category'] = 'vanilla'
        result['target'] = 'unspecified'

    return result


def prepare_data(data_dir: str, split: str, is_training: bool = True) -> List[Dict]:
    file_path = os.path.join(data_dir, f'{split}.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [process_sample(s, is_training) for s in data]


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--split', type=str, choices=['train', 'valid', 'test'], required=True)
    parser.add_argument('--is_training', action='store_true')
    args = parser.parse_args()

    processed = prepare_data(args.data_dir, args.split, args.is_training)

    os.makedirs(args.output_dir, exist_ok=True)
    output_path = os.path.join(args.output_dir, f'{split}_processed.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(processed, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(processed)} samples to {output_path}")


if __name__ == '__main__':
    main()