---
layout: default
title: Alpelisib
parent: Model Prediction Only (L5)
nav_order: 227
evidence_level: L5
indication_count: 1
monitor_inn: "ALPELISIB"
predicted_indications: ["pulmonary hypertension"]
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Alpelisib: From Breast Cancer / PIK3CA-Related Disorders to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib is a PI3K-alpha inhibitor marketed in the US as PIQRAY and VIJOICE. The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **0 clinical trials** and only **1 publication** (a case report describing a lung adverse effect, not a benefit). The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data compiled for this report (the product names PIQRAY and VIJOICE are associated with breast cancer and PIK3CA-related overgrowth disorders, respectively) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 3 NDAs are cancelled) |
| Number of NDAs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Alpelisib is known to be a PI3K-alpha inhibitor, and the PI3K/AKT/mTOR pathway is biologically implicated in pulmonary vascular remodeling, particularly the proliferation of pulmonary artery smooth muscle cells. This offers a plausible theoretical link between the drug and pulmonary hypertension.

However, this link is not supported by any evidence in the data compiled. The only publication retrieved (PMID 35730191) is a case report of alpelisib-induced interstitial lung disease in a patient with advanced breast cancer. It describes a pulmonary adverse effect rather than a therapeutic benefit, and it concerns interstitial lung disease rather than pulmonary hypertension. If anything, it is a lung safety signal.

The TxGNN score is very high (0.990), but it is a model-based prediction only, and the relationship between the original indications and pulmonary hypertension has not been established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case report | Journal of Oncology Pharmacy Practice | Alpelisib-induced interstitial lung disease in a patient with advanced breast cancer. This is an adverse-effect report, not evidence of benefit in pulmonary hypertension. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212526 | PIQRAY (Novartis) | Tablet | Not listed (status: cancelled) |
| NDA218466 | VIJOICE (Novartis) | Granule | Not listed (status: cancelled) |
| NDA215039 | VIJOICE (Novartis) | Tablet | Not listed (status: cancelled) |

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
The prediction is supported only by the model score (L5). There are no clinical trials, and the sole publication is a case report of a lung adverse effect rather than a benefit. All three US NDAs are cancelled, and label-based safety data is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed before safety screening can proceed
- Detailed mechanism-of-action data from DrugBank
- Preclinical evidence on PI3K-alpha inhibition in pulmonary hypertension models
- Evaluation of the interstitial lung disease signal and whether it conflicts with use in pulmonary disease
- Confirmation of the original approved indications and the reasons for the NDA cancellations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

