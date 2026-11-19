---
layout: default
title: Ruxolitinib
parent: Model Prediction Only (L5)
nav_order: 1140
evidence_level: L5
indication_count: 10
monitor_inn: "RUXOLITINIB"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection"]
last_modified_at: 2026-11-20
description: "Ruxolitinib: predicted new indication Uterine corpus perivascular epithelioid cell tumor (evidence level L5). In the US: 3 FDA applications (3 active)"
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
| US Market Status | Marketed (active FDA-approved applications: 3 of 3) |
| Number of FDA Applications | 3 (active: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for ruxolitinib: "Ruxolitinib, a kinase inhibitor, inhibits Janus Associated Kinases (JAKs), JAK1 and JAK2, which mediate the signaling of a number of cytokines and growth factors that are important for hematopoiesis and immune function. JAK signaling involves recruitment of STATs (signal transducers and activators of transcription) to cytokine receptors, activation, and subsequent localization of STATs to the nucleus leading to modulation of gene expression." ([DailyMed: Jakafi (ruxolitinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1c82580-87ae-11e0-bc84-0002a5d5c51b), label version 2026-07-20; accessed 2026-11-19.) Ruxolitinib is a Janus kinase (JAK) inhibitor. Its efficacy in myeloproliferative neoplasms is established, and mechanistically it may be applicable to diseases driven by JAK/STAT signaling.

For this specific prediction, the supporting rationale is weak. JAK/STAT signaling is a plausible link, but nothing in the compiled data supports it for this tumor. PEComa biology is mainly driven by dysregulation of the mTOR pathway (TSC1/TSC2), which differs from the JAK/STAT axis targeted by ruxolitinib. The high TxGNN score therefore reflects a network-level association rather than a demonstrated biological or clinical link.

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
| NDA202192 | JAKAFI | INCYTE CORP | Tablet; oral | Valid |
| NDA215309 | OPZELURA | INCYTE CORP | Cream; topical | Valid |
| NDA217180 | JAKAFI XR | INCYTE CORP | Tablet, extended release; oral | Valid |

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Jakafi (ruxolitinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1c82580-87ae-11e0-bc84-0002a5d5c51b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

