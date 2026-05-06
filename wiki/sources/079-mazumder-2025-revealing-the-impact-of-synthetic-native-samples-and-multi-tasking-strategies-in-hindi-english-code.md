---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, synthetic-data, sentiment-analysis, sarcasm, cross-lingual, benchmark]
sources: [raw/sources/Mazumder 等 - 2025 - Revealing the impact of synthetic native samples and multi-tasking strategies in Hindi-English code-.pdf]
---

# Mazumder 等 - 2025 - Revealing the impact of synthetic native samples and multi-tasking strategies in Hindi-English code-

## Metadata
- Source file: `raw/sources/Mazumder 等 - 2025 - Revealing the impact of synthetic native samples and multi-tasking strategies in Hindi-English code-.pdf`
- Year: 2025
- Pages: 31
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Revealing the impact of synthetic native samples and multi-tasking
- ing, (ii) multi-task learning (MTL), and (iii) ous and sarcastic expression in Hindi-English code-
- (MLM hereafter) has shown a new path to address
- MLMs using native monolingual task samples (e.g.

## Method
- tried three approaches: (i) native sample mix- sented in the Appendix.
- in developing new models (Sitaram et al., 2019;
- evolution of multilingual large language models
- very effective if training and testing samples share 2020), Mu RIL (Khanuja et al., 2021) and In-

## Data and Evaluation Setup
- In this paper, we reported our experiments with
- very effective if training and testing samples share 2020), Mu RIL (Khanuja et al., 2021) and In-
- similar linguistic and cultural contexts, the training
- mixed training sets can improve code-mixed task

## Results and Claims
- we got are (i) adding native samples improved hain.
- humor (raising the F1-score up to 6.76%) and (Translation: Never take a moral high ground.
- sarcasm (raising the F1-score up to 8.64%) de- There are no railings and one can fall at any
- (raising the F1-score up to 10.67%) and sar- • Sarcasm: Kuch logo ka number iss liye save

## Limitations and Follow-ups
- and error analysis discovered the cases where
- No- to Figure 5 in Appendix F) and spelling errors.
- NLD : NHD m BERTMTL XLM-RMTL Mu RILMTL • The error analysis (refer Section 5) revealed
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, retrieval, prompting, benchmark, sentiment-analysis, llm-reasoning, sarcasm
- Mentioned datasets: ATIS, TOP
- Mentioned metrics: accuracy, acc, f1, precision, recall, em

## Abstract (Extracted)
> setting. This is because models now need to un- derstand humour and sarcasm in an utterance ex- In this paper, we reported our experiments with pressed through altering multiple languages. More various strategies to improve code-mixed hu- details on the phenomenon of code-mixing are pre- mour and sarcasm detection. Particularly, we tried three approaches: (i) native sample mix- sented in the Appendix. An example of humor- ing, (ii) multi-task learning (MTL), and (iii) ous and sarcastic expression in Hindi-English code- prompting and instruction finetuning very large mixed language is given in the following. More multilingual language models (VMLMs). In examples are presented in Figure 1 of Appendix native sample mixing, we added monolingual B. In the following example, the English parts are task samples to code-mixed training sets. In marked in red, and the Hindi parts are marked in MTL

## Related Concepts
- [[synthetic-data-generation]]
- [[sentiment-analysis]]
- [[sarcasm-detection]]
- [[zero-shot-learning]]
- [[llm-evaluation]]
- [[nlp-research-collection]]
