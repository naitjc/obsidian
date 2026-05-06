---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, multimodal, sarcasm, zero-shot, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Jana 等 - 2024 - Continuous Attentive Multimodal Prompt Tuning for Few-Shot Multimodal Sarcasm Detection.pdf]
---

# Jana 等 - 2024 - Continuous Attentive Multimodal Prompt Tuning for Few-Shot Multimodal Sarcasm Detection

## Metadata
- Source file: `raw/sources/Jana 等 - 2024 - Continuous Attentive Multimodal Prompt Tuning for Few-Shot Multimodal Sarcasm Detection.pdf`
- Year: 2024
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- search communities. Existing studies depend sarcasm detection (Cai et al., 2019; Pan et al.,
- et al., 2023) suffer from some major challenges.
- datasets to achieve good performance. However,
- out-of-distribution (OOD) data. To address these datasets are difficult to obtain, and annota-

## Method
- Continuous Attentive Multimodal Prompt Tuning for Few-Shot Multimodal
- These models primarily rely on large annotated
- these issues, we propose Continuous Attentive tion is expensive and highly challenging due to
- Multimodal Prompt Tuning model (CAMP), socio-cultural and contextual dependencies (Rock-
- that leverages the prompt tuning paradigm to well and Theriot, 2001; Ivanko and Pexman, 2003;

## Data and Evaluation Setup
- datasets to achieve good performance. However,
- out-of-distribution (OOD) data. To address these datasets are difficult to obtain, and annota-
- input modalities. Experimental results indi- timodal models, they tend to overfit on in-domain
- Second, training all model weights increases pa- over strong multimodal baselines in a few-
- ability to better learn the continuous prompt tokens 2019) released a new image-text dataset based

## Results and Claims
- datasets to achieve good performance. However,
- data causing a reduction in performance for out-of-
- munities. Multiple modalities provide a crucial yields sub-optimal performance. Changes in token
- the vanilla Prompt Tuning approach, a significant 2016; Zhang et al., 2016; Poria et al., 2016; Ghosh
- ducing attentive mechanisms, thereby significantly late fusion method to combine the two modalities.

## Limitations and Follow-ups
- et al., 2023) suffer from some major challenges.
- dia platforms, multimodal sarcasm detection has main challenges. First, finding the right prompt
- limitation arises from the frozen nature of the pre- et al., 2017; Agrawal and An, 2018; Agrawal et al.,
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: ATIS, TOP, Persona
- Mentioned metrics: accuracy, acc, macro-f1, f1

## Benchmark Evidence Lines
- datasets to achieve good performance. However,
- out-of-distribution (OOD) data. To address these datasets are difficult to obtain, and annota-
- cate that our method outperforms other mul-
- ting and OOD scenarios. Our few-shot dataset
- ability to better learn the continuous prompt tokens 2019) released a new image-text dataset based
- state-of-the-art results in few-shot multimodal sar-
- 3. Our extensive experiments on two benchmark modal contrast between image and text to identify
- datasets showcase our model’s superiority sarcasm.

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
