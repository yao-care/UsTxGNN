---
layout: default
title: Chlorzoxazone
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 9
---

# Chlorzoxazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Using the `txgnn-pipeline` skill to confirm context, then generating the report now.

---

# Chlorzoxazone: From Musculoskeletal Pain to Migraine Disorder

## One-Sentence Summary

Chlorzoxazone is a centrally acting muscle relaxant traditionally used for the symptomatic relief of acute musculoskeletal pain and muscle spasm.
The TxGNN model predicts it may have potential for **Migraine Disorder**,
with **0 clinical trials** and **3 publications** currently available to support this direction — none of which directly test chlorzoxazone in migraine.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Musculoskeletal pain / Muscle spasm (centrally acting muscle relaxant) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorzoxazone is a centrally acting muscle relaxant that depresses polysynaptic reflex arcs at the spinal cord and subcortical brainstem level to relieve skeletal muscle spasm. Its efficacy in musculoskeletal pain has been established over decades, including use in combination with anti-inflammatory agents.

The mechanistic hypothesis connecting chlorzoxazone to migraine centers on **BK (large-conductance Ca²⁺-activated K⁺) channel activation**. By enhancing BK channel conductance, chlorzoxazone could theoretically reduce cortical neuron excitability and suppress **cortical spreading depression (CSD)** — the neurophysiological cascade widely accepted as the core mechanism underlying migraine aura and possibly the headache phase itself. Indirect support comes from PMID 23115190, which demonstrates that Ca²⁺-dependent K⁺ channel activators alleviate cerebellar ataxia driven by enhanced CaV2.1 (CACNA1A) currents in mutant mice. Critically, CACNA1A mutations are also the causal basis for **familial hemiplegic migraine (FHM)**, creating a partial biological overlap between the animal model findings and migraine pathophysiology.

However, this reasoning chain is long and highly speculative. No clinical trial, human study, or targeted in vitro experiment has directly tested whether chlorzoxazone affects CSD, migraine frequency, or any migraine-related biomarker. The available publications address adjacent neurological topics (vestibular disorders, cerebellar ataxia) rather than chlorzoxazone-specific migraine effects. This remains an early mechanistic hypothesis requiring prospective validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Basic Science / Animal Study | J Neuroscience | Ca²⁺-dependent K⁺ channel activators alleviate cerebellar ataxia from CaV2.1 gain-of-function (CACNA1A S218L mutant mice); CACNA1A mutations also underlie familial hemiplegic migraine — indirect mechanistic bridge |
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Narrative Review | Journal of Neurology | Pharmacotherapy of central vestibular and cerebellar disorders; discusses K⁺ channel modulation (4-AP) and its role in normalizing Purkinje cell firing — contextually adjacent to BK channel rationale |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Review | Deutsches Ärzteblatt International | Vestibular migraine accounts for 11.4% of vertigo cases; reviews pharmacological management of vestibular and migraine-related syndromes — no chlorzoxazone data |

---

## US Market Information

Chlorzoxazone currently holds **0 NDA approvals** and is **not marketed** in the United States. No licensed products, approved indications, or authorized dosage forms were found in the regulatory query.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields (key warnings, contraindications, drug-drug interactions) returned no data in the current evidence pack. The package insert should be reviewed directly before any clinical use or study design.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.73%), the supporting evidence is limited to L4 — preclinical and mechanistically adjacent publications with no direct clinical or in vitro data for chlorzoxazone in migraine. The BK channel → CSD hypothesis is biologically plausible but unvalidated, and the drug currently has no US market approval, adding regulatory and safety characterization hurdles before any repurposing pathway can proceed.

**To proceed, the following is needed:**
- **Confirm the MOA**: Verify chlorzoxazone's BK channel activation potency, selectivity, and dose-response in neuronal tissue (not just musculoskeletal)
- **Preclinical CSD study**: Test whether chlorzoxazone suppresses cortical spreading depression in validated rodent migraine models (e.g., CACNA1A mutant or trigeminovascular models)
- **CNS penetration data**: Confirm blood-brain barrier permeability at therapeutic doses relevant to migraine prevention
- **Full safety review**: Retrieve and parse the package insert to characterize warnings, contraindications, and DDI profile before any clinical planning
- **Regulatory pathway scoping**: Given 0 US approvals, an IND submission would be required; assess whether existing safety data (from musculoskeletal use) is sufficient for a Phase 1/2 proof-of-concept trial
- **Neurologist consultation**: Engage migraine specialists to assess unmet need vs. existing therapies (CGRP antagonists, triptans) and refine patient selection criteria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

