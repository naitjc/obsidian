---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, retrieval, prompting]
sources: [raw/sources/Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning.pdf]
---

# Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning

## Metadata
- Source file: `raw/sources/Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning.pdf`
- Year: 2024
- Pages: 15
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- We whichsubtledifferencesineitherimageortextmay demonstrate a retrieval-based hateful memes leadtoacompletelydifferentmeaning(Kielaetal., detectionsystem,whichiscapableofidentify- 2021).
- transfer and update of hateful memes detection systems to handle the fast-evolving landscape of LMMslikeFlamingo(Alayracetal.,2022)and hatefulmemesinreal-lifeapplications.
- Ourcontri- LENS (Berrios et al., 2023) have demonstrated butionsare: their effectiveness in detecting hateful memes.

## Method
- dingspacethroughretrieval-guidedcontrastive Correctlydetectinghatefulmemesremainsdiffi- training.
- Our approach achieves state-of-the- cult.
- Previousliteraturehasidentifiedaprominent artperformanceontheHatefulMemesdataset withanAUROCof87.0,outperformingmuch challenge in classifying "confounder memes", in largerfine-tunedlargemultimodalmodels.
- We whichsubtledifferencesineitherimageortextmay demonstrate a retrieval-based hateful memes leadtoacompletelydifferentmeaning(Kielaetal., detectionsystem,whichiscapableofidentify- 2021).

## Data and Evaluation Setup
- Previousliteraturehasidentifiedaprominent artperformanceontheHatefulMemesdataset withanAUROCof87.0,outperformingmuch challenge in classifying "confounder memes", in largerfine-tunedlargemultimodalmodels.
- temsontheHatefulMemesdatasetwithfarfewer modelparameters.
- In AUCandaccuracyusingtheKNNmajorityvoting thispaper,weshowthatsuchCLIP-basedmodels classifier, even outperforming large multi-modal canachievebetterperformancewithourproposed modelsundersimilarsettings.
- WithRGCLtraining,theretrieval-basedclas- sifierdemonstratesstrongcross-datasetgener- Sparseretrievalmethods,suchasBM-25(Robert- alizability,makingitsuitableforrealservices son and Zaragoza, 2009) have been used in con- inthedynamicenvironmentofonlinehateful trastive learning to obtain collections of hard memes.

## Results and Claims
- Previousliteraturehasidentifiedaprominent artperformanceontheHatefulMemesdataset withanAUROCof87.0,outperformingmuch challenge in classifying "confounder memes", in largerfine-tunedlargemultimodalmodels.
- Evenstate-of-the-art This paper contains content for demonstration models, such as HateCLIPper (Kumar and Nan- purposesthatmaybedisturbingforsomereaders.
- RGCLachieveshigherperfor- of such object detectors results in high inference mancethanstate-of-the-artlargemultimodalsys- latency(Kimetal.,2021).

## Limitations and Follow-ups
- Previousliteraturehasidentifiedaprominent artperformanceontheHatefulMemesdataset withanAUROCof87.0,outperformingmuch challenge in classifying "confounder memes", in largerfine-tunedlargemultimodalmodels.
- Menick, Sebastian cludesthedatacurationguidelines,biasofthean- Borgeaud,AndyBrock,AidaNematzadeh,Sahand notators,andthelimiteddefinitionofhatespeech.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, prompting, multimodal
- Mentioned datasets: hateful memes, gab, twitter
- Mentioned metrics: f1, accuracy, auc

## Abstract (Extracted)
> Abstract whichconsistofimagesaccompaniedbytexts,are becomingaprominentformofonlinehatespeech. Hatefulmemeshaveemergedasasignificant Thismaterialcanperpetuatestereotypes,incitedis- concern on the Internet. Detecting hateful crimination,andevencatalysereal-worldviolence. memes requires the system to jointly under- Toprovide usersthe optionof not seeingit, hate- stand the visual and textual modalities. Our ful memes detection systems have garnered sig- investigationrevealsthattheembeddingspace ofexistingCLIP-basedsystemslackssensitiv- nificantinterestintheresearchcommunity(Kiela itytosubtledifferencesinmemesthatarevital etal.,2021;Suryawanshietal.,2020b,a;Praman- forcorrecthatefulnessclassification. Wepro- ick et al., 2021a; Liu et al., 2022; Hossain et al., poseconstructingahatefulness-awareembed- 2022;Prakashetal.,2023;Sahinetal.,2023). dingspacethroughretrieval-guidedcontrastive Correctlydetectinghatefulmemesremainsdiffi- training. Our approach achieves state-of-the- cult. Previousliteraturehasidentifiedaprominent artperformanceontheHatefulMemesdataset withanAUROCof87.0,outperforming

## Benchmark Evidence Lines
- withanAUROCof87.0,outperformingmuch challenge in classifying "confounder memes", in
- tributetotheirhatefulnature. Evenstate-of-the-art
- mancethanstate-of-the-artlargemultimodalsys- latency(Kimetal.,2021).
- classifier, even outperforming large multi-modal canachievebetterperformancewithourproposed
- Flamingo80Bachievesastate-of-the-artAUROC
- of 86.6, outperforming previous CLIP-based sys-
- 87.0% and an accuracy of 78.8%, outperforming
- larlywithAUCscoresofaround79%. HateCLIPper2 85.5 76.0 89.7 84.8

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-datasets-and-benchmarks]]
