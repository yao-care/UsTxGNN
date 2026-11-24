---
layout: default
title: Alpelisib
parent: Model Prediction Only (L5)
nav_order: 227
evidence_level: L5
indication_count: 1
monitor_inn: "ALPELISIB"
predicted_indications: ["pulmonary hypertension"]
last_modified_at: 2026-11-24
description: "Alpelisib: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not listed in the data compiled for this report (the product names PI…"
---

# Alpelisib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Alpelisib: From Breast Cancer / PIK3CA-Related Disorders to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Alpelisib is a PI3K-alpha inhibitor marketed in the US as PIQRAY and VIJOICE. The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **0 clinical trials** and only **1 publication** (a case report describing a lung adverse effect, not a benefit). The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data compiled for this report (the product names PIQRAY and VIJOICE are associated with breast cancer and PIK3CA-related overgrowth disorders, respectively) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 3 of 3) |
| Number of FDA Applications | 3 (active: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for alpelisib: "Alpelisib is an inhibitor of phosphatidylinositol-3-kinase (PI3K) with inhibitory activity predominantly against PI3Kα. Gain-of-function mutations in the gene encoding the catalytic α-subunit of PI3K (PIK3CA) lead to activation of PI3Kα and Akt-signaling, cellular transformation and the generation of tumors in in vitro and in vivo models." ([DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b), label version 2026-10-28; accessed 2026-11-19.) Alpelisib is known to be a PI3K-alpha inhibitor, and the PI3K/AKT/mTOR pathway is biologically implicated in pulmonary vascular remodeling, particularly the proliferation of pulmonary artery smooth muscle cells. This offers a plausible theoretical link between the drug and pulmonary hypertension.

However, this link is not supported by any evidence in the data compiled. The only publication retrieved (PMID 35730191) is a case report of alpelisib-induced interstitial lung disease in a patient with advanced breast cancer. It describes a pulmonary adverse effect rather than a therapeutic benefit, and it concerns interstitial lung disease rather than pulmonary hypertension. If anything, it is a lung safety signal.

The TxGNN score is very high (0.9903), but it is a model-based prediction only, and the relationship between the original indications and pulmonary hypertension has not been established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case report | Journal of Oncology Pharmacy Practice | Alpelisib-induced interstitial lung disease in a patient with advanced breast cancer. This is an adverse-effect report, not evidence of benefit in pulmonary hypertension. |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA212526 | PIQRAY | NOVARTIS | Tablet; oral | Valid |
| NDA215039 | VIJOICE | NOVARTIS | Tablet; oral | Valid |
| NDA218466 | VIJOICE | NOVARTIS | Granule; oral | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3K-alpha inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified, and the 20 shown in the data compiled are all Moderate level. Most involve glucose-lowering drugs, which fits with alpelisib's known effect on glucose metabolism. They include:
  - Acarbose, acetohexamide, chlorpropamide, glimepiride, glipizide
  - Metformin, pioglitazone, alogliptin
  - Albiglutide, dulaglutide, exenatide
  - Canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Others: alosetron, bupropion, dexamethasone, dronabinol, fidaxomicin
- **Lung safety signal**: The only retrieved publication reports alpelisib-induced interstitial lung disease. This is relevant when considering use in patients with existing lung disease.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials, and the sole publication is a case report of a lung adverse effect rather than a benefit. The drug is marketed, with all three US NDAs valid, and label-based safety data is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed before safety screening can proceed
- Detailed mechanism-of-action data from DrugBank
- Preclinical evidence on PI3K-alpha inhibition in pulmonary hypertension models
- Evaluation of the interstitial lung disease signal and whether it conflicts with use in pulmonary disease
- Confirmation of the original approved indications

<!-- review:begin us-lic-20261106-alpelisib-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Confirmation of the original approved indications and the reasons for the NDA cancellations" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-alpelisib-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "and the reasons for the NDA cancellations" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

