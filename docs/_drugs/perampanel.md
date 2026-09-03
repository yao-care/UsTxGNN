---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 1032
evidence_level: L5
indication_count: 10
---

# Perampanel
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

# Perampanel: From Epilepsy (Partial-Onset Seizures) to Visual Epilepsy

## One-Sentence Summary

> Perampanel is a selective, non-competitive AMPA receptor antagonist used for partial-onset and generalized tonic-clonic seizures in epilepsy (per literature evidence; official indication text is not available in this data pack).
> The TxGNN model predicts it may also be effective for **Visual Epilepsy**, a photosensitive/visually-triggered reflex seizure subtype,
> with **3 clinical trials** and **20 publications** currently available as supporting context — though none directly study visual epilepsy as a distinct entity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory license data (0 licenses on file); per literature, perampanel is indicated for partial-onset seizures (adjunctive/monotherapy) and primary generalized tonic-clonic seizures |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a data gap). Based on the supporting literature retrieved, perampanel is a selective, non-competitive AMPA (α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid) receptor antagonist — the first drug in its class approved as an anti-epileptic agent. It works by inhibiting glutamate-mediated postsynaptic excitation, which underlies its broad-spectrum anticonvulsant activity across multiple seizure types (PMID 24559052, PMID 21635236).

Visual epilepsy is a reflex epilepsy subtype in which seizures are triggered by visual stimuli (e.g., flashing lights, patterns), involving cortical hyperexcitability in occipital/visual pathways. Since AMPA receptors mediate excitatory transmission broadly across the cortex — including visual cortex circuits — there is a plausible mechanistic rationale for perampanel's efficacy in this reflex seizure subtype, consistent with its demonstrated "broad-spectrum" anticonvulsant profile (PMID 29953584).

However, the clinical trial and literature evidence currently available addresses general epilepsy populations rather than visual/photosensitive epilepsy specifically. One retrieved trial (NCT03653741) did examine visual evoked potentials (VEP) as a neurophysiology endpoint, which is tangentially relevant but not a treatment-efficacy study for visual epilepsy. The prediction should therefore be regarded as mechanistically plausible but not yet clinically validated for this specific indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Randomised, double-blind, placebo-controlled tolerability/safety/PK study of E2007 (perampanel) in patients with partial and generalized seizures; not specific to visual epilepsy |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Evaluated perampanel's effects on cognition and EEG in epilepsy patients; general refractory partial-onset seizure population |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Assessed perampanel's effect on neurophysiology tests (EEG, SEP, BAEP, and visual evoked potential/VEP) in healthy volunteers; relevant to visual pathway function but not a treatment trial for visual epilepsy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Review | BMJ | Overview of anti-seizure medication management (incl. perampanel) during pregnancy/lactation; general safety context |
| [36218253](https://pubmed.ncbi.nlm.nih.gov/36218253/) | 2022 | Review | Revista de Neurología | Pediatric status epilepticus management overview |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Practice Guideline | Neurology | AAN/AES guideline update on efficacy/tolerability of new AEDs for new-onset epilepsy |
| [36034267](https://pubmed.ncbi.nlm.nih.gov/36034267/) | 2022 | Real-world study | Frontiers in Neurology | Real-life effectiveness/tolerability of perampanel as add-on/monotherapy in childhood absence epilepsy |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review | Epilepsy & Behavior | Review of perampanel monotherapy clinical trial and real-world evidence for focal-onset and generalized tonic-clonic seizures |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opin Drug Discov | Discovery/development history; approved in 35+ countries as adjunctive therapy for partial-onset seizures |
| [37775491](https://pubmed.ncbi.nlm.nih.gov/37775491/) | 2023 | Observational | Med J Malaysia | Efficacy/safety of adjunctive perampanel in epilepsy patients |
| [37329172](https://pubmed.ncbi.nlm.nih.gov/37329172/) | 2023 | Retrospective cohort | Ann Clin Transl Neurol | Efficacy of perampanel in pediatric epilepsy with known/presumed genetic etiology |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review / Network Meta-analysis | J Neurology | ASM comparison (incl. perampanel) for idiopathic generalized epilepsies |
| [37292124](https://pubmed.ncbi.nlm.nih.gov/37292124/) | 2023 | Retrospective cohort | Frontiers in Neurology | Effectiveness/tolerability of perampanel monotherapy in newly diagnosed pediatric focal epilepsy |

---

## US Market Information

Perampanel is currently recorded as **Not Marketed** in this regulatory dataset, with **0 licenses** on file. No NDA, product name, or approved indication text is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data were available in this evidence pack — all fields returned as data gaps.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap exists for TFDA/label warnings and contraindications, which prevents even an initial (S1) safety evaluation. In addition, while perampanel's AMPA-antagonist mechanism offers a plausible rationale for visual epilepsy, all available clinical trial and literature evidence addresses general epilepsy populations rather than the visual/photosensitive subtype specifically — evidence level is best characterized as L4 (mechanistic/indirect), not yet clinical proof-of-concept for this indication.

**To proceed, the following is needed:**
- TFDA/FDA label data — warnings, contraindications, and drug interactions (DG001, Blocking)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Disease-specific clinical evidence (case series, observational studies, or trials) evaluating perampanel in visual/photosensitive epilepsy specifically
- Confirmation of original indication and regulatory license status, since no licenses are currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

