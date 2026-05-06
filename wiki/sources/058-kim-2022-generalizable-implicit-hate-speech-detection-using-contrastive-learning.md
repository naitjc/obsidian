---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, contrastive-learning, retrieval, prompting, explainability]
sources: [raw/sources/Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning.pdf]
---

# Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning

## Metadata
- Source file: `raw/sources/Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning.pdf`
- Year: 2022
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Implicit hate is difficult because harmful meaning can depend on context and implication rather than explicit slurs.
- Models fine-tuned on one implicit hate dataset can degrade substantially when evaluated on another dataset.
- The paper focuses on cross-dataset generalization, not cross-lingual transfer.

## Method
- Proposes ImpCon, a contrastive learning method for implicit hate detection.
- Uses implication-aware positive pairs so a post and its underlying implication are pulled closer in representation space.
- Evaluates ImpCon with BERT and HateBERT backbones.

## Data and Evaluation Setup
- Uses three implicit hate benchmarks: IHC, SBIC, and DynaHate.
- Runs cross-dataset evaluation to test whether training on one dataset transfers to another.
- Publication-checked cross-dataset values are tracked in [[hate-speech-metrics-matrix]].

## Results and Claims
- The paper reports that cross-dataset F1 drops by at least 12.5 percentage points when models are evaluated outside the training dataset.
- ImpCon improves cross-dataset transfer for BERT and HateBERT; the paper reports maximum improvements of 9.10% for BERT and 8.71% for HateBERT.
- Publication-checked examples include IHC-to-SBIC, IHC-to-DynaHate, and SBIC-to-IHC/DynaHate rows.

## Limitations and Follow-ups
- The evidence is limited to three English implicit hate datasets and should not be generalized to cross-lingual transfer.
- Because contrastive pairs encode assumptions about shared implications, future checks should inspect whether implication labels or generated implications introduce bias.
- Exact priority values are publication-checked in [[hate-speech-metrics-matrix]].

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, prompting, explainability
- Mentioned datasets: IHC, SBIC, DynaHate
- Mentioned metrics: f1

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
