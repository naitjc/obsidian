---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, sarcasm, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Hwang 等 - 2025 - BottleHumor Self-Informed Humor Explanation using the Information Bottleneck Principle.pdf]
---

# Hwang 等 - 2025 - BottleHumor Self-Informed Humor Explanation using the Information Bottleneck Principle

## Metadata
- Source file: `raw/sources/Hwang 等 - 2025 - BottleHumor Self-Informed Humor Explanation using the Information Bottleneck Principle.pdf`
- Year: 2025
- Pages: 22
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- on three datasets confirm the advantage of our
- method over a range of baselines. Our method Figure 1: Humor understanding requires understanding
- tional tasks that can benefit from eliciting and dundancy in existing inputs (e.g. image descriptions)
- fer, 1999; Wanzer et al., 2010; Vartabedian, 1993; Several datasets for multimodal humor under-

## Method
- language models which is iteratively refined world hardship. struggles by mixing whimsy with
- method over a range of baselines. Our method Figure 1: Humor understanding requires understanding
- Kasulis, 1989) that can manifest in various forms, standing tasks were proposed, where models are
- imagination (Warren and Mcgraw, 2015; Warren overlooked in vision-and-language models (VLMs)
- multiple modalities (e.g., cartoons and memes; strated remarkable visual reasoning capabilities on

## Data and Evaluation Setup
- on three datasets confirm the advantage of our
- method over a range of baselines. Our method Figure 1: Humor understanding requires understanding
- fer, 1999; Wanzer et al., 2010; Vartabedian, 1993; Several datasets for multimodal humor under-
- et al., 2020). evaluations, possibly due to the subjective nature
- Shifman, 2013). Interpreting humor across modali- datasets requiring scientific knowledge (Lu et al.,

## Results and Claims
- ing capabilities of LLMs, we propose new auto- Eliciting knowledge from LLMs to improve pre-
- lines and outperforms existing self-refine methods setting (Zhang et al., 2024) by adding external
- significantly shorter or longer than the average re-
- dio, and images. It matches GPT-4’s performance
- After H iterations of refinement, we generate the in English text tasks with improved vision under-

## Limitations and Follow-ups
- In particular, humor is prevalent in online com- of humor and the challenges in evaluating free-text
- more complete, referencing visual information. To error analysis of our method’s predictions (§5.3).
- mance. The two most common errors are: dilution
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, sarcasm, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: UR-FUNNY, TOP, Persona
- Mentioned metrics: accuracy, f1, precision, recall

## Benchmark Evidence Lines
- on three datasets confirm the advantage of our
- fer, 1999; Wanzer et al., 2010; Vartabedian, 1993; Several datasets for multimodal humor under-
- et al., 2020). evaluations, possibly due to the subjective nature
- Shifman, 2013). Interpreting humor across modali- datasets requiring scientific knowledge (Lu et al.,
- modal humor explanation datasets: MemeCap (CoT; Wei et al., 2022). CoT steers LLMs to gen-
- evaluation. Leveraging the strong text understand- prove their answers with self-generated feedback.
- matic evaluation metrics that resemble precision dictions has been used for opinion understanding
- lines and outperforms existing self-refine methods setting (Zhang et al., 2024) by adding external

## Related Concepts
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
