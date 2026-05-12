---
created: 2026-04-23
updated: 2026-05-12
tags: [concept, hate-speech, generalization]
sources:
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.20.pdf
  - raw/sources/2025.woah-1.45.pdf
  - raw/sources/2505.06149v3.pdf
---

# Hate Speech Generalization and Transfer

## Problem
Performance drops under domain, platform, language, and style shifts.

## Strategy Patterns
- Contrastive learning
- Causal/disentangled representations
- Retrieval-augmented adaptation
- Counterfactual augmentation
- Cross-lingual transfer
- Definition-aware prompting
- Compositional target-expression balancing

## Practical Takeaway
A robust pipeline likely needs multiple strategies together rather than a single model trick.

## Recent Pure-Text Additions

- [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] treats generalization as compositional robustness over unseen target/expression/slot combinations.
- [[153-mnassri-2025-rag-and-recall-multilingual-hate-speech-detection-with-semantic-memory]] uses multilingual RAG plus semantic cache memory for English, French, and Arabic detection.
- [[156-melis-2025-a-modular-taxonomy-for-hate-speech-definitions-and-its-impact-on-zero-shot-llm-classification-performance]] shows that construct definitions alter false-positive and false-negative behavior in zero-shot LLM classification.
- [[157-ghorbanpour-2025-can-prompting-llms-unlock-hate-speech-detection-across-languages]] compares multilingual prompting with fine-tuned encoders across eight non-English languages and functional hate tests.
