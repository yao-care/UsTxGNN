---
layout: default
title: Undecylenic Acid
parent: Model Prediction Only (L5)
nav_order: 1275
evidence_level: L5
indication_count: 7
---

# Undecylenic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Undecylenic Acid: From Topical Antifungal Use to Dermatophytosis of Groin and Perianal Area

## One-Sentence Summary

Undecylenic acid is a topical fatty-acid antifungal marketed in the US in over-the-counter (OTC) liquid, cream, spray and paste products, though no labeled indication text was supplied.
The TxGNN model predicts it may be effective for **dermatophytosis of groin and perianal area (tinea cruris)**, but **no clinical trials and no relevant publications** currently support this prediction.
The support is a model score plus mechanistic plausibility only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided (the licenses carry no indication text; product names suggest topical antifungal use) |
| Predicted New Indication | Dermatophytosis of groin and perianal area |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (the five shown are OTC monograph entries, not NDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Undecylenic acid is generally described as a topical antifungal fatty acid that inhibits fungal hyphal morphogenesis and disrupts fungal membranes. This general description is not backed by a sourced MOA record in the supplied data.

Tinea cruris is a dermatophyte infection of non-follicular, glabrous skin in the groin. That is the kind of site where a topical antifungal can reach the organism, so the prediction is mechanistically plausible.

There is a caveat. OTC antifungal labeling for tinea cruris may already exist for this drug, which would make this an on-label use rather than true repurposing. The supplied data do not show the label, so this must be checked.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The licenses supplied carry no approved-indication text, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M005 | ViLLsure Antifungal Pen | Liquid | Jiangxi Yudexi Pharmaceutical Co., LTD |
| M005 | Myco Nail A Antifungal Solution | Liquid | Kramer Novis |
| part333C | CVS Pharmacy | Liquid | CVS Pharmacy |
| M005 | Noorish Foot Co. Anti-Fungal Pen | Liquid | Noorish Foot Co. LLC |
| M005 | NAIL REPAIR PEN | Liquid | Yunqi Cosmetics (Shenzhen) Co., Ltd |

Other dosage forms on the market include cream, spray and paste.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high TxGNN score (99.94%) and a plausible topical antifungal mechanism, with no trials or relevant literature (L5). Package-insert safety data and a sourced MOA are also missing. The other six predictions in the pack are weaker:
- Deep or hair-invasive infections (Majocchi granuloma, ectothrix and endothrix disease, scalp or beard dermatophytosis) are unlikely to respond to topical therapy.
- The 20 "literature" hits for scalp or beard dermatophytosis are keyword artifacts on "beard" and do not address this drug.
- Pityriasis versicolor (a Malassezia infection) has no supporting data.
- Superficial mycosis has one indirect onychomycosis formulation paper (PMID 28906086), which is why that prediction is graded L4.

**To proceed, the following is needed:**
- Check the current OTC label to see whether tinea cruris is already an approved use.
- Obtain the package-insert warnings and contraindications.
- Obtain a sourced mechanism of action from DrugBank.
- Run a targeted literature search on undecylenic acid and tinea cruris or dermatophytosis, then check the full text of PMID 28906086.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

