---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 1049
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# PIRFENIDONE: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

> Pirfenidone is an antifibrotic agent whose established pharmacology (inhibition of TGF-β1 and PDGF signaling, reducing fibroblast proliferation and collagen synthesis) underlies its approval for idiopathic pulmonary fibrosis.
> The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma**,
> but **no clinical trials** and **no publications** currently support this specific direction — this is a model-only prediction with a mechanistically weak rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic Pulmonary Fibrosis (per literature reference in evidence pack; no structured license record available) |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available for pirfenidone in this evidence pack. However, literature captured elsewhere in the pack (PMID 29702057) describes its known pharmacology: pirfenidone inhibits TGF-β1 and platelet-derived growth factor signaling, leading to decreased fibroblast proliferation and collagen synthesis. This antifibrotic mechanism is the basis of its approval for idiopathic pulmonary fibrosis.

Extracutaneous mastocytoma, by contrast, is a mast cell neoplasm whose pathogenesis is driven primarily by KIT mutations and mast cell hyperproliferation — a pathway that does not overlap with pirfenidone's TGF-β1/collagen-synthesis mechanism. The evidence pack's own rationale for this prediction explicitly flags this gap: *"TxGNN's high score reflects only knowledge-graph embedding similarity; pirfenidone's known action of inhibiting TGF-β1-mediated fibroblast proliferation/collagen synthesis and anti-inflammatory effects has no direct biological connection to the pathogenic mechanism of mast cell tumors (KIT mutation, mast cell proliferation) — the mechanistic link is weak."*

In other words, this prediction currently rests on graph-embedding similarity rather than any plausible or demonstrated biological pathway, and should be treated as a low-confidence hypothesis rather than a repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Pirfenidone has no license records in this evidence pack (`total_licenses: 0`, market status: Not Marketed). No authorization or product information is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are recorded as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for extracutaneous mastocytoma is supported only by a TxGNN embedding score (L5, model prediction only) — there are zero clinical trials and zero publications, and the drug's known antifibrotic mechanism does not plausibly connect to the KIT-mutation-driven pathology of this mast cell tumor.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): TFDA/manufacturer label warnings and contraindications
- Resolve DG002 (High): confirm pirfenidone's mechanism of action via DrugBank or primary literature
- In vitro/preclinical evidence testing pirfenidone activity in KIT-mutant mast cell models
- If mechanistic plausibility cannot be established, deprioritize this candidate in favor of higher-evidence predictions in the same batch (e.g., the fibroblastic neoplasm candidate, which has L3/S1 evidence but also carries an unresolved safety signal — sarcoma occurrence after pirfenidone use, PMID 29702057 — that should be investigated in parallel)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

