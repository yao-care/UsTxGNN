---
layout: default
title: Risperidone
parent: Model Prediction Only (L5)
nav_order: 1128
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Risperidone: From Schizophrenia and Bipolar Mania to Gaze Palsy, Familial Horizontal, with Progressive Scoliosis

## One-Sentence Summary

Risperidone is an atypical antipsychotic. A trial record in the pack (NCT00277654) states it is FDA-approved for schizophrenia and bipolar mania.
The TxGNN model's top-ranked prediction is **gaze palsy, familial horizontal, with progressive scoliosis**, a rare congenital brainstem disorder.
This prediction has **0 clinical trials** and **0 publications** behind it, so it looks like a knowledge-graph artifact rather than a real lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia and bipolar mania (from trial record NCT00277654; the license records list no indication text) |
| Predicted New Indication | Gaze palsy, familial horizontal, with progressive scoliosis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of Licenses (NDA/ANDA) | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the pack. Risperidone is known as a D2/5-HT2A antagonist, and its efficacy in psychotic and manic disorders is established.

That mechanism has no evident link to this prediction. Familial horizontal gaze palsy with progressive scoliosis is a rare congenital disorder of axon guidance and brainstem development. Blocking dopamine or serotonin receptors would not be expected to affect it. The high TxGNN score is therefore best read as a graph artifact, and the score alone is not sufficient evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Other Predicted Indications with Evidence

The top-ranked prediction is weak, but lower-ranked predictions in the same pack carry real evidence.

**Major affective disorder (rank 6, TxGNN 99.11%): L1, Proceed with Guardrails**
- Phase 3 completed RCTs graded relevant:
  - [NCT00095134](https://clinicaltrials.gov/study/NCT00095134): adjunctive risperidone vs placebo in MDD, n=630.
  - [NCT00044681](https://clinicaltrials.gov/study/NCT00044681): risperidone augmentation of an SSRI in treatment-resistant depression, n=258.
  - [NCT00221403](https://clinicaltrials.gov/study/NCT00221403): valproate and risperidone in young children with bipolar disorder, n=46.
- Systematic reviews and RCT:
  - [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/): Cochrane review of second-generation antipsychotics in MDD.
  - [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/): network meta-analysis of augmentation strategies in TRD.
  - [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/): randomized trial of risperidone in treatment-refractory MDD.
- Guardrails:
  - The term spans MDD and bipolar disorder, so the indication must be specified per subtype.
  - Trial outcome data were not supplied, so efficacy direction and effect size must be confirmed from the primary publications.
  - Metabolic, prolactin and extrapyramidal adverse effects must be weighed against the benefit.

**Trichotillomania (rank 5, TxGNN 99.51%): L4, Research Question**
- The evidence is almost entirely case reports and small case series of risperidone added to an SSRI, for example [10357517](https://pubmed.ncbi.nlm.nih.gov/10357517/) and [9108814](https://pubmed.ncbi.nlm.nih.gov/9108814/).
- There are no registered trials and no controlled studies. Concurrent SSRI, naltrexone or N-acetylcysteine therapy confounds the reports.

**Phelan-McDermid syndrome (rank 4, TxGNN 99.59%): L4, Research Question**
- The evidence is a management review, a zebrafish shank3 study and a single case study. There is no controlled human evidence.
- Any benefit would be symptomatic (irritability, aggression), not disease-modifying.

**Asperger syndrome, susceptibility to (rank 2)** and **amelocerebrohypohidrotic syndrome (rank 3)** have no trials or literature and no identifiable mechanistic link. Both are L5, Hold.

---

## US Market Information

The pack lists 20 licenses; the 5 shown here are those supplied. Indication text is not included in these records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA078707 | Risperidone | Tablet, film coated | Westminster Pharmaceuticals, LLC |
| NDA213586 | UZEDY | Injection, suspension, extended release | Teva Pharmaceuticals USA, Inc. |
| ANDA079059 | Risperidone | Solution | Bryant Ranch Prepack |
| ANDA201003 | Risperidone | Tablet | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA078040 | Risperidone | Tablet, film coated | American Health Packaging |

Available forms include oral tablets (including orally disintegrating), oral solution and extended-release injectable suspension.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trials, no literature and no plausible mechanism, so it should not be pursued. Risperidone's real repurposing signal lies elsewhere: major affective disorder is supported by multiple completed Phase 3 RCTs and meta-analyses, and trichotillomania and Phelan-McDermid syndrome are early research questions.

**To proceed, the following is needed:**
- Redirect evaluation to **major affective disorder** (per subtype, MDD vs bipolar), and confirm efficacy direction and effect size from the primary publications and meta-analyses.
- Obtain the FDA package insert warnings and contraindications. This is currently a blocking gap for safety screening.
- Obtain mechanism of action data (for example from DrugBank).
- For trichotillomania, look for controlled evidence beyond case reports before any further consideration.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

