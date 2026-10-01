---
layout: default
title: Trifluoperazine
parent: Model Prediction Only (L5)
nav_order: 1261
evidence_level: L5
indication_count: 1
---

# Trifluoperazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Trifluoperazine: From Antipsychotic Use to Manic Bipolar Affective Disorder

## One-Sentence Summary

Trifluoperazine is a high-potency phenothiazine antipsychotic and dopamine D2 receptor blocker, marketed in the US as oral tablets.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**.
Support is thin: **no registered clinical trials** and **20 publications**, none of which tests trifluoperazine in mania.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 (mechanism and class-level evidence only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 15 (all generic ANDA licenses) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for trifluoperazine is not available in the Evidence Pack. Based on known information, trifluoperazine is a high-potency phenothiazine and a dopamine D2 receptor antagonist. Antipsychotics that block D2 receptors are an established drug class for acute mania, so the prediction is biologically plausible as a class effect.

A 1976 case study, "A dopaminergic mechanism in mania," supports this view. Piribedil and d-amphetamine, which stimulate dopamine receptors, were associated with manic episodes. Pimozide, a dopamine blocker, had an antimanic effect. This suggests a dopamine-driven component in at least some manic patients.

Two caveats apply. First, none of the retrieved evidence tests trifluoperazine itself in mania. Second, the original labeled indications are missing from the data, so the new indication could not be checked against the drug's approved uses. The very high TxGNN score is a computational prediction and not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below is a controlled study of trifluoperazine in mania. They are ordered by relevance to the prediction, not by study quality.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [970489](https://pubmed.ncbi.nlm.nih.gov/970489/) | 1976 | Mechanistic case study | Am J Psychiatry | Dopamine agonists were linked to manic episodes. The dopamine blocker pimozide had an antimanic effect. |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | Reviews typical and atypical antipsychotics for anxiety symptoms in primary and comorbid conditions, including bipolar disorder. |
| [14309092](https://pubmed.ncbi.nlm.nih.gov/14309092/) | 1965 | Clinical study | Int J Neuropsychiatry | Studies haloperidol, a related antipsychotic, in schizophrenic and manic patients. No abstract available. |
| [11279762](https://pubmed.ncbi.nlm.nih.gov/11279762/) | 2001 | Systematic review | Cochrane Database Syst Rev | Reviews clotiapine, a different neuroleptic, for acute psychotic illness with agitation. |
| [14084030](https://pubmed.ncbi.nlm.nih.gov/14084030/) | 1963 | Double-blind study | Curr Ther Res | Withdrawal of trifluoperazine in patients maintained on tranylcypromine plus trifluoperazine. No abstract available. |
| [13761179](https://pubmed.ncbi.nlm.nih.gov/13761179/) | 1961 | Clinical report | Am J Psychiatry | Tranylcypromine plus trifluoperazine in agitated depression, not mania. No abstract available. |
| [40926568](https://pubmed.ncbi.nlm.nih.gov/40926568/) | 2026 | Review | J Appl Toxicol | Phenothiazine derivatives and apoptosis. Preclinical focus on cancer cells, with mania in bipolar disorder noted only as a background use. |
| [39202628](https://pubmed.ncbi.nlm.nih.gov/39202628/) | 2024 | Systematic review | Medicina (Kaunas) | Drug-induced "rabbit" syndrome (oral vertical dyskinesia), an antipsychotic adverse effect. |
| [2102674](https://pubmed.ncbi.nlm.nih.gov/2102674/) | 1990 | Case report | Br J Psychiatry | Atypical neuroleptic malignant syndrome after an overdose of trifluoperazine and carbamazepine. |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | J Psychiatr Pract | Safety of antipsychotic drugs during pregnancy. |

## US Market Information

The record lists 15 licenses in total. The five main ones are below. The approved-indication text is blank in the source records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA085786 | Trifluoperazine Hydrochloride | Tablet, film coated | Sandoz Inc. |
| ANDA085785 | Trifluoperazine Hydrochloride | Tablet, film coated | Sandoz Inc. |
| ANDA040209 | Trifluoperazine Hydrochloride | Tablet, film coated | RemedyRepack Inc. |
| ANDA040209 | Trifluoperazine Hydrochloride | Tablet, film coated | Mylan Pharmaceuticals Inc. |
| ANDA040209 | Trifluoperazine Hydrochloride | Tablet, film coated | Mylan Pharmaceuticals Inc. |

All listed products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information. The package insert warnings and contraindications could not be retrieved, and no drug-interaction records were found.

The retrieved literature mentions antipsychotic-class concerns that should be reviewed during any evaluation:
- Neuroleptic malignant syndrome, including a case after a trifluoperazine overdose
- Movement disorders such as "rabbit" syndrome
- Seizures and EEG changes during phenothiazine therapy
- Use during pregnancy and lactation

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The D2-blockade mechanism makes mania a plausible target, but there are no clinical trials and no trifluoperazine-specific mania studies. The missing package insert safety data is a blocking gap for safety screening, so this stays at the research-question stage.

**To proceed, the following is needed:**
- The package insert warnings and contraindications, obtained from the FDA label
- The drug's original approved indications and detailed mechanism of action, from DrugBank
- Trifluoperazine-specific evidence in mania, through a targeted literature search or a registered trial
- A comparison against established antimanic antipsychotics
- A drug-interaction and special-population review, covering pregnancy, lactation and neuroleptic malignant syndrome risk

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

