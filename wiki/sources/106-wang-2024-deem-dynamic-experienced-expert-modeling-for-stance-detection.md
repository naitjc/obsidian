---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, bias, verification]
sources: [raw/sources/Wang 等 - 2024 - DEEM Dynamic Experienced Expert Modeling for Stance Detection.pdf]
---

# Wang 等 - 2024 - DEEM Dynamic Experienced Expert Modeling for Stance Detection

## Metadata
- Source file: `raw/sources/Wang 等 - 2024 - DEEM Dynamic Experienced Expert Modeling for Stance Detection.pdf`
- Year: 2024
- Pages: 12
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- DEEM: Dynamic Experienced Expert Modeling for Stance Detection
- Recent work has made a preliminary attempt to use large language models (LLMs) to solve the stance detection
- task, showing promising results. However, considering that stance detection usually requires detailed background
- Keywords: Stance Detection, Dynamic Experienced Expert Modeling, Large Language Models

## Method
- DEEM: Dynamic Experienced Expert Modeling for Stance Detection
- Recent work has made a preliminary attempt to use large language models (LLMs) to solve the stance detection
- knowledge, the vanilla reasoning method may neglect the domain knowledge to make a professional and accurate
- analysis. Thus, there is still room for improvement of LLMs reasoning, especially in leveraging the generation
- from existing multi-agent works that require detailed descriptions and use fixed experts, we propose a Dynamic

## Data and Evaluation Setup
- demonstrate that DEEM consistently achieves the best results on three standard benchmarks, outperforms methods
- sive performance to detect stance in a zero-shot
- widely used datasets, including P-Stance (Li et al.,
- ment across all datasets. Furthermore, it also out-
- datasets (Augenstein et al., 2016; Zhang et al.,

## Results and Claims
- analysis. Thus, there is still room for improvement of LLMs reasoning, especially in leveraging the generation
- demonstrate that DEEM consistently achieves the best results on three standard benchmarks, outperforms methods
- pirically confirm that ChatGPT can achieve impres-
- sive performance to detect stance in a zero-shot
- Military_Science_Expert ● Response Accuracy Prompt + New Sent

## Limitations and Follow-ups
- with self-consistency reasoning, and reduces the bias of LLMs.
- hallucinations and factual errors (Guerreiro et al., you actually trying, as president of the U.S., to start
- tively. The green texts indicate the manually written
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, bias, verification
- Mentioned datasets: SemEval, P-Stance, ARC, MTS, Twitter
- Mentioned metrics: accuracy, acc, f1, recall, f1-score

## Abstract (Extracted)
> Recent work has made a preliminary attempt to use large language models (LLMs) to solve the stance detection task, showing promising results. However, considering that stance detection usually requires detailed background knowledge, the vanilla reasoning metho

## Benchmark Evidence Lines
- demonstrate that DEEM consistently achieves the best results on three standard benchmarks, outperforms methods
- sive performance to detect stance in a zero-shot
- generated agents by LLMs may not be suitable due
- widely used datasets, including P-Stance (Li et al.,
- 2021), SemEval-2016 (Mohammad et al., 2016),
- the task directly by zero-shot or few-shot reason- The overall pipeline of the proposed DEEM is
- Military_Science_Expert ● Response Accuracy Prompt + New Sent
- prediction accuracy Acc(·) of each expert em ∈ E :

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
