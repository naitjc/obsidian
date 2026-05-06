---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, retrieval, prompting, explainability]
sources: [raw/sources/Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection.pdf]
---

# Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection

## Metadata
- Source file: `raw/sources/Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection.pdf`
- Year: 2025
- Pages: 23
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Addresses hateful meme detection with large multimodal models, where performance and out-of-domain generalization remain limited.
- Notes that supervised fine-tuning and in-context learning alone can degrade general vision-language ability or fail to adapt robustly.
- Frames hateful meme detection as requiring both image-text understanding and reliable rationale generation.

## Method
- Proposes RA-HMD, a retrieval-augmented framework for hateful meme detection.
- Combines architectural enhancements with a two-stage fine-tuning strategy for adapting large multimodal models.
- Uses retrieved related examples or knowledge to improve classification and rationale quality.

## Data and Evaluation Setup
- Evaluates on hateful meme datasets and checks whether adaptation preserves general multimodal benchmark ability.
- Compares RA-HMD against supervised fine-tuning and other adaptation baselines.
- Assesses both detection performance and generated rationales.

## Results and Claims
- Claims improved hateful meme detection performance and better rationale quality than standard supervised fine-tuning.
- Reports stronger robustness to out-of-domain settings while preserving general vision-language capabilities.
- Exact dataset scores remain metrics-matrix evidence rather than publication-ready claims unless manually checked.

## Limitations and Follow-ups
- Retrieval quality can constrain both classification and rationale generation.
- Adaptation behavior may differ across LMM backbones and meme distributions.
- Verify exact metrics, benchmark settings, and rationale evaluation details before citation.

## Structured Signals
- Detected method keywords: multimodal hate detection, retrieval augmentation, large multimodal models, rationale generation
- Mentioned datasets: Hateful Memes and related hateful meme datasets
- Mentioned metrics: accuracy, AUC, rationale win rate

## Abstract (Extracted)
> The paper proposes RA-HMD, a retrieval-augmented adaptation framework for large multimodal models in hateful meme detection. It aims to improve detection, rationale quality, and out-of-domain robustness without degrading general vision-language capabilities.

## Evidence Handling
- Removed noisy auto-extracted benchmark snippets from the page body.
- Treat hateful-meme benchmark scores and rationale results as metrics-matrix evidence requiring table-level verification before external citation.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
