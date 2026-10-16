---
layout: default
title: Bevacizumab
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
monitor_inn: "BEVACIZUMAB"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
---

# Bevacizumab
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

# Bevacizumab: From Ovarian, Breast and Other Solid Cancers to Epiglottis Neoplasm

## One-Sentence Summary

Bevacizumab is an anti-VEGF monoclonal antibody originally used for solid tumours such as ovarian, peritoneal, breast, colorectal and brain cancers.
The TxGNN model predicts it may be effective for **epiglottis neoplasm**, but the data compiled for this report contain **0 clinical trials** and **0 publications** for this specific indication, so the prediction rests on the model alone.

Note: Ten predicted indications were compiled. The top-ranked one (epiglottis neoplasm) is the focus of the main sections below. Other candidates with more supporting evidence are summarised in the Conclusion.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license data; the knowledge graph lists peritoneal, ovarian, breast, colorectal and glioblastoma-related cancers |
| Predicted New Indication | Epiglottis neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (7 authorizations, all listed as cancelled) |
| Number of NDAs | 7 (all BLAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, bevacizumab is a monoclonal antibody that binds VEGF-A and inhibits tumour angiogenesis. Its efficacy has been established in several solid tumours, and mechanistically it may be applicable to other vascularised tumours, including those of the head and neck.

The original indications (ovarian, peritoneal, breast, colorectal and glioblastoma) are mostly vascular, VEGF-dependent solid tumours. Epiglottis neoplasm is a head and neck tumour, so the anti-angiogenic rationale is plausible. However, no trial or publication in the data directly addresses this site. The link is a model prediction plus general mechanistic reasoning, not demonstrated efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered for epiglottis neoplasm.

## Literature Evidence

Currently no related literature available for epiglottis neoplasm.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125085 | Avastin (Genentech) | Injection, solution | Not provided; status cancelled |
| BLA761028 | MVASI (Amgen) | Injection, solution | Not provided; status cancelled |
| BLA761099 | Zirabev (Pfizer) | Injection, solution | Not provided; status cancelled |
| BLA761268 | Vegzelma (Celltrion) | Injection, solution | Not provided; status cancelled |
| BLA761175 | JOBEVNE (Biocon Biologics) | Injection | Not provided; status cancelled |

Two further biosimilar authorizations (Avzivi, Alymsys) are also listed as cancelled. The regulatory status in the source data should be verified against current FDA records, since originator and biosimilar bevacizumab products are widely marketed.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Low as monotherapy; may rise in combination with chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood pressure, urine protein, CBC when combined with chemotherapy, signs of bleeding, wound healing |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 22 interactions were recorded in the DDI database (the 20 entries returned are the basis for the points below). Major-level interactions include:
  - Deferiprone
  - Panitumumab
  - Samarium (153Sm) lexidronam
  - Sunitinib
  - Thalidomide
- Moderate-level interactions include bisphosphonates (alendronic, risedronic, etidronic, pamidronic, tiludronic acid, ibandronate), growth factors (filgrastim, pegfilgrastim, sargramostim, palifermin), idelalisib, romosozumab, and several radiopharmaceuticals (radium Ra 223, strontium-89, sodium phosphate P32).

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Epiglottis neoplasm has only a model prediction (score 99.90%) and no trials or literature, so the evidence level is L5. Package insert safety data are also missing, which blocks safety screening.

**Other candidates in the ranked list:**
- **Cystic neoplasm (ovarian-type tumours)** has the strongest evidence (L1): the Phase 3 trial [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) (n=1052, active, not recruiting) and a systematic review of bevacizumab in low-grade serous ovarian cancer ([PMID 37754507](https://pubmed.ncbi.nlm.nih.gov/37754507/)). However, ovarian cancer is already an original indication, so this is not a novel repurposing signal.
- **Cervical neuroblastoma** has Phase 1/2 data from indirect settings and a case report of durable palliation in olfactory neuroblastoma ([PMID 22826790](https://pubmed.ncbi.nlm.nih.gov/22826790/)). It is a research question only.
- **Benign neoplasm of the tongue and floor of mouth** have only indirect preclinical or review literature.
- **Testicular tumour, hypopharynx benign neoplasm, mesenchymoma, jugular foramen schwannoma** have no trials or literature (L5).
- **Nasal cavity inverting papilloma** is linked only to non-specific head and neck trials, likely annotation overlap.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- Verification of current US market status, since all 7 licenses are listed as cancelled
- Disease-specific preclinical or clinical evidence for epiglottis neoplasm, or a focused review of existing head and neck anti-VEGF data
- A decision on whether to prioritise a candidate with stronger direct evidence, such as a non-ovarian indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

