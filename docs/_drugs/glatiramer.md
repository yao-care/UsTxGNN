---
layout: default
title: Glatiramer
parent: Model Prediction Only (L5)
nav_order: 752
evidence_level: L5
indication_count: 1
---

# Glatiramer
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

# Glatiramer: From Multiple Sclerosis to Hemoglobinopathy

## One-Sentence Summary

Glatiramer is an injectable immunomodulator used in multiple sclerosis.
The TxGNN model predicts it may be effective for **hemoglobinopathy**, but there are currently **0 clinical trials** and only **1 publication** (a case report that does not test this idea), so this is a model prediction without real supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (the US license records provided contain no indication text; this comes from the prediction rationale) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 16 (the five listed below are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Glatiramer is generally understood to mimic myelin basic protein and shift T-cell responses toward Th2/regulatory phenotypes. That explains its use in multiple sclerosis, an immune-mediated disease.

Hemoglobinopathies such as sickle cell disease and thalassemia are inherited disorders of globin production or structure. Glatiramer has no plausible disease-modifying target in them, so **no direct mechanistic link is supported**. The only speculative connection is to immune-mediated complications, such as autoimmune hemolysis or alloimmunization.

The high TxGNN score (0.990) is a computational output only. It should not be read as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Case report | Revue neurologique | A 35-year-old woman with multiple sclerosis and a history of beta thalassemia, bulimia and asthma developed multiple immune disorders after stopping natalizumab. She had previously received first-line subcutaneous immunomodulatory treatments. The report does not evaluate glatiramer as a treatment for hemoglobinopathy. |

## US Market Information

The license records provided contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA208468 | Glatiramer Acetate | Injection, solution | Zydus Pharmaceuticals USA Inc. |
| ANDA208468 | Glatiramer Acetate | Injection, solution | Italfarmaco SpA |
| ANDA090218 | Glatopa | Injection, solution | Sandoz Inc |
| ANDA091646 | Glatiramer Acetate | Injection, solution | Mylan Pharmaceuticals Inc. |
| ANDA090218 | Glatopa | Injection, solution | Bryant Ranch Prepack |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no registered trials, the only publication is an unrelated case report, and there is no plausible mechanism linking glatiramer to globin disorders.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data from DrugBank
- A specific, testable hypothesis, such as an immune-mediated complication of hemoglobinopathy
- A targeted literature search for preclinical or clinical data in sickle cell disease or thalassemia
- A check of route compatibility (glatiramer is injectable only) against the intended use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

