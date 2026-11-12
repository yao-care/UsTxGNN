---
layout: default
title: Fedratinib
parent: Model Prediction Only (L5)
nav_order: 694
evidence_level: L5
indication_count: 10
monitor_inn: "FEDRATINIB"
predicted_indications: ["benign PEComa", "lymphangiomyoma", "uterine corpus perivascular epithelioid cell tumor", "dermatofibrosarcoma protuberans", "rhabdoid tumor", "familial rhabdoid tumor", "autosomal recessive familial Mediterranean fever", "hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "lymphangioleiomyomatosis"]
last_modified_at: 2026-11-12
description: "Fedratinib: predicted new indication Benign PEComa (evidence level L5). Approved use: Not recorded in the local data"
---

# Fedratinib
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

## Fedratinib: Benign PEComa
{: .text-alpha }

## One-Sentence Summary

Fedratinib is an oral kinase inhibitor originally used to treat primary myelofibrosis and myelofibrosis.
The TxGNN model predicts it may be effective for **benign PEComa**,
but **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Benign PEComa |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, fedratinib is a JAK2 inhibitor (with additional FLT3 and BRD4 activity). Its efficacy in myelofibrosis, a disease driven by dysregulated JAK/STAT signaling, is the basis of its original use.

PEComas are typically driven by mTOR pathway activation through TSC1/TSC2 loss. No direct link between JAK2 inhibition and mTOR-driven biology is established in the data compiled for this report, so the mechanistic connection is weak and speculative. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top predictions share this limitation. Several are mTOR-related (lymphangiomyoma, uterine PEComa, lymphangioleiomyomatosis), where sirolimus is the established therapy. Two others are rhabdoid tumor entities, where a BRD4/epigenetic rationale is conceivable but untested. The two hemophagocytic lymphohistiocytosis (HLH) predictions have the most plausible class rationale (JAK/STAT cytokine signaling, with ruxolitinib as precedent), but no fedratinib-specific data exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA212327 | INREBIC | BRISTOL-MYERS | Capsule; oral | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically CBC, liver function, and renal function for kinase inhibitors) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database; the first 20 reviewed are mostly Moderate. The **Major** interactions among them are:
  - Dexamethasone
  - Clarithromycin
  - Eliglustat
  - Naloxegol
  
  Moderate interactions include proton pump inhibitors (omeprazole, rabeprazole, lansoprazole), cimetidine, aprepitant, naltrexone, saxagliptin, and several corticosteroids (hydrocortisone, triamcinolone, betamethasone, budesonide).

- **Boxed warning (from general knowledge, not the compiled data)**: Fedratinib is known to carry a boxed warning for encephalopathy, including Wernicke's. This is a particular concern for the critically ill patients seen in HLH. It should be verified against the current package insert.

The package insert warnings and contraindications were not available and must be obtained before any safety screening.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (evidence level L5), with no clinical trials or publications, a weak mechanistic link to mTOR-driven PEComa biology.

<!-- review:begin us-lic-20261106-fedratinib-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The prediction is supported only by the TxGNN model score (evidence level L5), with no clinical trials or publications, a weak mechanistic link to mTOR-driven PEComa biology, and a cancelled US NDA." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-fedratinib-2 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence of fedratinib activity in PEComa or TSC/mTOR-driven models
- A literature and trial search, and a comparison against established therapies (e.g., sirolimus for mTOR-driven diseases)
- Consideration of the HLH predictions as a more mechanistically plausible alternative, after assessing the safety profile in that setting

<!-- review:begin us-lic-20261031-fedratinib-1 -->

> **Review correction (2026-10-31)**: Originally stated: "Consideration of the HLH predictions as a more mechanistically plausible alternative, after assessing the safety profile in that setting / Clarification of the current US regulatory status of fedratinib, since the compiled record shows only a cancelled NDA" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-fedratinib-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "Clarification of the current US regulatory status of fedratinib, since the compiled record shows only a cancelled NDA" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "and a cancelled US NDA" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

