---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 886
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From Osmotic Diuresis to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is a sugar-alcohol osmotic diuretic long used to reduce intracranial/intraocular pressure and promote diuresis; specific TFDA-approved indication text is not present in this evidence pack. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but currently **no clinical trials** and only **1 tangential publication** support this direction — the evidence is essentially model-prediction-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (drug class: osmotic diuretic; regulatory indication text unavailable) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacological information, mannitol is a sugar alcohol classified as an osmotic diuretic; it raises plasma osmolality, draws free water out of tissues, and promotes renal excretion of water and solutes. This basic mechanism is well established, though this evidence pack does not contain the drug's specific TFDA-approved indication text.

NSIAD is a rare, congenital cause of euvolemic hyponatremia driven by a gain-of-function mutation in the vasopressin V2 receptor, which causes inappropriate renal water retention even in the absence of detectable antidiuretic hormone. Mechanistically, an osmotic diuretic that promotes free-water excretion is a plausible countermeasure to the water-retention physiology underlying NSIAD, which is likely why the TxGNN model links the two.

However, this mechanistic plausibility is not yet backed by direct empirical study. The single literature item returned for this pair discusses general pitfalls in evaluating hyponatremic patients rather than mannitol's therapeutic effect in NSIAD specifically, and no clinical trials have been registered for this drug-disease pair. The prediction should be read as a hypothesis generated from network-level associations, not as clinically validated evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European journal of internal medicine | Reviews common diagnostic pitfalls in hyponatremia work-up; discusses risks of under- and over-treatment. Does not evaluate mannitol therapy for NSIAD directly. |

## US Market Information

No marketing authorizations on record in this evidence pack (0 licenses; market status: 未上市/Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are zero clinical trials and only one tangential, non-specific publication supporting mannitol's use in NSIAD — this is model-prediction-only evidence (L5). Separately, TFDA label/warning data (DG001) is flagged as a **Blocking** gap, which prevents even a preliminary safety (S1) assessment.

**To proceed, the following is needed:**
- TFDA package insert — warnings, contraindications (DG001, Blocking)
- Detailed mechanism of action data (DG002)
- Mannitol's confirmed original/approved indications and regulatory history
- Targeted clinical evidence (trials, case series, or mechanistic studies) evaluating mannitol specifically in NSIAD or related hyponatremia syndromes
- Drug-drug interaction (DDI) screening data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

