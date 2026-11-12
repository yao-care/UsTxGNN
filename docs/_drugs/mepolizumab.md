---
layout: default
title: Mepolizumab
parent: Model Prediction Only (L5)
nav_order: 900
evidence_level: L5
indication_count: 5
monitor_inn: "MEPOLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
last_modified_at: 2026-11-12
description: "Mepolizumab: predicted new indication Thrombocytopenia due to immune destruction (evidence level L5). Approved use: Eosinophilic pneumonia"
---

# Mepolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Mepolizumab: From Eosinophilic Pneumonia to Thrombocytopenia Due to Immune Destruction
{: .text-alpha }

## One-Sentence Summary

Mepolizumab is an anti-IL-5 monoclonal antibody, originally used for eosinophilic pneumonia and pulmonary eosinophilia.
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**,
but currently only **1 case report** supports this direction, with **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Eosinophilic pneumonia; pulmonary eosinophilia |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mepolizumab is an anti-IL-5 monoclonal antibody that depletes eosinophils. Its use in eosinophil-driven conditions such as eosinophilic pneumonia and pulmonary eosinophilia is the basis of its original indications.

A plausible link to immune-mediated thrombocytopenia exists only in a narrow context: hypereosinophilic syndrome accompanied by an immune-mediated cytopenia, where eosinophil-driven immune dysregulation may contribute to platelet destruction. There is no established role for IL-5 blockade in primary immune thrombocytopenia, which is driven mainly by anti-platelet autoantibodies and T-cell dysregulation.

The high TxGNN score (0.9966) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It does not substitute for clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case report | Blood Cells Mol Dis | A steroid-resistant hypereosinophilic immune condition resolved with mepolizumab, with improvement of a mixed thrombotic microangiopathy. Concomitant treatment means the response cannot be attributed to mepolizumab alone. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125526 | Nucala (GlaxoSmithKline LLC) | Injection, powder, for solution | Not available (status: valid) |
| BLA761122 | Nucala (GlaxoSmithKline LLC) | Injection, solution | Not available (status: valid) |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single case report confounded by concomitant therapy, with no clinical trials and no established mechanistic link between IL-5 blockade and immune platelet destruction. The high TxGNN score alone does not justify advancing. In addition, safety label data are missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently blocking safety screening)
- Detailed mechanism of action data
- Clarification of current US market status
- Further clinical evidence, such as case series or prospective studies in hypereosinophilia-associated immune thrombocytopenia
- Assessment of whether the other predicted indications (primary release disorder of platelets, pseudo-von Willebrand disease, autoimmune thrombocytopenic, Glanzmann thrombasthenia) have any plausible rationale; at present they are supported only by model scores, and no mechanistic link is evident

<!-- review:begin us-lic-20261106-mepolizumab-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of current US market status, as both listed BLAs are cancelled" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 2 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-mepolizumab-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "as both listed BLAs are cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

