---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 422
evidence_level: L5
indication_count: 5
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-24
description: "Atenolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension and myocardial infarction"
---

# Atenolol
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

## Atenolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Atenolol is a beta-1 selective blocker, originally used for hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** currently address this disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and myocardial infarction (relations recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 15 of 42) |
| Number of FDA Applications | 42 (active: 15) |
| Number of approvals | At least 8 (1 NDA and 7 ANDAs; the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the FDA-approved prescribing information for atenolol: "TENORMIN is a beta 1 -selective (cardioselective) beta-adrenergic receptor blocking agent without membrane stabilizing or intrinsic sympathomimetic (partial agonist) activities. This preferential effect is not absolute, however, and at higher doses, TENORMIN inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature." ([DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a), label version 2025-09-18; accessed 2026-11-19.) Based on known pharmacology, atenolol is a beta-1 selective blocker that lowers blood pressure and reduces renin release. Hypertension is recorded as an original use in the knowledge graph, and that is a plausible link to hypertensive kidney damage.

The high score (0.9985) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Malignant hypertension is usually managed with intravenous agents in an acute setting, and oral beta-blockers are not the standard first-line approach. No supporting study was supplied, so the prediction should be treated as a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- review:begin us-lic-20261124b-atenolol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Eight single-ingredient oral tablet authorizations are listed in total, and the list may be partial." Removed: the number or type of FDA applications stated here did not match the FDA data (Drugs@FDA and the NDC Directory). The current figures are shown in the Quick Overview and in the program-generated table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261124b-atenolol-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA072304 | ATENOLOL | AIPING PHARM INC | Tablet; oral | Valid |
| ANDA073026 | ATENOLOL | PHARMOBEDIENT | Tablet; oral | Valid |
| ANDA073457 | ATENOLOL | MYLAN | Tablet; oral | Valid |
| ANDA074056 | ATENOLOL | TEVA | Tablet; oral | Valid |
| ANDA076900 | ATENOLOL | ZYDUS PHARMS USA | Tablet; oral | Valid |

Showing 5 of 42 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Contraindication relations in the knowledge graph (not label text):** asthma, atrioventricular block, diabetes mellitus (types 1 and 2, diabetic ketoacidosis), Raynaud disease, anaphylaxis, liver failure, pancreatitis, systemic lupus erythematosus, psoriasis, gout, anuria, anxiety and related disorders, and several electrolyte or mineral disorders (potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease).
- **Drug interactions:** 100 interactions were found. Moderate-level examples include epinephrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, acetohexamide, atropine, betamethasone, budesonide, and several calcium salts. Minor-level examples include acetylsalicylic acid, aluminum hydroxide, and attapulgite.

Please also refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no trials or publications on malignant hypertensive renal disease, and clinical practice for this condition favors intravenous agents. The evidence level is L5.

**To proceed, the following is needed:**
- Studies that directly address atenolol in malignant hypertensive renal disease
- Package insert warnings and contraindications
- Mechanism of action data
- Comparison with the current standard of care for malignant hypertension

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a) |
| 2026-11-24 | Removed: "Eight single-ingredient oral tablet authorizations are listed in total, and the list may be partial." | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

