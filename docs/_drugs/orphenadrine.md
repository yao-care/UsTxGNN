---
layout: default
title: Orphenadrine
parent: 僅模型預測 (L5)
nav_order: 997
evidence_level: L5
indication_count: 7
---

# Orphenadrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Orphenadrine: From Skeletal Muscle Relaxant to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

> Orphenadrine is an anticholinergic/antihistaminic skeletal muscle relaxant, with no formal original-indication or Taiwan/US license record available in this evidence pack.
> The TxGNN model predicts a possible link to **Retinal Dystrophy with or without Extraocular Anomalies**,
> but this is a **pure knowledge-graph similarity prediction** — **0 clinical trials** and **no literature directly connecting orphenadrine to this disease** currently exist.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — no Taiwan/US approved license data available |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for orphenadrine is not available in this evidence pack. Based on notes embedded elsewhere in the evidence (see the schizophrenia candidate below), orphenadrine is an anticholinergic/antihistaminic skeletal muscle relaxant, clinically used as an adjunct for muscle spasm and to counteract antipsychotic-induced extrapyramidal symptoms. No pharmacological pathway connecting this mechanism to retinal development or congenital extraocular anomalies is known.

The evidence pack itself flags this specific prediction as unsupported: *"TxGNN score is high but represents only KG-embedding similarity inference — no genuine mechanistic connection has been identified."* The 15 literature items retrieved for this indication are general reviews and case reports on orbital/ocular pathology and congenital dysinnervation disorders; none discuss orphenadrine specifically or any drug-disease mechanism.

For context, among the seven predicted indications in this pack, only **schizophrenia** (rank 5) has meaningful literature support (multiple cohort studies and two Cochrane systematic reviews, L3). However, that literature supports orphenadrine as an **adjunct for antipsychotic-induced extrapyramidal side effects**, not as a treatment for schizophrenia itself — an important distinction for any future evaluation of this drug's repurposing potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | General review of orbital infections; not orphenadrine-specific |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Clinical approach to diplopia; not drug-related |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging review of pediatric orbital/ocular pathologies |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Review of congenital ptosis |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Unilateral cryptophthalmia case description |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome vitreoretinal degeneration |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | Int J Mol Sci | Optic nerve/retinal abnormalities in congenital extraocular muscle fibrosis |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Congenital cranial dysinnervation disorders overview |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Pathogenesis of maculopathy with cavitary optic disc anomalies |

**Note:** None of the above literature discusses orphenadrine or any pharmacological intervention for this disease — all items are general disease-background references retrieved by the model.

---

## US Market Information

No marketing authorization (NDA) records are currently available for orphenadrine in this jurisdiction. Market status is recorded as **未上市 (Not Marketed)**, with **0 total licenses**.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are marked as data gaps in this evidence pack — notably DG001, classified as **Blocking** for any S1 safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by TxGNN knowledge-graph embedding similarity (L5), with zero clinical trials and no literature that mechanistically or clinically links orphenadrine to retinal dystrophy. There is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA-approved label warnings/contraindications (DG001 — blocking; required before any safety review)
- Confirmed mechanism of action (DG002) to assess biological plausibility
- Independent mechanistic or preclinical evidence specifically linking orphenadrine to retinal/extraocular developmental pathways
- If repurposing interest continues, consider re-scoping toward the schizophrenia/EPS-adjunct candidate (rank 5, L3 evidence), while clearly framing it as symptomatic management of antipsychotic-induced movement disorders rather than a schizophrenia treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

