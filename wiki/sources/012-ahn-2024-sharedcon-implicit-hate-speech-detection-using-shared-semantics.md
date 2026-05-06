---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, contrastive-learning, causal, prompting, explainability]
sources: [raw/sources/Ahn 等 - 2024 - SharedCon Implicit Hate Speech Detection using Shared Semantics.pdf]
---

# Ahn 等 - 2024 - SharedCon Implicit Hate Speech Detection using Shared Semantics

## Metadata
- Source file: `raw/sources/Ahn 等 - 2024 - SharedCon Implicit Hate Speech Detection using Shared Semantics.pdf`
- Year: 2024
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Recent studies suggest that classifyinghatefulpostsinjustabinaryman- ner may not adequately address the nuanced task of detecting implicit hate speech.
- Pre- methodologythatisnotdependentonhuman- viousstudiessuggestedmodelsforidentifyingim- writtenormachine-generatedaugmenteddata plicit hate speech (Sridhar and Yang, 2022; Lin, fortraining.
- Implicit hate speech, in particular, often thedatasets.

## Method
- Asthistaskisakintobinaryclassi- fication,oneofthepromisingapproachesfor hatespeechdetectionistheutilizationofcon- trastive learning.
- Previousstudiesproposedamodified Figure1: Anexampleofsharedsemanticsamongposts contrastive learning approach equipped with intheIHCdataset.
- While lightedportionrepresentsthecommonmeaningshared thisapproachcanpotentiallyenhancetheover- amongtheseposts.
- Pre- methodologythatisnotdependentonhuman- viousstudiessuggestedmodelsforidentifyingim- writtenormachine-generatedaugmenteddata plicit hate speech (Sridhar and Yang, 2022; Lin, fortraining.

## Data and Evaluation Setup
- Previousstudiesproposedamodified Figure1: Anexampleofsharedsemanticsamongposts contrastive learning approach equipped with intheIHCdataset.
- (2022) showed the impor- paredtoothertasksduetoitsvaryingperception tanceofthemodel’sgeneralizationatimplicithate anddefinitionamongindividuals,whichisreflected speechdetectionandproposedacontrastivelearn- intheinconsistenciesbetweendatasets(Luoetal., ingapproachthatutilizescommonimplicationsin 2023).
- Implicit hate speech, in particular, often thedatasets.
- Althoughtheirapproachshowsgood lacksexplicitcuessuchasswearwordsorinsults, performanceforin-dataset,usingimplicationsof in-dataset makes it difficult for them to perform 1Ourcodeisavailableathttps://github.com/hsannn/ sharedcon.

## Results and Claims
- Experimental results trastive learning (CL) with humman-written im- demonstratethatSharedConoutperformsourbase- plicationsormachine-generatedaugmentedtexts.
- lineswitha0.43%paverageimprovementinthein- However, there are some limitations to these ap- datasetsettingand1.43%paverageimprovement proaches: (1)Itrequiresexpertstomanuallygener- inthecross-datasetsetting.
- Wethentrainthe c k • We achieve performance that is comparable modeltobringpostswithinthesameclustercloser to and in some cases, even outperforms the togetherandtopushpostsfromdifferentclusters currentSOTAmodel,allwithouttheneedfor apart.

## Limitations and Follow-ups
- This challenge is largely due to the subtle nature andcontextdependencyofsuchpejorativere- marks.
- lineswitha0.43%paverageimprovementinthein- However, there are some limitations to these ap- datasetsettingand1.43%paverageimprovement proaches: (1)Itrequiresexpertstomanuallygener- inthecross-datasetsetting.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, causal, prompting, multimodal, explainability, cross-lingual
- Mentioned datasets: gab, founta, twitter
- Mentioned metrics: f1, macro-f1

## Abstract (Extracted)
> Abstract Theever-growingpresenceofhatespeechon socialnetworkservicesandotheronlineplat- formsnotonlyfuelsonlineharassmentbutalso presentsagrowingchallengeforhatespeech detection. Asthistaskisakintobinaryclassi- fication,oneofthepromisingapproachesfor hatespeechdetectionistheutilizationofcon- trastive learning. Recent studies suggest that classifyinghatefulpostsinjustabinaryman- ner may not adequately address the nuanced task of detecting implicit hate speech. This challenge is largely due to the subtle nature andcontextdependencyofsuchpejorativere- marks. Previousstudiesproposedamodified Figure1: Anexampleofsharedsemanticsamongposts contrastive learning approach equipped with intheIHCdataset. Weoftenfindarepresentativepost additional aids such as human-written impli- amongpostssharingsimilarsemantics,whichismore cationsormachine-generatedaugmenteddata accurate than human-written implications. The high- forbetterimplicithatespeechdetection. While lightedportionrepresentsthecommonmeaningshared thisapproachcanpotentiallyenhancetheover- amongtheseposts. all performance by its additional 

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
