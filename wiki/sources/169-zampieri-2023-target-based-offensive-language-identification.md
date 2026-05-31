---
created: 2026-05-21
updated: 2026-05-21
tags: [paper, deep-ingest-v2, hate-speech, benchmark, explainability]
sources: [raw/sources/2023.acl-short.66.pdf]
---

# Zampieri 等 - 2023 - Target-Based Offensive Language Identification

## Metadata
- Source file: `raw/sources/2023.acl-short.66.pdf`
- Year: 2023
- Venue: ACL 2023 Short Papers
- Pages: 9
- Ingest level: deep-ingest-v2 (target-relation literature pass)

## Problem Framing
- Post-level offensive language datasets identify whether a post is offensive but do not localize the target of the offensive expression.
- Token-level toxic-span datasets identify toxic expressions but usually omit the target that those expressions act upon.
- The paper argues for bridging post-level and token-level annotation with target-based offensive language identification.

## Method
- Introduces TBO, a target-based offensive language identification taxonomy.
- Annotates both post-level harmfulness and token-level triples containing the target and offensive argument expression.
- Draws an analogy to aspect-based sentiment analysis: the relevant unit is not only an expression but the expression-target pair.

## Data and Evaluation Setup
- Dataset: more than 4,500 English Twitter posts.
- Annotation: post-level harmfulness plus token-level targets and offensive argument expressions.
- Evaluates multiple models trained and tested on the TBO annotations.

## Results and Claims
- Provides a unified taxonomy connecting harmfulness, offensive expression span, and target span.
- Treats target and argument expression as a structured unit, making it one of the closest sources to candidate target-relation grounding.
- Exact model scores and label distributions should be verified in the original tables before external citation.

## Limitations and Follow-ups
- TBO is offensive-language oriented, not limited to protected-class hate speech.
- It grounds target-expression pairs but does not directly solve definition-sensitive hate verdict derivation across toxic and non-toxic target-present cases.
- Follow-up role: primary evidence anchor for [[target-relation-grounding-literature-map]].

## Structured Signals
- Detected method keywords: target-based offensive language identification, TBO, target span, offensive argument expression, harmfulness, explainability
- Mentioned datasets: TBO, OLID, Toxic Spans Detection, HateXplain
- Mentioned metrics: post-level and token-level modeling performance

## Related Concepts
- [[target-relation-grounding-literature-map]]
- [[leakage-resistant-target-relation-modeling]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
- [[hate-speech-source-hub]]
