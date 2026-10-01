---
layout: default
title: Prochlorperazine
parent: Model Prediction Only (L5)
nav_order: 1088
evidence_level: L5
indication_count: 10
---

# Prochlorperazine
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

# Prochlorperazine: From Nausea/Vomiting and Psychosis to Retinal Dystrophy (Prediction Not Supported)

## One-Sentence Summary

Prochlorperazine is a phenothiazine dopamine antagonist that is widely marketed in the US. It is generally known as an antiemetic and antipsychotic, although the license records in this data do not list indication text.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are **0 clinical trials** and **0 relevant publications** supporting this. The 15 retrieved papers are general eye-disease articles that do not study the drug.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license data (generally known use: severe nausea/vomiting and psychosis, based on general knowledge rather than the Evidence Pack) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.998% (model rank 138) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Prochlorperazine is a phenothiazine antipsychotic and antiemetic that works mainly by blocking dopamine D2 receptors.

The expert review found **no credible mechanistic link** between D2 antagonism and retinal dystrophy pathways. The 99.998% score comes from a graph-based prediction only, and a high score here does not indicate real efficacy.

The safety signal also points the wrong way. Phenothiazines are associated with retinal toxicity (pigmentary retinopathy), mainly with thioridazine and chlorpromazine at high doses. This argues against benefit in a retinal disease and raises a possible harm concern.

## Clinical Trial Evidence

Currently no related clinical trials registered (neither ClinicalTrials.gov nor ICTRP).

## Literature Evidence

None of the retrieved papers evaluates prochlorperazine in retinal dystrophy. They are general articles on eye and orbital conditions, and all are tagged "relevance: pending". None can be counted as supporting evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Orbital infections, most commonly from sinusitis; no drug-specific content |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Systematic approach to evaluating diplopia |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging features of pediatric ocular pathologies (e.g., Coats disease, retinopathy of prematurity) |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis: forms and examination |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex (vitreoretinal degeneration) |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Congenital cranial dysinnervation disorders and ophthalmoplegia |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | Int J Mol Sci | Optic nerve head and retinal abnormalities in congenital fibrosis of extraocular muscles |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two cases of unilateral cryptophthalmia |

## US Market Information

The source data does not provide approved indication text for any of these licenses. The full list contains 20 authorizations; the five main ones are shown.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA216495 | Prochlorperazine Maleate (Zydus Lifesciences) | Tablet | Not specified in source data |
| ANDA040268 | Prochlorperazine Maleate (Northwind Health) | Tablet | Not specified in source data |
| ANDA040101 | Prochlorperazine Maleate (Chartwell RX) | Tablet, film coated | Not specified in source data |
| ANDA204147 | Prochlorperazine Edisylate (Avenacy) | Injection, solution | Not specified in source data |
| ANDA216202 | Prochlorperazine Maleate (Major Pharmaceuticals) | Tablet | Not specified in source data |

Other available forms include injection and suppository.

## Safety Considerations

- **Retinal toxicity concern**: Phenothiazines as a class have been linked to pigmentary retinopathy, mainly thioridazine and chlorpromazine at high doses. This is a particular concern for any retinal indication.
- **Drug Interactions**: The DDI query returned no records.

Please refer to the package insert for warnings and contraindications, which are not available in the Evidence Pack. This gap is flagged as blocking for safety screening.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials and no relevant literature, and the mechanism is implausible. The known retinal toxicity of phenothiazines argues against benefit. The evidence level is L5.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap)
- Mechanism-of-action data from DrugBank
- Any preclinical evidence linking dopamine antagonism to retinal degeneration, or an explanation of why the model ranks this indication so high
- Retinal safety review for prochlorperazine

**Note on other predictions for this drug:** The same model output also ranks **manic bipolar affective disorder** (score 99.979%, model rank 1047). Its evidence level is L4 and it is at stage S1 as a "Research Question". It is biologically plausible, since D2-antagonist antipsychotics are established for acute mania. However, the literature is historical and indirect, with no trials and no drug-specific efficacy data. Better-characterized alternatives exist. Any follow-up should start with a safety review covering seizure risk, tardive dyskinesia, and metabolic effects.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

