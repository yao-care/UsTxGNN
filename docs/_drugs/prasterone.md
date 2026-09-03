---
layout: default
title: Prasterone
parent: 僅模型預測 (L5)
nav_order: 1074
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: From No Documented Indication to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

> Prasterone (DHEA, DrugBank DB01708) currently has no marketed formulation and no approved indication on file in this evidence pack.
> The TxGNN model predicts a possible link to **Heparin Cofactor 2 Deficiency**, with a very high computational score (99.99%),
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no biological or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no marketing licenses or MOA data on file) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Prasterone in this evidence pack (flagged as a High-severity data gap — DG002). No original approved indication is on file either, so there is no established pharmacological baseline from which to assess relevance to the predicted indication.

For the top-ranked prediction, the model itself flags the disconnect: heparin cofactor 2 deficiency is an extremely rare coagulation disorder, and there is no literature exploring any relationship between DHEA and heparin cofactor II activity. The TxGNN score is high purely on knowledge-graph topology — it reflects a statistical association within the graph, not a validated or hypothesized biological mechanism. Without MOA data or any supporting evidence, biological plausibility cannot currently be established for this specific indication.

It's worth noting that two other predictions in this pack — **thrombophilia** (rank 4) and **scleroderma** (rank 7) — do have supporting observational literature (androgen levels correlating with disease severity), and are staged further along (L4/S1, "Research Question") than the top-ranked candidate. These may be more productive directions for further review, though they are not the focus of this report per the ranking convention.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorizations are currently on file for Prasterone. Market status is recorded as **Not Marketed**, with 0 total licenses.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields — key warnings, contraindications, and drug-drug interactions — are currently data gaps; TFDA labeling review is flagged as a Blocking gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it is unsupported by any clinical trials or literature, and the drug itself lacks both MOA and original-indication data needed to assess biological plausibility. This does not meet the threshold to proceed.

**To proceed, the following is needed:**
- TFDA/FDA label (warnings, contraindications) — currently a **Blocking** gap (DG001)
- Mechanism of action data from DrugBank — currently a **High**-severity gap (DG002)
- Any mechanistic or preclinical rationale connecting DHEA to hemostasis/coagulation cofactor pathways
- If pursuing further, consider prioritizing **thrombophilia** or **scleroderma** instead, given their existing (though still non-interventional) literature base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

