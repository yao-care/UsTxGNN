---
layout: default
title: Aminocaproic Acid
parent: Model Prediction Only (L5)
nav_order: 327
evidence_level: L5
indication_count: 1
monitor_inn: "AMINOCAPROIC ACID"
predicted_indications: ["severe nonproliferative diabetic retinopathy"]
last_modified_at: 2026-11-12
description: "Aminocaproic Acid: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not stated in the compiled license data"
---

# Aminocaproic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Aminocaproic Acid: From Bleeding Control (Antifibrinolytic Therapy) to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Aminocaproic acid is an antifibrinolytic drug, used to control bleeding caused by excessive breakdown of blood clots. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled license data (the antifibrinolytic use is based on general knowledge of the drug class) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9927 |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Marketed (active FDA-approved applications: 20 of 31) |
| Number of FDA Applications | 31 (active: 20) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, aminocaproic acid is a lysine analog that inhibits plasminogen activation and plasmin activity, which reduces the breakdown of fibrin clots.

A possible link to diabetic retinopathy is that this action could limit bleeding from fragile new blood vessels in the retina. It might also influence fibrinolytic and extracellular-matrix remodeling pathways in the retina.

This link is hypothetical. It comes only from the high TxGNN score, with no supporting mechanistic or clinical data. There is also a safety concern: antifibrinolytic therapy carries a theoretical risk of thrombosis, and people with diabetes already have elevated vascular risk. Similarity to the original indication and route compatibility have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA070010 | AMINOCAPROIC ACID IN PLASTIC CONTAINER | HOSPIRA | Injectable; injection | Valid |
| ANDA071192 | AMINOCAPROIC ACID | LUITPOLD | Injectable; injection | Valid |
| ANDA209060 | AMINOCAPROIC ACID | SUNNY | Tablet; oral | Valid |
| ANDA212492 | AMINOCAPROIC ACID | AMNEAL | Tablet; oral | Valid |
| ANDA212494 | AMINOCAPROIC ACID | TP ANDA HOLDINGS | Solution; oral | Valid |

Showing 5 of 31 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

Available dosage forms were oral tablets, injectable solutions, and other solutions.

<!-- review:begin us-lic-20261106-aminocaproic_acid-1 -->

> **Review correction (2026-11-06)**: Originally stated: "13 valid licenses are on record for this drug in the US market, which is marketed. Available dosage forms were oral tablets, injectable solutions, and other solutions." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 31 FDA applications or NDC listings for this drug, 20 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-aminocaproic_acid-1 -->

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** The TxGNN knowledge graph links aminocaproic acid with contraindications in kidney disease, pyoureter, liver disease, gallbladder disease, disseminated intravascular coagulation, purpura fulminans (including acquired), and thrombotic disease. These come from model-derived data and should be verified against the official label.
- **Drug interactions:** The interaction query returned 75 entries. Most have an unknown severity level. The ones with a **moderate** level are:
  - Alteplase
  - Anistreplase

  This is expected, since thrombolytics and antifibrinolytics act in opposite directions. Other listed interacting drugs, with unknown severity, include morphine, omeprazole, lansoprazole, vancomycin, simvastatin, epinephrine, hydrocortisone, and acetylsalicylic acid.

Please refer to the package insert for warnings and contraindications from the label, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a high model score (L5). No trials or publications support it, the mechanistic link is hypothetical, and the thrombotic risk is a particular concern in diabetic patients. In addition, this drug is marketed in the US.

<!-- review:begin us-lic-20261106-aminocaproic_acid-2 -->

> **Review correction (2026-11-06)**: Originally stated: "In addition, this drug is marketed in the US with 13 valid licenses." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 31 FDA applications or NDC listings for this drug, 20 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-aminocaproic_acid-2 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search for antifibrinolytics in diabetic retinopathy or retinal and vitreous hemorrhage
- Preclinical evidence of benefit in retinal models
- Assessment of route compatibility (for example, whether a systemic or intravitreal route would be needed) and similarity to the original indication
- A thrombotic risk assessment for diabetic patients

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "13 valid licenses are on record for this drug in the US market, which is marketed" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 13 valid licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

