---
created: 2026-06-01
updated: 2026-06-01
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, explainability, information-extraction, weak-supervision]
sources: [raw/sources/2403.19836v2.pdf]
---

# Jafari 等 - 2024 - Target Span Detection for Implicit Harmful Content

## Metadata
- Source file: `raw/sources/2403.19836v2.pdf`
- Year: 2024
- Venue: ICTIR 2024
- Pages: 6
- Ingest level: deep-ingest-v2 (target-span pass; first three pages checked)

## Problem Framing
- Harmful content often targets protected groups through indirect references, metaphors, or stereotypes rather than explicit names.
- Existing IHC and SBIC target annotations identify groups but do not mark the text spans that realize explicit or implicit references.
- The paper formalizes implicit Target Span Identification (`iTSI`) as extracting non-overlapping target spans from harmful content.

## Method
- Introduces Implicit-Target-Span (`ITS`), merging target-span annotations over SBIC, DynaHate, and IHC.
- Uses a pooling-inspired annotation protocol: compare multiple LLM and prompt strategies against human annotations, then select the strongest strategy for broader annotation.
- Establishes transformer encoder baselines with BIO tagging.

## Data and Evaluation Setup
- Reports approximately 57,000 annotated samples with around 1.7 target spans per sample.
- Includes explicit target mentions and implicit references to the same target.
- Evaluates token-span detection against annotated start and end offsets.

## Results and Claims
- The dataset exposes a substantially larger target-span vocabulary than the original group-level annotations.
- The paper positions implicit target spans as a challenging information-extraction test bed.
- Exact model comparisons and numeric table values require table verification before external citation.

## Limitations and Follow-ups
- Target-span extraction alone does not label whether a candidate is attacked, quoted, neutrally mentioned, or part of counterspeech.
- The pooling protocol is useful for weak-label bootstrap design but still requires human audit.
- Follow-up use: upstream candidate-recall reference for [[p0-target-grounding-reading-synthesis-2026-06-01]].

## Related Concepts
- [[target-relation-grounding-literature-map]]
- [[privacy-filter-inspired-span-grounded-hate-detection]]
- [[missing-annotation-completion-and-utility-literature-map]]
- [[hate-speech-source-hub]]

