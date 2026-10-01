---
layout: default
title: Levetiracetam
parent: Model Prediction Only (L5)
nav_order: 850
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Partial-Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Levetiracetam is an antiseizure drug marketed as an add-on treatment for partial-onset seizures in adults with epilepsy, and the license records supplied here contain no indication text.
The TxGNN model predicts it may be effective for **visual epilepsy** (seizures triggered by visual stimuli).
Nine registered clinical trials and 20 publications were retrieved, but **none tests levetiracetam in visual or photosensitive epilepsy**, so this is still essentially a model prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial-onset seizures in epilepsy (adjunctive therapy in adults). This comes from trial registry text, because the license records have no indication text. |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (mechanistic plausibility only; no direct human studies) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (the five shown below are ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source dataset. From general pharmacology, levetiracetam binds synaptic vesicle protein 2A (SV2A). This reduces neurotransmitter release and dampens network hyperexcitability.

Visual epilepsy, meaning seizures provoked by flickering light or visual patterns, reflects abnormal cortical hyperexcitability. A drug that dampens excitatory synaptic release could plausibly help.

This link is not backed by any supplied trial or paper on visual or photosensitive epilepsy. The retrieved trials are general levetiracetam or epilepsy studies, and the retrieved papers cover general seizure management. The prediction currently rests on the drug's broad antiseizure activity, not on evidence for this syndrome.

---

## Clinical Trial Evidence

The nine trials below were retrieved for this prediction. All were graded as only indirectly relevant, and none enrolled patients with visual or reflex epilepsy.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not yet recruiting | 580 | Prophylactic levetiracetam vs placebo after intracerebral haemorrhage. Seizure prevention, not visual epilepsy. |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not yet recruiting | 1649 | MAST: phenytoin vs levetiracetam and AED duration after traumatic brain injury. |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | Placebo-controlled cognitive safety study of adjunctive levetiracetam in children with refractory partial seizures. |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | Levetiracetam and hippocampal hyperactivity in psychosis, using a visual scene task with fMRI. Not epilepsy. |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational study of newer AEDs as first-line combination therapy in focal epilepsy. |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Levetiracetam in neonatal seizures. |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label migraine prophylaxis, with or without visual aura. |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Levetiracetam and hippocampal hyperactivity; stopped after one participant. |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by invitation | 24 | Gene therapy for Canavan disease; levetiracetam is background medication. |

---

## Literature Evidence

The papers below are the most relevant of the 20 retrieved, prioritized by study type. None addresses visual or photosensitive epilepsy, so these results describe other seizure settings.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures. |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | The Lancet Neurology | PEACH: tested whether prophylactic levetiracetam reduces acute seizures after intracerebral haemorrhage. |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT (open label) | Seizure | Phenytoin vs levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome. |
| [30487494](https://pubmed.ncbi.nlm.nih.gov/30487494/) | 2018 | RCT | Mymensingh Med J | Phenobarbital vs levetiracetam in childhood epilepsy. |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Meta-analysis | Neurocritical Care | Levetiracetam prophylaxis in ICH, TBI, neurosurgery and SAH. Efficacy, dosing and adverse events were described as unclear. |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Network meta-analysis | J Neurol | Antiseizure medications for idiopathic generalized epilepsies. |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Meta-analysis | Epilepsy & Behavior | Levetiracetam vs other ASMs for myoclonic seizures in idiopathic generalized epilepsy, especially juvenile myoclonic epilepsy. |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Guideline | Neurocritical Care | Neurocritical Care Society guideline on seizure prophylaxis after moderate-severe TBI. |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | NEJM | Initial management of seizure in adults. |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arq Neuropsiquiatr | Diagnosis, monitoring and treatment of status epilepticus. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA090261 | Levetiracetam | Film-coated tablet | Mylan Pharmaceuticals Inc. |
| ANDA090515 | Levetiracetam | Film-coated tablet | Quallent Pharmaceuticals Health LLC |
| ANDA090515 | Levetiracetam | Film-coated tablet | Bryant Ranch Prepack |
| ANDA091491 | Levetiracetam | Tablet | Cranbury Pharmaceuticals, LLC |
| ANDA216375 | Levetiracetam | Film-coated tablet | Ascend Laboratories, LLC |

Across all 20 licenses, the dosage forms also include extended-release film-coated tablets and oral solution. The license records contain no approved indication text.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.98% TxGNN score is not backed by any direct human evidence. The retrieved trials and papers concern other seizure types, and the mechanistic argument (SV2A-mediated dampening of excitability) is general rather than specific to visual triggers.

**To proceed, the following is needed:**
- Direct evidence in photosensitive or visually triggered epilepsy, such as case series, EEG photoparoxysmal-response studies, or a small controlled trial
- Mechanism-of-action data and the FDA package insert warnings and contraindications, which are currently missing and block the safety screen
- Confirmation of the approved indication text on the US labels

Other predictions in the same evidence pack have more support. Status epilepticus is effectively an established use with direct randomized evidence (L1, Proceed with Guardrails). Startle epilepsy (L3) and reading seizures (L4) have small human reports and could be worth a closer look.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

