---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, zero-shot, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Xing 等 - 2024 - DC-Instruct An Effective Framework for Generative Multi-intent Spoken Language Understanding.pdf]
---

# Xing 等 - 2024 - DC-Instruct An Effective Framework for Generative Multi-intent Spoken Language Understanding

## Metadata
- Source file: `raw/sources/Xing 等 - 2024 - DC-Instruct An Effective Framework for Generative Multi-intent Spoken Language Understanding.pdf`
- Year: 2024
- Pages: 15
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- understanding, recent advancements have lever- … ... francisco I-toloc.city_N
- dual-task dependencies and the oversight of located O than O from O
- task-specific semantic differences among ut- 1017 B-DT.time toronto B-fromloc.city_N
- work based on Dual-task Inter-dependent In- R: relative atis_cheapest atis_aircraft

## Method
- DC-Instruct: An Effective Framework for Generative Multi-intent Spoken
- aged the potential of prompt learning frame- where O boston B-fromloc.city_N 10 B-DT.time
- frameworks: the lack of explicit modeling of mitchell I-airport_N … flight O
- language models (LLMs) to generate labels Figure 1: Some samples from MixATIS dataset. Intent
- tween intents and slots, recent models widely adopt

## Data and Evaluation Setup
- language models (LLMs) to generate labels Figure 1: Some samples from MixATIS dataset. Intent
- ing abilities. Extensive experiments on pub- gadharaiah and Narayanaswamy, 2019; Goo et al.,
- lic benchmark datasets show that DC-Instruct 2018; Liu et al., 2019; Qin et al., 2020, 2021; Xing
- Intent 4 beds, we conduct extensive experiments based on
- experimental results show that our models can

## Results and Claims
- same or similar labels. This can improve LLMs
- els and state-of-the-art methods, demonstrat-
- SLU (Kim et al., 2017) has garnered significant at-
- I : Same Intent Labels achieve consistent and significant improvements
- Determination Intent 7 over state-of-the-art models. The ablation study

## Limitations and Follow-ups
- To resolve the above challenges, in this work, while there are usually multi-intent utterances in
- To address the challenge of exploiting utterance propose to leverage the dual-task correlations in the
- Figure 3: Illustration of our framework. Due to space limitation, we omit the details of I -I . We show some
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, benchmark, graph
- Mentioned datasets: ATIS, SNIPS, TOP
- Mentioned metrics: accuracy, acc, f1

## Benchmark Evidence Lines
- language models (LLMs) to generate labels Figure 1: Some samples from MixATIS dataset. Intent
- lic benchmark datasets show that DC-Instruct 2018; Liu et al., 2019; Qin et al., 2020, 2021; Xing
- markedly outperforms current generative mod-
- els and state-of-the-art methods, demonstrat-
- Taking the public benchmark datasets as test
- Determination Intent 7 over state-of-the-art models. The ablation study
- examples of detailed instructions in Appendix (Table 5 and Table 6).
- Overall(Acc) Slot (F1) Intent(Acc) Overall(Acc) Slot(F1) Intent(Acc)

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
