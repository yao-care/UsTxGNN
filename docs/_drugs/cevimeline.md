---
layout: default
title: Cevimeline
parent: 僅模型預測 (L5)
nav_order: 517
evidence_level: L5
indication_count: 4
---

# Cevimeline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using `txgnn-pipeline` skill — confirmed applicable to TxGNN Evidence Pack report generation.

Now generating the evaluation report based on the Evidence Pack for Cevimeline (DB00185):

---

# Cevimeline: From Dry Mouth (Sjögren's Syndrome) to Hypertrichosis

## One-Sentence Summary

Cevimeline is a muscarinic M1/M3 receptor agonist primarily used to relieve dry mouth (xerostomia) in patients with Sjögren's syndrome, stimulating salivary and lacrimal gland secretion.
The TxGNN model predicts it may be effective for **Hypertrichosis** (abnormal excessive hair growth),
with **0 clinical trials** and **0 publications** currently supporting this direction — placing this at the lowest evidence level (**L5**).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan registration; known approved use: dry mouth in Sjögren's syndrome |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 (Model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registered Products | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on the drug profile described in the repurposing rationale, Cevimeline is a muscarinic cholinergic agonist with selectivity for M1 and M3 receptor subtypes. It acts primarily on exocrine glands — particularly salivary and lacrimal glands — to stimulate fluid secretion, which is the basis of its use in Sjögren's syndrome-related xerostomia.

Hypertrichosis, the condition of abnormal and excessive hair growth across the body, is governed by the Wnt/β-catenin, FGF, and androgen signaling pathways within hair follicles. The biological overlap between these growth-regulatory cascades and muscarinic cholinergic signaling is extremely limited. While M3 receptors are expressed at trace levels in cutaneous keratinocytes, there is no established causal pathway from M3 agonism to systemic hair follicle over-activation or generalized hair overgrowth.

The TxGNN model's high prediction score (99.26%) most likely reflects indirect topological proximity within the knowledge graph — shared node neighborhoods or co-occurrence patterns — rather than a direct, biologically meaningful mechanism. This is a known limitation of graph neural network models when applied to rare phenotypes with sparse graph connectivity. Without any corroborating clinical or preclinical evidence, the prediction cannot be considered actionable at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Cevimeline (DrugBank ID: DB00185) has no registered products in Taiwan. No TFDA-approved licenses are on record.

> **Note:** Cevimeline is approved in the United States (brand name Evoxac®) for the treatment of dry mouth symptoms in Sjögren's syndrome patients. Taiwan regulatory status remains "not marketed."

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (TFDA package insert warnings, contraindications, drug interactions) were not available at the time of this report. Retrieval from the TFDA official website is recommended before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on the TxGNN model score (L5 evidence) — there are no registered clinical trials, no relevant publications, and no biologically plausible mechanistic pathway linking M1/M3 muscarinic agonism to the pathogenesis of hypertrichosis. Advancing this candidate would not be scientifically justified at this stage.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full mechanism of action from DrugBank (DB00185) to confirm receptor selectivity and downstream signaling
- **Safety data**: Download TFDA package insert PDF to extract warnings, contraindications, and drug interaction profiles
- **Preclinical evidence**: Identify whether any in vitro or animal studies have examined M1/M3 agonists in hair follicle biology or skin biology
- **Graph topology review**: Assess whether the TxGNN score reflects a true biological signal or is an artifact of knowledge graph architecture (e.g., shared disease neighbors unrelated to mechanism)
- **Broader indication review**: Rank 3 prediction (**malformation syndrome with odontal/periodontal component**) shows a more biologically coherent indirect pathway — cevimeline → increased salivary secretion → oral microbiome protection → reduced periodontal pathogen burden — and carries 20 background literature references (L4). This indication warrants a separate, dedicated evaluation as a higher-priority repurposing candidate compared to hypertrichosis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

