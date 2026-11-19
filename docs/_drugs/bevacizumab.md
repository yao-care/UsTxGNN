---
layout: default
title: Bevacizumab
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
monitor_inn: "BEVACIZUMAB"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
last_modified_at: 2026-11-06
description: "Bevacizumab: predicted new indication epiglottis neoplasm (evidence level L5). In the US: 8 FDA applications (8 active)"
---

# Bevacizumab
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

## Bevacizumab: Anti-VEGF-A monoclonal antibody → epiglottis neoplasm
{: .text-alpha }

## One-Sentence Summary

Bevacizumab is a monoclonal antibody that blocks VEGF-A to inhibit tumour angiogenesis.
The TxGNN model predicts it may be relevant to **epiglottis neoplasm**, with a score of 0.9990.
However, **no clinical trials and no publications** directly support this prediction in the data compiled for this report, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | epiglottis neoplasm |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 8 of 8) |
| Number of FDA Applications | 8 (active: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for bevacizumab: "Bevacizumab products bind VEGF and prevent the interaction of VEGF to its receptors (Flt-1 and KDR) on the surface of endothelial cells. The interaction of VEGF with its receptors leads to endothelial cell proliferation and new blood vessel formation in in vitro models of angiogenesis." ([DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe), label version 2026-08-21; accessed 2026-11-19.) Based on general knowledge, bevacizumab binds VEGF-A and limits the formation of new tumour blood vessels, a process that many solid tumours depend on.

Epiglottis neoplasm is a head and neck tumour site. Anti-angiogenic therapy is plausibly relevant to head and neck tumours, but this is a site-level inference only. No study in the compiled data enrolled patients with epiglottis neoplasm, so the link remains a model-based hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered for this prediction.

## Literature Evidence

Currently no related literature available for this prediction.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761175 | JOBEVNE | Injection | Not recorded |
| BLA125085 | Avastin | Injection, solution | Not recorded |
| BLA761268 | Vegzelma | Injection, solution | Not recorded |
| BLA761198 | Avzivi | Injection, solution | Not recorded |
| BLA761231 | ALYMSYS | Injection, solution | Not recorded |

## Safety Considerations

- **Drug Interactions**: 22 interactions were recorded in total, and the list shown contains 20. Major-level interactions include deferiprone, samarium (153Sm) lexidronam, panitumumab, sunitinib and thalidomide. Moderate-level interactions include bisphosphonates (alendronic, risedronic, etidronic, pamidronic, tiludronic acid and ibandronate), colony-stimulating factors (filgrastim, pegfilgrastim, sargramostim), palifermin, strontium chloride Sr-89, idelalisib, radium Ra 223 dichloride, romosozumab and sodium phosphate P-32.

Please refer to the package insert for warnings and contraindications, as they are not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9990), but no trial or publication studies epiglottis neoplasm directly, so the evidence level is L5. Anti-angiogenic rationale alone is not enough to support further investment.

**To proceed, the following is needed:**
- Clinical or preclinical studies in laryngeal or epiglottic tumours specifically
- Mechanism-of-action data and package insert warnings and contraindications
- A review of head and neck experience with bevacizumab, including bleeding and wound-healing risks
- Assessment of the interaction profile in likely combination regimens

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

