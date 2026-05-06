---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark]
sources: [raw/sources/Lin 等 - 2024 - Generate then Refine Data Augmentation for Zero-shot Intent Detection.pdf]
---

# Lin 等 - 2024 - Generate then Refine Data Augmentation for Zero-shot Intent Detection

## Metadata
- Source file: `raw/sources/Lin 等 - 2024 - Generate then Refine Data Augmentation for Zero-shot Intent Detection.pdf`
- Year: 2024
- Pages: 9
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Generate then Refine: Data Augmentation for Zero-shot Intent Detection
- mentation method for intent detection in zero-
- mains and then applied to unseen domains. We ances for out-of-domain intent detection.
- evaluate our method by training an intent classi-

## Method
- guage model in a zero-shot setting. Second, we
- evaluate our method by training an intent classi-
- of a generative LLM in zero-shot setting and a training data. This is achieved by direct utilization
- smaller sequence-to-sequence model can pro- of a generative large language model (LLM) as a
- oriented dialogue (TOD) systems. Its objective on model performance. As a remedy, several works

## Data and Evaluation Setup
- enhance the performance of the intent classifier; formula-based metric, we opt for a potentially more
- metrics for data selection to filter sub-optimal ut-
- prior work has applied metric-based meta-learning domains, it is applied to LLM-generated utterances
- labeled dataset. We ensure that the length of the
- generated set matches that of our labeled dataset,

## Results and Claims
- (the Refiner), to improve the generated utter-
- nificantly improves the data utility and diversity
- of a generative LLM in zero-shot setting and a training data. This is achieved by direct utilization
- oriented dialogue (TOD) systems. Its objective on model performance. As a remedy, several works
- vent of transformer-based models has significantly Meng et al., 2022; Lin et al., 2023).

## Limitations and Follow-ups
- tents, a considerable challenge emerges, primarily ing). Our goal is to create high-quality training data
- Addressing this challenge involves maximizing domains. In these unseen domains, the intent labels
- utterances into better ones. The goal of our Refiner increases the challenge for LLMs to provide high-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, role-playing, emotion-recognition, benchmark
- Mentioned datasets: SGD, TOP, Persona
- Mentioned metrics: accuracy

## Benchmark Evidence Lines
- We assume the labeled dataset D = (u , y ) y
- compared to state-of-the-art data augmenta-
- labeled dataset. We ensure that the length of the
- generated set matches that of our labeled dataset,
- some domains from seen domains as validation set, ers derived from the datasets.
- fine-tuned with the labeled dataset D and is used to 7 during both training and inference. This includes
- Datasets. We use the CLINC150 (Larson et al., Evaluation. The main criterion for the generated
- 2019) and SGD (Rastogi et al., 2020) datasets for utterances is utility: to what extent can the same

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
