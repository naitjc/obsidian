---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, target-adaptive, bias, verification]
sources: [raw/sources/Zhang 等 - 2025 - MPVStance Mitigating Hallucinations in Stance Detection with Multi-Perspective Verification.pdf]
---

# Zhang 等 - 2025 - MPVStance Mitigating Hallucinations in Stance Detection with Multi-Perspective Verification

## Metadata
- Source file: `raw/sources/Zhang 等 - 2025 - MPVStance Mitigating Hallucinations in Stance Detection with Multi-Perspective Verification.pdf`
- Year: 2025
- Pages: 15
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- MPVStance: Mitigating Hallucinations in Stance Detection with
- Abstract a critical challenge in stance detection: the issue of
- Stance detection is a pivotal task in Natural Hallucination (Rawte et al., 2023) refers to the phe-
- is a Real Concern." The correct stance is "against"

## Method
- nomenon where the model generates content that,
- models generating plausible yet inaccurate con- Hallucination severely undermines the reliability
- troduce MPVStance, a framework that incor- accuracy and consistency. For instance, consider
- porates Multi-Perspective Verification (MPV) the tweet: "While climate change is something
- across a structured five-step verification pro-

## Data and Evaluation Setup
- troduce MPVStance, a framework that incor- accuracy and consistency. For instance, consider
- factual accuracy, logical consistency, contex-
- sive testing on the SemEval-2016 and VAST change in favor of other issues. However, a hallu-
- datasets, including scenarios that challenge cinating model might misinterpret the mention of
- in stance detection, particularly in zero-shot, detection to ensure reliable and accurate outcomes.

## Results and Claims
- troduce MPVStance, a framework that incor- accuracy and consistency. For instance, consider
- factual accuracy, logical consistency, contex-
- icantly outperforms current models. It effec-
- vanced the performance of stance detection, lever-
- accuracy and logical consistency, ensuring no as-

## Limitations and Follow-ups
- MPVStance: Mitigating Hallucinations in Stance Detection with
- Abstract a critical challenge in stance detection: the issue of
- hallucination(Hu et al., 2024; Gatto et al., 2023).
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, target-adaptive, bias, verification
- Mentioned datasets: SemEval, VAST, ARC
- Mentioned metrics: accuracy, f1, precision

## Benchmark Evidence Lines
- troduce MPVStance, a framework that incor- accuracy and consistency. For instance, consider
- factual accuracy, logical consistency, contex-
- sive testing on the SemEval-2016 and VAST change in favor of other issues. However, a hallu-
- icantly outperforms current models. It effec-
- new benchmarks for reliability and accuracy
- in stance detection, particularly in zero-shot, detection to ensure reliable and accurate outcomes.
- accuracy and logical consistency, ensuring no as-
- models. The zero-shot, few-shot, and challenging

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
