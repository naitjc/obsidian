---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, cross-lingual, benchmark, retrieval, explainability]
sources: [raw/sources/Sariyanto 等 - 2025 - Towards Explainable Hate Speech Detection.pdf]
---

# Sariyanto 等 - 2025 - Towards Explainable Hate Speech Detection

## Metadata
- Source file: `raw/sources/Sariyanto 等 - 2025 - Towards Explainable Hate Speech Detection.pdf`
- Year: 2025
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- To determine the optimal inewhetheranexistingconceptcanbemodifiedto weights and classification strategies, we ana- outperformorcompetewithneuralnetworks-based lyze hate speech and non-hate speech words strategies.
- for opinion mining and NLP tasks in social con- texts, e.g., alongside hate speech detection there 2 RelatedWork aremodelsforsentimentanalysisandironydetec- tion.
- Themodelsarefine-tunedpre-trainedmodels, Before neural networks became widely used in andthehatespeechdetectionmethodusesthepre- the field of hate speech detection, mostly tradi- trainedBERTweetmodel(Nguyenetal.,2020).

## Method
- However,de- spitetheiraccuracy,deeplearningmodelsrequire Recentadvancementsindeeplearninghavesig- substantialcomputationalresourcesandlongtrain- nificantlyenhancedtheefficiencyandaccuracy ing times.
- However,thesemodelsoftenrequiresubstan- training costs, the high computational demands tial computational resources, which remains remain a significant drawback (Yin and Zubiaga, a major drawback.
- of deep learning architectures, and exploring We can avoid the high cost associated with simpler yet effective approaches can lead to expensive hardware requirements and time- cost-efficientNLPsolutions.
- We addresshatespeechdetectionbyintroducing idea,andrecognizingthevalueofexploringsimple a model that employs a weighted sum of va- yeteffectiveapproachesalongsideproposingnew lence, arousal, and dominance (VAD) scores methodstoenhanceexistingtechniques,weexam- for classification.

## Data and Evaluation Setup
- However,de- spitetheiraccuracy,deeplearningmodelsrequire Recentadvancementsindeeplearninghavesig- substantialcomputationalresourcesandlongtrain- nificantlyenhancedtheefficiencyandaccuracy ing times.
- The study of Antypas and Cama- cordingtoourexperiments,oursimpleyeteffective choCollados(2023)investigatesthegeneralization methodcancompetewithneuralnetworks-based ofmodelsonunseendataanddiscusseshowdataset methods,includingrecentlargelanguagemodels.
- 2, we give a brief summary of tendencytofocusonacertaintypeofhatespeech methods utilized in our experiments.
- To address this, they constructed an wepresenttheVADalgorithm,andinSec.4,we ensembleofhatespeechdatasets,findingthattrain- demonstrateourexperimentalresults.

## Results and Claims
- To determine the optimal inewhetheranexistingconceptcanbemodifiedto weights and classification strategies, we ana- outperformorcompetewithneuralnetworks-based lyze hate speech and non-hate speech words strategies.
- Inpar- religion,ornationality,andthusspreadsorshows ticular,theintroductionofthetransformerarchitec- hate towards a certain group (Chiril et al., 2022; turehasledtoimprovementsintextgeneration,ma- Davidson et al., 2017; Cao et al., 2020).
- Weconclude ing on such an ensemble improves classification withasummaryanddiscussionoffuturedirections accuracy.

## Limitations and Follow-ups
- One of the great challengesofhatespeechdetectionistheusageof 1 Introduction informal language (Reyes et al., 2012).
- formation can inadvertently bias models toward Theremainderofthepaperisorganizedasfol- certaintypesofhatespeech,i.e.,itpointsoutthe lows.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: retrieval, multimodal, explainability, cross-lingual
- Mentioned datasets: gab, twitter
- Mentioned metrics: f1, accuracy, precision, recall

## Abstract (Extracted)
> Abstract etal.,2017;Patwardhanetal.,2023). However,de- spitetheiraccuracy,deeplearningmodelsrequire Recentadvancementsindeeplearninghavesig- substantialcomputationalresourcesandlongtrain- nificantlyenhancedtheefficiencyandaccuracy ing times. Although transfer learning can reduce of natural language processing (NLP) tasks. However,thesemodelsoftenrequiresubstan- training costs, the high computational demands tial computational resources, which remains remain a significant drawback (Yin and Zubiaga, a major drawback. Reducing the complexity 2021;Shariretal.,2020). of deep learning architectures, and exploring We can avoid the high cost associated with simpler yet effective approaches can lead to expensive hardware requirements and time- cost-efficientNLPsolutions. Thisisalsoastep consumingtrainingproceduresifatraditionalalgo- towardsexplainableAI,i.e.,uncoveringhowa rithm can achieve similar or even better results particulartaskiscarriedout. Forthisanalysis, while solving an NLP task. Motivated by this wechosethetaskofhatespeechdetection. We addresshatespeechdetectionbyintroducing idea

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
