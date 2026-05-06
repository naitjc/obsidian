---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, multimodal, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, conversational, target-adaptive, bias]
sources: [raw/sources/Liang 等 - 2024 - Multi-modal Stance Detection New Datasets and Model.pdf]
---

# Liang 等 - 2024 - Multi-modal Stance Detection New Datasets and Model

## Metadata
- Source file: `raw/sources/Liang 等 - 2024 - Multi-modal Stance Detection New Datasets and Model.pdf`
- Year: 2024
- Pages: 15
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Multi-modal Stance Detection: New Datasets and Model
- Abstract Target: Donald Trump Stance: Against
- Stance detection is a challenging task that aims Text: It is exactly what I want to say!!!
- vious work on stance detection largely focused

## Method
- Multi-modal Stance Detection: New Datasets and Model
- modal stance detection, we create five new datasets, Prompt Tuning Prompting (Liu et al., 2021a)
- and an image. These datasets contain a total of tions for pre-trained language models (PLMs) to
- To deal with multi-modal stance detection, we treat prompts as continuous vectors and optimize
- propose a simple yet effective Targeted Multi- them during fine-tuning, called Prompt Tuning (Li

## Data and Evaluation Setup
- Multi-modal Stance Detection: New Datasets and Model
- tection datasets of different domains based on
- modal stance detection, we create five new datasets, Prompt Tuning Prompting (Liu et al., 2021a)
- and an image. These datasets contain a total of tions for pre-trained language models (PLMs) to
- modalities. Then, the targeted prompts are fed to 3 Multi-modal Stance Detection Datasets

## Results and Claims
- achieves state-of-the-art performance in multi-
- that the proposed method significantly outperforms
- tion. In the MWTWT dataset, following (Conforti We use Macro F1-score to measure the model per-
- 3) KEBERT (Kawintiranon and Singh, 2022), a proposed TMPT outperforms fine-tuning based base-
- thus improving stance detection performance. Fur-

## Limitations and Follow-ups
- detection, which is also the main challenge of multi-
- sual prompt tuning proposed by (Jia et al., 2022), and bV ∈ R dh are biases. ∈
- input image for learning visual stance features on and bias respectively.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, conversational, target-adaptive, bias
- Mentioned datasets: SemEval, ARC, MTS, Twitter
- Mentioned metrics: macro f1, f1, f1-score

## Benchmark Evidence Lines
- achieves state-of-the-art performance in multi-
- that the proposed method significantly outperforms
- on the task of zero-shot stance detection2(Liu et al., 3.2 Data Annotation
- Table 1: Label distribution of the five multi-modal stance detection datasets.
- Table 2: The statistics of whether the image conveys
- guidelines are shown in Appendix B. The mean- ported in Table 1. Note that differences in label
- the three annotators, we invited three additional an- shown in Table 2. It can be seen that nearly half
- Table 3: The example of textual targeted prompts.

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
- [[sentiment-analysis]]
