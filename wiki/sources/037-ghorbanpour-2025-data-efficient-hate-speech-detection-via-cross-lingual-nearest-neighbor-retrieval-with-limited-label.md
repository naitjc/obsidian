---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, cross-lingual, benchmark, causal, retrieval, prompting]
sources: [raw/sources/Ghorbanpour 等 - 2025 - Data-Efficient Hate Speech Detection via Cross-Lingual Nearest Neighbor Retrieval with Limited Label.pdf]
---

# Ghorbanpour 等 - 2025 - Data-Efficient Hate Speech Detection via Cross-Lingual Nearest Neighbor Retrieval with Limited Label

## Metadata
- Source file: `raw/sources/Ghorbanpour 等 - 2025 - Data-Efficient Hate Speech Detection via Cross-Lingual Nearest Neighbor Retrieval with Limited Label.pdf`
- Year: 2025
- Pages: 19
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- gate redundancy and filter out highly similar Training on all available hate speech datasets retrievedinstances,resultinginimprovements mayseembeneficial,butitisofteninefficient,com- insomelanguages.1 putationallycostly,anddoesnotguaranteebetter Contentwarning:Thispapercontainsexamplesof performance(Casellietal.,2020).
- Moreover, Hate speech, abusive language targeting specific thisapproachlacksscalability,requiringfrequent groups (Ro¨ttger et al., 2021), is a global issue.
- priateintermediateEnglishtaskischallengingand When detecting hate speech in a low-resource language-dependent.

## Method
- ingapproach,weleveragenearest-neighborre- AsRo¨ttgeretal.(2022)state,havingsomelabeled trievaltoaugmentminimallabeleddatainthe datainthetargetlanguageiscrucialformodelef- target language, thereby enhancing detection performance.
- evaluateourapproachoneightlanguagesand Transferlearning,especiallyfromhigh-resource demonstrate that it consistently outperforms languageslikeEnglish,helpsmitigatedatascarcity models trained solely on the target language data.
- However, the ourapproachishighlydata-efficient,retrieving choiceofsourcetasksandlanguagesremainscru- as few as 200 instances in some cases while cial.
- Moreover, languagesduetoculturalsimilarities(Zhouetal., itisscalable,astheretrievalpoolcanbeeas- 2023),andcertainsourcetasksmaybemoreuse- ily expanded, and the method can be readily fulforparticulartargettasks(Ro¨ttgeretal.,2022; adaptedtonewlanguagesandtasks.

## Data and Evaluation Setup
- evaluateourapproachoneightlanguagesand Transferlearning,especiallyfromhigh-resource demonstrate that it consistently outperforms languageslikeEnglish,helpsmitigatedatascarcity models trained solely on the target language data.
- gate redundancy and filter out highly similar Training on all available hate speech datasets retrievedinstances,resultinginimprovements mayseembeneficial,butitisofteninefficient,com- insomelanguages.1 putationallycostly,anddoesnotguaranteebetter Contentwarning:Thispapercontainsexamplesof performance(Casellietal.,2020).
- redundancy,dataset-specificbiases,andannotation inconsistencies, leading to overfitting (Wiegand 1 Introduction etal.,2019;FortunaandNunes,2018).
- retrainingfornewdatasets(Vidgenetal.,2021a).

## Results and Claims
- evaluateourapproachoneightlanguagesand Transferlearning,especiallyfromhigh-resource demonstrate that it consistently outperforms languageslikeEnglish,helpsmitigatedatascarcity models trained solely on the target language data.
- Furthermore,inmostcases,ourmethod and improve detection performance (Bigoulaeva surpassesthecurrentstate-of-the-art.
- gate redundancy and filter out highly similar Training on all available hate speech datasets retrievedinstances,resultinginimprovements mayseembeneficial,butitisofteninefficient,com- insomelanguages.1 putationallycostly,anddoesnotguaranteebetter Contentwarning:Thispapercontainsexamplesof performance(Casellietal.,2020).

## Limitations and Follow-ups
- redundancy,dataset-specificbiases,andannotation inconsistencies, leading to overfitting (Wiegand 1 Introduction etal.,2019;FortunaandNunes,2018).
- Thissolutionaddressesseveralchallenges.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: causal, retrieval, prompting, multimodal, cross-lingual
- Mentioned datasets: gab, founta, twitter
- Mentioned metrics: f1

## Abstract (Extracted)
> Abstract (Poletto et al., 2021; Yin and Zubiaga, 2021). In contrast,languageslikeSpanish,French,andItal- Consideringtheimportanceofdetectinghate- ian,thoughnotlow-resourceforothertasks,lack fulcontent,labeledhatespeechdataisexpen- annotatedhatespeechdatasets(Polettoetal.,2021), siveandtime-consumingtocollectandanno- limiting model effectiveness in detecting and ad- tate, particularly for low-resource languages. dressinghatespeech. Priorworkhasdemonstratedtheeffectiveness ofcross-lingualtransferlearninganddataaug- Collectingandannotatingdataforlow-resource mentationinimprovingperformanceontasks languages is an effective solution, especially for withlimitedlabeleddata. Todevelopaneffi- capturing linguistic and cultural nuances in hate cientandscalablecross-lingualtransferlearn- speech (Pelicon et al., 2021; Aluru et al., 2020a). ingapproach,weleveragenearest-neighborre- AsRo¨ttgeretal.(2022)state,havingsomelabeled trievaltoaugmentminimallabeleddatainthe datainthetargetlanguageiscrucialformodelef- target language, thereby enhancing detection performance. Specifically,weassumeaccess fect

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-datasets-and-benchmarks]]
