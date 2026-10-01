---
layout: default
title: Selpercatinib
parent: Model Prediction Only (L5)
nav_order: 1153
evidence_level: L5
indication_count: 3
---

# Selpercatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Selpercatinib: From RET-Driven Cancers to Pulmonary Hypertension

## One-Sentence Summary

Selpercatinib is a selective RET kinase inhibitor marketed in the US as RETEVMO. The published literature describes its use in RET fusion-positive non-small cell lung cancer.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **0 clinical trials** and **no publications that address this indication**, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license records (the literature describes RET fusion-positive NSCLC) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 license records (2 distinct NDA numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Selpercatinib is a selective RET kinase inhibitor, and its efficacy in RET-driven cancers has been reported in real-world studies. There is no established biological link between RET inhibition and pulmonary hypertension. Any connection through pulmonary vascular remodeling, or through off-target kinase activity, is speculative.

The high score (99.18%) cannot be traced to a specific rationale in the available data, so it should be read as a computational signal only.

There is also a safety concern. Hypertension is a recognized adverse effect of RET inhibitors, and this should be evaluated before any efficacy question in a pulmonary vascular population.

Two other predictions for this drug are also L5 with no trials or literature:
- Migraine disorder (99.17%). RET is expressed in some sensory and trigeminal neurons, but a link to migraine is hypothetical.
- Migraine with brainstem aura (99.05%). This is likely correlated with the migraine prediction and adds no independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Neither publication addresses pulmonary hypertension. Both are listed as background on the drug, and their relevance to the predicted indication is still pending review.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Cohort (real-world, FAERS) | Front Pharmacol | Compares adverse event profiles of pralsetinib and selpercatinib using FDA adverse event reports |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Cohort (retrospective) | Ther Adv Med Oncol | SIREN: real-world analysis of selpercatinib in RET fusion-positive NSCLC patients treated through an access program |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA218160 | RETEVMO (Eli Lilly and Company) | Coated tablet | Not stated in the source record |
| NDA213246 | RETEVMO (Eli Lilly and Company) | Capsule | Not stated in the source record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood pressure (hypertension is a recognized RET inhibitor effect); other parameters per the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Key Concern**: Hypertension is a recognized adverse effect of RET inhibitors. This is directly relevant to a pulmonary vascular population.

Please refer to the package insert for other warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5): there are no trials, no supporting literature, and no traceable mechanism. A known hypertensive effect of the drug class raises a safety question for pulmonary hypertension.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data, to test whether any RET-related pathway plausibly connects to pulmonary vascular disease
- Cardiovascular and blood pressure safety review in the context of pulmonary hypertension
- Preclinical evidence in pulmonary hypertension models, before any clinical consideration
- Manual relevance review of the retrieved literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

