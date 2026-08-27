---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 933
evidence_level: L5
indication_count: 3
---

# Mirtazapine
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

# Mirtazapine: From Major Depressive Disorder to Ohdo Syndrome and Variants

## One-Sentence Summary

> Mirtazapine is a NaSSA-class antidepressant; this evidence pack does not contain confirmed original-indication or MOA data, but it is generally known as a treatment for Major Depressive Disorder.
> The TxGNN model predicts it may be relevant to **Ohdo Syndrome and Variants**, a rare congenital genetic disorder,
> but **no clinical trials and no literature** currently support this direction — the association appears to be a knowledge-graph artifact rather than a pharmacologically grounded hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in supplied regulatory data (generally known as Major Depressive Disorder) |
| Predicted New Indication | Ohdo Syndrome and Variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Mirtazapine is generally known as a NaSSA (noradrenergic and specific serotonergic antidepressant), acting via α2-adrenergic receptor antagonism and 5-HT2A/2C/3 and H1 receptor blockade.

Ohdo syndrome and its variant (blepharophimosis–intellectual disability syndrome, Ohdo type) are congenital developmental disorders caused by mutations in genes such as *KAT6B* and *MED12*, presenting with intellectual disability and structural anomalies. These are not receptor-signaling disorders, and there is no established pharmacological pathway by which an antidepressant acting on monoamine receptors would alter the underlying genetic pathology.

The rationale accompanying this prediction explicitly flags it as a likely **false positive**: the association probably arises from proximity in the knowledge graph (e.g., shared "intellectual disability" comorbidity nodes) rather than genuine mechanistic relevance. The two lower-ranked candidates (blepharophimosis–intellectual disability syndrome, Ohdo type; benign paroxysmal torticollis of infancy) show the same pattern — high TxGNN scores with no supporting trials, literature, or plausible mechanism, and in the case of infant torticollis, a serious safety concern given antidepressant use in infants is essentially unstudied.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No NDA or marketing authorization records were found for mirtazapine in this evidence pack; per the supplied regulatory data, the drug is currently not marketed (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety-stage (S1) evaluation can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on an L5 (model-prediction-only) score, with no clinical trials, no literature, and a mechanistic rationale that itself identifies the association as a probable false positive driven by knowledge-graph proximity rather than actual pharmacology. Combined with the unresolved Blocking safety data gap, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any safety screening
- Confirmed mechanism of action data from DrugBank (DG002, High)
- Independent pharmacological or preclinical rationale connecting mirtazapine's receptor activity to Ohdo syndrome pathophysiology, if any exists
- Re-evaluation of whether this TxGNN association reflects a genuine signal or a graph-topology artifact before committing further review resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

