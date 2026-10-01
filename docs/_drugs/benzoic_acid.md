---
layout: default
title: Benzoic Acid
parent: Model Prediction Only (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Benzoic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Benzoic Acid: From Unspecified Original Use to Bronchitis

## One-Sentence Summary

Benzoic acid is marketed in the US, but the available data lists no approved indication for it, so its original therapeutic use cannot be stated.
The TxGNN model predicts it may be effective for **bronchitis**, but there are **0 clinical trials** and only **2 publications**, and neither publication studies benzoic acid.
This is a model-only prediction (evidence level L5), so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the US license data) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for benzoic acid, and no approved original indication is recorded. The mechanistic link between benzoic acid and bronchitis therefore cannot be established from the current data.

The two publications retrieved for bronchitis do not support the prediction:

- One is a review of repaglinide in type 2 diabetes. Repaglinide is a benzoic acid derivative, but the paper concerns diabetes.
- The other is a preclinical study of a soluble epoxide hydrolase inhibitor in smoke-induced COPD. It does not involve benzoic acid.

The 99.98% score is a knowledge-graph model output and does not by itself indicate clinical plausibility. It should be treated as a hypothesis to test, not as evidence.

The other nine predictions (for example diabetic retinopathy, dry eye syndrome, fibromatosis and C1 inhibitor deficiency) are also weakly supported. Most have no trials or literature. Diabetic retinopathy has only indirect preclinical evidence on synthetic retinoids containing a benzoic acid moiety, which is a structural-class association and not evidence for benzoic acid itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Preclinical | Am J Respir Cell Mol Biol | Soluble epoxide hydrolase inhibitor in smoke-induced COPD (a condition that includes bronchitis). Does not study benzoic acid. |
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Review | Drugs | Review of repaglinide, a benzoic acid derivative, in type 2 diabetes. Not related to bronchitis or to benzoic acid itself. |

---

## US Market Information

The 14 licenses in the data all list no approved indication text. The five shown here are pellet products from Hahnemann Laboratories, OHM Pharma and Boiron. A liquid form is also recorded.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Acidum Benzoicum (Hahnemann Laboratories, Inc.) | Pellet | Not listed |
| Not listed | Benzoicum Acidum (OHM Pharma Inc.) | Pellet | Not listed |
| Not listed | Acidum Benzoicum (Hahnemann Laboratories, Inc.) | Pellet | Not listed |
| Not listed | Benzoicum acidum (Boiron) | Pellet | Not listed |
| Not listed | Acidum Benzoicum (Hahnemann Laboratories, Inc.) | Pellet | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests only on the model score. There are no trials, and neither retrieved paper studies benzoic acid. The mechanism of action and original indication are missing, and the safety data cannot support a screening review.

**To proceed, the following is needed:**
- Mechanism of action data (query DrugBank) and the original approved indication
- Package insert warnings and contraindications (download and parse from the FDA website), which block S1 safety screening
- A targeted literature search on benzoic acid itself in respiratory or bronchial inflammation
- A check of whether the marketed products are for a use unrelated to a therapeutic indication, and whether their route and dosage form suit a respiratory indication
- Only if the above shows a plausible link, preclinical evidence before considering clinical study

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

