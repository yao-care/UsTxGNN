---
layout: default
title: Procainamide
parent: 僅模型預測 (L5)
nav_order: 1085
evidence_level: L5
indication_count: 10
---

# Procainamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Procainamide: From Cardiac Arrhythmia to Tourette Syndrome

## One-Sentence Summary

> Procainamide is classically known as a Class Ia antiarrhythmic (sodium channel blocker) used for cardiac arrhythmias, though the evidence pack itself contains no structured record of its original approved indication.
> The TxGNN model's top prediction is **Tourette syndrome**, but this is supported by **0 clinical trials** and **0 publications** — the signal comes purely from the model score, with no mechanistic, clinical, or literature evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from evidence pack (no license records; drug is generally known as a Class Ia antiarrhythmic) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for procainamide is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, procainamide is a Class Ia antiarrhythmic that acts via cardiac sodium channel blockade, and is not associated with any known central nervous system or neuropsychiatric mechanism.

For the top-ranked prediction, Tourette syndrome, the model's own repurposing rationale is explicit and cautionary: *"no known mechanistic link — procainamide is a sodium channel blocker with no relationship to the dopamine/GABA-related pathology of Tourette syndrome; this is purely a model prediction score with no clinical or literature support."* No clinical trials or published literature currently support this indication.

Given this, the prediction should be treated as an unvalidated model artifact rather than a scientifically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorizations are on record for procainamide in this evidence pack (`total_licenses: 0`); market status is listed as **Not marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Tourette syndrome) has a high TxGNN similarity score but zero supporting clinical trials, zero publications, and an explicitly stated lack of mechanistic plausibility — this is Evidence Level L5 (model prediction only). The drug is also not currently marketed and lacks basic MOA and safety-label data, both flagged as blocking/high-severity gaps.

**Additional context:** the other high-ranked candidates in this evidence pack do not strengthen the case — literature for *hyperthyroidism* and *Prinzmetal angina* describes procainamide being used to manage arrhythmic complications in those conditions rather than treating the underlying disease, and evidence for *rheumatoid arthritis* points in the opposite direction (procainamide is a well-documented cause of drug-induced lupus/autoantibody formation, a safety signal rather than a therapeutic one).

**To proceed, the following is needed:**
- Procainamide MOA data (DrugBank API query)
- TFDA/FDA label warnings, contraindications, and DDI data (currently all [Data Gap])
- A dedicated mechanistic rationale connecting sodium-channel blockade to Tourette syndrome pathophysiology, ideally from preclinical or case-level sources
- Reassessment of lower-ranked candidates only if independent mechanistic evidence emerges — current top candidates do not warrant further investment at this time
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

