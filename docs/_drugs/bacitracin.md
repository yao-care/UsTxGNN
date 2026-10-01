---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Bacitracin
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

# Bacitracin: From Topical Antibacterial Use to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a polypeptide antibiotic marketed in the US as a topical ointment. The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **0 clinical trials** and **0 publications** currently support this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% (rank 64 overall) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

The licence records contain no approved-indication text, so the original labelled indication could not be extracted. The original use above is inferred from the product type (an ointment).

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank. Bacitracin is known to inhibit bacterial cell-wall synthesis by blocking dephosphorylation of C55-isoprenyl pyrophosphate. It acts mainly against gram-positive organisms, which is why it is used topically.

The link to the new indication is weak. Punctate epithelial keratoconjunctivitis is often viral, toxic, or dry-eye related rather than bacterial, so an antibacterial has no clear target. The TxGNN score of about 0.99999 should not be over-read. The top-ranked candidates all score almost identically, so the score does not discriminate between them. It probably reflects proximity in the knowledge graph rather than a real therapeutic signal.

The ophthalmic route is also unconfirmed. Route compatibility is still pending, and the only dosage form in the US records is an ointment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The 5 main entries below are the main listings out of 20. The records give no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M004 | Bacitracin | Ointment | A-S Medication Solutions |
| M004 | Bacitracin | Ointment | BluePoint Laboratories |
| M004 | Bacitracin | Ointment | Rugby Laboratories |
| M004 | Bacitracin | Ointment | CVS Pharmacy |
| M004 | Bacitracin | Ointment | H E B |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5). The mechanistic link is weak, because an antibacterial has little reason to help a largely non-bacterial condition. Safety data are also missing, which blocks any safety screening.

**To proceed, the following is needed:**
- The package insert warnings and contraindications, which are currently a blocking gap
- DrugBank mechanism of action data
- The labelled indications, so it is clear what counts as new use
- A check of whether an ophthalmic formulation exists or is feasible
- Evidence that bacterial infection contributes to this condition, plus any trials or literature testing bacitracin

Among the other top-ranked predictions, otitis externa (rank 4) is the only one with any literature. That includes one double-blind study of 151 patients using a polymyxin B plus bacitracin ointment. It is graded L4 and marked "Research Question", and it may be a better lead than the current top prediction.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

