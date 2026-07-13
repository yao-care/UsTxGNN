---
layout: default
title: Ergocalciferol
parent: 僅模型預測 (L5)
nav_order: 608
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
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

The TxGNN pipeline skill covers infrastructure work. The current task is report generation, which is fully governed by the system prompt (Drug Repurposing Evaluation Report Prompt v5). Proceeding to generate the report now.

---

# Ergocalciferol: From Vitamin D Deficiency to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

## One-Sentence Summary

Ergocalciferol (Vitamin D₂, DB00153) is a plant-derived fat-soluble prohormone traditionally used to correct vitamin D deficiency, treat nutritional rickets, and support calcium-phosphate homeostasis by activating the Vitamin D Receptor (VDR) pathway to enhance intestinal calcium absorption.
The TxGNN model predicts it may benefit patients with **Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion**, a rare inherited condition in which inadequate PTH release causes persistent hypocalcemia — a downstream deficit that ergocalciferol's VDR-mediated calcium uptake could partially compensate for.
However, **no dedicated clinical trials** and **no targeted publications** currently support this specific indication, placing the evidence squarely at **L4** (mechanistic rationale only), and making this a hypothesis for future investigation rather than a near-term clinical program.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No US NDA found in current dataset; general established use for vitamin D deficiency and nutritional rickets |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 — mechanistic rationale only; no dedicated clinical studies |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ergocalciferol is a plant-derived precursor to the active hormone 1,25-dihydroxyvitamin D₂ (calcitriol). After oral absorption, it undergoes sequential hydroxylation — first in the liver (CYP2R1/CYP27A1 → 25-hydroxyvitamin D₂) and then in the kidney (CYP27B1 → 1,25-dihydroxyvitamin D₂). This active metabolite binds the Vitamin D Receptor (VDR), a nuclear receptor that upregulates intestinal calcium transport proteins, notably TRPV6 (apical calcium channel) and S100G/calbindin-D9k (intracellular calcium chaperone), markedly increasing calcium absorption from the gut. Detailed pharmacological MOA data from DrugBank is not yet available for this report and should be retrieved to complete the mechanistic picture.

In familial isolated hypoparathyroidism due to impaired PTH secretion, the fundamental defect is insufficient PTH release — typically caused by mutations in genes such as *GCM2*, *PTH*, or *SOX3* — resulting in chronic hypocalcemia and hyperphosphatemia. Because PTH normally stimulates renal 1α-hydroxylase (CYP27B1) to produce active calcitriol, its absence also reduces endogenous vitamin D activation. Ergocalciferol can partially bypass this problem: by providing a large circulating reservoir of 25-hydroxyvitamin D₂, it can drive non-PTH-dependent (or extrarenal) pathways toward adequate 1,25(OH)₂D₂ production, thereby restoring intestinal calcium absorption and correcting hypocalcemia through a symptomatic, downstream route.

The mechanistic logic is coherent and biologically grounded — ergocalciferol compensates for the calcium deficit created when PTH fails, without addressing the PTH secretion defect itself. It is worth noting, however, that active vitamin D analogues (calcitriol, alfacalcidol) are the current clinical standard for managing hypoparathyroidism precisely because they bypass the impaired 1α-hydroxylation step entirely. The TxGNN model likely captures this pharmacological overlap correctly, but the question of whether ergocalciferol specifically adds value over established active analogues remains unanswered by any existing study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ergocalciferol in familial isolated hypoparathyroidism due to impaired PTH secretion.

---

## Literature Evidence

Currently no related literature available directly addressing ergocalciferol in familial isolated hypoparathyroidism due to impaired PTH secretion.

---

## US Market Information

No US FDA approvals (NDAs) for ergocalciferol are recorded in the current dataset.

| Item | Detail |
|------|--------|
| US Market Status | Not Marketed |
| Total NDAs | 0 |
| Note | Ergocalciferol is widely available as an OTC dietary supplement (Vitamin D₂) in the US, but no prescription NDA data was retrieved in this evidence pack. Regulatory records should be verified directly via the FDA Orange Book and DailyMed. |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug-drug interaction data were not retrieved in this evidence pack (both categorized as data gaps). Before any clinical use or research protocol design, the product labeling — including hypercalcemia risk, hypervitaminosis D toxicity thresholds, and interactions with thiazide diuretics, cardiac glycosides, and cholestyramine — must be reviewed. This is classified as a **Blocking** data gap for formal safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The VDR-mediated mechanism of ergocalciferol is plausible for compensating downstream hypocalcemia in PTH-deficient states, but there are zero disease-specific clinical trials or publications for this rare indication. Furthermore, the very enzyme required to activate ergocalciferol (renal CYP27B1/1α-hydroxylase) is normally stimulated by PTH — meaning ergocalciferol's conversion to its active form may itself be impaired in this disease context, raising a fundamental pharmacokinetic concern that active analogues (calcitriol, alfacalcidol) do not share.

**To proceed, the following is needed:**

- **Safety data retrieval (Blocking):** Download and parse the product labeling to obtain key warnings, contraindications, and drug interaction data before any evaluation can advance beyond S1
- **Mechanism of action documentation:** Query DrugBank API (DB00153) to retrieve full MOA, pharmacokinetics, and toxicity data
- **Preclinical studies:** Animal or in vitro experiments specifically examining ergocalciferol efficacy in PTH-deficient (e.g., parathyroidectomized) models, with measurement of 1α-hydroxylation capacity
- **Pharmacokinetic rationale:** Clarify whether residual renal 1α-hydroxylase activity or extrarenal CYP27B1 expression (e.g., macrophages, skin) is sufficient to activate ergocalciferol in patients with severe PTH deficiency
- **Comparative framework:** Establish whether ergocalciferol offers any clinical advantage over calcitriol/alfacalcidol in this setting — if not, repurposing effort should redirect to the active analogues
- **Orphan disease designation check:** Assess eligibility for rare disease research incentives (FDA Orphan Drug designation) given the ultra-rare nature of familial isolated hypoparathyroidism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

