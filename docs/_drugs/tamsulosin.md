---
layout: default
title: Tamsulosin
parent: 僅模型預測 (L5)
nav_order: 618
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# TAMSULOSIN: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tamsulosin is a selective α-1A/1B adrenergic receptor antagonist, globally approved for benign prostatic hyperplasia (BPH) and lower urinary tract symptoms (LUTS), though it currently holds no marketing authorization in Taiwan.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita** — an ultra-rare genetic hair overgrowth disorder linked to the 8q24 chromosomal region.
**No clinical trials or published literature** currently support this direction; this is a purely model-driven hypothesis with significant mechanistic concerns.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia / Lower Urinary Tract Symptoms (global; no Taiwan authorization on record) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.9956% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (0 licenses) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established background knowledge, Tamsulosin (DB00706) is a selective α-1A adrenergic receptor antagonist. By blocking α-1A receptors in prostatic smooth muscle, it reduces urethral resistance and alleviates BPH-related urinary symptoms. Its relative selectivity for α-1A over α-1B also limits systemic blood pressure effects, explaining its widespread clinical use for BPH and, off-label, for ureteral stone expulsion.

Ambras type hypertrichosis universalis congenita is caused by a rearrangement in the 8q24 chromosomal region disrupting TRPS1-related regulatory elements that govern hair follicle development. The proposed mechanistic link to α-1 receptor antagonism is tenuous: α-1 adrenergic receptors are expressed on dermal papilla cells and follicular microvasculature, and blocking them could theoretically modulate sympathetic vasoconstriction, altering follicle perfusion. However, this is far too indirect to address the underlying genetic defect in hair cycle regulation.

Critically, this prediction likely reflects a knowledge graph (KG) artifact: the TxGNN model's near-perfect score (>99.99%) appears to stem from topological proximity between hair biology nodes and the alpha-adrenergic pathway in the underlying KG, rather than genuine therapeutic plausibility. A key contradictory signal exists in the FDA adverse event database (FAERS), where Tamsulosin lists alopecia (hair loss) as a rare adverse effect — the opposite direction of what treating hypertrichosis would require. No preclinical or clinical evidence supports this repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Tamsulosin has not obtained marketing authorization in Taiwan. No NDA or equivalent drug licenses are on record as of the data cutoff (2026-06-22).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications in this pack are rare or genetic disorders (hair overgrowth, hair shaft abnormalities, congenital malformations, periodontal syndromes, migraine with brainstem aura) — none supported by clinical trials or drug-specific literature. The top-ranked prediction for Ambras hypertrichosis reflects an apparent KG topological artifact, not a viable drug-disease mechanism. A documented adverse-effect signal of alopecia in FAERS further undermines the hair disorder cluster as a repurposing direction.

**To proceed, the following is needed:**

- Retrieve Tamsulosin's full MOA profile via DrugBank API to identify any unexpected receptor activities beyond α-1 blockade
- Conduct a systematic FAERS review to quantify and characterize Tamsulosin-associated alopecia reports, which currently contradict the predicted hair disease benefit
- Investigate α-1 receptor functional expression in human dermal papilla cells with in vitro models before any clinical hypothesis can be formed
- Re-examine whether any BPH-adjacent indications (e.g., ureteral stone expulsion, overactive bladder) have stronger mechanistic and regulatory rationale for Taiwan market entry, as these are supported by global clinical evidence
- Obtain the Taiwan package insert (仿單) to complete safety data gap DG001 before any further clinical decision can be made
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

