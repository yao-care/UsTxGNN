---
layout: default
title: Ketamine
parent: Model Prediction Only (L5)
nav_order: 824
evidence_level: L5
indication_count: 1
---

# Ketamine
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

# Ketamine: From Anesthesia to Headache Disorder

## One-Sentence Summary

Ketamine is an injectable anesthetic and analgesic marketed in the US through generic (ANDA) products. The TxGNN model predicts it may be effective for **Headache Disorder**. This direction is supported by **about 10 headache-related clinical trials** (only one is a completed Phase 3 RCT, and none has posted results) and **a small set of relevant publications**, including one retrospective cohort study in headache disorders.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anesthesia (from general drug knowledge; the approved-indication text in the supplied US records is blank) |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L2 (one completed Phase 3 RCT, NCT03081416, with no results supplied; the source pack rated this L3, so treat L2 as the upper bound) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed products are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. Ketamine is generally known as a non-competitive NMDA receptor antagonist. The following mechanism is therefore general pharmacology, not confirmed by the supplied data.

Glutamatergic signaling and central sensitization are thought to contribute to migraine, cluster headache, and other refractory headaches. NMDA blockade may dampen cortical spreading depression and trigeminovascular sensitization, so a link between ketamine and headache relief is biologically plausible. It has not been confirmed for headache in this dataset.

The high TxGNN score (0.993) is a computational prediction and does not count as clinical evidence. The stronger support comes from the trial registry. Several emergency-department and refractory-headache studies, including intranasal and IV ketamine, are already registered or completed.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK trial: sub-dissociative intranasal ketamine vs standard care for primary headache in the ED (single-blind, placebo-controlled); no results supplied |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | Multi-center double-blind comparison of low-dose ketamine vs Compazine for ED headache; no results supplied |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | N/A | Completed | 34 | Randomized, double-blind, placebo-controlled test of sub-dissociative ketamine for acute migraine-type headache in the ED; no results supplied |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept study of intranasal ketamine spray in chronic cluster headache; no results supplied |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Oral ketamine + aspirin vs rimegepant for acute headache in the ED; very small enrollment |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | KetHead: multicenter placebo-controlled RCT of high-dose IV ketamine (1 mg/kg/h for 6 h) in chronic daily headache |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Recruiting | 90 | Single infusion of ketamine + magnesium sulfate for refractory chronic cluster headache |
| [NCT06608277](https://clinicaltrials.gov/study/NCT06608277) | Phase 2 | Recruiting | 175 | Ketamine, stellate ganglion block, or both vs sham for TBI-associated headache and PTSD |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Sub-dissociative ketamine vs ketorolac for acute headache in the ED (registry text mentions both tension-type headache and migraine) |
| [NCT05518877](https://clinicaltrials.gov/study/NCT05518877) | Phase 4 | Completed | 55 | Low-dose ketamine for ED analgesia (slow vs faster infusion), aimed at reducing side effects; not headache-specific, but gives indirect tolerability information |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Retrospective cohort | Front Neurol | Assessed the efficacy, duration and safety of inpatient IV lidocaine and ketamine infusions in headache disorders; prior support was limited to small case series |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Overview of acute and preventive drug therapy for cluster headache (the supplied abstract does not describe ketamine's role) |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline update | Headache | American Headache Society 2025 update on parenteral drugs for acute migraine in the ED (the supplied abstract does not state ketamine's position) |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Trigeminal neuralgia pharmacotherapy; ketamine is mentioned as a possible adjunct or monotherapy option |
| [37421541](https://pubmed.ncbi.nlm.nih.gov/37421541/) | 2023 | Review | Curr Pain Headache Rep | Evidence-based review of complex regional pain syndrome treatments; useful only as neighboring chronic-pain context |

## US Market Information

The approved-indication text is blank in all supplied records, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA074549 | Ketamine Hydrochloride | Injection, solution, concentrate | Medical Purchasing Solutions, LLC |
| ANDA216809 | Ketamine Hydrochloride | Injection, solution | Gland Pharma Limited |
| ANDA216809 | Ketamine Hydrochloride | Injection, solution | Sagent Pharmaceuticals |
| ANDA074549 | Ketamine Hydrochloride | Injection, solution, concentrate | Henry Schein, Inc. |

A fifth listed entry is a second Sagent Pharmaceuticals record under ANDA216809, identical to the third row above. All listed products are injectables. Non-injectable routes (for example intranasal or oral), which several of the trials use, are not among the supplied US licenses.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the supplied data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and several headache-specific ketamine trials exist, but no trial results are supplied and the only completed Phase 3 RCT is small (n=80). The package-insert safety data is missing, and the source pack flags that gap as blocking for safety screening. The current status is a research question, not an actionable candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, obtained by downloading and parsing the FDA label (blocking)
- Published results from NCT03081416 (THINK), NCT02657031 (CHECK) and NCT02697071, plus the outcome of NCT05306899 (KetHead)
- Mechanism of action data from DrugBank to support the mechanistic-link analysis
- Confirmation of which headache subtype is targeted (migraine, cluster, tension-type, or chronic daily headache), since the trials cover different subtypes
- Route feasibility, because the trials use intranasal, oral and IV routes but the supplied US products are injectables only
- A safety and tolerability plan for the sub-dissociative dose ranges used in these studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

