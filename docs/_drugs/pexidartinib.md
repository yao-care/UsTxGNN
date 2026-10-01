---
layout: default
title: Pexidartinib
parent: Model Prediction Only (L5)
nav_order: 1035
evidence_level: L5
indication_count: 10
---

# Pexidartinib
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

# Pexidartinib: From Tenosynovial Giant Cell Tumor to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Pexidartinib (Turalio) is an oral CSF1R/KIT/FLT3 kinase inhibitor. The supplied data list no approved-indication text, but the retrieved literature describes its FDA approval for symptomatic tenosynovial giant cell tumor (TGCT).
The TxGNN model predicts it may be effective for **HER2-positive breast carcinoma**, but only **1 indirect clinical trial** and **0 publications** support this, so it remains a prediction to be validated.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license data. Literature describes symptomatic tenosynovial giant cell tumor (TGCT) not amenable to surgery |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (effectively prediction-only; the one linked trial is indirect) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The mechanism of action field is empty in the Evidence Pack. Literature in the pack describes pexidartinib as a small-molecule inhibitor of CSF1R, KIT and FLT3-ITD. Blocking CSF1R can reduce the macrophages that support tumors, which is why it works in TGCT, a tumor driven by CSF1 overexpression.

The link to breast cancer is indirect. Tumor-associated macrophages are present in breast tumors, so CSF1R blockade could plausibly affect the tumor microenvironment. However, the pack contains no HER2-specific mechanism or data, and the high TxGNN score is a graph-based prediction only.

The pack's better-supported breast cancer signal is for the PR-negative (triple-negative-like) subset. There, a completed Phase 1/2 study combined pexidartinib (PLX3397) with eribulin. Efficacy results were not provided.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01042379](https://clinicaltrials.gov/study/NCT01042379) | Phase 2 | Recruiting | 5000 | I-SPY 2 adaptive platform trial across many breast cancer agents. A pexidartinib arm or HER2-specific result is not confirmed in the supplied data (relevance grade C) |
| [NCT01596751](https://clinicaltrials.gov/study/NCT01596751) | Phase 1/2 | Completed | 67 | PLX3397 plus eribulin in metastatic breast cancer, targeting macrophages in triple-negative/basal-like disease. It was listed under the PR-negative prediction, not HER2, and efficacy outcomes were not provided (relevance grade A for that subtype) |

## Literature Evidence

Currently no related literature available for HER2-positive breast carcinoma.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211810 | Turalio (Daiichi Sankyo Inc.) | Capsule (oral) | Not provided in the source data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CSF1R/KIT/FLT3 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function tests (hepatotoxicity is the key risk noted in the pack) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Key Warnings**: Hepatotoxicity boxed warning, with a restricted-access risk program (from the pack's repurposing rationale). Use is label-restricted to symptomatic TGCT not amenable to surgery.

Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HER2-positive breast carcinoma prediction rests on a high model score, one large platform trial with no confirmed pexidartinib arm, and no literature. The pack's best-supported use is TGCT (Phase 3 ENLIVEN, PMID 31229240, long-term follow-up and a Phase 4 study), which is already approved and is not a new repurposing. In breast cancer, only the PR-negative/triple-negative-like subset has a direct early-phase signal, and its efficacy outcomes have not been reviewed.

**To proceed, the following is needed:**
- Confirm whether I-SPY 2 (NCT01042379) included a pexidartinib arm, and obtain any HER2-specific results
- Obtain and review the efficacy outcomes of NCT01596751 (PLX3397 plus eribulin)
- Preclinical or mechanistic evidence for CSF1R inhibition in HER2-positive disease
- The FDA package insert warnings and contraindications (a blocking data gap), followed by a liver-safety monitoring plan
- Mechanism of action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

