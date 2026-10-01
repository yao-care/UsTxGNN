---
layout: default
title: Valsartan
parent: Moderate Evidence (L3-L4)
nav_order: 1282
evidence_level: L4
indication_count: 7
---

# Valsartan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Valsartan: From an Angiotensin Receptor Blocker to Malignant Renovascular Hypertension

## One-Sentence Summary

Valsartan is a marketed angiotensin II type 1 (AT1) receptor blocker. The input data does not list its original approved indication.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but the evidence is thin: **0 clinical trials** and **1 preclinical publication** support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available data (US license records contain no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (NDA and ANDA combined) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Valsartan is an AT1 receptor blocker, a class that acts on the renin-angiotensin system (RAS).

Malignant renovascular hypertension is strongly driven by RAS activation, with elevated angiotensin II. Blocking the AT1 receptor is therefore biologically plausible. The only supporting article is an animal study. It reports that AT1 receptor blockade prevented lethal malignant hypertension and was linked to reduced kidney inflammation. That finding applies to the drug class, not to valsartan specifically or to human patients.

The original indication and mechanism fields in the input are empty, so the link between the old and new indications cannot be assessed directly. The prediction is mechanistically reasonable but clinically unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Preclinical (animal model) | Circulation | AT1 receptor blockade prevented lethal malignant hypertension, linked to reduced kidney inflammation. The effect was tested even without a blood pressure-lowering effect. |

## US Market Information

The US license records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA203311 | Valsartan | Tablet, film coated | Proficient Rx LP |
| ANDA203311 | Valsartan | Tablet, film coated | AvPAK |
| ANDA204821 | Valsartan | Tablet | A-S Medication Solutions |
| NDA021283 | Diovan | Tablet | Novartis Pharmaceuticals Corporation |
| ANDA203311 | Valsartan | Tablet, film coated | Bryant Ranch Prepack |

Records show 20 licenses in total; the five above are shown. Forms on record are oral tablets and a solution.

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found for this drug in the data retrieved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but the only supporting evidence is one preclinical study of the drug class, with no clinical trials. The package insert safety data and mechanism data are also missing, so the candidate stays a research question.

Six other candidates were also predicted:
- Malignant hypertensive renal disease: its only article studies avosentan, a different drug.
- Chronic pulmonary heart disease: indirect evidence from heart failure trials, mostly of sacubitril/valsartan.
- Pulmonary hypertension (two entries), Braddock syndrome and Prinzmetal angina: no meaningful supporting evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, parsed from the FDA label, to allow safety screening
- Mechanism of action data from DrugBank
- Approved indication text, to define the original indication
- Human clinical evidence for valsartan in malignant renovascular hypertension, such as case series or trials
- Review of relevance for the retrieved article, which is still marked pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

