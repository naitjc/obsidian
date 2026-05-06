---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Xing和Tsang - 2022 - Co-guiding Net Achieving Mutual Guidances between Multiple Intent Detection and Slot Filling via He.pdf]
---

# Xing和Tsang - 2022 - Co-guiding Net Achieving Mutual Guidances between Multiple Intent Detection and Slot Filling via He

## Metadata
- Source file: `raw/sources/Xing和Tsang - 2022 - Co-guiding Net Achieving Mutual Guidances between Multiple Intent Detection and Slot Filling via He.pdf`
- Year: 2022
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Detection and Slot Filling via Heterogeneous Semantics-Label Graphs
- intent detection and slot filling have obtained
- two tasks. In the first stage, the initial estimated guidances between the two tasks.
- labels of both tasks are produced, and then they

## Method
- Detection and Slot Filling via Heterogeneous Semantics-Label Graphs
- Recent graph-based models for joint multiple decoding decoding
- ods (1) only model the unidirectional guidance shared encoder
- we propose a novel model termed Co-guiding Figure 1: (a) Previous framework which only models the
- Net, which implements a two-stage framework unidirectional guidance from multi-intent predictions to

## Data and Evaluation Setup
- and label nodes. Experiment results show that Narayanaswamy, 2019) make the first attempt to
- graphs for modeling the guidances from slot to in- tent and intent to slot, respectively. Experiment
- is retrieved from MixSNIPS dataset. The contributions of our work are three-fold: (1)
- { i n } As for evaluation metrics, following previous
- works, we adopt accuracy (Acc) for multiple intent

## Results and Claims
- our model outperforms existing models by a jointly model the multiple intent detection and slot
- large margin, obtaining a relative improvement
- ing state-of-the-art results and significant speedup.
- multi-intent SLU joint models have achieved, we
- results show that our Co-guiding Net significantly

## Limitations and Follow-ups
- i i 2Due to space limitation, the experiments using pre-trained
- Figure 6: Case study of slot-to-intent guidance (A) and intent-to-slot guidance (B). Red color denotes error.
- predicted, while there is an error in the predicted intent information into slot filling achieved by
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: prompting, retrieval, llm-reasoning, dialogue, emotion-recognition, benchmark, graph
- Mentioned datasets: ATIS, SNIPS, TOP
- Mentioned metrics: accuracy, acc, f1

## Benchmark Evidence Lines
- our model outperforms existing models by a jointly model the multiple intent detection and slot
- ing state-of-the-art results and significant speedup.
- Figure 2: Illustration of the bidirectional interrelations outperforms previous models, and model analysis
- is retrieved from MixSNIPS dataset. The contributions of our work are three-fold: (1)
- Hetegeneous Graph State-of-the-art models (Qin et al., 2020, 2021b)
- { i n } As for evaluation metrics, following previous
- works, we adopt accuracy (Acc) for multiple intent
- detection, F1 score for slot filling, and overall accu-

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[emotion-recognition]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
