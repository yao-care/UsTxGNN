---
layout: default
title: Anakinra
parent: Model Prediction Only (L5)
nav_order: 337
evidence_level: L5
indication_count: 9
monitor_inn: "ANAKINRA"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "aggressive systemic mastocytosis", "hepatic veno-occlusive disease", "peliosis hepatis", "oligoarticular juvenile idiopathic arthritis without anti-nuclear antibodies", "oligoarticular juvenile idiopathic arthritis with anti-nuclear antibodies", "pyogenic autoinflammatory syndrome", "unclassified autoinflammatory syndrome"]
last_modified_at: 2026-11-20
description: "Anakinra: predicted new indication extracutaneous mastocytoma (evidence level L5). In the US: 1 FDA application (1 active)"
---

# Anakinra
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

## Anakinra: IL-1 receptor antagonist → extracutaneous mastocytoma
{: .text-alpha }

## One-Sentence Summary

Anakinra is an interleukin-1 (IL-1) receptor antagonist marketed in the United States as an injectable solution.
The TxGNN model predicts it may be relevant for **extracutaneous mastocytoma**,
but **no clinical trials and no publications** were found for this specific disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | extracutaneous mastocytoma |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for anakinra: "KINERET blocks the biologic activity of IL-1 alpha and beta by competitively inhibiting IL-1 binding to the interleukin-1 type I receptor (IL-1RI), which is expressed in a wide variety of tissues and organs. IL-1 production is induced in response to inflammatory stimuli and mediates various physiologic responses including inflammatory and immunological responses." ([DailyMed: Kineret (anakinra) prescribing information, Swedish Orphan Biovitrum AB (publ)](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d9d74915-6606-4570-9c52-c4001d3177de), label version 2026-04-03; accessed 2026-11-19.) Based on general knowledge, anakinra blocks signaling of the cytokine IL-1 by occupying its receptor. IL-1 signaling is theoretically involved in mast cell-driven inflammation, which is the only conceptual bridge to this prediction.

However, the data compiled for this report show no direct link between anakinra and extracutaneous mastocytoma. No trials or publications address this disease, so the prediction should be treated as a hypothesis from the model rather than an evidence-backed direction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103950 | Kineret | Injection, solution | Not recorded in the local data |

The status should be verified against current FDA listings.

<!-- review:begin us-lic-20261106-anakinra-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The available record lists one authorization, and it is marked as cancelled in the licence details, while the overall market status is reported as marketed. The status should be verified against current FDA listings." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-anakinra-1 -->

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 entries; the first 20 are summarized here.
  - **Major**: deferiprone.
  - **Moderate**: corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone, prednisolone, prednisone, triamcinolone), simvastatin, apixaban, rivaroxaban, dicoumarol, and radiopharmaceutical antibody agents (ibritumomab tiuxetan, tositumomab, iobenguane I-131).
  - **Minor**: zinc salts (acetate, gluconate, sulfate).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no trials or publications for extracutaneous mastocytoma, and no plausible direct mechanistic link is shown in the available data. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Preclinical or mechanistic studies showing IL-1 involvement in extracutaneous mastocytoma
- Published case reports or registered trials of IL-1 blockade in mast cell neoplasms
- Mechanism of action data and package insert safety information (warnings and contraindications)
- Clarification of the current licence status of Kineret

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The available record lists one authorization, and it is marked as cancelled in the licence details, while the overall market status is repor" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Kineret (anakinra) prescribing information, Swedish Orphan Biovitrum AB (publ)](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d9d74915-6606-4570-9c52-c4001d3177de) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

