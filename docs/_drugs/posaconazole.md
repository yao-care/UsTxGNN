---
layout: default
title: Posaconazole
parent: Moderate Evidence (L3-L4)
nav_order: 1065
evidence_level: L4
indication_count: 1
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Posaconazole: From Antifungal Therapy to Pneumocystosis

## One-Sentence Summary

Posaconazole is an azole antifungal, marketed in the US as generic injection, delayed-release tablet and oral solution products.
The TxGNN model predicts it may be effective for **pneumocystosis** (score 99.77%), but the supporting evidence is weak: **2 clinical trials** and **5 publications**, none of which test posaconazole against Pneumocystis directly.
The known mechanism argues against the prediction, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed below are all ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Posaconazole inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis in the fungal cell membrane. The original mechanism-of-action field and the approved-indication text are not available in the source data. The description here therefore relies on the mechanism analysis in the Evidence Pack and on general knowledge of the drug class.

The high TxGNN score is probably not driven by a real mechanistic link. *Pneumocystis jirovecii* has little or no ergosterol in its membrane and uses cholesterol instead, so azoles are generally considered clinically ineffective against it. The first-line treatment is trimethoprim-sulfamethoxazole (TMP-SMX). The graph link most likely reflects posaconazole's broad antifungal class and its frequent co-mention with other invasive fungal diseases in transplant and haemato-oncology settings.

The prediction is therefore best read as a model artifact until direct data show otherwise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Rezafungin vs standard antimicrobial regimen (which may include posaconazole) to prevent invasive fungal disease after allogeneic transplant. Posaconazole is a comparator, and the trial gives no direct evidence for Pneumocystis. Relevance grade: B |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform protocol comparing post-transplant cyclophosphamide-based GVHD prophylaxis. Any posaconazole use would be background prophylaxis, so the link to pneumocystosis is indirect. Relevance grade: C |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Guideline | The Lancet Infectious Diseases | British Society for Medical Mycology update on diagnosing serious fungal diseases. It covers non-culture-based tests and is about diagnosis, not posaconazole treatment |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | Chinese Thoracic Society guideline on diagnosing and managing invasive pulmonary fungal disease, with emphasis on non-immunosuppressed patients |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and Pneumocystis pneumonia. Notes that mould-active posaconazole prophylaxis reduced invasive fungal disease in high-risk haemato-oncology patients |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Lung epithelial lining fluid penetration of antifungal and other anti-infective agents. Pharmacokinetic background only, with no Pneumocystis efficacy data |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective study of infectious complications in acute GVHD after liver transplantation, describing infection and antimicrobial management patterns |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA214842 | Posaconazole | Injection | Eugia US LLC |
| ANDA212226 | Posaconazole | Tablet, delayed release | Golden State Medical Supply, Inc. |
| ANDA219057 | Posaconazole | Solution | Camber Pharmaceuticals, Inc. |
| ANDA217553 | Posaconazole | Injection, solution | Gland Pharma Limited |
| ANDA214321 | Posaconazole | Tablet, delayed release | NorthStar RxLLC |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no study tests posaconazole against Pneumocystis. The two trials involve posaconazole only as a comparator or background therapy. Pneumocystis lacks the ergosterol target, and TMP-SMX is an established first-line therapy. The evidence level is L4.

**To proceed, the following is needed:**
- Direct evidence, such as in vitro susceptibility of Pneumocystis to posaconazole, animal models, or clinical reports of posaconazole prophylaxis or treatment
- Complete mechanism-of-action data from DrugBank
- FDA package insert warnings and contraindications (required before any safety screening)
- A comparison against TMP-SMX and other standard prophylaxis, to show a plausible added benefit in patients who cannot take TMP-SMX
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

