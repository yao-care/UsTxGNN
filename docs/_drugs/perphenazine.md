---
layout: default
title: Perphenazine
parent: Model Prediction Only (L5)
nav_order: 1033
evidence_level: L5
indication_count: 10
---

# Perphenazine
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

# Perphenazine: From Its Approved Use to Retinal Dystrophy (with or without Extraocular Anomalies)

## One-Sentence Summary

Perphenazine is a marketed oral phenothiazine drug, but the Evidence Pack does not record its original indication.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but this rests on a graph-based score alone, with **0 clinical trials** and **no relevant publications**.
The 15 retrieved papers match only the disease term and never mention perphenazine, so this prediction should be treated as unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.96% (model rank 1544) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed below are all ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, perphenazine is a phenothiazine-class drug. It blocks D2, 5-HT2A, H1 and alpha-1 receptors. No mechanism connects these actions to retinal dystrophy.

The 0.9996 score is best read as graph proximity in the knowledge graph, not as biological or clinical support. The retrieved literature covers orbital infections, congenital ptosis, extraocular muscle disorders and similar topics. None of it involves perphenazine.

The clinical signal actually points the other way. Phenothiazines, mainly thioridazine, are known for retinal toxicity, so this is a safety concern rather than a reason to expect benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these papers mention perphenazine. They matched only on the disease terms.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Orbital infections, most often from sinusitis. Not related to perphenazine. |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Approach to diagnosing diplopia. Not related to perphenazine. |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging of pediatric ocular pathologies. Not related to perphenazine. |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape. Not related to perphenazine. |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis. Not related to perphenazine. |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex. Not related to perphenazine. |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Ophthalmoplegia and congenital cranial dysinnervation disorders. Not related to perphenazine. |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Maculopathy with cavitary optic disc anomalies. Not related to perphenazine. |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Case series | Int J Mol Sci | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles. Not related to perphenazine. |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two cases of unilateral cryptophthalmia. Not related to perphenazine. |

---

## US Market Information

The pack gives no approved-indication text for these licenses.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA210163 | PERPHENAZINE | Tablet | REMEDYREPACK INC. |
| ANDA205973 | Perphenazine | Tablet, film coated | Bryant Ranch Prepack |
| ANDA040226 | Perphenazine | Tablet, film coated | Endo USA, Inc. |
| ANDA205973 | Perphenazine | Tablet, film coated | REMEDYREPACK INC. |

Only oral tablet forms are listed.

---

## Safety Considerations

- **Retinal toxicity:** Phenothiazines, mainly thioridazine, are associated with retinal toxicity. This is a concern for any retinal indication.

Please refer to the package insert for other safety information. The pack has no warning or contraindication data, and no drug interactions were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no relevant literature and no plausible mechanism. The known retinal toxicity of related phenothiazines argues against benefit. Package insert safety data is also missing, which blocks any safety screening.

**Other predictions in the pack:** The only candidate with some support is **anxiety disorder** (rank 10, score 99.53%, L3). It has historical, mostly combination-based literature, such as perphenazine with amitriptyline. Neither listed trial tests perphenazine directly for anxiety. It is worth evaluating separately as a research question, weighed against sedation and extrapyramidal risks.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap)
- Detailed mechanism of action data from DrugBank
- The original approved indication, which the pack does not record
- Evidence of a direct perphenazine link to the retinal condition, or de-prioritization of this prediction in favor of higher-evidence candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

