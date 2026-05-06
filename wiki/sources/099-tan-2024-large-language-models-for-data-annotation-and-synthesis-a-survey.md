---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, synthetic-data, llm-reasoning]
sources: [raw/sources/Tan 等 - 2024 - Large Language Models for Data Annotation and Synthesis A Survey.pdf]
---

# Tan 等 - 2024 - Large Language Models for Data Annotation and Synthesis A Survey

## Metadata
- Source file: `raw/sources/Tan 等 - 2024 - Large Language Models for Data Annotation and Synthesis A Survey.pdf`
- Year: 2024
- Pages: 29
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Furthermore, this survey and synthesis poses significant challenges for cur-
- cussion of the primary challenges and limita-
- this survey aims to assist researchers and prac- Gemini (Team et al., 2023), and LLa MA-2 (Tou-
- tasks, ensure consistency across large volumes of

## Method
- Large Language Models for Data Annotation and Synthesis: A Survey
- ered LLM architecture, training, and general 2022b), response (Zhang and Yang, 2023a), rea-
- includes an in-depth taxonomy of data types rent machine learning models due to the com-
- view of learning strategies for models utilizing

## Data and Evaluation Setup
- used for improving the efficacy of machine to understand how entities within a dataset interact
- ered LLM architecture, training, and general 2022b), response (Zhang and Yang, 2023a), rea-
- manually labeling or creating large datasets.
- titioners in exploring the potential of the latest vron et al., 2023b) offer a promising opportunity

## Results and Claims
- Abstract assigning confidence scores to assess annotation re-
- scores, contextual details, and other metadata, ex-
- from an aligned LLM and present a self-synthesis date response with the highest confidence score.
- To improve the diversity, Chan distill and augment the instruction tuning dataset by

## Limitations and Follow-ups
- The process, however, is with each other (Wadhwa et al., 2023), ❻ marking
- Furthermore, this survey and synthesis poses significant challenges for cur-
- cussion of the primary challenges and limita-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, synthetic-data, retrieval, prompting, graph, causal, benchmark, dialogue, llm-reasoning, multimodal
- Mentioned datasets: TOP, SQuAD, SST, MR
- Mentioned metrics: accuracy, acc, precision, bleu, mse, em

## Abstract (Extracted)
> assigning confidence scores to assess annotation re- liability (Lin et al., 2022), ❹ applying alignment or Data annotation and synthesis generally refers preference labels to tailor outputs to specific crite- to the labeling or generating of raw data with relevant information, which could be ria or user needs, ❺ annotating entity relationships used for improving the efficacy of machine to understand how entities within a dataset interact learning models. The process, however, is with each other (Wadhwa et al., 2023), ❻ marking labor-intensive and costly. The emergence semantic roles to define the underlying roles that of advanced Large Language Models (LLMs), entities play in a sentence (Larionov et al., 2019), exemplified by GPT-4, presents an unprece- ❼ tagging temporal sequences to capture the order dented opportunity to automate the compli- of events or actions (Yu et al., 2023), or

## Related Concepts
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[nlp-research-collection]]
