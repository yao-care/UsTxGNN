---
layout: default
title: Fluphenazine
parent: Model Prediction Only (L5)
nav_order: 725
evidence_level: L5
indication_count: 10
---

# Fluphenazine
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

# Fluphenazine: From Antipsychotic Use to Retinal Dystrophy (With or Without Extraocular Anomalies)

## One-Sentence Summary

Fluphenazine is a phenothiazine antipsychotic that acts as a dopamine D2 antagonist and is marketed in the US in oral, injectable and elixir forms.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are **0 clinical trials** and **no literature on fluphenazine for this condition**.
This is a graph-based prediction only, and phenothiazines are known to cause retinal toxicity, which argues against this use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antipsychotic use (indication text is not provided in the US license data) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.99% (model rank 321) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Fluphenazine is a high-potency phenothiazine and a D2 dopamine receptor antagonist.

The review found **no plausible mechanistic link** between D2 antagonism and the genetic or structural pathology of retinal dystrophy. The high TxGNN score (0.9999) reflects only a pattern in the knowledge graph, not biological or clinical support.

Phenothiazines are also known to cause retinal toxicity (pigmentary retinopathy). This is a reason for caution, not support for the prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 15 retrieved publications were matched on disease keywords (orbital, extraocular and congenital eye disorders). **None of them studies fluphenazine or any phenothiazine in retinal dystrophy.** The 10 below are the closest in topic, and all are background reading only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Orbital infections, mainly sinusitis-related; imaging and clinical signs |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Systematic approach to evaluating diplopia |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Differential diagnosis and imaging of pediatric ocular pathologies |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis and its associated findings |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex (vitreoretinal degeneration) |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Ophthalmoplegia and congenital cranial dysinnervation disorders |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | Int J Mol Sci | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two cases of unilateral cryptophthalmia |

## US Market Information

Of 20 authorizations, the 5 listed in the Evidence Pack are shown below. All are generic (ANDA) tablets.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA218173 | Fluphenazine Hydrochloride (Alembic) | Film-coated tablet | — |
| ANDA213647 | Fluphenazine Hydrochloride (Amneal) | Film-coated tablet | — |
| ANDA218055 | Fluphenazine Hydrochloride (Aurobindo) | Tablet | — |
| ANDA214534 | Fluphenazine Hydrochloride (American Health Packaging) | Film-coated tablet | — |
| ANDA217410 | Fluphenazine Hydrochloride (Ajanta) | Tablet | — |

Other US dosage forms for this drug are injection solution and elixir.

## Safety Considerations

- **Retinal toxicity**: Phenothiazines are known to cause pigmentary retinopathy. This directly conflicts with use in a retinal disease.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). There are no trials, no fluphenazine-specific literature and no plausible mechanism. The known retinal toxicity of phenothiazines argues against this indication.

**To proceed, the following is needed:**
- A defined mechanistic hypothesis that addresses the retinal toxicity concern, backed by preclinical data
- Full package insert warnings and contraindications
- Mechanism-of-action data from DrugBank

**Note on other predictions:** Of the 10 predicted indications, only rank 10, **manic bipolar affective disorder** (score 99.98%), has a plausible mechanism. Dopamine antagonism underlies the antimanic effect of the antipsychotic class, and class-level reviews and retrospective data support long-acting injectable antipsychotics in bipolar disorder. Fluphenazine-specific evidence is limited to one two-patient case report, so this is a class-effect inference. It is rated L4 and best treated as a research question, and it would be the better candidate for a follow-up report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

