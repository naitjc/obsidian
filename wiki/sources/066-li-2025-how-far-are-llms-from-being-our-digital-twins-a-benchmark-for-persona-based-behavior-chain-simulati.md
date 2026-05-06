---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, role-playing, llm-reasoning, zero-shot, few-shot, prompting, retrieval, benchmark, graph, causal]
sources: [raw/sources/Li 等 - 2025 - How Far are LLMs from Being Our Digital Twins A Benchmark for Persona-Based Behavior Chain Simulati.pdf]
---

# Li 等 - 2025 - How Far are LLMs from Being Our Digital Twins A Benchmark for Persona-Based Behavior Chain Simulati

## Metadata
- Source file: `raw/sources/Li 等 - 2025 - How Far are LLMs from Being Our Digital Twins A Benchmark for Persona-Based Behavior Chain Simulati.pdf`
- Year: 2025
- Pages: 28
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Digital-twin style agents require models to simulate persona-consistent behavior chains, not just answer isolated profile questions.
- Current LLMs may perform plausible single-step behavior while failing to maintain consistency over a sequence.
- The paper introduces BEHAVIORCHAIN to evaluate persona-based behavior chain simulation.

## Method
- Defines AvgScore for node-wise behavior correctness and CumScore for consecutive correct behavior-chain consistency.
- Evaluates both multiple-choice and generation settings for fictional and nonfictional personas.
- Compares closed-source and open-source models against random and half-selection baselines.

## Data and Evaluation Setup
- Uses BEHAVIORCHAIN with fictional and nonfictional persona behavior chains.
- Reports AvgScore and CumScore across multiple-choice, generation, and overall settings.
- Publication-checked values are tracked in [[llm-reasoning-metrics-matrix]].

## Results and Claims
- Models perform better on multiple-choice than generation and struggle with continuous behavior-chain consistency.
- Publication-checked leaders include Llama-3.1-70B overall multiple-choice AvgScore/CumScore 0.574/0.172 and GPT-4o 0.559/0.158; generation scores include GPT-4o 0.471/0.189.
- The benchmark is useful for evaluating long-horizon persona simulation rather than broad role-playing fluency alone.

## Limitations and Follow-ups
- Behavior simulation has non-unique plausible outputs, especially in generation settings.
- CumScore is stringent and should be interpreted as chain consistency rather than ordinary accuracy.
- Exact priority values are publication-checked in [[llm-reasoning-metrics-matrix]].

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, role-playing, emotion-recognition, benchmark, graph, causal
- Mentioned datasets: ATIS, MASSIVE, TOP, Persona, MAMI
- Mentioned metrics: accuracy, precision, recall


## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
