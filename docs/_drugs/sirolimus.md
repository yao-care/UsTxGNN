---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 1166
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
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

Sirolimus is an mTOR inhibitor that is already marketed in the United States.
The TxGNN model predicts it may be useful for **Liposarcoma**.
Evidence is thin: **1 clinical trial** (a Phase 2 study of sirolimus plus cyclophosphamide with no posted results) and **7 publications**, none of which tests sirolimus in liposarcoma directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 15 of 16) |
| Number of FDA Applications | 16 (active: 15) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Sirolimus is generally described as an inhibitor of mTORC1, a kinase complex that drives cell growth and proliferation.

Activation of the PI3K/AKT/mTOR pathway has been reported in soft tissue sarcomas, including liposarcoma. Blocking mTOR is therefore a plausible way to slow tumour growth, and this is the biological reasoning behind the prediction.

This is only a rationale. The only registered trial tests sirolimus together with cyclophosphamide, so the effect of sirolimus alone cannot be separated out. The publications are mostly reviews of targeted sarcoma therapy and studies of cancer risk after transplantation, which support the idea only indirectly.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre study of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma (2014–2021). No results are posted in the data compiled for this report. The single arm and the combination partner make it impossible to attribute any effect to sirolimus, and the liposarcoma subgroup size is not stated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of recent progress in molecular characterisation and new therapies for soft tissue sarcoma. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Current Opinion in Oncology | Rationale and results of recent trials of molecular-targeted agents in advanced sarcomas. |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT (secondary analysis) | Journal of the American Society of Nephrology | In renal transplant recipients, a sirolimus-based regimen after early cyclosporine withdrawal was assessed for cancer risk. This is not a liposarcoma study. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du Cancer | Targeted treatments for molecular subgroups of rare connective tissue tumours and sarcomas. |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplantation Proceedings | Cancer screening and the effects of long-term immunosuppressive drugs in renal transplant patients. |

None of these publications reports sirolimus given to patients with liposarcoma.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021110 | Sirolimus (Mylan) | Tablet, sugar coated | Not available |
| NDA213478 | HYFTOR (Nobelpharma America) | Gel | Not available |
| ANDA201676 | Sirolimus (Zydus) | Tablet, film coated | Not available |
| ANDA214753 | Sirolimus (Ascend) | Tablet, film coated | Not available |
| ANDA208691 | Sirolimus (Northstar Rx) | Tablet, film coated | Not available |

The records may be partial.

<!-- review:begin us-lic-20261105-sirolimus-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All 11 licences on record are valid, and the list above shows only the first five. The records may be partial." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 16 FDA applications or NDC listings for this drug, 15 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-sirolimus-1 -->

---

## Safety Considerations

- **Drug Interactions**: The interaction database lists 100 interacting drugs. Major-level interactions include:
  - Amphotericin B and amphotericin B (lipid complex)
  - Clarithromycin
  - Mesalazine
  - Balsalazide

  Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), several antidiabetic drugs (metformin, pioglitazone, alogliptin, acarbose, canagliflozin, dapagliflozin), cimetidine and aprepitant.

Package-insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No published study tests sirolimus in liposarcoma. The only trial is a single-arm combination study with no posted results, and the other items concern transplantation or are general sarcoma reviews. Despite the high model score (0.9989), the evidence level is L5.

**To proceed, the following is needed:**
- Posted or published results from NCT02821507, ideally with liposarcoma-specific outcomes and a way to separate the effect of sirolimus from cyclophosphamide
- Preclinical or clinical data on single-agent sirolimus in liposarcoma subtypes
- Detailed mechanism-of-action data
- Package-insert warnings and contraindications, and a safety plan covering the major drug interactions above

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All 11 licences on record are valid, and the list above shows only the first five" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

