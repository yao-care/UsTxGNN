---
layout: default
title: Aprepitant
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
monitor_inn: "APREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
last_modified_at: 2026-10-14
description: "Aprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not available in the compiled data"
---

# Aprepitant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Aprepitant: From Chemotherapy-Related Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Aprepitant is a substance P/NK1 receptor antagonist. The data compiled for this report do not include its approved indication text, but its marketed forms (oral capsules, fosaprepitant injection and emulsion products) are antiemetic products.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (US license records contain no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 14) |
| Number of NDAs | 14 (listed authorizations, including NDAs and ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, aprepitant is a substance P/NK1 receptor antagonist.

NSIAD is caused by gain-of-function variants of the vasopressin V2 receptor, which lead to water retention and low blood sodium. No established link connects NK1 receptor antagonism to this mechanism. The very high score from the TxGNN model (deep learning) (0.9997, rank 1274) may reflect similarities the model learned between related diseases, not biological evidence.

This prediction should therefore be treated as a hypothesis only. The mechanistic rationale is weak, and there is no clinical or literature support in the compiled data.

Other top-ranked predictions have no better support. They include hypertrichosis, pulmonary hypertension, leprosy, Ambras-type hypertrichosis, a malformation syndrome with a dental/periodontal component, kyphoscoliotic heart disease, a Dandy-Walker malformation syndrome, subarachnoid hemorrhage and isolated genetic hair shaft abnormality. Only pulmonary hypertension and subarachnoid hemorrhage have weak biological plausibility, through substance P signaling and neurogenic inflammation. None has direct clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction (NSIAD).

For the third-ranked prediction, pulmonary hypertension, one publication was automatically matched (PMID [28261651](https://pubmed.ncbi.nlm.nih.gov/28261651/), 2016, *Oncology and Therapy*). It is a Phase I pazopanib plus cisplatin dose-escalation trial in advanced solid tumours. It does not involve aprepitant or pulmonary hypertension and is considered an irrelevant match.

## US Market Information

The compiled data list 14 US authorizations, all with cancelled status and no indication text. The main ones are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021549 | EMEND | Capsule | Not available |
| NDA207865 | EMEND | Powder, for suspension | Not available |
| NDA209296 | CINVANTI | Injection, emulsion | Not available |
| NDA216457 | APONVIE | Emulsion | Not available |
| ANDA207777 | Aprepitant (Glenmark) | Capsule | Not available |

The remaining authorizations are generic aprepitant capsules and generic fosaprepitant lyophilized injections.

## Safety Considerations

- **Disease-level contraindication signal (knowledge graph)**: liver failure. This comes from the knowledge graph, not from label text.
- **Drug Interactions**: 100 interactions were found. Examples of **Major** interactions include fentanyl, alfentanil and acalabrutinib. **Moderate** examples include paclitaxel, abemaciclib, nifedipine, ibuprofen, hydrocortisone, levonorgestrel, fluvoxamine, fosphenytoin, gefitinib, rabeprazole, lidocaine and albendazole. Dolutegravir is a **Minor** interaction.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or relevant literature, and no plausible mechanistic link between NK1 antagonism and the V2 receptor gain-of-function that causes NSIAD. The compiled US regulatory records also show only cancelled licenses.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to enable mechanistic-link analysis
- Original approved indication text and current US marketing status confirmation
- Targeted literature and trial searches for aprepitant or NK1 antagonists in NSIAD or hyponatraemia, and preclinical data if any exist
- Review of the other top predictions, with subarachnoid hemorrhage and pulmonary hypertension the only ones with weak biological plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

