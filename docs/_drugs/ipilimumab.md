---
layout: default
title: Ipilimumab
parent: Model Prediction Only (L5)
nav_order: 808
evidence_level: L5
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ipilimumab: From Cutaneous Melanoma to Choroideremia

## One-Sentence Summary

Ipilimumab (Yervoy) is a CTLA-4 blocking antibody used in cutaneous melanoma. The TxGNN model predicts it may be effective for **choroideremia**, an inherited retinal degeneration. This prediction has **no clinical trials and no publications** behind it, so it is a model output only and is likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous melanoma (taken from the pack's mechanistic rationale; the license text fields are empty) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both entries carry the same number, BLA125377) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Ipilimumab is known to block CTLA-4, which releases a checkpoint on T-cell priming and increases T-cell activation. This is the mechanism behind its use in melanoma.

The evidence review found **no plausible mechanistic link** to this indication. Choroideremia is an X-linked disease caused by loss of function of the CHM (REP1) gene, and it degenerates the retina and choroid. Nothing in the data connects CTLA-4 blockade to that process.

The high score (0.99) is probably a knowledge-graph artifact. One possible source is neighboring ocular or uveal melanoma nodes. Systemic immune activation also carries a risk of ocular immune-related adverse events, which argues against using ipilimumab in a degenerative retinal disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125377 | YERVOY (E.R. Squibb & Sons, L.L.C.) | Injection | Not listed in the license data |

The pack lists two license entries. They are identical, so they are shown once. The only route is injectable.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (immune checkpoint inhibitor, anti-CTLA-4 antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Low in general, per drug class. Please refer to the package insert warnings and precautions. |
| Emetogenicity Classification | Low, per drug class. Please refer to the package insert. |
| Monitoring Items | Liver function, thyroid and adrenal function, blood glucose, and ocular and gastrointestinal symptoms, because of immune-related adverse events. Please refer to the package insert for the full schedule. |
| Handling Protection | Standard biologic handling. The package insert governs any special measures. |

---

## Safety Considerations

- **Ocular risk**: Systemic immune activation carries a risk of ocular immune-related adverse events. This is a concern in any retinal degenerative disease.

Please refer to the package insert for other safety information. The Evidence Pack contains no drug interaction data, warnings or contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support and no plausible mechanistic link. The model score alone is not enough, and the risk of ocular immune toxicity argues against pursuing it.

**To proceed, the following is needed:**
- Any preclinical or mechanistic evidence linking CTLA-4 blockade to retinal degeneration
- The full package insert warnings and contraindications
- Original indication and mechanism of action data for the drug record

**Note on the second prediction:** Non-cutaneous melanoma (rank 2, score 99.02%) has much stronger support. It has L3 evidence, many melanoma trials including a completed Phase 3 RCT, and a plausible mechanism. It is a better candidate for further review, but the melanoma subtypes enrolled in the trials still need to be confirmed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

