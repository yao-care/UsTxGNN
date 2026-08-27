---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 650
evidence_level: L5
indication_count: 3
---

# Empagliflozin
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

# Empagliflozin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor originally developed for type 2 diabetes mellitus (later expanded in real-world use to heart failure and chronic kidney disease). The TxGNN model predicts a possible link to **Classic Stiff Person Syndrome**, but this prediction is currently backed by **0 clinical trials** and **0 publications** — it reflects knowledge-graph topological similarity only, not any documented pharmacological or clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (general drug knowledge; not present in evidence pack — see data gaps below) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable for this evidence pack (DrugBank query returned no MOA text). Based on general pharmacological knowledge, empagliflozin inhibits SGLT2 in the renal proximal tubule, reducing glucose reabsorption — a mechanism specific to glucose/renal handling with no established connection to GABAergic neurotransmission or autoimmune neurology.

Classic stiff person syndrome is driven by anti-GAD65 autoantibodies that impair GABA synthesis, causing disrupted inhibitory signaling in the spinal cord and brainstem. The evidence pack's own mechanistic assessment states plainly that there is **no known intersection** between SGLT2 inhibition and this autoimmune/GABAergic pathway, and that the high TxGNN score (0.99) reflects graph-topology proximity rather than mechanistic support — the assessment explicitly flags this as a **low-confidence prediction**.

The two lower-ranked candidates (focal stiff limb syndrome, rank 2; opsismodysplasia, rank 3) share this pattern: focal stiff limb syndrome carries the *identical* TxGNN score as the top prediction, consistent with being a neighboring node pulled along by the same graph cluster rather than an independently supported signal. Opsismodysplasia's rationale invokes an indirect PI3K/insulin-signaling link (via SHIP2) that the evidence pack itself characterizes as an over-extended connection with no supporting literature. None of the three predictions currently rise above model-output-only status.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Empagliflozin currently holds no NDA or marketing authorization on file in this evidence pack (market status: **Not Marketed**; total licenses: **0**).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/FDA label warnings and contraindications could not be retrieved for this evidence pack — this is flagged as a **Blocking** data gap that prevents a full S1 safety evaluation.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications (classic stiff person syndrome, focal stiff limb syndrome, opsismodysplasia) rest solely on model score (L5) with zero clinical trials or literature, and the mechanistic rationale explicitly finds no established pharmacological link to SGLT2 inhibition. Combined with the absence of US marketing status and a blocking gap in safety-label data, there is no basis to advance any of these candidates past initial screening.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings and contraindications (blocking gap — required before any S1 safety review)
- Confirmed mechanism of action data from DrugBank or the approved label
- Preclinical or case-level evidence linking SGLT2 inhibition to GABAergic/autoimmune neurology or skeletal dysplasia pathways, if such a rationale is to be pursued further
- Reassessment of regulatory/licensing pathway given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

