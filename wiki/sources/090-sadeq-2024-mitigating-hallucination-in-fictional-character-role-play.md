---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, role-playing, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Sadeq 等 - 2024 - Mitigating Hallucination in Fictional Character Role-Play.pdf]
---

# Sadeq 等 - 2024 - Mitigating Hallucination in Fictional Character Role-Play

## Metadata
- Source file: `raw/sources/Sadeq 等 - 2024 - Mitigating Hallucination in Fictional Character Role-Play.pdf`
- Year: 2024
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- ter role-play. We introduce a dataset with over
- The code and the dataset are available at https:
- //github.com/NafisSadeq/rolefact.git. Hallucination remains a challenge for most
- retrieval augmented generation (RAG) (Karpukhin

## Method
- cision of generated responses by 18% for adver- the role-playing agent often hallucinates when
- retrieval augmented generation (RAG) (Karpukhin
- 2018), text classification (Wang et al., 2018), nat- language models (Shuster et al., 2021), it can-
- et al., 2020; Bubeck et al., 2023), prompting the base (Asai et al., 2023). Learning to improve char-
- agent level tasks such human simulacra (Park et al., are verifiable by a story-specific script serves as a

## Data and Evaluation Setup
- metric world knowledge of large language mod-
- ter role-play. We introduce a dataset with over
- confidence threshold. Experiments show that 2024a), Gemini (Google, 2024), Llama-3 (Meta,
- The code and the dataset are available at https:
- 2021), etc. has improved significantly (Brown tem are supported by a non-parametric knowledge

## Results and Claims
- the proposed method improves the factual pre- 2024) demonstrate some role-playing capabilities,
- The performance of LLMs on simple downstream et al., 2020; Lewis et al., 2020) may mitigate some
- 2021), etc. has improved significantly (Brown tem are supported by a non-parametric knowledge
- et al., 2020; Bubeck et al., 2023), prompting the base (Asai et al., 2023). Learning to improve char-
- role-play. One approach to achieve this is to strictly

## Limitations and Follow-ups
- Mitigating Hallucination in Fictional Character Role-Play
- mitigation of hallucination in fictional charac-
- Figure 1: Example of cross-universe hallucination (Hic-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: ATIS, MASSIVE, TOP, Persona
- Mentioned metrics: precision

## Benchmark Evidence Lines
- In this work, we focus on the evaluation and
- ter role-play. We introduce a dataset with over
- The code and the dataset are available at https:
- role-play is the lack of a suitable dataset. The lack
- of a dataset forces researchers to rely on a rating-
- based evaluation of hallucination (Shao et al., 2023;
- datasets in the role-play domain are insufficient
- • We release a dataset for Script Grounded Char-

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
