---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, llm-reasoning, zero-shot, few-shot, prompting, retrieval, cross-lingual, target-adaptive, bias, verification]
sources: [raw/sources/Zhang 等 - 2024 - An LLM-Enabled Knowledge Elicitation and Retrieval Framework for Zero-Shot Cross-Lingual Stance Iden.pdf]
---

# Zhang 等 - 2024 - An LLM-Enabled Knowledge Elicitation and Retrieval Framework for Zero-Shot Cross-Lingual Stance Iden

## Metadata
- Source file: `raw/sources/Zhang 等 - 2024 - An LLM-Enabled Knowledge Elicitation and Retrieval Framework for Zero-Shot Cross-Lingual Stance Iden.pdf`
- Year: 2024
- Pages: 14
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Zero-Shot Cross-Lingual Stance Identification
- Stance detection aims to identify the attitudes
- stance detection (CLSD) transfers the knowledge
- shot setting. Zero-shot cross-lingual stance detec-

## Method
- An LLM-Enabled Knowledge Elicitation and Retrieval Framework for
- edge elicitation and retrieval framework. The the stance toward certain targets when no training
- LLM’s reasoning process. Then, the knowl- approach (Hardalov et al., 2022) proposes to pre-
- edge retrieval module in KEAR matches the tar-
- train language models with sentiment-based data

## Data and Evaluation Setup
- Zero-Shot Cross-Lingual Stance Identification
- mainly conducted in monolingual setting on En- are conducted on English datasets, whereas in other
- glish datasets. To tackle the data scarcity prob- low-resource languages, it lacks sufficient data for
- shot setting. Zero-shot cross-lingual stance detec-
- Experiments on multilingual datasets show the

## Results and Claims
- rives different types of stance knowledge from ing data) in target language. The state-of-the-art
- performance. Specifically, D is used to acquire
- standard deviations of 5 runs in percentage. The best performances are marked in bold.
- We use accuracy and macro F1 as the evaluation
- with target language data): TaRA (Zhang et al., methods, the superior performances of fine-tuning

## Limitations and Follow-ups
- stereotype. She also emphasized on enhancing public education of stance knowledge from LLM’s reasoning pro-
- imply criticism, likely referencing the stereotype of gender and
- gender stereotype and blames for public education, indicating Explanation speech act theory (Searle, 1969), a speech act lexi-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, multimodal, cross-lingual, target-adaptive, bias, verification
- Mentioned datasets: SemEval, ARC, Twitter
- Mentioned metrics: accuracy, acc, macro f1, f1

## Benchmark Evidence Lines
- Zero-Shot Cross-Lingual Stance Identification
- is the most challenging in zero-shot setting
- proving the performance of zero-shot CLSD.
- shot setting. Zero-shot cross-lingual stance detec-
- rives different types of stance knowledge from ing data) in target language. The state-of-the-art
- itive baselines as well as the CLSD approaches of zero-shot CLSD. Since there is no training data
- defined targets (e.g., entities, controversial topics for zero-shot CLSD can serve as a feasible scheme
- And Retrieval (KEAR) framework for zero-shot

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
