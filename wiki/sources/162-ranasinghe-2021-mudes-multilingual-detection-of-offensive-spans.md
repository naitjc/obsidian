---
created: 2026-05-17
updated: 2026-05-17
tags: [paper, deep-ingest-v2, hate-speech, cross-lingual, benchmark, explainability]
sources: [raw/sources/2021.naacl-demos.17.pdf]
---

# Ranasinghe和Zampieri - 2021 - MUDES Multilingual Detection of Offensive Spans

## Metadata
- Source file: `raw/sources/2021.naacl-demos.17.pdf`
- Year: 2021
- Venue: NAACL 2021 Demonstrations
- Pages: 9
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Offensive language systems often classify whole posts, but moderators and analysts need to know which spans make a post offensive.
- Span detection can support interpretability and semi-automated moderation.
- The paper focuses on making offensive-span detection usable through pretrained models, an API, and a web interface.

## Method
- Presents MUDES, a multilingual framework for offensive span detection.
- Releases English base/large models and multilingual base/large models.
- Uses transformer-based token/span prediction and exposes model inference through a Python API and web UI.
- Extends span detection beyond English through multilingual transformer models.

## Data and Evaluation Setup
- Main training data: SemEval-2021 Task 5 Toxic Spans Detection data from Civil Comments.
- Off-domain English evaluation: OLID from OffensEval 2019.
- Multilingual evaluation: Danish and Greek OffensEval 2020 datasets.
- Metrics include toxic-span F1 and macro F1 for derived instance-level evaluations.

## Results and Claims
- Reports that MUDES improves over the SemEval toxic-span baseline on the trial set.
- Shows that multilingual models can identify offensive spans in Danish and Greek settings despite domain/language shift.
- The practical contribution is a deployable span-detection system rather than a new moderation taxonomy.
- Exact F1 values are table-dependent and should be checked in Tables 2-3 before external citation.

## Limitations and Follow-ups
- The system detects offensive spans, not necessarily hate-speech target relations or policy-rule violations.
- Instance-level labels in off-domain/multilingual evaluation require conversion because those datasets do not provide gold offensive spans.
- Follow-up: connect to HateXplain, HateBRXplain, STATE ToxiCN, and implicit hate target-span identification as span-level evidence resources.

## Structured Signals
- Detected method keywords: offensive spans, multilingual offensive language detection, transformer models, API, web UI
- Mentioned datasets: SemEval-2021 Toxic Spans Detection, Civil Comments, OLID, Danish OffensEval 2020, Greek OffensEval 2020
- Mentioned metrics: span F1, macro F1

## Related Concepts
- [[explainable-hate-speech-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-datasets-and-benchmarks]]
- [[hate-speech-source-hub]]
