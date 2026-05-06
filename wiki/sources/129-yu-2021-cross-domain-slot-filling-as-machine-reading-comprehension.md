---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, zero-shot, few-shot, retrieval, benchmark, graph]
sources: [raw/sources/Yu 等 - 2021 - Cross-Domain Slot Filling as Machine Reading Comprehension.pdf]
---

# Yu 等 - 2021 - Cross-Domain Slot Filling as Machine Reading Comprehension

## Metadata
- Source file: `raw/sources/Yu 等 - 2021 - Cross-Domain Slot Filling as Machine Reading Comprehension.pdf`
- Year: 2021
- Pages: 7
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- With task-oriented dialogue systems being widely
- component of task-oriented dialogue systems, is re-
- (MRC) problem. Our approach firstly transforms beling framework, slot labels are annotated in “BIO” format: “B”
- helpful for the detection of domain-specific slots.

## Method
- adopt sequence labeling framework, which, how- r_n r_n
- framing it as a machine reading comprehension work and reading comprehension framework. In the sequence la-
- (MRC) problem. Our approach firstly transforms beling framework, slot labels are annotated in “BIO” format: “B”
- reading comprehension framework, each slot type corresponds to
- for pre-training, which further alleviates the data

## Data and Evaluation Setup
- f19120432, jianliu, chenyf, jaxu, yjzhangg@bjtu.edu.cn
- In addition, we utilize the large-scale MRC dataset i
- scarcity problem. Experimental results on SNIPS “party size description”, respectively
- and ATIS datasets show that our approach con-
- datasets are required. However, slot filling faces the rapid

## Results and Claims
- f19120432, jianliu, chenyf, jaxu, yjzhangg@bjtu.edu.cn
- sistently outperforms the existing state-of-the-art
- completely new slot types (unseen slots), their performances
- would degrade significantly (As seen in our experiments of
- dataset, our approach achieves performance gains over cur- ferent domains, such models can not handle unseen slots.

## Limitations and Follow-ups
- There are mainly two challenges in cross-domain slot filling a BERT-based question-answering process to bridge MRC
- troduce extra noises caused by grammar errors. To wipe
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, retrieval, llm-reasoning, multimodal, dialogue, emotion-recognition, benchmark, graph
- Mentioned datasets: ATIS, SNIPS, TOP
- Mentioned metrics: f1, f1-score

## Benchmark Evidence Lines
- f19120432, jianliu, chenyf, jaxu, yjzhangg@bjtu.edu.cn
- In addition, we utilize the large-scale MRC dataset i
- and ATIS datasets show that our approach con-
- sistently outperforms the existing state-of-the-art
- datasets are required. However, slot filling faces the rapid
- scale MRC dataset for pre-training. Compared with the tra- labeled data to learn contextual embedding, i.e., ELMo [Pe-
- make full use of large-scale MRC datasets to learn semantic mains have different slot types, common slots such as “date”,
- tensive experiments on two benchmark datasets. For SNIPS While TF approaches can share knowledge learned on dif-

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
