---
layout: default
title: Lasmiditan
parent: 僅模型預測 (L5)
nav_order: 838
evidence_level: L5
indication_count: 3
---

# Lasmiditan
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

# Lasmiditan: From Migraine (Acute Treatment) to Migraine with Brainstem Aura

## One-Sentence Summary

Lasmiditan (DrugBank DB11732) is a selective 5-HT1F receptor agonist whose published, literature-confirmed indication is acute treatment of migraine, with or without aura, in adults. The TxGNN model predicts it may also be effective specifically for **migraine with brainstem aura**, a rare migraine subtype, with **0 clinical trials** and **18 publications** currently identified as supporting context — though none of the trials or publications are subtype-specific to lasmiditan in this population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine, with or without aura (per literature evidence, e.g. PMID 31749059) — not captured in the regulatory license database (see Market Status note below) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (per regulatory database; this appears inconsistent with the literature-reported 2019 FDA approval of lasmiditan (REYVOW) — flagged as a data quality gap, not resolved here) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank in this evidence pack (flagged as a blocking data gap, DG002). Based on the literature evidence collected, lasmiditan is a highly selective serotonin 5-HT1F receptor agonist. It acts on the trigeminovascular system to suppress CGRP release and pain transmission, and — unlike triptans (5-HT1B/1D agonists) — it lacks meaningful 5-HT1B-mediated vasoconstrictor activity.

Migraine with brainstem aura (formerly "basilar-type migraine") has traditionally been treated cautiously with triptans because of theoretical vasoconstriction risk in the vertebrobasilar circulation. Lasmiditan's non-vasoconstrictive mechanism is therefore mechanistically plausible for this subtype, since it would not carry the same theoretical contraindication.

However, this is an extrapolation rather than a demonstrated effect: the pivotal Phase 2/3 RCTs (e.g. PMID 31132795, 22459549, 33990951) and subsequent reviews/meta-analyses were conducted in general migraine populations with or without aura, and none of the 18 identified publications report outcomes specific to the brainstem-aura subtype in lasmiditan-treated patients. The prediction rests on plausible mechanistic reasoning, not on direct subtype-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31132795](https://pubmed.ncbi.nlm.nih.gov/31132795/) | 2019 | Phase 3 RCT | Brain | Randomized, placebo-controlled Phase 3 study confirming efficacy of oral lasmiditan for acute migraine, including a generalizable population with cardiovascular history. |
| [22459549](https://pubmed.ncbi.nlm.nih.gov/22459549/) | 2012 | Phase 2 RCT | The Lancet. Neurology | Dose-ranging, placebo-controlled Phase 2 study establishing efficacy and tolerability of oral lasmiditan for acute migraine treatment. |
| [33990951](https://pubmed.ncbi.nlm.nih.gov/33990951/) | 2021 | Phase 2 RCT | Headache | Placebo-controlled Phase 2 study confirming efficacy and safety of lasmiditan in Japanese migraine patients. |
| [32857291](https://pubmed.ncbi.nlm.nih.gov/32857291/) | 2020 | Systematic Review/Meta-analysis of RCTs | CNS Drugs | Confirms FDA-approved oral lasmiditan (100/200 mg) as the first 5-HT1F receptor agonist for acute migraine with or without aura. |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network Meta-analysis | The Journal of Headache and Pain | Indirect comparison of lasmiditan versus rimegepant and ubrogepant for acute oral migraine treatment, in the absence of head-to-head trials. |
| [33633424](https://pubmed.ncbi.nlm.nih.gov/33633424/) | 2020 | Review | Psychopharmacology Bulletin | Reviews lasmiditan's efficacy and safety profile for migraine treatment with or without aura. |
| [31749059](https://pubmed.ncbi.nlm.nih.gov/31749059/) | 2019 | Review (regulatory approval profile) | Drugs | Summarizes the October 2019 FDA approval of lasmiditan 50/100 mg tablets for acute migraine with or without aura, based on two pivotal Phase 3 trials. |
| [36138260](https://pubmed.ncbi.nlm.nih.gov/36138260/) | 2022 | Post-hoc subgroup analysis | Advances in Therapy | Secondary analysis of the MONONOFU trial evaluating lasmiditan efficacy across patient and migraine characteristics in Japanese patients. |
| [32783644](https://pubmed.ncbi.nlm.nih.gov/32783644/) | 2020 | Post-hoc analysis | Current Medical Research and Opinion | Post-hoc analysis of two Phase 3 RCTs showing lasmiditan efficacy/safety are maintained in patients with common migraine comorbidities. |
| [33907459](https://pubmed.ncbi.nlm.nih.gov/33907459/) | 2021 | Case report/clinical discussion | Journal of Pain Research | Describes clinical characteristics of migraine with brainstem aura accompanied by disorders of consciousness — relevant to the target disease subtype but not lasmiditan-specific. |

---

## US Market Information

No licenses/authorizations are recorded in the regulatory database (`total_licenses: 0`). This is inconsistent with literature evidence indicating lasmiditan (brand name REYVOW) received FDA approval in October 2019 — flagged for data reconciliation rather than assumed.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are not available in the current evidence pack — flagged as a blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lasmiditan's non-vasoconstrictive 5-HT1F mechanism provides a plausible rationale for use in migraine with brainstem aura, and its efficacy for general migraine (with/without aura) is well supported by Phase 2/3 RCTs and meta-analyses. However, no clinical trial or publication in this evidence pack directly studies lasmiditan in the brainstem-aura subtype, so the prediction remains mechanistic extrapolation.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (currently blocking — DG001)
- Confirmed DrugBank mechanism-of-action data (currently high-severity gap — DG002)
- Reconciliation of the "not marketed / 0 licenses" regulatory status against the literature-reported FDA approval
- A subtype-specific case series or trial in migraine with brainstem aura patients before any clinical use is considered
- Note: two other TxGNN-predicted indications for this drug (atrophoderma vermiculata, ulerythema ophryogenesis) were screened and assessed as likely knowledge-graph false positives (L5, no supporting evidence) — Hold, not pursued further.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

