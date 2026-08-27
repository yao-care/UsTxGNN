---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 665
evidence_level: L5
indication_count: 6
---

# Erdafitinib
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

# Erdafitinib: From Unspecified Original Indication to Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib (DrugBank DB12147) is a pan-FGFR tyrosine kinase inhibitor; its original approved indication is not recorded in this evidence pack. The TxGNN model predicts a possible effect on **Pulmonary Hypertension**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (marked as data gap in evidence pack; no `original_indications` or license text on file) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Market Status (Taiwan) | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for erdafitinib in this evidence pack (`original_moa` is unrecorded). Based on the mechanistic annotations attached to the predictions themselves, erdafitinib is referenced as a pan-FGFR inhibitor, and other candidate indications in this pack (rheumatoid arthritis, brachydactyly-syndactyly syndrome) independently corroborate this FGFR-inhibitor classification.

For the top-ranked prediction, pulmonary hypertension, the supplied rationale notes that the FGF/FGFR pathway participates in pulmonary vascular remodeling, but the direction of effect is **not clear**: FGFR inhibition could theoretically slow proliferative remodeling, but FGF2 also has endothelial-protective effects, so inhibition could equally impair vascular repair. The rationale explicitly flags this as bidirectionally uncertain with no clinical or literature support.

Given this, the mechanistic plausibility for pulmonary hypertension is weak and speculative rather than well-grounded — it should be treated as a hypothesis-generating signal only, not a validated repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: one literature record (PMID 31862477, a 2020 review on FDA-approved kinase inhibitors) exists elsewhere in this evidence pack, but it is attached to the rheumatoid arthritis candidate (rank 4), not to pulmonary hypertension, and only mentions erdafitinib in a general drug-class listing rather than in the context of either indication.*

---

## US Market Information

No approved licenses are currently on record. Taiwan regulatory status is listed as 未上市 (not marketed), with 0 total licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in this evidence pack — DG001 flags TFDA label warnings/contraindications as a **Blocking** data gap for safety screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction is evidence level L5 (model prediction only) with zero clinical trials and zero literature support, and its underlying mechanism is explicitly flagged as directionally uncertain. Combined with the drug's unmarketed status in Taiwan and a blocking data gap on safety labeling, there is currently no basis to advance past initial screening.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, blocking — required before any S1 safety screening)
- Erdafitinib mechanism of action detail (DG002)
- Confirmation of the drug's original approved indication(s), currently absent from this pack
- Preclinical or mechanistic studies resolving the directional uncertainty of FGFR inhibition in pulmonary vascular remodeling before any further evidence-gathering is prioritized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

