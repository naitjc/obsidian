---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark, contrastive-learning, retrieval, graph, prompting, explainability]
sources: [raw/sources/Cai 等 - 2025 - Unpacking Hateful Memes Presupposed Context and False Claims.pdf]
---

# Cai 等 - 2025 - Unpacking Hateful Memes Presupposed Context and False Claims

## Metadata
- Source file: `raw/sources/Cai 等 - 2025 - Unpacking Hateful Memes Presupposed Context and False Claims.pdf`
- Year: 2025
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- France online hate speech law to force social media sites to act quickly.
- Study finds persistent spike in hate speech on [16] RuiCao,RoyKa-WeiLee,Wen-HawChong,andJingJiang.2023.Promptingfor X.

## Method
- detectionframeworkdesignedtocapturethefundamentalnature of hate.
- degreeandrhetoricalform,alltypesofhateshareacommonkey PriorworkhasshownthatPLMsimplicitlyencodesyntacticstruc- feature:thepresenceofapresupposedevaluativecontext.InSHIELD, tures[22],whichcancapturethepresupposedcontextincertain thisismodeledviaPCMinSection4.1.
- bonemodelforaddressingthehatefulmemeclassificationtask.In contrast,PromptHateandExplainHMunderperformmainlydue 5.1.2 Baselines.
- ForQ2,wedesigntheFine-tunedMLPapproach,wherethelast 5.2 RQ1:HatefulMemeClassification hiddenstateofLLMisfedintoanMLPforbinaryclassification.

## Data and Evaluation Setup
- Extensive experiments show that SHIELD outperforms state-of-the-artmethodsacrossdatasetsandmetrics,whiledemon- nowoftenreferstohumorousorsatiricalimage-textcombinations stratingversatilityonothertasks,suchasfakenewsdetection.
- where𝜎representsthesigmoidfunction;𝑦˜isthepredictedlabel, RQ3: HowwelldoesSHIELDcapturetheessentialcharacteristics withavalueof1indicatingahatefulmemeand0otherwise.
- tectionperformance,itseffectivenessmaybelimitedincertain cases.Inthefalseclaimdetectionscenario,thelabelofagraphmay Table1:Summaryofhatefulmemedatasets.
- bonemodelforaddressingthehatefulmemeclassificationtask.In contrast,PromptHateandExplainHMunderperformmainlydue 5.1.2 Baselines.

## Results and Claims
- Extensive experiments show that SHIELD outperforms state-of-the-artmethodsacrossdatasetsandmetrics,whiledemon- nowoftenreferstohumorousorsatiricalimage-textcombinations stratingversatilityonothertasks,suchasfakenewsdetection.
- 4.4 AnalysisoftheReferenceGraph RQ4: HowdoesSHIELDperformonothermultimodalsocialmedia Whileconstructinganexplicitreferencegraphcanimprovede- taskssuchasfakenewsdetection?
- (3) SHIELD:Usingallmodulesbyfeedingthecompleterepre- (2)Despitetexttruncation,SHIELDoutperformsbaselinesonmost sentationℎintotheclassifier.

## Limitations and Follow-ups
- However,insomecases,therapidspreadofmemeshasbeen Disclaimer:Thispapercontainsdiscriminatorycontentthatmaybe exploitedtodisseminatehate,reinforcingsocietalbiasesandthreat- disturbingtosomereaders.
- poor,likelyduetoLLM’sinherentbiasinconceptualizinghatefulor thehallucinationsleadingtomisinterpretationsofmemes[25,32].
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, graph, prompting, multimodal, explainability
- Mentioned datasets: ethos, hateful memes, gab, twitter, reddit
- Mentioned metrics: f1, macro-f1, accuracy, precision, recall, auc

## Abstract (Extracted)
> Abstract Whilememesareoftenhumorous,theyarefrequentlyusedtodis- seminate hate, causing serious harm to individuals and society. Currentapproachestohatefulmemedetectionmainlyrelyonpre- trainedlanguagemodels.However,lessfocushasbeendedicatedto whatmakeamemehateful.Drawingoninsightsfromphilosophy andpsychology,wearguethathatefulmemesarecharacterizedby twoessentialfeatures:apresupposedcontextandtheexpression offalseclaims.Tocapturepresupposedcontext,wedevelopPCM formodelingcontextualinformationacrossmodalities.Todetect falseclaims,weintroducetheFACTmodule,whichintegratesex- ternalknowledgeandharnessescross-modalreferencegraphs.By combiningPCMandFACT,weintroduceSHIELD,ahatefulmeme Figure1:Anexampleofahatefulmeme.Memetext:goodguypolice officer,capturingthemyoung. detectionframeworkdesignedtocapturethefundamentalnature of hate. Extensive experiments show that SHIELD outperforms state-of-the-artmethodsacrossdatasetsandmetrics,whiledemon- nowoftenreferstohumorousorsatiricalimage-textcombinations stratingversatilityonothertasks,suchasfakenewsdetection. thatconveyindividualideologiesandrapidlye

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
