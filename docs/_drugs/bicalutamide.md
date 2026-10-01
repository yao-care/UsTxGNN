---
layout: default
title: Bicalutamide
parent: Moderate Evidence (L3-L4)
nav_order: 458
evidence_level: L4
indication_count: 10
---

# Bicalutamide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is a nonsteroidal androgen receptor antagonist, known as an antiandrogen for prostate cancer. The US license records provided do not state an approved indication.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and only **1 publication**, a comment letter, supporting this direction.
This is a hypothesis-level prediction with very thin evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data. Prostate cancer is inferred from general knowledge of the drug. |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 10 (NDA and ANDA authorizations combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bicalutamide blocks the androgen receptor, which reduces androgen-driven signaling. Androgens promote terminal (coarse) hair growth. Blocking the receptor could therefore plausibly reduce unwanted hair growth. Detailed mechanism-of-action data is not available in the source record, so this reasoning rests on the drug's known class.

The one supporting item is a comment letter on a retrospective review of 35 patients. That review reported bicalutamide improving **minoxidil-induced hypertrichosis in female pattern hair loss**. This is indirect, low-tier evidence. It does not address congenital or generalized hypertrichosis, and the letter's abstract is not available.

TxGNN also predicted several other conditions, including Ambras syndrome, hair shaft abnormalities, leprosy, and Dandy-Walker syndrome. Most have no androgen-based rationale, and the high scores likely reflect graph proximity rather than pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Comment/Letter | J Am Acad Dermatol | Comment on a retrospective review of 35 patients on bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss. No abstract is available, so no outcome data can be extracted. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020498 | Bicalutamide | Tablet | ANI Pharmaceuticals, Inc. |
| NDA020498 | Bicalutamide | Tablet | Golden State Medical Supply, Inc. |
| ANDA078917 | Bicalutamide | Tablet | Proficient Rx LP |
| ANDA078917 | Bicalutamide | Tablet | Accord Healthcare Inc. |
| ANDA079110 | Bicalutamide | Tablet, film coated | Sun Pharmaceutical Industries, Inc. |

All listed products are oral. The source record contains no approved indication text for any of them.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (nonsteroidal antiandrogen), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

The classification comes from general knowledge of the drug, because the DrugBank categories were not provided.

---

## Safety Considerations

Please refer to the package insert for safety information.

The drug-interaction query returned no results. Package insert warnings and contraindications have not yet been retrieved, so safety screening cannot proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hypertrichosis prediction rests on one comment letter and no registered trials, so it is a research question rather than an actionable candidate. Safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Retrieve and parse the FDA package insert to obtain warnings and contraindications.
- Obtain mechanism-of-action data from DrugBank.
- Retrieve the full text of the retrospective 35-patient study that the comment letter discusses.
- Define the target population, since acquired, drug-induced, and congenital hypertrichosis differ mechanistically.
- Consider prioritizing **female breast carcinoma** (rank 9) for further review. It has a Phase 2 trial, [NCT03650894](https://clinicaltrials.gov/study/NCT03650894), of nivolumab + bicalutamide + ipilimumab in metastatic HER2-negative breast cancer (n=30, active not recruiting). It also has preclinical support for androgen receptor-positive triple-negative breast cancer. However, the trial is a combination regimen with no reported results, and a Phase 2 single-arm study of bicalutamide plus an aromatase inhibitor (PMID [31434793](https://pubmed.ncbi.nlm.nih.gov/31434793/)) showed no synergistic activity in estrogen receptor-positive disease.

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

