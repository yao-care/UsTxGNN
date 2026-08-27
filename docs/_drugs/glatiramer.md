---
layout: default
title: Glatiramer
parent: 僅模型預測 (L5)
nav_order: 752
evidence_level: L5
indication_count: 1
---

# Glatiramer
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Glatiramer: From Multiple Sclerosis to Hemoglobinopathy

## One-Sentence Summary

Glatiramer (acetate) is an immunomodulatory agent whose established use is in multiple sclerosis; no Taiwan-approved indication is on record for this drug. The TxGNN model predicts potential relevance to **hemoglobinopathy**, but this direction is currently supported by **0 clinical trials** and only **1 tangentially related publication**, and the drug's own mechanism data show no known biological link to hemoglobinopathy pathology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (per mechanistic rationale; no Taiwan license record available) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for glatiramer is not available in the structured record ([Data Gap]). Based on the repurposing rationale supplied with this evidence pack, glatiramer acetate is a multiple sclerosis treatment that works through immune modulation — inducing a Th2 shift in regulatory T cells and interfering with myelin antigen presentation.

There is **no known biological relationship** between this immune-modulatory mechanism and hemoglobinopathies (e.g., sickle cell disease, thalassemia), which are caused by genetic mutations affecting hemoglobin structure or synthesis. The evidence pack explicitly notes that the high TxGNN score (0.99) reflects knowledge-graph embedding similarity rather than mechanistic evidence, and cautions that a credible mechanistic hypothesis cannot be established given the missing MOA data.

In short, this prediction should be treated as a data-driven signal only, not a mechanistically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Case report/Review | Revue neurologique | Case report of a multiple sclerosis patient (with an incidental past history of beta thalassemia) who developed multiple immune disorders after natalizumab discontinuation. Beta thalassemia is mentioned only as patient history, not as a treatment outcome for glatiramer — this reference does not provide direct evidence for glatiramer's efficacy in hemoglobinopathy. |

---

## Taiwan Market Information

Glatiramer is currently not marketed in Taiwan (未上市), and no license records are available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

(Note: TFDA warning/contraindication data is flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety-stage evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is unsupported by clinical trials and has only one weakly related, non-mechanistic literature citation. No plausible biological link between glatiramer's known MS mechanism and hemoglobinopathy pathology has been established, and core MOA and safety data remain missing.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently blocking — DG001)
- Verified mechanism of action data from DrugBank (DG002)
- Dedicated preclinical or mechanistic studies linking glatiramer to hemoglobinopathy pathways, if this direction is to be pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

