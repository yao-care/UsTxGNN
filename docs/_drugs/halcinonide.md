---
layout: default
title: Halcinonide
parent: Model Prediction Only (L5)
nav_order: 766
evidence_level: L5
indication_count: 10
---

# Halcinonide
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

# Halcinonide: From Topical Corticosteroid Therapy to Annular Atrophic Lichen Planus

## One-Sentence Summary

Halcinonide is a potent topical glucocorticoid, marketed in the US as creams and solutions.
The TxGNN model predicts it may be useful for **annular atrophic lichen planus**,
but there are currently **0 clinical trials** and **0 publications** for this specific indication, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied records (the approved indication text is empty for all listed licenses) |
| Predicted New Indication | Annular atrophic lichen planus |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied record. Halcinonide is known as a potent topical glucocorticoid, and this comes from class knowledge rather than the supplied data. Glucocorticoids suppress local inflammation and T-cell activity, which is plausible for T-cell-mediated lichenoid skin diseases such as lichen planus.

Two caveats limit this prediction:
- Topical corticosteroids are already established practice for lichen planus in general, so any added value of halcinonide specifically has not been assessed.
- Annular atrophic lichen planus is a rare variant, and no trial or publication was supplied for it.

TxGNN gives near-identical scores (about 99.93%) to several lichen planus variants (pigmentosus, hypertrophic, pemphigoides). This suggests the model is picking up a class-level pattern rather than evidence specific to this variant.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017556 | HALCINONIDE (Sun Pharmaceutical Industries, Inc.) | Cream | Not stated in supplied record |
| NDA017556 | Halog (Sun Pharmaceutical Industries, Inc.) | Cream | Not stated in supplied record |
| NDA017556 | Halog (Genus Lifesciences Inc.) | Cream | Not stated in supplied record |
| ANDA217671 | Halcinonide Topical Solution (INA Pharmaceutics Inc) | Solution | Not stated in supplied record |
| NDA017823 | HALOG (E.R. Squibb & Sons, L.L.C.) | Solution | Not stated in supplied record |

Seven licenses are recorded in total; five are shown above.

## Safety Considerations

Please refer to the package insert for safety information. The package insert warnings and contraindications were not included in the supplied record, and no drug interactions were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials or literature (L5), and the class-level rationale overlaps with existing topical corticosteroid use in lichen planus. Incremental value for this rare variant is unassessed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed for safety screening
- Approved indication text and mechanism of action data for halcinonide
- Any case reports or case series for annular atrophic lichen planus
- Comparison against existing topical corticosteroid practice for lichen planus

**Note on other predictions:** The rank 6 prediction, **alopecia areata**, has one publication: [PMID 915049](https://pubmed.ncbi.nlm.nih.gov/915049/) (Montes, J Cutan Pathol, 1977), "Topical halcinonide in alopecia areata and in alopecia totalis." Only the title was supplied, so the design and outcomes are unverified. It is provisionally L3 and could drop to L4 if it is an anecdotal report. It is the most evidence-supported of the ten predictions, but it remains a research question rather than a Go candidate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

