---
layout: default
title: Iloperidone
parent: Model Prediction Only (L5)
nav_order: 789
evidence_level: L5
indication_count: 10
---

# Iloperidone
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

# Iloperidone: From Schizophrenia to Retinal Dystrophy With or Without Extraocular Anomalies

## One-Sentence Summary

Iloperidone is an atypical antipsychotic that the published literature describes as approved for schizophrenia.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but this is a graph-based prediction only, with **0 clinical trials** and **15 publications**, none of which mention iloperidone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (from published literature; the license records contain no indication text) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.999% (rank 52 in the model's list) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 18 license records (2 unique authorizations) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on the literature, iloperidone is a benzisoxazole atypical antipsychotic that acts as a serotonin/dopamine (5-HT2A/D2) antagonist, with alpha-1 adrenergic blockade.

No plausible link was found between this receptor profile and inherited retinal dystrophy, which is a genetic degenerative eye condition. The high score (0.99999) comes from the knowledge graph alone. The 15 retrieved papers cover congenital orbital and ocular anomalies (for example orbital infections, congenital fibrosis of the extraocular muscles, and lens shape anomalies). They do not mention iloperidone, so they appear to be keyword matches on the disease name rather than drug evidence.

The same pack lists 9 other high-scoring predictions, and all have no clinical trials. They are:

- congenital disorder of glycosylation with defective fucosylation
- hydranencephaly
- Charcot-Marie-Tooth disease type 1G
- perisylvian polymicrogyria
- three myopia variants
- atypical glycine encephalopathy

Only the tenth prediction, **manic bipolar affective disorder**, has real support. It has 1 completed Phase 4 trial and a Phase 3 placebo-controlled RCT (PMID 38236020), and iloperidone is reported to already have a 2024 bipolar I mania indication. That is closer to a label extension than a new repurposing finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the papers below study iloperidone. They are general ophthalmology literature matched by disease keywords.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | Int J Mol Sci | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles (KIF21A/TUBB3 variants) |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Orbital infections, most commonly from sinusitis |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Systematic approach to diagnosing diplopia |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex: vitreoretinal degeneration with extraocular features |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis and its association with refractive errors |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Ophthalmoplegia and congenital cranial dysinnervation disorders |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging of pediatric ocular pathologies |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two patients with unilateral cryptophthalmia |

## US Market Information

The 18 license records collapse to 2 unique authorizations. The records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA022192 | FANAPT | Tablet (oral) | Vanda Pharmaceuticals Inc. |
| ANDA207231 | ILOPERIDONE | Tablet (oral) | Mylan Pharmaceuticals Inc. |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the query, which is likely a data gap rather than evidence of no interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The retinal dystrophy prediction rests only on a graph score. There are no trials, the retrieved literature is unrelated to iloperidone, and no mechanistic link was identified. Systemic antipsychotic exposure would also raise safety concerns for a chronic eye condition.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking iloperidone to retinal degeneration, which is currently absent
- Consider redirecting attention to the bipolar mania prediction (rank 10), which is Proceed with Guardrails at L1. The guardrails are QTc prolongation, metabolic and weight effects, orthostatic hypotension, and CYP2D6/3A4 interactions.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

