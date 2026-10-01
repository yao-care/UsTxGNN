---
layout: default
title: Molindone
parent: Model Prediction Only (L5)
nav_order: 940
evidence_level: L5
indication_count: 10
---

# Molindone
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

# Molindone: From Schizophrenia (Antipsychotic Use) to Retinal Dystrophy

## One-Sentence Summary

Molindone is an oral antipsychotic. The literature in the pack describes it as useful in schizophrenia, but the US license records list no approved indication.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but this rests on the model score alone: **0 clinical trials** and **no molindone-specific publications** support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records (literature describes antipsychotic use in schizophrenia) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 records, all under one ANDA (ANDA090453) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Molindone is a dopamine D2 antagonist antipsychotic and is chemically unlike the phenothiazines, butyrophenones, and other older antipsychotic classes.

**The mechanistic link is weak.** Retinal dystrophies are mostly inherited disorders of photoreceptors or the retinal pigment epithelium. A symptomatic D2 blocker has no clear way to alter them. The very high score (99.998%) reflects a knowledge-graph association, not a biological rationale.

The 15 PubMed hits appear to be keyword matches on congenital eye and orbit anomalies. None of the 10 titles shown mentions molindone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these papers studies molindone or retinal dystrophy treatment. They are general ophthalmology reviews and case reports that match the disease keywords.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Orbital infections, mostly from sinusitis; imaging and clinical features |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Systematic approach to evaluating diplopia |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging of pediatric ocular pathologies, including congenital and developmental lesions |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens size, shape, and position |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis: forms, associated findings, therapy |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex (vitreoretinal degeneration with extraocular features) |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Congenital cranial dysinnervation disorders and ophthalmoplegia |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Observational study | Int J Mol Sci | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two patients with unilateral cryptophthalmia |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090453 | Molindone Hydrochloride (Epic Pharma, LLC) | Tablet (oral) | Not stated in the record |

The pack contains three identical records for this authorization, shown here once.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. It has no trials, no molindone-specific literature, and no credible mechanism linking D2 antagonism to inherited retinal degeneration. The package insert warnings and mechanism of action are still missing, so safety screening cannot start.

**To proceed, the following is needed:**
- The package insert (warnings, contraindications, approved indication) for ANDA090453
- Mechanism of action data from DrugBank
- A mechanistic rationale or preclinical data linking molindone to retinal disease; without these, deprioritize this indication
- **Alternative lead:** the pack ranks *manic bipolar affective disorder* (score 99.984%) as more plausible through an antipsychotic class effect, at evidence level L4. It still lacks any molindone-specific trial. Neuroleptic malignant syndrome history and metabolic risk are safety considerations.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

