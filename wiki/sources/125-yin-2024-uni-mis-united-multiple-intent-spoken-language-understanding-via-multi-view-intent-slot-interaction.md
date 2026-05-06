---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Yin 等 - 2024 - Uni-MIS United Multiple Intent Spoken Language Understanding via Multi-View Intent-Slot Interaction.pdf]
---

# Yin 等 - 2024 - Uni-MIS United Multiple Intent Spoken Language Understanding via Multi-View Intent-Slot Interaction

## Metadata
- Source file: `raw/sources/Yin 等 - 2024 - Uni-MIS United Multiple Intent Spoken Language Understanding via Multi-View Intent-Slot Interaction.pdf`
- Year: 2024
- Pages: 9
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Uni-MIS: United Multiple Intent Spoken Language Understanding via Multi-View
- So far, multi-intent spoken language understanding (SLU) Chunk-level Atis_Flight_No ...... TP ...... Atis_Airfare
- slot interaction to model joint intent detection and slot fill- Figure 1: An example with multi-intent detection and
- action fusion to better capture the interaction information af- within a single utterance, and the Amazon internal dataset

## Method
- slot interaction to model joint intent detection and slot fill- Figure 1: An example with multi-intent detection and
- intent-guiding information during joint training. In this work,
- we present a novel architecture by modeling the multi-intent
- SLU as a multi-view intent-slot interaction. The architecture
- by effectively modeling the intent-slot relations with utter-

## Data and Evaluation Setup
- action fusion to better capture the interaction information af- within a single utterance, and the Amazon internal dataset
- tensive experiments on two widely used benchmark datasets and Atis Airfare) and a sequence labeling task to pre-
- strong baselines, pushing the state-of-the-art performance of
- tion point, achieving a promising performance. However, it evaluation metrics.
- is still possible to come across the problem of error propaga- • We construct a ChatGPT evaluation benchmark for

## Results and Claims
- strong baselines, pushing the state-of-the-art performance of
- request. This semantic frame is meticulously crafted through (AGIF) to achieve fine-grained multi-intent information in-
- tion point, achieving a promising performance. However, it evaluation metrics.
- filling and ignores rich anisotropic intent information during for improvement in performance, indicating significant
- intent information plays a significant role in guiding slot fill-

## Limitations and Follow-ups
- ing, which resulted in a failure to fully utilize anisotropic
- is still possible to come across the problem of error propaga- • We construct a ChatGPT evaluation benchmark for
- as bias parameters during training. where || denotes a concatenate operation, h′S denotes the
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: prompting, retrieval, llm-reasoning, dialogue, benchmark, graph
- Mentioned datasets: ATIS, SNIPS
- Mentioned metrics: accuracy, acc, f1

## Benchmark Evidence Lines
- action fusion to better capture the interaction information af- within a single utterance, and the Amazon internal dataset
- tensive experiments on two widely used benchmark datasets and Atis Airfare) and a sequence labeling task to pre-
- strong baselines, pushing the state-of-the-art performance of
- tion point, achieving a promising performance. However, it evaluation metrics.
- is still possible to come across the problem of error propaga- • We construct a ChatGPT evaluation benchmark for
- benchmark datasets, MixATIS and MixSNIPS, and con- Users often express multiple intentions within a fragment
- struct a ChatGPT evaluation benchmark for multi-intent within a sentence, not at the token-level or utterance-level.
- SLU. The results show that our model outperforms current To this end, we adopt a chunk-level approach (Huang et al.

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
