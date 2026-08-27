---
layout: default
title: Ketamine
parent: 僅模型預測 (L5)
nav_order: 824
evidence_level: L5
indication_count: 1
---

# Ketamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ketamine: From Anesthesia to Headache Disorder

## One-Sentence Summary

> Ketamine is a well-known dissociative anesthetic and analgesic agent (a non-competitive NMDA receptor antagonist); the specific original indication text was not present in the source data, though esketamine, its S-enantiomer, is separately approved for treatment-resistant depression.
> The TxGNN model predicts it may be effective for **Headache Disorder**,
> with **9 headache-relevant clinical trials** and **5 headache/pain-relevant publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in source data (ketamine is widely known as a dissociative anesthetic/analgesic) |
| Predicted New Indication | Headache Disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism-of-action documentation for ketamine is not available in the source data. Based on known pharmacology, ketamine is a non-competitive NMDA (N-methyl-D-aspartate) receptor antagonist. NMDA receptor activity is central to two processes implicated in chronic and refractory headache disorders: central sensitization and cortical spreading depression. Both are thought to drive the pathophysiology of chronic migraine, refractory headache, and trigeminal autonomic cephalalgias (TACs) such as cluster headache.

By blocking NMDA receptors, ketamine may theoretically reduce sensitization of the trigeminovascular system, which is the shared pain-signaling pathway implicated across multiple headache subtypes. This same NMDA-antagonist mechanism underlies ketamine's established use in other central-sensitization-related pain conditions, such as complex regional pain syndrome (CRPS) and refractory neuropathic pain, lending biological plausibility to its repurposing for headache disorder.

That said, the bulk of large randomized controlled trial evidence for ketamine to date centers on psychiatric indications (treatment-resistant depression, via esketamine). Headache-specific evidence remains concentrated in smaller trials, retrospective cohorts, and one completed Phase 3 study, with a larger confirmatory Phase 3 RCT (KetHead) still recruiting.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK Trial: randomized, single-blind, placebo-controlled trial of sub-dissociative dose intranasal ketamine vs. standard therapy for primary headache syndromes in the emergency department. |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | The CHECK Trial: multicenter, randomized, double-blind comparison of low-dose ketamine vs. compazine for ED headache control. |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | N/A | Completed | 34 | Randomized, placebo-controlled trial of sub-dissociative ketamine for acute migraine-type headache in the ED, assessing pain reduction and recurrence. |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept study of intranasal ketamine spray for chronic cluster headache; builds on prior small case-series data. |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | The KetHead Study: multicenter, placebo-controlled RCT of high-dose IV ketamine infusion for chronic daily headaches via reversal of receptor-mediated sensitization. |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Recruiting | 90 | Single infusion of ketamine combined with magnesium sulfate for refractory chronic cluster headache. |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Oral ketamine + aspirin + rimegepant vs. standard care for acute headache presenting to the ED. |
| [NCT06608277](https://clinicaltrials.gov/study/NCT06608277) | Phase 2 | Recruiting | 175 | Multicenter RCT comparing ketamine, stellate ganglion block, and combination therapy vs. sham for TBI-associated headache and PTSD. |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Ketamine vs. ketorolac for acute treatment of generalized tension-type headache. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Cohort | Frontiers in Neurology | Retrospective cohort study of inpatient lidocaine and ketamine infusions for headache disorders, assessing efficacy, duration, and safety. |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 2025 American Headache Society guideline update on parenteral pharmacotherapies (including ketamine) for acute migraine treatment in the ED. |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Review of acute and prophylactic drug therapy for cluster headache and other trigeminal autonomic cephalalgias. |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Update on trigeminal neuralgia pharmacotherapy, noting ketamine among emerging adjuvant/monotherapy options. |
| [37421541](https://pubmed.ncbi.nlm.nih.gov/37421541/) | 2023 | Review | Current Pain and Headache Reports | Evidence-based review of CRPS pathophysiology and treatment, relevant to the shared central-sensitization mechanism with headache disorders. |

---

## US Market Information

No NDA or marketing authorization was found for ketamine in the source regulatory database (0 licenses on record; market status: Not Marketed). This may reflect a gap in the reviewed license dataset rather than the drug's true global regulatory status, since ketamine/esketamine formulations are approved in other jurisdictions for anesthesia and treatment-resistant depression.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in the source data — notably, a **blocking data gap** was flagged for TFDA label warnings/contraindications, which prevents completion of a preliminary safety assessment for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap exists on TFDA labeling (warnings/contraindications), which prevents even a preliminary (S1) safety assessment. While mechanistic plausibility is reasonable and one completed Phase 3 trial plus several smaller completed studies support directional efficacy, the pivotal confirmatory Phase 3 RCT (KetHead) is still recruiting, and formal MOA/original-indication documentation is missing.

**To proceed, the following is needed:**
- TFDA label PDF (warnings/contraindications) to complete the S1 safety screen
- Confirmed drug-drug interaction (DDI) data
- Formal mechanism-of-action and original-indication documentation from DrugBank
- Completion of the ongoing KetHead Phase 3 RCT (NCT05306899, expected 2026-06) for confirmatory efficacy data
- Verification of actual US/Taiwan market and licensing status, given the "0 licenses" result may reflect a data-source gap rather than true absence from market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

