---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, benchmark, contrastive-learning, causal, prompting, explainability]
sources: [raw/sources/Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det.pdf]
---

# Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det

## Metadata
- Source file: `raw/sources/Jiang - 2025 - Learn from Failure Causality-guided Contrastive Learning for Generalizable Implicit Hate Speech Det.pdf`
- Year: 2025
- Pages: 10
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- In this paper, we propose a novel approach using causality-guided contrastive learning (CCL) to enhance the generalizabil- ity of implicit hate speech detection.
- Hate speech target- aware hard negative sampling was introduced to ingindividualsbasedonreligion,gender,orother optimize the learning of hard negatives by fully characteristics not only causes mental distress to utilizinglabelinformation(Kimetal.,2024).
- Inthecontextofimplicithatespeech Recently, contrastive learning has emerged as detection,thesubtlenatureofimplicitlanguageex- an effective approach for detecting implicit hate acerbatesthesespuriouscorrelations.

## Method
- In this paper, we propose a novel approach using causality-guided contrastive learning (CCL) to enhance the generalizabil- ity of implicit hate speech detection.
- This method reduces the model’s re- falsepositives.
- Ourextensiveexperi- implicationsofanchorsentencesaspositivesam- mentsonmultipleimplicithatespeechdatasets ples,applyingcontrastivelosstoimprovedetection.
- show that our approach outperforms current Similarly,ConPrompt(Kimetal.,2023)leveraged state-of-the-artmethodsincross-domaingener- machine-generated statements to enhance perfor- alization.

## Data and Evaluation Setup
- Ourextensiveexperi- implicationsofanchorsentencesaspositivesam- mentsonmultipleimplicithatespeechdatasets ples,applyingcontrastivelosstoimprovedetection.
- Figure2: Illustrationofthepositivessamplingstrategy • We demonstrate the effectiveness of CCL withinthreecontrastivelearningmethodsinasituation through cross-dataset evaluation, achieving wheretheclassoftheanchorishatespeechwhilepre- state-of-the-artperformanceonthreewidely- dicted correctly.
- (a) Supervised contrastive learning (SCL)selectsallthesamegroundtruthlabelswiththe used benchmark datasets for implicit hate anchoraspositivesamples.
- is the lack of high-quality datasets.

## Results and Claims
- Ourextensiveexperi- implicationsofanchorsentencesaspositivesam- mentsonmultipleimplicithatespeechdatasets ples,applyingcontrastivelosstoimprovedetection.
- show that our approach outperforms current Similarly,ConPrompt(Kimetal.,2023)leveraged state-of-the-artmethodsincross-domaingener- machine-generated statements to enhance perfor- alization.
- Figure2: Illustrationofthepositivessamplingstrategy • We demonstrate the effectiveness of CCL withinthreecontrastivelearningmethodsinasituation through cross-dataset evaluation, achieving wheretheclassoftheanchorishatespeechwhilepre- state-of-the-artperformanceonthreewidely- dicted correctly.

## Limitations and Follow-ups
- subtlety can result in false negatives, while case (4)showshowtermbiascanleadtofalsepositives.
- Asignif- Contrastive Learning (CCL) for implicit hate icant challenge in implicit hate speech detection speech detection, grounded in causal reasoning.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, causal, prompting, multimodal, explainability
- Mentioned datasets: toxigen, gab, twitter
- Mentioned metrics: f1, accuracy

## Abstract (Extracted)
> Abstract Implicithatespeechpresentsasignificantchal- lenge for automatic detection systems due to its subtlety and ambiguity. Traditional mod- elstrainedusingempiricalriskminimization (a)Falsenegativeashardpositive. (ERM)oftenrelyoncorrelationsbetweenclass labelsandspuriousattributes, whichleadsto poor performance on data lacking these cor- relations. In this paper, we propose a novel approach using causality-guided contrastive learning (CCL) to enhance the generalizabil- ity of implicit hate speech detection. Since ERMtendstoidentifyspuriousattributes,CCL (b)Falsepositiveashardpositive. worksbyaligningtherepresentationsofsam- Figure1:Ourresearchmotivations. Hardpositiveshave pleswiththesameclassbutoppositespurious same ground truth label but opposite predicted label attributes,identifiedthroughERM’sinference with the anchor, including (a) false negatives and (b) failure. This method reduces the model’s re- falsepositives. lianceonspuriouscorrelations,allowingitto learnmorerobustfeaturesandhandlediverse, nuancedcontextsbetter. Ourextensiveexperi- implicationsofanchorsentencesaspositi

## Benchmark Evidence Lines
- show that our approach outperforms current Similarly,ConPrompt(Kimetal.,2023)leveraged
- state-of-the-artmethodsincross-domaingener-
- state-of-the-artperformanceonthreewidely-
- ble 1. We use the macro F1-score measure for
- themacroF1-scoreonthetestset. and synonym substitution (Kim et al., 2022), as
- outperformsincross-datasetevaluations. Simply betweenthevariousmethodsareminimal,consis-
- whiledemonstratingsomeoverlap,isoutperformed
- consistently outperform SCL methods. A possi- Similarly,increasingthenumberofpositivesam-

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
