---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, cross-lingual, benchmark, retrieval, explainability]
sources: [raw/sources/Sariyanto 等 - 2025 - Towards Explainable Hate Speech Detection.pdf]
---

# Sariyanto 等 - 2025 - Towards Explainable Hate Speech Detection

## Metadata
- Source file: `raw/sources/Sariyanto 等 - 2025 - Towards Explainable Hate Speech Detection.pdf`
- Year: 2025
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Questions whether high-cost deep learning is always necessary for hate speech detection.
- Frames simpler lexicon-based methods as a path toward cost-efficient and explainable NLP.
- Uses hate speech detection as the task for comparing simple affective features with neural methods.

## Method
- Introduces a learning-free algorithm based on weighted sums of valence, arousal, and dominance values.
- Uses VAD lexicon features to classify text as hate speech or non-hate speech.
- Analyzes weight and classification strategies to balance simplicity and performance.

## Data and Evaluation Setup
- Compares the VAD-based method with neural-network and large-language-model baselines.
- Uses hate speech datasets with disagreement-aware or benchmark-style labels.
- Discusses related lexicon, sentiment, and hate speech resources.

## Results and Claims
- Claims the simple VAD method can compete with neural-network-based methods in the evaluated setting.
- Positions the approach as more interpretable and resource-efficient than heavier models.
- Exact comparisons should be checked against the original tables before citation.

## Limitations and Follow-ups
- Lexicon-based affect features may miss context, target identity, sarcasm, and implicit hate.
- Performance may depend strongly on language, dataset construction, and annotation disagreement.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: explainability, lexicon method, hate speech classification, lightweight NLP
- Mentioned datasets: hate speech datasets, NRC-VAD Lexicon
- Mentioned metrics: accuracy, F1, classification performance

## Abstract (Extracted)
> The paper studies whether a simple, explainable VAD lexicon method can compete with neural approaches for hate speech detection. It uses weighted valence, arousal, and dominance values to classify text while reducing computational cost.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
