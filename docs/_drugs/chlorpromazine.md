---
layout: default
title: Chlorpromazine
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using `txgnn-pipeline` to check report generation context — confirmed this is a standard Evidence Pack to evaluation report task. Proceeding to generate the report.

---

# Chlorpromazine: From Schizophrenia to Early-Onset Schizophrenia

## One-Sentence Summary

Chlorpromazine, the world's first synthesized antipsychotic (phenothiazine class), has been used since the 1950s to manage schizophrenia and acute psychotic episodes in adults.
The TxGNN model generates 10 predicted indications; the most clinically supported prediction is **Early-Onset Schizophrenia** (onset before age 18),
with **1 clinical trial** and **8 publications** providing contextual evidence — though the drug's pediatric safety profile (particularly extrapyramidal symptoms) demands careful evaluation before any research initiation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia and psychotic disorders (no current Taiwan registration) |
| Predicted New Indication | Early-Onset Schizophrenia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registered Products | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Chlorpromazine is a phenothiazine-class first-generation (typical) antipsychotic. Its core mechanism involves antagonism of dopamine D2/D3/D4 receptors in the mesolimbic pathway, which suppresses positive psychotic symptoms — hallucinations, delusions, and thought disorganization. It also blocks histamine H1, muscarinic M1, and α1-adrenergic receptors, accounting for its sedative and anticholinergic side effect profile.

Early-onset schizophrenia (EOS, onset < 18 years) shares the same fundamental pathophysiology as adult schizophrenia: mesolimbic dopamine hyperactivity and mesocortical hypodopaminergia. The mechanistic rationale for chlorpromazine's activity is therefore directly transferable. Historically, chlorpromazine was used in pediatric and adolescent psychiatric settings before second-generation antipsychotics (SGAs) became widely available. It was phased out of pediatric practice not due to inefficacy, but because extrapyramidal symptoms (EPS) and tardive dyskinesia occur with greater frequency and severity in younger patients. Pharmacogenomic studies on BDNF (Val66Met) and AKT1 variants suggest potential biomarkers for predicting both chlorpromazine response and EPS risk — offering a possible precision psychiatry research angle.

> Currently, detailed mechanism of action data is not available from the data source (DrugBank API query pending). The mechanistic reasoning above is based on established pharmacological knowledge for the phenothiazine class.

---

## ⚠️ Note on Top-Ranked TxGNN Predictions

TxGNN assigns the 9 highest prediction scores to indications other than early-onset schizophrenia. However, expert mechanistic review finds **all 9 are "Hold"** — several with actively contradictory rationale. This section summarises why they were set aside in favour of rank 10 as the primary focus of this report.

| Rank | TxGNN Score | Disease | Primary Concern |
|------|------------|---------|----------------|
| 1 | 99.95% | Retinal dystrophy with extraocular anomalies | Phenothiazines **cause** retinal toxicity (>800 g cumulative) — therapeutically opposite |
| 2 | 99.94% | CDG with defective fucosylation | No link to fucosylation or GDP-fucose synthesis pathway |
| 3 | 99.94% | Myopia, X-linked | D2 antagonism may block dopamine's protective role in ocular axial elongation |
| 4 | 99.94% | Syndromic myopia | Structural genetic aetiology (Stickler, Marfan, NF1); no dopaminergic pathway relevance |
| 5 | 99.93% | Hydranencephaly | Structural cortical absence; drug cannot restore tissue that does not exist |
| 6 | 99.93% | Polymicrogyria with cerebellar hypoplasia | Structural neurodevelopmental disorder; chlorpromazine may worsen motor symptoms |
| 7 | 99.93% | Myopia 26, X-linked, female-limited | No known mechanistic link to causative locus |
| 8 | 99.93% | Charcot-Marie-Tooth type 1G | Chlorpromazine has peripheral neurotoxic potential — therapeutically opposite |
| 9 | 99.92% | Atypical glycine encephalopathy | Only a highly indirect NMDA downstream effect; no clinical evidence |

> The 15 PubMed returns retrieved for rank 1 (retinal dystrophy) were reviewed and found to cover orbital infections, diplopia, and congenital eye anatomy — none directly support chlorpromazine as a treatment for retinal dystrophy. These appear to be query noise rather than meaningful supporting literature.

This pattern underscores a critical limitation of ML-based drug repurposing: **high prediction scores alone are insufficient to establish clinical viability**. Expert pharmacological review before any go/hold decision is essential.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06128408](https://clinicaltrials.gov/study/NCT06128408) | N/A | Unknown | 300 | Observational study characterising treatment-resistant schizophrenia from illness onset. Up to 30% of first-episode patients show inadequate response to standard antipsychotics; 80% of all treatment-resistant cases demonstrate resistance from first episode. Characterises the EOS population relevant to this repurposing hypothesis, but is **not** a chlorpromazine intervention trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10703271](https://pubmed.ncbi.nlm.nih.gov/10703271/) | 1999 | Retrospective Observational | Social Psychiatry & Psychiatric Epidemiology | Earlier onset of schizophrenia correlates with different neuroleptic (typical antipsychotic) dosage requirements in outpatients; directly relevant to dosing strategy for EOS |
| [18408624](https://pubmed.ncbi.nlm.nih.gov/18408624/) | 2008 | Genetic Association | Pharmacogenetics and Genomics | **BDNF gene** identified as schizophrenia risk factor and predictor of **chlorpromazine-induced extrapyramidal syndrome** in Chinese population; key pharmacogenomic biomarker candidate |
| [17915974](https://pubmed.ncbi.nlm.nih.gov/17915974/) | 2007 | Genetic Association | Journal of Clinical Psychiatry | **AKT1 polymorphisms** associated with schizophrenia susceptibility and antipsychotic treatment response; may predict chlorpromazine therapeutic outcomes |
| [28976410](https://pubmed.ncbi.nlm.nih.gov/28976410/) | 2017 | Cohort | Clinical Neuropharmacology | Clinical features and correlates of EOS with comorbid OCD; population characterisation for target indication definition |
| [26916502](https://pubmed.ncbi.nlm.nih.gov/26916502/) | 2016 | Cohort | Acta Neuropsychiatrica | Theory of mind and executive function deficits in adolescent EOS; relevant for outcome measure selection in future trial design |
| [24854724](https://pubmed.ncbi.nlm.nih.gov/24854724/) | 2015 | Cohort | L'Encéphale | Neurological soft signs in EOS support the neurodevelopmental model; useful for baseline and monitoring assessment |
| [24289465](https://pubmed.ncbi.nlm.nih.gov/24289465/) | 2013 | Comparative Study | Psychogeriatrics | Early- vs late-onset schizophrenia clinical feature comparison in Asian population; contextual reference for patient stratification |
| [22802957](https://pubmed.ncbi.nlm.nih.gov/22802957/) | 2012 | Neuroimaging | PloS ONE | Temporal gyrus grey matter volume loss in first-episode EOS; neurobiological substrate documentation for treatment target |

---

## Taiwan Market Information

Chlorpromazine currently has **no registered products in Taiwan** (TFDA query returned 0 results; 0 NDA/license records on file).

| Status | Detail |
|--------|--------|
| Taiwan Registration | Not marketed |
| Registered Products | 0 |
| Reference Markets | United States (Thorazine); United Kingdom (Largactil) — approved for schizophrenia, acute psychosis, nausea/vomiting, and intractable hiccups |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Chlorpromazine's D2 antagonism mechanism is directly applicable to early-onset schizophrenia, and the drug was historically effective in this population — but it was replaced by second-generation antipsychotics precisely because extrapyramidal symptom risk is disproportionately high in children and adolescents. A viable repurposing case would need to define a specific clinical or pharmacogenomic subgroup (e.g., BDNF or AKT1 variant carriers) for whom chlorpromazine offers a meaningful advantage over current standard of care. This cannot be assessed without the missing safety data and a formal research protocol.

**To proceed, the following is needed:**

- **Safety data retrieval**: Obtain Taiwan package insert (TFDA 仿單) for formal contraindication and warning review; this is currently a blocking data gap
- **MOA documentation**: Complete DrugBank API query for DB00477 to formally document mechanism of action
- **Paediatric safety review**: Systematic review of chlorpromazine EPS and tardive dyskinesia incidence in paediatric versus adult patients, benchmarked against current SGA comparators
- **Pharmacogenomic hypothesis**: Develop a testable precision-medicine hypothesis based on BDNF (Val66Met) and AKT1 variants as EPS-risk and response predictors
- **Clinical needs assessment**: Consult paediatric psychiatrists in Taiwan to confirm whether any unmet clinical need exists in EOS that current SGAs fail to address
- **Regulatory pathway**: Assess feasibility of paediatric antipsychotic clinical trials under Taiwan regulations before committing to study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

