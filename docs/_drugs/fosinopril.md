---
layout: default
title: Fosinopril
parent: 僅模型預測 (L5)
nav_order: 738
evidence_level: L5
indication_count: 5
---

# Fosinopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Fosinopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Fosinopril is an ACE inhibitor whose original approved indication is not formally recorded in this data pack (mechanism-of-action and original-indication fields are gaps), though it is pharmacologically known as an antihypertensive. TxGNN predicts it may be effective for **Malignant Hypertensive Renal Disease**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-score prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (drug not marketed in Taiwan; known pharmacologically as an ACE inhibitor / antihypertensive) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature identified) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for fosinopril is not available in this pack. Based on known drug-class information, fosinopril is an ACE inhibitor (ACEi); this class lowers systemic blood pressure and reduces intraglomerular pressure, which is the established rationale for renal protection in hypertensive kidney disease.

Malignant hypertension with renal involvement is mechanistically continuous with the standard hypertension indication ACEi drugs are known for — the predicted indication is an extension of an established drug-class effect rather than a novel mechanism. TxGNN's high score (99.87%) is directionally consistent with this known pharmacology, but the pack contains **no trial or literature evidence** specific to fosinopril in this indication, so the prediction remains a research hypothesis, not an evidence-backed finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications data is a Blocking-severity gap in this pack (DG001) — this must be resolved before any initial safety (S1) review can proceed.*

---

## Other Predicted Indications (Lower Priority, Not Detailed Above)

The pack includes four additional TxGNN predictions for fosinopril, all similarly unsupported by trial or literature evidence:

| Rank | Disease | Score | Note |
|------|---------|-------|------|
| 2 | Malignant renovascular hypertension | 99.87% | Same ACEi rationale as rank 1, but ACEi use carries a known acute renal-failure risk in (especially bilateral) renal artery stenosis — a safety concern, not just an efficacy question. |
| 3 | Pulmonary hypertension, unclear/multifactorial mechanism (WHO Group 5) | 99.87% | No established ACEi mechanism for this heterogeneous group; mechanistic link is weak. |
| 4 | Pulmonary hypertension due to lung disease/hypoxia (WHO Group 3) | 99.87% | 20 literature hits returned, but on review all are basic hypoxia/neurodegeneration/oncology studies unrelated to fosinopril or this indication — a keyword-matching false positive, not real evidence. |
| 5 | Braddock syndrome | 99.81% | A rare genetic disorder with no known link to ACE inhibition; likely a knowledge-graph embedding artifact rather than a real signal. |

None of these should be advanced without independent literature/trial searches, as the current searches for all five diseases returned zero directly relevant hits.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (malignant hypertensive renal disease) has plausible drug-class mechanism but zero supporting trials or literature (L5), and fosinopril is not currently marketed in Taiwan/US. A Blocking-severity safety data gap (TFDA label warnings/contraindications) also prevents initial safety screening.

**To proceed, the following is needed:**
- TFDA/FDA label data: warnings, contraindications, DDI (currently all gaps)
- Formal original indication and mechanism-of-action documentation for fosinopril
- Targeted literature/trial search using ACEi-class terms (not just "fosinopril") for malignant hypertensive renal disease, since direct searches returned no hits
- Re-validation of rank 4 and 5 predictions before any further evaluation, given the mismatched literature and likely embedding artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

