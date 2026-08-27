---
layout: default
title: Fludrocortisone
parent: 僅模型預測 (L5)
nav_order: 716
evidence_level: L5
indication_count: 8
---

# Fludrocortisone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Fludrocortisone: Original Indication Not on File — Assessing Primary Cutaneous T-Cell Lymphoma as a Predicted New Indication

## One-Sentence Summary

The evidence pack for Fludrocortisone (DrugBank DB00687) does not contain its original approved indication or mechanism-of-action data — both are flagged as gaps. The TxGNN model's top-ranked prediction is **Primary Cutaneous T-Cell Lymphoma**, but this direction is currently supported by **0 clinical trials** and only **1 case-report-level publication**, and the evidence pack's own mechanistic analysis flags weak biological plausibility for this specific pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no licenses or approved-indication text on file) |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for fludrocortisone is not available in this evidence pack (flagged as a High-severity data gap). Likewise, no original indication is on file, and the drug has zero licenses/approvals recorded in the current market dataset.

That said, the evidence pack's own mechanistic rationale for this candidate offers relevant context: fludrocortisone acts primarily as a **mineralocorticoid receptor agonist**, with glucocorticoid activity far weaker than corticosteroids such as prednisone or dexamethasone — the agents actually used for immune modulation and lymphotoxic effect in cutaneous T-cell lymphoma (CTCL). The analysis notes there is **no established mechanistic basis** for fludrocortisone itself to exert direct anti-tumor or immunomodulatory activity against T-cell lymphoma.

The most plausible explanation offered is that the high TxGNN score reflects a broad "corticosteroid class" edge shared in the knowledge graph between steroid-class drugs and lymphoma-related disease nodes, rather than a drug-specific pharmacological signal for fludrocortisone. This distinction matters: it means the prediction score alone should not be read as evidence of a real biological effect for this specific drug–disease pair.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6028675](https://pubmed.ncbi.nlm.nih.gov/6028675/) | 1967 | Case Report | Archives of Dermatology | "Pathergic granulomatosis" — no abstract available; relevance to CTCL and to fludrocortisone specifically has not been confirmed (title-only reference, Tier 3) |

Only one publication is associated with this drug–disease pair, and it is a low-tier case report without an available abstract, so its direct relevance to fludrocortisone's use in CTCL cannot be confirmed from the evidence on hand.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data were all queried but returned no results — DDI query status: not found; 0 interactions identified.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial evidence, only a single low-quality case report (Tier 3, relevance unconfirmed), and the evidence pack's own mechanistic review concludes there is no credible pharmacological basis linking fludrocortisone's mineralocorticoid-dominant activity to a therapeutic effect in Primary Cutaneous T-Cell Lymphoma. The high TxGNN score most likely reflects a shared "corticosteroid class" association in the knowledge graph rather than a drug-specific signal.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (currently a **Blocking** data gap — required before any S1 safety screening can occur)
- Confirmed mechanism-of-action data for fludrocortisone (currently a **High**-severity gap)
- Original approved indication and licensing history, to establish a proper baseline for comparison against the predicted indication
- Full-text review of PMID 6028675 to confirm whether it has any genuine relevance to CTCL or fludrocortisone's use in it
- If further exploration of this drug is warranted, the "eye disease" candidate (rank 6, evidence level L4, decision stage S1) shows comparatively stronger — though still indirect — literature support (including a Phase 1 safety trial, PMID 36161841) and may be a more productive research direction than the top-ranked CTCL prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

