---
layout: default
title: Tiagabine
parent: Moderate Evidence (L3-L4)
nav_order: 1226
evidence_level: L4
indication_count: 1
---

# Tiagabine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Tiagabine: From Focal Epilepsy to Visual Epilepsy

## One-Sentence Summary

Tiagabine is an oral antiseizure drug that, per the literature, is used as add-on therapy for focal (partial) seizures. The TxGNN model predicts it may be useful for **visual epilepsy**, with a very high score. Support for this specific indication is weak: **1 clinical trial** (general antiepileptic context only) and **17 publications**, none of which tests tiagabine in visual or occipital epilepsy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Focal (partial) seizures, add-on therapy (from the literature; the license records contain no indication text) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The mechanism of action field in the record is empty. The literature fills the gap: tiagabine selectively blocks the GABA transporter GAT-1, so GABA uptake into neurons and glia falls and extracellular GABA rises (PMID 10530690, 10030435). GABA is the brain's main inhibitory neurotransmitter, and impaired GABAergic inhibition is a recognised route to seizures (PMID 11520315, 32120063).

Visual epilepsy is a focal epilepsy with visual-onset seizures, such as occipital-origin seizures. Tiagabine is already used for focal seizures, so a benefit here is mechanistically plausible.

The 99.25% score most likely reflects tiagabine's existing link to epilepsy in the knowledge graph. It is not evidence of a distinct effect in visual epilepsy. There is also a safety concern specific to this indication. Tiagabine has been discussed alongside vigabatrin in relation to visual field effects (PMID 12588906), which would matter for patients whose condition already involves the visual system.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Liceo study: observational study of newer antiepileptic drugs (gabapentin, lamotrigine, levetiracetam, oxcarbazepine, pregabalin, tiagabine, topiramate) as first-choice combination therapy in focal epilepsy. General context only; no tiagabine-specific or visual-epilepsy results are reported |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31608990](https://pubmed.ncbi.nlm.nih.gov/31608990/) | 2019 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Tiagabine as add-on therapy for drug-resistant focal epilepsy. The retrieved abstract gives background only |
| [22592677](https://pubmed.ncbi.nlm.nih.gov/22592677/) | 2012 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Earlier version of the add-on review for drug-resistant partial epilepsy |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES update on newer antiepileptic drugs for new-onset focal or generalized epilepsy |
| [12588906](https://pubmed.ncbi.nlm.nih.gov/12588906/) | 2003 | Review/Commentary | J Neurol Neurosurg Psychiatry | Visual field safety of vigabatrin and tiagabine (no abstract available) |
| [17560495](https://pubmed.ncbi.nlm.nih.gov/17560495/) | 2007 | Review | Pediatr Neurol | Antiepileptic drugs and visual disturbances, especially visual field and colour vision deficits |
| [10530690](https://pubmed.ncbi.nlm.nih.gov/10530690/) | 1999 | Review (drug monograph) | Epilepsia | GAT-1 mechanism, predictable pharmacokinetics, few interactions, effective as add-on for partial seizures |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review (mechanisms) | Neuropharmacology | Mechanisms of action of currently used antiseizure drugs |
| [11520315](https://pubmed.ncbi.nlm.nih.gov/11520315/) | 2001 | Review (mechanisms) | Epilepsia | GABAergic inhibition and its role in epilepsy |
| [26210064](https://pubmed.ncbi.nlm.nih.gov/26210064/) | 2015 | Review | Epilepsy Behav | Drug-induced status epilepticus. Sodium-channel and GABAergic antiseizure drugs can worsen seizures in some epilepsies, and tiagabine appears to be discussed (the abstract is truncated) |
| [9097364](https://pubmed.ncbi.nlm.nih.gov/9097364/) | 1997 | Review (drug monograph) | Semin Pediatr Neurol | Pharmacokinetics, efficacy and safety of tiagabine; effective for partial seizures in adults and adolescents |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020646 | Tiagabine Hydrochloride (Teva Pharmaceuticals USA) | Film-coated tablet | — |
| ANDA214816 (4 entries) | Tiagabine Hydrochloride (Novadoz Pharmaceuticals) | Tablet | — |

The indication text is not populated in these license records.

---

## Safety Considerations

Please refer to the package insert for safety information.

Two signals from the retrieved literature are relevant to this indication:
- Visual field effects have been discussed for tiagabine alongside vigabatrin (PMID 12588906, 17560495).
- GABAergic antiseizure drugs can aggravate seizures in some epilepsy types (PMID 26210064).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a general link between tiagabine and epilepsy, plus a plausible GABAergic mechanism. No retrieved study tests tiagabine in visual or occipital epilepsy, and the only trial is general-context observational work (relevance grade C). Package insert warnings and contraindications are still missing, which blocks safety screening. The visual field concern adds to the need for caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, obtained and parsed
- Confirmed mechanism of action data from DrugBank
- Searches for tiagabine studies specific to visual or occipital-onset epilepsy
- A visual field monitoring plan and a review of seizure-aggravation risk in this population
- Confirmation of the approved indication from the label, since the license records are empty
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

