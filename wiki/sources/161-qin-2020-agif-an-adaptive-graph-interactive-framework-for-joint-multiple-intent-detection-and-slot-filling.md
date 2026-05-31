---
created: 2026-05-17
updated: 2026-05-17
tags: [paper, deep-ingest-v2, dialogue, benchmark, graph]
sources: [raw/sources/2020.findings-emnlp.163.pdf]
---

# Qin 等 - 2020 - AGIF An Adaptive Graph-Interactive Framework for Joint Multiple Intent Detection and Slot Filling

## Metadata
- Source file: `raw/sources/2020.findings-emnlp.163.pdf`
- Year: 2020
- Venue: Findings of EMNLP 2020
- Pages: 10
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Real user utterances can express multiple intents, while many SLU models assume a single intent.
- Simply passing a global multi-intent context vector to all tokens gives every slot token the same intent information, which can blur token-specific intent-slot relations.
- The paper asks how to incorporate fine-grained multiple-intent information into token-level slot prediction.

## Method
- Proposes AGIF, an Adaptive Graph-Interactive Framework for joint multiple intent detection and slot filling.
- Introduces an intent-slot graph interaction layer that adaptively extracts relevant intent information for each token.
- Uses graph neural interaction to connect predicted intents and token-level slot representations.
- Releases code and constructs multi-intent benchmark variants.

## Data and Evaluation Setup
- Multi-intent datasets: DSTC4, MixATIS, and MixSNIPS.
- Single-intent datasets: ATIS and SNIPS.
- Metrics include slot F1, intent macro F1, intent accuracy, and sentence-level overall accuracy.

## Results and Claims
- Reports substantial gains over the Joint Multiple ID-SF baseline on multi-intent datasets.
- Claims new state-of-the-art performance on both multi-intent and single-intent benchmarks at publication time.
- Ablations indicate that adaptive graph interaction is responsible for much of the improvement over simpler attention or graph variants.
- Exact benchmark numbers are table-dependent and should be checked in Tables 1-4 before external citation.

## Limitations and Follow-ups
- AGIF's token-level graph interaction is computationally heavier than later sentence-level DGM-style graph interaction.
- The model assumes a fixed supervised intent and slot schema; open-ended policy or moderation rules would need schema design.
- Follow-up: use as the primary predecessor when explaining DGM and Co-guiding Net in the dialogue direction.

## Structured Signals
- Detected method keywords: adaptive graph interaction, multi-intent SLU, intent-slot graph, slot filling
- Mentioned datasets: DSTC4, MixATIS, MixSNIPS, ATIS, SNIPS
- Mentioned metrics: slot F1, intent F1, intent accuracy, overall accuracy

## Related Concepts
- [[dialogue-systems]]
- [[intent-slot-style-hate-speech-modeling]]
- [[dialogue-systems-source-hub]]
