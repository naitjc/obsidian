---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, zero-shot, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Han 等 - 2025 - Reasoning with Graphs Structuring Implicit Knowledge to Enhance LLMs Reasoning.pdf]
---

# Han 等 - 2025 - Reasoning with Graphs Structuring Implicit Knowledge to Enhance LLMs Reasoning

## Metadata
- Source file: `raw/sources/Han 等 - 2025 - Reasoning with Graphs Structuring Implicit Knowledge to Enhance LLMs Reasoning.pdf`
- Year: 2025
- Pages: 16
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- of tasks; however, they still encounter chal-
- lenges in reasoning tasks that require under-
- ever, in many reasoning tasks, no pre-existing
- question answering tasks. improvement in certain reasoning tasks without

## Method
- Reasoning with Graphs: Structuring Implicit Knowledge to Enhance
- lenges in reasoning tasks that require under-
- cesses, such as logical reasoning and multi-hop Output Output Output
- Figure 1: Comparison of Reasoning with Graph (RwG)
- text are crucial. Graphs, as fundamental data

## Data and Evaluation Setup
- answering (Yang et al., 2024). abilities with the constructed graph. Experimental
- eral evaluations (Guo et al., 2023; Liu and Wu,
- 4 Experiment LLaMA3.1 70B (Touvron et al., 2023). Ad-
- eral representative baselines, such as the Chain-
- dataset, there are only 3 different relations between

## Results and Claims
- proving both logical reasoning and multi-hop to the final answer. CoT has shown significant
- question answering tasks. improvement in certain reasoning tasks without
- still encounter significant challenges in certain ar- respectively. These methods prompt LLMs to gen-
- to figure out the relationships between entities in cantly improves the performance of various LLMs
- of questions pose significant challenges for LLMs, LLaMA-3 (Touvron et al., 2023), suggest that the

## Limitations and Follow-ups
- still encounter significant challenges in certain ar- respectively. These methods prompt LLMs to gen-
- key limitation lies in their struggle with reasoning ious structures. Despite the successes of these
- tasks (Yang et al., 2024; Huang et al., 2023), par- approaches, they still face challenges in handling
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, role-playing, benchmark, graph
- Mentioned datasets: ATIS, TOP
- Mentioned metrics: accuracy

## Benchmark Evidence Lines
- eral evaluations (Guo et al., 2023; Liu and Wu,
- dataset, there are only 3 different relations between
- RWG for these dataset are shown in Appendix A.2.
- AIW+ datasets are presented in Table 1, while
- the results for the LogiQA and LSAT datasets are
- shown in Table 2. From these results, we can make
- step for effective logical reasoning. The general ious LLMs on all datasets.
- and relations; (2) Verification: Verify whether the and AIW+ datasets, applying RWG usually does

## Related Concepts
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
