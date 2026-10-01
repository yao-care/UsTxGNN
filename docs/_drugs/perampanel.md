---
layout: default
title: Perampanel
parent: Model Prediction Only (L5)
nav_order: 1032
evidence_level: L5
indication_count: 10
---

# Perampanel
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

# Perampanel: From Focal-Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Perampanel is an oral anti-seizure medication, marketed in the US for focal-onset seizures and generalized tonic-clonic seizures.
The TxGNN model predicts it may be effective for **visual epilepsy** (a reflex, visually triggered seizure type), with a very high score of 99.92%.
The evidence is indirect: **3 clinical trials** and **20 publications** are linked, but none tests a visually triggered epilepsy population.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 (indirect; no study in a visual or photosensitive epilepsy population) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

The US approved-indication text is not in the provided data. The original indication above comes from the literature (PMID 36150304).

## Why is This Prediction Reasonable?

The Evidence Pack has no structured mechanism-of-action entry for perampanel. The literature describes it as a selective, non-competitive AMPA-type glutamate receptor antagonist. It is approved in the US for focal-onset seizures (adjunctive and monotherapy) and as adjunctive treatment of generalized tonic-clonic seizures.

Visually triggered (reflex) seizures involve cortical hyperexcitability and excessive excitatory glutamate signalling. Blocking AMPA receptors is therefore mechanistically plausible. Preclinical work supports this in related reflex models, where perampanel suppressed audiogenic seizures in genetically epilepsy-prone rats (PMID 30092489).

The plausibility is generic, however. The drug is already used for broad seizure types, and no linked trial or paper tests it in visual or photosensitive epilepsy. The high TxGNN score reflects graph proximity, not direct evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Randomized, double-blind, placebo-controlled study of tolerability, safety and pharmacokinetics (E2007 is perampanel's development code) in patients with partial and generalized seizures. It does not target visually triggered seizures. |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Effects of perampanel on cognition and EEG in general epilepsy. No visual-epilepsy efficacy data. |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Effects of perampanel on neurophysiology tests (EEG, SEP, BAEP, VEP). Not an efficacy study for visually triggered seizures. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematic review / meta-analysis of RCTs | Seizure | Efficacy and safety of perampanel in epilepsy, based on randomized trials. |
| [37059702](https://pubmed.ncbi.nlm.nih.gov/37059702/) | 2023 | Cochrane review | Cochrane Database Syst Rev | Perampanel add-on for drug-resistant focal epilepsy. |
| [35061214](https://pubmed.ncbi.nlm.nih.gov/35061214/) | 2022 | Network meta-analysis | Drugs | Indirect comparison of perampanel and other third-generation anti-seizure medications as adjunctive therapy for focal-onset seizures in adults. |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Network meta-analysis | J Neurol | Compares anti-seizure medications for idiopathic generalized epilepsies. |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES guideline update on new anti-epileptic drugs for new-onset epilepsy. |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Clinical trial and real-world evidence | Epilepsy Behav | Perampanel monotherapy in focal-onset seizures. Confirms the US-approved uses. |
| [37292124](https://pubmed.ncbi.nlm.nih.gov/37292124/) | 2023 | Cohort | Front Neurol | Effectiveness and tolerability of perampanel as first monotherapy in children with newly diagnosed focal epilepsy. |
| [38602656](https://pubmed.ncbi.nlm.nih.gov/38602656/) | 2024 | Mechanistic study | Mol Neurobiol | Investigates perampanel's effects on autophagy-mediated regulation of GluA2 and PSD95 in epilepsy. |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opin Drug Discov | Discovery and development of perampanel as an AMPA receptor antagonist. |
| [36034267](https://pubmed.ncbi.nlm.nih.gov/36034267/) | 2022 | Real-life study | Front Neurol | Perampanel as add-on and second-line monotherapy in childhood absence epilepsy. |

None of these papers addresses visual or photosensitive epilepsy. They support general epilepsy use only.

## US Market Information

The Evidence Pack lists 20 authorizations. The distinct main ones are below. Approved-indication text is not provided for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA 202834 | Fycompa | Tablet | Eisai Inc. |
| ANDA 209801 | Perampanel | Tablet, film coated | Teva Pharmaceuticals, Inc. |
| ANDA 209538 | Perampanel | Tablet, film coated | Sun Pharmaceutical Industries, Inc. |

Oral tablets and an oral suspension form are on the market.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible, and perampanel's safety in general epilepsy is well characterized. However, no linked trial or publication tests it in visually triggered epilepsy, and the only completed randomized study (n=18) is an indirect tolerability study. The safety review is also blocked because package insert warnings and contraindications are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking for safety screening)
- Structured mechanism-of-action data from DrugBank
- Case series, or a targeted trial, in photosensitive or visually triggered epilepsy
- Systematic literature screening, since most linked papers have not yet been classified for relevance

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

