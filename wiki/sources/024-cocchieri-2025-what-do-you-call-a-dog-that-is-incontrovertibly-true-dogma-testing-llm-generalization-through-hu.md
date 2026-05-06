---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, zero-shot, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Cocchieri 等 - 2025 - “What do you call a dog that is incontrovertibly true Dogma” Testing LLM Generalization through Hu.pdf]
---

# Cocchieri 等 - 2025 - “What do you call a dog that is incontrovertibly true Dogma” Testing LLM Generalization through Hu

## Metadata
- Source file: `raw/sources/Cocchieri 等 - 2025 - “What do you call a dog that is incontrovertibly true Dogma” Testing LLM Generalization through Hu.pdf`
- Year: 2025
- Pages: 16
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- The paper tests whether LLMs genuinely generalize linguistic reasoning or mainly exploit familiar benchmark patterns.
- It uses humor and puns because they require flexible wordplay, ambiguity handling, and out-of-distribution reasoning.
- The central benchmark is PHUNNY, a manually curated humor-based QA dataset.

## Method
- Designs pun comprehension, pun resolution, and pun generation tasks.
- Evaluates both coherent puns and misleading/non-pun cases to test whether models distinguish real wordplay from surface associations.
- Compares closed models, open models, reasoning models, and human baselines.

## Data and Evaluation Setup
- PHUNNY includes 350 manually curated novel heterographic pun types.
- The evaluation covers comprehension, resolution, constrained generation, and free generation.
- Publication-checked values are tracked in [[llm-reasoning-metrics-matrix]].

## Results and Claims
- Humans strongly outperform models on misleading-pun recognition, while o3-mini is strongest on several structured resolution/generation tasks.
- Publication-checked values include human CPA/MPA 87.9/90.9, o3-mini CPA 78.3, o3-mini resolution ACC 93.9, and human resolution ACC 85.7.
- The paper is best used as evidence that LLM reasoning strength can be brittle under creative linguistic generalization.

## Limitations and Follow-ups
- PHUNNY is focused on English wordplay, so conclusions should not be generalized to all humor or all languages.
- Free-generation accuracy and creativity need to be interpreted together; high accuracy can coexist with low diversity.
- Exact priority values are publication-checked in [[llm-reasoning-metrics-matrix]].

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: SemEval, ATIS, TOP
- Mentioned metrics: accuracy, acc


## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
