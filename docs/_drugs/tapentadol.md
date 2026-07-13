---
layout: default
title: Tapentadol
parent: 僅模型預測 (L5)
nav_order: 619
evidence_level: L5
indication_count: 3
---

# Tapentadol
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

# Tapentadol: From Moderate-to-Severe Pain to Migraine Disorder

## One-Sentence Summary

Tapentadol is a centrally acting analgesic with a dual mechanism of action — μ-opioid receptor (MOR) agonism and norepinephrine reuptake inhibition (NRI) — used for moderate-to-severe acute and chronic pain management.
The TxGNN model predicts it may have relevance for **Migraine Disorder** as its top-ranked candidate,
however only **2 indirectly related publications** were retrieved and **no clinical trials** have investigated this combination, placing the evidence at the lowest possible level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No US NDA records captured in this dataset (data gap suspected; see note below) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | Not marketed (per dataset — 0 licenses found) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tapentadol is a centrally acting analgesic that integrates two complementary pharmacological mechanisms: μ-opioid receptor (MOR) agonism and norepinephrine reuptake inhibition (NRI). Although detailed MOA data was not available in this dataset, the repurposing rationale analysis identifies both components as relevant to this prediction.

The NRI component provides the strongest mechanistic rationale for migraine. Norepinephrine reuptake inhibition enhances descending pain modulation via the locus coeruleus pathway projecting to the trigeminal nucleus caudalis — a key relay in trigeminovascular pain transmission, which is the central mechanism of migraine headache. Theoretically, boosting this descending inhibitory tone could attenuate trigeminal nociception and reduce migraine pain. This pathway is shared with SNRIs (e.g., venlafaxine, duloxetine), which have some evidence for migraine prevention.

However, the prediction faces a critical mechanistic counterargument that substantially undermines its translational value. Opioids, including the MOR agonist component of tapentadol, are a leading cause of **medication overuse headache (MOH)** — a well-established clinical syndrome in which regular use of analgesics, particularly opioids, paradoxically increases headache frequency and transforms episodic migraine into chronic daily headache. Current international migraine guidelines list opioid use as a major risk factor for chronification and an indication to be avoided. The potential NRI benefit and the opioid-driven MOH risk are in direct conflict, and for most migraine patients the net effect of tapentadol would likely be harmful rather than therapeutic.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for tapentadol in migraine disorder.

---

## Literature Evidence

The 2 publications retrieved were not directly studying tapentadol in migraine. They were captured via overlapping search terms (pain + migraine) and provide contextual background on the migraine treatment landscape only — neither evaluates tapentadol as a migraine therapy.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Cochrane SR | Cochrane Database Syst Rev | Dipyrone (metamizole) for acute postoperative pain; notes that dipyrone is used for migraine in some countries — not about tapentadol |
| [27096438](https://pubmed.ncbi.nlm.nih.gov/27096438/) | 2016 | Cochrane SR | Cochrane Database Syst Rev | Sumatriptan + naproxen combination for acute migraine attacks; establishes treatment landscape context — not about tapentadol |

---

## US Market Information

No US NDA records were found for tapentadol in this dataset.

> **Data Gap Note:** Tapentadol (brand names Nucynta®, Nucynta® ER) has well-known FDA approvals for moderate-to-severe acute pain and chronic pain including diabetic peripheral neuropathy. The absence of records here likely reflects a data collection gap rather than a true absence of approval. Cross-referencing the FDA Orange Book (https://www.accessdata.fda.gov/scripts/cder/ob/) is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Mechanistic Safety Alert (from repurposing analysis):** The opioid (MOR agonist) component of tapentadol carries a well-recognized, class-level risk of **medication overuse headache (MOH)**. Regular opioid use in headache patients paradoxically worsens headache frequency and severity over time, representing a fundamental barrier to using tapentadol as a migraine treatment. This concern applies regardless of the NRI benefit and is flagged by migraine treatment guidelines as a contraindication to opioid use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is at Level L5 — model prediction only, with no direct clinical trials and no tapentadol-specific literature in migraine. More importantly, the opioid component of tapentadol carries a recognized class-level contraindication for migraine therapy (MOH risk), which substantially undermines the mechanistic case despite the theoretically favorable NRI effect.

**To proceed, the following is needed:**

- Confirm actual US FDA approval status via the FDA Orange Book — the dataset shows 0 licenses, which is inconsistent with Nucynta's known approval history and must be resolved before regulatory conclusions can be drawn (DG001 remediation)
- Obtain full MOA documentation from DrugBank (DG002) — particularly to quantify the relative NRI vs. MOR agonist contribution at clinically relevant doses
- Retrieve package insert warnings and contraindications (DG001) — opioid-class warnings, abuse potential, and any migraine-specific contraindications
- Commission a targeted literature review specifically on: (a) opioid MOH risk quantification for tapentadol, and (b) NRI-mediated effects on trigeminovascular nociception
- If mechanistic analysis remains promising: evaluate whether the NRI component alone (i.e., a selective NRI without opioid activity) could address migraine without the MOH liability — tapentadol itself may not be the right vehicle even if the NRI target is valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

