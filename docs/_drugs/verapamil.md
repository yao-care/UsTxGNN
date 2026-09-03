---
layout: default
title: Verapamil
parent: 僅模型預測 (L5)
nav_order: 1287
evidence_level: L5
indication_count: 7
---

# Verapamil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Verapamil: From Unspecified Original Indication to Obsolete Bundle Branch Block

## One-Sentence Summary

> No original indication data is on file for this drug in the current regulatory dataset (0 licenses recorded).
> The TxGNN model's top-ranked prediction is **Obsolete Bundle Branch Block**, with a **99.62%** prediction score,
> but **no clinical trials and no literature** currently support this direction — and the mechanistic rationale provided actually argues *against* it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license records on file |
| Predicted New Indication | Obsolete Bundle Branch Block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured record (flagged as a High-severity data gap, DG002). The evidence pack's own repurposing rationale, however, identifies verapamil as an **L-type calcium channel blocker with negative dromotropic (conduction-slowing) activity**.

This is precisely why the top-ranked prediction is **not** mechanistically reasonable: in patients with existing bundle branch block or AV conduction disease, verapamil's conduction-slowing effect is a recognized **risk factor requiring caution or contraindication**, not a therapeutic target. The evidence pack explicitly notes the TxGNN score likely reflects node co-occurrence in the knowledge graph rather than a genuine treatment relationship, and no clinical trial or literature evidence was found to support this indication.

Given this, the top prediction should be treated as a **negative/implausible signal** rather than a repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No license records are available for this drug (0 NDAs on file; market status: Not Marketed). Regulatory/label data has not yet been collected — see Safety Considerations below.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data have not yet been collected for this drug (flagged as a **Blocking** data gap — DG001: TFDA label warnings/contraindications — which must be resolved before any safety pre-screening, S1, can proceed).

---

## Other TxGNN Candidates for This Drug

The evidence pack contains 7 ranked candidates for this drug, all at Evidence Level L5. Most show either no supporting evidence or a mechanistic direction that conflicts with known CCB pharmacology; one stands out as a plausible (if untested) hypothesis:

| Rank | Predicted Indication | Score | Recommendation | Note |
|------|----------------------|-------|-----------------|------|
| 1 | Obsolete Bundle Branch Block | 99.62% | Hold | Mechanistically contradictory (see above) |
| 2 | Malignant Hypertensive Renal Disease | 99.27% | Hold | No trial/literature evidence; wrong care setting (IV titration typically needed) |
| 3 | Malignant Renovascular Hypertension | 99.27% | Hold | Cited literature not specific to verapamil treatment of this condition |
| 4 | Pulmonary HTN, unclear/multifactorial mechanism (Group 5) | 99.26% | Hold | CCBs not indicated per guidelines for this PH group |
| 5 | Pulmonary HTN due to lung disease/hypoxia (Group 3) | 99.26% | Hold | CCBs may worsen V/Q mismatch and systemic hypotension; literature is unrelated (hypoxia biology, not verapamil) |
| 6 | Braddock Syndrome | 99.15% | Hold | No known pathological link; pure KG co-occurrence signal |
| 7 | Periodic Paralysis w/ transient compartment-like syndrome | 99.08% | **Research Question** | Some biological plausibility via skeletal muscle calcium channel (CACNA1S) involvement; no clinical evidence yet — hypothesis-generation only |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All candidates are L5 (model prediction only), with no clinical trials and essentially no directly relevant literature. The top-ranked candidate is mechanistically contradicted by verapamil's known negative dromotropic effect, and a Blocking-severity data gap (missing TFDA label/warnings) prevents even an initial safety screen.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — Blocking gap (DG001), required before any S1 safety screening
- Verapamil MOA confirmation via DrugBank — High-severity gap (DG002)
- If pursuing further, redirect research focus toward Rank 7 (periodic paralysis) as a hypothesis-generation candidate rather than the top-scored but mechanistically contradictory Rank 1 candidate
- Independent literature search specific to verapamil (current literature hits for Ranks 3 and 5 are not drug-specific and should not be counted as supporting evidence)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

