---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Liu 等 - 2022 - Cross-Domain Slot Filling as Machine Reading Comprehension A New Perspective.pdf]
---

# Liu 等 - 2022 - Cross-Domain Slot Filling as Machine Reading Comprehension A New Perspective

## Metadata
- Source file: `raw/sources/Liu 等 - 2022 - Cross-Domain Slot Filling as Machine Reading Comprehension A New Perspective.pdf`
- Year: 2022
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- learning for a target domain remains a challenge. In contrast to and labor-intensive. Furthermore, approaches based on this
- machine reading comprehension (MRC) problem for the first
- more, we devise a dynamic question generation approach that
- We conducted extensive experiments on four datasets to evaluate require a lot of domain knowledge for model designation. Fur-

## Method
- and more important in our daily lives, slot filling, one of the ing paradigm, in which training and evaluation are limited
- prior methods that supplemented a sequence labeling model with paradigm are typically unable to address the practical situ-
- answering process. In the framework above, we present both mentioned limitations, researchers have begun to investigate
- to a single-domain learning model, such as slot descriptions
- we construct a pre-training and fine-tuning training approach

## Data and Evaluation Setup
- and more important in our daily lives, slot filling, one of the ing paradigm, in which training and evaluation are limited
- We conducted extensive experiments on four datasets to evaluate require a lot of domain knowledge for model designation. Fur-
- our approach, and the experimental results clearly justified the thermore, previous methods assume that the source and target
- MRC dataset (e.g., SQuAD [22]) to improve learning. The data
- model is first trained on external MRC datasets to gain generic Fig. 1. Comparison of the views of sequence labeling and MRC for

## Results and Claims
- complimentary effects in diverse cross-domain contexts. Further- various domains in order to improve learning [15]–[18]. Previ-
- that enables us to improve learning by utilizing MRC’s resources. [15], [17], slot examples [15], and so on [16], but they still
- T HROUGH natural language interfaces, intelligent dialogue edge, but has significant advantages over previous cross-domain
- MRC dataset (e.g., SQuAD [22]) to improve learning. The data
- F1 over current state-of-the-art methods in a common zero- in order to complete the task. The most popular approach for

## Limitations and Follow-ups
- learning for a target domain remains a challenge. In contrast to and labor-intensive. Furthermore, approaches based on this
- answering process. In the framework above, we present both mentioned limitations, researchers have begun to investigate
- cross-domain adaptation methods. the labeling bias issue; [37] propose a model to capture the
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: ATIS, SNIPS, MultiWOZ, SGD, DSTC, TOP, Persona
- Mentioned metrics: f1

## Benchmark Evidence Lines
- and more important in our daily lives, slot filling, one of the ing paradigm, in which training and evaluation are limited
- We conducted extensive experiments on four datasets to evaluate require a lot of domain knowledge for model designation. Fur-
- in accomplishing certain tasks, such as reserving a table at
- user request “I’d like to book a table at Hat Restaurant for
- MRC dataset (e.g., SQuAD [22]) to improve learning. The data
- model is first trained on external MRC datasets to gain generic Fig. 1. Comparison of the views of sequence labeling and MRC for
- We conducted extensive experiments on four benchmarks
- F1 over current state-of-the-art methods in a common zero- in order to complete the task. The most popular approach for

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
