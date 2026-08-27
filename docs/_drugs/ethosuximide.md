---
layout: default
title: Ethosuximide
parent: 僅模型預測 (L5)
nav_order: 682
evidence_level: L5
indication_count: 1
---

# Ethosuximide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ethosuximide: From Absence Seizures to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ethosuximide is a T-type calcium channel blocker traditionally used to treat absence seizures. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own mechanistic rationale flags the link as likely a false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence seizures (epilepsy) — per pharmacological reference; not confirmed via regulatory filing, as the drug is not marketed in Taiwan/US |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.91% (rank 2935) |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ethosuximide in this evidence pack. Based on known pharmacological information, ethosuximide inhibits T-type (Cav3) calcium channels in thalamic neurons, an action that underlies its efficacy in absence seizures.

NSIAD is caused by a gain-of-function mutation in the AVPR2 (vasopressin V2) receptor, leading to constitutive activation of the Gs–cAMP–PKA signaling pathway and ADH-independent water retention with hyponatremia. There is no known mechanistic intersection between T-type calcium channel blockade and the V2 receptor–cAMP–PKA pathway.

Given the absence of MOA data on file, the absence of any supporting clinical trials or literature, and the explicit assessment that the pharmacological link is weak and speculative, this prediction should be treated as **highly likely a false positive** arising from knowledge-graph topological similarity rather than a genuine pharmacological relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Ethosuximide has no registered authorizations in the current dataset (0 NDAs; market status: not marketed). No product/dosage form information is available.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications data is currently a blocking data gap (DG001) — this drug cannot proceed past initial safety screening (S1) until this is resolved.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on TxGNN model output (L5, no clinical or literature corroboration), and the mechanistic rationale itself concludes the drug–disease link is pharmacologically implausible and likely a knowledge-graph artifact. Combined with a blocking data gap on TFDA safety labeling, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) — currently blocking
- Confirmed mechanism of action (MOA) from DrugBank or primary literature
- Independent mechanistic or preclinical evidence linking T-type calcium channel blockade to AVPR2/cAMP-PKA signaling, if this candidate is to be reconsidered
- At minimum, case reports or preclinical studies before re-evaluating evidence level above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

