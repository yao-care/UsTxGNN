---
layout: default
title: Methionine
parent: Model Prediction Only (L5)
nav_order: 908
evidence_level: L5
indication_count: 10
monitor_inn: "METHIONINE"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "nuclear senile cataract", "mature cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "tetanic cataract", "craniostenosis cataract", "diabetic cataract"]
last_modified_at: 2026-10-30
description: "Methionine: predicted new indication Acne (disease) (evidence level L5). Approved use: No approved indication text available in the data compiled for this r…"
---

# Methionine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Methionine: From an Unlabeled Marketed Product to Acne (Disease)
{: .text-alpha }

## One-Sentence Summary

Methionine is an essential sulfur-containing amino acid. The data compiled for this report contain no approved indication text for the single US product listed.
The TxGNN model predicts it may be effective for **acne (disease)**, but there are **0 clinical trials** and only **2 publications** (a case report and a cohort study) that touch on this prediction indirectly, so the evidence is limited to the model prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text available in the data compiled for this report |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Number of approvals | 1 license (listed as a single-ingredient product; the license number is not recorded) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Methionine is known to be an amino acid that feeds into homocysteine and one-carbon metabolism, but the data compiled for this report do not describe how it would act on acne.

The two retrieved papers do not support the prediction directly. One reports elevated plasma homocysteine in patients taking isotretinoin for cystic acne, and the other is a case report of an MTHFR mutation in a neonate with encephalopathy, in which neonatal acne was one of several skin findings. Both touch on methionine/homocysteine metabolism but neither addresses acne pathogenesis or treatment with methionine. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No mechanistic link to acne has been established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | International Journal of Dermatology | Plasma homocysteine was elevated in patients receiving isotretinoin for cystic acne; this is a drug side-effect observation, not a test of methionine as a treatment |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Reports | A neonate with a novel MTHFR mutation had encephalopathy, hair loss, marfanoid features and neonatal acne; acne was incidental |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not recorded | L-Methionine High (Professional Complementary Health Formulas) | Liquid | Not stated |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links methionine to a number of conditions as contraindications. These are graph relations, not confirmed label contraindications. They include:
  - Cardiovascular and metabolic: hypertension, heart disease, cardiovascular disease, hyperlipidemia, familial hyperlipidemia, diabetes mellitus, diabetic ketoacidosis, digitalis poisoning, ventricular fibrillation
  - Kidney: kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
  - Calcium and phosphorus: hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease
  - Amino acid metabolism: phenylketonuria and other disorders of phenylalanine metabolism
- **Drug Interactions** (5 recorded, from DDInter):
  - Activated charcoal: Moderate
  - Ephedrine, pseudoephedrine, mexiletine and flecainide: Minor

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trial or publication tests methionine in acne, and the two retrieved papers are only tangentially related through homocysteine metabolism. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data linking methionine to acne biology
- Label text (indications, warnings, contraindications) for the marketed product
- Preclinical or early clinical studies that directly address methionine in acne
- A safety review of homocysteine elevation and the knowledge-graph contraindication relations, especially cardiovascular and renal conditions

---

### Supplementary Note: Other Predicted Indications

The data also list nine further predictions (e.g., severe nonproliferative diabetic retinopathy, several cataract subtypes). Of these, diabetic cataract has the strongest indirect rationale. Methionine sulfoxide reductase B1 protects lens epithelial cells from high-glucose-induced and peroxynitrite-induced damage in laboratory studies. However, none of the papers studies diabetic cataract with methionine treatment, so its evidence level also remains L5 under the direct-study requirement. No interventional trials exist for any of these indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

