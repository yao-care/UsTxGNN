---
layout: default
title: Tropicamide
parent: 僅模型預測 (L5)
nav_order: 1269
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tropicamide: From Ophthalmic Mydriasis to Cauda Equina Syndrome

## One-Sentence Summary

> Tropicamide is a short-acting antimuscarinic agent used topically as eye drops to induce mydriasis (pupil dilation) for ophthalmic examinations.
> The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
> but **no clinical trials** and **no publications** currently support this direction — the prediction rests solely on the model's graph-based inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ophthalmic mydriasis (pupil dilation for eye examinations) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank for this candidate. Based on the rationale accompanying the evidence pack, Tropicamide is a short-acting antimuscarinic drug (M3 muscarinic receptor antagonist) applied topically to the eye to produce pupil dilation and cycloplegia; it has no approved systemic indication.

Cauda equina syndrome is a neurological compression disorder of the lumbosacral nerve roots, with no established pathophysiological link to muscarinic receptor blockade. The evidence pack's own mechanistic assessment states that this prediction likely arises through an indirect graph path — possibly via "neurogenic bladder/bowel dysfunction," a common *complication* of cauda equina syndrome, rather than a treatment for the underlying nerve compression itself. No plausible causal mechanism connecting Tropicamide to cauda equina syndrome treatment has been identified.

By contrast, the model's second- and third-ranked predictions (neurogenic bladder, irritable bowel syndrome) at least have class-level pharmacological plausibility, since other antimuscarinics (oxybutynin, dicyclomine, hyoscyamine) are established treatments for these conditions via smooth-muscle relaxation. However, Tropicamide's topical ocular route of administration results in minimal systemic bioavailability, making it pharmacokinetically unsuited to reach therapeutic concentrations in the bladder or gut even under this class-level analogy. Overall, this candidate reflects a model-only signal without drug-specific mechanistic or clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Tropicamide currently has no marketing authorization on file (market status: Not Marketed; 0 licenses recorded), so no product/indication table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications data are currently unavailable and are flagged as a **Blocking** data gap — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a TxGNN model score (L5, no clinical trials or literature), and the accompanying mechanistic review explicitly could not establish a plausible causal link between Tropicamide and cauda equina syndrome. Combined with the drug's unmarketed status and unresolved safety data gaps, there is insufficient basis to advance beyond S0.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — currently a **Blocking** gap (DG001)
- Confirmed mechanism of action data from DrugBank — currently a **High** severity gap (DG002)
- Preclinical or mechanistic studies specifically evaluating systemic antimuscarinic effects relevant to cauda equina syndrome, neurogenic bladder, or IBS
- Pharmacokinetic assessment of systemic exposure achievable via ophthalmic dosing, if systemic repurposing is to be considered at all
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

