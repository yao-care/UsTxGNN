---
layout: default
title: Collagenase Clostridium Histolyticum
parent: Model Prediction Only (L5)
nav_order: 548
evidence_level: L5
indication_count: 9
monitor_inn: "COLLAGENASE CLOSTRIDIUM HISTOLYTICUM"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "Ledderhose disease", "infantile digital fibromatosis", "hemorrhagic disorder due to a constitutional thrombocytopenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "posterior leukoencephalopathy syndrome"]
last_modified_at: 2026-11-12
description: "Collagenase Clostridium Histolyticum: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Not recorded in the local data"
---

# Collagenase Clostridium Histolyticum
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

## Collagenase Clostridium Histolyticum: Primary release disorder of platelets
{: .text-alpha }

## One-Sentence Summary

Collagenase Clostridium histolyticum is a collagen-degrading enzyme product that is marketed in the United States. The TxGNN model predicts it may be relevant to **primary release disorder of platelets**, but **no clinical trials and no publications** were found for this disease. The prediction rests on model output alone, and the mechanistic review found no plausible therapeutic rationale.

<!-- review:begin us-lic-20261106-collagenase_clostridium_histolyticum-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Collagenase Clostridium histolyticum is a collagen-degrading enzyme product that is marketed in the United States as a topical ointment." Removed: its description of the US products did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 2 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-collagenase_clostridium_histolyticum-2 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2; OTC monograph / unapproved listings: 1) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Collagenase Clostridium histolyticum is a bacterial enzyme preparation that breaks down collagen. Its use is built on that collagen-lysing action.

Primary release disorder of platelets is a platelet function defect. Platelets fail to release their granule contents properly, so they do not aggregate normally. It is not a disorder of collagen accumulation, so a collagen-degrading enzyme has no obvious target.

The high score most likely reflects the model's association between collagen and platelet biology (platelets are activated by contact with collagen). It does not reflect a therapeutic rationale. Collagen degradation could plausibly worsen bleeding in a patient who already has impaired hemostasis. This prediction should be treated as a model artifact unless direct evidence emerges.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA125338 | XIAFLEX | AUXILIUM PHARMS | Solution; injection | Valid |
| BLA761146 | QWO | ENDO GLOBAL AESTHETICS LTD | Solution; subcutaneous | Valid |
| NDC 85212-0011 | NOAVIA Retinol Moisturizer | Beijing JUNGE Technology Co., Ltd. | Cream | NDC listing, no FDA application (OTC monograph drug) |

<!-- licenses:end -->

At least one valid licence exists, so the drug is currently marketed in the United States.

<!-- review:begin us-lic-20261106-collagenase_clostridium_histolyticum-3 -->

> **Review correction (2026-11-06)**: Originally stated: "At least one valid licence exists, so the drug is currently marketed in the United States. The manufacturer is Smith & Nephew, Inc." Removed: it conflicted with the FDA application data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 2 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-collagenase_clostridium_histolyticum-3 -->

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 49 interacting drugs. The 20 shown in the data compiled for this report are all rated Moderate. The main groups are:
  - **Tetracycline antibiotics**: doxycycline, minocycline, tetracycline
  - **Antiplatelet agents**: acetylsalicylic acid, abciximab, cangrelor, cilostazol, clopidogrel
  - **Anticoagulants and thrombolytics**: fondaparinux, alteplase, anistreplase, antithrombin III human, apixaban, betrixaban, bivalirudin, argatroban, dalteparin, danaparoid, defibrotide, caplacizumab
- **Bleeding concern**: The condition involves impaired platelet function. Combining a collagen-degrading enzyme with the many antithrombotic interaction partners above is a theoretical bleeding risk in this population.

Label warnings and contraindications were not available in the compiled data. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it (evidence level L5), with no trials or publications for this disease. The mechanistic review found no plausible benefit and a possible bleeding risk, so there is no basis to advance it.

**To proceed, the following is needed:**
- Any direct preclinical or clinical evidence linking collagenase to platelet release disorders
- A mechanism of action dataset for the drug
- Label warnings and contraindications from the package insert
- A bleeding-risk assessment in patients with platelet function defects

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "Verification of the regulatory and supply status of the injectable product in the US, since the only record listed is a cancelled ointment" | No longer present after the report was regenerated (2026-11-12: the report was regenerated in 2026-11 and no longer contains this statement; was: Corrected) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "as a topical ointment" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "The manufacturer is Smith & Nephew, Inc" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

