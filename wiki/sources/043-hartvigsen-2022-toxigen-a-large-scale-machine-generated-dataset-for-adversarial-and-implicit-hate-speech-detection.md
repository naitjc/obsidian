---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, prompting, explainability]
sources: [raw/sources/Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection.pdf]
---

# Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection

## Metadata
- Source file: `raw/sources/Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection.pdf`
- Year: 2022
- Pages: 18
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Targets failures of toxicity detectors that over-rely on minority-group mentions.
- Highlights two linked problems: benign minority mentions can be falsely flagged, while implicit toxic statements can be missed.
- Frames adversarial and implicit toxicity as a dataset and evaluation challenge.

## Method
- Creates TOXIGEN, a large machine-generated dataset of toxic and benign statements about minority groups.
- Uses demonstration-based prompting and adversarial classifier-in-the-loop decoding to generate challenging examples.
- Includes human annotation and analysis to separate benign identity mentions from toxic content.

## Data and Evaluation Setup
- The dataset contains 274,186 generated statements about 13 minority groups.
- Evaluates multiple toxicity / hate classifiers on subtle toxic and benign identity-related statements.
- Compares TOXIGEN with existing implicit hate and toxicity resources.

## Results and Claims
- Shows that widely used toxicity systems can both over-flag benign minority mentions and under-detect implicit toxicity.
- Presents TOXIGEN as an adversarial benchmark for more robust toxicity and hate-speech detection.
- Records dataset-level statistics in the metrics matrix for internal use.

## Limitations and Follow-ups
- Machine-generated data can reflect prompting choices and model biases.
- Human validation is essential before treating generated examples as ground truth.
- Verify exact dataset statistics and classifier results before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: implicit hate, adversarial data generation, benchmark, prompting
- Mentioned datasets: ToxiGen, ImplicitHateCorpus
- Mentioned metrics: dataset size, toxicity score, hate score

## Abstract (Extracted)
> TOXIGEN is a large machine-generated dataset designed to expose toxicity detectors that rely on spurious identity correlations. It contains toxic and benign statements about minority groups and supports adversarial evaluation of implicit toxicity detection.

## Evidence Handling
- Removed noisy auto-extracted benchmark snippets from the page body.
- Treat dataset statistics and classifier results as metrics-matrix evidence requiring table-level verification before external citation.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
