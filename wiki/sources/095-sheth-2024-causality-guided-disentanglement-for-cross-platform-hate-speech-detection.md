---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, cross-lingual, benchmark, contrastive-learning, causal, prompting, explainability]
sources: [raw/sources/Sheth 等 - 2024 - Causality Guided Disentanglement for Cross-Platform Hate Speech Detection.pdf]
---

# Sheth 等 - 2024 - Causality Guided Disentanglement for Cross-Platform Hate Speech Detection

## Metadata
- Source file: `raw/sources/Sheth 等 - 2024 - Causality Guided Disentanglement for Cross-Platform Hate Speech Detection.pdf`
- Year: 2024
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Addresses cross-platform hate-speech detection under distribution shift.
- Argues that models often rely on platform-specific terms or surface linguistic cues that do not generalize.
- Motivates causal representation learning to separate invariant hate cues from spurious platform cues.

## Method
- Introduces CATCH, a causality-guided disentanglement framework for cross-platform hate speech detection.
- Separates representations associated with aggression, sentiment, and platform-specific confounders.
- Uses causal objectives to improve transfer across social media platforms.

## Data and Evaluation Setup
- Evaluates cross-platform transfer across multiple English hate-speech datasets.
- Compares against deep learning and domain-generalization baselines.
- Reports macro-F1 style transfer results in table form.

## Results and Claims
- Claims CATCH improves cross-platform generalization by focusing on causal hate-related cues.
- Metrics matrix records visually verified table evidence for several cross-platform transfer cells.
- Avoid claiming universal superiority beyond the evaluated datasets and transfer settings.

## Limitations and Follow-ups
- The causal cue design may not capture all forms of hate or all platform shifts.
- Cross-platform datasets can differ in labeling policy as well as language distribution.
- Verify exact transfer scores and dataset pairings before external citation.

## Structured Signals
- Detected method keywords: causal representation learning, cross-platform transfer, disentanglement
- Mentioned datasets: Gab, Reddit, Twitter, YouTube style hate-speech datasets
- Mentioned metrics: macro-F1, cross-platform transfer score

## Abstract (Extracted)
> CATCH is a causality-guided disentanglement framework for cross-platform hate speech detection. It aims to learn representations that capture invariant hate cues while reducing reliance on platform-specific spurious correlations.

## Evidence Handling
- Removed noisy auto-extracted benchmark snippets from the page body.
- Treat cross-platform macro-F1 transfer rows as metrics-matrix evidence requiring table-level verification before external citation.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
