---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, cross-lingual, benchmark, retrieval, prompting, explainability]
sources: [raw/sources/Hee 等 - 2024 - Bridging Modalities Enhancing Cross-Modality Hate Speech Detection with Few-Shot In-Context Learnin.pdf]
---

# Hee 等 - 2024 - Bridging Modalities Enhancing Cross-Modality Hate Speech Detection with Few-Shot In-Context Learnin

## Metadata
- Source file: `raw/sources/Hee 等 - 2024 - Bridging Modalities Enhancing Cross-Modality Hate Speech Detection with Few-Shot In-Context Learnin.pdf`
- Year: 2024
- Pages: 15
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- By to explore the transferability of hate speech leveragingtherichnessoftext-baseddata,weaim detection between modalities.
- Recent hate speech strationsinfew-shotlearningcontextsoutperform studies have developed models targeting specific vision-languagedemonstrations,highlightingthe modalities (Cao et al., 2023; Awal et al., 2021).
- First,thereisascarcity As all forms of hate speech share one definition, ofdatasets,asthisareahasonlyrecentlygainedlots thisstudyinvestigatestheusefulnessofusinghate ofattention.

## Method
- Incontrast,theabundanceanddiversityof centresearchhasdevelopeddetectionmodels text-based data offer a potential source for cross- tailoredtospecificmodalities;however,there modalityknowledgetransfer(Heeetal.,2024).
- This paper investigates conductsextensiveexperimentsusingfew-shot whethertext-basedhatespeechdetectioncapabili- in-contextlearningwithlargelanguagemodels tiescanbetransferredtomultimodalformats.
- matsusingfew-shotin-contextlearningwithlarge language models.
- Recent hate speech strationsinfew-shotlearningcontextsoutperform studies have developed models targeting specific vision-languagedemonstrations,highlightingthe modalities (Cao et al., 2023; Awal et al., 2021).

## Data and Evaluation Setup
- This paper investigates conductsextensiveexperimentsusingfew-shot whethertext-basedhatespeechdetectioncapabili- in-contextlearningwithlargelanguagemodels tiescanbetransferredtomultimodalformats.
- Our findings to enhance the detection of vision-language hate demonstratethattext-basedhatespeechexam- speech,addressingcurrentresearchlimitationsand ples can significantly enhance the classifica- tionaccuracyofvision-languagehatespeech.
- Hatespeechintheonlinespaceap- theclassificationaccuracyofvision-languagehate pearsinvariousforms,includingtext-basedtweets speech.
- First,thereisascarcity As all forms of hate speech share one definition, ofdatasets,asthisareahasonlyrecentlygainedlots thisstudyinvestigatestheusefulnessofusinghate ofattention.

## Results and Claims
- (ii) We demonstrate that text- 1 Introduction basedhatespeechexamplessignificantlyimprove Motivation.
- Recent hate speech strationsinfew-shotlearningcontextsoutperform studies have developed models targeting specific vision-languagedemonstrations,highlightingthe modalities (Cao et al., 2023; Awal et al., 2021).
- First,thereisascarcity As all forms of hate speech share one definition, ofdatasets,asthisareahasonlyrecentlygainedlots thisstudyinvestigatestheusefulnessofusinghate ofattention.

## Limitations and Follow-ups
- Conse- Thewidespreadpresenceofhatespeechonthe quently,thelimitedavailabilityofvision-language internet,includingformatssuchastext-based data hampers performance in out-of-distribution tweetsandvision-languagememes,posesasig- nificantchallengetodigitalplatformsafety.Re- cases.
- Our findings to enhance the detection of vision-language hate demonstratethattext-basedhatespeechexam- speech,addressingcurrentresearchlimitationsand ples can significantly enhance the classifica- tionaccuracyofvision-languagehatespeech.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: retrieval, prompting, multimodal, explainability, cross-lingual
- Mentioned datasets: latent hatred, hateful memes, twitter
- Mentioned metrics: f1, accuracy

## Abstract (Extracted)
> Abstract iscomplicatedbycopyrightissuesandincreasingly stringent regulations on social platforms. Conse- Thewidespreadpresenceofhatespeechonthe quently,thelimitedavailabilityofvision-language internet,includingformatssuchastext-based data hampers performance in out-of-distribution tweetsandvision-languagememes,posesasig- nificantchallengetodigitalplatformsafety.Re- cases. Incontrast,theabundanceanddiversityof centresearchhasdevelopeddetectionmodels text-based data offer a potential source for cross- tailoredtospecificmodalities;however,there modalityknowledgetransfer(Heeetal.,2024). is a notable gap in transferring detection ca- pabilitiesacrossdifferentformats. Thisstudy Research Objectives. This paper investigates conductsextensiveexperimentsusingfew-shot whethertext-basedhatespeechdetectioncapabili- in-contextlearningwithlargelanguagemodels tiescanbetransferredtomultimodalformats. By to explore the transferability of hate speech leveragingtherichnessoftext-baseddata,weaim detection between modalities. Our findings to enhance the detection of vision-language hate demonstratethattex

## Benchmark Evidence Lines
- and vision-language memes. Recent hate speech strationsinfew-shotlearningcontextsoutperform
- two datasets in terms of F1 score. Secondly, the achievesanF1scoreimprovementof0.64and1.23
- strategiesconsistentlyoutperformedzero-shotin-
- learningoutperformsusingvision-languagedemon-
- tionmodelsagainstcovid-19-relatedhatefulmemes.
- We use the Mistral-7B model, a state-of-the-art "Insummary, thispost/memeis{label}". During

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
