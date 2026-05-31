---
created: 2026-05-27
updated: 2026-05-27
tags: [paper, deep-ingest-v2, information-extraction, weak-supervision, cross-lingual, benchmark]
sources: [raw/sources/K19-1060.pdf]
---

# Mayhew 等 - 2019 - Named Entity Recognition with Partially Annotated Training Data

## Metadata
- Source file: `raw/sources/K19-1060.pdf`
- Year: 2019
- Venue: CoNLL 2019
- Pages: 11
- Ingest level: deep-ingest-v2 (missing-annotation literature pass; first page visually checked)

## Problem Framing
- In low-resource and cross-language settings, available NER data can identify some valid entities while leaving other true entities unlabeled.
- Treating every untagged token as non-entity introduces false negatives and makes partial data noisy.
- The relevant challenge is estimating which unlabeled instances are reliable negatives.

## Method
- Introduces Constrained Binary Learning (CBL), an iterative algorithm that detects likely false negatives and downweights them.
- Produces a weighted training set for neural or non-neural NER models.
- Uses constraints and background knowledge to guide the iterative true-negative selection.

## Data and Evaluation Setup
- Evaluates partial annotation learning across eight languages and multiple script families.
- Includes a real-world romanized Bengali corpus annotated by non-speakers.
- Reports weighted-model performance in terms of NER F1.

## Results and Claims
- Finds strong ability to learn from partial data across languages.
- In the Bengali case, non-speaker partial annotation with CBL exceeds the cited prior state of the art by more than five F1 points.
- The durable local lesson is to represent weakly completed target spans with provenance or weights rather than converting them directly to gold training labels.

## Limitations and Follow-ups
- NER spans are not sufficient to identify whether a candidate target is attacked or merely mentioned.
- Results do not validate any particular LLM-completed IHC/SBIC target field.
- Follow-up use: informs weak-label weighting and manual-audit design for [[ihc-sbic-target-completion-layer]].

## Structured Signals
- Detected method keywords: partial annotation, constrained binary learning, false-negative weighting, NER, cross-lingual supervision
- Mentioned datasets: multilingual NER data, romanized Bengali NER corpus
- Mentioned metrics: F1

## Related Concepts
- [[missing-annotation-completion-and-utility-literature-map]]
- [[ihc-sbic-target-completion-layer]]
- [[target-relation-grounding-literature-map]]
