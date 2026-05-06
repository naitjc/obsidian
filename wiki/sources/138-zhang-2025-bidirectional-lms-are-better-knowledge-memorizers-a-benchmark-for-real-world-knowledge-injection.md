---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, llm-reasoning, benchmark]
sources: [raw/sources/Zhang 等 - 2025 - Bidirectional LMs are Better Knowledge Memorizers A Benchmark for Real-world Knowledge Injection.pdf]
---

# Zhang 等 - 2025 - Bidirectional LMs are Better Knowledge Memorizers A Benchmark for Real-world Knowledge Injection

## Metadata
- Source file: `raw/sources/Zhang 等 - 2025 - Bidirectional LMs are Better Knowledge Memorizers A Benchmark for Real-world Knowledge Injection.pdf`
- Year: 2025
- Pages: 18
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- tiple question–answer pairs spanning diverse task formats from easy cloze prompts
- Previous work suggests significant challenges in effectively updating the internal knowledge of
- Source Scope Frequency Curated Extension Tasks
- Figure 1: Proposed knowledge injection evaluation workflow.

## Method
- Despite significant advances in large language models (LLMs), their knowledge
- Extensive experiments using continued pre-training reveal a surprising in-
- sight: despite their prevalence in modern LLMs, Causal Language Models (CLMs)
- to Bidirectional Language Models (Bi LMs), exhibiting a 23% lower accuracy in

## Data and Evaluation Setup
- A Benchmark for Real-world Knowledge Injection
- large-scale knowledge injection benchmark that evolves continuously over time
- Extensive experiments using continued pre-training reveal a surprising in-
- Large language models (LLMs) acquire most of their knowledge during pre-training, by learning

## Results and Claims
- to Bidirectional Language Models (Bi LMs), exhibiting a 23% lower accuracy in
- our framework further improves the reliability accuracy by up to 29.1%.
- As a result, LLMs are often treated as static knowledge bases – capable of
- their effectiveness in accurately reflecting model performance.

## Limitations and Follow-ups
- Previous work suggests significant challenges in effectively updating the internal knowledge of
- Finally, to address the challenges of scaling knowledge injection while miti-
- information (Mecklenburg et al., 2024), though retention remains a challenge (Ovadia et al., 2023).
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, synthetic-data, retrieval, prompting, graph, causal, benchmark, llm-reasoning
- Mentioned datasets: MASSIVE, TOP
- Mentioned metrics: accuracy, acc, f1, recall, em

## Abstract (Extracted)
> Despite significant advances in large language models (LLMs), their knowledge memorization capabilities remain underexplored, due to the lack of standardized and high-quality test ground. In this paper, we introduce a novel, real-world and large-scale knowledge injection benchmark that evolves continuously over time without requiring human intervention. Specifically, we propose WIKIDYK, which leverages recently-added and human-written facts from Wikipedia’s “Did You Know...” entries. These entries are carefully selected by expert Wikipedia editors based on criteria such as verifiability and clarity. Each entry is converted into mul- tiple question–answer pairs spanning diverse task formats from easy cloze prompts to complex multi-hop questions. WIKIDYK contains 12, 290 facts and 77, 180 questions, which is also seamlessly extensible with future updates from Wikipedia editors. Extensive e

## Related Concepts
- [[llm-reasoning]]
- [[llm-evaluation]]
- [[nlp-research-collection]]
