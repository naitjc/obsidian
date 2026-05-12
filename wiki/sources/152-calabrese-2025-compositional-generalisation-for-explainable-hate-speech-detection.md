---
created: 2026-05-12
updated: 2026-05-12
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, synthetic-data, explainability]
sources: [raw/sources/2025.emnlp-main.703.pdf]
---

# Calabrese 等 - 2025 - Compositional Generalisation for Explainable Hate Speech Detection

## Metadata
- Source file: `raw/sources/2025.emnlp-main.703.pdf`
- Year: 2025
- Venue: EMNLP 2025
- Pages: 23
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Argues that sentence-level hate labels hide the internal structure of hate speech and lead models to learn dataset-specific correlations.
- Focuses on compositional generalization: whether a model can recognize known hateful expressions, targets, and slot labels in unseen combinations.
- Treats span/slot annotations as necessary but insufficient if models still bind slot meanings to biased target-expression co-occurrences.

## Method
- Builds on PLEAD's intent-classification and slot-filling formulation for explainable hate speech detection.
- Defines a hate speech grammar over slots such as target/protected characteristic, dehumanising comparison, threatening speech, negative opinion, hate entity, support of hate crimes, and negative stance.
- Creates U-PLEAD, a large synthetic dataset designed to balance expression-target and slot-context combinations.
- Introduces TARGET, a manually validated compositional generalization benchmark with approximately 8,000 posts across eight tests.

## Data and Evaluation Setup
- Uses PLEAD as the human-sourced base dataset.
- Generates roughly 364,000 synthetic U-PLEAD posts with controlled slot and expression combinations.
- Evaluates Gemma-2-9B and LLaMA-3.1-8B style models on intent classification and joint intent classification/slot filling.
- Reports Micro-F1 for intent classification plus production F1 and exact match for tree/slot structure.

## Results and Claims
- Training on a combination of U-PLEAD and real PLEAD improves compositional generalization on TARGET without sacrificing in-domain PLEAD performance.
- The most important claim is structural: balanced synthetic data helps disentangle slot meanings from surrounding context.
- Exact TARGET and PLEAD scores are table-dependent and should be checked before external citation.

## Limitations and Follow-ups
- Synthetic examples intentionally include implausible combinations, which is useful for decorrelation but may not represent natural platform distributions.
- The benchmark tests compositional robustness, not full real-world deployment behavior.
- High-value follow-up: connect U-PLEAD/TARGET to [[using-not-toxic-targets-for-hate-speech-detection]] as a principled way to generate target-aware hard negatives and target-expression swaps.

## Structured Signals
- Detected method keywords: compositional generalization, slot filling, intent classification, synthetic data, target-expression balancing
- Mentioned datasets: PLEAD, U-PLEAD, TARGET
- Mentioned metrics: Micro-F1, production F1, exact match accuracy

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[synthetic-data-generation]]
- [[hate-speech-research-map]]
