---
layout: default
title: Crizotinib
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 9
monitor_inn: "CRIZOTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
last_modified_at: 2026-11-24
description: "Crizotinib: predicted new indication fibromatosis, gingival (evidence level L5). In the US: 2 FDA applications (2 active)"
---

# Crizotinib
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

## Crizotinib: ALK/ROS1/MET tyrosine kinase inhibitor → fibromatosis, gingival
{: .text-alpha }

## One-Sentence Summary

Crizotinib is an oral kinase inhibitor that blocks ALK, ROS1 and MET. The TxGNN model predicts it may be relevant to **fibromatosis, gingival**, but this is a computational prediction only. The data compiled for this report contain **0 clinical trials** and **0 publications** for this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | fibromatosis, gingival |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for crizotinib: "Crizotinib is an inhibitor of receptor tyrosine kinases including ALK, Hepatocyte Growth Factor Receptor (HGFR, c-Met), ROS1 (c-ros), and Recepteur d'Origine Nantais (RON). Translocations can affect the ALK gene resulting in the expression of oncogenic fusion proteins." ([DailyMed: Xalkori (crizotinib) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2a51b0de-47d6-455e-a94c-d2c737b04ff7), label version 2026-10-29; accessed 2026-11-19.) From published descriptions, crizotinib inhibits the receptor tyrosine kinases ALK, ROS1 and MET.

The data show no plausible biological link between inhibition of these targets and gingival fibromatosis. Gingival fibromatosis is a fibrous overgrowth of the gums, and nothing compiled for this report connects it to ALK, ROS1 or MET signalling. The high score (0.9981) therefore reflects a computational pattern and is not backed by mechanistic or clinical data. The prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA202570 | XALKORI | PF PRISM CV | Capsule; oral | Valid |
| NDA217581 | XALKORI | PF PRISM CV | Capsule, pellets; oral | Valid |

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 recorded interactions. Examples with a **Major** severity level are:
  - clarithromycin
  - cisapride
  - dolasetron
  - eliglustat
  - granisetron

  Many others are rated Moderate, including famotidine, metformin, loperamide, bupropion, aprepitant, dexamethasone and budesonide.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications for gingival fibromatosis, and no mechanistic link to crizotinib's targets is evident. The evidence level is L5.

**To proceed, the following is needed:**
- A mechanistic hypothesis connecting ALK, ROS1 or MET signalling to gingival fibromatosis, supported by preclinical data
- Mechanism-of-action data for crizotinib in the compiled dataset
- Package insert warnings and contraindications, which are currently missing
- A review of the major drug interactions and the drug's overall safety profile against the likely benefit in this benign condition

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xalkori (crizotinib) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2a51b0de-47d6-455e-a94c-d2c737b04ff7) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

