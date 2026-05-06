---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, conversational, target-adaptive, bias, verification]
sources: [raw/sources/Ding 等 - 2025 - Zero-Shot Conversational Stance Detection Dataset and Approaches.pdf]
---

# Ding 等 - 2025 - Zero-Shot Conversational Stance Detection Dataset and Approaches

## Metadata
- Source file: `raw/sources/Ding 等 - 2025 - Zero-Shot Conversational Stance Detection Dataset and Approaches.pdf`
- Year: 2025
- Pages: 15
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Zero-Shot Conversational Stance Detection: Dataset and Approaches
- Stance detection, which aims to identify public tion (Zhang et al., 2020; Upadhyaya et al., 2023;
- tional stance detection has become a crucial re-
- stance detection datasets are restricted to a lim- Existing research on stance detection is typically

## Method
- the effectiveness of stance detection models categories for training and evaluating models, with
- ing the ZS-CSD dataset, we propose SITPCL, gage in conversations and express their views in the
- ical contrastive learning model, and establish Multi-party conversation understanding involves
- modeling process, only the reply relationship and
- ing the annotation and modeling process, without

## Data and Evaluation Setup
- Zero-Shot Conversational Stance Detection: Dataset and Approaches
- stance detection datasets are restricted to a lim- Existing research on stance detection is typically
- ited set of specific targets, which constrains divided into in-target, cross-target, and zero-shot
- quality zero-shot conversational stance detec-
- ing the ZS-CSD dataset, we propose SITPCL, gage in conversations and express their views in the

## Results and Claims
- the-art performance in zero-shot conversational
- attains only an F1-macro score of 43.81%, high- Currently, five conversational stance detection
- our proposed SITPCL model achieves state-of-the- threads—increasingly relevant. The SRQ dataset
- art performance in zero-shot conversational stance (Villa-Cox et al., 2020) pioneered stance detection
- performance is evaluated using the F1 score for the categories: favor, against, neutral, and the overall F1-macro.

## Limitations and Follow-ups
- this gap, we manually curate a large-scale, high-
- lighting the persistent challenges in zero-shot datasets have been developed, including SRQ
- Our new task challenges in two main aspects. First,
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, conversational, target-adaptive, bias, verification
- Mentioned datasets: SemEval, VAST, P-Stance, EZ-STANCE, WT-WT, ARC, Twitter, Reddit, Weibo
- Mentioned metrics: f1

## Benchmark Evidence Lines
- Zero-Shot Conversational Stance Detection: Dataset and Approaches
- ited set of specific targets, which constrains divided into in-target, cross-target, and zero-shot
- quality zero-shot conversational stance detec-
- the benchmark performance in the zero-shot
- the-art performance in zero-shot conversational
- attains only an F1-macro score of 43.81%, high- Currently, five conversational stance detection
- lighting the persistent challenges in zero-shot datasets have been developed, including SRQ
- of zero-shot conversational stance detection tasks

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
- [[sentiment-analysis]]
