---
created: 2026-04-23
updated: 2026-04-23
tags: [paper, deep-ingest-v2, hate-speech, cross-lingual, benchmark]
sources: [raw/sources/de Gibert 等 - 2018 - Hate Speech Dataset from a White Supremacy Forum.pdf]
---

# de Gibert 等 - 2018 - Hate Speech Dataset from a White Supremacy Forum

## Metadata
- Source file: `raw/sources/de Gibert 等 - 2018 - Hate Speech Dataset from a White Supremacy Forum.pdf`
- Year: 2018
- Pages: 10
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Considerthefollowing2: web content on social media, the amount of (1) “Godblessthemall,tohellwiththeblacks” hate speech is also steadily increasing.
- Over the past years, interest in online hate speech Thissentenceclearlycontainshatespeechagainst detection and, particularly, the automation of a target group because of their skin colour.
- How- this task has continuously grown, along with ever, the identification of hate speech is often not the societal impact of the phenomenon.

## Method
- The paper also provides a Silva et al., 2016; Davidson et al., 2017), which thoughtfulqualitativeandquantitativestudyof woulddefinehatespeechasa)adeliberateattack, the resulting dataset and several baseline ex- perimentswithdifferentclassificationmodels.
- ThetoolispublishedasanAPIandgivesa belled hate speech dataset; this includes the de- toxicityscorebetween0and100usingamachine signoftheannotationguidelines,theresultingcri- learning model.
- Such model has been trained on teria,theinter-annotatoragreementandaquantita- thousands of comments manually labelled by a tivedescriptionoftheresultingdataset;next,Sec- team of people8; to our knowledge, the resulting tion 4 presents several baseline experiments with datasetisnotpubliclyavailable.
- different classification models using the labelled Thedetectionofhatespeechhasbeentackledin data; finally,Section5providesabriefdiscussion three main different ways.

## Data and Evaluation Setup
- Besides defining hate speech paper describes a hate speech dataset com- as a verbal abuse directed to a group of people posed of thousands of sentences manually la- because of specific characteristics, other defini- belled as containing hate speech or not.
- The paper also provides a Silva et al., 2016; Davidson et al., 2017), which thoughtfulqualitativeandquantitativestudyof woulddefinehatespeechasa)adeliberateattack, the resulting dataset and several baseline ex- perimentswithdifferentclassificationmodels.
- b)directedtowardsaspecificgroupofpeople,and Thedatasetispubliclyavailable.
- 1 Introduction This paper presents the first public dataset of hate speech annotated on Internet forum posts in The rapid growth of content in social networks English at sentence-level.

## Results and Claims
- Over the past years, interest in online hate speech Thissentenceclearlycontainshatespeechagainst detection and, particularly, the automation of a target group because of their skin colour.
- Finally, the dataset has been contrasted against The difference of the PMI value of a word w and the English vocabulary in Hatebase.
- Ontheotherhand,theleasthatefulwords experiments just use the provided dataset and are neutral in this regard and belong to the se- well-knownapproachesfromtheliteraturetopro- manticfieldsofInternet, ortemporalexpressions, vide a baseline for further research and improve- among others.

## Limitations and Follow-ups
- Itcanhappentohumanannotators anycase,despitetheeffortstomaketheannotation and, of course, to automatic classifiers, as con- guidelinesasclear,rationalandcomprehensiveas firmed in the error analysis (Section 4.3).
- Challengesindis- tectiononTwitter.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: cross-lingual
- Mentioned datasets: stormfront, twitter
- Mentioned metrics: accuracy, precision, recall

## Abstract (Extracted)
> Abstract Although there is no universal definition for hate speech, the most accepted definition is pro- Hatespeechiscommonlydefinedasanycom- vided by Nockleby (2000): “any communication munication that disparages a target group of that disparages a target group of people based on people based on some characteristic such as somecharacteristicsuchasrace,colour,ethnicity, race, colour, ethnicity, gender, sexualorienta- gender,sexualorientation,nationality,religion,or tion,nationality,religion,orothercharacteris- tic. Duetothemassiveriseofuser-generated othercharacteristic”. Considerthefollowing2: web content on social media, the amount of (1) “Godblessthemall,tohellwiththeblacks” hate speech is also steadily increasing. Over the past years, interest in online hate speech Thissentenceclearlycontainshatespeechagainst detection and, particularly, the automation of a target group because of their skin colour. How- this task has continuously grown, along with ever, the identification of hate speech is often not the societal impact of the phenomenon. This so straightforward. Besides defining

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[hate-speech-research-map]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-datasets-and-benchmarks]]
