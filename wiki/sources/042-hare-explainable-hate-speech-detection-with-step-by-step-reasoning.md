---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, prompting, explainability]
sources: [raw/sources/HARE_ Explainable Hate Speech Detection with Step-by-Step Reasoning.pdf]
---

# HARE Explainable Hate Speech Detection with Step-by-Step Reasoning

## Metadata
- Source file: `raw/sources/HARE_ Explainable Hate Speech Detection with Step-by-Step Reasoning.pdf`
- Year: 2019
- Pages: 16
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- HARE: Explainable Hate Speech Detection with Step-by-Step Reasoning Warning:Thispapercontainsexamplesofcontentthatisoffensiveandmaybeupsetting.
- To combat nu- ancedformsofhatespeech,itisimportantto identify and thoroughly explain hate speech to help users understand its harmful effects.
- Inthispaper,weintroduceahatespeech to generate hate speech explanations step-by-step.

## Method
- Recent benchmarks have attempted to tackle this issue by training generative models on free-text annotations of implications in hate- fultext.However,wefindsignificantreasoning gapsintheexistingannotationsschemes,which mayhinderthesupervisionofdetectionmod- Figure1: HAREuseslargelanguagemodels(LLMs) els.
- (b)Weproposetheuseof supervisionofdetectionmodels.
- Experiments LLMstofillinthegapsandenabledetectionmodelsto onSBICandImplicitHatebenchmarksshow understandandexplainhatespeech.
- thatourmethod,usingmodel-generateddata, consistently outperforms baselines, using ex- isting free-text human annotations.

## Data and Evaluation Setup
- Recent benchmarks have attempted to tackle this issue by training generative models on free-text annotations of implications in hate- fultext.However,wefindsignificantreasoning gapsintheexistingannotationsschemes,which mayhinderthesupervisionofdetectionmod- Figure1: HAREuseslargelanguagemodels(LLMs) els.
- Experiments LLMstofillinthegapsandenabledetectionmodelsto onSBICandImplicitHatebenchmarksshow understandandexplainhatespeech.
- thatourmethod,usingmodel-generateddata, consistently outperforms baselines, using ex- isting free-text human annotations.
- This can help mitigate distri- demonstratesthatourmethodenhancestheex- butional biases inherent in simple classification, planation quality of trained models and im- allowingpeopletounderstandandreasonaboutthe provesgeneralizationtounseendatasets.

## Results and Claims
- thatourmethod,usingmodel-generateddata, consistently outperforms baselines, using ex- isting free-text human annotations.
- code is available at https://github.com/ Explanations can also improve the transparency joonkeekim/hare-hate-speech.git.
- More- isimportantforsystemstonotonlyidentifyhate over,weobservethattheprovidedrationalesgive speechbutalsoprovideinterpretableexplanations marginal improvement to detection performance ∗equalcontribution †correspondingauthors underjointtraining.

## Limitations and Follow-ups
- This can help mitigate distri- demonstratesthatourmethodenhancestheex- butional biases inherent in simple classification, planation quality of trained models and im- allowingpeopletounderstandandreasonaboutthe provesgeneralizationtounseendatasets.
- Limitations Evaluation (IITP) grant funded by Korea govern- ment (MSIT) [No.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: prompting, explainability
- Mentioned datasets: gab, twitter
- Mentioned metrics: f1, accuracy

## Abstract (Extracted)
> Abstract With the proliferation of social media, accu- ratedetectionofhatespeechhasbecomecrit- ical to ensure safety online. To combat nu- ancedformsofhatespeech,itisimportantto identify and thoroughly explain hate speech to help users understand its harmful effects. Recent benchmarks have attempted to tackle this issue by training generative models on free-text annotations of implications in hate- fultext.However,wefindsignificantreasoning gapsintheexistingannotationsschemes,which mayhinderthesupervisionofdetectionmod- Figure1: HAREuseslargelanguagemodels(LLMs) els. Inthispaper,weintroduceahatespeech to generate hate speech explanations step-by-step. detection framework, HARE, which harnesses (a)Recentbenchmarksonunderstandinghatespeech the reasoning capabilities of large language providefree-textannotationsontheimplicationsofhate models (LLMs) to fill these gaps in explana- speech,butgapsinreasoninghinderthesupervisionof tions of hate speech, thus enabling effective generativedetectionmodels. (b)Weproposetheuseof supervisionofdetectionmodels. Experiments LLMstofillinthegapsandenabl

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
