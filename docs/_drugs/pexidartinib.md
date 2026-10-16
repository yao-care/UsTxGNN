---
layout: default
title: Pexidartinib
parent: Model Prediction Only (L5)
nav_order: 1035
evidence_level: L5
indication_count: 10
monitor_inn: "PEXIDARTINIB"
predicted_indications: ["HER2 positive breast carcinoma", "progesterone-receptor positive breast cancer", "normal breast-like subtype of breast carcinoma", "progesterone-receptor negative breast cancer", "breast tumor luminal A or B", "synovium cancer", "synovium disease", "dermatofibrosarcoma protuberans", "multifocal choroiditis", "malignant giant cell tumor"]
last_modified_at: 2026-10-14
description: "Pexidartinib: predicted new indication HER2 positive breast carcinoma (evidence level L5). Approved use: Tenosynovial giant cell tumor (including the localized type and pigme…"
---

# Pexidartinib
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

# Pexidartinib: From Tenosynovial Giant Cell Tumor to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Pexidartinib is an oral kinase inhibitor originally used to treat tenosynovial giant cell tumor (TGCT, also called pigmented villonodular synovitis).
The TxGNN model predicts it may be effective for **HER2 positive breast carcinoma**, but this rests on the model score alone: there are **0 clinical trials** and **1 preclinical publication**, and that paper does not study HER2-positive disease or pexidartinib itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tenosynovial giant cell tumor (including the localized type and pigmented villonodular synovitis) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. The published literature describes pexidartinib as an oral inhibitor of colony-stimulating factor 1 receptor (CSF1R), KIT and FLT3-ITD. In TGCT, CSF1 overexpression recruits CSF1R-bearing macrophages that drive tumor growth, and pexidartinib's efficacy there is well established.

The proposed link to breast cancer is indirect. CSF1R inhibition can reprogram tumor-associated macrophages, which may counter immunosuppression in the tumor microenvironment. The only linked paper (PMID 41986650) is a preclinical study in which CSF1R inhibitors reduced CDK4/6 inhibitor-induced immunosuppression in **HR+/HER2-** breast cancer. It addresses CSF1R inhibitors in general, not HER2-positive disease and not pexidartinib specifically.

TGCT is a benign, locally aggressive synovial tumor, so its biology is very different from HER2-driven breast cancer. The high TxGNN score (99.98%) is a computational prediction only and is not backed by indication-specific clinical or mechanistic data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41986650](https://pubmed.ncbi.nlm.nih.gov/41986650/) | 2026 | Preclinical | Oncogene | CSF1R inhibitors mitigate CDK4/6 inhibitor-induced immunosuppression and increase antitumor immunity in HR+/HER2- breast cancer. It does not address HER2-positive disease or pexidartinib. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211810 (cancelled) | Turalio (Daiichi Sankyo Inc.) | Capsule (oral) | Indication text not provided in the data compiled |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (small-molecule kinase inhibitor: CSF1R, KIT, FLT3) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function is the key parameter (hepatotoxicity is the principal concern, with a boxed warning and REMS program noted in the compiled data); other parameters per the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Key Warnings**: The compiled data notes a boxed warning for serious hepatotoxicity and restricted access through a REMS program. A dedicated long-term hepatic safety analysis in TGCT patients is available (PMID 33289960). Full package insert text was not available.
- **Drug Interactions**: The query returned 100 interactions, of which 20 were reviewed. Major-level interactions among them include:
  - Acid-suppressing drugs: omeprazole, rabeprazole, dexlansoprazole
  - Antibiotics: clarithromycin, doxycycline, minocycline, tetracycline
  - Other drugs: acarbose, pioglitazone, bupropion, aprepitant, chenodeoxycholic acid

  Moderate interactions include famotidine, ranitidine, cimetidine, metformin, dexamethasone, budesonide, magnesium oxide and saxagliptin. A clinical study (PMID 32918831) evaluated pexidartinib's effects on CYP2C9, CYP2C19, CYP3A and P-glycoprotein substrates.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for HER2-positive breast carcinoma has no clinical trials and only one general preclinical paper in a different breast cancer subtype (HR+/HER2-). The evidence level is L5, and the US license is cancelled-only. The boxed hepatotoxicity warning also raises the bar for any new oncology use.

**To proceed, the following is needed:**
- Pexidartinib-specific preclinical data in HER2-positive breast cancer models, alone and combined with HER2-targeted therapy
- Detailed mechanism-of-action data (MOA) and a clear rationale for the CSF1R/macrophage link in HER2-positive disease
- Full package insert warnings and contraindications, including the hepatotoxicity risk-benefit assessment for a non-TGCT population
- A review of regulatory and REMS availability, given the cancelled-only market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

