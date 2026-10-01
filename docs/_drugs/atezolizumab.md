---
layout: default
title: Atezolizumab
parent: Model Prediction Only (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Its Approved PD-L1 Oncology Uses to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab (brand name TECENTRIQ) is a PD-L1-blocking antibody marketed in the US as an injectable biologic. The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**. The supporting evidence is thin: **2 clinical trials** (one Phase 1b multi-tumor study and one Phase 2 study in bladder cancer) and **no publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied record |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 as scored, provisional (the only completed Phase 2 trial is single-arm and in bladder cancer, so it does not strictly meet the RCT criterion) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both entries are BLA761034, a biologics license) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Based on known drug-class information, atezolizumab blocks PD-L1 and restores T-cell activity against tumors. The mechanistic link below is inferred from class knowledge, not from the supplied data.

Prostatic urethra urothelial carcinoma has the same histologic lineage as bladder urothelial carcinoma. The PD-1/PD-L1 rationale therefore plausibly carries over from bladder disease to this site.

The clinical link is indirect. The bladder-cancer trial does not address prostatic urethral involvement, and the multi-tumor study only includes a urothelial cohort. The model's high score is a hypothesis, not proof.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Atezolizumab in BCG-unresponsive non-muscle-invasive bladder cancer. Same urothelial lineage but a bladder-specific population, and it appears single-arm. Relevance grade B. |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 (1b) | Active, not recruiting | 914 | Dose-escalation of cabozantinib alone or with atezolizumab in multiple advanced solid tumors, including urothelial carcinoma (bladder, renal pelvis, ureter, urethra). Linked only through the urothelial cohort. Relevance grade C. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761034 | TECENTRIQ (Genentech, Inc.) | Injection, solution | Not stated in the supplied record |

The record lists this authorization twice with identical content. Only injectable forms are on file.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-L1 checkpoint inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Not characterized in the supplied record. Class knowledge suggests low, but please refer to the package insert. |
| Emetogenicity Classification | Not characterized in the supplied record. Class knowledge suggests low. |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Not classified in the supplied record. Class knowledge suggests standard biologic handling rather than cytotoxic-drug precautions, but please confirm against the label. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, but no evidence addresses prostatic urethral disease specifically. The available trials are bladder-only, early-phase or multi-tumor. The safety data (warnings and contraindications) are also missing and were flagged as a blocking gap, so the candidate cannot pass safety screening yet.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indications) to clear the blocking safety gap and confirm the original indications
- Mechanism of action data from DrugBank
- Cohort-level data from NCT03170960 confirming whether prostatic urethra or other non-bladder urothelial patients were enrolled
- Published results from NCT02844816 (completed, n=172) and a review of relevant urothelial-carcinoma literature
- A comparison with other predictions in this pack. Endocervical carcinoma (rank 6) currently has more clinical evidence, with two trials and one review, and may be a stronger candidate to prioritize.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

