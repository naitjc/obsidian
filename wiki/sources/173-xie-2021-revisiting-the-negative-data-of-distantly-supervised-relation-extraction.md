---
created: 2026-05-27
updated: 2026-05-27
tags: [paper, deep-ingest-v2, information-extraction, weak-supervision, benchmark]
sources: [raw/sources/2021.acl-long.277.pdf]
---

# Xie 等 - 2021 - Revisiting the Negative Data of Distantly Supervised Relation Extraction

## Metadata
- Source file: `raw/sources/2021.acl-long.277.pdf`
- Year: 2021
- Venue: ACL-IJCNLP 2021
- Pages: 10
- Ingest level: deep-ingest-v2 (missing-annotation literature pass; first page visually checked)

## Problem Framing
- Distant supervision produces false-positive relation labels when a knowledge-base relation is not expressed by a sentence.
- It also produces false negatives when a sentence expresses a relation missing from the knowledge base, causing the sentence to be labeled `NA`.
- The paper notes that the high volume of apparent negative labels can suppress useful positive evidence.

## Method
- Formulates distantly supervised relation extraction as a positive-unlabeled learning problem to reduce missing-relation false negatives.
- Proposes ReRe, a pipeline that first classifies sentences by relation labels and then extracts subject/object arguments.
- Adds cleaner annotated test sets to reduce the impact of prior evaluation noise.

## Data and Evaluation Setup
- Uses distantly supervised relation extraction benchmarks and introduces NYT21 and SKE21 evaluation sets.
- NYT21 and SKE21 contain 370 and 1,150 manually checked samples as reported in the paper text.
- Evaluates relation extraction under both false-negative and false-positive label noise.

## Results and Claims
- Reports consistent improvements over compared approaches and resilience when trained with substantial false-positive data.
- For the current wiki, the useful claim is not a direct hate result: missing candidate-target relation labels can be treated as unlabeled rather than definitively neutral.
- Exact model results remain table-dependent and are not elevated to publication-checked claims here.

## Limitations and Follow-ups
- Knowledge-base distant supervision differs from annotation-policy missingness in IHC/SBIC.
- A positive-unlabeled relation formulation needs relation-specific audit and untouched test sets before it can be adopted for hate detection.
- Follow-up use: method analogue for [[leakage-resistant-target-relation-modeling]].

## Structured Signals
- Detected method keywords: distant supervision, positive-unlabeled learning, relation extraction, false negatives, ReRe
- Mentioned datasets: NYT21, SKE21
- Mentioned metrics: relation extraction performance

## Related Concepts
- [[missing-annotation-completion-and-utility-literature-map]]
- [[target-relation-grounding-literature-map]]
- [[leakage-resistant-target-relation-modeling]]
