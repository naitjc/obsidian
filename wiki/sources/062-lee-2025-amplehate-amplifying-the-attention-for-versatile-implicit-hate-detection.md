---
created: 2026-04-23
updated: 2026-04-23
tags:
  - paper
  - hate-speech
  - deep-ingest-v2
  - implicit
  - cross-lingual
  - benchmark
  - contrastive-learning
  - retrieval
  - prompting
  - multimodal
  - explainability
sources:
  - raw/sources/Lee 等 - 2025 - AmpleHate Amplifying the Attention for Versatile Implicit Hate Detection.pdf
---

# Lee 等 - 2025 - AmpleHate Amplifying the Attention for Versatile Implicit Hate Detection

## Metadata
- Source file: `raw/sources/Lee 等 - 2025 - AmpleHate Amplifying the Attention for Versatile Implicit Hate Detection.pdf`
- Year: 2025
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- AmpleHate Amplify Current approaches rely on contrastive learn- ing,whichisshowntobeeffectiveondistin- guishinghateandnon-hatesentences.Humans, however, detect implicit hate speech by first identifyingspecifictargetswithinthetextand White man built America.
- Yet, alongside the ben- shipsbetweenexplicit,implicittargetsandsen- efits, these platforms also enable the spread of tence context and then, directly injects these hate speech, becoming a serious social issue.
- outperforming contrastive learning baselines For explicit hate speech detection, traditional by an average of 82.14% and achieves faster textclassificationapproachessuchthatlearnglobal convergence.

## Method
- AmpleHate Amplify Current approaches rely on contrastive learn- ing,whichisshowntobeeffectiveondistin- guishinghateandnon-hatesentences.Humans, however, detect implicit hate speech by first identifyingspecifictargetswithinthetextand White man built America.
- Motivated Figure1:AmpleHateeffectivelydetectsimplicithate bythisreasoningprocess,weproposeAmple- sentences by amplifying the target signals of hate- Hate,anovelapproachdesignedtomirrorhu- relatedtokensinthecontextofimplicithateness.
- maninferenceforimplicithatedetection.Am- pleHateidentifiesexplicittargetsusingapre- trainedNamedEntityRecognitionmodeland capturesimplicittargetinformationvia[CLS] enabling rapid information dissemination and in- tokens.
- outperforming contrastive learning baselines For explicit hate speech detection, traditional by an average of 82.14% and achieves faster textclassificationapproachessuchthatlearnglobal convergence.

## Data and Evaluation Setup
- outperforming contrastive learning baselines For explicit hate speech detection, traditional by an average of 82.14% and achieves faster textclassificationapproachessuchthatlearnglobal convergence.
- gets whose embeddings align more closely with In the implicit hate speech dataset, the crit- the sentence-level context.
- sure that the output contains the signals of target 4 ExperimentsandAnalysis relations.
- Byinjectingr intoh 0 Dynahate (Vidgenetal.,2021)introducedachal- rightbeforeclassification,AmpleHateamplifies lenginghatespeechdatasetbuiltviaahuman-and- target-context interactions directly in the final model-in-the-loopprocess,incorporatingperturbed logits.

## Results and Claims
- outperforming contrastive learning baselines For explicit hate speech detection, traditional by an average of 82.14% and achieves faster textclassificationapproachessuchthatlearnglobal convergence.
- Table1showsthatAmple- uses each cluster centroid as an anchor, and then Hateconsistentlyoutperformsnearlyallbaseline fine-tunesthemodelwithasupervisedcontrastive models,withparticularlystronggainsondatasets loss.
- withimplicithate(e.g.,+27.32%ponWhite).On average, it improves over BERT by 6.87%p and LAHN (Kimetal.,2024)integratesmomentum overthestrongestbaseline(LAHN)by5.58%p.

## Limitations and Follow-ups
- This tence and subsequently interpreting how the con- posesasignificantchallengeforautomatedimplicit text frames or characterizes these targets to infer hatespeechdetection.Recentworkshaveprimarily hateful intent.
- Acknowledgments Limitations ThisresearchwassupportedbytheNRFgrant(RS- AmpleHatereliesontheaccuracyoftheexternal 2025-0222262) and the AI Graduate School Pro- NER tagger for explicit target identification; er- gram (RS-2020-II201361) funded by the Korean rorsorinsufficiententityrecognitionmaylimitper- government(MSIT).
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, prompting, multimodal, explainability, cross-lingual
- Mentioned datasets: toxigen, ethos, gab, twitter, reddit
- Mentioned metrics: f1, macro-f1, accuracy, precision

## Abstract (Extracted)
> Abstract Target signals in a hate speech sentence Current SOTA model Implicithatespeechinvolvessubtleandindi- Hate detection rect expressions of prejudice or hostility to- ward a group. Detecting it is challenging be- cause it relies on nuanced context and impli- White man built America. Western civilization is the best cationratherthanexplicitoffensivelanguage. AmpleHate Amplify Current approaches rely on contrastive learn- ing,whichisshowntobeeffectiveondistin- guishinghateandnon-hatesentences.Humans, however, detect implicit hate speech by first identifyingspecifictargetswithinthetextand White man built America. Western civilization is the best subsequentlyinterpretinghowthesetargetsre- late to their surrounding context. Motivated Figure1:AmpleHateeffectivelydetectsimplicithate bythisreasoningprocess,weproposeAmple- sentences by amplifying the target signals of hate- Hate,anovelapproachdesignedtomirrorhu- relatedtokensinthecontextofimplicithateness. maninferenceforimplicithatedetection.Am- pleHateidentifiesexplicittargetsusingapre- trainedNamedEntityRecognitionmodeland capturesimp

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
