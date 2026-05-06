---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, causal, retrieval, prompting, explainability]
sources: [raw/sources/Yang 等 - 2024 - Uncertainty-Aware Cross-Modal Alignment for Hate Speech Detection.pdf]
---

# Yang 等 - 2024 - Uncertainty-Aware Cross-Modal Alignment for Hate Speech Detection

## Metadata
- Source file: `raw/sources/Yang 等 - 2024 - Uncertainty-Aware Cross-Modal Alignment for Hate Speech Detection.pdf`
- Year: 2024
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Whileofferingunparalleledcon- for multimodal hate speech through the strategic veniencetousers,socialmediaplatformshavealso combinationofimagesandtext,particularlyinthe becomeconduitsfortherapiddisseminationofhate contextofcontemporarypoliticalandsocio-cultural speech,especiallyinthewakeofsignificantevents divisions.
- Therefore, detecting 2020;Leeetal.,2021)andfine-tuninglarge-scale and curbing hate speech is a particularly urgent pretrained multimodal models (Das et al., 2020; researchissue.
- Toalleviatetheissuesmentionedabove,thispa- per proposes an uncertainty-aware cross-modal alignment (UCA) framework for multimodal hate speech detection.

## Method
- Tothisend, thispaperproposesanuncertainty-awarecross-modal alignment(UCA)frameworkformodelingthemisalignmentanduncertaintyinmultimodalhatespeechdetection.
- Therefore, detecting 2020;Leeetal.,2021)andfine-tuninglarge-scale and curbing hate speech is a particularly urgent pretrained multimodal models (Das et al., 2020; researchissue.
- Mostworks presentonsocialmediaplatforms,andtheabove focusoncapturingcriticalfeaturessuchasentities unimodal approaches are no longer sufficient to and demographic information, while ignoring the effectively respond.
- Toalleviatetheissuesmentionedabove,thispa- per proposes an uncertainty-aware cross-modal alignment (UCA) framework for multimodal hate speech detection.

## Data and Evaluation Setup
- Finally,across-modal uncertaintylearningmoduleisproposed,whichevaluatesthedivergencebetweenunimodalfeaturedistributionstoto balanceunimodalandcross-modalfusionfeatures.
- Extensiveexperimentsonfivepubliclyavailabledatasetsshow thattheproposedUCAproducesacompetitiveperformancecomparedwiththeexistingmultimodalhatespeech detectionmethods.
- imagecanthemodelaccuratelyidentifythehate • Extensive experiments on five publicly avail- tendencyinit.
- Similarly,forthememebelow,only abledatasetsdemonstratesthattheproposed byaligningtheAsiansinthetextwiththeexagger- UCA yields competitive performance when atedeye-openingmovementsintheimagecanthe comparedtoexistingmultimodalhatespeech potentialhateofnationalitybeidentified.

## Results and Claims
- The top meme expresses discrimina- distributions, enabling adaptive control over tionagainstthedisabled,butonlywhentheleg in thebalanceofcross-modalandunimodalfea- the text corresponds to the prosthetic limb in the turesinmemes.
- Researchersfromdiversefields hateinformationagainstreligioninmemes.
- Model Overview etal.,2021;Zhu,2020;Leeetal.,2021;Caoetal., 2022)andensemblestrategies(Yangetal.,2022, In this section, we describe the proposed 2023) to improve the hate speech classification uncertainty-aware cross-modal alignment (UCA) performance.

## Limitations and Follow-ups
- Nowadays,therearevari- ingprogress,therearestillthefollowinglimitations: ousformsofhatespeech(suchasmemes)widely 1)Themisalignmentofimageandtext.
- Finally,across-modaluncertaintylearning Hateful Non-Hateful moduleisproposedtoestimatetheuncertaintybe- tweenmodalitiesbylearningfromthedistributional Figure 1: Examples illustrate two challenges en- divergenceofunimodalfeatures.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, causal, retrieval, prompting, multimodal, explainability
- Mentioned datasets: hateful memes, gab, twitter
- Mentioned metrics: f1, macro-f1, accuracy, precision, recall

## Abstract (Extracted)
> Abstract Hatespeechdetectionhasbecomeanurgenttaskwiththeemergenceofhugemultimodalharmfulcontent(e.g., memes)onsocialmediaplatforms. Previousstudiesmainlyfocusoncomplexfeatureextractionandfusiontolearn discriminativeinformationfrommemes. However,thesemethodsignoretwokeypoints: 1)themisalignmentofimage andtextinmemescausedbythemodalitygap,and2)theuncertaintybetweenmodalitiescausedbythecontribution degreeofeachmodalitytohatesentiment. Tothisend, thispaperproposesanuncertainty-awarecross-modal alignment(UCA)frameworkformodelingthemisalignmentanduncertaintyinmultimodalhatespeechdetection. Specifically,wefirstutilizethecross-modalfeatureencodertocaptureimageandtextfeaturerepresentationsin memes. Then,across-modalalignmentmoduleisappliedtoreducesemanticgapsbetweenmodalitiesbyaligning thefeaturerepresentations. Next,across-modalfusionmoduleisdesignedtolearnsemanticinteractionsbetween modalitiestocapturecross-modalcorrelations,providingcomplementaryfeaturesformemes. Finally,across-modal uncertaintylearningmoduleisproposed,whichevaluatesthedivergencebetweenunimodalfeaturedistributionstoto bala

## Benchmark Evidence Lines
- 2023) to improve the hate speech classification uncertainty-aware cross-modal alignment (UCA)
- UCA(Ours) 76.10 84.32 Models F1↑ Pre.↑ Rec.↑
- Acc.↑ F1↑ MMAE↓ UCA(Ours) 65.89 66.09 66.90
- CLIP 73.45 72.61 0.2508 utilizingAcc.,Macro-F1(F1),andMacro-Averaged
- Inthecross-modalfeatureencoder,weemploythe et al., 2019), using F1, Pre., Rec. and Acc. as
- sequencestomatchthesequencesize. M isfixed UCAobtainsanewstate-of-the-artresultwithan
- while C is set to 256, consistent with the output a significant improvement of approximately +3%.
- theminibatchisfixedat64. Thetrainingepochsfor state-of-the-artresultontheSarcasmdataset. The

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
