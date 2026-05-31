---
created: 2026-05-27
updated: 2026-05-27
tags: [paper, deep-ingest-v2, information-extraction, weak-supervision, benchmark]
sources: [raw/sources/N19-1079.pdf]
---

# Jie 等 - 2019 - Better Modeling of Incomplete Annotations for Named Entity Recognition

## Metadata
- Source file: `raw/sources/N19-1079.pdf`
- Year: 2019
- Venue: NAACL-HLT 2019
- Pages: 6
- Ingest level: deep-ingest-v2 (missing-annotation literature pass; first page visually checked)

## Problem Framing
- Standard NER assumes fully annotated entities, but practical annotation can omit valid spans.
- A missing label is not the same as a confirmed `O` label: incorrectly forcing omitted entities to negative labels creates false negative supervision.
- The paper emphasizes that realistic partial annotation operates at complete spans, not arbitrary token deletion.

## Method
- Defines a learning setup for incomplete named-entity labels without assuming that unlabeled tokens are verified non-entities.
- Proposes an easy-to-implement model that accounts for compatible label sequences under incomplete span annotations.
- Evaluates the approach against baselines relying on less realistic partial-label assumptions.

## Data and Evaluation Setup
- Benchmarks include CoNLL-2003 English and CoNLL-2002 Spanish.
- Includes industrial Chinese datasets Taobao and Youku.
- Evaluates NER precision, recall, and F-score under varying levels of incomplete annotation.

## Results and Claims
- Reports significant improvements over previous incomplete-annotation approaches across the evaluated datasets.
- The critical local implication is that an absent target-span annotation cannot be used directly as `no_relevant_target` supervision unless the annotation policy guarantees exhaustive marking.
- It is a transfer-method source, not direct evidence about IHC or SBIC annotation quality.

## Limitations and Follow-ups
- The task identifies entities rather than target-attacked relations; relation-state completion remains a separate problem.
- Exact F-score gains require table verification before external citation.
- Follow-up use: informs candidate-target span handling and audit design in [[missing-annotation-completion-and-utility-literature-map]].

## Structured Signals
- Detected method keywords: incomplete annotations, named entity recognition, partial spans, compatible sequences, false negatives
- Mentioned datasets: CoNLL-2003, CoNLL-2002, Taobao, Youku
- Mentioned metrics: precision, recall, F-score

## Related Concepts
- [[missing-annotation-completion-and-utility-literature-map]]
- [[intent-slot-style-hate-speech-modeling]]
- [[target-relation-grounding-literature-map]]
