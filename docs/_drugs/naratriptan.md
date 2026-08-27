---
layout: default
title: Naratriptan
parent: 僅模型預測 (L5)
nav_order: 954
evidence_level: L5
indication_count: 3
---

# Naratriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Naratriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Naratriptan is a selective 5-HT1B/1D receptor agonist used for the acute treatment of migraine.
> The TxGNN model predicts an extremely high association with **Migraine with Brainstem Aura**,
> supported by **0 clinical trials** and **19 publications** — but this specific subtype is a
> recognized class contraindication for triptans, so the signal points to a safety flag rather than
> a viable repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine, acute treatment (per known pharmacology; no formal label data available in this evidence pack) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Naratriptan is a 5-HT1B/1D receptor agonist. Its accepted mechanism in ordinary migraine involves cranial vasoconstriction and inhibition of trigeminal CGRP/neuropeptide release, which together relieve migraine pain and associated symptoms. This mechanism is directly relevant to migraine pathophysiology in general.

However, "Migraine with Brainstem Aura" (formerly "basilar-type migraine") is a distinct subtype in which triptans, including naratriptan, are conventionally **contraindicated**. The theoretical concern is that vasoconstriction in the vertebrobasilar territory could precipitate brainstem or cerebral ischemia in a population already prone to aura-related vascular phenomena. The American Headache Society evidence assessment (PMID 25600718) and related literature reflect this standing caution.

In other words, the TxGNN model has correctly identified a strong *mechanistic* link between naratriptan and this migraine subtype — but the direction of that link is toward risk, not therapeutic opportunity. The high prediction score should be read as evidence of pharmacological relevance, not as support for clinical use in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomized crossover trial comparing headache recurrence rates between naratriptan and sumatriptan in recurrence-prone migraine patients |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT | Cephalalgia | Evaluated naratriptan given during the migraine prodrome to prevent headache onset |
| [12752749](https://pubmed.ncbi.nlm.nih.gov/12752749/) | 2003 | RCT | Headache | Analysis of adolescent migraine characteristics from the Glaxo Wellcome clinical trials database, including naratriptan trial participants |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | RCT | Headache | Randomized, double-blind, placebo-controlled study of naratriptan 1 mg and 2.5 mg for short-term prophylaxis of menstrually associated migraine |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Found reduced triptan efficacy in migraine **with aura** versus without aura — directly relevant to the aura-related indication under review |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including triptan-class safety considerations |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of menstrual migraine treatment options, including naratriptan's role in short-term prophylaxis |
| [22337860](https://pubmed.ncbi.nlm.nih.gov/22337860/) | 2013 | Review | Cephalalgia | Literature review on treating migraine during the premonitory phase, referencing naratriptan prodrome data |
| [25100506](https://pubmed.ncbi.nlm.nih.gov/25100506/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Updated review of menstrual migraine hormonal causes, prophylaxis, and treatment, including naratriptan |
| [17578540](https://pubmed.ncbi.nlm.nih.gov/17578540/) | 2007 | Review | Headache | Open-label, long-term tolerability data for naratriptan used intermittently as prophylaxis for menstrually related migraine |

---

## US Market Information

No approved marketing authorization (NDA) was found for naratriptan in this evidence pack — market status is recorded as **Not Marketed (未上市)**, with 0 licenses on file.

---

## Safety Considerations

- **Key Warning (from clinical literature, not the safety data field):** Migraine with brainstem aura is a well-recognized contraindication for triptan-class drugs, including naratriptan, due to theoretical risk of vasoconstriction-related ischemia in the vertebrobasilar territory. This is the central safety consideration for the predicted indication itself.
- All other structured safety fields (key warnings, contraindications, drug-drug interactions) are currently data gaps. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (migraine with brainstem aura) is not a repurposing opportunity — it is a subtype where triptans are conventionally contraindicated on mechanistic grounds. Despite the high TxGNN score and substantial general-migraine literature, no evidence supports safe or effective use in this specific population, and no clinical trials exist for this pairing. The two lower-ranked predictions in this evidence pack (atrophoderma vermiculata, ulerythema ophryogenesis) are L5, model-only signals with zero supporting literature or trials and should also remain on Hold.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications for naratriptan (currently a blocking data gap, DG001)
- Confirmed mechanism-of-action data sourced directly from DrugBank (DG002)
- Clinical or pharmacovigilance rationale for why the model associates naratriptan with this specific aura subtype, to rule out a data/labeling artifact
- If pursuing further, a formal risk-benefit review by a headache specialist given the standing contraindication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

