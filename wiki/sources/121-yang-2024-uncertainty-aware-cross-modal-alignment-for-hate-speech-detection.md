---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, causal, retrieval, prompting, explainability]
sources: [raw/sources/Yang 等 - 2024 - Uncertainty-Aware Cross-Modal Alignment for Hate Speech Detection.pdf]
---

# Yang 等 - 2024 - Uncertainty-Aware Cross-Modal Alignment for Hate Speech Detection

## Metadata
- Source file: `raw/sources/Yang 等 - 2024 - Uncertainty-Aware Cross-Modal Alignment for Hate Speech Detection.pdf`
- Year: 2024
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Multimodal hate speech often depends on the alignment between text and image; either modality alone may be insufficient.
- Existing multimodal classifiers can miss two issues: image-text misalignment and uncertainty about which modality carries the hate signal.
- The paper proposes UCA to model both alignment and uncertainty in multimodal hate detection.

## Method
- Encodes image and text features, aligns cross-modal representations, then fuses them for multimodal classification.
- Adds cross-modal uncertainty learning to balance unimodal and fused features according to distributional divergence.
- Treats uncertainty as a control signal for deciding when cross-modal alignment should dominate.

## Data and Evaluation Setup
- Evaluates on five public multimodal datasets covering hate, harmful memes, offense, and sarcasm-style multimodal classification.
- Metrics include accuracy, F1, AUROC, precision, recall, and MMAE depending on dataset.
- Publication-checked priority values are tracked in [[hate-speech-metrics-matrix]].

## Results and Claims
- UCA is reported as competitive across multiple multimodal hate-related datasets.
- Publication-checked values include Hate Acc 76.10 and AUROC 84.32; Harm-C Acc/F1/MMAE 88.98/88.31/0.1015; Harm-P Acc/F1/MMAE 92.68/92.66/0.0739; Offense F1/Pre/Rec 65.89/66.09/66.90; Sarcasm F1/Pre/Rec/Acc 87.36/87.13/87.64/87.80.
- Use these values as dataset-specific evidence, not a cross-task leaderboard.

## Limitations and Follow-ups
- Dataset heterogeneity matters because hate, harm, offense, and sarcasm metrics are not directly comparable.
- Follow-up questions should test whether uncertainty estimates remain calibrated under new meme formats and target groups.
- Exact priority values are publication-checked in [[hate-speech-metrics-matrix]].

## Structured Signals
- Detected method keywords: contrastive-learning, causal, retrieval, prompting, multimodal, explainability
- Mentioned datasets: hateful memes, gab, twitter
- Mentioned metrics: f1, macro-f1, accuracy, precision, recall


## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
