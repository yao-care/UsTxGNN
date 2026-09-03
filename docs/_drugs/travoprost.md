---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 1253
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma / Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

> Travoprost is a topical prostaglandin F2α (FP receptor) agonist originally used to lower intraocular pressure in open-angle glaucoma and ocular hypertension.
> The TxGNN model predicts it may be effective for **Visceral Calciphylaxis**,
> but currently **no clinical trials and no publications** directly support this specific direction — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / Ocular Hypertension (topical IOP reduction) — inferred from trial evidence in this pack; formal MOA/indication record is a data gap |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available (flagged as a High-severity data gap). Based on information present in the evidence pack, travoprost is a selective FP receptor agonist; its established clinical effect is increasing uveoscleral outflow to reduce intraocular pressure, and its proven efficacy is limited to glaucoma and ocular hypertension.

Visceral calciphylaxis is a distinct disease process involving vascular medial calcification and microthrombosis, typically seen in end-stage renal disease. There is no established pharmacological pathway connecting FP receptor agonism to the calcification/thrombotic cascade underlying calciphylaxis.

The evidence pack's own mechanistic assessment for this candidate explicitly notes that the connection is **not a known biological pathway** — the high TxGNN score likely reflects semantic clustering of "vascular disease"-related nodes in the knowledge graph embedding space, rather than a genuine pharmacological relationship. This should be treated as a hypothesis-generating signal only, not as mechanistically substantiated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorization records are present in the reviewed dataset (Market Status: Not marketed; Total licenses: 0). Travoprost's marketed formulations elsewhere are ophthalmic solutions for glaucoma/ocular hypertension (e.g., Travatan®/Travatan Z®), referenced only indirectly through clinical trial titles in this pack — no formal license data was available to tabulate here.

---

## Safety Considerations

Please refer to the package insert for safety information. Note that TFDA warning/contraindication data for this candidate is currently an unresolved **Blocking** data gap, which by itself prevents any progression to a formal safety review (S1) regardless of efficacy evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (visceral calciphylaxis) has zero supporting clinical trials or literature, and the mechanistic rationale itself flags the association as likely a graph-embedding artifact rather than a genuine pharmacological link. Combined with a Blocking-severity gap in TFDA label/safety data, there is no basis to advance this candidate beyond model prediction (L5/S0).

**To proceed, the following is needed:**
- TFDA (or equivalent regulatory) label data — warnings, contraindications, DDI (Blocking gap, required before any S1 safety screen)
- Confirmed mechanism of action documentation from DrugBank or primary literature
- Preclinical or case-level evidence specifically linking FP receptor agonism to vascular calcification/calciphylaxis pathophysiology
- If pursued, re-evaluate lower-ranked candidates in this pack with actual trial/literature support (e.g., "vascular disease," "hemangioendothelioma") — though note those signals were graded low-relevance (mismatched to glaucoma trials) or, in one case, evidence of an **adverse** effect (uveal effusion) rather than therapeutic benefit, and would also require independent validation before advancing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

