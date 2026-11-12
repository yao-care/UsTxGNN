---
layout: default
title: Ecallantide
parent: Model Prediction Only (L5)
nav_order: 639
evidence_level: L5
indication_count: 5
monitor_inn: "ECALLANTIDE"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "Peyronie disease", "pancreatitis", "esophageal varices without bleeding", "esophageal varices with bleeding"]
last_modified_at: 2026-11-12
description: "Ecallantide: predicted new indication Serpinopathy with toxic serpin polymerization (evidence level L5). Approved use: Not recorded in the local data"
---

# Ecallantide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ecallantide: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## One-Sentence Summary

Ecallantide is a recombinant kallikrein inhibitor protein given by injection.
The TxGNN model predicts it may be relevant to **serpinopathy with toxic serpin polymerization**, but **no clinical trials and no publications** currently support this direction, so it rests on a computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Serpinopathy with toxic serpin polymerization |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ecallantide is known as a kallikrein inhibitor, a protein-based drug that acts on the plasma kallikrein pathway.

The model's high score is likely driven by a network-level association within the SERPIN protein family, which includes C1 inhibitor (SERPING1), a protein related to the pathway ecallantide acts on. This is a statistical link, not a demonstrated biological one.

Mechanistically, the link is weak. Ecallantide inhibits kallikrein, but it does not correct serpin misfolding or polymerization, which is the core problem in serpinopathies. No demonstrated mechanistic rationale exists for this use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125277 | Kalbitor (Takeda Pharmaceuticals America, Inc.) | Injection, solution | Not listed in the data compiled for this report |

The US market status is Marketed, with 1 valid licence on record. The product is an injectable.

## Safety Considerations

Please refer to the package insert for safety information.

One theoretical point from the pathway biology: ecallantide acts on the contact/kallikrein system and can prolong aPTT. This is a general concern for any use in settings involving active bleeding or an acutely ill population, and it has not been characterized for this predicted indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (0.9999). There are no clinical trials, no literature, and no plausible mechanistic rationale, since ecallantide does not address serpin misfolding or polymerization.

**To proceed, the following is needed:**
- A defined mechanistic hypothesis showing how kallikrein inhibition could affect serpin polymerization pathology
- Preclinical or in vitro data testing that hypothesis
- Mechanism of action data and package insert warnings and contraindications to support a safety review
- Route-of-administration feasibility assessment for the target disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "Confirmation of current US availability, since the only license (BLA125277) is cancelled" | No longer present after the report was regenerated (2026-11-12: the report was regenerated in 2026-11 and no longer contains this statement; was: Corrected) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

