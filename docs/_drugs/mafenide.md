---
layout: default
title: Mafenide
parent: Model Prediction Only (L5)
nav_order: 881
evidence_level: L5
indication_count: 10
---

# Mafenide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Mafenide: From Topical Burn Wound Antibacterial to Irritable Bowel Syndrome

## One-Sentence Summary

> Mafenide is a sulfonamide-class topical antibacterial historically used for burn wound infection prophylaxis (brand name Sulfamylon), but it currently holds **no marketing license in Taiwan**.
> The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags it as likely model noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no TFDA license on file; historically used as a topical antibacterial for burn wounds (Sulfamylon) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for mafenide is not available in this evidence pack (Data Gap). Based on general pharmacological knowledge, mafenide is a topical sulfonamide antibacterial (a PABA antagonist that inhibits bacterial folate synthesis), historically marketed as Sulfamylon for burn wound infection prophylaxis. It is not currently licensed in Taiwan — 0 TFDA licenses, market status "not marketed."

There is no established mechanistic or clinical relationship between mafenide's known antibacterial action and irritable bowel syndrome, a functional gastrointestinal motility/sensitivity disorder. No shared pathway, receptor, or pharmacological class connects a topical wound antiseptic to IBS pathophysiology.

The evidence pack's own rationale assessment concludes that this TxGNN score most likely reflects knowledge-graph embedding noise — arising from mafenide's sparse connectivity as a drug node — rather than a genuine biological signal. This pattern repeats across the drug's full top-10 prediction list (cauda equina syndrome, panuveitis, iris disease, uveitis, acne, isolated iridoschisis, abnormal pupillary function, benign neoplasm of iris, iris cancer): all score >99.9%, all are L5/Hold, and all lack any clinical or literature support. Only the acne and ophthalmic-cluster candidates carry even a weak theoretical rationale (antibacterial analogy for acne; sulfonamide/carbonic-anhydrase-inhibitor analogy for eye disease), and the rationale text explicitly notes these remain unsupported by data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Mafenide currently holds no TFDA license in Taiwan (0 total licenses; market status: not marketed). No product-level licensing records are available for tabulation.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are not available in this evidence pack; DDI query returned "not found.")

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support, no mechanism-of-action data, and no current Taiwan marketing authorization. The evidence level is L5 (model prediction only), and the evidence pack's own mechanistic assessment considers the TxGNN score likely to be knowledge-graph noise rather than a real signal.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, blocking — required before any S1 safety screening)
- Verified mechanism-of-action source from DrugBank or primary literature (DG002)
- Preclinical or mechanistic studies establishing a plausible pathway between mafenide and IBS
- Reassessment of regulatory feasibility given mafenide has no existing Taiwan marketing authorization to build on
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

