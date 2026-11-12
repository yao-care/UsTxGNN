---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 762
evidence_level: L5
indication_count: 5
monitor_inn: "GRISEOFULVIN"
predicted_indications: ["myiasis", "wound myiasis", "creeping myiasis", "furuncular myiasis", "echinococcus granulosus infectious disease"]
last_modified_at: 2026-11-12
description: "Griseofulvin: predicted new indication Myiasis (evidence level L5). Approved use: Not recorded in the local data"
---

# Griseofulvin
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

## Griseofulvin: Myiasis
{: .text-alpha }

## One-Sentence Summary

Griseofulvin is an oral antifungal originally used to treat dermatophyte (tinea) infections of the skin, scalp, nails and groin.
The TxGNN model predicts it may be effective for **myiasis**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction is model-only and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 12 of 22) |
| Number of FDA Applications | 22 (active: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, griseofulvin is a fungistatic agent that is understood to disrupt microtubule function and mitosis in fungal cells. Its efficacy in dermatophyte infections is established.

The link to myiasis is weak. Myiasis is an infestation of tissue by fly (Diptera) larvae, which is a parasitic rather than fungal condition. No established mechanism connects griseofulvin to larvicidal activity. Standard care is already in place: larval removal, and ivermectin in selected cases.

The nearly identical scores across the myiasis subtypes (wound, creeping and furuncular myiasis all score 0.9934) suggest the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The high score should therefore be read as a model-level association, not proof of plausibility.

**Other predictions in the list:**

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Wound myiasis | 0.9934 | Likely inherited from the parent term "myiasis"; no evidence |
| 3 | Creeping myiasis | 0.9934 | Treated with ivermectin or albendazole; no antiparasitic mechanism for griseofulvin |
| 4 | Furuncular myiasis | 0.9934 | Managed by larval extraction or occlusion; no larvicidal mechanism |
| 5 | Echinococcus granulosus infection | 0.9932 | The most conceivable mechanistically (tubulin targeting, as with benzimidazoles), but no demonstrated anthelmintic activity |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Griseofulvin is marketed in the US, and no approved-indication text was recorded. The first five are listed below.

<!-- review:begin us-lic-20261106-griseofulvin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Griseofulvin is marketed in the US, with 10 valid licenses, and no approved-indication text was recorded for them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 22 FDA applications or NDC listings for this drug, 12 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-griseofulvin-2 -->

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA091592 | Griseofulvin (Sandoz Inc) | Tablet | Not recorded |
| ANDA061996 | Ultramicrosize Griseofulvin (Chartwell RX) | Tablet | Not recorded |
| ANDA204371 | Ultramicrosize Griseofulvin (Amneal) | Tablet, coated | Not recorded |
| ANDA065354 | Griseofulvin (Cipla USA) | Suspension | Not recorded |
| ANDA065200 | Griseofulvin (Chartwell RX) | Suspension | Not recorded |

The remaining five licences are also cancelled. Available dosage forms were oral tablets (including coated tablets) and suspensions.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): liver failure; porphyria (including inherited porphyria and porphyrin metabolism disease); systemic lupus erythematosus (including the paediatric form); substance abuse/dependence; and agranulocytosis and neutropenia (including cyclic hematopoiesis and congenital neutropenia syndromes).
- **Drug interactions:** The interaction screening returned 100 records. Most of those listed are of Moderate severity, with a few Minor. Notable moderate interactions include:
  - Anticoagulants and antiplatelets: warfarin, dicoumarol, apixaban, rivaroxaban, ticagrelor
  - Antidiabetic agents: saxagliptin, linagliptin, repaglinide
  - Antimalarials and antiparasitics: artemether, mefloquine, praziquantel
  - Others: aprepitant, rolapitant, eliglustat, naloxegol, nitisinone, fostamatinib, macimorelin
  - Minor: acetylsalicylic acid, liraglutide

Please refer to the package insert for label warnings and contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no trials or publications and no plausible mechanism for activity against fly larvae. Established treatments already exist. The drug is marketed in the US, and label safety data are missing.

<!-- review:begin us-lic-20261106-griseofulvin-3 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US with 10 valid licenses, and label safety data are missing." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 22 FDA applications or NDC listings for this drug, 12 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-griseofulvin-3 -->

**To proceed, the following is needed:**
- Mechanism of action data for griseofulvin and a documented mechanistic rationale for myiasis
- FDA package insert warnings and contraindications, needed for safety screening
- In vitro or animal data showing larvicidal activity (for myiasis), or protoscolicidal or cyst-model data (for echinococcosis, the most conceivable alternative)
- A review of whether the identical subtype scores reflect an ontology artefact
- Assessment of the formulation and route needed for any new indication

<!-- review:begin us-lic-20261106-griseofulvin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Assessment of the formulation and route needed for any new indication, including the implications of the cancelled US marketing status" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 22 FDA applications or NDC listings for this drug, 12 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-griseofulvin-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "including the implications of the cancelled US marketing status" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 10 valid licenses for them" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 10 valid licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

