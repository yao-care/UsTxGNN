---
layout: default
title: Lithium Carbonate
parent: Model Prediction Only (L5)
nav_order: 865
evidence_level: L5
indication_count: 10
monitor_inn: "LITHIUM CARBONATE"
predicted_indications: ["pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "myosclerosis", "brachyolmia-amelogenesis imperfecta syndrome", "brachydactyly-syndactyly syndrome", "Behr syndrome", "WHIM syndrome", "combined immunodeficiency due to moesin deficiency"]
---

# Lithium Carbonate
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

# Lithium Carbonate: From Bipolar Disorder to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate is a mood stabiliser, originally used for bipolar disorder and related affective disorders, and the knowledge graph also links it to several arthropathies.
The TxGNN model predicts it may be effective for **Pseudoachondroplasia**, a rare skeletal dysplasia, but **0 clinical trials** and **0 publications** currently support this direction.
This is a model-only prediction with no direct supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bipolar disorder (also major affective disorder, manic bipolar affective disorder, and several arthropathies in the knowledge graph) |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences in the data compiled for this report) |
| Number of NDAs | 10 authorisation records (2 NDAs and 7 ANDAs, plus 1 record without a number) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, lithium inhibits GSK-3β and modulates Wnt/β-catenin signalling. This pathway influences chondrocyte differentiation and skeletal cell stress responses.

Pseudoachondroplasia is caused by COMP mutations, which lead to endoplasmic reticulum stress in chondrocytes and defects in the extracellular matrix. The model's link likely comes from lithium's association with arthropathies (rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy) in the knowledge graph. These share network neighbours with skeletal disorders.

No direct evidence connects lithium to COMP-related pathology, so the mechanistic rationale is speculative.

**Other predictions of note:** The other top-ranked predictions are also model-only, with scores from 99.29% to 99.96%. They include acromesomelic dysplasia (Hunter-Thompson type), brachyolmia, myosclerosis, Behr syndrome, WHIM syndrome and moesin-deficiency immunodeficiency. Only brachyolmia-amelogenesis imperfecta syndrome has an associated paper, and it is a general review with no lithium-specific data. Lithium's known teratogenicity concern argues for caution in the developmental skeletal conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for pseudoachondroplasia.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017812 | Lithium Carbonate (Cardinal Health 107) | Capsule, gelatin coated | Not stated; status cancelled |
| NDA018558 | Lithium Carbonate (Hikma) | Tablet | Not stated; status cancelled |
| ANDA204779 | Lithium Carbonate (RemedyRepack) | Tablet, extended release | Not stated; status cancelled |
| ANDA076832 | Lithium Carbonate (Hikma) | Tablet, extended release | Not stated; status cancelled |
| ANDA079159 | Lithium Carbonate (Alembic) | Capsule | Not stated; status cancelled |

All 10 authorisation records in the data are marked cancelled, with no currently valid single-ingredient or combination licences. Cancelled status in this dataset may not reflect actual marketing, so it should be verified against current FDA records.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (graph-derived, not label text): kidney disease, pyoureter, cognitive disorder, hypothyroidism, myxedema, congenital hypothyroidism, psoriasis, parapsoriasis, sudden cardiac arrest, heart conduction disease, diabetes insipidus (including neurohypophyseal and central forms).
- **Drug interactions:** 100 interactions were identified. Examples are listed below.
  - **Major:** bupropion, lorcaserin.
  - **Moderate:** acarbose, famotidine, albiglutide, alogliptin, metformin, pioglitazone, loperamide, mesalazine, morphine, balsalazide, metronidazole, canagliflozin, chlorpropamide, potassium citrate, clarithromycin.
  - **Minor:** doxycycline, epinephrine, acetylsalicylic acid.
- **Developmental concern:** Lithium is a known teratogenicity concern, which matters for the paediatric and developmental skeletal conditions among the predictions.

Please refer to the package insert for the full warnings and contraindications, which are not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials and no supporting literature. The mechanistic link is speculative, and lithium has a narrow therapeutic index and teratogenicity concerns. The package insert safety data is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, to complete safety screening
- Mechanism of action data, to support a mechanistic link analysis
- Preclinical evidence (for example COMP-mutant chondrocyte or mouse models) testing the effect of lithium or GSK-3β inhibition on ER stress and matrix defects
- A literature review for lithium in skeletal dysplasias and chondrocyte biology
- Confirmation of current US marketing status
- A risk-benefit assessment for a rare, largely paediatric population, given lithium's toxicity profile and teratogenic risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

