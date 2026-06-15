---
layout: default
title: Aripiprazole Lauroxil
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 9
---

# Aripiprazole Lauroxil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Aripiprazole Lauroxil: From Schizophrenia to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

Aripiprazole Lauroxil (Aristada) is a long-acting injectable prodrug of aripiprazole, approved in the United States for schizophrenia treatment in adults.
The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**, with **0 clinical trials** and **15 background-only publications** (none directly evaluating this drug-indication pair) available.
The mechanistic rationale is assessed as absent, and this candidate is classified as **Hold** at evidence stage L5/S0.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia (US FDA-approved as Aristada; not registered in Taiwan) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Aripiprazole Lauroxil is a fatty acid ester prodrug of aripiprazole. After intramuscular injection, it is slowly cleaved in muscle tissue to release aripiprazole, which acts as a partial agonist at dopamine D2/D3 receptors and serotonin 5-HT1A receptors, and as an antagonist at 5-HT2A receptors. This mechanism underlies its antipsychotic efficacy in schizophrenia. Full mechanism of action data (MOA) was not retrieved during this evidence collection cycle and remains a data gap.

The TxGNN model's prediction may reflect a biological signal embedded in its knowledge graph: the retina contains a dopaminergic sub-network (dopaminergic amacrine cells), and retinal dopamine signaling influences eye development, photoresponse adaptation, and potentially axial elongation. Some basic research has explored dopamine's role in retinal function and myopia, which could explain why a dopaminergic compound ranks among predictions for retinal and extraocular conditions.

However, expert assessment of the mechanistic rationale is clear: **retinal dystrophies are primary genetic disorders** causing progressive photoreceptor degeneration (e.g., through mutations in RPGR, PRPF31, USH2A), with pathophysiology that is independent of dopaminergic signaling. There is no established pharmacological pathway by which aripiprazole's receptor-level activity could prevent or reverse hereditary photoreceptor loss. The high TxGNN score (99.99%) appears to reflect a knowledge graph topology artifact rather than a pharmacologically grounded repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The following publications were retrieved by PubMed search combining aripiprazole lauroxil with retinal dystrophy / extraocular anomalies. **None directly evaluate aripiprazole or its prodrug for retinal dystrophy.** They represent background ophthalmology literature on extraocular anomalies and ocular development; relevance to this repurposing hypothesis is pending and likely low.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and key imaging features of pediatric ocular pathologies, including congenital/developmental lesions, optic disc drusen, and retinopathy of prematurity |
| [36892533](https://pubmed.ncbi.nlm.nih.gov/36892533/) | 2023 | Genetic study | Investigative Ophthalmology & Visual Science | Monoallelic MAB21L1 missense mutations cause autosomal dominant BAMD syndrome with blepharophimosis, anterior segment dysgenesis, and macular dysgenesis |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape, with discussion of association with anterior segment dysgenesis and persistence of fetal vasculature |
| [36116851](https://pubmed.ncbi.nlm.nih.gov/36116851/) | 2022 | Review | Seminars in Ultrasound, CT, and MR | Anatomy and MRI pathology of the oculomotor nerve; parasympathetic fibers controlling sphincter pupillae and ciliary muscles |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Congenital cranial dysinnervation disorders (CCDDs) arising from cranial nucleus/nerve developmental defects; substantial limitations of ocular motility |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | American Journal of Ophthalmology | Pathogenesis of maculopathy associated with cavitary optic disc anomalies and proposed rational approach for permanent cure |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | Journal of Neuro-Ophthalmology | Isolated trochlear-oculomotor synkinesis in a 6-year-old boy; rare subset of congenital cranial dysinnervation disorders |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Clinical review | Seminars in Neurology | Systematic approach to history and examination for diplopia across ocular, neurologic, and extraocular muscle disorders |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Case series | Documenta Ophthalmologica | Wagner-Stickler syndrome: vitreoretinal degeneration with myopia, optically empty vitreous, and high-risk retinal detachment; evidence for phenotypic variability with sensorineural deafness and skeletal dysplasia |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review/Case series | Seminars in Ultrasound, CT, and MR | Five-stage classification of orbital cellulitis secondary to sinusitis; systemic predisposing conditions including diabetes and immunosuppression |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top TxGNN predictions for aripiprazole lauroxil map to rare genetic or structural conditions — hereditary retinal dystrophies, brain malformations, inherited peripheral neuropathies, and glycosylation defects — none of which have an established pharmacological connection to aripiprazole's dopaminergic/serotonergic mechanism of action. The highest-ranked prediction (retinal dystrophy with extraocular anomalies) has zero supporting clinical trials, no directly relevant published studies, and an expert-assessed absent mechanistic link. An L5 evidence level at decision stage S0 does not justify further resource allocation for any of the 9 predicted indications in this pack.

**To proceed, the following is needed:**

- **Mechanistic hypothesis**: Establish a biologically plausible pathway by which aripiprazole's receptor pharmacology could influence photoreceptor survival or retinal dystrophy progression before any preclinical studies are initiated
- **MOA data retrieval**: Query DrugBank API to complete the mechanism of action record (currently a High-severity data gap)
- **Knowledge graph audit**: Investigate whether the TxGNN predictions reflect true pharmacological signals or are driven by shared disease ontology node topology (e.g., "extraocular anomalies" serving as a bridge between unrelated disease clusters)
- **Deprioritization**: Without a plausible mechanism or at minimum preliminary in vitro / in vivo data, none of the 9 predicted indications in this pack should advance to the S1 safety assessment phase
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

