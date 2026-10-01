---
layout: default
title: Filgrastim
parent: Moderate Evidence (L3-L4)
nav_order: 707
evidence_level: L4
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From G-CSF Neutrophil Support to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a granulocyte colony-stimulating factor (G-CSF) marketed in the US as several injectable biologics. The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but the evidence is weak. The **14 registered clinical trials** and **1 publication** found are mostly stem cell transplant or mobilization studies matched by keyword, and none tests filgrastim in this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed below are BLAs) |
| Recommended Decision | Hold |

The pack has no approved-indication text for the US labels, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the input. From the pack's own analysis, filgrastim acts on the neutrophil lineage and on mobilizing hematopoietic stem cells. It does not act on platelet granule release or platelet function.

The high TxGNN score (0.99998, rank 171) comes from graph-based similarity and has no supporting mechanism. Most of the retrieved trials involve transplant or mobilization, where filgrastim is a supportive agent rather than the tested treatment. The only Phase 3 trial (NCT04047628) compares autologous transplant with best available therapy in multiple sclerosis.

The other nine TxGNN predictions were also reviewed:
- Five have no clinical trials and no literature: pseudo-von Willebrand disease, Glanzmann thrombasthenia, constitutional thrombocytopenia, collagen receptor defect, and C1 inhibitor deficiency.
- Serpinopathy and fetal/neonatal alloimmune thrombocytopenia are also prediction-only.
- Scott syndrome and platelet-type bleeding disorder have keyword-matched trials only.
- All nine were rated Hold, and none has a plausible link to G-CSF signaling.

---

## Clinical Trial Evidence

All trials below were graded C (indirect or unrelated). None reports results for filgrastim in this disease. Ten of the 14 registered trials are shown.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated-donor stem cell transplant for hematological malignancies; filgrastim incidental |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs unselected autologous transplant in mantle cell and diffuse large B-cell lymphoma |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous stem cell transplant vs best available therapy in relapsing multiple sclerosis; the only Phase 3 trial |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Post-transplant cyclophosphamide GVHD prophylaxis platform in mismatched unrelated donor transplant |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic transplant with busulfan, fludarabine and total body irradiation |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Banked HLA-mismatched donor marrow with post-transplant cyclophosphamide; no participants enrolled |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Blood stem cell transplant pilot in high-risk pediatric sarcomas |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Umbilical cord blood transplant with NK cells in myeloid leukemia |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity stem cell transplant for GATA2 mutations |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion plus autologous transplant in severe lupus |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Observational | Frontiers in Immunology | G-CSF mobilization of stem cells in healthy donors preferentially mobilizes lymphocyte subsets. This concerns transplant immunology, not platelet disorders. |

---

## US Market Information

The pack lists 20 licenses in total and gives no approved-indication text for any of them. Five are shown.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| BLA761080 | Nivestym (Pfizer) | Injection, solution |
| BLA125553 | ZARXIO (Sandoz) | Injection, solution |
| BLA125294 | GRANIX (Cephalon) | Injection, solution |
| BLA103353 | NEUPOGEN (Amgen) | Injection, solution |
| BLA761126 | NYPOZI (Cipla USA) | Injection |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no plausible mechanism. G-CSF does not drive platelet production or platelet function, and no trial or publication tests filgrastim in this disease. The L4 rating reflects only the loose transplant context of the keyword-matched trials.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Approved-indication text for the US labels
- Preclinical or mechanistic evidence that G-CSF affects platelet release, plus any trial that tests filgrastim directly in this disease
- Pharmacology review of whether the model prediction reflects graph artifacts rather than real biology

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

