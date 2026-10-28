---
layout: default
title: Diethyltoluamide
parent: Model Prediction Only (L5)
nav_order: 605
evidence_level: L5
indication_count: 8
monitor_inn: "DIETHYLTOLUAMIDE"
predicted_indications: ["insomnia (disease)", "attention deficit hyperactivity disorder, inattentive type", "specific developmental disorder", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "heparin cofactor 2 deficiency", "migraine disorder", "attention deficit-hyperactivity disorder"]
last_modified_at: 2026-10-28
description: "Diethyltoluamide: predicted new indication Insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Diethyltoluamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Diethyltoluamide: Insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Diethyltoluamide (DEET) is widely known as an insect repellent, and its only U.S. record in the data compiled for this report is a cancelled liquid product with no approved indication text.
The TxGNN model predicts it may be effective for **insomnia** (score 0.9967), but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction with no supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. DEET is known as an insect repellent that acts on insect olfactory receptors, and it has been reported to inhibit acetylcholinesterase in insects. No documented link connects these actions to sleep regulation in humans.

The original indication is not specified in the available data, so no relationship between an original and a new indication can be drawn. The high TxGNN score (0.9967) reflects a computational prediction only. A mechanistic link to insomnia is speculative.

Other predictions follow the same pattern. All eight predicted indications are L5 with no trials or literature:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Support |
|------|------|------|------|
| 1 | Insomnia | 0.9967 | None documented |
| 2 | ADHD, inattentive type | 0.9957 | None documented |
| 3 | Specific developmental disorder | 0.9944 | None documented |
| 4 | Factor 5 excess with spontaneous thrombosis | 0.9916 | None documented |
| 5 | Antithrombin deficiency type 2 | 0.9916 | None documented |
| 6 | Heparin cofactor 2 deficiency | 0.9912 | None documented |
| 7 | Migraine disorder | 0.9907 | None documented |
| 8 | ADHD | 0.9906 | None documented (overlaps with rank 2) |

The coagulation-related predictions (ranks 4–6) come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | MOSQUITO BUG OFF (Lydia Co., Ltd.) | Liquid | Not specified (status: cancelled) |


## Safety Considerations

- **Neurotoxicity**: DEET has known neurotoxicity signals at high exposure, which is a particular concern for neurological and developmental indications (insomnia, ADHD, developmental disorders).
- **Irritant potential**: DEET is a known irritant and may provoke headache in sensitive individuals, which is relevant to the migraine prediction.

No drug interaction records were found, and no contraindications from the knowledge graph were identified. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All eight predictions are supported only by model scores, with no clinical trials, literature, or documented mechanism. DEET's neurotoxicity signals make neurological and developmental indications especially unfavorable without foundational data. The only U.S. license is cancelled, and no label-based safety information is available.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Preclinical evidence of a biological link to the predicted indication (e.g., sleep-related targets for insomnia)
- A toxicology and exposure assessment for any systemic or therapeutic use, since DEET is used topically as a repellent
- Route and formulation feasibility assessment, as route compatibility has not yet been evaluated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

