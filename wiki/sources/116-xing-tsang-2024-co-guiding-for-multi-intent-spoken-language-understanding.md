---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, zero-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Xing和Tsang - 2024 - Co-Guiding for Multi-Intent Spoken Language Understanding.pdf]
---

# Xing和Tsang - 2024 - Co-Guiding for Multi-Intent Spoken Language Understanding

## Metadata
- Source file: `raw/sources/Xing和Tsang - 2024 - Co-Guiding for Multi-Intent Spoken Language Understanding.pdf`
- Year: 2024
- Pages: 16
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- achieving the mutual guidances between the two tasks. In the first
- stage, the initial estimated labels of both tasks are produced, and
- propose Co-guiding-SCL Net, which exploits the single-task and Fig. 1. (a) Previous framework which only models the unidirectional guidance
- dual-task semantics contrastive relations. For the first stage, we from multi-intent predictions to slot filling. (b) Our framework which models

## Method
- Abstract—Recent graph-based models for multi-intent SLU have
- obtained promising results through modeling the guidance from the
- methods (1) only model the unidirectional guidance from intent to
- and slot; (2) adopt homogeneous graphs to model the interactions
- limit the performance. In this paper, we propose a novel model

## Data and Evaluation Setup
- learning procedure. Experiment results on multi-intent SLU show
- model on MixATIS dataset in overall accuracy. We also evaluate our
- by 33.5% on average in terms of overall accuracy for the total 9 Recently, researchers discovered that these two tasks are
- slot (red) labels. The sample is retrieved from MixSNIPS dataset.
- regarding not only the own task’s contrastive labels but also Co-guiding-SCL Net. Experimental results are reported and

## Results and Claims
- limit the performance. In this paper, we propose a novel model
- that our model outperforms existing models by a large margin, includes two subtasks: intent detection and slot filling [2]. Intent
- obtaining a relative improvement of 21.3% over the previous best detection aims to predict the intention of the user utterance and
- model on MixATIS dataset in overall accuracy. We also evaluate our
- that our model can relatively improve the state-of-the-art model

## Limitations and Follow-ups
- Fig. 10. Case study of slot-to-intent guidance (a) and intent-to-slot guidance (b). Red color denotes error.
- moving anyone of IntentSCL and SlotSCL leads to the decreases while there is an error in the predicted slots. In the second
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: ATIS, SNIPS, Persona
- Mentioned metrics: accuracy, acc, f1

## Benchmark Evidence Lines
- that our model outperforms existing models by a large margin, includes two subtasks: intent detection and slot filling [2]. Intent
- model on MixATIS dataset in overall accuracy. We also evaluate our
- that our model can relatively improve the state-of-the-art model
- by 33.5% on average in terms of overall accuracy for the total 9 Recently, researchers discovered that these two tasks are
- by A * STAR Centre for Frontier AI Research. Recommended for acceptance slot hidden states, obtaining state-of-the-art results and signifi-
- slot (red) labels. The sample is retrieved from MixSNIPS dataset.
- datasets show that our Co-guiding Net significantly out- intent, which may not be practical in real-world scenarios, where
- dynamic and fine-grained correlations between the multi- the state-of-the-art performance.

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
