---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, retrieval, prompting, explainability]
sources: [raw/sources/Huang 等 - 2025 - Evolver Chain-of-Evolution Prompting to Boost Large Multimodal Models for Hateful Meme Detection.pdf]
---

# Huang 等 - 2025 - Evolver Chain-of-Evolution Prompting to Boost Large Multimodal Models for Hateful Meme Detection

## Metadata
- Source file: `raw/sources/Huang 等 - 2025 - Evolver Chain-of-Evolution Prompting to Boost Large Multimodal Models for Hateful Meme Detection.pdf`
- Year: 2025
- Pages: 10
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- The memeofTrumpisinfluencedbythememeofasadfrog 1 Introduction inanimageandtextsymbol,whichcreatesanewhateful meme.
- Incontrast,our thefieldofmultimodalresearch,aimingtoidentify Evolver capturestheevolutionandcontextofmemes, contentthatcombinestextandimagestopropagate utilizingthemaspromptsforlargemultimodalmodels hate speech or offensive messages.
- widespread cultural phenomenon, proliferate on theInternet,blendingimagesandtextstoconvey 2021) for hateful meme detection have demon- sophisticatedmeanings.

## Method
- In thiswork,weproposeEvolver,whichincorpo- (b) Conventional Two- Interpretability: Evolutionary: rates Large Multimodal Models (LMMs) via Steam Methods Chain-of-Evolution(CoE)Prompting,byinte- grating the evolution attribute and in-context Text Encoder information of memes.
- OCR Text ExtensiveexperimentsonpublicFHM,MAMI, ❄ Chain-of-Evolution Large Multimodal Prediction andHarMdatasetsshowthatCoEprompting Prompt Model canbeincorporatedintoexistingLMMstoim- Explanation provetheirperformance.
- Incontrast,our thefieldofmultimodalresearch,aimingtoidentify Evolver capturestheevolutionandcontextofmemes, contentthatcombinestextandimagestopropagate utilizingthemaspromptsforlargemultimodalmodels hate speech or offensive messages.
- Theseshortcom- ingshindertheunderstandingofmemes’evolving 2.2 LargeMultimodalModels natureandtheircontextualnuances,leadingtoover- Vision Encoder serves as a translator to help fittingontrainingsetsanddiminishedeffectiveness language models understand visual content.

## Data and Evaluation Setup
- OCR Text ExtensiveexperimentsonpublicFHM,MAMI, ❄ Chain-of-Evolution Large Multimodal Prediction andHarMdatasetsshowthatCoEprompting Prompt Model canbeincorporatedintoexistingLMMstoim- Explanation provetheirperformance.
- Bydevelopingabenchmarkspecificallytai- where h v is the language embedding tokens.
- Exten- t t n siveexperimentshaveshowntheeffectivenessof (cid:89) p(w) = p(w |w ,h ,h ) (4) ourmethodacrossthreewidelyrecognizedhateful i <i t v i=1 memedetectiondatasets,demonstratingasuperior abilitytoidentifyandinterprethatefulmemes.
- curatedmemepoolsratherthananyotherdataset, Input:[image0:<image0>,caption0:texts[0],image1:<im- wherethememesfollowthesamedefinitionofhate- age1>,caption1:texts[1],image2:<image2>,caption2:texts[2], fulness/harm/misogyny.

## Results and Claims
- ItexpandsLMMswithan 2.3 Evolver: Chain-of-EvolutionPrompting evolutionreasoningabilitywhileofferinggood To improve LMMs’ understanding of the online interpretability.
- The common in these memes is that makes fun of or discriminates against individuals with disabilities or genetic conditions.
- Notably, both MMICL and LLaVA-1.5 and open-source LMMs (e.g., LLaVA) can be with CoE Prompting outperform their zero-shot foundinAppendixA.

## Limitations and Follow-ups
- Thecombination Figure1(a),theextensiveevolutionofmemesfus- oftextandimagespresentssignificantchallenges ing together complicates the detection of hateful inhatefulmemedetection,especiallyfordetecting memes as they continuously evolve, bring new andmoderatinghatefulcontent(Levine,2013).
- Tra- Withtheadvancesinimage-textpre-training,ef- ditional methods for hateful meme detection, as fortstoleverageandfine-tuneCLIP(Radfordetal., illustratedinFigure1(b),sufferfromlimitationsin *Equalcontribution.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, prompting, multimodal, explainability
- Mentioned datasets: hateful memes, gab
- Mentioned metrics: accuracy, auc

## Abstract (Extracted)
> Abstract (a) The Evolutionof “Sad Frog” Memes Hateful memes continuously evolve as new onesemergebyblendingprogressivecultural ideas,renderingexistingmethodsthatrelyon extensive training obsolete or ineffective. In thiswork,weproposeEvolver,whichincorpo- (b) Conventional Two- Interpretability: Evolutionary: rates Large Multimodal Models (LMMs) via Steam Methods Chain-of-Evolution(CoE)Prompting,byinte- grating the evolution attribute and in-context Text Encoder information of memes. Specifically, Evolver Visual Language Prediction Model simulatestheevolvingandexpressingprocess Image Encoder ofmemesandreasonsthroughLMMsinastep- by-stepmannerusinganevolutionarypairmin- (c) Evolver (Ours) Interpretability: Evolutionary: ing module, an evolutionary information ex- Instruction + tractor, and a contextual relevance amplifier. OCR Text ExtensiveexperimentsonpublicFHM,MAMI, ❄ Chain-of-Evolution Large Multimodal Prediction andHarMdatasetsshowthatCoEprompting Prompt Model canbeincorporatedintoexistingLMMstoim- Explanation provetheirperformance. Moreencouragingly, ❄Image Encoder itcanserveasanin

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
