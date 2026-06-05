---
created: 2026-06-01
updated: 2026-06-01
tags: [paper, deep-ingest-v2, hate-speech, explainability, llm-reasoning, benchmark, verification]
sources: [raw/sources/2026.eacl-long.198.pdf]
---

# Hu 和 Lee - 2026 - HateXScore A Metric Suite for Evaluating Reasoning Quality in Hate Speech Explanations

## Metadata
- Source file: `raw/sources/2026.eacl-long.198.pdf`
- Year: 2026
- Venue: EACL 2026 Long Papers
- Pages: 20
- Ingest level: deep-ingest-v2 (explanation-metric pass; first three pages checked)

## Problem Framing
- Standard classification metrics do not reveal why a moderation model reaches a hate-speech verdict.
- Existing explanation metrics often miss whether a model quotes the harmful span, whether removing it changes the prediction, and whether the explanation identifies the targeted protected group.

## Method
- Introduces HateXScore, a four-component diagnostic suite:
  - conclusion explicitness;
  - quotation faithfulness with causal masking;
  - policy-configurable target-group identification;
  - logical consistency among explanation elements.

## Data and Evaluation Setup
- Evaluates model explanations across six hate-speech datasets spanning English, Chinese, and Korean.
- Uses human evaluation and case studies to assess alignment with explanation-quality judgments.

## Results and Claims
- Reports that HateXScore exposes explanation failures and annotation inconsistencies hidden by accuracy and F1.
- Positions explanation-quality evaluation as a complement to label agreement rather than a replacement for classification metrics.

## Limitations and Follow-ups
- HateXScore evaluates explanations; it does not generate faithful evidence or solve relation classification.
- Exact metric comparisons require table verification before external citation.
- Follow-up use: adapt quotation faithfulness, target-group identification, and consistency checks to the local structured output schema.

## Related Concepts
- [[p0-target-grounding-reading-synthesis-2026-06-01]]
- [[explainable-hate-speech-detection]]
- [[llm-evaluation]]
- [[hate-speech-source-hub]]

