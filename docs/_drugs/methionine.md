---
layout: default
title: Methionine
parent: Model Prediction Only (L5)
nav_order: 908
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methionine: predicted new indication Acne (disease) (evidence level L5). Approved use: Not available (the one US listing has no indication text)"
monitor_inn: "METHIONINE"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "nuclear senile cataract", "mature cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "tetanic cataract", "craniostenosis cataract", "diabetic cataract"]
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

# Methionine: From an Unspecified Original Indication to Acne

## One-Sentence Summary

Methionine is an essential sulfur-containing amino acid. Its original approved indication is not recorded in the data compiled for this report, and its only US product listing is cancelled.
The TxGNN model predicts it may be effective for **acne (disease)**, but **no clinical trials** and only **2 indirect publications** (a case report and a cohort study) exist, and neither supports methionine as a treatment.
Evidence for this prediction is model-only (L5), and the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the one US listing has no indication text) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active listing) |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Methionine is a proteinogenic amino acid and a precursor in the methionine-homocysteine cycle, but the data compiled for this report do not describe how it would act on acne.

No direct mechanistic link between methionine and acne is established. The two retrieved papers are indirect:
- One reports that isotretinoin therapy raises plasma homocysteine (a methionine-cycle metabolite) in cystic acne patients. This is a side-effect observation, not a therapeutic signal.
- The other is a neonatal MTHFR mutation case report in which neonatal acne was one of many features. It is unrelated to acne treatment.

The very high TxGNN score is a model prediction only and is not supported by clinical data. Other top-ranked predictions are mostly cataract subtypes and severe nonproliferative diabetic retinopathy, also at L5. The one exception is diabetic cataract, which has indirect preclinical and observational support (L4) and is better framed as a research question than a repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | Int J Dermatol | Plasma homocysteine was elevated in patients on isotretinoin for cystic acne. This is a drug side-effect observation, not evidence of methionine benefit. |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Reports | A neonate with a novel MTHFR mutation had encephalopathy, hair loss, marfanoid features and neonatal acne. The link to acne treatment is indirect. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | L-Methionine High (Professional Complementary Health Formulas), cancelled | Liquid | Not available |

## Safety Considerations

- **Disease contraindications from the knowledge graph (not label text):** the TxGNN knowledge graph links methionine to contraindications in several disease groups:
  - Cardiovascular: hypertension, heart disease, cardiovascular disease, hyperlipidemia (including familial), ventricular fibrillation, digitalis poisoning
  - Renal: kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, phenylketonuria and other disorders of phenylalanine metabolism, phosphorus metabolism disease
  - Calcium-related: hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis
- **Drug interactions** (5 recorded):
  - Moderate: activated charcoal
  - Minor: ephedrine, pseudoephedrine, mexiletine, flecainide
- **Homocysteine concern:** supplementation could in principle raise homocysteine, which is associated with vascular disease. This is especially relevant given the cardiovascular contraindications listed above.

Please refer to the package insert for label-based warnings and contraindications; this information was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction rests solely on a model score. There are no clinical trials, and the two retrieved papers do not support methionine as an acne treatment. The drug has no active US listing, and the label-based safety information is missing. The knowledge-graph contraindication signals (cardiovascular, renal, metabolic) call for caution.

**To proceed, the following is needed:**
- Mechanism of action data for methionine and a plausible pathway to acne pathophysiology
- FDA package insert warnings and contraindications (blocking gap for safety screening)
- The original approved indication and current regulatory status
- Preclinical or clinical studies directly testing methionine in acne
- A homocysteine and cardiovascular safety assessment if the work advances
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

