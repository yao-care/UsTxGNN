---
layout: default
title: Lusutrombopag
parent: Model Prediction Only (L5)
nav_order: 880
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "LUSUTROMBOPAG"
predicted_indications: ["hereditary thrombocytopenia with normal platelets", "marcothrombocytopenia with mitral valve insufficiency", "transient neonatal thrombocytopenia", "dense granule disease", "platelet storage pool deficiency", "amyotrophic lateral sclerosis", "lower motor neuron syndrome with late-adult onset", "bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia"]
description: "Lusutrombopag: predicted new indication Hereditary thrombocytopenia with normal platelets (evidence level L5). Approved use: Not recorded in the local data"
---

# Lusutrombopag
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Lusutrombopag: Hereditary thrombocytopenia with normal platelets
{: .text-alpha }

## One-Sentence Summary

Lusutrombopag is an oral thrombopoietin (TPO) receptor agonist, originally used to treat thrombocytopenia.
The TxGNN model predicts it may be effective for **hereditary thrombocytopenia with normal platelets**,
but **no clinical trials or publications** were found in the data compiled for this report, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hereditary thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, lusutrombopag is a TPO receptor (c-Mpl) agonist. Its efficacy in thrombocytopenia has been established in patients with chronic liver disease undergoing procedures, and mechanistically it may be applicable to inherited thrombocytopenias.

Stimulating megakaryocyte production through the TPO receptor could plausibly raise platelet counts in inherited thrombocytopenias where megakaryocytes can still respond. This is the link between the original and predicted indications.

There are several caveats:
- The genetic causes of inherited thrombocytopenia are heterogeneous, so a TPO receptor agonist may not work across all of them.
- The disease name "with normal platelets" contradicts the concept of thrombocytopenia. The ontology entry should be checked before any further work.
- No trials or literature were found to support the prediction.

### Other Predictions from the Model

The model also returned nine other predictions, all at evidence level L5 with no trials or literature. All are rated Hold.

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Macrothrombocytopenia with mitral valve insufficiency | 1.0000 | Link is only the shared low-platelet feature. The drug would not address the valve component, and the entry may be an ontology artifact. |
| 3 | Transient neonatal thrombocytopenia | 1.0000 | Theoretically plausible, but the condition resolves on its own. Neonatal and pediatric safety is not established. |
| 4 | Dense granule disease | 1.0000 | This is mainly a platelet function defect, not a count defect. Benefit is likely limited and thrombotic risk is a concern. |
| 5 | Platelet storage pool deficiency | 0.9996 | A qualitative platelet disorder that is unlikely to respond to a higher platelet count alone. |
| 6 | Amyotrophic lateral sclerosis | 0.9995 | No plausible link between TPO receptor agonism and motor neuron degeneration. |
| 7 | Lower motor neuron syndrome with late-adult onset | 0.9995 | No recognized link to the TPO pathway. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| 9 | Bilateral parasagittal parieto-occipital polymicrogyria | 0.9995 | A developmental cortical malformation. The drug has no plausible effect. |
| 10 | Axial spondylometaphyseal dysplasia | 0.9995 | A skeletal dysplasia with no relation to TPO signaling. Likely a computational artifact. |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA210923 | MULPLETA | VANCOCIN ITALIA | Tablet; oral | Valid |

<!-- licenses:end -->

This limits practical access.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interactions, and the 20 listed in the data are all rated Moderate. They include:
  - Antibiotics: clarithromycin, azithromycin, fidaxomicin
  - Steroid and hormone: hydrocortisone, testosterone
  - Cardiovascular and lipid agents: amiodarone, nifedipine, simvastatin
  - Others: cobicistat, atazanavir, abiraterone, afatinib, alpelisib, cabozantinib, eliglustat, rolapitant, lidocaine, apremilast, tolbutamide, ginger

  Many of these are enzyme or transporter interactors, so combined use needs review.

Please refer to the package insert for warnings and contraindications. That label information was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials or literature (L5). Label safety data and mechanism data are also missing.

<!-- review:begin us-lic-20261031-lusutrombopag-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The disease name is internally inconsistent, and the only US authorization is cancelled. Label safety data and mechanism data are also missing." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-lusutrombopag-1 -->

**To proceed, the following is needed:**
- Retrieve the FDA package insert warnings and contraindications, which block safety screening
- Obtain detailed mechanism of action data
- Check the predicted disease entry against the ontology and clarify the "with normal platelets" wording
- Search for preclinical or clinical evidence in inherited thrombocytopenias, and define which genetic subtypes could respond
- Assess safety in pediatric and neonatal populations if that direction is pursued
- Confirm whether the drug can be obtained

<!-- review:begin us-lic-20261106-lusutrombopag-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Confirm whether the drug can be obtained, given the cancelled US authorization" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-lusutrombopag-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The disease name is internally inconsistent, and the only US authorization is cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "given the cancelled US authorization" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

