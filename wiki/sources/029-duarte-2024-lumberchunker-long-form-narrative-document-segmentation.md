---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, retrieval, llm-reasoning, benchmark]
sources: [raw/sources/Duarte 等 - 2024 - LumberChunker Long-Form Narrative Document Segmentation.pdf]
---

# Duarte 等 - 2024 - LumberChunker Long-Form Narrative Document Segmentation

## Metadata
- Source file: `raw/sources/Duarte 等 - 2024 - LumberChunker Long-Form Narrative Document Segmentation.pdf`
- Year: 2024
- Pages: 14
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- propose Lumber Chunker, a method leveraging Retrieval Augmented Generation (RAG) systems
- proves to be more effective than other chunking In this paper, we propose Lumber Chunker, a
- range of tasks, including translation (Alves et al.,
- issue arises when these models are tasked with gen-

## Method
- Lumber Chunker: Long-Form Narrative Document Segmentation
- retrieval methods to access up-to-date and rele-
- by the premise that retrieval benefits from seg-
- propose Lumber Chunker, a method leveraging Retrieval Augmented Generation (RAG) systems

## Data and Evaluation Setup
- petitive baseline by 7.37% in retrieval perfor-
- methods and competitive baselines, such as the novel text segmentation method based on the prin-
- QA task to assess its effect on the accuracy of the splitting (Langchain, 2023) segments text based
- • We introduce Guten QA, a new benchmark com-

## Results and Claims
- n AI, 2022) in court, resulting in sanctions for the
- We sion and accuracy of information are paramount,
- ber Chunker not only outperforms the most com-
- ciple that retrieval efficiency improves when con-

## Limitations and Follow-ups
- lawyer and highlighting the severe risks of unveri-
- This avoids potential errors that often We compare its DCG@k and Recall@k scores
- the increased computational cost of segmenting a
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, synthetic-data, retrieval, prompting, graph, benchmark, llm-reasoning
- Mentioned datasets: ATIS, TOP, MR
- Mentioned metrics: accuracy, acc, recall, rouge, exact match, em

## Abstract (Extracted)
> quences, like the recent incident where a lawyer cited fictitious cases produced by Chat GPT (Ope- Modern NLP tasks increasingly rely on dense n AI, 2022) in court, resulting in sanctions for the retrieval methods to access up-to-date and rele- lawyer and highlighting the severe risks of unveri- vant contextual information. We are motivated fied AI-generated information (Bohannon, 2023). by the premise that retrieval benefits from seg- ments that can vary in size such that a content’s In the field of question answering, where preci- semantic independence is better captured. We sion and accuracy of information are paramount, propose Lumber Chunker, a method leveraging Retrieval Augmented Generation (RAG) systems an LLM to dynamically segment documents, present a viable solution to hallucinations by which iteratively prompts the LLM to identify grounding the model’s generation on contextua

## Related Concepts
- [[retrieval-augmented-generation]]
- [[llm-reasoning]]
- [[llm-evaluation]]
- [[nlp-research-collection]]
