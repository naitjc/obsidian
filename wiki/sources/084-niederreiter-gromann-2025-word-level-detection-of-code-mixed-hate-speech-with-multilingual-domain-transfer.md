---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, cross-lingual, benchmark, retrieval, prompting]
sources: [raw/sources/Niederreiter和Gromann - 2025 - Word-Level Detection of Code-Mixed Hate Speech with Multilingual Domain Transfer.pdf]
---

# Niederreiter和Gromann - 2025 - Word-Level Detection of Code-Mixed Hate Speech with Multilingual Domain Transfer

## Metadata
- Source file: `raw/sources/Niederreiter和Gromann - 2025 - Word-Level Detection of Code-Mixed Hate Speech with Multilingual Domain Transfer.pdf`
- Year: 2025
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Ever-growingoffensiveonlinecontentscanneg- In combination with profane language, the com- atively impact humans (Nozza and Hovy, 2023; plexity of the hate speech detection task is con- Jagdaleetal.,2024),whichcanbeaddressedwith siderably increased by code-mixing.
- the hate speech label is assigned to entire sen- To address this limitation, we contribute tences.
- They use the Hate Speech and Offensive EnglishraplyricsdatasetfromtheGermanrapdo- Content Identification (HASOC) dataset (Modha main.

## Method
- However,profanelanguage English Holyshitman,Igotheadlast tends to contain code-mixing, a combination of more than one language, which requires a night morenuanceddetectionapproachthanbinary [‘B-B’, ‘B’, ‘n’, ‘n’, ‘n’, ‘B- classification.
- Thischallengehasbeenaddressed tilingual methods (Nkemelu et al., 2022; Nozza withapproachestosyntheticallycreatecode-mixed and Hovy, 2023).
- A similar comparison that as well as across domains, which is compared to also included neural networks was performed by thezero-shotperformanceofstate-of-the-artLarge DhanyaandBalakrishnan(2024)onacode-mixed Language Models (LLMs).
- Although the size of Malayalam-Englishdataset,findingwithlittlesur- theproposeddatasetsiscomparativelylimited,this prisethatneuralnetworksoutperformedstatistical papercontributesareal-worldbenchmarkonmul- machinelearningmodels.

## Data and Evaluation Setup
- Agenerallackofavailablecode- B’,‘B’,‘n’,‘n’] mixeddatasetsaggravatestheproblem.
- One growing challenge in lan- datasets(e.g.Salaametal.,2022).
- However,such guagedetectiontasksiscode-mixing(Aguilaretal., datasetsmightnotaccuratelyrepresentthehuman 21093 FindingsoftheAssociationforComputationalLinguistics:ACL2025,pages21093–21104 July27-August1,2025©2025AssociationforComputationalLinguistics tendencytodynamicallycreatenovelprofanities.
- They use the Hate Speech and Offensive EnglishraplyricsdatasetfromtheGermanrapdo- Content Identification (HASOC) dataset (Modha main.

## Results and Claims
- A similar comparison that as well as across domains, which is compared to also included neural networks was performed by thezero-shotperformanceofstate-of-the-artLarge DhanyaandBalakrishnan(2024)onacode-mixed Language Models (LLMs).
- Although the size of Malayalam-Englishdataset,findingwithlittlesur- theproposeddatasetsiscomparativelylimited,this prisethatneuralnetworksoutperformedstatistical papercontributesareal-worldbenchmarkonmul- machinelearningmodels.
- Con- model(DEFT)improvesitsabilitytogeneralizeto sequently,itisessentialtotestthemodels’gener- German-English code-mixed hate speech.

## Limitations and Follow-ups
- Thischallengehasbeenaddressed tilingual methods (Nkemelu et al., 2022; Nozza withapproachestosyntheticallycreatecode-mixed and Hovy, 2023).
- One growing challenge in lan- datasets(e.g.Salaametal.,2022).
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: retrieval, prompting, cross-lingual
- Mentioned datasets: gab, twitter, reddit
- Mentioned metrics: f1, precision, recall

## Abstract (Extracted)
> Abstract Dataset InputandOutput German Hurensohn manchmal denk Theexponentialgrowthofoffensivelanguage ichmireinfachnurfickdich on social media tends to fuel online harass- [‘B-B’, ‘n’, ‘n’, ‘n’, ‘n’, ‘n’, ment and challenges detection mechanisms. ‘n’,‘B-B’,‘B’](Sonofabitch, Hatespeechdetectioniscommonlytreatedas sometimes I just think fuck a monolingual or multilingual sentence-level you) classificationtask. However,profanelanguage English Holyshitman,Igotheadlast tends to contain code-mixing, a combination of more than one language, which requires a night morenuanceddetectionapproachthanbinary [‘B-B’, ‘B’, ‘n’, ‘n’, ‘n’, ‘B- classification. Agenerallackofavailablecode- B’,‘B’,‘n’,‘n’] mixeddatasetsaggravatestheproblem. Toad- Code-Mixed Ah , was ist das für ein dress this issue, we propose five word-level Muschibattle annotated hate speech datasets, EN and DE [‘n’,‘n’,‘n’,‘n’,‘n’,‘n’,‘n’, fromsocialnetworks,onesubsetoftheDE-EN ‘B-B’](Ah,whatapussybattle Offensive Content Detection Code-Switched Dataset,oneDE-ENcode-mixedGermanrap isthis) lyricsheld-outtestset,andacross-domainheld- C

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-datasets-and-benchmarks]]
