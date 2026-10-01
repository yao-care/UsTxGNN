---
layout: default
title: Alitretinoin
parent: Model Prediction Only (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Alitretinoin
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

# Alitretinoin: From an Unrecorded Original Indication to Amenorrhea

## One-Sentence Summary

Alitretinoin (9-cis-retinoic acid) is a retinoid marketed in the US as a topical gel (PANRETIN), but the record does not state its approved indication.
The TxGNN model predicts it may be effective for **amenorrhea**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
It is a knowledge-graph score only, and the biology argues against it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available record |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the record. Alitretinoin is the 9-cis form of retinoic acid and acts as a pan-agonist of the retinoic acid receptors (RAR) and retinoid X receptors (RXR).

The prediction is hard to justify biologically. Systemic retinoids are teratogenic and can disturb menstrual function, so they are more likely to cause menstrual problems than to treat them. The only marketed product here is a topical gel, so systemic exposure for a gynecologic condition would also be a different route from anything on the US label.

The high score should be read as a graph-based association, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020886 | PANRETIN (Advanz Pharma (US) Corp.) | Gel (topical) | Not listed in the record |

## Safety Considerations

- **Class warning**: Systemic retinoids are teratogenic and can disturb menstrual function.

Please refer to the package insert for drug-specific warnings, contraindications and drug interactions. No interaction data were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or publications. Known retinoid biology (teratogenicity, menstrual disturbance) points away from a therapeutic role in amenorrhea.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indication)
- Mechanism of action data from DrugBank
- Any human or mechanistic evidence linking 9-cis-retinoic acid to amenorrhea; none was found

**Note:** Within the same evidence pack, the rank 2 prediction, **acne**, has the only human evidence (Evidence Level L3, recommendation "Research Question"). It includes a 1996 clinical comparison of oral 9-cis- vs 13-cis-retinoic acid ([PMID 8884148](https://pubmed.ncbi.nlm.nih.gov/8884148/)). It would be a better candidate for further review, weighed against the established option of isotretinoin.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

