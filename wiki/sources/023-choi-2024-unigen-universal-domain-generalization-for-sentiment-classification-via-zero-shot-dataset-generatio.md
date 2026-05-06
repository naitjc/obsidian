---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, zero-shot, few-shot, synthetic-data, prompting, sentiment-analysis, benchmark]
sources: [raw/sources/Choi 等 - 2024 - UniGen Universal Domain Generalization for Sentiment Classification via Zero-shot Dataset Generatio.pdf]
---

# Choi 等 - 2024 - UniGen Universal Domain Generalization for Sentiment Classification via Zero-shot Dataset Generatio

## Metadata
- Source file: `raw/sources/Choi 等 - 2024 - UniGen Universal Domain Generalization for Sentiment Classification via Zero-shot Dataset Generatio.pdf`
- Year: 2024
- Pages: 14
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Abstract However, the approaches proposed thus far have
- ators and a tiny task-specific model be trained primary limitation of the TAM-based approach
- task model to any domain that shares the label the costs of dataset generation and TAM training
- experiments indicate that the proposed method

## Method
- Abstract However, the approaches proposed thus far have
- ators and a tiny task-specific model be trained primary limitation of the TAM-based approach
- generates a dataset regardless of the target do- based approach because it requires many separately
- task model to any domain that shares the label the costs of dataset generation and TAM training

## Data and Evaluation Setup
- for Sentiment Classification via Zero-shot Dataset Generation
- Recent studies have TAM trained on these data has limited general-
- suggested that PLMs be used as dataset gener- ization ability across other domains.
- ators and a tiny task-specific model be trained primary limitation of the TAM-based approach

## Results and Claims
- As the size and performance of pre-trained lan- mains (Wang et al., 2022; Zhou et al., 2022).
- While scholars of single-domain generalization, which achieves
- low-cost inference compared to the case in which This allows TAMs to achieve domain generalizabil-
- Furthermore, because the PLM-based dataset gen- improve performance compared to PROMPTING.

## Limitations and Follow-ups
- Abstract However, the approaches proposed thus far have
- ators and a tiny task-specific model be trained primary limitation of the TAM-based approach
- task model to any domain that shares the label the costs of dataset generation and TAM training
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, synthetic-data, retrieval, prompting, benchmark, sentiment-analysis
- Mentioned datasets: MASSIVE, TOP, Amazon, Yelp, Twitter, SST, IMDB
- Mentioned metrics: acc, em

## Abstract (Extracted)
> However, the approaches proposed thus far have relied on domain-specific prompts, for example, Although pre-trained language models have “The movie review in positive sentiment is:.” Be- exhibited great flexibility and versatility with cause the data generated using this prompt are re- prompt-based few-shot learning, they suffer lated only to the domain of movie reviews, the from the extensive parameter size and limited applicability for inference. Recent studies have TAM trained on these data has limited general- suggested that PLMs be used as dataset gener- ization ability across other domains. This is the ators and a tiny task-specific model be trained primary limitation of the TAM-based approach to achieve efficient inference. However, their compared to prompt-based zero-shot learning that applicability to various domains is limited be- directly uses PLMs (PROMPTING), which allows ca

## Related Concepts
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[sentiment-analysis]]
- [[llm-evaluation]]
- [[nlp-research-collection]]
