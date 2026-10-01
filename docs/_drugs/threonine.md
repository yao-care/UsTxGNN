---
layout: default
title: Threonine
parent: Model Prediction Only (L5)
nav_order: 1224
evidence_level: L5
indication_count: 1
---

# Threonine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Threonine: Predicted New Indication of Gastroparesis (No Established Original Indication on Record)

## One-Sentence Summary

Threonine (DrugBank DB00156) is an amino acid. The record lists one marketed US product, L-Threonine High (liquid), but no approved indication. The TxGNN model predicts it may be relevant to **Gastroparesis**, but there are **0 clinical trials** and **1 publication**. That publication is a rat study that does not mention threonine, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (license number not listed in the record) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is recorded for this drug. The score is high (99.32%), but it comes from knowledge-graph link prediction only. The graph provides no explicit drug-to-disease pathway.

One speculative link exists. Amino acids such as threonine can influence mTOR signaling. The single retrieved paper (PMID 28627597) reports changes in gastric smooth muscle cell apoptosis and in PI3K-AKT-mTOR and AMPK-mTOR signaling in a diabetic gastroparesis rat model. This is a pathway overlap only. The paper's title does not mention threonine, and it is unknown whether any effect would be beneficial or harmful.

Until direct evidence appears, this prediction should be treated as a hypothesis to test rather than a supported candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28627597](https://pubmed.ncbi.nlm.nih.gov/28627597/) | 2017 | Preclinical study (rat model) | Molecular Medicine Reports | Examined gastric smooth muscle cell apoptosis and PI3K-AKT-mTOR and AMPK-mTOR signaling changes in diabetic gastroparesis rats. Threonine is not mentioned, so this is indirect pathway context only. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | L-Threonine High (Professional Complementary Health Formulas) | Liquid | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. The package insert warnings and contraindications have not yet been obtained, and no drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence is model-only (L5). There are no clinical trials, and the one publication is a preclinical study that does not involve threonine. Safety data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, needed for safety screening
- Original indication and mechanism of action data (e.g., via DrugBank)
- Literature that directly studies threonine in gastroparesis or gastric motility
- Route and formulation compatibility assessment for the predicted indication
- Confirmation of the actual license or NDA number and regulatory status of the listed product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

