---
layout: default
title: Omidenepag Isopropyl
parent: 僅模型預測 (L5)
nav_order: 994
evidence_level: L5
indication_count: 7
---

# Omidenepag Isopropyl
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

# Omidenepag Isopropyl: From Glaucoma to Pancreatitis

## One-Sentence Summary

> Omidenepag isopropyl is a selective EP2 receptor agonist used to lower intraocular pressure in glaucoma/ocular hypertension.
> The TxGNN model predicts it may be effective for **Pancreatitis**,
> but this is currently a **pure algorithmic prediction with 0 clinical trials and 0 publications** supporting the connection, and the model's own rationale explicitly states that no plausible mechanistic link could be established.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / Ocular Hypertension (inferred from known EP2 receptor agonist mechanism; not present in formal drug record) |
| Predicted New Indication | Pancreatitis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data for omidenepag isopropyl is not available in this evidence pack. Based on the drug's known pharmacological class referenced within the evidence itself, it is a selective **EP2 (prostaglandin E2) receptor agonist**, used clinically to reduce intraocular pressure by promoting uveoscleral outflow — a mechanism entirely specific to ocular tissue.

The predicted new indication, pancreatitis, involves pancreatic enzyme autodigestion and acute inflammatory pathways. The evidence pack's own mechanistic rationale for this candidate explicitly states: *"目前無法建立 EP2 receptor agonism 與胰臟炎病理機轉（胰酶自體消化、發炎反應）之間的合理連結，此候選適應症機轉基礎薄弱，僅為知識圖譜相似性推論"* — i.e., no biologically plausible link between EP2 agonism and pancreatitis pathophysiology has been established. This candidate is a knowledge-graph similarity output rather than a mechanism-supported hypothesis.

Given the drug is not marketed in this jurisdiction, has no formal MOA record, and the top-ranked predicted indication itself lacks mechanistic justification, this prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

The drug is currently not marketed in this jurisdiction (0 licenses on record); no authorization information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (pancreatitis) is supported only by TxGNN's knowledge-graph similarity score (L5), with zero clinical trials or literature, and the evidence pack's own mechanistic analysis concludes no plausible biological link exists between EP2 receptor agonism and pancreatitis pathophysiology. The drug is also not currently marketed in this jurisdiction, and formal MOA/safety data are missing (flagged as Blocking/High severity data gaps).

**To proceed, the following is needed:**
- Confirmed original indication and formal MOA documentation (currently DrugBank data gap)
- TFDA/regulatory label warnings and contraindications (blocking gap for safety review)
- Preclinical or mechanistic studies specifically linking EP2 agonism to pancreatic inflammation before further investment
- Reassessment of lower-ranked candidates (e.g., esophageal varices, rank 3–4) which at least have a theoretical vascular/smooth-muscle rationale, versus pancreatitis which does not
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

