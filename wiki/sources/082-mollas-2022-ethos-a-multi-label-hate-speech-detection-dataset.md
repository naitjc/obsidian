---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, multimodal, benchmark]
sources: [raw/sources/Mollas 等 - 2022 - ETHOS a multi-label hate speech detection dataset.pdf]
---

# Mollas 等 - 2022 - ETHOS a multi-label hate speech detection dataset

## Metadata
- Source file: `raw/sources/Mollas 等 - 2022 - ETHOS a multi-label hate speech detection dataset.pdf`
- Year: 2022
- Pages: 16
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- keeps the smallest unit containing hate speech and reduces noise.
- anyinformationastobeaccordinglyclassified.Furthermore, There is clearly a lot of work and numerous publicly informationlikethepost-identifierandthesentence’sposi- available datasets for hate speech identification.
- The label ‘isHate’ was the result tively.AllthisinformationisalsovisibleinFig.4.InTable2, of summing up the positive votes P 1,i of the contributors, the balance between hate speech categories (last column) divided by N , so its values are within the range of [0,1].

## Method
- almost every country has responded by drawing up corre- spondinglegalframeworks,whileresearchwhichisrelatedto (co)winningCrowdFlower’sAIforEveryoneChallengeforQ4of mechanismsthattrytoremedysuchphenomenahasrecently 2017:https://prn.to/2KVWubz.
- wastackledbetterbysingle-tasklanguagemodels,therest4 The overview of the proposed annotation protocol is visu- classificationtasks,whichincludedatleast5labelgradations, alised through a flowchart in Fig.
- The finally obtained wereclearlyboostedviamultitasksingle/multi-languageor dataset is the outcome of a three-stage process, which we single/multi-lingualmodels.
- The locally retained pre-trained batches of files regarding Reddit comments on a monthly ML model predicts the class of each comment, exporting basis.

## Data and Evaluation Setup
- while learning from short-text segments is blooming in the AsimpleapplicationthatusestheMLLschemaprovided lastyears[51].Twoofthemostimportantfeaturesaccompa- bytheproposedHSdatasetcouldbeanassistancesystemfor nyingtheshort-textsegments,sparseness,andthepresenceof humanstaffreviewingcommentsonsocialmediaplatforms.
- contains numerous manually created HS datasets [58,61].
- minethebaselineperformanceofthisparticulardatasetusing Labeldependenciesandthesemanticoverlapthatoccurson state-of-the-art (SOTA) techniques.
- Experiments using Transformers (BERT (multi-labElhaTespeecHdetectiOndataSet).Finally,afew andDistilBERT)werealsoincluded,becausetheyappearto literaturegapsarepresentedinthelastparagraphofthissec- beextremelypromisinginmanytext-relatedmachinelearn- tion.

## Results and Claims
- minethebaselineperformanceofthisparticulardatasetusing Labeldependenciesandthesemanticoverlapthatoccurson state-of-the-art (SOTA) techniques.
- The NNs seem to iments in this stage: Multinomial and Bernoulli variations outperformtheconventionalMLtechniques.Itisworthmen- of Naive Bayes (MNB and BNB, respectively) [31], LR, tioningthatBayesianlearnershadthelowestperformancein SVMs, RF, and Gradient Boosting (Grad) [13].
- However, in terms of didnotmanagetogetimprovedregardingthepredictiveness accuracy,ahigherscoreisobtainedbyrandomdatasets.We ofHSinstances.

## Limitations and Follow-ups
- almost every country has responded by drawing up corre- spondinglegalframeworks,whileresearchwhichisrelatedto (co)winningCrowdFlower’sAIforEveryoneChallengeforQ4of mechanismsthattrytoremedysuchphenomenahasrecently 2017:https://prn.to/2KVWubz.
- willbemorehelpfulforthereadertoconcludeandcondemn To achieve high performance in real-world tasks, AI itforcontainingHSratherthanbeingpresentedwithasingle methodologies require balanced, accurate, and unbiased label (e.g., ‘may contain HS’:{‘yes’,‘no’}).
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: multimodal
- Mentioned datasets: ethos, gab, stormfront, twitter, reddit
- Mentioned metrics: f1, accuracy, precision, recall

## Abstract (Extracted)
> Abstract Onlinehatespeechisarecentprobleminoursocietythatisrisingatasteadypacebyleveragingthevulnerabilitiesofthe corresponding regimes that characterise most social media platforms. This phenomenon is primarily fostered by offensive comments,eitherduringuserinteractionorintheformofapostedmultimediacontext.Nowadays,giantcorporationsown platformswheremillionsofuserslogineveryday,andprotectionfromexposuretosimilarphenomenaappearstobenecessary tocomplywiththecorrespondinglegislationandmaintainahighlevelofservicequality.Arobustandreliablesystemfor detectingandpreventingtheuploadingofrelevantcontentwillhaveasignificantimpactonourdigitallyinterconnectedsociety. Severalaspectsofourdailylivesareundeniablylinkedtooursocialprofiles,makingusvulnerabletoabusivebehaviours.As aresult,thelackofaccuratehatespeechdetectionmechanismswouldseverelydegradetheoveralluserexperience,although its erroneous operation would pose many ethical concerns. In this paper, we present ‘ETHOS’ (multi-labEl haTe speecH detectiOn dataSet), a textual dataset with two variants: binary and multi-label, based on YouTube and 

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-datasets-and-benchmarks]]
