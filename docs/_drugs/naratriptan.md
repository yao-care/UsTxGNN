---
layout: default
title: Naratriptan
parent: Moderate Evidence (L3-L4)
nav_order: 955
evidence_level: L4
indication_count: 3
---

# Naratriptan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Naratriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Naratriptan is a triptan, a selective 5-HT1B/1D agonist used to treat migraine attacks.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but there are **0 registered clinical trials** and only **general migraine literature (18 publications)**. None of it studies this subtype specifically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine (acute treatment). The US license records in the Evidence Pack have no indication text, so this comes from the drug class and the literature |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (all are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Naratriptan is a selective 5-HT1B/1D receptor agonist. It causes cranial vasoconstriction and inhibits trigeminal CGRP release, which makes it plausible for migraine headache in general. Migraine with brainstem aura is a subtype of migraine with aura, so the disease is biologically related to the drug's established use.

The link is weaker for this subtype. The aura is thought to arise from cortical spreading depression involving the brainstem, and triptans have no established effect on it. Triptan labels also usually caution against use in basilar-type and hemiplegic migraine because of vasoconstriction concerns. A cohort study (PMID 25841032) found reduced efficacy of sumatriptan in migraine with aura compared with migraine without aura.

The very high TxGNN score probably reflects the parent migraine indication rather than subtype-specific evidence. Detailed mechanism of action data is also not available in the source data, which limits deeper mechanistic analysis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The literature covers migraine in general, mostly acute treatment and menstrual migraine. None of it addresses brainstem aura directly.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | RCT (double-blind, placebo-controlled) | Headache | Naratriptan 1 mg and 2.5 mg twice daily vs placebo as short-term prophylaxis of menstrually associated migraine |
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clin Ther | Naratriptan vs sumatriptan on headache recurrence in recurrence-prone migraine patients |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT | Cephalalgia | Naratriptan given during the prodrome to prevent migraine headache |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Sumatriptan was less effective in migraine with aura than without aura |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Open-label pilot | Neurol Sci | Naratriptan for short-term prophylaxis of pure menstrual migraine, six-month multicentre non-comparative study |
| [17578540](https://pubmed.ncbi.nlm.nih.gov/17578540/) | 2007 | Open-label study | Headache | Long-term tolerability of intermittent naratriptan for menstrually related migraine prevention |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Review | Headache | Managing intractable migraine with naratriptan |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Treatment options for menstrual migraine |
| [23877022](https://pubmed.ncbi.nlm.nih.gov/23877022/) | 2014 | Case report | Brain Dev | Naratriptan relieved intractable migraine-like headaches with visual aura in a patient with Sturge-Weber syndrome |

## US Market Information

The source data lists 6 licenses, but they cover only 3 unique ANDA numbers (some entries are duplicates). All are oral tablets.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA200502 | Naratriptan (Heritage / Avet) | Tablet | Not provided in the source data |
| ANDA091441 | Naratriptan (Bionpharma) | Tablet, film coated | Not provided in the source data |
| ANDA090381 | Naratriptan (Hikma) | Tablet | Not provided in the source data |

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records, which means the interactions are unverified rather than absent.

Please refer to the package insert for warnings and contraindications. Triptan labels typically caution against use in basilar-type and hemiplegic migraine because of vasoconstriction concerns, which is directly relevant to this predicted indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by subtype-specific evidence. There are no registered trials, and the literature covers migraine in general. The triptan class also carries a known cautionary signal for brainstem-type aura. The two other predictions for this drug (atrophoderma vermiculata and ulerythema ophryogenesis) have no evidence and no plausible mechanism (both L5), so they should also stay on Hold.

**To proceed, the following is needed:**
- The full FDA package insert, to confirm warnings, contraindications and the approved indication (currently a blocking gap)
- Mechanism of action data from DrugBank
- A targeted literature review on triptan safety and efficacy in brainstem aura, basilar-type and hemiplegic migraine
- Expert neurology review of whether the vasoconstriction concern rules this indication out

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

