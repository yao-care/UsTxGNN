---
layout: default
title: Scopolamine
parent: 僅模型預測 (L5)
nav_order: 1145
evidence_level: L5
indication_count: 6
---

# Scopolamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Scopolamine: From Unspecified Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Scopolamine (DrugBank DB00747) is a non-selective muscarinic receptor antagonist; no original indication is recorded in the current evidence pack. The TxGNN model predicts potential relevance to **Cauda Equina Syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags a possible directional mismatch (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the available evidence pack |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Scopolamine in this evidence pack, and no original indication is on file. What is known is that Scopolamine acts as a non-selective muscarinic (anticholinergic) receptor antagonist — a class of drugs generally used to reduce smooth muscle spasm, secretions, or (in ophthalmology) induce pupil dilation and ciliary muscle paralysis.

For the top-ranked prediction, **Cauda Equina Syndrome**, the evidence pack's own mechanistic rationale raises a significant concern rather than confirming applicability: cauda equina syndrome typically presents with neurogenic bladder dysfunction characterized by urinary retention from a **hypotonic/acontractile** detrusor muscle. An anticholinergic agent like scopolamine would be expected to further suppress residual detrusor contraction, potentially **worsening** rather than treating urinary retention — i.e., the mechanism points in the opposite direction of clinical need. This is characterized in the evidence pack as a "high-risk mismatch hypothesis," not merely an untested but plausible one.

The remaining five candidates (obsolete neurogenic bladder concept, papillary/atopic/rosacea/vernal conjunctivitis) show similarly weak or indirect mechanistic links — largely attributable to knowledge-graph neighborhood effects (e.g., shared "ophthalmic drug" or "bladder-related" nodes) rather than genuine pharmacological rationale, and none have any supporting trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Scopolamine is currently **not marketed** in the reviewed jurisdiction, and no license/NDA records are present in the evidence pack (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA label warnings/contraindications are flagged as a **Blocking** data gap (DG001) in the evidence pack — this must be resolved before any safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six predicted indications are TxGNN score–only associations (Evidence Level L5) with zero supporting clinical trials or literature. The highest-ranked candidate, Cauda Equina Syndrome, carries an explicit mechanistic red flag — an anticholinergic agent may worsen the underlying urinary retention rather than treat it — making it unsuitable to advance without further mechanistic clarification.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism of action (MOA) for Scopolamine (High-severity data gap, DG002)
- Clarification of the actual disease concept behind "obsolete neurogenic bladder (disease)" in the knowledge graph, including bladder-dysfunction subtype (spastic vs. hypotonic)
- Preclinical or case-level evidence specifically evaluating scopolamine (not other anticholinergics) in neurogenic bladder/cauda equina syndrome contexts
- Drug interaction (DDI) data, currently unavailable (`query_status: not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

