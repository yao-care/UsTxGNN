---
layout: default
title: Clobetasol Propionate
parent: 僅模型預測 (L5)
nav_order: 537
evidence_level: L5
indication_count: 7
---

# Clobetasol Propionate
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

The `txgnn-pipeline` skill confirms this is standard TxGNN pipeline work. Now I'll generate the report following the Drug Repurposing Evaluation Report Prompt (v5) instructions.

---

# Clobetasol Propionate: From Inflammatory Skin Disorders to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Clobetasol propionate is a super-potent (Class I/VII) topical corticosteroid widely used for severe inflammatory skin conditions such as psoriasis, lichen sclerosus, and chronic eczema.
The TxGNN model predicts it may be effective for **Vulvar Inverted Follicular Keratosis**,
but currently there are **no clinical trials** and **no publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory skin disorders (no Taiwan regulatory approval data on file) |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacological class information, clobetasol propionate is a glucocorticoid receptor (GR) agonist. By activating GR, it suppresses the transcription factors NF-κB and AP-1, downregulating pro-inflammatory cytokines (IL-1β, TNF-α, IL-6) and inhibiting T-cell and mast cell activation. These effects account for its well-established efficacy in a broad range of inflammation-driven skin diseases.

Vulvar inverted follicular keratosis (IFK), however, is a benign epithelial tumor — essentially a squamous proliferative lesion histologically characterized by squamous eddies and endophytic growth. Its pathogenesis involves abnormal follicular epithelial differentiation rather than a sustained inflammatory cascade. There is no established mechanistic rationale for why glucocorticoid-mediated anti-inflammation would modify the course of this tumor.

The TxGNN model's high prediction score (99.46%) most likely arises from broad node proximity between "vulvar skin disease" entities within the knowledge graph, rather than a genuine mechanistic connection between clobetasol and IFK. This is considered a probable false positive from the model, and no clinical or preclinical evidence exists to substantiate this repurposing direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Vulvar inverted follicular keratosis is a benign, non-inflammatory epithelial tumor whose pathogenesis (abnormal follicular epithelial differentiation) has no biologically plausible connection to clobetasol's anti-inflammatory glucocorticoid mechanism. With zero supporting clinical trials or literature, and a TxGNN score that likely reflects knowledge graph structural artifact rather than true mechanistic overlap, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Obtain detailed MOA data from DrugBank API (DG002 remediation) to formally characterize the mechanistic gap
- Download Taiwan FDA package insert PDF to assess warnings and contraindications (DG001 remediation — currently Blocking)
- Conduct a literature review on IFK pathobiology to determine whether any glucocorticoid-responsive pathway (e.g., keratinocyte differentiation via GR) is plausibly involved
- Evaluate preclinical in vitro data (e.g., effect of clobetasol on squamous epithelial cell lines) before any further clinical consideration

---

> **Note on higher-ranked evidence within this Evidence Pack:** While the top TxGNN prediction (Rank 1) warrants a Hold, Rank 3 — **Exanthem (disease)** — carries an **L1 evidence level** with multiple completed Phase 3/4 RCTs directly testing clobetasol (e.g., [NCT05010421](https://clinicaltrials.gov/study/NCT05010421), [NCT01323673](https://clinicaltrials.gov/study/NCT01323673)) and a **"Proceed with Guardrails"** recommendation. A separate targeted report on the Exanthem/Lichen Sclerosus/Lichen Planus indication cluster is strongly recommended as the primary repurposing opportunity for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

