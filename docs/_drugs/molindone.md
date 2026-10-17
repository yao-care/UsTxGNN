---
layout: default
title: Molindone
parent: Model Prediction Only (L5)
nav_order: 940
evidence_level: L5
indication_count: 10
monitor_inn: "MOLINDONE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "hydranencephaly (disease)", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia X-linked", "syndromic myopia", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
last_modified_at: 2026-10-14
description: "Molindone: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia"
---

# Molindone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Molindone: From Schizophrenia to Retinal Dystrophy (Top-Ranked Prediction, Unsupported)

## One-Sentence Summary

Molindone is a typical (first-generation) antipsychotic originally used to treat schizophrenia.
The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but it has **0 clinical trials** and **0 publications** behind it, so it is a computational signal only.
The only prediction with any literature is **manic bipolar affective disorder** (rank 10, **5 publications**, all indirect), which is the more credible research direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (from the knowledge graph; no approved indication text on the US license record) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies (rank 1); manic bipolar affective disorder is the only prediction with literature (rank 10) |
| TxGNN Prediction Score | 99.998% (rank 1); 99.984% (manic bipolar affective disorder) |
| Evidence Level | L5 (rank 1); L4 (manic bipolar affective disorder) |
| US Market Status | Cancelled only (no active marketing authorization) |
| Number of NDAs | 1 (an ANDA, cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, molindone is a dopamine D2 receptor antagonist and a structurally distinct dihydroindolone antipsychotic. Its efficacy in schizophrenia is established.

**Rank 1 (retinal dystrophy):** No plausible mechanistic link was identified. Retinal dystrophies are mainly genetic, and nothing suggests D2 antagonism would alter their course. The high score is a graph-based artifact rather than a pharmacological signal.

**Other top-ranked predictions (ranks 2–9)** are similarly unsupported. They include congenital glycosylation disorder, hydranencephaly, Charcot-Marie-Tooth type 1G, several myopia forms, polymicrogyria, and atypical glycine encephalopathy. All are genetic or structural conditions with no trials or literature. For the myopia forms, dopamine signaling is discussed in general eye-growth biology. There is no evidence that a D2 antagonist helps, and antagonism could even be counterproductive.

**Manic bipolar affective disorder (rank 10)** is the only biologically plausible prediction. D2-blocking antipsychotics are an established class for acute mania, and schizophrenia is a related psychotic disorder. However, the retrieved literature does not test molindone in mania, so the support is class-level and indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for either the top-ranked prediction or manic bipolar affective disorder.

---

## Literature Evidence

No literature is available for the top-ranked prediction (retinal dystrophy). The table below covers manic bipolar affective disorder (rank 10); none of these studies tests molindone for mania.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31922663](https://pubmed.ncbi.nlm.nih.gov/31922663/) | 2020 | RCT | World Psychiatry | IMPACT trial: metformin add-on vs. antipsychotic switch vs. continued treatment in overweight/obese youth with severe mental illness. About antipsychotic metabolic effects, not mania efficacy |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | Antipsychotics for primary and comorbid anxiety in depression or bipolar disorder |
| [21127693](https://pubmed.ncbi.nlm.nih.gov/21127693/) | 2010 | Review | Neuropsychiatr Dis Treat | Olanzapine approved for adolescent schizophrenia and manic/mixed episodes in bipolar I, showing class relevance in mania |
| [2507394](https://pubmed.ncbi.nlm.nih.gov/2507394/) | 1989 | Case report | Gen Hosp Psychiatry | Molindone successfully reintroduced in a patient with prior neuroleptic malignant syndrome |
| [15516311](https://pubmed.ncbi.nlm.nih.gov/15516311/) | 2004 | Case report | J Anal Toxicol | Tissue distribution of molindone in a multidrug overdose (postmortem toxicology) |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090453 (cancelled) | Molindone Hydrochloride (Epic Pharma, LLC) | Tablet (oral) | Not listed |

---

## Safety Considerations

**Knowledge-graph contraindication signals** (from graph edges, not label text):
- **Hematologic:** neutropenia, agranulocytosis, leukopenia, and congenital or constitutional neutropenia syndromes
- **Neurologic:** epilepsy, Parkinson disease and parkinsonian disorders, Alzheimer disease, tardive dyskinesia, neuroleptic malignant syndrome
- **Endocrine/oncologic:** hyperprolactinemia (including prolactin-producing pituitary tumor), female breast carcinoma, brain neoplasm
- **Organ disease:** liver disease, gallbladder disease

**Drug interactions:** 86 interactions were recorded. Examples of **Major** interactions include bupropion, morphine, and potassium citrate. Many **Moderate** interactions involve anticholinergic or GI-motility agents (e.g., atropine, hyoscyamine, glycopyrronium, dicyclomine, loperamide), as well as epinephrine, dronabinol, and lorcaserin.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (retinal dystrophy) and all other top-ten predictions except one have no trials, no literature, and no plausible mechanism. Molindone also has no active US marketing authorization, which limits practical development.
- Manic bipolar affective disorder is a reasonable research question (L4), but current evidence is class-level and does not test molindone directly.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Direct comparative or molindone-specific data in mania, if that direction is pursued
- Assessment of reformulation or re-marketing feasibility given the cancelled license
- A review of the knowledge-graph contraindications (especially neutropenia and seizure risk) against any target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

