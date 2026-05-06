---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, retrieval, benchmark]
sources: [raw/sources/Sengupta 等 - TOP-Training Target-Oriented Pretraining for Medical Extractive Question Answering.pdf]
---

# Sengupta 等 - TOP-Training Target-Oriented Pretraining for Medical Extractive Question Answering

## Metadata
- Source file: `raw/sources/Sengupta 等 - TOP-Training Target-Oriented Pretraining for Medical Extractive Question Answering.pdf`
- Year: 2025
- Pages: 20
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Abstract This includes tasks like identifying the medica-
- To handle those challenges, we pro- ing (Medical-EQA) (Tian et al., 2023).
- pose TOP-Training, a target-oriented pre- mary challenges in Medical-EQA stem from i)
- the target problem to have a large set of unla- dataset is severely limited, with scarce training data

## Method
- TOP-Training: Target-Oriented Pretraining for Medical Extractive
- pose TOP-Training, a target-oriented pre- mary challenges in Medical-EQA stem from i)
- which many AI models struggle to recognize and
- ples with two main issues: i) Some approaches rely

## Data and Evaluation Setup
- TOP-Training: Target-Oriented Pretraining for Medical Extractive
- pose TOP-Training, a target-oriented pre- mary challenges in Medical-EQA stem from i)
- with the target dataset, and (ii) it does not Despite considerable research efforts and ad-
- impractical due to privacy constraints (Brown et al.,

## Results and Claims
- thetic text data yields better performance erative large language models (LLMs) pre-trained
- (EHR) underscores the growing significance of scales, TOP-Training extracts medical entities
- data, thus bolstering extractive LLMs for improved EQA datasets, especially in the medical domain,
- TOP-Training achieves state-of-the-art perfor- indices indicating either token or sentence-level

## Limitations and Follow-ups
- To handle those challenges, we pro- ing (Medical-EQA) (Tian et al., 2023).
- pose TOP-Training, a target-oriented pre- mary challenges in Medical-EQA stem from i)
- the limitations of autoregressive LLMs, empha- we harness the rich pre-trained knowledge in LLMs
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, synthetic-data, retrieval, prompting, graph, causal, benchmark, llm-reasoning
- Mentioned datasets: ATIS, TOP, SQuAD, MR
- Mentioned metrics: acc, f1, precision, recall, exact match, em

## Abstract (Extracted)
> This includes tasks like identifying the medica- tions a patient is currently taking and uncovering We study extractive question-answering in the recorded drug allergies or adverse reactions. Ex- medical domain (Medical-EQA). This prob- tractive Question Answering (EQA) plays a central lem has two main challenges: (i) domain role in EHR-based IE, wherein the system must specificity, as most AI models lack neces- provide a relevant textual excerpt from medical sary domain knowledge, and (ii) extraction- based answering style, which restricts most records based on a query. This is commonly re- autoregressive LLMs due to potential halluci- ferred to as Medical Extractive Question Answer- nations. To handle those challenges, we pro- ing (Medical-EQA) (Tian et al., 2023). The pri- pose TOP-Training, a target-oriented pre- mary challenges in Medical-EQA stem from i) training paradigm that stan

## Related Concepts
- [[retrieval-augmented-generation]]
- [[llm-evaluation]]
- [[nlp-research-collection]]
