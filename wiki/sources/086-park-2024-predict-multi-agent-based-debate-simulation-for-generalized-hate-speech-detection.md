---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, benchmark, retrieval, prompting, explainability]
sources: [raw/sources/Park 等 - 2024 - PREDICT Multi-Agent-based Debate Simulation for Generalized Hate Speech Detection.pdf]
---

# Park 等 - 2024 - PREDICT Multi-Agent-based Debate Simulation for Generalized Hate Speech Detection

## Metadata
- Source file: `raw/sources/Park 等 - 2024 - PREDICT Multi-Agent-based Debate Simulation for Generalized Hate Speech Detection.pdf`
- Year: 2024
- Pages: 25
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Addresses poor generalization caused by inconsistent labeling criteria across hate speech datasets.
- Frames different benchmark definitions as independent perspectives rather than noise to be merged away.
- Motivates consensus-building as an inference strategy for ambiguous hate speech decisions.

## Method
- Proposes PREDICT, a multi-agent debate simulation framework for generalized hate speech detection.
- Creates agents from induced labeling criteria or perspectives of public datasets.
- Uses perspective-based reasoning followed by debate to produce a final decision and justification.

## Data and Evaluation Setup
- Evaluates across public hate speech datasets with differing annotation criteria.
- Compares against data integration, augmentation, and explanation-based approaches.
- Tests whether modeling multiple perspectives improves generalization under label-definition shifts.

## Results and Claims
- Claims PREDICT improves hate speech detection by incorporating diverse dataset perspectives.
- Highlights consensus through debate as useful for handling conflicting labeling criteria.
- Exact dataset-level improvements should be checked in the original result tables before citation.

## Limitations and Follow-ups
- Agent perspectives inherit biases from the datasets used to induce them.
- Debate quality depends on the clarity and coverage of available labeling criteria.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: generalized hate detection, multi-agent debate, prompting, explainability
- Mentioned datasets: public hate speech benchmarks
- Mentioned metrics: accuracy, F1, cross-dataset performance

## Abstract (Extracted)
> PREDICT treats differences in hate-speech labeling criteria as independent perspectives. It creates agents from those perspectives and uses debate simulation to reach a consensus decision, aiming to improve generalized hate speech detection.

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
