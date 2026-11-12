---
layout: default
title: Capmatinib
parent: Model Prediction Only (L5)
nav_order: 493
evidence_level: L5
indication_count: 2
monitor_inn: "CAPMATINIB"
predicted_indications: ["rheumatoid arthritis", "brachydactyly-syndactyly syndrome"]
last_modified_at: 2026-11-12
description: "Capmatinib: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Capmatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Capmatinib: From an Unspecified Original Indication to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Capmatinib is an oral MET (c-Met) tyrosine kinase inhibitor, marketed in the US as TABRECTA, but the data compiled for this report do not list its original approved indication.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**.
Support is very limited: **0 clinical trials** and **1 general review publication**, so this is essentially a model-based prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank are not available in the data compiled for this report. Capmatinib is known as a selective MET (c-Met) tyrosine kinase inhibitor, and its original indication could not be confirmed from the data provided.

There is a plausible but unproven mechanistic link. HGF/MET signaling has been reported to be upregulated in rheumatoid synovium. It may contribute to synovial fibroblast activation, angiogenesis, and inflammatory cell migration. In theory, blocking MET could dampen these processes.

However, no clinical or preclinical evidence supporting MET inhibition in rheumatoid arthritis was found. The high TxGNN score is a model-based prediction only. Because the original indication and MOA are missing, the prediction cannot be cross-checked against the drug's established use.

The second-ranked prediction, brachydactyly-syndactyly syndrome (score 0.9903), has no supporting trials or literature and no evident mechanistic link. It is a congenital limb malformation, and MET inhibition is not expected to correct it. It is likely a network-proximity artifact and is not pursued here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | 2021 update on FDA-approved small-molecule protein kinase inhibitors. A general overview of the kinase inhibitor class, not specific evidence for capmatinib in rheumatoid arthritis. |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA213591 | TABRECTA | NOVARTIS PHARM | Tablet; oral | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for safety information.

**Drug Interactions:** A search found 100 recorded interactions. The main ones from the listed entries:
- **Major:** Dexamethasone, Clarithromycin
- **Moderate:** Metformin, Alosetron, Loperamide, Aprepitant, Empagliflozin, Glycerol phenylbutyrate, Methylnaltrexone, Metreleptin, Naldemedine, Naltrexone
- **Minor:** Proton pump inhibitors (rabeprazole, dexlansoprazole, esomeprazole, lansoprazole, omeprazole, pantoprazole), fidaxomicin, naloxegol

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no registered trials and no disease-specific literature. The package insert safety data and the original indication and MOA are missing, so the prediction cannot be properly assessed.

<!-- review:begin us-lic-20261031-capmatinib-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction rests on model output alone (L5), with no registered trials and no disease-specific literature. The drug's only US license is cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 1 FDA application or NDC listing for this drug, 1 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-capmatinib-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, to allow safety screening
- Original indication and mechanism-of-action data (e.g., from DrugBank)
- Preclinical evidence of MET inhibition in rheumatoid synovium or in arthritis models
- Review of the risk-benefit balance for a chronic inflammatory condition, given the drug's oncology-type safety profile and the significant interactions (e.g., dexamethasone, clarithromycin)
- Clarification of current US market and availability status

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The drug's only US license is cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

