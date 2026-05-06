---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, zero-shot, prompting, synthetic-data, retrieval, benchmark, causal]
sources: [raw/sources/Jang 等 - 2025 - Expanding Computation Spaces of LLMs at Inference Time.pdf]
---

# Jang 等 - 2025 - Expanding Computation Spaces of LLMs at Inference Time

## Metadata
- Source file: `raw/sources/Jang 等 - 2025 - Expanding Computation Spaces of LLMs at Inference Time.pdf`
- Year: 2025
- Pages: 17
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Chain-of-thought (CoT) rationale enables language models to use additional task-
- related text for problem-solving, benefiting not only from detailed reasoning steps
- from 1.7B to 32B across open-domain QA and math tasks show that appropri-
- across tasks by guiding models to decompose and solve problems step by step, thereby making rea-

## Method
- Chain-of-thought (CoT) rationale enables language models to use additional task-
- related text for problem-solving, benefiting not only from detailed reasoning steps
- study, we investigate whether language models can leverage artificially inserted
- types, numbers, and insertion locations, then examine at what stage of training
- models begin to exploit the expanded computation space, and finally analyze dy-

## Data and Evaluation Setup
- namics within these spaces via attention maps. Experiments on models ranging
- the input. In addition, we experiment with transformer-based causal decoder-only language models
- Our experiments show that models can exploit filler tokens as expanded computation spaces even
- these special tokens leads to performance improvements across several benchmarks. In Lanham
- To investigate this, we first conduct experiments on question answering tasks (§ 4.1) and mathemat-

## Results and Claims
- Chain-of-thought (CoT) prompting has been shown to substantially improve reasoning performance
- tokens in the input as an expanded computation space can enhance model performance.
- kens consistently improve performance, with smaller models benefiting more, which is likely due to
- ing the pre-training (PT) or fine-tuning (FT) stages, aiming to improve the reasoning of the models.
- plored the use of special thinking tokens to prompt models to engage in improved reasoning Fan

## Limitations and Follow-ups
- (MMLU, Hendrycks et al. (2021)) and AI2 Reasoning Challenge (ARC, Clark et al. (2018)) for
- challenge test subset, which has 1172 samples in science questions with mostly 4 options, but also
- expanded space compensates for the limitations imposed by its smaller parameter size. We also ob-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, role-playing, emotion-recognition, benchmark, causal
- Mentioned datasets: ATIS, MASSIVE, TOP
- Mentioned metrics: accuracy

## Abstract (Extracted)
> Chain-of-thought (CoT) rationale enables language models to use additional task- related text for problem-solving, benefiting not only from detailed reasoning steps but also from the expanded computational space of longer inputs. Prior work has trained filler or special tokens to

## Benchmark Evidence Lines
- these special tokens leads to performance improvements across several benchmarks. In Lanham
- We primarily experiment with two datasets: Measuring Massive Multitask Language Understanding
- with 3 and 5 options. We additionally consider the mathematics dataset GSM8K and MATH-500 1
- mathematics. MATH-500 consists of 500 problems from the MATH benchmark that OpenAI created
- ARC datasets, which consist of multiple-choice questions with mostly four options, we provide
- For our experiments, we use a zero-shot setting, providing the models only with the dataset samples
- swering performance of models on MMLU, a general-domain QA benchmark, and ARC, a science-
- ‘<pad>’ (pad), ‘-’ (dash). Across models, we observe accuracy improvements of up to 12.372

## Related Concepts
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
