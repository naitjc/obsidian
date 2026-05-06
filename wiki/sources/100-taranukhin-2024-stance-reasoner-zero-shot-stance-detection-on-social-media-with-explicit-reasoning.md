---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, llm-reasoning, zero-shot, few-shot, prompting, synthetic-data, retrieval, cross-lingual, conversational, target-adaptive]
sources: [raw/sources/Taranukhin 等 - 2024 - Stance Reasoner Zero-Shot Stance Detection on Social Media with Explicit Reasoning.pdf]
---

# Taranukhin 等 - 2024 - Stance Reasoner Zero-Shot Stance Detection on Social Media with Explicit Reasoning

## Metadata
- Source file: `raw/sources/Taranukhin 等 - 2024 - Stance Reasoner Zero-Shot Stance Detection on Social Media with Explicit Reasoning.pdf`
- Year: 2024
- Pages: 16
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Social media platforms are rich sources of opinionated content. Stance detection allows the automatic extraction of
- users’ opinions on various topics from such content. We focus on zero-shot stance detection, where the model’s
- be employed for new topics. We present Stance Reasoner, an approach to zero-shot stance detection on social media
- Keywords: stance detection, reasoning, social media

## Method
- users’ opinions on various topics from such content. We focus on zero-shot stance detection, where the model’s
- success relies on (a) having knowledge about the target topic; and (b) learning general reasoning strategies that can
- that leverages explicit reasoning over background knowledge to guide the model’s inference about the document’s
- stance on a target. Specifically, our method uses a pre-trained language model as a source of world knowledge,
- with the chain-of-thought in-context learning approach to generate intermediate reasoning steps. Stance Reasoner

## Data and Evaluation Setup
- users’ opinions on various topics from such content. We focus on zero-shot stance detection, where the model’s
- be employed for new topics. We present Stance Reasoner, an approach to zero-shot stance detection on social media
- outperforms the current state-of-the-art models on 3 Twitter datasets, including fully supervised models. It can bet-
- lenging variant of the task, zero-shot stance detec-
- The concept of model generalization in zero-shot

## Results and Claims
- outperforms the current state-of-the-art models on 3 Twitter datasets, including fully supervised models. It can bet-
- ond, even models that incorporate knowledge from • We demonstrate that our method outperforms
- external knowledge bases (KBs) may struggle from the current state-of-the-art models on 3 Twitter
- to subpar performance (Ma et al., 2019). Lastly, and it can better generalize across targets,
- document’s stance on a target. To achieve this,

## Limitations and Follow-ups
- our method can be used to detect annotation errors
- generate multiple paraphrases of manually defined
- additional context, or due to annotation errors. We
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, cross-lingual, conversational, target-adaptive
- Mentioned datasets: SemEval, WT-WT, ARC, Twitter
- Mentioned metrics: accuracy, precision

## Abstract (Extracted)
> Social media platforms are rich sources of opinionated content. Stance detection allows the automatic extraction of users’ opinions on various topics from such content. We focus on zero-shot stance detection, where the model’s success relies on (a) having know

## Benchmark Evidence Lines
- Zero-Shot Stance Detection on Social Media
- users’ opinions on various topics from such content. We focus on zero-shot stance detection, where the model’s
- be employed for new topics. We present Stance Reasoner, an approach to zero-shot stance detection on social media
- outperforms the current state-of-the-art models on 3 Twitter datasets, including fully supervised models. It can bet-
- ter generalize across targets, while at the same time providing explicit and interpretable explanations for its predictions.
- lenging variant of the task, zero-shot stance detec-
- The concept of model generalization in zero-shot
- 1We use the term “zero-shot” to describe the evalu- Previous approaches to zero-shot stance detec-

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[sentiment-analysis]]
