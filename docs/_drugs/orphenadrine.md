---
layout: default
title: Orphenadrine
parent: Model Prediction Only (L5)
nav_order: 997
evidence_level: L5
indication_count: 7
---

# Orphenadrine
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

# Orphenadrine: From Muscle Spasm to Retinal Dystrophy (Prediction Not Supported by Evidence)

## One-Sentence Summary

Orphenadrine is an anticholinergic muscle relaxant, used clinically for muscle spasm and for antipsychotic-induced extrapyramidal symptoms.
The TxGNN model ranks **retinal dystrophy with or without extraocular anomalies** as its top prediction (99.29%), but there are **0 clinical trials** and **15 publications**, none of which mention orphenadrine.
This is a graph-based prediction only, and the evidence supports **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records (clinically used for muscle spasm) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 (all listed as ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not, based on current data. Detailed mechanism of action data is not available in the Evidence Pack. Orphenadrine is known as an anticholinergic (muscarinic and H1 antagonist) with NMDA-antagonist and sodium-channel-blocking activity. None of these actions is known to act on inherited retinal dystrophy pathways.

The 0.993 score reflects proximity in the knowledge graph, not a biological link. The 15 retrieved papers cover congenital orbital and ocular anomalies (for example orbital infection, ptosis, congenital fibrosis of the extraocular muscles). They appear to be keyword matches on the disease name rather than drug evidence.

Other predictions in the list are equally weak: congenital glycosylation disorder, polymicrogyria, CMT1G and two X-linked myopia forms. Only one of them, **schizophrenia** (rank 5, score 99.13%), has drug-specific literature.

That literature is small clinical and naturalistic studies of orphenadrine in schizophrenia patients. It concerns adjunctive control of antipsychotic-induced extrapyramidal symptoms, not treatment of the core disease. The Cochrane reviews of anticholinergics for tardive dyskinesia show no clear benefit. Anticholinergic burden may also worsen cognition and tardive dyskinesia.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 15 papers retrieved for retinal dystrophy are listed below (10 shown). None mentions orphenadrine, and all are general ophthalmology literature.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Overview of orbital infections, mostly sinusitis-related; no orphenadrine data |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Approach to diagnosing double vision; no drug data |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging of pediatric ocular pathologies (microphthalmos, coloboma, Coats disease, etc.) |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape and size |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis forms and associated eye findings |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex with vitreoretinal degeneration |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Congenital cranial dysinnervation disorders causing ophthalmoplegia |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | Int J Mol Sci | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two patients with unilateral cryptophthalmia |

For reference, the most relevant orphenadrine literature sits under schizophrenia (adjunct use for extrapyramidal symptoms): [4571143](https://pubmed.ncbi.nlm.nih.gov/4571143/) (1972 RCT vs amantadine and placebo), [29341071](https://pubmed.ncbi.nlm.nih.gov/29341071/) (2018 Cochrane review on anticholinergics for tardive dyskinesia) and [3698889](https://pubmed.ncbi.nlm.nih.gov/3698889/) (1986 haloperidol plus orphenadrine study).

## US Market Information

17 authorizations are on record; 5 main ones are shown. The records do not include approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090585 | Orphenadrine Citrate (Sagent Pharmaceuticals) | Injection, solution | Not listed in the record |
| ANDA040284 | Orphenadrine Citrate (A-S Medication Solutions) | Tablet, extended release | Not listed in the record |
| ANDA040327 | Orphenadrine Citrate (Proficient Rx LP) | Tablet, extended release | Not listed in the record |
| ANDA040284 | Orphenadrine Citrate (NuCare Pharmaceuticals) | Tablet, extended release | Not listed in the record |
| ANDA040284 | Orphenadrine Citrate (Bryant Ranch Prepack) | Tablet, extended release | Not listed in the record |

Available routes are oral (extended-release tablet) and injectable.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The retinal dystrophy prediction rests on a graph score alone. There are no trials, and the retrieved literature is unrelated to orphenadrine. No plausible mechanistic link exists, and the other top-ranked predictions are similarly unsupported. Schizophrenia is the only prediction with drug-specific literature, and that literature concerns side-effect management, not disease treatment. At most it could be a research question, not a repurposing candidate.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (needed before any safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Any direct preclinical evidence linking orphenadrine to retinal degeneration pathways; without it, deprioritize this indication
- For schizophrenia, a defined question that accounts for anticholinergic burden, cognition and tardive dyskinesia risk

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

