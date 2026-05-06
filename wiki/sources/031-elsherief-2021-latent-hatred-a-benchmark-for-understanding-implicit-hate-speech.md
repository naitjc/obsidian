---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, cross-lingual, benchmark, causal, explainability]
sources: [raw/sources/ElSherief 等 - 2021 - Latent Hatred A Benchmark for Understanding Implicit Hate Speech.pdf]
---

# ElSherief 等 - 2021 - Latent Hatred A Benchmark for Understanding Implicit Hate Speech

## Metadata
- Source file: `raw/sources/ElSherief 等 - 2021 - Latent Hatred A Benchmark for Understanding Implicit Hate Speech.pdf`
- Year: 2021
- Pages: 19
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Addresses implicit hate speech, which is coded, indirect, and less keyword-driven than explicit hate.
- Argues that prior hate-speech work focused too heavily on overt discriminatory language.
- Motivates a theoretically grounded taxonomy and benchmark for fine-grained implicit hate analysis.

## Method
- Introduces a taxonomy of implicit hate speech grounded in social-science literature.
- Builds a Twitter benchmark corpus with fine-grained labels for each message and its implied meaning.
- Uses baseline models to study both detection and explanation of implicit hate speech.

## Data and Evaluation Setup
- Annotates implicit hate messages across prevalent hate-target groups in the United States.
- Provides natural-language implication annotations in addition to category labels.
- Evaluates contemporary classifiers and generation-style explanations on the benchmark.

## Results and Claims
- Shows that implicit hate remains challenging even when high-level hate classification appears effective.
- Identifies features that make implicit hate difficult for existing models, including coded language and pragmatic implication.
- Records table-verified benchmark values separately in the metrics matrix.

## Limitations and Follow-ups
- The dataset focuses on U.S.-oriented social-media hate targets and may not transfer directly across cultural settings.
- Implicit hate labels and implications involve pragmatic judgment, so annotation framing matters.
- Verify exact metric values and label distributions before external citation.

## Structured Signals
- Detected method keywords: implicit hate, taxonomy, benchmark, explanation
- Mentioned datasets: Latent Hatred / implicit hate corpus, Twitter
- Mentioned metrics: precision, recall, F1, accuracy

## Abstract (Extracted)
> Latent Hatred introduces a theoretically grounded taxonomy and benchmark corpus for implicit hate speech. It provides fine-grained labels and implication annotations, then evaluates baseline systems for detecting and explaining implicit hate.

## Evidence Handling
- Removed noisy auto-extracted benchmark snippets from the page body.
- Treat quantitative benchmark values as metrics-matrix evidence requiring table-level verification before external citation.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
