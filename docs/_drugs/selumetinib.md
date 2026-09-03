---
layout: default
title: Selumetinib
parent: 僅模型預測 (L5)
nav_order: 1154
evidence_level: L5
indication_count: 10
---

# Selumetinib
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

# Selumetinib: From NF1-Related Plexiform Neurofibroma to Familial Generalized Lentiginosis

## One-Sentence Summary

> Selumetinib is a MEK1/2 inhibitor whose established use — noted in the evidence pack's rationale text rather than the structured drug profile — is NF1-related plexiform neurofibroma; formal original-indication and mechanism-of-action fields are flagged as data gaps in this pack.
> The TxGNN model's top prediction is **Familial Generalized Lentiginosis**,
> but this specific prediction currently has **0 clinical trials** and **0 publications** supporting it — it is a model-score-only candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NF1-related plexiform neurofibroma *(sourced from repurposing-rationale text; not present in structured `original_indications` field — data gap DG002 relates)* |
| Predicted New Indication | Familial Generalized Lentiginosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (marked as a High-severity data gap, DG002). Based on information embedded in the pack's own rationale text, Selumetinib is understood to be a MEK1/2 inhibitor, and its use in NF1-related plexiform neurofibroma is referenced as an established application of this drug class.

Familial generalized lentiginosis belongs to the multiple-lentigines/RASopathy disease group, which can involve overlapping germline genes (e.g., *PTPN11*) that sit upstream in the RAS–RAF–MEK–ERK signaling cascade. Since MEK inhibitors act directly downstream of this pathway, there is a plausible mechanistic rationale for testing selumetinib in RASopathy-spectrum conditions.

That said, the evidence pack explicitly states this rationale is "purely a TxGNN prediction score, with no clinical or literature support" (from the pack's own rank-1 rationale text). The mechanistic plausibility is real, but it remains theoretical for this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Selumetinib currently has **no NDA or marketing authorization on file** in this evidence pack — market status is recorded as "未上市" (Not Marketed) with 0 total licenses. No product/dosage-form/indication data is available to tabulate.

---

## Cytotoxicity

Selumetinib is a targeted small-molecule kinase inhibitor (MEK1/2), used in the oncology/RASopathy space based on the evidence pack's rationale references; several of the drug's other predicted indications in this pack are neoplasms (rhabdoid tumor, peripheral nerve schwannoma), supporting its classification here.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (All key warnings, contraindications, and drug-interaction fields in this evidence pack are marked as data gaps; DG001 flags this as a **Blocking** gap that prevents entry into S1 safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (familial generalized lentiginosis) has zero clinical trial or literature support and is explicitly labeled L5/model-prediction-only in the evidence pack itself. Combined with the blocking safety data gap (no TFDA/package-insert warnings available) and the drug's unmarketed US status, there is currently no basis to advance this specific indication.

**To proceed, the following is needed:**
- Package insert / regulatory label data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Any preclinical or clinical evidence specific to familial generalized lentiginosis or the broader RASopathy/lentiginosis spectrum
- Formal original-indication records for Selumetinib (currently only inferable from rationale text, not a structured field)

**Note on portfolio prioritization:** Within this same evidence pack, **rank 9 — peripheral nerve schwannoma** carries substantially stronger evidence (L3, one Phase 2 trial with direct NF2-schwannoma relevance plus 7 supporting publications including a preclinical MEK/ERK mechanistic study) and may warrant separate evaluation ahead of the top-ranked candidate discussed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

