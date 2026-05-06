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
- LLMs still struggle with reasoning tasks that require implicit entity-relation structure.
- Many reasoning problems do not provide a clean pre-existing graph, so graph structure must be inferred.
- The paper asks whether explicit graph construction and verification can improve logical and multi-hop reasoning.

## Method
- Proposes Reasoning with Graphs (RWG), which generates graph structures from text, verifies them, and updates missing or incorrect relations.
- Uses graph verification and iterative graph generation before answer prediction.
- Compares RWG with vanilla prompting, CoT, self-consistency, and least-to-most prompting.

## Data and Evaluation Setup
- Evaluates on AIW, AIW+, LogiQA, AR-LSAT, and additional multi-hop QA settings.
- Reports accuracy-like scores across Claude, GPT-4o, Llama3.1-8B, and Llama3.1-70B.
- Publication-checked priority values are tracked in [[llm-reasoning-metrics-matrix]].

## Results and Claims
- RWG improves several logical and multi-hop reasoning settings, especially where missing relationships must be inferred.
- Publication-checked examples include GPT-4o 0.8666 with RWG+Relation on AIW, GPT-4o 0.5294 with RWG on AIW+, and GPT-4o 0.6451/0.4521 with RWG+Self-Consistency on LogiQA/AR-LSAT.
- The useful synthesis point is that explicit intermediate structure helps when the bottleneck is relational completeness.

## Limitations and Follow-ups
- RWG's benefit depends on whether generated graph relations are correct and complete.
- Follow-up analysis should inspect graph errors, not only final answer accuracy.
- Exact priority values are publication-checked in [[llm-reasoning-metrics-matrix]].

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, role-playing, benchmark, graph
- Mentioned datasets: ATIS, TOP
- Mentioned metrics: accuracy


## Related Concepts
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
