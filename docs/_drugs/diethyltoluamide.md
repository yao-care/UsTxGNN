---
layout: default
title: Diethyltoluamide
parent: Model Prediction Only (L5)
nav_order: 605
evidence_level: L5
indication_count: 8
monitor_inn: "DIETHYLTOLUAMIDE"
predicted_indications: ["insomnia (disease)", "attention deficit hyperactivity disorder, inattentive type", "specific developmental disorder", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "heparin cofactor 2 deficiency", "migraine disorder", "attention deficit-hyperactivity disorder"]
last_modified_at: 2026-10-14
description: "Diethyltoluamide: predicted new indication Insomnia (evidence level L5). Approved use: Not available"
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Diethyltoluamide: From an Insect Repellent (No Approved Indication on Record) to Insomnia

## One-Sentence Summary

Diethyltoluamide (DEET) is widely known as an insect repellent, and its only U.S. record in the data compiled for this report is a cancelled liquid product with no approved indication text.
The TxGNN model predicts it may be effective for **insomnia** (score 99.67%), but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only prediction with no supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the one U.S. license on record has no indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. DEET is known as an insect repellent that acts on insect olfactory receptors, and it has been reported to inhibit acetylcholinesterase in insects. No documented link connects these actions to sleep regulation in humans.

The original indication is not specified in the available data, so no relationship between an original and a new indication can be drawn. The high TxGNN score (0.997) reflects a computational prediction only. A mechanistic link to insomnia is speculative.

Other predictions follow the same pattern. All eight predicted indications are L5 with no trials or literature:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Support |
|------|------|------|------|
| 1 | Insomnia | 99.67% | None documented |
| 2 | ADHD, inattentive type | 99.57% | None documented |
| 3 | Specific developmental disorder | 99.44% | None documented |
| 4 | Factor 5 excess with spontaneous thrombosis | 99.16% | None documented |
| 5 | Antithrombin deficiency type 2 | 99.16% | None documented |
| 6 | Heparin cofactor 2 deficiency | 99.12% | None documented |
| 7 | Migraine disorder | 99.07% | None documented |
| 8 | ADHD | 99.06% | None documented (overlaps with rank 2) |

The coagulation-related predictions (ranks 4–6) appear to be graph-based artifacts, likely driven by network proximity rather than biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | MOSQUITO BUG OFF (Lydia Co., Ltd.) | Liquid | Not specified (status: cancelled) |

No valid single-ingredient or combination licenses are currently active.

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

