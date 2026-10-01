---
layout: default
title: Chlorpromazine
parent: Model Prediction Only (L5)
nav_order: 523
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
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

# Chlorpromazine: From Schizophrenia (Presumed) to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Chlorpromazine is a first-generation antipsychotic. The data provided does not state its original indication, but it is presumed to be schizophrenia.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**.
There are **0 clinical trials** and **15 publications** on this disease, and none of the publications studies chlorpromazine, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US label data provided (presumed schizophrenia) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database record. The evidence assessment describes chlorpromazine as an antagonist of dopamine D2, histamine H1, muscarinic and alpha-1 receptors. That profile explains its use as an antipsychotic.

**This prediction is not mechanistically credible.** Retinal dystrophies with extraocular anomalies are mostly monogenic structural or degenerative conditions. Chlorpromazine has no known target or pathway that would treat them. The very high TxGNN score (0.9995) appears to reflect proximity in the knowledge graph rather than a therapeutic rationale.

Chlorpromazine is also known to cause ocular side effects, including lens and corneal deposits and, rarely, pigmentary retinopathy. A safety signal in the eye is therefore more plausible than a benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 15 retrieved publications are background papers on eye and orbit disorders. None of them evaluates chlorpromazine. The table lists the 10 most relevant, with reviews first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Orbital infections, mostly sinusitis-related, and how they present |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic approach to evaluating double vision |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric ocular pathologies (e.g. coloboma, Coats disease) |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis and its association with refractive errors |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler vitreoretinal degeneration and its extraocular features |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocular Vision and Ocular Motility | Congenital cranial dysinnervation disorders causing ophthalmoplegia |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | American Journal of Ophthalmology | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Case series | Int J Mol Sciences | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two patients with unilateral cryptophthalmia |

---

## US Market Information

There are 20 US authorizations in total. Five entries were returned, which reduce to two distinct ANDAs. Approved indication text was not included in the data.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA217350 | Chlorpromazine | Tablet | Alembic Pharmaceuticals Limited |
| ANDA214256 | ChlorproMAZINE Hydrochloride | Tablet, sugar coated | Sun Pharmaceutical Industries Inc |

Other forms on the US market: film-coated tablets, coated tablets and injection.

---

## Safety Considerations

- **Ocular safety signal**: Chlorpromazine is known to cause lens and corneal deposits and, rarely, pigmentary retinopathy. This is a concern for any use in retinal disease. It comes from the evidence assessment's rationale, not from label data.
- **Drug Interactions**: The database returned no interaction records.

Please refer to the package insert for key warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no relevant literature and no plausible mechanism. The only known ocular effect of chlorpromazine is harmful. The high TxGNN score reflects graph proximity, not therapeutic evidence.

Among this drug's other predictions, only early-onset schizophrenia has any supporting material (L3, Research Question). It is probably an existing labeled use rather than true repurposing. The other predictions are all L5 with no supporting evidence.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications, approved indications), which blocks safety screening
- Confirmed mechanism of action data from DrugBank
- The drug's original indication, which the record leaves empty
- Any preclinical or clinical evidence linking chlorpromazine to retinal dystrophy, and an ocular toxicity assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

