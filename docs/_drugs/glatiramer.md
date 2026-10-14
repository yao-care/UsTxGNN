---
layout: default
title: Glatiramer
parent: Model Prediction Only (L5)
nav_order: 752
evidence_level: L5
indication_count: 1
---

# Glatiramer
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Glatiramer: From Multiple Sclerosis to Hemoglobinopathy

## One-Sentence Summary

Glatiramer is an immunomodulator marketed under the brand name Copaxone and as generics, used in multiple sclerosis (MS).
The TxGNN model predicts it may be effective for **hemoglobinopathy**,
but currently there are **0 clinical trials** and only **1 loosely related publication**, which does not study glatiramer in this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data compiled for this report (generally used for relapsing multiple sclerosis) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 9 (1 NDA, 8 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, glatiramer acetate is an immunomodulator that shifts T-cell responses toward a Th2 phenotype and induces regulatory T cells. It is used in multiple sclerosis.

No plausible direct mechanistic link to hemoglobinopathies (such as sickle cell disease or thalassemia) has been established. The only linked publication (PMID 28372806) is a case-based commentary on immune disorders after natalizumab discontinuation in an MS patient who also had beta thalassemia. It does not evaluate glatiramer in hemoglobinopathy. The very high TxGNN score is therefore most likely a graph-proximity artifact from shared immune-related nodes rather than evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Case-based commentary | Revue neurologique | Multiple immune disorders after natalizumab discontinuation in a woman with MS and a history of beta thalassemia; glatiramer was not evaluated for hemoglobinopathy |

## US Market Information

All nine authorizations are cancelled, and no approved indication text is available in the data compiled for this report.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020622 | Copaxone (Teva Neuroscience) | Injection, solution | Not available (cancelled) |
| ANDA090218 | Glatopa (Sandoz) | Injection, solution | Not available (cancelled) |
| ANDA091646 | Glatiramer Acetate (Mylan) | Injection, solution | Not available (cancelled) |
| ANDA206936 | Glatiramer Acetate (Mylan) | Injection, solution | Not available (cancelled) |
| ANDA203857 | Glatiramer Acetate (Sun Pharmaceutical) | Injection, solution | Not available (cancelled) |

## Safety Considerations

- **Drug Interactions**: One interaction is recorded. **Natalizumab** is classed as **Major** (source: DDInter).

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score. There are no clinical trials, the single linked publication does not study glatiramer in hemoglobinopathy, and no mechanistic link is established. All US licenses are cancelled, which further limits translational feasibility.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Preclinical or mechanistic evidence linking glatiramer's immunomodulation to hemoglobinopathy pathophysiology
- Clarification of which hemoglobinopathy (sickle cell disease, thalassemia, etc.) is targeted, and of the route and formulation requirements
- Confirmation of current regulatory and market status, since all US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

