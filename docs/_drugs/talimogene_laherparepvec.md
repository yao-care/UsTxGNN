---
layout: default
title: Talimogene Laherparepvec
parent: 僅模型預測 (L5)
nav_order: 1197
evidence_level: L5
indication_count: 7
---

# Talimogene Laherparepvec
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using no specific skill (this is a direct content-generation task per the explicit report template already provided in the prompt).

# Talimogene Laherparepvec: From Melanoma (Skin/Lymph Node Metastasis) to CMM7

## One-Sentence Summary

> Talimogene laherparepvec (T-VEC) is an oncolytic HSV-1-based immunotherapy approved for intratumoral injection in unresectable melanoma with skin/lymph node metastases.
> The TxGNN model predicts it may be effective for **CMM7** (a cutaneous malignant melanoma susceptibility subtype),
> but **no clinical trials** and **no literature** currently support this specific prediction — it is based solely on knowledge-graph inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma with skin/lymph node metastases (unresectable) |
| Predicted New Indication | CMM7 |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, talimogene laherparepvec is an oncolytic herpes simplex virus type 1 (HSV-1)-based immunotherapy engineered to express GM-CSF, already approved for local intratumoral injection in unresectable melanoma with skin and lymph node metastases; mechanistically it may be applicable to CMM7.

CMM7 (cutaneous malignant melanoma susceptibility locus 7) represents a genetic subtype within the same melanoma disease spectrum as the drug's approved indication, giving the prediction reasonable biological plausibility as a within-lineage extension rather than a cross-tumor-type leap. However, this mechanistic link has not been validated by any subtype-specific clinical trial or publication, and CMM7 as a genetically defined susceptibility classification (rather than a distinct clinical entity) raises questions about how this indication would translate into an actual treatable population.

Other TxGNN-predicted candidates for this drug (pediatric leptomeningeal melanoma, uveal melanoma, and several non-melanoma carcinomas — glottis SCC, occult lung SCC, rectal cloacogenic carcinoma, gallbladder adenosquamous carcinoma) show progressively weaker mechanistic rationale, particularly for non-melanoma histologies where intratumoral injectability and antigenic relevance to T-VEC's mechanism are questionable. All seven predictions share the same evidentiary limitation: model score only, no supporting trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The drug is currently **not marketed** in this jurisdiction (0 licenses on file), so no authorization records are available for tabulation.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (oncolytic viral therapy, HSV-1-based, GM-CSF-expressing) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As a live attenuated oncolytic virus, administration requires institutional biosafety/infection-control precautions (e.g., avoiding contact with immunocompromised individuals, herpes-naive close contacts, and pregnant individuals); specifics not confirmed in current evidence pack |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven TxGNN-predicted indications are rated L5 (model prediction only) with zero supporting clinical trials or literature. Additionally, a blocking data gap exists for TFDA/FDA label warnings and contraindications (DG001), which prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain and parse the official package insert for warnings/contraindications from the relevant regulatory agency
- Resolve DG002: obtain detailed mechanism of action data via DrugBank API to strengthen mechanistic-link analysis
- Generate or identify subtype-specific clinical/literature evidence for CMM7 before advancing beyond S0
- Assess route compatibility (intratumoral injection feasibility) for each candidate indication, particularly deep-visceral or CNS-involving sites (leptomeningeal, gallbladder, lung occult SCC)
- Given the weak mechanistic basis for non-melanoma candidates (ranks 4–7), consider deprioritizing these in favor of melanoma-lineage subtypes (ranks 1–3)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

