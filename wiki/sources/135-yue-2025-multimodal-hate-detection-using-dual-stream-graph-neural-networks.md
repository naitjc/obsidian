---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, cross-lingual, benchmark, contrastive-learning, retrieval, graph, prompting]
sources: [raw/sources/Yue 等 - 2025 - Multimodal Hate Detection Using Dual-Stream Graph Neural Networks.pdf]
---

# Yue 等 - 2025 - Multimodal Hate Detection Using Dual-Stream Graph Neural Networks

## Metadata
- Source file: `raw/sources/Yue 等 - 2025 - Multimodal Hate Detection Using Dual-Stream Graph Neural Networks.pdf`
- Year: 2025
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- In the future, we would like to extend our model through multi-scale analysis to localizehatefulcontent,whichcouldimprovetheefficiencyofcurrentcontentmoderation.
- Automated hate speech detection and the problem of offensive language.
- Thehatefulmemeschallenge: Detectinghate speechinmultimodalmemes.

## Method
- Althoughmultimodalclassificationapproaches integratinginformationfromseveralmodalitiesoutperformunimodalones,theytypically neglectthatevenminimalhatefulcontentdefinesavideo’scategory.
- Toaddressthese limitations,weproposeanovelmultimodaldual-streamgraphneuralnetworkmodel.
- Importance weights and in- stancefeaturesarecombinedtogeneratevideolabels.Ourmodelemploysagraph-based framework to systematically model structured relationships within and across modali- ties.
- Extensiveexperimentsonpublicdatasetsshowthatourmodelisstate-of-the-artin hateful video classification and has strong explainability.

## Data and Evaluation Setup
- Extensiveexperimentsonpublicdatasetsshowthatourmodelisstate-of-the-artin hateful video classification and has strong explainability.
- Additionally,ourmethodemploysdual-streamgraphstomitigatetheinter- ferenceofnon-hatefulcontentinhatefulvideos.Wedemonstratethatourmodelachievesthe state-of-the-artperformanceonpublicdatasets.
- • Wedemonstratethatourmodelachievesthestate-of-the-artperformanceonthewidely usedpublicdatasetHateMM[4]andMultiHateClip[24].
- [4]constructedavaluable multimodalvideodataset,comprising1083videosandannotatedthemashateornon-hate.

## Results and Claims
- Althoughmultimodalclassificationapproaches integratinginformationfromseveralmodalitiesoutperformunimodalones,theytypically neglectthatevenminimalhatefulcontentdefinesavideo’scategory.
- Extensiveexperimentsonpublicdatasetsshowthatourmodelisstate-of-the-artin hateful video classification and has strong explainability.
- Toovercomethis,multimodalmodels[4,24,30]havebeenproposed,whichintegrate informationacrossdifferentmodalitiesandsignificantlyoutperformunimodalapproaches.

## Limitations and Follow-ups
- Toaddressthese limitations,weproposeanovelmultimodaldual-streamgraphneuralnetworkmodel.
- To address these two key challenges, we propose MultiHateGNN, a novel multimodal dual-streamgraphneuralnetwork.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, graph, prompting, multimodal, cross-lingual
- Mentioned datasets: founta, twitter
- Mentioned metrics: f1, accuracy, precision, recall

## Abstract (Extracted)
> Abstract Hatefulvideospresentseriousriskstoonlinesafetyandreal-worldwell-being,ne- cessitatingeffectivedetectionmethods. Althoughmultimodalclassificationapproaches integratinginformationfromseveralmodalitiesoutperformunimodalones,theytypically neglectthatevenminimalhatefulcontentdefinesavideo’scategory. Specifically,they generally treat all content uniformly, instead of emphasizing the hateful components. Additionally,existingmultimodalmethodscannotsystematicallycapturestructuredin- formationinvideos, limitingtheeffectivenessofmultimodalfusion. Toaddressthese limitations,weproposeanovelmultimodaldual-streamgraphneuralnetworkmodel. It constructsaninstancegraphbyseparatingthegivenvideointoseveralinstancestoex- tractinstance-levelfeatures. Then, acomplementaryweightgraphassignsimportance weights to these features, highlighting hateful instances. Importance weights and in- stancefeaturesarecombinedtogeneratevideolabels.Ourmodelemploysagraph-based framework to systematically model structured relationships within and across modali- ties. Extensiveexperimentsonpublicdatasetsshowthatourmodel

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-datasets-and-benchmarks]]
