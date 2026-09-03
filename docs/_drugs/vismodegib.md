---
layout: default
title: Vismodegib
parent: 僅模型預測 (L5)
nav_order: 1294
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: From Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

> Vismodegib is a Smoothened (SMO) antagonist originally developed and approved for locally advanced/metastatic basal cell carcinoma (BCC).
> The TxGNN model predicts it may also be effective for **Medulloblastoma with Extensive Nodularity (MBEN)**, a Sonic Hedgehog (SHH)-activated pediatric brain tumor subtype,
> though this evidence pack currently contains **0 clinical trials** and **0 publications** specifically indexed for this subtype — the case rests on strong mechanistic reasoning rather than direct trial evidence in this pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Basal cell carcinoma (locally advanced/metastatic) — inferred from supporting literature in this pack; not present in formal license records |
| Predicted New Indication | Medulloblastoma with Extensive Nodularity |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formally documented mechanism of action (`original_moa`) is not available in this evidence pack (data gap DG002). Based on the repurposing rationale collected alongside this pack, vismodegib is a Smoothened (SMO) antagonist that directly blocks the Hedgehog (SHH) signaling pathway — an established, well-characterized targeted mechanism rather than conventional cytotoxic chemotherapy.

Medulloblastoma with Extensive Nodularity (MBEN) is a histological subtype of medulloblastoma that is strongly enriched for SHH-pathway activation (frequently via PTCH1 or SMO mutations), particularly in infants and young children. This is not a speculative mechanistic leap: vismodegib has already received global regulatory approval (FDA/EMA) for recurrent or refractory SHH-activated medulloblastoma in adults and adolescents. The TxGNN prediction for MBEN therefore aligns with an on-mechanism, largely on-label extension rather than a novel repurposing hypothesis.

Supporting this mechanistic confidence, a separate prediction within this same evidence pack — basal cell carcinoma (ranked #9, "skin cancer") — is backed by an extensive, high-quality body of Phase 2 RCTs and guideline literature confirming that SMO blockade with vismodegib reliably drives clinical responses in Hedgehog-driven tumors. This corroborates the plausibility of the MBEN prediction even though MBEN-specific trials/publications were not captured in this particular evidence pull.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for this specific predicted indication, MBEN, in this evidence pack).

---

## Literature Evidence

Currently no related literature available (for this specific predicted indication, MBEN, in this evidence pack).

---

## US Market Information

Vismodegib currently has no license records on file (`total_licenses = 0`, `market_status = 未上市 / Not Marketed`) in this jurisdiction's regulatory dataset.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Hedgehog pathway (Smoothened) inhibitor; not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | No toxicity data available in this evidence pack; please refer to the package insert |
| Emetogenicity Classification | No toxicity data available in this evidence pack; please refer to the package insert |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack — including a **Blocking**-severity gap, DG001, for TFDA-equivalent label warnings/contraindications, which must be resolved before any S1 safety screening can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN score (99.93%) and mechanistic rationale for MBEN are strong — SHH-activated medulloblastoma is already a globally approved indication for vismodegib — but this specific evidence pack lacks any MBEN-specific trials or publications, the drug has no market/license presence on file, and safety label data has a **Blocking** gap. The mechanistic strength alone does not justify unguarded advancement.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse formal label warnings/contraindications before S1 safety evaluation
- Resolve DG002 (High): confirm mechanism of action via DrugBank API to formally document MOA
- Source MBEN- or SHH-medulloblastoma-specific clinical trial and literature evidence (e.g., cross-check ClinicalTrials.gov/PubMed with broader "medulloblastoma" search terms, since existing global approval implies trials exist but were not captured under this exact disease-name match)
- Clarify market/licensing status — confirm whether "Not Marketed / 0 licenses" reflects this jurisdiction only, given vismodegib's known FDA approval (as Erivedge) elsewhere
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

