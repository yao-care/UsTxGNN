---
layout: default
title: Paliperidone
parent: Model Prediction Only (L5)
nav_order: 1010
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy (With or Without Extraocular Anomalies)

## One-Sentence Summary

Paliperidone is an atypical antipsychotic (a D2/5-HT2A antagonist) used for schizophrenia.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but **0 clinical trials** and **15 retrieved publications** support this direction, and none of those publications mentions paliperidone.
The high score looks like a knowledge-graph artifact rather than a real signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (from drug class knowledge; the license records contain no indication text) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (license records, including ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Paliperidone (9-hydroxyrisperidone) is a dopamine D2 and serotonin 5-HT2A receptor antagonist. Detailed mechanism-of-action data is not populated in the DrugBank field of this Evidence Pack, so this description comes from the drug's known pharmacology.

Nothing in this mechanism connects to inherited retinal degeneration. Retinal dystrophies are mostly monogenic disorders of photoreceptor or retinal pigment epithelium function, and blocking D2/5-HT2A receptors is not expected to change that course. The 15 papers retrieved for this prediction are general ophthalmology and congenital eye anomaly papers (orbital infections, diplopia, congenital ptosis, extraocular muscle disorders). None discusses paliperidone or any antipsychotic.

The score of 0.999 (rank 2706) is therefore best read as a graph-structure artifact, not evidence of therapeutic potential. The other top-ranked predictions (X-linked myopia, hydranencephaly, glycosylation disorders and others) show the same pattern of high scores with no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomized trials were found. The retrieved papers are reviews, one case series and one case report, all on general eye conditions and none on paliperidone.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections. Sinusitis is the most common cause, and cellulitis is described in five stages. |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic approach to history and examination of patients with double vision. |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and imaging features of pediatric ocular pathologies. |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens size, shape and position. |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis and its association with refractive errors and binocular vision problems. |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex, a vitreoretinal degeneration with extraocular features. |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Congenital cranial dysinnervation disorders that cause ophthalmoplegia. |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | American Journal of Ophthalmology | Pathogenesis and treatment of maculopathy associated with cavitary optic disc anomalies. |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Case series | International Journal of Molecular Sciences | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles. |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two patients with unilateral cryptophthalmia. |

## US Market Information

Five of the 20 licenses are shown. The license records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA218755 | Paliperidone (Eskayef Pharmaceuticals) | Tablet, extended release | Not listed in record |
| ANDA218330 | Paliperidone (Alembic Pharmaceuticals) | Tablet, extended release | Not listed in record |
| NDA207946 | INVEGA TRINZA (Janssen) | Injection, suspension, extended release | Not listed in record |
| ANDA218514 | Paliperidone (Ajanta Pharma USA) | Tablet, extended release | Not listed in record |
| NDA022264 | INVEGA SUSTENNA (Janssen) | Injection | Not listed in record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no paliperidone-specific literature and no plausible mechanistic link to retinal dystrophy, so it stays at evidence level L5 (model prediction only). The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- A mechanistic hypothesis linking D2/5-HT2A antagonism to retinal or photoreceptor biology, supported by preclinical data.
- Package insert warnings and contraindications, which are missing and block any safety screening.
- Approved-indication text in the license records. The original indication is currently inferred from drug class.

**Note on another prediction in this pack:** The rank 10 prediction, treatment-refractory schizophrenia, is biologically plausible and has 4 Phase 4 trials plus 2 reviews (evidence level L3). It is close to the drug's on-label use, so it may not count as true repurposing. Confirm the indication scope against the label before pursuing it.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

