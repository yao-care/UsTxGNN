---
layout: default
title: Lusutrombopag
parent: 僅模型預測 (L5)
nav_order: 880
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# Lusutrombopag: From Unconfirmed Original Indication to Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Lusutrombopag (DrugBank DB13125) is a thrombopoietin (TPO) receptor agonist; its original approved indication is not recorded in this evidence pack, and the drug is not currently marketed in Taiwan (0 TFDA licenses on file). The TxGNN model's top prediction is **Hereditary Thrombocytopenia with Normal Platelets**, but this is currently supported by **0 clinical trials** and **0 publications** — the evidence pack itself flags the prediction as a possible knowledge-graph artifact rather than a confirmed mechanistic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/indication records in evidence pack (drug not marketed in Taiwan) |
| Predicted New Indication | Hereditary Thrombocytopenia with Normal Platelets |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status (TFDA) | 未上市 (Not marketed) |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lusutrombopag in this evidence pack. Based on general pharmacological class knowledge, lusutrombopag is a TPO receptor agonist, a class of drugs that stimulate megakaryocyte production in the bone marrow to raise platelet counts — mechanistically, this pathway is broadly relevant to conditions of platelet under-production.

However, the evidence pack's own rationale raises a significant concern about the top prediction: "hereditary thrombocytopenia with normal platelets" is a semantically contradictory disease label (low platelet count vs. normal platelet count), which the evidence pack interprets as more likely to be a rare disease taxonomy entry than a genuine TPO-agonist target. The high TxGNN score may reflect knowledge-graph term proximity to the word "thrombocytopenia" rather than a real pharmacological relationship. Because the original indication is also unrecorded here, there is no confirmed baseline to assess mechanistic similarity between old and new indications.

This same caution extends across all 10 ranked predictions in this pack: ranks 2–5 involve structural/functional platelet disorders (mitral valve disease, dense granule disease, storage pool deficiency) where TPO-driven platelet *production* would not address the underlying defect, and ranks 6–10 (ALS, motor neuron disease, cortical malformation, skeletal dysplasia) have no stated mechanistic link to TPO signaling at all — the evidence pack explicitly labels several of these as likely "KG embedding noise" or "false positive" clusters.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

No license or marketing authorization on record — lusutrombopag is not currently marketed in Taiwan (0 TFDA licenses).

## Safety Considerations

Please refer to the package insert for safety information.

Note: this evidence pack flags TFDA label/warning data as a **Blocking** data gap (DG001) — without it, even a basic safety pre-screen (S1) cannot be completed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are TxGNN model output only (L5), with zero clinical trials or literature identified across 33 source queries. The top-ranked prediction itself is flagged by the evidence pack as a probable knowledge-graph artifact due to a semantically contradictory disease name, and a Blocking data gap (missing TFDA label/warnings, DG001) prevents any safety pre-screening.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications data (resolves DG001, currently Blocking)
- Confirmed original approved indication(s) and mechanism of action (resolves DG002)
- Independent verification of whether the top candidate diseases (ranks 1–5) represent a real TPO-pathway signal or a KG term-proximity artifact, before committing further evaluation resources
- If pursued, reassessment of ranks 6–10 is not recommended given the evidence pack's own assessment that these lack any plausible mechanistic basis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

