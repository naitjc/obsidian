---
created: 2026-05-12
updated: 2026-05-12
tags: [paper, deep-ingest-v2, hate-speech, cross-lingual, benchmark, explainability]
sources: [raw/sources/2025.coling-main.446.pdf]
---

# Salles 等 - 2025 - HateBRXplain A Benchmark Dataset with Human-Annotated Rationales for Explainable Hate Speech Detection in Brazilian Portuguese

## Metadata
- Source file: `raw/sources/2025.coling-main.446.pdf`
- Year: 2025
- Venue: COLING 2025
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Targets explainable hate speech detection for Brazilian Portuguese, where hate/offensive datasets exist but human rationale annotations are scarce.
- Frames lack of rationales as a practical blocker for trustworthy moderation systems because high-performing classifiers can still rely on biased or unfaithful cues.
- Connects Portuguese hate detection to the broader problem of group-identifier oversensitivity, where identity mentions are flagged without sufficient offensive context.

## Method
- Introduces HateBRXplain by adding human-annotated rationale spans to the existing HateBR Instagram-comment corpus.
- Evaluates mBERT, BERTimbau, DistilBERTimbau, and PTT5 for hate/offensive classification.
- Uses LIME and SHAP as post-hoc explanation methods and compares model-highlighted rationales against human-highlighted spans with plausibility and faithfulness metrics.

## Data and Evaluation Setup
- Dataset: 7,000 Brazilian Portuguese Instagram comments from HateBR, balanced between offensive and non-offensive comments.
- Rationale annotations are provided for 3,500 offensive comments.
- Evaluation covers classification accuracy/macro-F1 and explanation quality with IOU-F1, token precision/recall/F1, and faithfulness checks.

## Results and Claims
- BERTimbau achieves the strongest classification performance, with the paper reporting F1 around 0.91 and AUC around 0.97.
- LIME and SHAP can produce plausible rationales compared with human annotations, but high classification performance does not guarantee faithful explanations.
- The paper is most useful as a dataset and evaluation resource rather than as a new modeling architecture.

## Limitations and Follow-ups
- Exact classification and rationale scores should be checked against the paper tables before publication-grade citation.
- Rationale quality is assessed with post-hoc explanation methods, so explanation faithfulness remains a central uncertainty.
- Follow-up use: compare HateBRXplain with [[042-hare-explainable-hate-speech-detection-with-step-by-step-reasoning]] and [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] for rationale-vs-tag explanations.

## Structured Signals
- Detected method keywords: human rationales, explainability, post-hoc explanations, low-resource language, Portuguese hate speech
- Mentioned datasets: HateBR, HateBRXplain, HateXplain, ToLD-Br, OLID-BR
- Mentioned metrics: macro-F1, AUC, IOU-F1, token-F1, plausibility, faithfulness

## Related Concepts
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-research-map]]
