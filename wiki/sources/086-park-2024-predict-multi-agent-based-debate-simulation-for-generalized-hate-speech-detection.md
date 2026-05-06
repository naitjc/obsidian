---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, benchmark, retrieval, prompting, explainability]
sources: [raw/sources/Park 等 - 2024 - PREDICT Multi-Agent-based Debate Simulation for Generalized Hate Speech Detection.pdf]
---

# Park 等 - 2024 - PREDICT Multi-Agent-based Debate Simulation for Generalized Hate Speech Detection

## Metadata
- Source file: `raw/sources/Park 等 - 2024 - PREDICT Multi-Agent-based Debate Simulation for Generalized Hate Speech Detection.pdf`
- Year: 2024
- Pages: 25
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- PREDICT: Multi-Agent-based Debate Simulation for Generalized Hate Speech Detection TriggerWarning:Thispapercontainsdiscussionsofhatespeechthatmaybedistressingortriggeringforsomereaders.
- Inour frameworkthatusesthenotionofmulti-agent research,thelabelingcriteriaofthepublicdatasetwere for hate speech detection.
- Previousstudieshaveattemptedtoaddressthe TheriseofhatespeechontheInternethasbecome issue of generalization in hate speech detection asignificantsocialissue,promptingextensivere- through various approaches, including data inte- searchonhatespeechdetection(Moyetal.,2021; gration,augmentation,andexplanationgeneration.

## Method
- Previous research has pre- sentedmethodstogeneralizemodelsthrough dataintegrationoraugmentation,butovercom- ingthedifferencesinlabelingcriteriabetween datasetsremainsalimitation.
- Toaddressthese Figure1: Ourresearchismotivatedbytheclassification challenges, we propose PREDICT, a novel ofthesametextunderdifferentlabelingcriteria.
- Inour frameworkthatusesthenotionofmulti-agent research,thelabelingcriteriaofthepublicdatasetwere for hate speech detection.
- Thus, an approach availableathttps://github.com/Hanyang-HCC- thatdoesnotoverlyrelyonspecificlabelingcrite- Lab/PREDICT riaisneededtoimprovethegeneralizationofhate 1 Introduction speechdetection.

## Data and Evaluation Setup
- Previous research has pre- sentedmethodstogeneralizemodelsthrough dataintegrationoraugmentation,butovercom- ingthedifferencesinlabelingcriteriabetween datasetsremainsalimitation.
- Inour frameworkthatusesthenotionofmulti-agent research,thelabelingcriteriaofthepublicdatasetwere for hate speech detection.
- One Theintegrationofdatasetscoveringdiversetopics, ofthemaindifficultiesencounteredinhatespeech suchasgenderandrace(Bourgeadeetal.,2023),al- detectionisgeneralization(YinandZubiaga,2021).
- However,thisapproachhasalim- toimprovetheaccuracyofhatespeechdetection.

## Results and Claims
- Thus, an approach availableathttps://github.com/Hanyang-HCC- thatdoesnotoverlyrelyonspecificlabelingcrite- Lab/PREDICT riaisneededtoimprovethegeneralizationofhate 1 Introduction speechdetection.
- However,thisapproachhasalim- toimprovetheaccuracyofhatespeechdetection.
- have partially improved the performance of hate speechdetection,thereremainlimitationsineffec- • Consensus through Debate: PREDICT tivelyincorporatingdifferencesinlabelingcriteria presentsareasoning-baseddebatesimulation intothemodel’strainingorinferenceprocess.

## Limitations and Follow-ups
- Previous research has pre- sentedmethodstogeneralizemodelsthrough dataintegrationoraugmentation,butovercom- ingthedifferencesinlabelingcriteriabetween datasetsremainsalimitation.
- Toaddressthese Figure1: Ourresearchismotivatedbytheclassification challenges, we propose PREDICT, a novel ofthesametextunderdifferentlabelingcriteria.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: retrieval, prompting, explainability
- Mentioned datasets: gab
- Mentioned metrics: f1, accuracy, auc

## Abstract (Extracted)
> Abstract While a few public benchmarks have been proposed for training hate speech detection models,thedifferencesinlabelingcriteriabe- tween these benchmarks pose challenges for generalized learning, limiting the applicabil- ity of the models. Previous research has pre- sentedmethodstogeneralizemodelsthrough dataintegrationoraugmentation,butovercom- ingthedifferencesinlabelingcriteriabetween datasetsremainsalimitation. Toaddressthese Figure1: Ourresearchismotivatedbytheclassification challenges, we propose PREDICT, a novel ofthesametextunderdifferentlabelingcriteria. Inour frameworkthatusesthenotionofmulti-agent research,thelabelingcriteriaofthepublicdatasetwere for hate speech detection. PREDICT con- usedtodevelopanagent. sists of two phases: (1) PRE (Perspective- basedREasoning): Multipleagentsarecreated basedontheinducedlabelingcriteriaofgiven datasets,andeachagentgeneratesstancesand trainedonaparticulardatasetmayperformpoorly reasons;(2)DICT(DebateusingInCongruenT whenthemodelisappliedtoadifferentdataset(Cai references): Agentsrepresentinghateandnon- etal.,2022). Thisismainlydue

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
