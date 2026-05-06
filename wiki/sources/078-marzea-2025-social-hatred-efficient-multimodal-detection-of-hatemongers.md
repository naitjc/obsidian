---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, multimodal, cross-lingual, benchmark, graph, prompting, explainability]
sources: [raw/sources/Marzea 等 - 2025 - Social Hatred Efficient Multimodal Detection of Hatemongers.pdf]
---

# Marzea 等 - 2025 - Social Hatred Efficient Multimodal Detection of Hatemongers

## Metadata
- Source file: `raw/sources/Marzea 等 - 2025 - Social Hatred Efficient Multimodal Detection of Hatemongers.pdf`
- Year: 2025
- Pages: 15
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- In this work, we explore computational ap- (ii) We use the fixed threshold τU as a strong proachesthatcanbeusedtostudythephenomena baseline;however,amorecomprehensivecompari- atscale,ratherthanproposeafunctionalend-to-end sontootherexistingmethods(e.g.,diffusion-based contentmoderationsystem.
- efficacy of reddit’s 2015 ban examined through hate speech.
- Automated hate speech de- negative sampling strategies with momentum con- tection and the problem of offensive language.

## Method
- edgeorspecifictrainingdata.Allusions(#4-7)and twistedslogans(#7-8)furthercomplicatedetection Offensivecontentwarning:Theillustrativeex- forbothmodelsandhumans.Adetailedanalysis amplesthroughoutthemanuscript,andspecifically oftheseexamplesisprovidedinAppendixA.
- We propose a princi- proachcombiningpredictionsfromauser’sposts, pledwaytocombinepredictionsandmodalitiesfor followers,andfollowees.
- We propose a robust and efficient multi- et al., 2021; Utku et al., 2024).
- Early detection modal aggregative approach for detecting ofpotentialspreadersusingauthorprofilingtech- hate-mongers.

## Data and Evaluation Setup
- Table1:Examplesofhate-promotingtexts.DHB:deHateBERT(Aluruetal.,2020);JS:Google’sJigsaw;FTDB: DistillBERT fine-tuned on our datasets; GPT-4 & Gemini 1.5 Pro predictions (see Appendix B).
- Wedemonstratethebenefitsofcontextualag- RecentworkexploresusingLLMrationalesfor gregationoverthreeuniquedatasets(Twitter, interpretability(Nirmaletal.,2024),thoughfine- Gab,Parler).
- WeshareanovelannotateddatasetofParler nuanced tasks like hate detection (Ziems et al., hateusers.
- ThethresholdτU controlssensitivity(e.g.,τU = 1 for zero-tolerance4, higher values for repeated 3.2 Socially-awareBaselines offenders).WedenotethisclassificationC F .

## Results and Claims
- ofillustrativecases.Ourmethodcanbeusedto improvetheclassificationofcodedmessages, Table1providesexamplesillustratingthesechal- dog-whistling,andracialgas-lighting,aswell lenges.
- tunedmodelsoftenoutperformLLMsonsocially 3.
- Wecomparethemultimodalaggregationsagainst We propose more robust aggregations consid- anumberofstrongbaselinesthatleveragethenet- ering nuance and social context, training Θ (e.g., workstructure.

## Limitations and Follow-ups
- Node2Vec(GroverandLeskovec,2016):Em- →− followees u)ingraphG(V,E).Θ R (u)combines beddingsfrombiasedrandomwalks.
- cialnetworkdynamics,ourmethodachieveshigher Recognizingthelimitationsmentionedaboveis accuracy and robustness compared to traditional crucial for the ongoing development of more ef- text-only models.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: graph, prompting, multimodal, explainability, cross-lingual
- Mentioned datasets: gab, twitter, reddit
- Mentioned metrics: f1, accuracy, precision, recall, auc

## Abstract (Extracted)
> Abstract 2016;Davidsonetal.,2017).Onlinehateisoften linkedtoreal-worldviolence(Munn,2019;Male- Automatic detection of online hate speech vichandRobertso,2019;Thomas,2019;McIlroy- serves as a crucial step in the detoxification YoungandAnderson,2019;Mathewetal.,2019; of the online discourse. Moreover, accurate ADL,2023). classificationcanpromoteabetterunderstand- Hateisoftenpromotedbycommunities,rather ingoftheproliferationofhateasasocialphe- nomenon.Whilemostpriorworkfocusonthe than by isolated individuals. Shifting the focus detectionofhatefulutterances,wearguethat fromtheutterance(post)leveltotheuserandcom- focusingontheuser levelisasimportant,al- munity level can be beneficial: it may provide a beit challenging. In this paper we consider a better understanding of hate group dynamics; it multimodalaggregativeapproachforthedetec- could improve detection of coded language (dog tionofhate-mongers,takingintoaccountthe whistling, gas-lighting) at the post level; and it potentiallyhatefultexts,useractivity,andthe couldinforminterventionstrategies1 (Thomasand usernetwork.Evaluatingourmetho

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
