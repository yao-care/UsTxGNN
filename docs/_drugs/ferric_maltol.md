---
layout: default
title: Ferric Maltol
parent: Model Prediction Only (L5)
nav_order: 702
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "FERRIC MALTOL"
predicted_indications: ["vitamin B12- and folate-independent constitutional megaloblastic anemia", "IRIDA syndrome"]
description: "Ferric Maltol: predicted new indication Vitamin B12- and folate-independent constitutional megaloblastic anemia (evidence level L5). In the US: 1 FDA application (1 active)"
---

# Ferric Maltol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Ferric Maltol: Vitamin B12- and folate-independent constitutional megaloblastic anemia
{: .text-alpha }

## One-Sentence Summary

Ferric maltol is an oral iron preparation used to replace iron in iron-deficiency states. The TxGNN model predicts it may be effective for **vitamin B12- and folate-independent constitutional megaloblastic anemia**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vitamin B12- and folate-independent constitutional megaloblastic anemia |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the FDA-approved prescribing information for ferric maltol: "ACCRUFER delivers iron for uptake across the intestinal wall and transfer to transferrin and ferritin." ([DailyMed: Accrufer (ferric maltol) prescribing information, Shield TX (UK) Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=367ac157-2d25-4f34-99ce-b126e0f03851), label version 2026-01-02; accessed 2026-11-19.) Based on what is known, ferric maltol is an oral, lipophilic iron complex designed to deliver iron for absorption in the gut.

The mechanistic link to the predicted condition is weak. Megaloblastic anemia is typically driven by impaired DNA synthesis, through B12 or folate pathways or through inherited defects in nucleotide metabolism. It is not driven by iron deficiency. Iron replacement would not be expected to correct a megaloblastic defect that is independent of B12 and folate, unless iron deficiency is also present. The very high score of 0.9998 most likely reflects closeness to other anemia-related conditions in the model's network rather than a true therapeutic mechanism. The score is a model output only and does not show that the drug works for this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA212320 | ACCRUFER | SHIELD TX | Capsule; oral | Valid |

<!-- licenses:end -->

The data list one valid licence, a single-ingredient product taken by mouth (capsule). The manufacturer is Shield TX (UK) Ltd.

## Safety Considerations

- **Conditions where use may be problematic (recorded as drug–disease contraindication relations, not taken from label text):** hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease. These are consistent with the general caution against giving iron to people with iron overload.
- **Drug Interactions:** No interaction records were found in the data compiled for this report.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or publications, and the biology argues against it: this form of megaloblastic anemia is independent of B12, folate and iron status. Evidence is at level L5 (model prediction only).

**To proceed, the following is needed:**
- Any clinical or mechanistic study that directly addresses this form of megaloblastic anemia and iron therapy
- Mechanism-of-action data for ferric maltol
- Package insert warnings and contraindications, to complete the safety review
- Evidence that patients with this condition also have iron deficiency that would justify iron replacement

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for ferric maltol are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Accrufer (ferric maltol) prescribing information, Shield TX (UK) Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=367ac157-2d25-4f34-99ce-b126e0f03851) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

