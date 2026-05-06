---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, cross-lingual, benchmark]
sources: [raw/sources/Garibo i Orts - 2019 - Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter at SemEval-2019 Task 5.pdf]
---

# Garibo i Orts - 2019 - Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter at SemEval-2019 Task 5

## Metadata
- Source file: `raw/sources/Garibo i Orts - 2019 - Multilingual Detection of Hate Speech Against Immigrants and Women in Twitter at SemEval-2019 Task 5.pdf`
- Year: 2019
- Pages: 4
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- AuthorProfilingiswidelystud- resentation approach to the task of Multilin- ied and some new ideas arise from time to time gual Detection of Hate Speech Against Im- (Rangel et al., 2016).
- Hate Speech Detection against Im- speech can be addressed to individuals or groups migrants and Women: a two class classifica- duetotherace,sexuality,religionandsomeother tion where systems have to predict whether characteristics.
- (cid:88) C = TF ∀k ∈ K (3) k a a∈Ak to classify hateful tweets (e.g., tweets where Hate Speech against women or immigrants These vectors are then used to codify the texts.

## Method
- AuthorProfilingiswidelystud- resentation approach to the task of Multilin- ied and some new ideas arise from time to time gual Detection of Hate Speech Against Im- (Rangel et al., 2016).
- Ourapproachcon- chines with linear kernel.
- sisInterpolation(FAI)istheapproachweuse to achieve rank 5th in Spanish language and 2 Corpus 9th in English language in sub-task B in both cases.
- LinearSVCsup- priori class dependent probability for each term portvectormachinefromPythonsSklearnlibrary for each class simply by counting the number of is used to train the model and, of course, to pre- times a term occurs for each class, and dividing dicttheresults.

## Data and Evaluation Setup
- For each Social media has become a new standard of com- language, a training and an evaluation datasets municationsinthelastyears.
- Thecontentsofbothdatasets morepeopleactivelyparticipateinthecontentcre- areindividualtweets,thathavebeencollectedand ation, sometimes under the shield of anonymity.
- Agressive Behaviour and Target 1alt.qcri.org/semeval2019/ Classification: where systems are asked first Language Training Evaluation HS AG TR Label English 10,000 3,000 0 0 0 000 Spanish 5,000 1,600 1 0 0 100 1 0 1 101 Table1: Numberoftweetsperdataset.
- hasbeenidentified)asagressiveornotagres- Each word in the text is substituted by the a pri- sive, labeled as AG column in the datasets, ori probabilityfor each classin as manyarrays as and second to identify the target harassed as classes.

## Results and Claims
- AuthorProfilingiswidelystud- resentation approach to the task of Multilin- ied and some new ideas arise from time to time gual Detection of Hate Speech Against Im- (Rangel et al., 2016).
- Social media has become a complex communica- The goal of this task is to identify tweets which tion channel in which usually offensive contents contain hate against women and immigrants.
- Hate Speech Detection against Im- speech can be addressed to individuals or groups migrants and Women: a two class classifica- duetotherace,sexuality,religionandsomeother tion where systems have to predict whether characteristics.

## Limitations and Follow-ups
- As future work we think of exploring new configurations of our method.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: cross-lingual
- Mentioned datasets: twitter
- Mentioned metrics: f1, accuracy, precision

## Abstract (Extracted)
> Abstract goalisbuildingasystemwhichwouldideallyde- tect author whose content is offensive to women Thisdocumentdescribesatextchangeofrep- and/orimmigrant. AuthorProfilingiswidelystud- resentation approach to the task of Multilin- ied and some new ideas arise from time to time gual Detection of Hate Speech Against Im- (Rangel et al., 2016). We have developed a new migrants and Women in Twitter, as part of representationmethodfortextthatreducesthedi- SemEval-20191. The task is divided in two mensionality of the information for each author sub-tasks. Sub-task A consists in classifying to 6 characteristics per class. This representation, tweetsasbeinghatefulornothateful,whereas sub-task B requires fine tuning the classifica- Frequency Analysis Interpolation, is used to cod- tionbyclassifyingthehatefultweetsasbeing ify the texts for each user and this codified infor- directedtosingleindividualsorgeneric,ifthe mationisusedasinputdatatosupportvectorma- tweetisaggressiveornot. Ourapproachcon- chines with linear kernel. In a Big Data environ- sistsofachangeofthespaceofrepresentation ment,redu

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-datasets-and-benchmarks]]
