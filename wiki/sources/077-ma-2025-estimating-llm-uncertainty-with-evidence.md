---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, few-shot, prompting, retrieval, benchmark]
sources: [raw/sources/Ma 等 - 2025 - Estimating LLM Uncertainty with Evidence.pdf]
---

# Ma 等 - 2025 - Estimating LLM Uncertainty with Evidence

## Metadata
- Source file: `raw/sources/Ma 等 - 2025 - Estimating LLM Uncertainty with Evidence.pdf`
- Year: 2025
- Pages: 14
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- processes. We employ evidence modeling to implement LogTokU and use the estimated uncertainty to guide downstream tasks. The
- Unsolved Physics Problem Same probability distribution
- where LLMs have rich knowledge, are less reliable than on unsolved physics problems. This is because probability cannot reflect whether a low
- express “Lack knowledge, but I suggest” and “I know more classes. However, sampling-based methods can not evaluate

## Method
- Abstract—Over the past few years, Large Language Models (LLMs) have developed rapidly and are widely applied in various domains.
- However, LLMs face the issue of hallucinations, generating responses that may be unreliable when the models lack relevant knowledge.
- information which is accumulated in the training stage. Therefore, we present Logits-induced token uncertainty (LogTokU), a framework
- processes. We employ evidence modeling to implement LogTokU and use the estimated uncertainty to guide downstream tasks. The
- Index Terms—Uncertainty estimation, Foundation models

## Data and Evaluation Setup
- experimental results demonstrate that LogTokU has significant effectiveness and promise. Our code is available at link.
- The role of gradient dynamics. The purported scale in- Fig. 3. Illustration of experimental setting in Table 1.
- 4.1 LogTokU-guided Decoding maintaining accuracy. Specifically, we evaluate whether the
- diversity, especially in diversity-driven fields such as LLM- guidance of uncertainty on the multi-label LLM benchmark
- both diversity and accuracy in the generated responses. strategies and two dynamic decoding strategies based on

## Results and Claims
- experimental results demonstrate that LogTokU has significant effectiveness and promise. Our code is available at link.
- performance, LLMs remain prone to hallucinations [1], which
- methods often fail to achieve satisfactory results. For example,
- induced Token Uncertainty (LogTokU), which achieves both responses remain consistent across three samplings for each
- tainty are treated as separate cases. Compared to probability- Entropy (SE) [15], which improves token-level measures by

## Limitations and Follow-ups
- However, LLMs face the issue of hallucinations, generating responses that may be unreliable when the models lack relevant knowledge.
- To be aware of potential hallucinations, uncertainty estimation methods have been introduced, and most of them have confirmed that
- performance, LLMs remain prone to hallucinations [1], which
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, role-playing, emotion-recognition, benchmark
- Mentioned datasets: SemEval, ATIS, TOP
- Mentioned metrics: accuracy, precision, auroc, rouge

## Abstract (Extracted)
> —Over the past few years, Large Language Models (LLMs) have developed rapidly and are widely applied in various domains. However, LLMs face the issue of hallucinations, generating responses that may be unreliable when the models lack relevant knowledge. To be aware of potential h

## Benchmark Evidence Lines
- more than one token that can be the suitable next-token.
- Therefore, measuring the probability of a single suitable
- predicting the next token, the triangular patterns represent the corresponding Dirichlet distribution, and the table below compares uncertainty
- knowledge and knows more than one suitable answer. For example, the LLM generates “[comma]”, which can be replaced by many other suitable
- can be formulated as: training paradigm. There may be more than one suitable
- j=1 t−1 m=1 training process, the suitable token accumulates evidence
- model intends to express that there is more than one suitable
- The role of gradient dynamics. The purported scale in- Fig. 3. Illustration of experimental setting in Table 1.

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
