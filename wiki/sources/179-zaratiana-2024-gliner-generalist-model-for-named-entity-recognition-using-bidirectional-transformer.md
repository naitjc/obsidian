---
created: 2026-06-01
updated: 2026-06-01
tags: [paper, deep-ingest-v2, information-extraction, benchmark, zero-shot]
sources: [raw/sources/2024.naacl-long.300.pdf]
---

# Zaratiana 等 - 2024 - GLiNER Generalist Model for Named Entity Recognition using Bidirectional Transformer

## Metadata
- Source file: `raw/sources/2024.naacl-long.300.pdf`
- Year: 2024
- Venue: NAACL 2024 Long Papers
- Pages: 13
- Ingest level: deep-ingest-v2 (open-NER method pass; first three pages checked)

## Problem Framing
- Conventional NER systems are limited to predefined entity types.
- Instruction-following LLMs can extract arbitrary entity types but are comparatively expensive for large-scale use.

## Method
- Introduces GLiNER, a compact open-type NER model based on a bidirectional transformer encoder.
- Scores text spans against natural-language entity-type embeddings, enabling parallel extraction under user-specified labels.
- Positions GLiNER as a practical alternative to both fixed-label NER and sequential generative extraction.

## Data and Evaluation Setup
- Evaluates zero-shot entity extraction on multiple NER benchmarks.
- The inspected paper text reports comparisons against ChatGPT and fine-tuned LLM baselines.
- Exact benchmark values require table verification before external citation.

## Results and Claims
- Reports strong zero-shot NER performance while retaining compact encoder-style inference.
- Supports CPU-friendly and resource-constrained deployment scenarios.

## Limitations and Follow-ups
- GLiNER extracts spans but does not resolve target-evidence relations.
- Social groups, implicit references, and overlapping hate-speech roles need task-specific validation.
- Follow-up use: compact candidate-span baseline for [[privacy-filter-inspired-span-grounded-hate-detection]].

## Related Concepts
- [[intent-slot-style-hate-speech-modeling]]
- [[privacy-filter-inspired-span-grounded-hate-detection]]
- [[target-relation-grounding-literature-map]]

