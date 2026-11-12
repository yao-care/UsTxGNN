---
layout: default
title: Demeclocycline
parent: Model Prediction Only (L5)
nav_order: 580
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
monitor_inn: "DEMECLOCYCLINE"
predicted_indications: ["chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
description: "Demeclocycline: predicted new indication Chronic ethmoidal sinusitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Demeclocycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Demeclocycline: Chronic ethmoidal sinusitis
{: .text-alpha }

## One-Sentence Summary

Demeclocycline is a tetracycline-class antibiotic, originally used to treat a range of bacterial infections such as urinary tract infection, bronchitis, gonorrhea and anthrax.
The TxGNN model predicts it may be effective for **chronic ethmoidal sinusitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Chronic ethmoidal sinusitis |
| TxGNN Prediction Score | 0.9914 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 3 of 8) |
| Number of FDA Applications | 8 (active: 3) |
| Recommended Decision | Hold |

Two other predictions were also generated, both with L5 evidence and a Hold recommendation:
- Chronic rhinosinusitis (score 0.9909)
- Paranasal sinus neoplasm (score 0.9905)

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, demeclocycline is a tetracycline antibiotic whose efficacy in bacterial infections of the respiratory tract and other sites is established. Mechanistically, it may be applicable to chronic sinusitis, where bacterial involvement is possible.

Tetracyclines have also been reported to have anti-inflammatory and matrix metalloproteinase-inhibiting effects, which could be relevant to chronic sinus inflammation. These are hypotheses and are not supported by data compiled for this report.

The other two predictions are weaker. Chronic rhinosinusitis shares the same rationale as ethmoidal sinusitis. The paranasal sinus neoplasm prediction is very different from the drug's anti-infective uses and likely reflects network proximity to sinus-related terms rather than a true therapeutic effect. It should not be advanced without supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261106-demeclocycline-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Both authorizations are cancelled, which limits practical feasibility for any repurposing effort." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 8 FDA applications or NDC listings for this drug, 3 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-demeclocycline-1 -->

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA065389 | DEMECLOCYCLINE HYDROCHLORIDE | EPIC PHARMA LLC | Tablet; oral | Valid |
| ANDA065425 | DEMECLOCYCLINE HYDROCHLORIDE | AMNEAL PHARM | Tablet; oral | Valid |
| ANDA065447 | DEMECLOCYCLINE HYDROCHLORIDE | EPIC PHARMA LLC | Tablet; oral | Valid |
| ANDA065094 | DEMECLOCYCLINE HYDROCHLORIDE | IMPAX LABS | Tablet; oral | Discontinued in Drugs@FDA |
| ANDA065171 | DEMECLOCYCLINE HYDROCHLORIDE | BARR | Tablet; oral | Discontinued in Drugs@FDA |

Showing 5 of 8 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and diabetes insipidus (including neurohypophyseal and central forms).
- **Drug Interactions**: 100 interactions were identified; the first 20 are listed in the data compiled for this report.
  - **Major**: Vitamin A.
  - **Moderate**: Amoxicillin, balsalazide, and polyvalent cation products (calcium phosphate, calcium acetate, magnesium oxide, magnesium sulfate, magnesium chloride, zinc sulfate, zinc acetate, potassium citrate). Several insulin products (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, and inhaled rapid-acting) are also Moderate.
  - **Minor**: Mannitol.

Please refer to the package insert for full warnings and precautions, as label text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9914), but there are no clinical trials or publications, so evidence is L5 (model prediction only).

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- A literature and trial search for tetracycline-class drugs in chronic sinusitis
- Assessment of route compatibility and whether a marketed product is available
- Clarification of why the predicted indication sits far from the original anti-infective profile, particularly for the paranasal sinus neoplasm prediction

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Both authorizations are cancelled, which limits practical feasibility for any repurposing effort" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

