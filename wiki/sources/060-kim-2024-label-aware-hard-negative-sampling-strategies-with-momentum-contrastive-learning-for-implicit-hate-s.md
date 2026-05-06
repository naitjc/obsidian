---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, contrastive-learning, causal, retrieval, prompting, explainability]
sources: [raw/sources/Kim 等 - 2024 - Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate S.pdf]
---

# Kim 等 - 2024 - Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate S

## Metadata
- Source file: `raw/sources/Kim 等 - 2024 - Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate S.pdf`
- Year: 2024
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate Speech Detection Warning:Thispapercontainsexamplesthatcanbeoffensiveorupsetting.
- Detecting implicit hate speech that is not di- Easy negative (label: non-hate) 0.45 rectlyhatefulremainsachallenge.
- search has attempted to detect implicit hate speechbyapplyingcontrastivelearningtopre- Hard negative (label: non-hate) trained language models such as BERT and Black people contributed a lot to the elimination of racism.

## Method
- Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate Speech Detection Warning:Thispapercontainsexamplesthatcanbeoffensiveorupsetting.
- search has attempted to detect implicit hate speechbyapplyingcontrastivelearningtopre- Hard negative (label: non-hate) trained language models such as BERT and Black people contributed a lot to the elimination of racism.
- RoBERTa,buttheproposedmodelsstilldonot haveasignificantadvantageovercross-entropy Figure1: Ourresearchmotivation.
- Wefoundthatcontrastive alowsemanticsimilaritytoanchors,andhardnegatives learningbasedonrandomlysampledbatchdata haveahighsemanticsimilaritytoanchors.

## Data and Evaluation Setup
- detailedfeaturesfromhardnegativesamples, Researchhasbuiltimplicithatespeechdatasetsof instead of naive negative samples in random implicit hate speech (ElSherief et al., 2021; Sap batch,usingmomentum-integratedcontrastive etal.,2020;Hartvigsenetal.,2022;Vidgenetal., learning.
- LAHNoutperformstheexistingmod- 2021)andproposeddetectionmodels(Kimetal., elsforimplicithatespeechdetectionbothin- and cross-datasets.
- TherecentlyproposedConPrompt(Kim and cross-dataset evaluation with a simple etal.,2023)utilizedmachine-generatedstatements dropoutnoiseaugmentationwithoutexternal to improve implicit hate speech performance by knowledgeandadditionalcost.
- However, thesepreviousmethodsstillhave mance in both in- and cross-dataset evalua- limitationsduetorelianceonpre-definedexternal tiononfourrepresentativepublicbenchmark knowledgeortextgenerationcosts.

## Results and Claims
- LAHNoutperformstheexistingmod- 2021)andproposeddetectionmodels(Kimetal., elsforimplicithatespeechdetectionbothin- and cross-datasets.
- socialproblemsasitleadstodiscriminationagainst Figure1showsaneasynegative(middle)anda certaingroupsandsocialconflict(Howard,2019; hardnegative(bottom)forananchorsentencetar- Matamoros-Fernández and Farkas, 2021).
- implicationofanchorsentences)aspositivesam- • Contrarytopreviousstudies,weobservethat plesusingcontrastivelossforimplicithatespeech LAHN can improve performance in both in- detection.

## Limitations and Follow-ups
- Detecting implicit hate speech that is not di- Easy negative (label: non-hate) 0.45 rectlyhatefulremainsachallenge.
- However, thesepreviousmethodsstillhave mance in both in- and cross-dataset evalua- limitationsduetorelianceonpre-definedexternal tiononfourrepresentativepublicbenchmark knowledgeortextgenerationcosts.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, causal, retrieval, prompting, multimodal, explainability
- Mentioned datasets: toxigen, gab, twitter
- Mentioned metrics: f1

## Abstract (Extracted)
> Abstract Blacks have contributed nothing to humanity. Detecting implicit hate speech that is not di- Easy negative (label: non-hate) 0.45 rectlyhatefulremainsachallenge. Recentre- Jews recognize that they can sometimes be 0.85 victims of racism themselves. search has attempted to detect implicit hate speechbyapplyingcontrastivelearningtopre- Hard negative (label: non-hate) trained language models such as BERT and Black people contributed a lot to the elimination of racism. RoBERTa,buttheproposedmodelsstilldonot haveasignificantadvantageovercross-entropy Figure1: Ourresearchmotivation. Easynegativeshave loss-basedlearning. Wefoundthatcontrastive alowsemanticsimilaritytoanchors,andhardnegatives learningbasedonrandomlysampledbatchdata haveahighsemanticsimilaritytoanchors. does not encourage the model to learn hard negative samples. In this work, we propose Label-aware Hard Negative sampling strate- models to learn subtle differences between simi- gies(LAHN)thatencouragethemodeltolearn lar sentences that might otherwise confuse them. detailedfeaturesfromhardnegativesamples, Researchhasbu

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
