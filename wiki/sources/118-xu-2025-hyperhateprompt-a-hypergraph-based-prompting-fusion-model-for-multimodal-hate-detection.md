---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, cross-lingual, benchmark, contrastive-learning, graph, prompting, explainability]
sources: [raw/sources/Xu 等 - 2025 - HyperHatePrompt A Hypergraph-based Prompting Fusion Model for Multimodal Hate Detection.pdf]
---

# Xu 等 - 2025 - HyperHatePrompt A Hypergraph-based Prompting Fusion Model for Multimodal Hate Detection

## Metadata
- Source file: `raw/sources/Xu 等 - 2025 - HyperHatePrompt A Hypergraph-based Prompting Fusion Model for Multimodal Hate Detection.pdf`
- Year: 2025
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- De- spite promising progress, three critical chal- lenges, the absence of implicit hateful cues, the cross-modal-induced hate, and the diver- CAN NIGGER BE A GOOD LEADER?
- Detect- *CorrespondingAuthor ing these implicit hateful cues is essential for ac- curately identifying hate speech across multiple ability,hypergraphsofferamoresophisticatedand modalities.
- Whileconcatenating etal.(2021)appliedmultiplemodelstodetectBen- cross-modal features, as in previous works (Hee gali hate speech.

## Method
- Toaddressthese challenges, wepro- pose a hypergraph-based prompting fusion model.
- Ourmodelfirstusestailoredprompts multiplemodalities(SchmidtandWiegand,2017), toinferimplicithatefulcues.
- Finally,hypergraphconvo- ingcomprehensiveandaccuratecuesofhate,thus lution fuses diverse hateful cues, enhancing multimodalapproachisessentialforamoreprecise theexplorationofcross-modalhateandtarget- andin-depthunderstandinganddetectionofhate ing specific groups.
- Therefore, recent research has increas- twobenchmarkdatasetsshowthatourmodel achievesstate-of-the-artperformanceinmulti- inglyfocusedonthedetectionofmultimodalhate modalhatedetection.

## Data and Evaluation Setup
- Experimental results on content.
- Therefore, recent research has increas- twobenchmarkdatasetsshowthatourmodel achievesstate-of-the-artperformanceinmulti- inglyfocusedonthedetectionofmultimodalhate modalhatedetection.
- Addressingthisdiversityisessential forimprovingtheperformanceandfairnessofmul- • We evaluate our model on two benchmark timodalhatedetection.
- datasets,anddemonstrateitssuperiorityover To address these challenges, we propose a state-of-the-artbaselinesinmultimodalhate hypergraph-basedpromptingfusionmodel,Hyper- detectionthroughextensiveexperiments.

## Results and Claims
- Therefore, recent research has increas- twobenchmarkdatasetsshowthatourmodel achievesstate-of-the-artperformanceinmulti- inglyfocusedonthedetectionofmultimodalhate modalhatedetection.
- datasets,anddemonstrateitssuperiorityover To address these challenges, we propose a state-of-the-artbaselinesinmultimodalhate hypergraph-basedpromptingfusionmodel,Hyper- detectionthroughextensiveexperiments.
- The learning i goalistoidentifywhetheradatasampleishateor 2.2 MultimodalHateDetection notbycollectivelyconsideringthesemanticcues presentedinboththetextandimagemodalities,pre- Multimodal hate detection has gained significant dictingthecorrespondinghatelabely.

## Limitations and Follow-ups
- Toaddressthese challenges, wepro- pose a hypergraph-based prompting fusion model.
- Hate con- challenges in multimodal hate detection remain tent,whichincludesaggressive,discriminatoryand largelyoverlooked: theabsenceofimplicithateful derogatorytextandvisualsaimedatspecificgroups cues,cross-modal-inducedhate,andthediversity based on race, gender, and religion, is a harm- ofhatetargetgroups.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, graph, prompting, multimodal, explainability, cross-lingual
- Mentioned datasets: hateful memes, gab, twitter, reddit
- Mentioned metrics: f1, macro-f1, accuracy, auc

## Abstract (Extracted)
> Abstract Multimodalhatedetectionaimstoidentifyhate contentacrossmultiplemodalitiesforpromot- ing a harmonious online environment. De- spite promising progress, three critical chal- lenges, the absence of implicit hateful cues, the cross-modal-induced hate, and the diver- CAN NIGGER BE A GOOD LEADER? The oratory ignites a wave of snoring… Cali…in full RETARD mode sityofhatetargetgroups,inherentinthemul- （a） (b) timodal hate detection task, have been over- Figure1: Twoexamplesofmultimodalhatedetection. looked. Toaddressthese challenges, wepro- pose a hypergraph-based prompting fusion model. Ourmodelfirstusestailoredprompts multiplemodalities(SchmidtandWiegand,2017), toinferimplicithatefulcues. Itthenintroduces hyperedges to capture cross-modal-induced isofgreatersignificanceasitcanintegratediverse hate and applies a diversity-oriented hyper- informationfromtext,imageandothermodalities, edgeexpansionstrategytoaccountfordifferent whilesingle-modaldetectionislimitedincaptur- hatetargetgroups. Finally,hypergraphconvo- ingcomprehensiveandaccuratecuesofhate,thus lution fuses diverse hateful 

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
