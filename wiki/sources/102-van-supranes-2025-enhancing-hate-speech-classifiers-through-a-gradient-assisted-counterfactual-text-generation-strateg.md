---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, causal, prompting, counterfactual]
sources: [raw/sources/Van Supranes 等 - 2025 - Enhancing Hate Speech Classifiers through a Gradient-assisted Counterfactual Text Generation Strateg.pdf]
---

# Van Supranes 等 - 2025 - Enhancing Hate Speech Classifiers through a Gradient-assisted Counterfactual Text Generation Strateg

## Metadata
- Source file: `raw/sources/Van Supranes 等 - 2025 - Enhancing Hate Speech Classifiers through a Gradient-assisted Counterfactual Text Generation Strateg.pdf`
- Year: 2025
- Pages: 16
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- GPT-basedevaluationreferstothesubjectiveratingsof fluency,similarity,andtoxicitydonebypromptingGPT-4o-mini.
- withrespecttofluency,semanticsimilaritytothe Original:Youcouldjuststayinyourstate original text, and perceived toxicity.
- Over- on binary classification: hate speech (a = 1) vs.

## Method
- However, approaches with a classification, but automating counterfactual purelygenerativegoaldonotdirectlymitigatebias text generation remains a challenge.
- We propose Gradient- andTonelli,2023).
- CDA methodsthatsolelyrelyoneitherprompting, involves generating synthetic data by modifying gradient-basedsteering,orenergy-basedsam- observed texts to satisfy target attributes while pling,GENESismorelikelytojointlysatisfy preserving their original meaning.
- Studies have attributealignmentandsemanticpreservation showed that training on both original and coun- underthesamebasemodel.

## Data and Evaluation Setup
- Whenappliedto terfactual data help reduce the model’s reliance dataaugmentation,GENESachievedthebest onspuriouscorrelations,improvingout-of-domain macro F1-score in two of three test sets, and generalization(Kaushiketal.,2021;Madaanetal., it improved robustness in detecting targeted abusive language.
- Based counterfactual texts continue to be the standard on our cross-dataset evaluation, the average (Sen et al., 2023), manual generation is time- performance of models aided by GENES is consuming and resource-intensive.
- quireslargedatasetsandsignificantcomputational resources.
- This 1 Introduction ispartlyduetobuilt-insafeguardsagainstoffensive Theriseofhatespeechhasdriventhedevelopment content(Wangetal.,2024)andtheinherentdiffi- of datasets and machine learning models aimed culty of generating text with subjective concepts atmitigatingharm.

## Results and Claims
- Strong attributecontrolcandistortmeaning,whilepri- and may lead to inconsistent performance gains oritizing semantic preservation may weaken (Wullach et al., 2021; Feng et al., 2021; Casula attribute alignment.
- Whenappliedto terfactual data help reduce the model’s reliance dataaugmentation,GENESachievedthebest onspuriouscorrelations,improvingout-of-domain macro F1-score in two of three test sets, and generalization(Kaushiketal.,2021;Madaanetal., it improved robustness in detecting targeted abusive language.
- This 1 Introduction ispartlyduetobuilt-insafeguardsagainstoffensive Theriseofhatespeechhasdriventhedevelopment content(Wangetal.,2024)andtheinherentdiffi- of datasets and machine learning models aimed culty of generating text with subjective concepts atmitigatingharm.

## Limitations and Follow-ups
- However, approaches with a classification, but automating counterfactual purelygenerativegoaldonotdirectlymitigatebias text generation remains a challenge.
- ingitseffectivenessasalightweightalterna- Toaddresstheselimitations,weinvestigatedthe tive.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: causal, prompting, counterfactual
- Mentioned datasets: toxigen, ethos, gab, twitter, reddit
- Mentioned metrics: f1, accuracy, precision, recall

## Abstract (Extracted)
> Abstract tokenbiases(Swamyetal.,2019;Nejadgholiand Kiritchenko, 2020; Ramponi and Tonelli, 2022; Counterfactualdataaugmentation(CDA)isa Bourgeade et al., 2023). Data augmentation is a promisingstrategyforimprovinghatespeech potential solution. However, approaches with a classification, but automating counterfactual purelygenerativegoaldonotdirectlymitigatebias text generation remains a challenge. Strong attributecontrolcandistortmeaning,whilepri- and may lead to inconsistent performance gains oritizing semantic preservation may weaken (Wullach et al., 2021; Feng et al., 2021; Casula attribute alignment. We propose Gradient- andTonelli,2023). Ideally,augmentationisdone assisted Energy-based Sampling (GENES) tobreakcorrelationsbetweentargetvariablesand for counterfactual text generation, which re- irrelevantfeatures. stricts accepted samples to text meeting a In this regard, counterfactual data augmen- minimum BERTScore threshold and applies tation (CDA) has emerged as a promising strat- gradient-assisted proposal generation to im- proveattributealignment. Comparedtoother egy(Samoryeta

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[hate-speech-datasets-and-benchmarks]]
