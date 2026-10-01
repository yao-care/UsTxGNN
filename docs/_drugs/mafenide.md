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

# Mafenide: From Burn Wound Infection to Irritable Bowel Syndrome

## One-Sentence Summary

Mafenide is a topical sulfonamide antimicrobial, marketed in the US as a cream (Sulfamylon) for burn wound care.
The TxGNN model predicts it may be effective for **irritable bowel syndrome**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US label data (mafenide is known as a topical burn wound antimicrobial) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Mafenide is a topical sulfonamide antimicrobial and carbonic anhydrase inhibitor, used on the skin and not systemically. Its effect on burn wound infection is established, but that does not carry over to irritable bowel syndrome (IBS).

We found no credible mechanistic link between mafenide and IBS. IBS is a functional gut disorder, and a cream applied to burn wounds has no known action on gut motility, visceral sensitivity, or the gut microbiome. The score of 99.97% (model rank 1234) is a graph-based result and does not indicate clinical promise.

The route also does not fit. Mafenide is available only as a cream, and no evaluation of a route suitable for IBS has been done. Route compatibility is still pending.

The other nine top predictions show the same pattern, with no trials or literature for any of them:
- **Eye-related (uveitis, panuveitis, iris disease, iridoschisis, abnormal pupillary function, iris neoplasms):** These likely reflect clustering of iris and eye nodes in the knowledge graph. The only conceivable link is carbonic anhydrase inhibition, and mafenide has no evidence of ocular safety or efficacy.
- **Cauda equina syndrome:** This is a surgical neurological emergency with no plausible role for a topical antimicrobial.
- **Acne:** This is the most biologically plausible candidate, since mafenide is antibacterial and acne involves *Cutibacterium acnes*. Local irritation, pain on application, and established topical alternatives limit its practical value. It is flagged only as a research question.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016763 | SULFAMYLON (Rising Pharma Holdings, Inc.) | Cream (topical) | Not listed in the source data |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried database.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and no credible mechanism links a topical burn antimicrobial to IBS. A high model score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to allow a proper mechanistic analysis
- A route-compatibility assessment, since only a topical cream exists
- Any preclinical or clinical signal for IBS
- If the project wants to pursue a candidate for this drug, the acne prediction (the only one flagged as a research question) is the better one to examine first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

