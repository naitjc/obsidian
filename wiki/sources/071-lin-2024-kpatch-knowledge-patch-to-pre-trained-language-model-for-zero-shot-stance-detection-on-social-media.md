---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, conversational, target-adaptive, bias]
sources: [raw/sources/Lin 等 - 2024 - KPatch Knowledge Patch to Pre-trained Language Model for Zero-Shot Stance Detection on Social Media.pdf]
---

# Lin 等 - 2024 - KPatch Knowledge Patch to Pre-trained Language Model for Zero-Shot Stance Detection on Social Media

## Metadata
- Source file: `raw/sources/Lin 等 - 2024 - KPatch Knowledge Patch to Pre-trained Language Model for Zero-Shot Stance Detection on Social Media.pdf`
- Year: 2024
- Pages: 13
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Zero-shot stance detection on social media (ZSSD-SM) aims to distinguish the attitude in tweets towards an unseen
- Keywords: Zero-Shot Stance Detection, Knowledge Graph, Knowledge Injection
- Zero-shot stance detection on social media (ZSSD-
- Favor, Against, or Neutral) expressed in tweets to-

## Method
- KPatch: Knowledge Patch to Pre-trained Language Model for
- semantics. In this paper, we propose a novel knowledge injection method for ZSSD-SM, which adopts two training
- model (PLM) and adaptively expand tweets context. Specifically, in the knowledge compression stage, the latent
- 1. Introduction alignment techniques to map external knowledge
- into the pre-trained language model (PLM) (Devlin

## Data and Evaluation Setup
- Zero-shot stance detection on social media (ZSSD-SM) aims to distinguish the attitude in tweets towards an unseen
- knowledge, and then complete the fine-tuning of the ZSSD-SM task. Extensive experiments on multiple datasets show
- Keywords: Zero-Shot Stance Detection, Knowledge Graph, Knowledge Injection
- Zero-shot stance detection on social media (ZSSD-
- that misses some entities because the NER did not 2.1. Zero-shot Stance Detection on

## Results and Claims
- lack of context knowledge hinders the detection performance. Recent studies have been devoted to obtaining the
- performance. However, these knowledge injection methods still suffer from two challenges: (i) The pipeline of
- (Chen et al., 2023) for ZSSD-SM task, and achieve
- achieves better performance against the base-
- effectively overcome the performance bottleneck

## Limitations and Follow-ups
- performance. However, these knowledge injection methods still suffer from two challenges: (i) The pipeline of
- knowledge injection causes error accumulation and (ii) irrelevant knowledge makes them fail to understand the
- error over time. Therefore, how to effectively
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, conversational, target-adaptive, bias
- Mentioned datasets: SemEval, ARC
- Mentioned metrics: f1, recall

## Benchmark Evidence Lines
- Zero-Shot Stance Detection on Social Media
- Zero-shot stance detection on social media (ZSSD-SM) aims to distinguish the attitude in tweets towards an unseen
- Keywords: Zero-Shot Stance Detection, Knowledge Graph, Knowledge Injection
- Zero-shot stance detection on social media (ZSSD-
- Data Topic: Climate Change is a Real Concern to adaptively select the most suitable knowl-
- that misses some entities because the NER did not 2.1. Zero-shot Stance Detection on
- The application of social media has made zero-shot
- learn to extract the most suitable knowledge for

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
- [[sentiment-analysis]]
