---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, cross-lingual, benchmark, contrastive-learning, retrieval, prompting, explainability]
sources: [raw/sources/Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning.pdf]
---

# Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning

## Metadata
- Source file: `raw/sources/Kim 等 - 2022 - Generalizable Implicit Hate Speech Detection Using Contrastive Learning.pdf`
- Year: 2022
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Text(Input): However,itischallengingtoidentifyimplicit “thatispartofthewhitesupremacylogicthat hate speech in nuance or context when there nativepeoplearelessthanhuman.
- Theexperimen- white supremacy .” talresultsoncross-datasetshowthatImpCon SharedImplication Implicit Hate Speeches improvesatmost9.10%onBERT,and8.71% onHateBERT.
- andSikdar,2017;Badjatiyaetal.,2017;Parkand Fung, 2017; Zhang et al., 2018; Lee et al., 2019; Hate speech is “any communication that dis- Wangetal.,2020).

## Method
- Recently,thereare Label: NotHate severalattemptstodetectimplicithatespeech Text(Input): leveraging pre-trained language models such “sendthembacktothecountries as BERT and HateBERT.
- We tackle this cross-dataset under- performingproblemusingcontrastivelearning.
- laughable moment though .” weproposeanovelcontrastivelearningmethod, ImpCon,thatpullsanimplicationanditscor- People of color are “reverse all engines !
- Whiletheseapproacheswork parages a target group of people based on some fairlywellwhenatextcontainsanexplicithateor characteristicsuchasrace,color,ethnicity,gender, abusiveword,theyoftenfailtodetectimplicitones.

## Data and Evaluation Setup
- Fine-tuning on an theycamefrom” implicithatespeechdatasetshowssatisfactory Label: Hate performancewhenevaluatedonthetestsetof thedatasetusedfortraining.
- However,weem- piricallyconfirmthattheperformancedropsat Table 1: Example input texts and labels (Hate / Not least 12.5%p in F1 score when tested on the Hate)fromIMPLICITHATECORPUS(IHC)(ElSherief datasetthatisdifferentfromtheoneusedfor etal.,2021)whichisanimplicithatespeechdataset.
- We tackle this cross-dataset under- performingproblemusingcontrastivelearning.
- inferior to white people make americawhite again .” We evaluate the effectiveness of ImpCon by running cross-dataset evaluation on three im- “everything worthwhile in a society is plicithatespeechbenchmarks.

## Results and Claims
- Hatespeechdetectionhasgainedincreasingat- laughablemomentthough.” tentionwiththegrowingprevalenceofhateful Label: Hate contents.
- inferior to white people make americawhite again .” We evaluate the effectiveness of ImpCon by running cross-dataset evaluation on three im- “everything worthwhile in a society is plicithatespeechbenchmarks.
- Theexperimen- white supremacy .” talresultsoncross-datasetshowthatImpCon SharedImplication Implicit Hate Speeches improvesatmost9.10%onBERT,and8.71% onHateBERT.

## Limitations and Follow-ups
- We use three implicit hate datasets(IMPLICITHATECORPUS(IHC),SOCIAL 3 Approach BIAS INFERENCE CORPUS (SBIC) and DYNA- 3.1 OverallTrainingObjective HATE)followingHartvigsenetal.(2022).
- We consider all samples other than 3.2.1 AugmentedPostasPositiveSamples a positive sample as negative samples, excluding It has been shown that unintended biases in a itself.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, prompting, multimodal, explainability, cross-lingual
- Mentioned datasets: toxigen, gab, founta, twitter
- Mentioned metrics: f1

## Abstract (Extracted)
> Abstract Text(Input): “myworldorbitsaroundwhitesasitshould. Hatespeechdetectionhasgainedincreasingat- laughablemomentthough.” tentionwiththegrowingprevalenceofhateful Label: Hate contents. Whenatextcontainsanobvioushate wordorexpression,itisfairlyeasytodetectit. Text(Input): However,itischallengingtoidentifyimplicit “thatispartofthewhitesupremacylogicthat hate speech in nuance or context when there nativepeoplearelessthanhuman. wearen’t.” areinsufficientlexicalcues. Recently,thereare Label: NotHate severalattemptstodetectimplicithatespeech Text(Input): leveraging pre-trained language models such “sendthembacktothecountries as BERT and HateBERT. Fine-tuning on an theycamefrom” implicithatespeechdatasetshowssatisfactory Label: Hate performancewhenevaluatedonthetestsetof thedatasetusedfortraining. However,weem- piricallyconfirmthattheperformancedropsat Table 1: Example input texts and labels (Hate / Not least 12.5%p in F1 score when tested on the Hate)fromIMPLICITHATECORPUS(IHC)(ElSherief datasetthatisdifferentfromtheoneusedfor etal.,2021)whichisanimplicithatespeechdataset. training. We

## Benchmark Evidence Lines
- least 12.5%p in F1 score when tested on the Hate)fromIMPLICITHATECORPUS(IHC)(ElSherief
- improvesatmost9.10%onBERT,and8.71%
- outperform other baselines in terms of in-dataset Train IHC SBIC DYNAHATE
- tionforthecurrentstate-of-the-artmodelstrained dicatesthedatasetusedfortraining,whiletherowon
- ization ability of implicit hate detectors on cross- 2.92% improvement), ImpCon brings consistent
- tobeclosetogetherandnegativepairstobeapart els (at most 9.10% improvement to BERT and
- intherepresentationspace(RethmeierandAugen- 8.71%improvementtoHateBERT).Theconsistent
- stein,2022). Oneofthekeyissuesincontrastive improvement of ImpCon demonstrates the effec-

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
