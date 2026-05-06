---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, cross-lingual, benchmark, contrastive-learning, causal, prompting, explainability]
sources: [raw/sources/Sheth 等 - 2024 - Causality Guided Disentanglement for Cross-Platform Hate Speech Detection.pdf]
---

# Sheth 等 - 2024 - Causality Guided Disentanglement for Cross-Platform Hate Speech Detection

## Metadata
- Source file: `raw/sources/Sheth 等 - 2024 - Causality Guided Disentanglement for Cross-Platform Hate Speech Detection.pdf`
- Year: 2024
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Citation in BibTeX format Causality Guided Disentanglement for Cross-Platform Hate Speech .
- aftermath of hate speech, it becomes imperative to detect such contentononlinesocialmediaplatformsandpreventitsspreadfor CCSCONCEPTS arespectfulandsustainableonlineenvironment.
- Therefore, by isolating the CAusality-awaredisenTanglementframeworkforCross-platform target-dependentaspectofinputrepresentation,wecanusethe Hatespeechdetection,namely,CATCH1thatleveragesthecausal remainingcomponenttocreategeneralizablehaterepresentations.

## Method
- Citation in BibTeX format Causality Guided Disentanglement for Cross-Platform Hate Speech .
- •Computingmethodologies→Naturallanguageprocessing; Duetothevolumeofonlinecontent,itisinfeasibletodetect Causalreasoninganddiagnostics.
- qualitytrainingdatafromotherplatforms(source).However,ifthe WSDM’24,March4–8,2024,Merida,Mexico modeldoesnotadjustforthebiasespresentinthetrainingdataof ©2024Copyrightisheldbytheowner/author(s).PublicationrightslicensedtoACM.
- areknowntobegenerallyinvariant,thuscanenhancethegen- Recent works aim to build such generalizable models for de- eralization capabilities of machine learning models [4].

## Data and Evaluation Setup
- itthussuggestedusingtheannotator’straitsandthegroundtruth labelduringtrainingtoimprovehatespeechdetection.Incontrast, • Experimentalresultsonfourplatformsdemonstratethat anotherstudy[8]trainedamodelforpredictingusersatisfaction CATCHoutperformsthestate-of-the-artbaselines.
- Theauthorsof[14]trainedfourmodelsonnineEnglishdatasetsand Anotherwork[38]manuallyidentifiedtwocausalcues,aggression analyzedtheirgeneralizationcapabilities.Theyconcludedthatthe andsentiment,togeneralizethelanguagemodelrepresentations.
- causalcomponentandaplatform-dependentcomponent(target) Allthesedatasetscontainthehatelabelsaswellasthetargetlabels.
- aidinlearninginvariantcausalrepresentationsthatcanimprove AsummaryofthedatasetscanbefoundinTable2.Weusemacro thegeneralizabilityofhatespeechdetection?

## Results and Claims
- itthussuggestedusingtheannotator’straitsandthegroundtruth labelduringtrainingtoimprovehatespeechdetection.Incontrast, • Experimentalresultsonfourplatformsdemonstratethat anotherstudy[8]trainedamodelforpredictingusersatisfaction CATCHoutperformsthestate-of-the-artbaselines.
- aidinlearninginvariantcausalrepresentationsthatcanimprove AsummaryofthedatasetscanbefoundinTable2.Weusemacro thegeneralizabilityofhatespeechdetection?
- Baselines WecompareourCATCHframeworkagainstvarious Table2:Datasetstatisticswithcorrespondingplatformsand stateoftheartbaselines.Thesebaselinemethodsweredesignedto percentageofhatefulcommentsorposts.

## Limitations and Follow-ups
- qualitytrainingdatafromotherplatforms(source).However,ifthe WSDM’24,March4–8,2024,Merida,Mexico modeldoesnotadjustforthebiasespresentinthetrainingdataof ©2024Copyrightisheldbytheowner/author(s).PublicationrightslicensedtoACM.
- humiliation,inferiorstatus,violence,dehumanization,genocide, • PEACE[38]leveragestwocausalcues,namely,thesentiment attack/defense,hatespeech),whicharedebiasedandaggregated andaggression,tomakerepresentationsmoregeneralizable.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, causal, prompting, explainability, cross-lingual
- Mentioned datasets: gab, twitter, reddit
- Mentioned metrics: f1, macro-f1

## Abstract (Extracted)
> ABSTRACT KEYWORDS Despitetheirvalueinpromotingopendiscourse,socialmediaplat- domaingeneralization,hatespeechdetection,causalrepresentation formsareoftenexploitedtospreadharmfulcontent.Currentdeep learning learningandnaturallanguageprocessingmodelsusedfordetect- ACMReferenceFormat: ingthisharmfulcontentrelyondomain-specifictermsaffecting ParasSheth,RahaMoraffah,TharinduS.Kumarage,AmanChadha,andHuan theirabilitytoadapttogeneralizablehatespeechdetection.This Liu.2024.CausalityGuidedDisentanglementforCross-PlatformHateSpeech isbecausetheytendtofocustoonarrowlyonparticularlinguistic Detection.InProceedingsofthe17thACMInternationalConferenceonWeb signalsortheuseofcertaincategoriesofwords.Anothersignifi- SearchandDataMining(WSDM’24),March4–8,2024,Merida,Mexico.ACM, cantchallengeariseswhenplatformslackhigh-qualityannotated NewYork,NY,USA,10pages.https://doi.org/10.1145/3616855.3635771 datafortraining,leadingtoaneedforcross-platformmodelsthat canadapttodifferentdistributionshifts.Ourresearchintroduces

## Benchmark Evidence Lines
- enhancedefficacycomparedtoexistingstate-of-the-artmethodsin andhatecrimes[1,41].Thus,giventheheinouseffectsandthe
- hinderstheperformanceoftheexistingmodelsistheover-reliance challenges posed by existing state-of-the-art models that strive
- state-of-the-artmodelsoverlyrelyonidentitywords(e.g.,"jews") limitations.Aprevalentandproventechniqueforconstructinga
- CATCHoutperformsthestate-of-the-artbaselines. usingdatafromtheirsocialcontextandtheirprofiles.However,
- currentstate-of-the-art(SOTA)modelstrainedonspecifictopics
- teXplain[29]isimprovedwithanemphasisonathree-classclas-
- dataobtainedfromasingleplatformandassessedagainsttestsets 4
- comparedusingthemacro-F1measureasabenchmarkinTable1. 0 0

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
