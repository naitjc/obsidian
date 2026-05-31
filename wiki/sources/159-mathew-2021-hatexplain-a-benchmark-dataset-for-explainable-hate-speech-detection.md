---
created: 2026-05-17
updated: 2026-05-17
tags: [paper, deep-ingest-v2, hate-speech, benchmark, explainability, bias]
sources: [raw/sources/17745-13-21239-1-2-20210518.pdf]
---

# Mathew 等 - 2021 - HateXplain A Benchmark Dataset for Explainable Hate Speech Detection

## Metadata
- Source file: `raw/sources/17745-13-21239-1-2-20210518.pdf`
- Year: 2021
- Venue: AAAI 2021
- Pages: 9
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Argues that hate speech models should be evaluated not only by classification accuracy but also by explanation quality and identity-term bias.
- Highlights two recurring risks: models may over-associate protected identity terms with toxicity, and high-performing classifiers may provide implausible or unfaithful explanations.
- Positions human rationales as a way to test whether model decisions align with annotator-highlighted evidence.

## Method
- Introduces HateXplain, a benchmark dataset where each post is annotated for class label, target community, and rationales.
- Labels use a three-way scheme: hate, offensive, or normal.
- Collects rationales as text spans that justify annotators' decisions, enabling plausibility and faithfulness evaluation.
- Evaluates neural and transformer baselines with and without rationale supervision.

## Data and Evaluation Setup
- Data sources include Twitter and Gab posts.
- The dataset contains roughly 20K posts, with posts annotated by multiple crowd workers.
- Evaluation covers macro F1 and AUROC for classification, AUC-based identity bias metrics, and rationale metrics such as IOU F1, token F1, AUPRC, comprehensiveness, and sufficiency.

## Results and Claims
- Models trained with human rationales improve classification-oriented metrics in some settings and reduce unintended identity-based bias.
- Strong classification performance does not guarantee high plausibility or faithfulness of explanations.
- The dataset's main durable contribution is a joint benchmark for labels, target communities, and human rationales.
- Exact model scores and community-wise bias values are table/figure-dependent and should be checked before external citation.

## Limitations and Follow-ups
- Rationales explain annotator decisions but do not automatically solve policy-definition ambiguity.
- Target communities are useful for bias analysis, but the page should not treat them as sufficient evidence that a post is hateful.
- Follow-up: connect HateXplain to PLEAD, HateBRXplain, target-span identification, and NER-enriched moderation pages as part of an explanation-focused hate detection line.

## Structured Signals
- Detected method keywords: human rationales, explainability, plausibility, faithfulness, identity bias
- Mentioned datasets: HateXplain, Twitter, Gab
- Mentioned metrics: macro F1, AUROC, subgroup AUC, BPSN AUC, BNSP AUC, GMB AUC, IOU F1, token F1, AUPRC, comprehensiveness, sufficiency

## Related Concepts
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
- [[implicit-hate-speech-detection]]
- [[hate-speech-source-hub]]
