---
layout: default
title: Asenapine
parent: Model Prediction Only (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Asenapine
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

# Asenapine: From Schizophrenia and Bipolar I Disorder to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Asenapine is an atypical antipsychotic used for schizophrenia and manic or mixed episodes of bipolar I disorder. The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies** (score 99.77%), but **0 clinical trials** and **0 relevant publications** support this prediction. The 15 retrieved papers are general eye and orbit articles that never mention asenapine, so this is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia and manic or mixed episodes of bipolar I disorder (from published literature; the US license records in the pack contain no indication text) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (generic ANDA licenses) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank record for this pack. Published reviews describe asenapine as a multi-receptor antipsychotic. It binds serotonin 5-HT2A and dopamine D2 receptors, with higher affinity for 5-HT2A, and also acts on histamine and muscarinic receptors. It has reported effects on NMDA and AMPA signaling as well.

I could not identify a plausible link between this pharmacology and inherited retinal degeneration or ocular developmental disorders. Nothing in the data connects asenapine to the genetic or developmental pathways of retinal dystrophy. The high score of 99.77% comes only from the knowledge-graph model. The literature retrieved for this prediction appears to be keyword-match noise: reviews on orbital infections, diplopia, congenital ptosis and similar topics.

For context, this run also produced nine other low-evidence predictions, such as hydranencephaly, several myopia subtypes and Charcot-Marie-Tooth type 1G. None of them has a mechanistic link or trial data either. The only prediction in the pack with real evidence is **major affective disorder** (rank 10). It has four registered trials, including completed Phase 3 RCTs in bipolar I mania, and is very likely an existing labeled use rather than true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the papers below concerns asenapine. They are general ophthalmology and congenital anomaly articles, and no RCTs were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections, with sinusitis as the most common cause |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic approach to evaluating patients with double vision |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric ocular pathologies (e.g., coloboma, Coats disease) |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis and associated eye problems |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex of vitreoretinal degeneration |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Congenital cranial dysinnervation disorders causing ophthalmoplegia |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | American Journal of Ophthalmology | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | International Journal of Molecular Sciences | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia |

## US Market Information

Three unique licenses appear among the five records; the pack lists two of them twice. The approved indication text is empty in all of them. Asenapine is also listed in an extended-release film form under a non-oral route.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA205960 | Asenapine (Breckenridge Pharmaceutical, Inc.) | Tablet | Not listed in source record |
| ANDA205960 | Asenapine (MSN Laboratories Private Limited) | Tablet | Not listed in source record |
| ANDA206107 | Asenapine (Sigmapharm Laboratories, LLC) | Tablet | Not listed in source record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for asenapine in the pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The retinal dystrophy prediction rests only on a knowledge-graph score. It has no clinical trials, no relevant literature and no plausible mechanistic link to asenapine's receptor pharmacology (evidence level L5, stage S0). Package insert warnings are also missing, so safety screening cannot start.

**To proceed, the following is needed:**
- A credible biological hypothesis linking asenapine's receptor activity to retinal degeneration, plus a targeted literature search that uses asenapine terms rather than disease keywords
- Preclinical evidence in a retinal dystrophy model, if the hypothesis holds up
- The FDA package insert, to fill the warnings and contraindications gap
- Mechanism-of-action data from DrugBank
- A separate review of the major affective disorder prediction, which has Phase 3 evidence but is probably an on-label use, so the labeled indication scope needs confirming first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

