---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, contrastive-learning, causal, retrieval, prompting, explainability]
sources: [raw/sources/Kim 等 - 2024 - Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate S.pdf]
---

# Kim 等 - 2024 - Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate S

## Metadata
- Source file: `raw/sources/Kim 等 - 2024 - Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate S.pdf`
- Year: 2024
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Targets implicit hate speech, where semantically similar non-hate examples can be hard negatives.
- Observes that earlier contrastive learning methods do not consistently outperform cross-entropy training.
- Motivates label-aware negative sampling to learn sharper class boundaries.

## Method
- Proposes LAHN, label-aware hard negative sampling with momentum contrastive learning.
- Selects negative samples from the opposite class rather than random negatives.
- Uses semantic similarity to emphasize hard negatives that are close to hate anchors.

## Data and Evaluation Setup
- Evaluates on implicit hate-speech datasets against cross-entropy and contrastive-learning baselines.
- Compares random negative selection with label-aware hard negative strategies.
- Studies representation quality and classification performance.

## Results and Claims
- Claims label-aware hard negatives improve implicit hate-speech detection over prior contrastive setups.
- Shows that carefully selected negatives can better separate hate and non-hate representations.
- Exact improvements should be checked in the original result tables before citation.

## Limitations and Follow-ups
- Hard-negative mining depends on label quality and representation similarity.
- Implicit hate boundaries can remain ambiguous when non-hate examples discuss identity groups.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: implicit hate, contrastive learning, hard negative sampling, momentum contrast
- Mentioned datasets: implicit hate speech datasets
- Mentioned metrics: accuracy, F1, representation quality

## Abstract (Extracted)
> The paper proposes LAHN, a label-aware hard negative sampling strategy for momentum contrastive learning in implicit hate-speech detection. It selects semantically close opposite-class negatives to improve representation separation.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
