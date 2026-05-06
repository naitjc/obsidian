---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, retrieval, prompting]
sources: [raw/sources/Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning.pdf]
---

# Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning

## Metadata
- Source file: `raw/sources/Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning.pdf`
- Year: 2024
- Pages: 15
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Hateful meme detection requires joint image-text reasoning, where subtle changes in either modality can flip the label.
- The paper focuses on the weakness of existing CLIP-based hateful meme systems: their embedding spaces are not sensitive enough to fine-grained hateful versus non-hateful distinctions.
- The practical motivation is fast adaptation to evolving online meme content without relying only on very large multimodal models.

## Method
- Proposes retrieval-guided contrastive learning (RGCL) to construct a hatefulness-aware embedding space.
- Uses retrieved hard examples to sharpen representations for confounder memes and nearest-neighbor classification.
- Keeps the system retrieval-oriented and comparatively lightweight rather than depending solely on fine-tuned large multimodal models.

## Data and Evaluation Setup
- Evaluates on HatefulMemes and cross-dataset hateful meme settings, including HarMeme evidence used in the metrics matrix.
- Reports AUC and accuracy, with nearest-neighbor majority voting over the learned representation space.
- The publication-checked metrics row is tracked in [[hate-speech-metrics-matrix]].

## Results and Claims
- RGCL improves HateCLIPper-style retrieval classification and is reported as competitive with much larger multimodal systems.
- Publication-checked values: HateCLIPper with RGCL reports HatefulMemes AUC 87.0 and accuracy 78.8; HarMeme AUC 91.8 and accuracy 87.0.
- The result is most useful as evidence for retrieval-guided representation learning in hateful meme detection, not as a global SOTA claim across all multimodal hate settings.

## Limitations and Follow-ups
- Benchmark interpretation depends on dataset definitions, annotation bias, and the scope of hateful meme labels.
- Cross-dataset generalization is the key follow-up: check whether retrieval examples remain useful when meme styles, targets, and social context shift.
- Exact metrics for this priority row are publication-checked in [[hate-speech-metrics-matrix]].

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, prompting, multimodal
- Mentioned datasets: hateful memes, gab, twitter
- Mentioned metrics: f1, accuracy, auc

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-datasets-and-benchmarks]]
