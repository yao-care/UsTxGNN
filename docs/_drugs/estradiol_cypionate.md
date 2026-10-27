---
layout: default
title: Estradiol Cypionate
parent: Model Prediction Only (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
monitor_inn: "ESTRADIOL CYPIONATE"
predicted_indications: ["symptomatic form of fragile X syndrome in female carrier", "partial trisomy/tetrasomy of the short arm of chromosome 12", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 18", "ovarian remnant syndrome", "anovulation", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "blepharophimosis-epicanthus inversus-ptosis", "partial autosomal trisomy/tetrasomy", "luteoma of pregnancy"]
last_modified_at: 2026-10-14
description: "Estradiol Cypionate: predicted new indication Symptomatic form of fragile X syndrome in female carrier (evidence level L5). Approved use: Primary ovarian failure"
---

# Estradiol Cypionate
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

## Estradiol Cypionate: From Primary Ovarian Failure to Symptomatic Fragile X Syndrome in Female Carriers
{: .text-alpha }

## One-Sentence Summary

Estradiol cypionate is a long-acting injectable estrogen, originally used to treat primary ovarian failure.
The TxGNN model predicts it may be effective for **symptomatic form of fragile X syndrome in female carrier**,
but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary ovarian failure (from the knowledge graph; the US license record has no indication text) |
| Predicted New Indication | Symptomatic form of fragile X syndrome in female carrier |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 (cancelled; the record is an ANDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known pharmacology, estradiol cypionate is an ester of estradiol, given by injection as a long-acting estrogen. It is used to replace estrogen when the ovaries do not produce enough.

Female carriers of an FMR1 premutation can develop fragile X-associated primary ovarian insufficiency (FXPOI). This overlaps directly with the drug's original indication of primary ovarian failure. Estrogen replacement is therefore plausible for the hypoestrogenic manifestations of the condition.

This link is an inference from the original indication and the high TxGNN score, not direct evidence. Estrogen would not be expected to treat other features of fragile X syndrome, such as cognitive or behavioural symptoms. The drug also has no currently valid US license.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top predicted indication. The only literature compiled for this report relates to a lower-ranked prediction, **anovulation** (rank 6), and all of it is animal or formulation research, so it does not support the fragile X prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17491141](https://pubmed.ncbi.nlm.nih.gov/17491141/) | 2007 | Review (veterinary) | Society of Reproduction and Fertility Supplement | Strategies to control follicle growth and synchronize ovulation in dairy cattle (Ovsynch program) |
| [12512597](https://pubmed.ncbi.nlm.nih.gov/12512597/) | 2002 | Animal study | Journal of Dairy Science | Estradiol cypionate (10 mg) extended the postpartum anovulatory period in dairy cows |
| [35150853](https://pubmed.ncbi.nlm.nih.gov/35150853/) | 2022 | Preclinical formulation study | Journal of Equine Veterinary Science | SAIB as a delivery vehicle for estradiol cypionate and sulpiride in geldings and seasonally anovulatory mares |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA085470 (cancelled) | Depo-Estradiol (Pharmacia & Upjohn Company LLC) | Injection | Not stated in the available record |

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not available for this report. Please refer to the package insert for safety information.

The drug-disease knowledge graph lists a number of conditions associated with contraindication or caution for this drug. These come from the graph, not from label text, and should be verified against the official label. They include:

- **Cardiovascular:** hypertension, congestive heart failure
- **Hepatic and renal:** liver disease, liver failure, gallbladder disease, kidney disease
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, hypothyroidism, humoral hypercalcemia of malignancy
- **Neurological and psychiatric:** epilepsy, anxiety disorder, dysthymic disorder, substance abuse/dependence
- **Other:** asthma, systemic lupus erythematosus, osteoporosis, benign prostatic hyperplasia, gynecomastia

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible for the ovarian insufficiency component of fragile X premutation carriers, but it is supported only by a model score. There are no clinical trials or human literature, and the original mechanism data and label safety data are missing. The drug is also cancelled-only in the US market.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are blocking for safety screening
- Mechanism of action data (for example, from DrugBank)
- A literature search on estrogen replacement in FXPOI and FMR1 premutation carriers
- A clear definition of the target outcome (ovarian insufficiency symptoms versus other fragile X features)
- Confirmation of an available marketed estradiol product and route, since this license is cancelled
- Review of the knowledge graph contraindication list against the official label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

