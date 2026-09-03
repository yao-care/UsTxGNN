---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 1116
evidence_level: L5
indication_count: 6
---

# Remdesivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Remdesivir: From COVID-19 to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Remdesivir is a nucleotide prodrug antiviral originally developed and used for COVID-19 (and related viral infections such as Ebola).
> The TxGNN model's top prediction is **Multiple Endocrine Neoplasia (MEN)**, with a raw prediction score of 99.50%,
> but **zero clinical trials and zero publications** currently support this specific link — the prediction rationale itself flags this as likely knowledge-graph noise rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COVID-19 (not recorded in local regulatory licenses — drug is not currently marketed in this jurisdiction; based on public/clinical trial record) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, remdesivir is an adenosine nucleotide prodrug that inhibits the viral RNA-dependent RNA polymerase (RdRp), and its efficacy against SARS-CoV-2 (and Ebola virus) has been established through multiple completed Phase 3 trials.

For the top-ranked prediction, **Multiple Endocrine Neoplasia (MEN)**, no biologically plausible mechanistic link exists. MEN is a hereditary endocrine tumour syndrome driven by *RET* or *MEN1* gene mutations — an oncogenic/genetic pathway entirely unrelated to viral RdRp inhibition. The evidence pack itself explicitly characterizes this as a likely **false-positive signal from the TxGNN knowledge graph**, with no clinical trials or literature identified to support the association.

It is worth noting that a lower-ranked prediction (HIV infectious disease, rank 2) did return 10+ clinical trials and 20 publications, but closer inspection shows nearly all of this evidence actually concerns remdesivir's use in **COVID-19**, not HIV — the model appears to have confused disease categories under a shared "infectious disease" label. This reinforces that, for this candidate, the top-ranked prediction should be treated with caution rather than acted upon.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Remdesivir currently holds no marketing authorization records in this jurisdiction (`total_licenses = 0`, market status: Not Marketed). No license table is available to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Multiple Endocrine Neoplasia) has an evidence level of L5 — a model score with no corroborating clinical trials, literature, or plausible mechanism of action. The next-ranked signal (HIV) initially appears stronger (L2) but on inspection reflects a data/label mismatch with COVID-19 evidence rather than genuine HIV-specific support. No indication in this candidate set currently meets a bar sufficient to proceed.

**To proceed, the following is needed:**
- Confirm and document remdesivir's mechanism of action (MOA) from DrugBank or primary literature
- Obtain TFDA/US labeling data (warnings, contraindications) to clear the blocking safety data gap (DG001)
- Re-validate the HIV-labeled evidence set to separate true HIV-specific studies from COVID-19-related trials/literature that were miscategorized
- If pursuing MEN or SIV/FIV signals further, commission a targeted literature/mechanism review before any trial design work, as no supporting evidence currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

