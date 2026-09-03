---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 1301
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

> Zanamivir is a neuraminidase inhibitor publicly known for the treatment and prevention of influenza A and B (this indication is not yet confirmed in the current regulatory dataset).
> The TxGNN model predicts a possible new indication in **Pyelonephritis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the mechanistic rationale available indicates limited biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the regulatory dataset (0 licenses on file). Based on public drug information, Zanamivir is indicated for treatment/prophylaxis of influenza A and B — not independently confirmed here. |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only, no supporting clinical trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this drug entry is currently a data gap. Based on the repurposing rationale generated alongside this prediction, Zanamivir is a viral neuraminidase inhibitor that targets a surface glycoprotein of the influenza virus, and its established clinical role is antiviral treatment of influenza.

Pyelonephritis is a bacterial ascending urinary tract infection with a fundamentally different pathophysiology — it does not involve viral neuraminidase, and there is no known host neuraminidase pathway implicated in its disease process. The mechanistic rationale accompanying this prediction explicitly states that there is **no biological plausibility** connecting Zanamivir's mode of action to pyelonephritis, and that the high TxGNN score likely reflects a knowledge-graph association artifact rather than genuine mechanistic or clinical evidence.

Given this, the prediction should be treated as a hypothesis-generating signal only, not as a mechanistically grounded repurposing candidate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Zanamivir currently has no license/NDA records in the regulatory dataset (market status: Not Marketed, 0 total licenses). No product- or dosage-form-level information is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is evidence level L5 (model prediction only) with zero supporting clinical trials or publications, and the mechanistic rationale itself flags an absence of biological plausibility between Zanamivir's antiviral mechanism and bacterial pyelonephritis. There is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- MOA and TFDA label/warning data (DG002, DG001 — currently blocking safety review)
- Independent mechanistic or preclinical evidence linking neuraminidase inhibition (host or bacterial) to pyelonephritis pathophysiology
- Any real-world, case-report, or observational data, since no clinical trials or literature currently exist for this indication
- Re-evaluation of the TxGNN association to rule out knowledge-graph entity-matching artifacts (as seen with the rank-2 candidate, where unrelated neuraminidase-resistance literature was linked to an unrelated metabolic disorder)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

