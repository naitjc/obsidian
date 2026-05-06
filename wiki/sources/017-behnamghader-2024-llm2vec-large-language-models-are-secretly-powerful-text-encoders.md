---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark, graph, causal]
sources: [raw/sources/BehnamGhader 等 - 2024 - LLM2Vec Large Language Models Are Secretly Powerful Text Encoders.pdf]
---

# BehnamGhader 等 - 2024 - LLM2Vec Large Language Models Are Secretly Powerful Text Encoders

## Metadata
- Source file: `raw/sources/BehnamGhader 等 - 2024 - LLM2Vec Large Language Models Are Secretly Powerful Text Encoders.pdf`
- Year: 2024
- Pages: 28
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- on most of today’s NLP tasks and benchmarks. Yet, the community is only
- slowly adopting these models for text embedding tasks, which require rich
- and evaluate the transformed models on English word- and sequence-level
- tasks. We outperform encoder-only models by a large margin on word-level

## Method
- LLM2Vec: Large Language Models Are Secretly Powerful Text
- Large decoder-only language models (LLMs) are the state-of-the-art models
- on most of today’s NLP tasks and benchmarks. Yet, the community is only
- slowly adopting these models for text embedding tasks, which require rich
- and evaluate the transformed models on English word- and sequence-level

## Data and Evaluation Setup
- on most of today’s NLP tasks and benchmarks. Yet, the community is only
- Massive Text Embeddings Benchmark (MTEB). Moreover, when combining
- contextualized token representations. On the Massive Text Embeddings Benchmark (MTEB),
- Models For most of our results, we experiment with 3 different decoder-only LLMs
- pre-training mixture of all the models we experiment with. It is therefore fair to assume that

## Results and Claims
- Large decoder-only language models (LLMs) are the state-of-the-art models
- tasks. We outperform encoder-only models by a large margin on word-level
- tasks and reach a new unsupervised state-of-the-art performance on the
- LLM2Vec with supervised contrastive learning, we achieve state-of-the-art
- performance on MTEB among models that train only on publicly available

## Limitations and Follow-ups
- limitation is necessary for generative capabilities, it is sub-optimal for text embeddings as it
- Overcoming this architectural limitation of decoder-only LLMs for text embedding tasks is
- 1We acknowledge that there are also several challenges associated with the large size of these
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, emotion-recognition, benchmark, graph, causal
- Mentioned datasets: SemEval, MASSIVE, TOP, Facebook, ECHO
- Mentioned metrics: none detected

## Abstract (Extracted)
> Large decoder-only language models (LLMs) are the state-of-the-art models on most of today’s NLP tasks and benchmarks. Yet, the community is only slowly adopting these models for text embedding tasks, which require rich contextualized representations. In this work, we introduce L

## Benchmark Evidence Lines
- Large decoder-only language models (LLMs) are the state-of-the-art models
- on most of today’s NLP tasks and benchmarks. Yet, the community is only
- tasks. We outperform encoder-only models by a large margin on word-level
- tasks and reach a new unsupervised state-of-the-art performance on the
- Massive Text Embeddings Benchmark (MTEB). Moreover, when combining
- LLM2Vec with supervised contrastive learning, we achieve state-of-the-art
- recognition, and part-of-speech tagging), LLM2Vec-transformed models outperform strong
- contextualized token representations. On the Massive Text Embeddings Benchmark (MTEB),

## Related Concepts
- [[llm-reasoning]]
- [[emotion-recognition]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
