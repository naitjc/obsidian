---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, sarcasm, zero-shot, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Ravi 等 - 2024 - Small But Funny A Feedback-Driven Approach to Humor Distillation.pdf]
---

# Ravi 等 - 2024 - Small But Funny A Feedback-Driven Approach to Humor Distillation

## Metadata
- Source file: `raw/sources/Ravi 等 - 2024 - Small But Funny A Feedback-Driven Approach to Humor Distillation.pdf`
- Year: 2024
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- guage generation capabilities, particularly in
- works well for simpler tasks, there is a sub-
- stantial performance gap on tasks requiring in-
- such as humor generation. We hypothesize Figure 1: Performance gap between LLMs and SLMs:

## Method
- chain-of-thought reasoning (Li et al., 2023a), and
- SLMs and their larger counterparts compared et al., 2023) to smaller language models. However,
- large models (OpenAI, 2023; Touvron et al., 2023). match the subtleties of humor in human-written
- straints of SLMs, such as reduced model capacity,
- Second, although imitating a teacher model is a 2 Related Work

## Data and Evaluation Setup
- Evaluation of our student models on the proposed currently led to the creation of large joke datasets
- task based on EmpatheticDialogues (Rashkin et al., (Weller et al., 2020) and benchmarks (Hossain et al.,
- 2019) and Samsum (Gliwa et al., 2019) datasets 2020).
- benchmarks (Hessel et al., 2023) have been devel-
- potential evaluation biases on narrowing the gap

## Results and Claims
- stantial performance gap on tasks requiring in-
- such as humor generation. We hypothesize Figure 1: Performance gap between LLMs and SLMs:
- could yield higher performance. To address has evolved to denote the process of distilling the
- LLMs achieve high performance across many tasks text (Hessel et al., 2023; Chakrabarty et al., 2023),
- to improve task understanding through distilling ods. Raskin (1979) introduced a semantic analysis

## Limitations and Follow-ups
- the strengths and limitations of the critic in eval-
- can also suffer from biases due to length, position,
- or other biases. We explore the effect of data size,
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: SemEval, TOP, ECHO, Persona
- Mentioned metrics: accuracy, bleu, rouge

## Benchmark Evidence Lines
- Evaluation of our student models on the proposed currently led to the creation of large joke datasets
- task based on EmpatheticDialogues (Rashkin et al., (Weller et al., 2020) and benchmarks (Hossain et al.,
- 2019) and Samsum (Gliwa et al., 2019) datasets 2020).
- the time, and significantly outperforms supervised
- benchmarks (Hessel et al., 2023) have been devel-
- human judgments with up to 76% accuracy, but
- potential evaluation biases on narrowing the gap
- Automatic evaluation of Natural Language Genera-

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
