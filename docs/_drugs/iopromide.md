---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 806
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide (DB09156) is a non-ionic iodinated X-ray contrast medium used for diagnostic imaging (angiography, CT, urography) — it has no on-file therapeutic indication. TxGNN's top prediction, **Osteoarthritis Susceptibility**, scores **99.57%**, but is supported by **zero clinical trials** and **zero publications**, and the model's own mechanistic rationale flags this as a likely knowledge-graph artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic contrast agent for radiographic/CT imaging (no therapeutic indication on record; no Taiwan license found) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status | 未上市 (Not Marketed) — 0 licenses on file in Taiwan |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known information, iopromide is a non-ionic iodinated contrast agent whose only established clinical role is as an imaging aid — it is administered to visualize vasculature, organs, or the urinary tract, not to treat disease.

The predicted indication, "osteoarthritis susceptibility," describes a genetic/risk-factor category rather than a treatable clinical endpoint, and there is no known pharmacological pathway connecting an iodinated contrast agent to joint disease modification. The evidence pack's own rationale is explicit on this point: the high TxGNN score most likely arises from knowledge-graph edges representing "contrast agent used to image a joint/bone condition" being conflated with a therapeutic relationship — a common failure mode for imaging agents in repurposing models.

This pattern holds across the other top-ranked predictions in this evidence pack as well. Rank 2 (osteoarthritis) and rank 3 (rheumatoid arthritis) show the same signature — the only literature hit for rheumatoid arthritis (PMID 19435939) describes using iopromide-enhanced CT to *image* synovitis, not to treat it. Rank 9 (hemoglobinopathy) is more concerning: rather than supporting repurposing, the literature includes a case report (PMID 16628721) of a cerebral vaso-occlusive event following low-osmolar IV contrast in a sickle cell disease patient — a potential harm signal, not a benefit signal. Taken together, none of the top 10 predictions in this pack constitute a plausible repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No market authorization is on file for iopromide in Taiwan (0 licenses; market status: 未上市/Not Marketed). No product/dosage-form data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information (key warnings, contraindications, and drug interaction data are not currently on file — DG001, Blocking).

**Additional signal identified in literature (outside the formal safety dataset):** one case report (PMID 16628721) describes a cerebral vaso-occlusive event in a sickle cell disease patient following low-osmolar IV contrast administration. This surfaced only under the "hemoglobinopathy" prediction branch, not the formal safety fields, but is relevant to any future evaluation of iopromide in patients with hemoglobinopathies and should be tracked alongside the TFDA label review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or therapeutic literature support (Evidence Level L5), and the evidence pack's own mechanistic analysis concludes the TxGNN score likely reflects contrast-imaging co-occurrence rather than a real drug–disease relationship. A Blocking data gap (TFDA label/warnings, DG001) also prevents any safety pre-screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) to close DG001 before any S1 safety evaluation
- Confirmed mechanism of action (DG002) to test whether any plausible pharmacological link to osteoarthritis exists
- Re-scoring or filtering of TxGNN output to account for imaging-agent co-occurrence artifacts, given the same pattern appears across ranks 1–10
- If pursued further, a targeted safety review of iopromide use in hemoglobinopathy/sickle cell populations given the vaso-occlusive event signal noted above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

