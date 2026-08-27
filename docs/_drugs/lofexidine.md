---
layout: default
title: Lofexidine
parent: 僅模型預測 (L5)
nav_order: 866
evidence_level: L5
indication_count: 2
---

# Lofexidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Lofexidine: From Opioid Withdrawal Management to Migraine Disorder

## One-Sentence Summary

Lofexidine hydrochloride is a selective α2-adrenergic receptor agonist; its original indication is not captured in this evidence pack (data gap — see DG001/DG002), though it is generally known as an opioid-withdrawal symptom management agent. The TxGNN model predicts a possible new application in **Migraine Disorder**, but this is currently supported by **0 clinical trials** and only **1 tangentially related publication** — evidence is essentially model-prediction-only at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (original_indications empty; original_moa flagged as data gap DG002) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lofexidine in this evidence pack (DG002). Based on known pharmacological classification, lofexidine is a selective α2-adrenergic receptor agonist, in the same class as clonidine.

The mechanistic rationale offered for the migraine prediction relies entirely on class analogy: clonidine has limited, largely superseded, off-label literature on migraine prophylaxis via sympathetic outflow reduction and vascular stabilization. There is **no direct evidence for lofexidine itself** in migraine — the link is inferred purely from shared receptor pharmacology with clonidine, not from any lofexidine-specific data.

For the secondary candidate, **migraine with brainstem aura**, the rationale is even weaker: this subtype involves distinct brainstem vascular/neural pathology where the direction of an α2-agonist's effect (symptom relief vs. aggravation) cannot be determined from any available data. No direct or indirect clinical evidence exists for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30580925](https://pubmed.ncbi.nlm.nih.gov/30580925/) | 2019 | Other (new-drug-approval roundup, not a clinical study) | Journal of the American Pharmacists Association (JAPhA) | A digest article summarizing several drugs approved around the same period (baloxavir marboxil, fremanezumab, galcanezumab, lofexidine hydrochloride). Lofexidine is co-listed because of its concurrent FDA approval timing — the article does not report any migraine-specific data or trial results for lofexidine. |

**Caution:** This is the only literature hit for lofexidine + migraine, and it is an administrative/announcement-type reference, not primary research. It should not be interpreted as supporting evidence for efficacy.

---

## US Market Information

Lofexidine is not currently marketed under the reviewed jurisdiction (market status: Not Marketed, 0 licenses on file). No authorization records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all currently unavailable — DG001 is flagged as a **Blocking** gap, meaning this candidate cannot yet pass initial safety screening (S1) without TFDA-equivalent label data.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 — no clinical trials and only one tangential, non-substantive literature mention support the migraine hypothesis, and the mechanistic link is based on drug-class analogy rather than lofexidine-specific data. In addition, a **Blocking** safety data gap (DG001) prevents this candidate from entering initial safety evaluation.

**To proceed, the following is needed:**
- TFDA (or equivalent) label warnings/contraindications (DG001 — Blocking)
- Confirmed mechanism of action from DrugBank (DG002)
- Original indication/labeling data, currently absent from this evidence pack
- Any preclinical or mechanistic studies specifically evaluating lofexidine (not just the clonidine class) in migraine
- Reassessment of the "migraine with brainstem aura" candidate once primary migraine evidence is established, given its distinct pathophysiology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

