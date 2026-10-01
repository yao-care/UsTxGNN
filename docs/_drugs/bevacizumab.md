---
layout: default
title: Bevacizumab
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
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

# Bevacizumab: From Anti-VEGF Cancer Therapy to Epiglottis Neoplasm

## One-Sentence Summary

Bevacizumab is a monoclonal antibody that neutralizes VEGF-A and blocks tumor angiogenesis. It is marketed in the US under multiple biologics licenses.
The TxGNN model predicts it may be effective for **epiglottis neoplasm**, but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Epiglottis neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs/BLAs | 16 |
| Recommended Decision | Hold |

The approved indication text is empty in the supplied US license records, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

Bevacizumab binds and neutralizes VEGF-A, which inhibits tumor angiogenesis. The original MOA field in the Evidence Pack is a data gap, so this description comes from the mechanistic note attached to the prediction.

Epiglottis neoplasm is a head and neck tumor. Vascularized head and neck tumors depend on VEGF-driven blood supply, so anti-VEGF therapy is mechanistically plausible.

This is a generic anti-angiogenic argument only. No trial or publication has tested bevacizumab in this disease. The similarity to the original indication has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The Evidence Pack lists 16 licenses in total. The table shows the unique products among the first five records; Avastin appears twice with the same license number.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761175 | JOBEVNE (Biocon Biologics Inc.) | Injection | Not listed in the data |
| BLA125085 | Avastin (Genentech, Inc.) | Injection, solution | Not listed in the data |
| BLA761268 | Vegzelma (CELLTRION USA, Inc.) | Injection, solution | Not listed in the data |
| BLA761198 | Avzivi (Bio-Thera Solutions, Ltd.) | Injection, solution | Not listed in the data |

All listed products are injectables.

---

## Cytotoxicity

Bevacizumab is an antineoplastic agent. It is a targeted antibody, not a conventional cytotoxic chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF-A monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a very high model score (99.90%) and a generic anti-angiogenic rationale. There are no trials or publications for epiglottis neoplasm, so the evidence level is L5. The package insert warnings and contraindications are also missing, which the Evidence Pack flags as a blocking gap for safety screening.

Other candidates in the same pack have more evidence and are better places to start:
- **Cystic neoplasm** reaches L2, driven by a Phase 3 ovarian cancer trial (NCT00565851). Ovarian cancer is probably already a labeled use, so this may not be true repurposing, and the disease term should be clarified first.
- **Benign neoplasm of floor of mouth** is provisionally L3, but its only trial is a Phase 1 study in advanced cancers.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text (blocking gap)
- Mechanism of action data from DrugBank
- A targeted search of ClinicalTrials.gov and PubMed for bevacizumab in laryngeal, epiglottic and head and neck tumors
- An assessment of similarity to the original indication and of route compatibility
- Clarification of whether this benign or malignant disease entity fits the intended repurposing question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

