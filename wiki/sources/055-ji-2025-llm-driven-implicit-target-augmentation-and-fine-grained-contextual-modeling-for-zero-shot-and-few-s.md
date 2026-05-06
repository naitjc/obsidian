---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S.pdf]
---

# Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S

## Metadata
- Source file: `raw/sources/Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S.pdf`
- Year: 2025
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Stance detection can miss implicit targets because datasets often annotate explicit textual cues while leaving latent targets underspecified.
- Zero-shot and few-shot stance settings require models to infer target-relevant context without relying on abundant labeled examples.
- The paper focuses on implicit target augmentation and context-sensitive text-target modeling.

## Method
- Proposes HCTA, an LLM-driven implicit target augmentation strategy using Chain-of-Thought prompting and multi-LLM voting.
- Combines HCTA with DyMCA, a model architecture that dynamically adjusts text-target contributions.
- Tests both augmentation components and model architecture through ablations.

## Data and Evaluation Setup
- Evaluates zero-shot, few-shot, all-setting, low-resource, and VAST phenomenon-level stance detection.
- Reports macro F1 for main stance settings and accuracy for VAST phenomena.
- Publication-checked values are tracked in [[llm-reasoning-metrics-matrix]].

## Results and Claims
- DyMCA with HCTA reports the strongest main macro F1 values in the checked table: 0.810 zero-shot, 0.771 few-shot, and 0.776 all.
- The ablations show degradation when HCTA, CoT, voting, or key model components are removed.
- Treat this as stance-detection evidence inside the LLM reasoning/evaluation cluster; do not compare it globally to unrelated reasoning tasks.

## Limitations and Follow-ups
- LLM-generated implicit targets may encode model bias or hallucinated target assumptions.
- Follow-up checks should inspect generated targets, not only downstream stance scores.
- Exact priority values are publication-checked in [[llm-reasoning-metrics-matrix]].

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, sarcasm, emotion-recognition, benchmark, graph
- Mentioned datasets: SemEval, ATIS, TOP, Facebook
- Mentioned metrics: accuracy, macro f1, f1, f1-score


## Related Concepts
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
