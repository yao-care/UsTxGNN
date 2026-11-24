---
layout: default
title: Lithium Carbonate
parent: Model Prediction Only (L5)
nav_order: 865
evidence_level: L5
indication_count: 10
monitor_inn: "LITHIUM CARBONATE"
predicted_indications: ["pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "myosclerosis", "brachyolmia-amelogenesis imperfecta syndrome", "brachydactyly-syndactyly syndrome", "Behr syndrome", "WHIM syndrome", "combined immunodeficiency due to moesin deficiency"]
last_modified_at: 2026-11-24
description: "Lithium Carbonate: predicted new indication Pseudoachondroplasia (evidence level L5). In the US: 36 FDA applications (13 active), plus 71 OTC monograph/unapproved NDC listings"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Lithium Carbonate: Pseudoachondroplasia
{: .text-alpha }

## One-Sentence Summary

Lithium carbonate is a mood stabilizer, originally used for bipolar disorder and related affective disorders, and the TxGNN model (deep learning) also predicts it for several arthropathies; these predictions may reflect similarities the model learned between related diseases, not biological evidence.
The TxGNN model predicts it may be effective for **Pseudoachondroplasia**, a rare skeletal dysplasia, but **0 clinical trials** and **0 publications** currently support this direction.
This is a model-only prediction with no direct supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 13 of 36; OTC monograph / unapproved listings: 71) |
| Number of FDA Applications | 36 (active: 13) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for lithium carbonate: "The mechanism of action of lithium as a mood stabilizing agent is unknown." ([DailyMed: Lithium Carbonate Lithium Carbonate (lithium carbonate) prescribing information, Alembic Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ca2b977-b94c-4232-9b7e-835db97c9544), label version 2022-11-03; accessed 2026-11-19.) Based on general pharmacology, lithium inhibits GSK-3β and modulates Wnt/β-catenin signalling. This pathway influences chondrocyte differentiation and skeletal cell stress responses.

Pseudoachondroplasia is caused by COMP mutations, which lead to endoplasmic reticulum stress in chondrocytes and defects in the extracellular matrix. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the arthropathies associated with lithium (rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy) and skeletal disorders, not biological evidence.

No direct evidence connects lithium to COMP-related pathology, so the mechanistic rationale is speculative.

**Other predictions of note:** The other top-ranked predictions are also model-only, with scores from 0.9929 to 0.9996. They include acromesomelic dysplasia (Hunter-Thompson type), brachyolmia, myosclerosis, Behr syndrome, WHIM syndrome and moesin-deficiency immunodeficiency. Only brachyolmia-amelogenesis imperfecta syndrome has an associated paper, and it is a general review with no lithium-specific data. Lithium's known teratogenicity concern argues for caution in the developmental skeletal conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for pseudoachondroplasia.

---

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA076691 | LITHIUM CARBONATE | HIKMA | Tablet, extended release; oral | Valid |
| ANDA076832 | LITHIUM CARBONATE | HIKMA | Tablet, extended release; oral | Valid |
| ANDA079139 | LITHIUM CARBONATE | GLENMARK PHARMS LTD | Capsule; oral | Valid |
| ANDA079159 | LITHIUM CARBONATE | ALEMBIC LTD | Capsule; oral | Valid |
| ANDA090702 | LITHIUM CARBONATE | HETERO LABS LTD III | Capsule; oral | Valid |

Showing 5 of 107 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

Cancelled status in this dataset may not reflect actual marketing, so it should be verified against current FDA records.

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lithium Carbonate Lithium Carbonate (lithium carbonate) prescribing information, Alembic Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ca2b977-b94c-4232-9b7e-835db97c9544) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

