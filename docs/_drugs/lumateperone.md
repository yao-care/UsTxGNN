---
layout: default
title: Lumateperone
parent: Model Prediction Only (L5)
nav_order: 877
evidence_level: L5
indication_count: 9
---

# Lumateperone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Lumateperone: From Antipsychotic Therapy to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Lumateperone is an oral antipsychotic marketed in the US as CAPLYTA.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but this rests on the model score alone: **0 clinical trials** are registered, and none of the **15 retrieved publications** studies lumateperone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available label data (drug is classed as an antipsychotic) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all listings under NDA209500) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Lumateperone is an antipsychotic. It acts mainly as a 5-HT2A antagonist, a D2 receptor modulator and a serotonin reuptake inhibitor.

**The mechanistic link is weak.** Inherited retinal dystrophy is driven by gene defects in photoreceptors and the retinal pigment epithelium. No known pathway connects lumateperone's targets to that biology. The 99.97% score is a graph-based prediction only and cannot be cross-checked against mechanism data.

The 15 retrieved papers cover general ophthalmology and orbital topics, such as congenital extraocular muscle disorders, orbital infections and lens anomalies. Based on their titles and abstracts, none evaluates lumateperone or related agents, so they are not drug-specific evidence.

The other eight predictions for this drug (polymicrogyria, hydranencephaly, CMT1G, three X-linked/syndromic myopia entries, a congenital glycosylation disorder and atypical glycine encephalopathy) show the same pattern. All are L5 with no trials or literature and no identified mechanistic link. The three myopia entries have near-identical scores, which suggests correlated predictions from shared graph neighbours rather than independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomized trials were found. The table below lists 10 of the 15 papers, with reviews given priority. All are general disease background, and none tests lumateperone.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and imaging features of pediatric ocular pathologies (e.g., coloboma, Coats disease) |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape and associated anterior segment findings |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Congenital cranial dysinnervation disorders causing ophthalmoplegia |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | American Journal of Ophthalmology | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis and its association with refractive errors |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic approach to evaluating diplopia |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Orbital infections, mostly secondary to sinusitis |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex (vitreoretinal degeneration with extraocular features) |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Observational study | International Journal of Molecular Sciences | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia |

## US Market Information

The record contains three CAPLYTA listings under one NDA, with the same manufacturer and dosage form.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209500 | CAPLYTA (Intra-Cellular Therapies, Inc) | Capsule (oral) | Not provided in the available data |

## Safety Considerations

Please refer to the package insert for safety information. No warnings or contraindications were retrieved, and no drug-drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score. There are no trials, no drug-specific literature and no plausible mechanism linking lumateperone's targets to retinal dystrophy. Package insert safety data are also missing, so the candidate cannot pass the first safety screen.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence connecting lumateperone's targets to retinal biology
- Any drug-specific studies in retinal disease, and the label-approved indications for the original-indication baseline
- Independent review of the correlated myopia predictions before treating them as separate signals

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

