---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, contrastive-learning, causal, prompting, explainability]
sources: [raw/sources/Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det.pdf]
---

# Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det

## Metadata
- Source file: `raw/sources/Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det.pdf`
- Year: 2025
- Pages: 10
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Addresses poor generalization in implicit hate speech detection caused by spurious correlations learned by ERM models.
- Focuses on subtle and ambiguous hate speech where surface cues are unreliable.
- Frames model failures as useful evidence for identifying hard positive examples.

## Method
- Proposes causality-guided contrastive learning (CCL) for implicit hate speech detection.
- Uses ERM inference failures to identify samples with the same class but opposite spurious attributes.
- Aligns hard positives in representation space to reduce reliance on spurious correlations.

## Data and Evaluation Setup
- Evaluates CCL in cross-dataset implicit hate speech settings.
- Tests CCL within multiple contrastive-learning methods and compares against existing baselines.
- Uses benchmark implicit hate datasets for generalization evaluation.

## Results and Claims
- Claims state-of-the-art performance on three implicit hate speech benchmark datasets.
- Reports that using ERM failures as hard positives improves cross-dataset robustness.
- Treat exact gains as table-level evidence requiring PDF verification before external citation.

## Limitations and Follow-ups
- The method depends on ERM failure patterns being good proxies for spurious attributes.
- Cross-dataset success may vary when label definitions or target groups shift substantially.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: implicit hate, contrastive learning, causality, generalization
- Mentioned datasets: implicit hate speech benchmarks
- Mentioned metrics: macro-F1, cross-dataset performance

## Abstract (Extracted)
> The paper proposes CCL, a causality-guided contrastive learning method for implicit hate speech detection. It uses ERM model failures to identify hard positives and reduce reliance on spurious correlations, improving cross-dataset generalization.

## Evidence Handling
- Removed noisy auto-extracted benchmark snippets from the page body.
- Treat cross-dataset macro-F1 gains as metrics-matrix evidence requiring table-level verification before external citation.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
