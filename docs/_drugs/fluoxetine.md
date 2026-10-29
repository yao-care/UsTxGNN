---
layout: default
title: Fluoxetine
parent: Model Prediction Only (L5)
nav_order: 724
evidence_level: L5
indication_count: 9
monitor_inn: "FLUOXETINE"
predicted_indications: ["histrionic personality disorder (disease)", "schizotypal personality disorder", "schizoid personality disorder", "paranoid personality disorder", "benign paroxysmal torticollis of infancy", "agoraphobia", "manic bipolar affective disorder", "phobic disorder", "Ohdo syndrome and variants"]
last_modified_at: 2026-10-30
description: "Fluoxetine: predicted new indication Histrionic personality disorder (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Fluoxetine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Fluoxetine: Histrionic personality disorder (disease)
{: .text-alpha }

## One-Sentence Summary

Fluoxetine is a widely marketed serotonin-reuptake-inhibitor antidepressant.
The TxGNN model predicts it may be effective for **histrionic personality disorder**, with a very high score (0.9992).
However, there are **0 clinical trials** and **2 publications**, and neither publication studies this disease, so the prediction currently rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Histrionic personality disorder (disease) |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of NDAs | at least 12 |
| Number of Approvals | At least 12 ANDAs (the list may be partial) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Fluoxetine belongs to the selective serotonin reuptake inhibitor (SSRI) class. Its use in mood and anxiety disorders is recorded in the knowledge graph, and mechanistically it may be applicable to personality-disorder symptoms driven by serotonin signalling.

The plausible link is that serotonergic modulation could ease affective lability and impulsivity, which are features sometimes seen in histrionic personality disorder. No direct link between fluoxetine and this disorder is documented, though. The high TxGNN score is a computational prediction without clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28791577](https://pubmed.ncbi.nlm.nih.gov/28791577/) | 2018 | Case report | Neuropsychiatrie | A 37-year-old woman with body dysmorphic disorder, admitted for an eating disorder. It does not address histrionic personality disorder or fluoxetine efficacy. |
| [11865567](https://pubmed.ncbi.nlm.nih.gov/11865567/) | 2001 | Review / case report | L'Encephale | Psychiatric manifestations of lupus and Sjögren's syndrome, with a case treated with cyclophosphamide. It does not address histrionic personality disorder. |

Neither publication directly studies the predicted disease.

---

## US Market Information

Approved-indication text is not available in the records compiled for this report. Twelve valid single-ingredient ANDA records were listed, and the list may be partial. The five shown here are the main ones.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA078619 | Fluoxetine (Aurobindo Pharma Limited) | Capsule |
| ANDA075525 | Fluoxetine (Saptalis Pharmaceuticals, LLC.) | Solution |
| ANDA075452 | Fluoxetine (Teva Pharmaceuticals USA, Inc.) | Capsule |
| ANDA213286 | Fluoxetine (Aurobindo Pharma Limited) | Tablet, film coated |
| ANDA209695 | Fluoxetine (Nivagen Pharmaceuticals, Inc.) | Tablet |

---

## Safety Considerations

- **Contraindication-type relations in the knowledge graph (not label text):** The graph links fluoxetine to the following conditions:
  - Neurological and cardiovascular: epilepsy, orthostatic hypotension and other hypotensive disorders, stroke and cerebrovascular disorders, myocardial infarction.
  - Hepatic and blood: liver failure, liver disease, cirrhosis, neutropenia, agranulocytosis, blood coagulation disease.
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperlipidemia, obesity.
  - Psychiatric: bipolar disorder.
  - Other: benign prostatic hyperplasia, gallbladder disease, female breast carcinoma.

  These should be verified against the package insert.
- **Drug Interactions:** 100 interactions were found in total. Major-level interactions in the first 20 reviewed include bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron and cisapride. Moderate interactions include aspirin, morphine, clarithromycin and famotidine, among others.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials, and neither retrieved publication studies histrionic personality disorder. Because no cited study addresses this disease, the evidence level is L5.

**To proceed, the following is needed:**
- Any direct clinical evidence (trials, case series or controlled studies) of fluoxetine in histrionic personality disorder
- FDA package insert warnings and contraindications, to complete safety screening
- Detailed mechanism of action data to support the serotonergic hypothesis
- A comparison with other predicted indications for fluoxetine that have more direct supporting studies, such as schizotypal personality disorder, to decide where to prioritise effort
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

