---
layout: default
title: Methazolamide
parent: Model Prediction Only (L5)
nav_order: 907
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "METHAZOLAMIDE"
predicted_indications: ["congestive heart failure", "acute pulmonary heart disease"]
description: "Methazolamide: predicted new indication Congestive heart failure (evidence level L5). Approved use: Not recorded in the local data"
---

# Methazolamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Methazolamide: Congestive heart failure
{: .text-alpha }

## One-Sentence Summary

Methazolamide is a carbonic anhydrase inhibitor originally used to treat open-angle and angle-closure glaucoma.
but currently there are **0 clinical trials** and **0 publications** specific to this indication. The prediction rests on model score and mechanistic similarity alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congestive heart failure |
| TxGNN Prediction Score | 0.9943 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 4 of 4) |
| Number of FDA Applications | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, methazolamide is a carbonic anhydrase inhibitor. It lowers intraocular pressure by reducing aqueous humor secretion, and its efficacy in open-angle and angle-closure glaucoma is established.

However, this is an extension within the same drug class and disease family rather than a true repurposing.

Pediatric and congenital glaucoma generally depend on surgery. Systemic carbonic anhydrase inhibitors are mostly a bridging therapy in these cases.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

For context, the second-ranked prediction (congestive heart failure, score 0.9943) has some literature. It is preclinical or review-level only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38450431](https://pubmed.ncbi.nlm.nih.gov/38450431/) | 2024 | Review | Expert Opin Drug Metab Toxicol | Review of drug interactions of carbonic anhydrase inhibitors and activators |
| [35043173](https://pubmed.ncbi.nlm.nih.gov/35043173/) | 2022 | Preclinical | Diabetes | Methazolamide attenuated diabetic cardiomyopathy in type 1 diabetic mice via β-catenin degradation |
| [17124262](https://pubmed.ncbi.nlm.nih.gov/17124262/) | 2007 | Preclinical | J Physiol | Carbonic anhydrase inhibition prevented and reversed cardiomyocyte hypertrophy |
| [16634001](https://pubmed.ncbi.nlm.nih.gov/16634001/) | 2006 | Review | G Ital Nefrol | Diuretic therapy in heart failure, including carbonic anhydrase inhibitors |
| [14172002](https://pubmed.ncbi.nlm.nih.gov/14172002/) | 1964 | Review | Am Heart J | Historical review of diuretic therapy |

There are no clinical trials for heart failure. The third prediction (acute pulmonary heart disease, 0.9928) has no trials or literature.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA207438 (Bausch & Lomb) | Methazolamide | Tablet | Not available; status: cancelled |
| ANDA040001 (Bryant Ranch Prepack) | Methazolamide | Tablet | Not available; status: cancelled |
| ANDA217408 (Ajanta Pharma USA) | Methazolamide | Tablet | Not available; status: cancelled |
| ANDA215615 (Precision Dose) | Methazolamide | Tablet | Not available; status: cancelled |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded; the first 20 retrieved include:
  - **Major**: metformin, acetylsalicylic acid (aspirin)
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone), diabetes drugs (acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, saxagliptin), amphotericin B (including lipid complex), and laxatives or bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol)
  - **Minor**: doxycycline

Package insert warnings and contraindications could not be retrieved. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a mechanistic extension of methazolamide's existing glaucoma use. No trials or literature support it specifically, and the evidence level is L4. The heart failure and acute pulmonary heart disease predictions are research questions only, supported by preclinical or no data.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clinical or observational data on carbonic anhydrase inhibitors in hereditary or congenital glaucoma
- Review of the knowledge-graph contraindications (for example renal, hepatic, diabetic and adrenal conditions) against the target population
- Confirmation of whether any methazolamide product remains available in the US market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

