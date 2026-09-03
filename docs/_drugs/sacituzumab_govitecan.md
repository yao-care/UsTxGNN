---
layout: default
title: Sacituzumab Govitecan
parent: 僅模型預測 (L5)
nav_order: 1141
evidence_level: L5
indication_count: 4
---

# Sacituzumab Govitecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using no specialized skill here — this is a straightforward evidence-pack-to-report writing task with a fixed template; proceeding directly.

# Sacituzumab Govitecan: From Oncology (Antibody-Drug Conjugate) Therapy to Drug-Induced Osteoporosis

## One-Sentence Summary

> Sacituzumab govitecan is a Trop-2 targeted antibody-drug conjugate carrying the cytotoxic payload SN-38 (a topoisomerase I inhibitor); its original approved indication is not documented in the current evidence pack.
> The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but this is a **model-score-only prediction (L5)** with **zero supporting clinical trials and zero supporting literature**, and the accompanying mechanistic analysis explicitly flags it as pharmacologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available data |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal MOA documentation is not available in this evidence pack (flagged as a High-severity data gap, DG002). However, the mechanistic rationale accompanying the prediction identifies sacituzumab govitecan as a Trop-2-directed antibody-drug conjugate whose cytotoxic payload, SN-38, is a topoisomerase I inhibitor that induces DNA damage and myelosuppression — a mechanism consistent with its known use as an oncology therapeutic.

Critically, **this mechanism does not support the predicted indication**. The evidence pack's own repurposing rationale states that cytotoxic chemotherapy agents are more commonly associated with *causing* bone loss (e.g., chemotherapy-induced menopause, corticosteroid co-administration) rather than treating osteoporosis. The direction of the prediction is opposite to established pharmacology, and the same pattern repeats across all four ranked candidates (osteoporosis, diabetic retinopathy — two variants, diabetic cataract): none have a plausible mechanistic link to SN-38's cytotoxic, DNA-damaging activity, and several conditions (retinal/ocular disease) instead overlap with known ADC-class ocular toxicity signals.

Given this, the prediction should be interpreted as likely **knowledge-graph embedding noise** rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorizations are currently on record for this product in this jurisdiction (market status: Not Marketed; total licenses: 0).

---

## Cytotoxicity

Sacituzumab govitecan is an antibody-drug conjugate carrying a cytotoxic topoisomerase I inhibitor payload (SN-38), meeting criteria for antineoplastic/cytotoxic classification.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Trop-2 antibody-drug conjugate) with conventional cytotoxic payload (SN-38, topoisomerase I inhibitor) |
| Myelosuppression Risk | High — SN-38 payload is known to induce DNA damage and myelosuppression |
| Emetogenicity Classification | Moderate to High — consistent with topoisomerase I inhibitor class (SN-38/irinotecan-related agents) |
| Monitoring Items | CBC with differential (neutropenia), liver and renal function, GI toxicity/diarrhea monitoring, infusion-related reaction monitoring |
| Handling Protection | Yes — must follow cytotoxic/hazardous drug handling regulations applicable to ADC agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four ranked predictions carry TxGNN scores above 99% but have **no supporting clinical trials or literature** (Evidence Level L5), and the mechanistic analysis explicitly identifies the top candidate — and the pattern across all candidates — as contrary to SN-38's known cytotoxic pharmacology. This is best interpreted as a knowledge-graph embedding artifact rather than a viable repurposing lead.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, Blocking — required before any S1 safety screening)
- Formal, sourced mechanism of action and confirmed original approved indication(s) (DG002)
- A mechanistically plausible candidate indication before allocating further review resources — current top-4 candidates do not meet this bar
- If repurposing exploration continues, prioritize lower-ranked TxGNN candidates with actual clinical trial or literature support, rather than acting on score alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

