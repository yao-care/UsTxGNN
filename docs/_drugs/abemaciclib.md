---
layout: default
title: Abemaciclib
parent: Moderate Evidence (L3-L4)
nav_order: 43
evidence_level: L4
indication_count: 10
---

# Abemaciclib
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

# Abemaciclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib is an oral CDK4/6 inhibitor. The records in this Evidence Pack describe it as a treatment for HR+/HER2- breast cancer, but they do not list an approved indication.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 clinical trials** and only **1 publication** (an observational study), and that study does not show therapeutic benefit. The prediction currently rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the licence records; the trial and literature records show use in HR+/HER2- breast cancer |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 licence records (all NDA208716, Verzenio) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, abemaciclib is a CDK4/6 inhibitor whose efficacy in HR+/HER2- breast cancer is established through phase 3 work such as MONARCH 2. Mechanistically, it may be applicable to rheumatoid arthritis.

The proposed link is plausible but unverified. CDK4/6 inhibition could dampen the proliferation of activated lymphocytes and synovial fibroblasts, both of which drive joint inflammation. No study in the pack tests this hypothesis in rheumatoid arthritis.

The only literature item is a 2025 cohort study of immune-mediated diseases in breast cancer patients on CDK4/6 inhibitors. It describes how often these diseases occur or flare, not whether the drug helps them. The high TxGNN score of 0.97 is therefore a model prediction with no supporting efficacy evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort | The Oncologist | Investigates how common autoimmune diseases are in HR+/HER2- breast cancer patients on CDK4/6 inhibitors plus endocrine therapy, to find predictive biomarkers and assess the impact on treatment. It reports disease occurrence, not therapeutic benefit, so it does not support efficacy in rheumatoid arthritis. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208716 | Verzenio (Eli Lilly and Company) | Tablet (oral) | Not specified in the record |

The four licence records are identical entries under the same NDA, so they are shown once.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Literature retrieved for other predicted indications (mainly heart disease) shows these class-level and drug-level signals. They matter for any future assessment in a patient population with comorbidities:
- **Cardiovascular**: QTc prolongation and cardiovascular adverse events with CDK4/6 inhibitors (systematic reviews and FAERS pharmacovigilance studies). One case report describes myocardial infarction due to coronary plaque erosion two weeks after starting abemaciclib.
- **Renal**: An FAERS analysis reports abemaciclib-associated kidney injury.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no trials in rheumatoid arthritis, and the single observational study describes autoimmune disease occurrence, not benefit. The 0.97 score is a prediction only, so the evidence does not yet justify moving forward.

**To proceed, the following is needed:**
- The package insert warnings and contraindications, and detailed mechanism of action data
- Preclinical data, for example activated lymphocytes or synovial fibroblasts, or an arthritis animal model, testing whether CDK4/6 inhibition has anti-arthritic activity
- A safety assessment for a chronic inflammatory population, covering the cardiovascular and renal signals above and overlap with immunosuppressive therapy
- Route and formulation compatibility, currently pending

Other predicted indications are weaker still. Amyotrophic lateral sclerosis has only preclinical cell-model evidence (TDP-43 clearance) and is flagged as a research question, and heart disease shows a safety signal rather than benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

