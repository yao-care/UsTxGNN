---
layout: default
title: Droperidol
parent: 僅模型預測 (L5)
nav_order: 630
evidence_level: L5
indication_count: 10
---

# Droperidol
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

# Droperidol: From Unrecorded Original Indication to Tourette Syndrome

## One-Sentence Summary

Droperidol's original approved indication is not recorded in this evidence pack (the drug is currently not marketed, with zero active licenses on file). The TxGNN model predicts it may be effective for **Tourette Syndrome**, but this direction is currently supported by only **0 clinical trials** and **1 publication** — and that single publication studies haloperidol, not droperidol directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license records in evidence pack (drug not marketed) |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Research Question (early-stage screening, decision stage S1) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for droperidol is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the repurposing rationale supplied alongside the prediction, droperidol is a butyrophenone-class D2 dopamine receptor antagonist — the same pharmacological class as haloperidol, which is a traditional treatment option for Tourette syndrome. D2 antagonism theoretically suppresses tics, which is the mechanistic basis offered for this prediction (a class-effect argument rather than direct evidence).

The one supporting publication in this evidence pack (PMID 791589, 1976) studies haloperidol, not droperidol, so it provides only indirect, low-tier support (tier 3, case series). No droperidol-specific clinical trial or literature evidence for Tourette syndrome currently exists in this pack. In addition, droperidol carries a known QT-prolongation risk that must be resolved in an initial safety assessment (S1) before this direction can advance — this is why the internal recommendation is "Research Question" rather than a more advanced stage.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [791589](https://pubmed.ncbi.nlm.nih.gov/791589/) | 1976 | Case series (haloperidol, indirect) | Current psychiatric therapies | Discusses haloperidol (same drug class, not droperidol) in severe behavior disorders; no abstract available and relevance to droperidol/Tourette syndrome is not yet confirmed |

## US Market Information

No approved licenses on file — droperidol is currently not marketed (0 total licenses recorded).

## Safety Considerations

Formal safety labeling data (key warnings, contraindications, drug interactions) is not available for droperidol in this evidence pack — the TFDA warning/contraindication label lookup is an unresolved Blocking data gap (DG001) that must be closed before any formal safety review.

Separately, the repurposing rationale for this and other candidate indications repeatedly flags droperidol's known **QT-prolongation / cardiac arrhythmia risk** as a class characteristic requiring ECG monitoring if this direction is pursued clinically.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature support is an indirect haloperidol study rather than droperidol-specific evidence, and the drug is unmarketed with no safety labeling on file — this is flagged internally as a "Research Question" at the earliest decision stage (S1), not yet ready for a Go/Guardrails decision.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert warnings/contraindications (Blocking data gap DG001)
- Confirmed mechanism-of-action documentation for droperidol specifically (High-severity data gap DG002)
- Droperidol-specific (not haloperidol) clinical or preclinical evidence in Tourette syndrome
- QT-interval/cardiac safety assessment before any clinical exploration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

