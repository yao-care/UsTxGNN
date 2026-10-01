---
layout: default
title: Trihexyphenidyl
parent: Model Prediction Only (L5)
nav_order: 1263
evidence_level: L5
indication_count: 10
---

# Trihexyphenidyl
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

# Trihexyphenidyl: From Parkinsonism to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Trihexyphenidyl is an anticholinergic drug that is generally used for parkinsonism and drug-induced movement disorders. This is general pharmacology, because the US label data in this pack contain no indication text.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but there are **0 clinical trials** and only **1 indirectly related publication**. The score comes from the model alone, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US licence data (parkinsonism per general pharmacology) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (the pack lists L4, but its only literature item is an indirect cohort study with no drug-specific data) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 16 (the licences listed are all ANDAs, i.e. generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, trihexyphenidyl is a muscarinic (M1-preferring) anticholinergic. It is used to treat movement symptoms by blocking cholinergic signalling in the brain.

No direct mechanism links cholinergic blockade to the core symptoms of ADHD (inattention, hyperactivity, impulsivity). The only literature hit is about primary tic disorder with dystonia, where anticholinergics may help the dystonic component. That is a comorbid movement-disorder link, not evidence of ADHD efficacy.

The very high TxGNN score (99.92%) is a knowledge-graph prediction only. Because of this, the prediction should be treated as a hypothesis to examine, not as support for efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Cohort | Movement Disorders | Large clinical series and review of patients with tics and persistent dystonia, describing the prevalence and clinical features of this combined syndrome. It does not evaluate ADHD or trihexyphenidyl efficacy. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040254 | Trihexyphenidyl Hydrochloride (Novitium Pharma LLC) | Tablet | Not provided |
| ANDA091630 | Trihexyphenidyl Hydrochloride (Natco Pharma Limited) | Tablet | Not provided |
| ANDA040251 | Trihexyphenidyl Hydrochloride (Akorn) | Syrup | Not provided |
| ANDA040177 | Trihexyphenidyl Hydrochloride (PAI Pharma) | Solution | Not provided |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the available data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, no drug-specific literature, and no mechanistic basis linking anticholinergic action to ADHD. The high TxGNN score is the only support. Safety data (warnings and contraindications) are also missing, so the candidate cannot move on to safety screening.

The other nine predicted indications are weaker still. Eight have no usable evidence (L5, Hold), and the ADHD, inattentive type prediction is likely a duplicate of the ADHD signal. The one exception is **PLA2G6-associated neurodegeneration**, which is flagged as a research question. Any benefit there would be symptomatic only (dystonia-parkinsonism), and its two case-level reports have not been confirmed to involve trihexyphenidyl.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication text for the US licences
- A systematic search for trihexyphenidyl-specific ADHD data, and full-text review of the tic-with-dystonia and PLA2G6 literature to confirm whether the drug was actually evaluated
- Review of anticholinergic safety in children and people with ADHD, since cognitive and CNS adverse effects are a particular concern in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

