---
created: 2026-05-21
updated: 2026-05-21
tags: [paper, deep-ingest-v2, hate-speech, conversational, benchmark, explainability]
sources: [raw/sources/2022.naacl-main.433.pdf]
---

# Yu 等 - 2022 - Hate Speech and Counter Speech Detection Conversational Context Does Matter

## Metadata
- Source file: `raw/sources/2022.naacl-main.433.pdf`
- Year: 2022
- Venue: NAACL-HLT 2022
- Pages: 13
- Ingest level: deep-ingest-v2 (target-relation literature pass)

## Problem Framing
- Hate and counter-speech judgments often change when the preceding conversational context is shown.
- The paper defines context as the parent comment in a Reddit thread and studies whether the target comment is hate, counter-hate, or neutral.
- This supports treating quotation, reply, counterspeech, and conversation state as context modifiers rather than surface text features.

## Method
- Builds a context-aware Reddit dataset of parent-target comment pairs.
- Annotates the target comment twice: once in isolation and once with the parent context.
- Compares context-unaware and context-aware neural classifiers.

## Data and Evaluation Setup
- Dataset: 6,846 pairs of parent and target Reddit comments.
- Labels: hate speech, counter speech, and neutral.
- Evaluates changes in human labels and model performance when context is included.

## Results and Claims
- Human judgments change for many comments when context is provided.
- Context-aware models significantly outperform context-unaware models.
- Qualitative examples show that a target comment can switch between neutral, hate, and counter-hate depending on the parent comment.

## Limitations and Follow-ups
- Context is limited to the parent comment rather than full conversational history.
- The paper does not provide target-relation labels, but it strongly motivates a `context modifier` layer in relation-grounded hate detection.
- Follow-up role: supports context-sensitive relation states in [[leakage-resistant-target-relation-modeling]].

## Structured Signals
- Detected method keywords: conversational context, counter speech, Reddit, context-aware classification, annotation shift
- Mentioned datasets: context-aware Reddit hate/counter-hate dataset
- Mentioned metrics: classification performance, human label changes

## Related Concepts
- [[target-relation-grounding-literature-map]]
- [[leakage-resistant-target-relation-modeling]]
- [[hate-speech-datasets-and-benchmarks]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-source-hub]]
