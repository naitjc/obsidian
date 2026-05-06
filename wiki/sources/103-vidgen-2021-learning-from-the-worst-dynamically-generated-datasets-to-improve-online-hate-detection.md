---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, cross-lingual, benchmark, retrieval, counterfactual, explainability]
sources: [raw/sources/Vidgen 等 - 2021 - Learning from the Worst Dynamically Generated Datasets to Improve Online Hate Detection.pdf]
---

# Vidgen 等 - 2021 - Learning from the Worst Dynamically Generated Datasets to Improve Online Hate Detection

## Metadata
- Source file: `raw/sources/Vidgen 等 - 2021 - Learning from the Worst Dynamically Generated Datasets to Improve Online Hate Detection.pdf`
- Year: 2021
- Pages: 16
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- In other datasets are formed with bootstrapped sampling, cases,falsenegativescanbeprovokedbychanging such as keyword searches, due to the low preva- the‘sensitive’attributeofhatefulcontent,suchas lence of hate speech ‘in the wild’ (Vidgen et al., changing the target from ‘gay’ to ‘black’ people 2019b).
- Subtle and implicit forms of hate speech positives and false negatives (Schmidt and Wie- canalsocreatefalsenegatives(VidgenandYasseri, gand,2017;Mishraetal.,2019;VidgenandDer- 2019;Palmeretal.,2020;Mathewetal.,2020),as czynski,2020;Ro¨ttgeretal.,2020;Mathewetal., well as more ‘complex’ forms of speech such as 2020).
- However, to date, these approaches Dehumanization Contentwhich‘perceiv[es]or remain under-explored for hate speech detection treat[s] people as less than human’ (Haslam and and to the best of our knowledge no prior work Stratemeyer, 2016).

## Method
- We then tasked annotators with presentingcontentthatwouldtrickthemodeland We present a human-and-model-in-the-loop yield misclassifications.
- At the end of the round process for dynamically generating datasets wetrainedanewmodelusingthenewlypresented and training better performing and more ro- data.
- In the next round the process was repeated busthatedetectionmodels.
- Weprovideanew dataset of ∼40,000 entries, generated and la- withthenewmodelintheloopfortheannotatorsto belled by trained annotators over four rounds trick.

## Data and Evaluation Setup
- Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection BertieVidgen†,TristanThrush‡,ZeerakWaseem(cid:63),DouweKiela‡ †TheAlanTuringInstitute;(cid:63)UniversityofSheffield;‡FacebookAIResearch bvidgen@turing.ac.uk Abstract speech datasets.
- At the end of the round process for dynamically generating datasets wetrainedanewmodelusingthenewlypresented and training better performing and more ro- data.
- Weprovideanew dataset of ∼40,000 entries, generated and la- withthenewmodelintheloopfortheannotatorsto belled by trained annotators over four rounds trick.
- Hateful entries make up 54% split into half original content and half pertur- of the dataset, which is substantially higher bations.

## Results and Claims
- Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection BertieVidgen†,TristanThrush‡,ZeerakWaseem(cid:63),DouweKiela‡ †TheAlanTuringInstitute;(cid:63)UniversityofSheffield;‡FacebookAIResearch bvidgen@turing.ac.uk Abstract speech datasets.
- The perturbations are challenging ‘con- thancomparabledatasets.Weshowthatmodel trastsets’,whichmanipulatetheoriginaltextjust performance is substantially improved using thisapproach.
- However,detectingon- improves(seeTable4).

## Limitations and Follow-ups
- Suchbootstrappingcansubstantiallybias (Garg et al., 2019).
- intheirdefinition,andZampierietal.(2019)who Another way of addressing the limitations of include‘insults’.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: retrieval, counterfactual, explainability, cross-lingual
- Mentioned datasets: gab, founta, twitter
- Mentioned metrics: f1, accuracy, recall

## Abstract (Extracted)
> Abstract speech datasets. We then tasked annotators with presentingcontentthatwouldtrickthemodeland We present a human-and-model-in-the-loop yield misclassifications. At the end of the round process for dynamically generating datasets wetrainedanewmodelusingthenewlypresented and training better performing and more ro- data. In the next round the process was repeated busthatedetectionmodels. Weprovideanew dataset of ∼40,000 entries, generated and la- withthenewmodelintheloopfortheannotatorsto belled by trained annotators over four rounds trick. Wehadfourroundsbutthisapproachcould, ofdynamicdatacreation. Itincludes∼15,000 inprinciple,becontinuedindefinitely. challengingperturbationsandeachhatefulen- Round 1 contains original content created syn- try has fine-grained labels for the type and thetically by annotators. Rounds 2, 3 and 4 are target of hate. Hateful entries make up 54% split into half original content and half pertur- of the dataset, which is substantially higher bations. The perturbations are challenging ‘con- thancomparabledatasets.Weshowthatmodel trastsets’,whichmanipulat

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
