---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, few-shot, prompting, retrieval, benchmark, graph, causal]
sources: [raw/sources/Yin 等 - MIDLM Multi-Intent Detection with Bidirectional Large Language Models.pdf]
---

# Yin 等 - MIDLM Multi-Intent Detection with Bidirectional Large Language Models

## Metadata
- Source file: `raw/sources/Yin 等 - MIDLM Multi-Intent Detection with Bidirectional Large Language Models.pdf`
- Year: unknown
- Pages: 10
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- MIDLM: Multi-Intent Detection with Bidirectional Large
- Decoder-only Large Language Models on the MixATIS and MixSNIPS datasets (Qin
- SNIPS (Coucke et al., 2018) datasets to incorpo-
- sensitive language understanding tasks rate multiple intents. However, these datasets pri-

## Method
- Decoder-only Large Language Models on the MixATIS and MixSNIPS datasets (Qin
- of their autoregressive architecture, which junctions: “and,” “and then,” “and also,” and “,”
- framework allows autoregressive LLMs to to offer greater diversity in coordinating conjunc-
- through post-training, eliminating the need for existing multi-intent resources, referred to as the
- training the models from scratch. Comprehen- MixX series, but provide more varied connec-

## Data and Evaluation Setup
- Decoder-only Large Language Models on the MixATIS and MixSNIPS datasets (Qin
- SNIPS (Coucke et al., 2018) datasets to incorpo-
- sensitive language understanding tasks rate multiple intents. However, these datasets pri-
- evaluations conducted using these datasets. To ad-
- introduced BlendX, a series of datasets designed

## Results and Claims
- demonstrating its superior performance in the
- have made significant strides in language gener-
- els from scratch. Our model outperforms strong
- experiments revealed varying model performance
- lines, achieving superior performance in the MID

## Limitations and Follow-ups
- remains challenging due to the limitations marily use only four types of coordinating con-
- dress the limitation, Yoon et al. (2024) recently
- fundamental challenge. Traditionally, it has been
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, benchmark, graph, causal
- Mentioned datasets: ATIS, SNIPS, MASSIVE, TOP
- Mentioned metrics: accuracy, acc, mae

## Benchmark Evidence Lines
- Decoder-only Large Language Models on the MixATIS and MixSNIPS datasets (Qin
- SNIPS (Coucke et al., 2018) datasets to incorpo-
- sensitive language understanding tasks rate multiple intents. However, these datasets pri-
- evaluations conducted using these datasets. To ad-
- introduced BlendX, a series of datasets designed
- leverage bidirectional information awareness tions and soft links. These datasets build upon
- sive evaluations across 8 datasets show that
- MIDLM consistently outperforms both exist-

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
