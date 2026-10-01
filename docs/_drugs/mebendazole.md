---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 889
evidence_level: L5
indication_count: 1
---

# Mebendazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Mebendazole: From Anthelmintic Use to Acne

## One-Sentence Summary

Mebendazole is a benzimidazole anthelmintic (anti-worm drug) marketed in the US as Vermox chewable tablets. The TxGNN model predicts it may be effective for **acne**, but the prediction has **0 clinical trials** and **1 publication** behind it, and that publication does not address acne treatment. This is a model-only prediction (evidence level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (drug class: anthelmintic) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, mebendazole is a benzimidazole anthelmintic that inhibits tubulin polymerization and impairs glucose uptake in parasites. No original indication text is recorded in the input, so the link between the original and new indication cannot be assessed from the data provided.

Acne involves excess sebum production, follicular hyperkeratinization, *Cutibacterium acnes* colonization and inflammation. Any connection to mebendazole would rest on speculative anti-inflammatory or antiproliferative effects of tubulin inhibition. No preclinical or clinical data in this dataset support that idea.

The high TxGNN score (0.992) is a model output only, and nothing in this dataset corroborates it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case report | Am J Trop Med Hyg | Report of human proliferative sparganosis (a tapeworm larval infection) in Venezuela. The patient had acne-like skin lesions as one symptom. This is not a study of acne treatment and does not support the prediction. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA208398 | VERMOX | Chewable tablet (oral) | Janssen Pharmaceuticals, Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no registered trials, the single publication is an unrelated case report, and no mechanistic link to acne is established. Basic safety and mechanism data are also missing from the record.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking item for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence that tubulin inhibition or another mechanism affects acne pathways (sebum, keratinization, inflammation)
- Assessment of route compatibility (the only US form is oral; a suitable route for acne is not yet defined)
- Any clinical or observational data on mebendazole in acne

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

