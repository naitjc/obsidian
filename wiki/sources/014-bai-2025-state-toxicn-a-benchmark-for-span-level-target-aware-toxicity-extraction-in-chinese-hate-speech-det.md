---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, cross-lingual, benchmark, prompting, explainability]
sources: [raw/sources/Bai 等 - 2025 - STATE ToxiCN A Benchmark for Span-level Target-Aware Toxicity Extraction in Chinese Hate Speech Det.pdf]
---

# Bai 等 - 2025 - STATE ToxiCN A Benchmark for Span-level Target-Aware Toxicity Extraction in Chinese Hate Speech Det

## Metadata
- Source file: `raw/sources/Bai 等 - 2025 - STATE ToxiCN A Benchmark for Span-level Target-Aware Toxicity Extraction in Chinese Hate Speech Det.pdf`
- Year: 2025
- Pages: 14
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Furthermore, ever, research on Chinese hate speech detection thelackofresearchonChinesehatefulslang lagssignificantlybehind.
- First,we 2022)islimitedtothepost-level,leavingspan-level constructaSpan-levelTarget-AwareToxicity Extractiondataset(STATETOXICN),which Chinesehatespeechdetectionunexplored.
- Thein- is the first span-level Chinese hate speech tensityanddirectionalityofhatespeechareclosely dataset.

## Method
- IntheChineselinguis- models using STATE TOXICN.
- Chinese hateful slang often dividualsandsociety,hatelanguageisnowwidely evades model detection through techniques such consideredasaproblemofincreasingimportance ashomophonicsubstitution,charactersplittingand (Silva et al., 2016).
- detailedannotationstoconstructthefirstannotated • Weevaluatemodelson STATE TOXICN,as- lexicon for Chinese hateful slang.
- Using pre-trained models to address this issue (Caselli thisdataset,weevaluatetheperformanceofLLMs etal.,2020;HanuandUnitaryteam,2020;Zhou inspan-levelChinesehatespeechdetection.

## Data and Evaluation Setup
- rectionalityofhatearecloselytiedtothetarget andargumentitisassociatedwith.However,re- Approximately 941 million people, or 12% of searchonhatespeechdetectioninChinesehas theglobalpopulation,speakMandarinChineseas laggedbehind,andexistingdatasetslackspan- their first language (Eberhard et al., 2024).
- First,we 2022)islimitedtothepost-level,leavingspan-level constructaSpan-levelTarget-AwareToxicity Extractiondataset(STATETOXICN),which Chinesehatespeechdetectionunexplored.
- Thein- is the first span-level Chinese hate speech tensityanddirectionalityofhatespeechareclosely dataset.
- Secondly,weevaluatethespan-level tiedtothetargetandargumentitisassociatedwith hatespeechdetectionperformanceofexisting (CowanandHodge,1996).

## Results and Claims
- Asanideo- harmagainstspecificgroupsorindividualsbased graphic language, Chinese has a wealth of syn- onrace,religion,gender,region,sexualorientation, onymsandnear-synonyms(Mair,1991), making physicalcharacteristics,andotherfactors(Bilewicz the forms and types of hateful slang diverse and andSoral,2020).
- challengesandinsightsforimprovement.
- TOCPandTOCAB,de- helps to understand how hateful slang is used to rivedfromTaiwan’sPTTplatform,focusondetect- disguise hate speech, but also provides valuable ingprofanityandabusivelanguage(ChungandLin, annotateddatatoevaluateandimprovetheability 2021).

## Limitations and Follow-ups
- Therearetwokeyissues posesasignificantchallenge.
- Finally, we tic context, challenges in span-level hate speech conductthefirststudyonChinesehatefulslang detectionariseduetoflexiblewordorderandthe andevaluatetheabilityofLLMstounderstand absence of word delimiterslikespaces.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: prompting, multimodal, explainability, cross-lingual
- Mentioned datasets: toxigen, toxicn, gab, founta, twitter
- Mentioned metrics: f1, accuracy

## Abstract (Extracted)
> Abstract detection, and this research has gradually shifted frompost-level(Ahnetal.,2024;AlKhamissietal., Theproliferationofhatespeechhascausedsig- 2022b) to span-level (Pavlopoulos et al., 2021; nificantharmtosociety. Theintensityanddi- Mathewetal.,2021;Zampierietal.,2023). rectionalityofhatearecloselytiedtothetarget andargumentitisassociatedwith.However,re- Approximately 941 million people, or 12% of searchonhatespeechdetectioninChinesehas theglobalpopulation,speakMandarinChineseas laggedbehind,andexistingdatasetslackspan- their first language (Eberhard et al., 2024). How- level fine-grained annotations. Furthermore, ever, research on Chinese hate speech detection thelackofresearchonChinesehatefulslang lagssignificantlybehind. Therearetwokeyissues posesasignificantchallenge. Inthispaper,we thatremainunresolved. Firstly, existingresearch providetwovaluablefine-grainedChinesehate (Dengetal.,2022;Jiangetal.,2022;Zhouetal., speechdetectionresearchresources. First,we 2022)islimitedtothepost-level,leavingspan-level constructaSpan-levelTarget-AwareToxicity Extractiondataset(STATETOXICN),w

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
