---
layout: default
title: Aprepitant
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
monitor_inn: "APREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
last_modified_at: 2026-11-20
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
| US Market Status | Marketed (active FDA-approved applications: 7 of 9) |
| Number of FDA Applications | 9 (active: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for aprepitant: "Aprepitant is a selective high-affinity antagonist of human substance P/neurokinin 1 (NK 1 ) receptors. Aprepitant has little or no affinity for serotonin (5-HT 3 ), dopamine, and corticosteroid receptors. Aprepitant has been shown in animal models to inhibit emesis induced by cytotoxic chemotherapeutic agents, such as cisplatin, via central actions." ([DailyMed: Cinvanti (aprepitant) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4c218d3a-a508-4abc-9ed8-a6e8e191d1b4), label version 2026-04-01; accessed 2026-11-19.) Based on general pharmacology, aprepitant is a substance P/NK1 receptor antagonist.

NSIAD is caused by gain-of-function variants of the vasopressin V2 receptor, which lead to water retention and low blood sodium. No established link connects NK1 receptor antagonism to this mechanism. The very high score from the TxGNN model (deep learning) (0.9997, rank 1274) may reflect similarities the model learned between related diseases, not biological evidence.

This prediction should therefore be treated as a hypothesis only. The mechanistic rationale is weak, and there is no clinical or literature support in the compiled data.

Other top-ranked predictions have no better support. They include hypertrichosis, pulmonary hypertension, leprosy, Ambras-type hypertrichosis, a malformation syndrome with a dental/periodontal component, kyphoscoliotic heart disease, a Dandy-Walker malformation syndrome, subarachnoid hemorrhage and isolated genetic hair shaft abnormality. Only pulmonary hypertension and subarachnoid hemorrhage have weak biological plausibility, through substance P signaling and neurogenic inflammation. None has direct clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction (NSIAD).

For the third-ranked prediction, pulmonary hypertension, one publication was automatically matched (PMID [28261651](https://pubmed.ncbi.nlm.nih.gov/28261651/), 2016, *Oncology and Therapy*). It is a Phase I pazopanib plus cisplatin dose-escalation trial in advanced solid tumours. It does not involve aprepitant or pulmonary hypertension and is considered an irrelevant match.

## US Market Information

The main ones are shown below.

<!-- review:begin us-lic-20261106-aprepitant-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The compiled data list 14 US authorizations, all with cancelled status and no indication text. The main ones are shown below." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-aprepitant-2 -->

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
The prediction is supported only by a model score. There are no trials or relevant literature, and no plausible mechanistic link between NK1 antagonism and the V2 receptor gain-of-function that causes NSIAD.

<!-- review:begin us-lic-20261031-aprepitant-1 -->

> **Review correction (2026-10-31)**: Originally stated: "There are no trials or relevant literature, and no plausible mechanistic link between NK1 antagonism and the V2 receptor gain-of-function that causes NSIAD. The compiled US regulatory records also show only cancelled licenses." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-aprepitant-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to enable mechanistic-link analysis
- Original approved indication text and current US marketing status confirmation
- Targeted literature and trial searches for aprepitant or NK1 antagonists in NSIAD or hyponatraemia, and preclinical data if any exist
- Review of the other top predictions, with subarachnoid hemorrhage and pulmonary hypertension the only ones with weak biological plausibility

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The compiled US regulatory records also show only cancelled licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "The compiled data list 14 US authorizations, all with cancelled status and no indication text" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cinvanti (aprepitant) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4c218d3a-a508-4abc-9ed8-a6e8e191d1b4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

