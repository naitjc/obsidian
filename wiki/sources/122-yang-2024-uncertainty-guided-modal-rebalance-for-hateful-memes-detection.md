---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, causal, retrieval, prompting, explainability]
sources: [raw/sources/Yang 等 - 2024 - Uncertainty-Guided Modal Rebalance for Hateful Memes Detection.pdf]
---

# Yang 等 - 2024 - Uncertainty-Guided Modal Rebalance for Hateful Memes Detection

## Metadata
- Source file: `raw/sources/Yang 等 - 2024 - Uncertainty-Guided Modal Rebalance for Hateful Memes Detection.pdf`
- Year: 2024
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- modality imbalance is alleviated by improv- Previous research on hateful memes detection ingcosinelossfromtheperspectivesofinter- has employed pre-trained vision-language mod- modalfeatureandweightvectorsconstraints.
- Prior research has delved into clas- Toaddresstheaboveissues,thispaperproposes sic dual-stream models that integrate visual and an Uncertainty-guided Modal Rebalance (UMR) textual features derived from image and text en- framework for hateful memes detection.
- Furthermore, we consider the fying hateful memes.

## Method
- Tothis end,thispaperproposesanUncertainty-guided ModalRebalance(UMR)frameworkforhate- number of individuals are exploiting this format fulmemesdetection.
- elsforlearningvision,language,andcross-modal Inthisway,thesuppressedunimodalrepresen- tationabilityinmultimodalmodelswouldbe interactions comprehensively (Das et al., 2020; unleashed,whilethelearningofmodalitycon- Muennighoff, 2020; Zhou et al., 2021).
- To simplifymodeling,weassociateeachmemewitha text-only model Gaussiandistributioninalatentspacedefinedby text in CLIP image-text in CLIP mean and variance parameters.
- Bymodelinguncertainty,weflex- Figure 2: Examples demonstrate the modality imbal- iblycombinediscriminativecross-modalanduni- anceinhatefulmemes,wheretextmodalitysuppresses modalfeatures.

## Data and Evaluation Setup
- Exten- while,sophisticatedfusiontechniques(Kielaetal., siveexperimentalresultsdemonstratethatthe 2020;Leeetal.,2021;Yangetal.,2023)andexter- proposed UMR produces the state-of-the-art nalknowledgeenhancementmethods(Zhu,2020; performanceonfourwidely-useddatasets.
- Through experimental analysis, we find that there is a modality imbalance phe- • Extensive experimental results demonstrate nomenonbetweentheunimodalfeaturesinhateful that1)UMRproducesthestate-of-the-artper- memes.
- As shown in Figure 2, the performance formance on four widely-used datasets; 2) oftextisclosertomultimodalrepresentationcom- UMR provides consistent improvement on paredtoimage,buttheperformanceoftextandim- fourvision-languagebackbones.
- benchmarkspertainingtoCOVID-19andUSpoli- 3 Methodology tics.

## Results and Claims
- Exten- while,sophisticatedfusiontechniques(Kielaetal., siveexperimentalresultsdemonstratethatthe 2020;Leeetal.,2021;Yangetal.,2023)andexter- proposed UMR produces the state-of-the-art nalknowledgeenhancementmethods(Zhu,2020; performanceonfourwidely-useddatasets.
- How- AsillustratedinFigure1,thetextintheleftmeme ever, against a backdrop of current political and narratesanincrediblestory,whiletheimageshows socio-culturalfragmentation,asharplyincreasing twosmilingindividuals.
- Finally, we improve the cosine loss denotesobtainingtextfeaturesfromCLIP.

## Limitations and Follow-ups
- FacebookfirstproposestheHateful leashthecorrespondingdiscriminativecapabilities, Memes Challenge (Kiela et al., 2020) to prompt therebyaffectingthejudgmentofmodalitycontri- researcherstopinpointspecificcategoriesofhate- butions.
- In X i=1 j=1 the computer vision domain, to model visual un- where N represents thePbatch size, W R 2d × n certainty,somestudieshaveintroducedGaussian andb R n representfullyconnectedlay ∈ erweight representationsintospecifictasks,suchasperson ∈ andbias,respectively.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: causal, retrieval, prompting, multimodal, explainability
- Mentioned datasets: hateful memes, gab
- Mentioned metrics: f1, macro-f1, accuracy, precision, recall

## Abstract (Extracted)
> Abstract Hatefulmemesdetectionisachallengingmul- timodalunderstandingtaskthatrequirescom- prehensive learning of vision, language, and cross-modalinteractions.Previousresearchhas focusedondevelopingeffectivefusionstrate- giesforintegratinghateinformationfromdif- ferentmodalities. However,thesemethodsex- Figure 1: Examples demonstrate the inherent uncer- cessivelyrelyoncross-modalfusionfeatures, taintyinhatefulmemes,whichisthedegreeofcontri- ignoring the modality uncertainty caused by butionbetweenmodalitiestohatesentiment. Theleft the contribution degree of each modality to exampleindicatesthatidentifyinghatesentimentshould hate sentiment and the modality imbalance focusoncross-modalfeatures,whiletherightexample causedbythedominantmodalitysuppressing shouldfocusonunimodalfeatures. theoptimizationofanothermodality. Tothis end,thispaperproposesanUncertainty-guided ModalRebalance(UMR)frameworkforhate- number of individuals are exploiting this format fulmemesdetection. Theuncertaintyofeach topropagatehatecontentonplatformsbyadeptly meme is explicitly formulated by designing stochasticrep

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
