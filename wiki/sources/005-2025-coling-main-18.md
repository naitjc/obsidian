---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, multimodal, emotion-recognition, zero-shot, few-shot, retrieval, benchmark, graph]
sources: [raw/sources/2025.coling-main.18.pdf]
---

# 2025.coling-main.18

## Metadata
- Source file: `raw/sources/2025.coling-main.18.pdf`
- Year: 2025
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- effectively alleviates the overfitting problem of
- nition datasets demonstrate that the proposed
- problem of over-smoothing of nodes. Furthermore,
- tures in emotion recognition tasks as a continuous has become a key issue (Ai et al., 2024e).

## Method
- Dynamic Graph Neural Ordinary Differential Equation Network for
- 2024b,a; Yin et al.) to effectively model the con-
- information diffusion on the graph and alleviate the
- static images. How to model the temporal fea- stand the emotional information in multimodal data
- and model the complex patterns of emotion chang- works (RNNs) to model conversations, which

## Data and Evaluation Setup
- nition datasets demonstrate that the proposed
- datasets to verify the effectiveness of DGODE. sations through a self-attention mechanism. SDT
- Happy Sad Neutral Angry Excited Frustrated W-F1 Neutral Surprise Fear Sadness Joy Disgust Anger W-F1
- Table 1: Comparison with other baselines on the IEMOCAP and MELD dataset.
- where p contains the model’s predicted probability 5.1 Datasets and Evaluation Metrics

## Results and Claims
- use GCN to improve performance, but exist- 64
- to improve the generalization ability of GCNs
- (MERC) technology significantly improves the ac-
- can not only improve the intelligence of human-
- Figure 1: Performance comparison of different methods

## Limitations and Follow-ups
- ing over time remains a challenge. Therefore, this mainly capture emotional information by process-
- faces some challenges, especially in the recognition
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, retrieval, llm-reasoning, multimodal, dialogue, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: MELD, IEMOCAP, ATIS, TOP
- Mentioned metrics: accuracy, f1

## Abstract (Extracted)
> 72 Multimodal emotion recognition in conversa- tion (MERC) refers to identifying and classi- 70 fying human emotional states by combining 68 data from multiple different modalities (e.g., audio, images, text, video, etc.). Most exist- 66 ing multimodal emotion recognition methods

## Benchmark Evidence Lines
- nition datasets demonstrate that the proposed
- changes. DGODE shows stable performance as 2023). For example, CTNet (Lian et al., 2021) uses
- datasets to verify the effectiveness of DGODE. sations through a self-attention mechanism. SDT
- time and are suitable for complex tasks involving cally, consider an input data x(t) and describe its
- Happy Sad Neutral Angry Excited Frustrated W-F1 Neutral Surprise Fear Sadness Joy Disgust Anger W-F1
- Table 1: Comparison with other baselines on the IEMOCAP and MELD dataset.
- where p contains the model’s predicted probability 5.1 Datasets and Evaluation Metrics
- We used two used MERC datasets in our experi-

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
