---
layout: default
title: Ruxolitinib
parent: Model Prediction Only (L5)
nav_order: 1140
evidence_level: L5
indication_count: 10
monitor_inn: "RUXOLITINIB"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection"]
last_modified_at: 2026-10-28
description: "Ruxolitinib: predicted new indication Uterine corpus perivascular epithelioid cell tumor (evidence level L5). Approved use: Not recorded in the local data"
---

# Ruxolitinib
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

## Ruxolitinib: Uterine corpus perivascular epithelioid cell tumor
{: .text-alpha }

## One-Sentence Summary

Ruxolitinib is a JAK inhibitor originally used for myeloproliferative neoplasms such as myelofibrosis and polycythemia vera.
The TxGNN model predicts it may be effective for **uterine corpus perivascular epithelioid cell tumor (PEComa)**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Uterine corpus perivascular epithelioid cell tumor |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of NDAs | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Ruxolitinib is a Janus kinase (JAK) inhibitor. Its efficacy in myeloproliferative neoplasms is established, and mechanistically it may be applicable to diseases driven by JAK/STAT signaling.

For this specific prediction, the supporting rationale is weak. JAK/STAT signaling is a plausible link, but nothing in the compiled data supports it for this tumor. PEComa biology is mainly driven by dysregulation of the mTOR pathway (TSC1/TSC2), which differs from the JAK/STAT axis targeted by ruxolitinib. The high TxGNN score therefore reflects a network-level association rather than a demonstrated biological or clinical link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| NDA215309 | OPZELURA | Cream | Incyte Corporation | Valid |
| NDA202192 | JAKAFI | Tablet | Incyte Corporation | Valid |
| NDA217900 | LEQSELVI | Tablet, film coated | Sun Pharmaceutical Industries, Inc. | Valid |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (JAK inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

No warning or contraindication data (label-based or knowledge-graph-based) were available for this report. Please refer to the package insert for these.

- **Drug Interactions**: The interaction query returned 100 interactions in total, and 20 were available for review. Among those 20:
  - **Major**: clarithromycin, cobicistat, deferasirox, deferiprone, ibritumomab tiuxetan, tositumomab (including I-131), samarium (153Sm) lexidronam
  - **Moderate**: dexamethasone, rosuvastatin, dexfenfluramine, fenfluramine, sibutramine, troglitazone, palifermin, strontium chloride Sr-89
  - **Minor**: aprepitant, cimetidine, miconazole, clotrimazole

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for uterine corpus PEComa rests on the model score alone (L5). There are no trials or publications, and the known biology of this tumor points to mTOR rather than JAK/STAT signaling. All three US licenses are also valid.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking JAK/STAT signaling to PEComa
- Detailed mechanism of action data
- The package insert warnings and contraindications, which were not available
- A review of the full interaction list (only 20 of 100 interactions were available)
- Confirmation of route and formulation compatibility with the target disease

**Note on other predictions:** Among the other predicted indications, hemophagocytic syndrome associated with an infection has far more support. It is graded L3 and has about 20 publications, including a pediatric stratified-treatment study, case series, and murine mechanism work. No registered trials were provided, and study designs were inferred from titles only, so they need verification. If the goal is to prioritize repurposing candidates, that indication is a better starting point than this one.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

