---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, prompting, explainability]
sources: [raw/sources/Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection.pdf]
---

# Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection

## Metadata
- Source file: `raw/sources/Hartvigsen 等 - 2022 - ToxiGen A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection.pdf`
- Year: 2022
- Pages: 18
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- TOXIGEN: A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection Warning:thispaperdiscussesandcontainscontentthatcanbeoffensiveorupsetting.
- Impor- struggle with detecting implicitly toxic lan- tantly,suchbiasesintoxicitydetectionriskfurther guage.
- While such human-like bias and toxicity ing subset of TOXIGEN and find that annota- posesrealthreats,weusethisundesirablebehavior torsstruggletodistinguishmachine-generated inmodelslikeGPT-3toimproveexistingtoxiclan- text from human-written language.

## Method
- We de- velopademonstration-basedpromptingframe- Weintroduce TOXIGEN,alarge-scalemachine- work and an adversarial classifier-in-the-loop generateddatasetof274,186toxicandbenignstate- decodingmethodtogeneratesubtlytoxicand ments.
- To create this dataset, we leverage the benigntextwithamassivepretrainedlanguage massivepretrainedlanguagemodelGPT-3(Brown model (Brown et al., 2020).
- While such human-like bias and toxicity ing subset of TOXIGEN and find that annota- posesrealthreats,weusethisundesirablebehavior torsstruggletodistinguishmachine-generated inmodelslikeGPT-3toimproveexistingtoxiclan- text from human-written language.
- Using basedpromptingandpretrainedtoxicityclassifiers, threepublicly-availabledatasets,weshowthat finetuning a toxicity classifier on our data im- TOXIGENcoversover135ktoxicand135kbenign provesitsperformanceonhuman-writtendata statementsabout13minorityidentitygroups(e.g., substantially.

## Data and Evaluation Setup
- TOXIGEN: A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection Warning:thispaperdiscussesandcontainscontentthatcanbeoffensiveorupsetting.
- To help mitigate these issues, we cre- marginalizingorcensoringminoritygroups(Yasin, ateTOXIGEN,anewlarge-scaleandmachine- 2018;Sapetal.,2019;DiasOlivaetal.,2020;Are, generated dataset of 274k toxic and benign 2020;DíazandHecht-Felella,2021).
- We de- velopademonstration-basedpromptingframe- Weintroduce TOXIGEN,alarge-scalemachine- work and an adversarial classifier-in-the-loop generateddatasetof274,186toxicandbenignstate- decodingmethodtogeneratesubtlytoxicand ments.
- To create this dataset, we leverage the benigntextwithamassivepretrainedlanguage massivepretrainedlanguagemodelGPT-3(Brown model (Brown et al., 2020).

## Results and Claims
- While such human-like bias and toxicity ing subset of TOXIGEN and find that annota- posesrealthreats,weusethisundesirablebehavior torsstruggletodistinguishmachine-generated inmodelslikeGPT-3toimproveexistingtoxiclan- text from human-written language.
- GEN can be used to fight machine-generated Usingthismachinegeneratedapproachhastwo toxicity as finetuning improves the classifier advantages over scraping posts from the web as significantly on our evaluation subset.
- fine-tuning existing classifiers on TOXIGEN con- Togenerateachallengingsubsetof TOXIGEN, sistentlyimprovesperformance(+7–19%)on3ex- weintroduce ALICE,2 anadversarialclassifier-in- isting human-written implicit toxic datasets: Im- the-loop decoding algorithm.

## Limitations and Follow-ups
- Impor- struggle with detecting implicitly toxic lan- tantly,suchbiasesintoxicitydetectionriskfurther guage.
- While such human-like bias and toxicity ing subset of TOXIGEN and find that annota- posesrealthreats,weusethisundesirablebehavior torsstruggletodistinguishmachine-generated inmodelslikeGPT-3toimproveexistingtoxiclan- text from human-written language.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: prompting, explainability
- Mentioned datasets: toxigen, gab, stormfront, founta, twitter, reddit
- Mentioned metrics: f1, auc

## Abstract (Extracted)
> Abstract Röttgeretal.,2021). Thiscanleadtosevereunder- detectionofsubtlehate(e.g.,“Theyhavebeenbred Toxiclanguagedetectionsystemsoftenfalsely to be good at sports and entertainment, but not flag text that contains minority group men- muchelse”;Figure1)andover-detectionofbenign tions as toxic, as those groups are often the targets of online hate. Such over-reliance on statements (e.g., “child abuse is wrong, racism spurious correlations also causes systems to is wrong, sexism is wrong”; Figure 1). Impor- struggle with detecting implicitly toxic lan- tantly,suchbiasesintoxicitydetectionriskfurther guage. To help mitigate these issues, we cre- marginalizingorcensoringminoritygroups(Yasin, ateTOXIGEN,anewlarge-scaleandmachine- 2018;Sapetal.,2019;DiasOlivaetal.,2020;Are, generated dataset of 274k toxic and benign 2020;DíazandHecht-Felella,2021). statements about 13 minority groups. We de- velopademonstration-basedpromptingframe- Weintroduce TOXIGEN,alarge-scalemachine- work and an adversarial classifier-in-the-loop generateddatasetof274,186toxicandbenignstate- decodingmethodtogeneratesubt

## Benchmark Evidence Lines
- the only thing that can be done to improve the situation is to put them all in 2% hate
- Togenerateachallengingsubsetof TOXIGEN, sistentlyimprovesperformance(+7–19%)on3ex-
- ityclassifieragainstatextgeneratorduringbeam et al., 2021). This indicates that the dataset gen-
- 2 ImplicitHateAgainstMinorityGroups
- Table 4: AUC for HateBert and RoBERTa both zero-
- Susan Benesch. 2020. Proposals for improved regula-
- ingtoxicspeechdetectorsagainstveiledtoxicity. In 2021. Agreeing to disagree: Annotating offensive

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-datasets-and-benchmarks]]
