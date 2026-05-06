---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Wu 等 - Incorporating Instructional Prompts into a Unified Generative Framework for Joint Multiple Intent De.pdf]
---

# Wu 等 - Incorporating Instructional Prompts into a Unified Generative Framework for Joint Multiple Intent De

## Metadata
- Source file: `raw/sources/Wu 等 - Incorporating Instructional Prompts into a Unified Generative Framework for Joint Multiple Intent De.pdf`
- Year: unknown
- Pages: 6
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- for Joint Multiple Intent Detection and Slot Filling
- Slot Filling (SF) is a significant challenge in
- NIPS dataset(Coucke et al., 2018; Qin et al., 2020).
- prompt-based paradigm, and formulate the task PlayList and RateBook) and the slot values with

## Method
- Incorporating Instructional Prompts into A Unified Generative Framework
- Generative framework (UGEN) based on a models are expected to identify the intents (AddTo-
- prompt-based paradigm, and formulate the task PlayList and RateBook) and the slot values with
- prompts, UGEN is guided to understand in- which achieve fine-grained multi-intent informa-
- two popular multi-intent benchmark datasets, able success.

## Data and Evaluation Setup
- NIPS dataset(Coucke et al., 2018; Qin et al., 2020).
- two popular multi-intent benchmark datasets, able success.
- and surpasses the baselines by a large margin
- Question-3 lists the slot values in X and steers the evaluation phase, only question-1 and question-5
- slot value with its slot name (positive) or random 4 Experiments

## Results and Claims
- Slot Filling (SF) is a significant challenge in
- prompts, UGEN is guided to understand in- which achieve fine-grained multi-intent informa-
- ods with PLMs have achieved substantial improve-
- Baselines We compare UGEN with existing top- leads to slight improvements (0.1% and 0.9%) com-
- their names. Turning to intent accuracy, UGEN

## Limitations and Follow-ups
- Slot Filling (SF) is a significant challenge in
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, prompting, retrieval, dialogue, benchmark, graph
- Mentioned datasets: ATIS, SNIPS, TOP
- Mentioned metrics: accuracy, acc, f1

## Benchmark Evidence Lines
- NIPS dataset(Coucke et al., 2018; Qin et al., 2020).
- two popular multi-intent benchmark datasets, able success.
- Experiments on two multi-intent benchmarks
- show that UGEN outperforms the baselines and
- Question-3 lists the slot values in X and steers the evaluation phase, only question-1 and question-5
- all the slot values and their names by the given Dataset We compare our method with the base-
- question and options. Here, Questions 2-4 act as lines on two popular multi-intent SLU datasets,
- capture the links between slot names and their men- from SNIPS dataset (Coucke et al., 2018) which

## Related Concepts
- [[dialogue-systems]]
