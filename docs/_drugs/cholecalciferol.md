---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 526
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
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

Based on the Evidence Pack, I'll now generate the evaluation report for Cholecalciferol. The top predicted indication (rank 1) is used as the primary focus.

---

# Cholecalciferol: From Vitamin D Deficiency to Familial Isolated Hypoparathyroidism (Impaired PTH Secretion)

## One-Sentence Summary

Cholecalciferol (Vitamin D3) is a fat-soluble prohormone widely used to correct vitamin D deficiency, nutritional rickets, and related calcium-phosphorus metabolism disorders.
The TxGNN model predicts it may be effective for **Familial Isolated Hypoparathyroidism due to Impaired PTH Secretion** (score 99.79%), yet this specific indication currently has **0 clinical trials** and **0 publications** directly supporting this use.
While a mechanistic link exists through the calcium-VDR pathway, the PTH-deficient state critically impairs cholecalciferol's activation to its therapeutic form, making active vitamin D analogues (calcitriol, alfacalcidol) pharmacologically preferable in standard practice.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin D deficiency, nutritional rickets, osteomalacia |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only — no direct studies found) |
| US Market Status | No prescription NDA records (marketed as OTC dietary supplement) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the queried database (DrugBank API query pending). Based on established pharmacology, however, cholecalciferol (Vitamin D3) is a secosteroid prohormone synthesised in the skin upon UV-B exposure or absorbed from dietary sources. It is sequentially hydroxylated — first in the liver to 25-hydroxyvitamin D3 [25(OH)D3], then in the kidney by 1α-hydroxylase (CYP27B1) to the biologically active hormone calcitriol [1,25(OH)2D3]. Calcitriol binds the vitamin D receptor (VDR) in intestinal epithelial cells and parathyroid tissue, driving calcium absorption and suppressing PTH gene expression.

In familial isolated hypoparathyroidism (FIH) due to impaired PTH secretion, the parathyroid glands cannot produce adequate PTH, leading to hypocalcemia and hyperphosphatemia. There is genuine biochemical overlap with cholecalciferol's domain: even without optimal 1α-hydroxylase activity, cholecalciferol can partially compensate by elevating 25(OH)D3 stores and enhancing calcium absorption through residual VDR signalling (including extra-renal 1α-hydroxylation in macrophages and other tissues). The TxGNN model most likely identified this link through the calcium metabolism → VDR pathway in its knowledge graph.

The critical mechanistic limitation, however, is that PTH is the primary driver of renal 1α-hydroxylase. In the PTH-deficient state, conversion of 25(OH)D3 to calcitriol is substantially impaired — meaning the inactive prohormone cholecalciferol cannot be efficiently activated. Standard management of FIH therefore prioritises **active vitamin D analogues** (calcitriol or alfacalcidol) that bypass this enzymatic bottleneck, combined with oral calcium supplementation. Cholecalciferol plays only a supportive role in correcting co-morbid vitamin D insufficiency, and no direct clinical evidence validates its use as a primary agent for FIH.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for familial isolated hypoparathyroidism due to impaired PTH secretion with cholecalciferol.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## US Market Information

No prescription NDA records were identified in the US FDA database for cholecalciferol. In the United States, cholecalciferol (Vitamin D3) is predominantly available as an over-the-counter (OTC) dietary supplement; OTC products are not captured in the prescription NDA database queried for this report. Prescription-strength cholecalciferol formulations (e.g., high-dose weekly capsules) do exist in clinical practice under various product registrations not reflected in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no direct clinical or preclinical evidence supporting cholecalciferol as a primary treatment for familial isolated hypoparathyroidism due to impaired PTH secretion. The fundamental mechanistic barrier — PTH-dependent 1α-hydroxylase activity being absent or severely reduced in this condition — means cholecalciferol cannot be efficiently activated to its therapeutic form (calcitriol) without enzyme bypass, making this a low-priority repurposing candidate compared to active vitamin D analogues already used as standard of care.

**To proceed, the following is needed:**
- Complete DrugBank API query to retrieve full mechanism of action data (remediation for data gap DG002)
- FDA/TFDA package insert review to obtain key warnings and contraindications (remediation for data gap DG001)
- Preclinical data (animal models of PTH deficiency) demonstrating whether cholecalciferol supplementation provides additive benefit beyond calcitriol alone
- Clinical case series or pilot studies comparing outcomes of cholecalciferol vs. calcitriol supplementation specifically in PTH-deficient patients
- Regulatory pathway assessment: whether re-labelling an OTC supplement for a rare genetic disease (FIH) would require a full NDA submission or a different designation (e.g., Orphan Drug)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

