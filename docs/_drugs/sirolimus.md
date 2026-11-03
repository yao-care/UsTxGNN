---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 1166
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-03
monitor_inn: "SIROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: predicted new indication Liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Sirolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sirolimus: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sirolimus is an mTOR inhibitor (mTORC1 blocker) marketed in the United States in several oral, topical and solution products.
The TxGNN model predicts it may be effective for **liposarcoma**, with **1 clinical trial** (a single-arm Phase 2 study of a sirolimus combination) and **7 publications** currently linked to this direction, none of which tests sirolimus alone in liposarcoma.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of FDA Applications | at least 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on what is known, sirolimus inhibits mTORC1, a kinase that drives cell growth and survival. Activation of the PI3K/AKT/mTOR pathway has been reported in soft tissue sarcomas, including liposarcoma, and mouse models suggest that mTOR inhibition can slow tumour growth.

This gives a plausible biological rationale for testing sirolimus in liposarcoma. However, the support is indirect. The only trial combines sirolimus with cyclophosphamide, so any effect cannot be attributed to sirolimus alone. The literature is mainly reviews of targeted sarcoma therapy and studies of cancer risk in transplant patients.

Because no study directly addresses sirolimus for liposarcoma as the disease studied, the evidence level is set at L5 (model prediction with only indirect support), even though the model score is high.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre trial of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma. No randomised control, and no results are given in the data compiled. The liposarcoma subgroup size is not stated. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT (secondary analysis) | J Am Soc Nephrol | In adult kidney transplant recipients, sirolimus after early cyclosporine withdrawal reduced cancer risk. This is transplant cancer risk, not liposarcoma treatment. |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapies in soft tissue sarcoma. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of recent trials of molecular-targeted agents in advanced sarcomas. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatments for rare connective tissue tumours and sarcomas. |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | Cancer screening and effects of immunosuppressive drugs in long-term kidney transplant patients. |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Cohort | Fam Cancer | Clinical spectrum of PTEN hamartoma tumor syndrome; indirect relevance. |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Case report | Diagn Pathol | Three fibro-adipose vascular anomaly cases with emphasis on the mTOR pathway. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021110 | Sirolimus (Mylan) | Tablet, sugar coated | Not available |
| NDA213478 | HYFTOR (Nobelpharma America) | Gel | Not available |
| ANDA201676 | Sirolimus (Zydus) | Tablet, film coated | Not available |
| ANDA214753 | Sirolimus (Ascend) | Tablet, film coated | Not available |
| ANDA208691 | Sirolimus (Northstar Rx) | Tablet, film coated | Not available |

These are 5 of the 11 licences on record, and the list may be partial.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; typically blood counts, liver and kidney function, and lipids and glucose |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. Major-level examples include amphotericin B (including the lipid complex), mesalazine, balsalazide and clarithromycin. Moderate-level examples include acarbose, metformin, pioglitazone, several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aprepitant, cimetidine, canagliflozin and dapagliflozin.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only linked trial is a single-arm Phase 2 study of a sirolimus combination, and no study tests sirolimus alone in liposarcoma. The score is high, but the clinical support is indirect, so the evidence is at L5.

**To proceed, the following is needed:**
- Liposarcoma-specific data separating the effect of sirolimus from its combination partner, including the liposarcoma subgroup results of NCT02821507
- Mechanism-of-action data and package insert warnings and contraindications
- A safety monitoring plan for a cancer population, including interaction management

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

