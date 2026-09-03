---
layout: default
title: Selegiline
parent: 僅模型預測 (L5)
nav_order: 1150
evidence_level: L5
indication_count: 4
---

# Selegiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Selegiline: From Parkinson's Disease to Schizophrenia (Negative Symptoms)

## One-Sentence Summary

> Selegiline is a selective, irreversible monoamine oxidase type-B (MAO-B) inhibitor originally used for Parkinson's disease (oral) and major depressive disorder (transdermal).
> The TxGNN model predicts it may be useful as an **augmentation therapy for negative symptoms of schizophrenia**,
> with **1 registered clinical trial** and **20 publications** — including several double-blind, placebo-controlled RCTs — supporting this direction.
> Three other TxGNN-predicted indications (a rare cerebral malformation syndrome, a congenital glycosylation disorder, and a retinal dystrophy syndrome) show no mechanistic plausibility or supporting evidence and are assessed as likely knowledge-graph artifacts — they are not carried forward in this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's Disease (oral); Major Depressive Disorder (transdermal) — per literature (PMID 37087864); no formal Taiwan license record available |
| Predicted New Indication | Schizophrenia (negative symptoms, adjunct to antipsychotics) |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L3 (multiple published RCTs and a systematic review/meta-analysis; no confirmed completed Phase 2/3 registry trial) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available for this drug in the evidence pack. Based on the literature evidence collected, selegiline is an irreversible, selective MAO-B inhibitor approved for Parkinson's disease (oral formulation) and major depressive disorder (transdermal formulation); at oral doses ≥20 mg/day it loses MAO-B selectivity and behaves as a non-selective MAOI (PMID 37087864).

The dopaminergic hypothesis links selegiline's mechanism to schizophrenia's negative symptoms: negative symptoms have long been hypothesized to reflect regionally deficient CNS dopaminergic activity (PMID 8627275), and MAO-B inhibition increases synaptic dopamine availability. This provides a plausible pharmacological rationale for using low-dose selegiline as an *adjunct* to antipsychotic therapy specifically to target negative symptoms — a treatment gap that standard antipsychotics do not adequately address.

By contrast, the three other TxGNN top predictions (polymicrogyria with cerebellar hypoplasia, a congenital disorder of glycosylation, and a retinal dystrophy syndrome) are rare monogenic structural/metabolic disorders with no known relationship to monoaminergic or dopaminergic pathways. The retrieved "literature" for these diseases consists of unrelated ophthalmology/neuroanatomy papers matched only by disease-name keywords, not drug-disease evidence. These are assessed as likely false positives arising from sparse nodes in the knowledge graph and are excluded from further evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00456976](https://clinicaltrials.gov/study/NCT00456976) | Early Phase 1 | Completed | 70 | RCT evaluating selegiline augmentation of antipsychotic medication for negative symptoms in chronic inpatient schizophrenia; primary endpoint was reduction in negative symptoms vs placebo. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15677608](https://pubmed.ncbi.nlm.nih.gov/15677608/) | 2005 | RCT | Am J Psychiatry | Double-blind, placebo-controlled, multicenter trial of selegiline augmentation in outpatients with schizophrenia and moderate-or-greater negative symptoms. |
| [17972359](https://pubmed.ncbi.nlm.nih.gov/17972359/) | 2008 | RCT | Hum Psychopharmacol | 8-week double-blind RCT of selegiline add-on to risperidone for negative symptoms of chronic schizophrenia. |
| [8102552](https://pubmed.ncbi.nlm.nih.gov/8102552/) | 1993 | RCT | Biol Psychiatry | Placebo-controlled trial of selegiline (10 mg/day) for neuroleptic-induced tardive dyskinesia; also assessed parkinsonism, akathisia, and negative symptoms. |
| [37087864](https://pubmed.ncbi.nlm.nih.gov/37087864/) | 2023 | Systematic Review/Meta-analysis | Eur Neuropsychopharmacol | Systematic review and meta-analysis of efficacy/safety of selegiline (oral and transdermal) across psychiatric disorders. |
| [17405823](https://pubmed.ncbi.nlm.nih.gov/17405823/) | 2007 | Review | Ann Pharmacother | Reviews the role of selegiline specifically in treating negative symptoms of schizophrenia. |
| [16930948](https://pubmed.ncbi.nlm.nih.gov/16930948/) | 2006 | Systematic Review | Schizophr Res | Systematic review of pharmacological treatments (including selegiline) for primary negative symptoms in schizophrenia. |
| [8627275](https://pubmed.ncbi.nlm.nih.gov/8627275/) | 1996 | Open-label pilot study | J Nerv Ment Dis | Pilot study testing the dopamine-deficiency hypothesis of negative symptoms using low-dose selegiline augmentation. |
| [10080262](https://pubmed.ncbi.nlm.nih.gov/10080262/) | 1999 | Case series | Compr Psychiatry | Case series of 3 schizophrenia patients showing improvement in negative symptoms and functioning after adding selegiline. |
| [7831475](https://pubmed.ncbi.nlm.nih.gov/7831475/) | 1994 | Mechanism review | Prog Neurobiol | Reviews possible mechanisms of action of deprenyl (selegiline) and other MAO-B inhibitors in neurologic/psychiatric disorders. |
| [8988464](https://pubmed.ncbi.nlm.nih.gov/8988464/) | 1996 | Review | J Neural Transm Suppl | Reviews clinical potential of deprenyl across neurologic and psychiatric disorders beyond Parkinson's disease. |

---

## Market Information (Taiwan)

No Taiwan marketing authorization records are available for selegiline in this evidence pack — market status is recorded as **Not Marketed**, with 0 licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack (a **Blocking** data gap — TFDA label/warning data is required before this candidate can proceed to safety pre-assessment, given selegiline's known MAOI-related interaction risks, e.g., serotonergic drugs and dietary tyramine, which are not yet documented here).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Mechanistic rationale and multiple published double-blind RCTs support selegiline augmentation for negative symptoms of schizophrenia, but no completed Phase 2/3 registry trial confirms efficacy, and results across existing small trials have been mixed.
- A **Blocking** data gap (missing TFDA label warnings/contraindications) prevents safety pre-assessment (S1), and the drug currently has zero market authorizations in this jurisdiction.

**To proceed, the following is needed:**
- TFDA label / package insert data (warnings, contraindications, DDI) — required to clear the Blocking gap (DG001)
- Structured mechanism-of-action data from DrugBank (DG002)
- A confirmatory Phase 2/3 RCT specifically powered for negative-symptom endpoints, given the existing trials are small, heterogeneous, and largely from the 1990s–2000s
- Formal review of the 2023 systematic review/meta-analysis (PMID 37087864) to consolidate pooled efficacy/safety estimates before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

