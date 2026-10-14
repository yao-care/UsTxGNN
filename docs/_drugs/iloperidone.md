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

Iloperidone is an atypical antipsychotic originally used to treat schizophrenia.
The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but it has **0 clinical trials** and **0 publications** behind it, so it is a graph-based prediction only.
Among the model's ten predictions, only **manic bipolar affective disorder** (rank 10) has real supporting evidence, including a Phase 3 placebo-controlled study, and it is the more actionable direction (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid licenses in the data) |
| Number of NDAs | 2 (1 NDA, 1 ANDA; both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From the published literature, iloperidone is a benzisoxazole atypical antipsychotic that antagonises dopamine D2 and serotonin 5-HT2A receptors. Its efficacy in schizophrenia is established.

For retinal dystrophy, no mechanistic link is supported. Inherited retinal degeneration has no known pathway connecting it to D2/5-HT2A antagonism. The very high score (0.99999, rank 52 overall) reflects a pattern in the knowledge graph rather than a biological rationale. Treat this prediction as unvalidated until independent evidence appears.

Most of the other top-ranked predictions are similarly implausible. They include a glycosylation disorder, hydranencephaly, Charcot-Marie-Tooth type 1G, a polymicrogyria syndrome, X-linked myopias and atypical glycine encephalopathy. All have no trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Alternative Candidate With Evidence: Manic Bipolar Affective Disorder (Rank 10)

Manic bipolar affective disorder has a lower TxGNN score (99.98%, overall rank 1121) but is the only prediction with supporting literature. The mechanistic rationale is strong. D2/5-HT2A antagonism is shared with other antipsychotics approved for acute mania.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38236020](https://pubmed.ncbi.nlm.nih.gov/38236020/) | 2024 | RCT | J Clin Psychiatry | Phase 3, randomized, double-blind, placebo-controlled study in adults with bipolar mania. Iloperidone (up to 24 mg/day) was compared with placebo for 4 weeks, with change in Young Mania Rating Scale as the primary endpoint. |
| [39800949](https://pubmed.ncbi.nlm.nih.gov/39800949/) | 2025 | Review | Ann Pharmacother | Reviews efficacy in bipolar I mania and the safety profile (QTc prolongation, orthostatic hypotension, metabolic effects). |
| [39008105](https://pubmed.ncbi.nlm.nih.gov/39008105/) | 2024 | Review | Med Lett Drugs Ther | Commentary on a new bipolar disorder indication for iloperidone (Fanapt). |
| [39126643](https://pubmed.ncbi.nlm.nih.gov/39126643/) | 2024 | Review | Expert Opin Drug Saf | Safety review of atypical antipsychotics, QTc interval and torsades de pointes. |
| [22900950](https://pubmed.ncbi.nlm.nih.gov/22900950/) | 2012 | Systematic review | CNS Drugs | Body weight and metabolic adverse effects of iloperidone and other newer antipsychotics in schizophrenia and bipolar disorder. |
| [28817490](https://pubmed.ncbi.nlm.nih.gov/28817490/) | 2017 | Open trial | J Clin Psychopharmacol | Open trial of iloperidone for mixed episodes in bipolar disorder. |
| [42213400](https://pubmed.ncbi.nlm.nih.gov/42213400/) | 2026 | Review | Clin Drug Investig | Describes milsaperidone, an active metabolite of iloperidone. States that iloperidone has been approved in the USA for schizophrenia since 2009 and for acute bipolar I disorder since 2024. |

No registered clinical trials were supplied for this indication.

**Evidence level note:** The data labels this candidate L1. Under the stated rules (L1 requires at least 2 completed Phase 3 RCTs), a single Phase 3 RCT fits L2 better. The level should be confirmed from the full text.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022192 | FANAPT (Vanda Pharmaceuticals) | Tablet | Not listed in the compiled data; status cancelled |
| ANDA207231 | Iloperidone (Mylan Pharmaceuticals) | Tablet | Not listed in the compiled data; status cancelled |

The licence data shows both authorizations as cancelled. However, the 2026 literature describes iloperidone as approved in the USA for schizophrenia (2009) and acute bipolar I disorder (2024). This conflict should be reconciled against the current FDA record.

---

## Safety Considerations

Label warnings and contraindications were not available in the compiled data, so the items below come from other sources.

- **Knowledge-graph contraindications (not label text):** The knowledge graph links iloperidone to many conditions. The main groups are:
  - Cardiovascular and QT-related: long QT syndrome, torsades de pointes, myocardial infarction, heart conduction disease, sudden cardiac arrest, orthostatic hypotension.
  - Metabolic: diabetes mellitus, hyperglycemia, diabetic ketoacidosis, obesity.
  - Haematological: neutropenia, leukopenia, agranulocytosis.
  - Neurological: epilepsy, Alzheimer disease, neuroleptic malignant syndrome, tardive dyskinesia.
  - Other: liver disease, gallbladder disease, priapism, female breast carcinoma, potassium deficiency.
- **Safety themes from the literature:** QTc prolongation and torsades de pointes (PMID 39126643), somnolence (PMID 27372312), weight gain and metabolic effects (PMID 22900950), and orthostatic hypotension (PMID 39800949).
- **Drug interactions:** 100 interactions are recorded. Major-level examples include **bupropion**, **morphine** and **clarithromycin**. Moderate-level examples include metformin, pioglitazone, epinephrine, atropine, famotidine and several antidiabetic and anticholinergic agents.

---

## Conclusion and Next Steps

**Decision: Hold** (for retinal dystrophy, the top-ranked prediction)

**Rationale:**
- The prediction rests only on a knowledge-graph score. There are no trials or publications, and no plausible mechanism links an antipsychotic to inherited retinal degeneration.
- If the goal is a practical repurposing direction, manic bipolar affective disorder has Phase 3 RCT support and may merit **Proceed with Guardrails**. This is subject to the licence-status discrepancy and the evidence-level check.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) from DrugBank.
- The FDA package insert (warnings and contraindications), which is currently a blocking gap for safety screening.
- For retinal dystrophy: independent preclinical or mechanistic evidence before any further investment.
- For bipolar mania: full-text verification of the Phase 3 study (design, endpoints, results) and confirmation of the current US approval and licence status.
- A guardrail plan for QTc/ECG monitoring, metabolic monitoring and interaction screening.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

