---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, zero-shot, prompting, synthetic-data, retrieval, benchmark]
sources: [raw/sources/Wang 等 - 2025 - Socratic-Zero  Bootstrapping Reasoning via Data-Free Agent Co-evolution.pdf]
---

# Wang 等 - 2025 - Socratic-Zero Bootstrapping Reasoning via Data-Free Agent Co-evolution

## Metadata
- Source file: `raw/sources/Wang 等 - 2025 - Socratic-Zero  Bootstrapping Reasoning via Data-Free Agent Co-evolution.pdf`
- Year: 2025
- Pages: 23
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Recent breakthroughs in large language models (LLMs) on reasoning tasks rely
- heavily on massive, high-quality datasets—typically human-annotated and thus
- fidelity curriculum generation. This closed-loop system produces a self-improving
- curriculum—requiring no pre-existing tasks or labels. Remarkably, starting from

## Method
- Recent breakthroughs in large language models (LLMs) on reasoning tasks rely
- dynamically adapt to the evolving capabilities of the model, leading to suboptimal
- training signals. To address these limitations, we introduce Socratic-Zero, a fully
- autonomous framework that generates high-quality training data from minimal seed
- examples through the co-evolution of three agents: the Teacher, the Solver, and the

## Data and Evaluation Setup
- heavily on massive, high-quality datasets—typically human-annotated and thus
- reasoning benchmarks (AMC23, AIME24-25, Olympiad, MATH-500, Minerva,
- (SOTA) commercial LLMs on these benchmarks, including Qwen3-235B-A22B,
- capabilities. (b) Our Socratic-Solver-8B achieves an impressive 56.1% average accuracy, marking a
- matical problems (Hendrycks et al., 2021; Cobbe et al., 2021), these advances rely on massive datasets

## Results and Claims
- only 100 seed questions, our Socratic-Solver-8B achieves an average gain of +20.2
- dent LLMs to achieve superior performance compared to other state-of-the-art
- (SOTA) commercial LLMs on these benchmarks, including Qwen3-235B-A22B,
- LLM—guides the co-evolution of two agents. The Solver improves by generating solutions and
- Figure 2: Overall performance comparison demonstrating the giant effectiveness of Socratic-Zero.

## Limitations and Follow-ups
- training signals. To address these limitations, we introduce Socratic-Zero, a fully
- To overcome these limitations, we introduce Socratic-Zero, a paradigm-shifting framework that
- the frozen Teacher strategically generates challenging problems based on Solver failures using fixed
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, role-playing, benchmark
- Mentioned datasets: MASSIVE, TOP
- Mentioned metrics: accuracy, precision

## Benchmark Evidence Lines
- heavily on massive, high-quality datasets—typically human-annotated and thus
- reasoning benchmarks (AMC23, AIME24-25, Olympiad, MATH-500, Minerva,
- dent LLMs to achieve superior performance compared to other state-of-the-art
- (SOTA) commercial LLMs on these benchmarks, including Qwen3-235B-A22B,
- the Teacher’s behavior to produce an increasingly suitable curriculum for the Solver.
- performance competitive with much larger state-of-the-art models, showcasing strong generalization
- capabilities. (b) Our Socratic-Solver-8B achieves an impressive 56.1% average accuracy, marking a
- matical problems (Hendrycks et al., 2021; Cobbe et al., 2021), these advances rely on massive datasets

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
