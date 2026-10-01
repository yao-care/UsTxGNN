---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 487
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Calcitriol: Repurposing Prediction for Obsolete Vitamin D Deficiency

## One-Sentence Summary

Calcitriol is the active form of vitamin D and is widely marketed in the US as generic products. The TxGNN model predicts it may be effective for **obsolete vitamin D deficiency**, its top-ranked prediction. That term is flagged "obsolete" in the ontology, so the high score is probably an artifact, and **no clinical trials or publications** support this specific prediction. The strongest-supported candidate in the same output is **hereditary hypophosphatemic rickets** (6 trials, 20 publications).

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sampled licenses are ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Calcitriol is the active form of vitamin D, so replacing it in a vitamin D deficiency state is biologically plausible.

The problem is the disease label. "Obsolete vitamin D deficiency" is a deprecated ontology term, so the 99.96% score most likely reflects the graph structure rather than a distinct new indication. No trials or literature were retrieved for it.

Other candidates from the same run differ in strength:
- **Hereditary hypophosphatemic rickets** (rank 7, L3): excess FGF23 suppresses renal CYP27B1 and lowers 1,25(OH)2D. Calcitriol plus phosphate is already conventional therapy for XLH, so the mechanism is well supported.
- **Familial isolated hypoparathyroidism** (rank 3, L5): without PTH, renal 1-alpha-hydroxylase is not stimulated. Exogenous calcitriol bypasses this step, but there is no disease-specific evidence.
- **Renal tubular acidosis** (rank 2, L4): calcitriol may help the bone and mineral complications. The literature is mostly case reports, and some studies show circulating calcitriol is unchanged in RTA, which weakens the replacement rationale.
- **Acromesomelic dysplasia (Campailla-Martinelli), craniofacial conodysplasia, Dahlberg-Borer-Newcomer syndrome** (ranks 4-6): no clear mechanistic link. These look like graph-proximity or keyword-overlap matches.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked indication (obsolete vitamin D deficiency).

For reference, the best-supported candidate, **hereditary hypophosphatemic rickets**, has these trials:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | High vs low dose active vitamin D (e.g., calcitriol) with neutral phosphate in children with XLH. Directly relevant; no results available |
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, not recruiting | 20 | Calcitriol monotherapy for one year in children and adults with XLH (mineral ions, growth, skeletal parameters). Directly relevant but small; no reported results |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, not recruiting | 27 | ENERGY 3: INZ-701 in children with ENPP1 deficiency. Indirect context only; calcitriol is not the test drug |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Withdrawn | 0 | Cinacalcet in familial hypophosphatemic rickets; calcitriol is background therapy only |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completed | 260 | Observational study of inappropriate FGF23 secretion in hypophosphatemia; no calcitriol intervention |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not yet recruiting | 65 | Phosphorus-31 spectroscopy of ATP in phosphate diabetes; diagnostic or mechanistic study |

---

## Literature Evidence

Currently no related literature is available for the top-ranked indication (obsolete vitamin D deficiency).

For reference, selected publications for **hereditary hypophosphatemic rickets**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical study | J Clin Invest | High-dose calcitriol plus phosphorus in 5 XLH patients aimed to heal osteomalacia as well as rickets |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical study | N Engl J Med | 11 children with vitamin D-resistant rickets; calcitriol raised circulating levels and increased intestinal phosphate absorption |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Clinical study | Calcif Tissue Int | Bone mass measured in 17 children after calcitriol plus phosphate therapy |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Cohort | Pediatr Endocrinol Rev | Spontaneous growth and effect of early calcitriol and phosphate therapy in 127 XLH patients from 49 centres |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Cohort | J Endocrinol Invest | Retrospective cohort on height and body proportion from birth to adulthood |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | Lancet | XLH review: FGF23 excess causes renal phosphate wasting and decreased calcitriol synthesis |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Review | Calcif Tissue Int | Diagnosis and therapy of XLH |
| [31863781](https://pubmed.ncbi.nlm.nih.gov/31863781/) | 2020 | Review | Metabolism | Management of XLH in adults |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Rickets types and treatment with vitamin D and analogues, including calcitriol |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | Horm Res Paediatr | Historical and physiological overview of rickets, vitamin D and Ca/P metabolism |

No RCTs were retrieved. Direct calcitriol evidence comes from small, older clinical studies.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA091356 | Calcitriol | Capsule | Strides Pharma Science Limited |
| ANDA091174 | Calcitriol | Capsule, liquid filled | Golden State Medical Supply, Inc. |
| ANDA203289 | Calcitriol | Capsule | Amneal Pharmaceuticals LLC |
| ANDA091356 | Calcitriol | Capsule | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA091174 | Calcitriol | Capsule, liquid filled | A-S Medication Solutions |

Available forms across all 20 licenses: oral capsules, ointment, solution and injection. The record contains no approved-indication text.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

For the hypophosphatemic rickets candidate, monitor for hypercalciuria, nephrocalcinosis and secondary or tertiary hyperparathyroidism.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, obsolete vitamin D deficiency, is an ontology artifact with no supporting trials or literature (L5). The more credible direction is hereditary hypophosphatemic rickets (L3, S2), where calcitriol is already conventional therapy. It should be evaluated as a separate research question, not as a new repurposing indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Results from NCT03820518 and NCT03748966, plus a comparison with the approved label indications
- Confirmation of whether the hypophosphatemic rickets indication is already covered by existing labeling

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

