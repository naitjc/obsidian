---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, synthetic-data, retrieval, cross-lingual, conversational, bias]
sources: [raw/sources/Li和Zhang - 2024 - Pro-Woman, Anti-Man Identifying Gender Bias in Stance Detection.pdf]
---

# Li和Zhang - 2024 - Pro-Woman, Anti-Man Identifying Gender Bias in Stance Detection

## Metadata
- Source file: `raw/sources/Li和Zhang - 2024 - Pro-Woman, Anti-Man Identifying Gender Bias in Stance Detection.pdf`
- Year: 2024
- Pages: 8
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Pro-Woman, Anti-Man? Identifying Gender Bias in Stance Detection
- detection, determining whether models consis- result in low robustness in stance detection models.
- et al., 2019; Sun et al., 2019; Blodgett et al., 2020; how it arises in stance detection, we construct a
- cilia and Alikhani, 2023) and machine translation nouns as Against and label those with female nouns

## Method
- models, which has the potential to perpetuate
- detection, determining whether models consis- result in low robustness in stance detection models.
- lar gender group. We find that all models are
- foundation model itself. detection systems tend to associate the stance la-
- models has been recently identified as a major con- decision-making.

## Data and Evaluation Setup
- paper, we construct a dataset GenderStance of datasets inevitably inherit the biases of their anno-
- 36k samples to measure gender bias in stance tators and overfitting on these dataset biases can
- tently predict the same stance for a particu- Kaushal et al. (2021) identify the dataset biases as
- sive experiments indicate that sources of gen- not taken gender bias into consideration. As com-
- Stan´czak and Augenstein, 2021; Thakur et al., challenging dataset, GenderStance, to explore the

## Results and Claims
- et al., 2018; Zhao et al., 2018; Cao and Daumé III, state-of-the-art models (Allaway and McKeown,
- this tendency on F1 measure. An unbiased model
- We calculate the F1 for each class and adopt the pair for classification. KASD (Li et al., 2023a)
- macro-average F1 of all classes as the evalua- employs the RoBERTa as the encoding module
- average F1 between genders, defined as In addition, GPT-3.5 (Zhang et al., 2023) and GPT-

## Limitations and Follow-ups
- Pro-Woman, Anti-Man? Identifying Gender Bias in Stance Detection
- Abstract studies showing presence of systematic gender bias
- harmful stereotypes and discrimination. In this
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, synthetic-data, retrieval, llm-reasoning, cross-lingual, conversational, bias
- Mentioned datasets: SemEval, VAST, P-Stance, ARC
- Mentioned metrics: f1

## Abstract (Extracted)
> studies showing presence of systematic gender bias in prolifically applied NLP methods, little attention Gender bias has been widely observed in NLP has been paid to the role of gender in stance detec- models, which has the potential to perpetuate tion. Schill

## Benchmark Evidence Lines
- et al., 2018; Zhao et al., 2018; Cao and Daumé III, state-of-the-art models (Allaway and McKeown,
- Table 1: The list of categories used in GenderStance.
- Ds= (xs, ts, ys) Ns and two gender evaluation Table 2: Examples of noun phrases representing the
- nology. The complete domain list is shown in Table
- of which are shown in Table 2, [TOPIC] repre- × ×
- Table 4: Statistics of VAST and SemEval-2016 datasets.
- ics (VAST) (Allaway and McKeown, 2020) and
- SemEval-2016 (Mohammad et al., 2016). VAST

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[sentiment-analysis]]
