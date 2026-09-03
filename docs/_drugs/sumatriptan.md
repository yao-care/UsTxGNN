---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 1189
evidence_level: L5
indication_count: 1
---

# Sumatriptan
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

# Sumatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Sumatriptan is a 5-HT1B/1D receptor agonist used for the acute treatment of migraine.
> The TxGNN model predicts a very high association (**99.74%**) with **migraine with brainstem aura**,
> but this signal is supported only by **mechanism-level literature (19 publications, no dedicated clinical trials)**,
> and the underlying pharmacology actually points toward a **safety caution rather than a therapeutic opportunity** in this specific subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in local license records (drug is unlicensed in Taiwan); internationally indicated for acute treatment of migraine |
| Predicted New Indication | Migraine with brainstem aura (formerly "basilar-type migraine") |
| TxGNN Prediction Score | 99.74% (rank 7127) |
| Evidence Level | L4 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data is not available for this drug (Data Gap DG002). However, the evidence pack's mechanistic rationale confirms sumatriptan is a selective **5-HT1B/1D receptor agonist**, whose therapeutic effect in typical migraine relies on constricting dilated cranial/dural blood vessels and suppressing vasoactive neuropeptide release from trigeminal afferents.

Migraine with brainstem aura shares the "migraine" disease family with the drug's original indication, which likely explains the high embedding-based similarity score from TxGNN — the two conditions are closely linked in the knowledge graph. However, this subtype's pathophysiology specifically involves **transient dysfunction of the vertebrobasilar (posterior circulation) territory**.

This is where the prediction becomes mechanistically double-edged: the same vasoconstrictive action that makes sumatriptan effective in typical migraine is precisely why headache guidelines (AHS/IHS) flag triptans as **relatively-to-absolutely contraindicated** in migraine with brainstem aura — vasoconstriction in an already compromised posterior circulation carries a theoretical risk of exacerbating ischemia. In other words, the TxGNN score reflects semantic/topological proximity in the knowledge graph, not confirmed clinical benefit, and existing literature (e.g., PMID 25841032, showing reduced sumatriptan efficacy in migraine with aura vs. without aura) reinforces that this subtype behaves differently from the drug's proven indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Double-blind, placebo-controlled trial of oral sumatriptan 200mg in acute migraine **with aura**; efficacy comparable to open-label studies |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytotherapy Research | Double-blind RCT comparing ginger powder vs. sumatriptan for acute migraine (without aura); similar efficacy |
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT | Cephalalgia | Early sumatriptan administration prevented PACAP38-induced migraine attacks |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort/Comparative | Neurology | Sumatriptan showed **reduced efficacy in migraine with aura compared to migraine without aura** — directly relevant to the safety/efficacy caveat for this prediction |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Mechanism study | Neurology | Examined subcutaneous sumatriptan's effect on the migraine aura phase itself |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Mechanism study | JAMA Neurology | PET study of central 5-HT1B receptor binding during sumatriptan-treated migraine attacks |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review (Tier 1) | Headache | AHS evidence assessment of acute migraine pharmacotherapies, including triptans |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Critical review of sumatriptan's clinical use in migraine and cluster headache |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Review | Expert Rev Neurother | Sumatriptan needle-free subcutaneous formulation approved for acute migraine (with or without aura) and cluster headache |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | Overview of status migrainosus as a migraine complication |

---

## US Market Information

Sumatriptan currently has **no active marketing authorization on file** in this jurisdiction (0 licenses; market status: Not Marketed). No license-level indication text is available for comparison.

---

## Safety Considerations

- **Mechanistic Safety Concern**: The repurposing rationale itself flags a specific pharmacological risk — triptans, including sumatriptan, cause cranial vasoconstriction. In migraine with brainstem aura, pathology involves the vertebrobasilar (posterior circulation) territory, and this class of drug is considered relatively-to-absolutely contraindicated per AHS/IHS headache treatment guidelines due to theoretical risk of worsening posterior-circulation ischemia.

No TFDA label warnings, contraindications, or drug interaction data are currently available for this drug (Data Gap DG001 — blocking for a full safety review).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a very high similarity score (99.74%), the supporting evidence is mechanism/review-level only (L4) with no dedicated clinical trials, and the pharmacological rationale actually argues **against** use in this specific migraine subtype due to vasoconstriction risk in the vertebrobasilar territory — a concern also echoed in clinical guidelines. This is a case where a high model score does not translate into a favorable repurposing candidate.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001) to confirm formal contraindication status for migraine with brainstem aura
- Structured MOA data from DrugBank (DG002) to formally document the 5-HT1B/1D vasoconstrictive mechanism
- A formal literature review of AHS/IHS guideline language specifically excluding triptans in this subtype, to convert this from a "Hold" into a documented "Do Not Pursue" if confirmed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

