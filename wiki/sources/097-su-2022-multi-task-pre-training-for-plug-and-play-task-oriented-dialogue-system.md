---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, zero-shot, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Su 等 - 2022 - Multi-Task Pre-Training for Plug-and-Play Task-Oriented Dialogue System.pdf]
---

# Su 等 - 2022 - Multi-Task Pre-Training for Plug-and-Play Task-Oriented Dialogue System

## Metadata
- Source file: `raw/sources/Su 等 - 2022 - Multi-Task Pre-Training for Plug-and-Play Task-Oriented Dialogue System.pdf`
- Year: 2022
- Pages: 16
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- cently shown to benefit task-oriented dialogue
- ing methods often formulate this task as a cas-
- error accumulation across different sub-tasks methods formulate task-oriented dialogue as a cas-
- and greater data annotation overhead. In this caded generation problem, that is, the model can

## Method
- and greater data annotation overhead. In this caded generation problem, that is, the model can
- play model for task-oriented dialogue. In ad- outputs of previous ones. For instance, to generate
- the response (NLG), the model must rely on the
- pre-training strategy that allows the model to
- tensively test our model on three benchmark Asl et al., 2020; Peng et al., 2021), we identify

## Data and Evaluation Setup
- tensively test our model on three benchmark Asl et al., 2020; Peng et al., 2021), we identify
- classification. Experimental results show that
- model pre-training (Zhang et al., 2020c; Wu et al., • Extensive evaluations on three benchmark
- logue corpora. The collected datasets are partially
- all pre-training corpora. All datasets are partially an-

## Results and Claims
- against previous SOTA methods show that the Secondly, the training data must be annotated for
- 2020; Peng et al., 2021), we propose a dialogue TOD tasks reporting state-of-the-art results in
- art approaches show that PPTOD achieves better and Vulic´ (2019) first applied the GPT-2 model for
- performance in both full-training and low-resource the NLG task. Lin et al. (2020) and Yang et al.
- oracle information. To improve the system perfor- ATIS (cid:88) × × × 10,772 1

## Limitations and Follow-ups
- error accumulation across different sub-tasks methods formulate task-oriented dialogue as a cas-
- TOD tasks, including end-to-end dialogue three major limitations in the cascaded formulation
- solves all sub-tasks in a sequential order, the errors
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, role-playing, benchmark, graph
- Mentioned datasets: ATIS, SNIPS, MultiWOZ, DSTC, MASSIVE, TOP, Persona
- Mentioned metrics: accuracy, acc, bleu

## Benchmark Evidence Lines
- tensively test our model on three benchmark Asl et al., 2020; Peng et al., 2021), we identify
- model pre-training (Zhang et al., 2020c; Wu et al., • Extensive evaluations on three benchmark
- 2020; Peng et al., 2021), we propose a dialogue TOD tasks reporting state-of-the-art results in
- logue corpora. The collected datasets are partially
- tails in Table 1). When applying the pre-trained
- Table 1: The summary of data annotations and number
- all pre-training corpora. All datasets are partially an-
- including language understanding (Peters et al., In this section, we first discuss the datasets and

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
