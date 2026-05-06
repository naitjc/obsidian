---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, retrieval, prompting, explainability]
sources: [raw/sources/Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection.pdf]
---

# Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection

## Metadata
- Source file: `raw/sources/Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection.pdf`
- Year: 2025
- Pages: 23
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- WhileLargeMulti- Furthermore,thegenerativenatureofLMMsoffers modal Models (LMMs) have shown promise interpretability,allowingmodelstoprovideratio- in hateful meme detection, they face notable challengeslikesub-optimalperformanceand nalesfortheirdetectiondecisions.
- Recentstudiesfurtherrevealthelimita- toadapttotherapidlyevolvinglandscapeofonline tionsofbothsupervisedfine-tuning(SFT)and memes,makingthemwell-suitedfordeployment in-contextlearningwhenappliedtoLMMsin inreal-worldcontentmoderationsystems.
- To address these issues, we pro- this potential, current LMMs face the following posearobustadaptationframeworkforhateful challenges when applied to hateful meme detec- meme detection that enhances in-domain ac- curacyandcross-domaingeneralizationwhile tion.

## Method
- WhileLargeMulti- Furthermore,thegenerativenatureofLMMsoffers modal Models (LMMs) have shown promise interpretability,allowingmodelstoprovideratio- in hateful meme detection, they face notable challengeslikesub-optimalperformanceand nalesfortheirdetectiondecisions.
- To address these issues, we pro- this potential, current LMMs face the following posearobustadaptationframeworkforhateful challenges when applied to hateful meme detec- meme detection that enhances in-domain ac- curacyandcross-domaingeneralizationwhile tion.
- Analysis reveals that our ap- proachachievesimprovedrobustnessunderad- tolearntheinterplayofvisualandtextualcues versarialattackscomparedtoSFTmodels.
- Ex- inherent in hateful memes through standard perimentsonsixmemeclassificationdatasets supervisedfine-tuning(SFT),asreportedby showthatourapproachachievesstate-of-the- Mei et al.

## Data and Evaluation Setup
- Ex- inherent in hateful memes through standard perimentsonsixmemeclassificationdatasets supervisedfine-tuning(SFT),asreportedby showthatourapproachachievesstate-of-the- Mei et al.
- Their overfitting, which degrades performance on 23818 Proceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pages23818–23840 November4-9,2025©2025AssociationforComputationalLinguistics generalmultimodalbenchmarkslikeMMMU 2 RelatedWork (Yueetal.,2023).
- Other works andRA-HMDQwen2-VL-7BmodelsontheHateful- incorporate caption models into the CLIP-based Memesdataset.
- (2024) results on six widely used meme classifica- demonstratedthatfine-tunedCLIPmodelscanout- tion datasets.

## Results and Claims
- Ideally,LMMs limitedout-of-domaingeneralizationcapabil- alsobringimprovedgeneralizability,enablingthem ities.
- Analysis reveals that our ap- proachachievesimprovedrobustnessunderad- tolearntheinterplayofvisualandtextualcues versarialattackscomparedtoSFTmodels.
- We also report that SFT art performance, outperforming larger agen- LMMsproducelower-qualityrationaleswhen ticsystems.

## Limitations and Follow-ups
- WhileLargeMulti- Furthermore,thegenerativenatureofLMMsoffers modal Models (LMMs) have shown promise interpretability,allowingmodelstoprovideratio- in hateful meme detection, they face notable challengeslikesub-optimalperformanceand nalesfortheirdetectiondecisions.
- To address these issues, we pro- this potential, current LMMs face the following posearobustadaptationframeworkforhateful challenges when applied to hateful meme detec- meme detection that enhances in-domain ac- curacyandcross-domaingeneralizationwhile tion.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, prompting, multimodal, explainability
- Mentioned datasets: hateful memes, gab, twitter, reddit
- Mentioned metrics: f1, accuracy, precision, recall, auc

## Abstract (Extracted)
> Abstract strongcapabilitiesacrossarangeofgeneralvision- language tasks provide a solid foundation for un- Hatefulmemeshavebecomeasignificantcon- derstandingtheintricateinterplaybetweentextand cernontheInternet,necessitatingrobustauto- imageinmemes(Zhuetal.,2023;Liuetal.,2023b). mateddetectionsystems. WhileLargeMulti- Furthermore,thegenerativenatureofLMMsoffers modal Models (LMMs) have shown promise interpretability,allowingmodelstoprovideratio- in hateful meme detection, they face notable challengeslikesub-optimalperformanceand nalesfortheirdetectiondecisions. Ideally,LMMs limitedout-of-domaingeneralizationcapabil- alsobringimprovedgeneralizability,enablingthem ities. Recentstudiesfurtherrevealthelimita- toadapttotherapidlyevolvinglandscapeofonline tionsofbothsupervisedfine-tuning(SFT)and memes,makingthemwell-suitedfordeployment in-contextlearningwhenappliedtoLMMsin inreal-worldcontentmoderationsystems. Despite this setting. To address these issues, we pro- this potential, current LMMs face the following posearobustadaptationframeworkforhateful challenges when applied to hateful meme

## Benchmark Evidence Lines
- art performance, outperforming larger agen-
- classification,achievingnewstate-of-the-art
- demonstratesstate-of-the-artperformancefor
- where few-shot systems consistently outperform
- Observation 3: RA-HMD outperforms all
- outperformsVPD-PaLI-X-55BonHatefulMemes.
- mainingstate-of-the-artmodels,includingISSUES
- sifiersoutperformbaselineLMMs. ilar to Mei et al. (2024): models fine-tuned on

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
