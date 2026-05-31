#!/bin/bash

MODEL_PATH="/data/public_model/Qwen3-4B"
DATASET=${1:-IHC}
SPLIT=${2:-test}

echo "Running inference on ${DATASET} ${SPLIT}..."

python3 -c "
import sys
sys.path.insert(0, 'model')
from dual_model import DualModelHateDetector, load_data, evaluate

detector = DualModelHateDetector('${MODEL_PATH}', dataset='${DATASET}')
data = load_data('data/${DATASET}/${SPLIT}_processed.json')

posts = [d['post'] for d in data]
references = [d['label'] for d in data]

predictions = []
for i, post in enumerate(posts):
    if i % 100 == 0:
        print(f'Processing {i}/{len(posts)}...')
    result = detector.infer(post)
    predictions.append(result['label'])

metrics = evaluate(predictions, references)
print(f'\nResults on ${DATASET} ${SPLIT}:')
for k, v in metrics.items():
    print(f'  {k}: {v:.4f}')
"