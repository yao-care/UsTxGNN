---
layout: default
title: Naphazoline
parent: 僅模型預測 (L5)
nav_order: 953
evidence_level: L5
indication_count: 10
---

# Naphazoline
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

# Naphazoline: From Nasal/Ocular Decongestion to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Naphazoline is an imidazoline-class α1-adrenergic agonist, described in this evidence pack's own rationale notes as a topical vasoconstrictor conventionally used to relieve nasal and ocular mucosal congestion (formal MOA data is flagged as a gap). The TxGNN model's top prediction points to **Hypotrichosis Simplex of the Scalp**, but this direction is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic annotation explicitly argues *against* biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in a formal US license (0 NDAs on file); evidence-pack notes describe conventional use as a topical nasal/ocular decongestant |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.83% (absolute rank 5,091 among all candidates) |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for naphazoline is currently unavailable (flagged as a **Blocking/High-severity data gap** in this evidence pack). Based on the drug's known pharmacological class, naphazoline is an imidazoline α1-adrenergic receptor agonist that produces local vasoconstriction — the basis for its conventional use in relieving nasal and ocular congestion.

The evidence pack's own mechanistic annotation for this prediction is explicit that this pharmacology does **not** support a role in scalp hair regrowth: hypotrichosis simplex of the scalp is a genetic disorder of hair follicle cycling, and no vasoconstrictor mechanism is known to promote follicular growth. If anything, established hair-growth agents (e.g., minoxidil) work through local **vasodilation**, the opposite pharmacological direction from naphazoline. The TxGNN score therefore should be read as a graph-embedding similarity signal rather than a mechanistically grounded hypothesis.

It is also worth noting that all 10 predicted indications in this evidence pack (ranks 1–10, covering hair-loss/growth disorders, glaucoma, and unrelated congenital syndromes) carry the same pattern: very high TxGNN similarity scores (99.5–99.8%) but very low absolute ranks (5,000–11,500+), no clinical trials, and either no literature or literature that is topically unrelated (e.g., the periodontitis literature surfaced for rank 9 does not mention naphazoline or vasoconstrictors at all). This is consistent with a batch of low-confidence, exploratory model outputs rather than a validated signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

No US marketing authorizations are on file for naphazoline in this evidence pack (market status: not marketed, 0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is evidence level L5 (model prediction only) with no supporting clinical trials or literature, and the drug's own mechanistic rationale contradicts the plausibility of the predicted indication (vasoconstriction vs. the vasodilation typically needed for hair regrowth). Combined with missing MOA data and no TFDA/US labeling on file, there is not enough basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for naphazoline (DrugBank API query — currently a High-severity gap)
- TFDA/FDA label warnings and contraindications (currently a Blocking gap preventing any safety pre-screen)
- Preclinical or mechanistic studies specifically linking imidazoline α1-agonism to hair follicle biology, if this candidate is to be pursued further
- Given the contradictory mechanistic direction, consider whether this candidate should be deprioritized in favor of higher-ranked, better-supported predictions from other drugs in the pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

