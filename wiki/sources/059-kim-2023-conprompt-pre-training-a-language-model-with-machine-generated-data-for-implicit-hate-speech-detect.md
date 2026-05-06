---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, contrastive-learning, retrieval, prompting, counterfactual, explainability]
sources: [raw/sources/Kim 等 - 2023 - ConPrompt Pre-training a Language Model with Machine-Generated Data for Implicit Hate Speech Detect.pdf]
---

# Kim 等 - 2023 - ConPrompt Pre-training a Language Model with Machine-Generated Data for Implicit Hate Speech Detect

## Metadata
- Source file: `raw/sources/Kim 等 - 2023 - ConPrompt Pre-training a Language Model with Machine-Generated Data for Implicit Hate Speech Detect.pdf`
- Year: 2023
- Pages: 17
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- While 55 somepre-trainedlanguagemodelshavebeen 50 IHC SBIC-h DH developedforhatespeechdetection,theyare Evaluation dataset not specialized in implicit hate speech.
- Weanalyzetherepresentation qualityofTOXIGEN-CONPROMPTandshow itsabilitytoconsidertargetgroupandtoxicity, whicharedesirablefeaturesintermsofimplicit hatespeeches.1 1 Introduction Warning: thispapercontainscontentthatcanbe offensiveandupsetting.
- For example, we as a society should not take care of those with mental illness is an example of implicit hate speech targeting ∗ The work was done when Youngwook Kim was in YonseiUniversity.

## Method
- While 55 somepre-trainedlanguagemodelshavebeen 50 IHC SBIC-h DH developedforhatespeechdetection,theyare Evaluation dataset not specialized in implicit hate speech.
- Re- cently, animplicithatespeechdatasetwitha massivenumberofsampleshasbeenproposed bycontrollingmachinegeneration.Wepropose apre-trainingapproach,CONPROMPT,tofully leveragesuchmachine-generateddata.
- Specifi- cally,givenamachine-generatedstatement,we use example statements of its origin prompt as positive samples for contrastive learning.
- Through pre-training with CONPROMPT, we presentTOXIGEN-CONPROMPT,apre-trained languagemodelforimplicithatespeechdetec- tion.

## Data and Evaluation Setup
- While 55 somepre-trainedlanguagemodelshavebeen 50 IHC SBIC-h DH developedforhatespeechdetection,theyare Evaluation dataset not specialized in implicit hate speech.
- Re- cently, animplicithatespeechdatasetwitha massivenumberofsampleshasbeenproposed bycontrollingmachinegeneration.Wepropose apre-trainingapproach,CONPROMPT,tofully leveragesuchmachine-generateddata.
- The performance of the pre- trainedmodelsseverelydropsoncross-datasetevalua- tion,althoughalldatasetstargetthesametask(implicit hate speech detection).
- Each model is fine-tuned on IMPLICITHATECORPUS(IHC)dataset.

## Results and Claims
- Onepossiblewaytoimprovethegeneralization abilityisfurtherpre-trainingmodelsontherelevant largecorpus.
- Specifically, we present CON- TOXIGEN-CONPROMPTconsistentlyoutperforms PROMPT 3,apre-trainingapproachwhichutilizes other pre-trained language models.
- thedataset(e.g.,toxicstatementsinimplicitforms (2) We present TOXIGEN-CONPROMPT, a pre- against Mentally Disabled).

## Limitations and Follow-ups
- For relyonspuriouscorrelationssuchasidentityterm example, given a set of examples with {implicit, bias(i.e.,classifyingatextashatefuljustbecause Asian,toxic}propertiesasaprompt,GPT-3tends ofthepresenceofidentitytermssuchasAsian).
- igates the identity term bias compared to BERT, 3Contrastive learning approach leveraging machine- generatedstatementanditsoriginPrompt.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: contrastive-learning, retrieval, prompting, counterfactual, multimodal, explainability
- Mentioned datasets: toxigen, gab, stormfront, twitter, reddit
- Mentioned metrics: f1

## Abstract (Extracted)
> Abstract 80 75 Implicithatespeechdetectionisachallenging 70 65 taskintextclassificationsincenoexplicitcues 60 (e.g., swear words) exist in the text. While 55 somepre-trainedlanguagemodelshavebeen 50 IHC SBIC-h DH developedforhatespeechdetection,theyare Evaluation dataset not specialized in implicit hate speech. Re- cently, animplicithatespeechdatasetwitha massivenumberofsampleshasbeenproposed bycontrollingmachinegeneration.Wepropose apre-trainingapproach,CONPROMPT,tofully leveragesuchmachine-generateddata. Specifi- cally,givenamachine-generatedstatement,we use example statements of its origin prompt as positive samples for contrastive learning. Through pre-training with CONPROMPT, we presentTOXIGEN-CONPROMPT,apre-trained languagemodelforimplicithatespeechdetec- tion. Weconductextensiveexperimentsonsev- eralimplicithatespeechdatasetsandshowthe superior generalization ability of TOXIGEN- CONPROMPT compared to other pre-trained models.Additionally,weempiricallyshowthat CONPROMPTiseffectiveinmitigatingidentity termbias,demonstratingthatitnotonlymakes a model more generalizable but also r

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[multimodal-hate-detection]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
