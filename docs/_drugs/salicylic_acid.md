---
layout: default
title: Salicylic Acid
parent: 僅模型預測 (L5)
nav_order: 1143
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
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

# Salicylic Acid: From Topical Dermatological Use to Papillary Conjunctivitis

## One-Sentence Summary

> Salicylic acid is a keratolytic agent primarily known for topical dermatological use, but detailed regulatory indication and mechanism-of-action data are not available in this dataset.
> The TxGNN model predicts it may be effective for **Papillary Conjunctivitis**,
> but **no clinical trials** and **no publications** currently support this direction — the model's own rationale flags this as a likely false-positive association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset (salicylic acid is generally used as a topical keratolytic for dermatological conditions; no specific regulatory indication text on file) |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a High-severity data gap). Based on known pharmacology, salicylic acid is a keratolytic agent that acts by dissolving intercellular cement in the stratum corneum, and is used topically for conditions such as acne, warts, calluses, and psoriasis.

There is no established pharmacological pathway connecting a keratolytic skin agent to papillary conjunctivitis, an inflammatory condition of the ocular mucosa. The model's own repurposing rationale is explicit on this point: it states that salicylic acid "lacks a pharmacological basis" for this conjunctival condition, and that mucosal irritation is a known **risk**, not a therapeutic mechanism, of salicylic acid exposure.

The rationale further suggests that the high TxGNN score likely reflects a **clustering artifact** in the knowledge graph — where "inflammatory ocular surface disease" nodes are embedded near each other regardless of causal drug relationships — rather than genuine mechanistic or causal evidence. This candidate should therefore be interpreted with significant caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Currently no marketing authorization records — this drug is not currently marketed under the reviewed dataset (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/FDA labeling warnings and contraindications for this drug are currently an unresolved **Blocking** data gap (DG001), meaning a formal safety (S1) assessment cannot yet be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (Evidence Level L5), the drug is not currently marketed, and the model's own mechanistic rationale explicitly identifies the prediction as a probable knowledge-graph artifact rather than a biologically plausible signal.

**To proceed, the following is needed:**
- Resolve the Blocking data gap on labeling warnings/contraindications (DG001) before any safety-stage review
- Obtain verified mechanism-of-action data (DG002) to properly assess mechanistic plausibility
- Preclinical or in-vitro evidence establishing any relevant activity in ocular/conjunctival tissue
- Re-evaluation against the other 9 ranked candidates (all also L5/Hold), several of which (e.g., spondyloarthropathy susceptibility, given salicylic acid's relation to aspirin's COX-inhibitory mechanism) may warrant relatively higher mechanistic interest despite equally absent clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

