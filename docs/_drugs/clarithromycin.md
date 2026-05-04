---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 450
evidence_level: L5
indication_count: 5
---

# Clarithromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using `txgnn-pipeline` to confirm this is a TxGNN drug repurposing report generation task — the skill confirms standard workflow and no additional overrides apply. Proceeding to generate the report per the v5 prompt format.

---

# Clarithromycin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic with established antibacterial and immunomodulatory properties, widely used for respiratory tract infections and *Helicobacter pylori* eradication.
The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (no regulatory records available in current data) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Clarithromycin is a macrolide antibiotic (same class as Azithromycin and Erythromycin) that works through two complementary pathways: (1) antibacterial action via inhibition of bacterial protein synthesis at the 50S ribosomal subunit, and (2) immunomodulatory effects including NF-κB pathway inhibition and downregulation of pro-inflammatory cytokines such as IL-6 and TNF-α.

Polyclonal hyperviscosity syndrome arises from excessive production of polyclonal immunoglobulins (IgM/IgG/IgA), elevating plasma viscosity to levels that impair microcirculation — commonly seen as a complication of Waldenström's macroglobulinemia, multiple myeloma, or chronic inflammatory conditions. The TxGNN model likely captured Clarithromycin's immunomodulatory properties as a theoretical basis for suppressing the B-cell overactivation that drives hyperglobulinemia.

However, this mechanistic link is highly indirect. The established standard of care for hyperviscosity syndrome is plasmapheresis for acute management, combined with disease-targeted therapy (e.g., rituximab-based regimens, proteasome inhibitors) addressing the underlying plasma cell or lymphoplasmacytic disorder. No clinical evidence supports Clarithromycin in this indication. This prediction is best understood as a hypothesis-generating signal rather than an actionable repurposing candidate.

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
This is a model-only prediction (Evidence Level L5) with zero clinical trials and zero literature support. The proposed mechanistic link between Clarithromycin's immunomodulatory properties and polyclonal hyperviscosity syndrome is theoretically weak and conflicts with established treatment paradigms that rely on plasma exchange and B-cell–targeted biologics.

**To proceed, the following is needed:**
- Retrieve detailed MOA data from DrugBank (DrugBank ID: DB01211)
- Obtain US FDA NDA regulatory records and Clarithromycin package insert warnings and contraindications
- Identify any preclinical evidence (in vitro / animal) showing Clarithromycin effects on immunoglobulin overproduction or plasma viscosity
- Clarify whether Clarithromycin's known IL-6 suppression is quantitatively sufficient to affect hyperviscosity endpoints
- Assess DDI profile, particularly with CYP3A4-metabolized disease-targeted agents commonly co-used in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

