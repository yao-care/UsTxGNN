---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 753
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Glimepiride: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea antidiabetic, pharmacologically known for stimulating insulin secretion via pancreatic β-cell SUR1/KATP channels (Type 2 Diabetes Mellitus is its established use, though a formal indication text is not present in this evidence pack). The TxGNN model predicts a high score (**99.75%**) for **Classic Stiff Person Syndrome**, but **0 clinical trials** and **0 publications** currently support this specific drug–disease pairing, and the model's own mechanistic review flags this as a likely false association driven by a shared knowledge-graph node (GAD65) rather than genuine pharmacological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (drug not marketed; no license data). Based on known pharmacological class, glimepiride is a sulfonylurea used for Type 2 Diabetes Mellitus |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The formal `original_moa` field is a data gap, but the evidence pack's own mechanistic annotation describes glimepiride as a sulfonylurea that binds SUR1/KATP channels on pancreatic β-cells to stimulate insulin secretion — a well-established antidiabetic mechanism.

Classic Stiff Person Syndrome (SPS) is a rare autoimmune neurological disorder caused by anti-GAD65 antibodies damaging GABAergic neurons in the CNS. GAD65 is coincidentally also a pancreatic β-cell autoantigen, and Type 1 Diabetes and SPS are known clinical comorbidities. This shared "GAD65" node in the knowledge graph is almost certainly what is driving the high TxGNN score — **not** a genuine pharmacological pathway connecting glimepiride to SPS pathophysiology.

The evidence pack's own analysis explicitly labels this as a mechanistically implausible, high-score/low-plausibility association ("偽關聯"), rather than a credible repurposing rationale. No clinical trial, trial registry, or literature evidence exists to counter this assessment. This candidate should be treated as a knowledge-graph artifact pending further validation, not as a supported repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No approved authorizations on record — the drug is not marketed in this jurisdiction (`total_licenses = 0`, no license entries).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are a blocking data gap — see DG001 below.)*

---

## Other Ranked Candidates (Context)

All 9 TxGNN-predicted indications in this evidence pack carry Evidence Level L5 (model prediction only) with a scoring recommendation of **Hold**, and none has supporting clinical trial or trial-registry evidence. One exception is worth flagging: rank 9, *pancreatic agenesis*, retrieved a single tangential PubMed reference (PMID 12720536, on endosonographic pitfalls in insulinoma imaging) — not disease-relevant evidence. More importantly, its own mechanistic rationale argues the *opposite* of support: pancreatic agenesis typically leaves no residual functional β-cells, so glimepiride's SUR1/KATP-dependent mechanism would be expected to be ineffective — this should be read as a negative/contraindicating signal, not corroborating evidence. The remaining 7 candidates (stiff limb syndrome, opsismodysplasia, thiamine-responsive dysfunction syndrome, and four lipodystrophy variants) share no established pathophysiological link to sulfonylurea pharmacology per the evidence pack's own annotations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Classic Stiff Person Syndrome) has a high TxGNN score but zero supporting clinical or literature evidence, and the mechanistic review itself identifies the association as likely spurious (shared GAD65 knowledge-graph node rather than a real pharmacological pathway). Across all 9 ranked candidates, no pairing reaches beyond Evidence Level L5, and none has a coherent, literature-supported mechanistic rationale.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, blocking — required before any S1 safety screening)
- Verified original mechanism-of-action documentation from DrugBank (DG002)
- Broader literature search using free-text terms (e.g., "sulfonylurea" + "stiff person syndrome") rather than exact disease-name matching only, since the current zero-hit queries may reflect terminology mismatch rather than a true absence of evidence
- Re-evaluation once independent (non-KG-node-sharing) mechanistic or case-level evidence emerges for any of the 9 candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

