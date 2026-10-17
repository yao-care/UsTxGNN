---
layout: default
title: Cemiplimab
parent: Model Prediction Only (L5)
nav_order: 511
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cemiplimab: predicted new indication Gallbladder adenosquamous carcinoma (evidence level L5). Approved use: Squamous cell carcinoma"
monitor_inn: "CEMIPLIMAB"
predicted_indications: ["gallbladder adenosquamous carcinoma", "rectal cloacogenic carcinoma", "external ear basal cell carcinoma", "adenosquamous prostate carcinoma", "urethral verrucous carcinoma", "pancreatic adenosquamous carcinoma"]
---

# Cemiplimab
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

# Cemiplimab: From Squamous Cell Carcinoma to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab is a PD-1 blocking antibody, originally used to treat squamous cell carcinoma (specifically cutaneous squamous cell carcinoma).
The TxGNN model predicts it may be effective for **gallbladder adenosquamous carcinoma**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Squamous cell carcinoma |
| Predicted New Indication | Gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single BLA on record is listed as cancelled) |
| Number of NDAs | 1 (BLA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cemiplimab (LIBTAYO) is a monoclonal antibody that targets human PD-1 (PDCD1, CD279). It blocks the PD-1/PD-L1 interaction with an IC50 below 1 nM in an ELISA, which releases the brake on T-cell activity against tumour cells. A formal mechanism-of-action entry was not available in the data compiled for this report, but the target and binding activity are well described in the pharmacology data.

The FDA authorised cemiplimab in September 2018 for metastatic or locally advanced cutaneous squamous cell carcinoma that cannot be treated with surgery or radiotherapy. In the early trials, about 50% of patients with advanced disease responded, and 82% of responders with metastatic disease had durable responses. The approval was later expanded to first-line PD-L1-high non-small cell lung cancer (February 2021) and to adjuvant treatment of cutaneous squamous cell carcinoma (October 2025).

The predicted indication, gallbladder adenosquamous carcinoma, contains a squamous component, so PD-1 blockade could plausibly act on it. However, this link rests only on shared squamous histology and the model score. No trial or publication was provided for this disease, and the similarity to the original indication has not yet been assessed.

### Other Top Predictions

The model produced nine other high-scoring predictions, all with scores around 99.99%. Only one has any supporting literature.

| Rank | Predicted Indication | Evidence Level | Comment |
|---|---|---|---|
| 2 | Glottis squamous cell carcinoma | L5 | Head and neck squamous cancers respond to PD-1 blockade as a class; no cemiplimab-specific data |
| 3 | Rectal cloacogenic carcinoma | L5 | Squamous features; PD-1 blockade explored in anal squamous carcinoma |
| 4 | External ear basal cell carcinoma | L4 | One case report; the most supported of the ten |
| 5 | Adenosquamous prostate carcinoma | L5 | Prostate cancer generally responds poorly to PD-1 blockade |
| 6 | Urethral verrucous carcinoma | L5 | Usually treated surgically; weak rationale |
| 7 | Lung occult squamous cell carcinoma | L5 | Class activity in squamous NSCLC; no data for the occult setting |
| 8 | Pancreatic adenosquamous carcinoma | L5 | Immunosuppressive microenvironment; weak rationale |
| 9 | Non-keratinizing sinonasal squamous cell carcinoma | L5 | Shares biology with head and neck squamous cancer |
| 10 | Supraglottis squamous cell carcinoma | L5 | Laryngeal subsite of head and neck squamous cancer |

## Clinical Trial Evidence

Currently no related clinical trials registered for gallbladder adenosquamous carcinoma.

## Literature Evidence

Currently no related literature available for gallbladder adenosquamous carcinoma.

For reference, the one publication supplied for another predicted indication (external ear basal cell carcinoma, rank 4) is:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34157152](https://pubmed.ncbi.nlm.nih.gov/34157152/) | 2021 | Case report | Clinical and Experimental Dermatology | Lasting response after cemiplimab was discontinued in a patient with locally advanced basal cell carcinoma |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761097 | LIBTAYO | Injection | Not listed in the data compiled; the record shows the authorization as cancelled (manufacturer: Regeneron Pharmaceuticals, Inc.) |

The cancelled status in this record conflicts with the pharmacology data, which describe FDA approval in 2018 with expansions in 2021 and 2025. The current marketing status should be confirmed against the FDA database before any decision is made.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-1 checkpoint inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: Ten interaction records were found. Nine are rated Moderate and involve corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone and deflazacort. The tenth is a pharmacology record for the PD-1 target itself, with no severity level.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for gallbladder adenosquamous carcinoma has no trials or literature behind it (Evidence Level L5). Its only support is the model score and shared squamous histology. The label-level safety data and the market status record are also incomplete or inconsistent.

**To proceed, the following is needed:**
- Search for cemiplimab or other PD-1 inhibitor studies in gallbladder, biliary and adenosquamous tumours
- Obtain the FDA package insert to complete warnings and contraindications (a blocking gap for safety screening)
- Confirm the current US marketing status of LIBTAYO (BLA761097), since the record shows it as cancelled
- Obtain formal mechanism-of-action data and assess the similarity between the original and predicted indications
- Consider whether external ear basal cell carcinoma (rank 4, L4) is a better candidate to evaluate first, given its supporting case report. Pivotal basal cell carcinoma data outside this data set should also be reviewed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

