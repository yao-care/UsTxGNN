---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 864
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From Hypertension/Post-MI Cardioprotection to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is a well-established ACE inhibitor (ACEi), historically used for hypertension and post-myocardial-infarction cardioprotection. The TxGNN model's top-ranked prediction for this drug is **posterolateral myocardial infarction**, an anatomically-specific ICD subtype of MI, but this evidence pack currently contains **zero clinical trials and zero publications** directly supporting this exact prediction — the score most likely reflects a known ACEi class effect combined with knowledge-graph disease-ontology granularity, rather than an independently verified new signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / post-MI cardioprotection (established ACEi class use; no TFDA license record exists in this pack to confirm approved label text — see Market Information below) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (mechanism-only; no direct trial or literature match) |
| Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for lisinopril in this evidence pack (data gap DG002, severity High). Based on the information available, lisinopril is an ACE inhibitor, and its use in reducing post-myocardial-infarction ventricular remodeling and mortality is an established pharmacological class effect, referenced in historical RCTs such as GISSI-3.

The predicted new indication, posterolateral myocardial infarction, is not a distinct disease mechanism but an anatomical subtype of MI within the ICD ontology. Mechanistically, lisinopril's known post-MI cardioprotective effect would plausibly extend to this subtype the same way it applies to MI generally. However, no clinical trial or publication in this evidence pack directly addresses this specific anatomical subtype — the same pattern repeats for the equally-ranked "posteroinferior" and "septal" MI subtypes (ranks 2 and 7). This strongly suggests the prediction is driven by the knowledge graph splitting "myocardial infarction" into many fine-grained anatomical entities rather than by a genuine, independently evidenced new indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Market Information

No license records are present in this dataset (0 licenses). The drug is recorded as "Not Marketed" in the underlying regulatory source used for this pack. This status is worth an independent data-quality check, since lisinopril is a long-established, widely marketed generic ACE inhibitor globally — the "Not Marketed" / 0-license result may reflect a gap in the source data pipeline rather than actual market absence.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or literature evidence directly supports posterolateral myocardial infarction as a distinct new indication for lisinopril; the signal is most plausibly an artifact of disease-ontology granularity layered on top of a known ACEi class effect. In addition, blocking data gap DG001 (TFDA label warnings/contraindications) means this candidate cannot yet clear the S1 safety screening stage.

**To proceed, the following is needed:**
- TFDA package insert / warnings & contraindications data (DG001, blocking)
- Drug mechanism-of-action detail from DrugBank (DG002)
- Verification of the "Not Marketed / 0 NDAs" market status, which is inconsistent with lisinopril's known global marketing history
- Consider reprioritizing evaluation toward **chronic pulmonary heart disease** (rank 9 in this pack): it reached evidence level L3 / stage S2 ("Research Question") with 5 clinical trials and 8 publications, including two studies directly testing lisinopril in chronic cor pulmonale/pulmonary hypertension (PMID 17047621, PMID 14524095) — a substantially stronger candidate than the top-ranked MI-subtype prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

