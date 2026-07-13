---
layout: default
title: Erenumab
parent: 僅模型預測 (L5)
nav_order: 607
evidence_level: L5
indication_count: 1
---

# Erenumab
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

Using **txgnn-pipeline** to confirm report generation scope. Now writing the evaluation report.

---

# Erenumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Erenumab is a fully humanized monoclonal antibody targeting the CGRP receptor, approved for migraine prevention in multiple countries, but not currently registered in the local market.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (ICHD-3 subtype 1.2.2),
with **no dedicated clinical trials** but **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine prevention (episodic and chronic) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Market Status | Not registered (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Erenumab is a fully humanized IgG2 monoclonal antibody that selectively binds and blocks the calcitonin gene-related peptide (CGRP) receptor, interrupting CGRP-mediated neurogenic inflammation and vasodilation along the trigeminal vascular pathway. CGRP is the central neuropeptide released during migraine attacks, and blocking its receptor has demonstrated robust efficacy in preventing both episodic and chronic migraine in Phase 3 trials.

Migraine with brainstem aura (MwBA, formerly "basilar-type migraine") is ICHD-3 subtype 1.2.2, defined by aura symptoms originating from brainstem structures — dysarthria, vertigo, tinnitus, diplopia, and ataxia — followed by headache. The underlying pathophysiology involves brainstem cortical spreading depression (CSD) and downstream activation of the trigeminal vascular system: precisely the circuit where CGRP is densely expressed, including in the dorsal raphe nucleus and trigeminal nucleus caudalis. The mechanistic overlap with erenumab's target is therefore direct and strong.

A particularly compelling clinical rationale exists here: MwBA has historically been a therapeutic orphan because triptans and ergotamine were considered contraindicated due to concern over basilar artery vasospasm. Erenumab, as a large-molecule receptor blocker with no vasoconstrictive pharmacology, sidesteps this concern entirely — representing a genuine clinical unmet need. One important mechanistic caveat emerges from PMID 38850034, which demonstrates that sildenafil-induced migraine attacks proceed via the cGMP pathway independently of CGRP receptor activation, suggesting that a subset of MwBA episodes may be non-CGRP-dependent and therefore less responsive to erenumab.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine with brainstem aura specifically.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | Phase 3 RCT Secondary Analysis | JAMA Neurology | Erenumab shows comparable safety and efficacy in migraine with aura vs. without aura; no elevated vascular risk in aura subgroup |
| [35230406](https://pubmed.ncbi.nlm.nih.gov/35230406/) | 2022 | RCT Subgroup Report | JAMA | Confirms erenumab is safe and effective for patients with migraine with aura across pooled Phase 3 data |
| [41888647](https://pubmed.ncbi.nlm.nih.gov/41888647/) | 2026 | Prospective RCT (REFORM) | J Headache Pain | Characterizes longitudinal changes in aura frequency during and after erenumab preventive treatment in adults with confirmed migraine aura |
| [40275185](https://pubmed.ncbi.nlm.nih.gov/40275185/) | 2025 | Prospective Biomarker Study (REFORM) | J Headache Pain | suPAR (a systemic inflammation marker elevated in migraine with aura) is linked to erenumab treatment response, supporting CGRP-inflammatory axis in aura subtypes |
| [38850034](https://pubmed.ncbi.nlm.nih.gov/38850034/) | 2024 | Provocation RCT / Mechanistic | Cephalalgia | Sildenafil-induced attacks (cGMP pathway) occur independently of CGRP receptor activation under erenumab pretreatment — identifies a potential efficacy ceiling in MwBA |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Prospective Observational | Headache | Long-term CV safety of erenumab stratified by baseline CV risk; no excess risk in high-risk patients — directly relevant to MwBA's vascular concerns |
| [32867533](https://pubmed.ncbi.nlm.nih.gov/32867533/) | 2021 | Prospective Mechanistic | Cephalalgia | Erenumab does not alter cerebral vasomotor reactivity or flow-mediated dilation — supports haemodynamic safety in brainstem-involved migraine variants |
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | Phase 3b RCT | Lancet | Erenumab efficacious and well-tolerated in episodic migraine patients who failed 2–4 prior preventive treatments; establishes treatment-resistant population benefit |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic Review | Int Immunopharmacology | Comprehensive systematic review of erenumab efficacy across episodic and chronic migraine prevention; confirms consistent benefit across trial populations |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handb Exp Pharmacology | Foundational review of CGRP's role in migraine pathophysiology, including the aura subtype and trigeminal-brainstem network |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note from mechanistic review:** Erenumab lacks vasoconstrictive activity, which is directly relevant for MwBA — a subtype historically excluded from triptan and ergotamine use. Pooled long-term trial data (PMID 36942409) shows no elevated cardiovascular signal even in higher-risk patients. Cerebral haemodynamic studies (PMID 32867533) confirm no adverse effect on cerebral vasomotor reactivity. Given the brainstem involvement in MwBA, baseline neurovascular assessment is recommended before treatment initiation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The biological rationale is strong and mechanistically coherent — CGRP plays a well-established role in the brainstem-trigeminal circuit underlying MwBA, and erenumab's non-vasoconstrictive profile uniquely removes the principal historical barrier to treating this subtype. Indirect clinical evidence from Phase 3 RCT secondary analyses and real-world studies in migraine with aura broadly supports safety and efficacy, though no dedicated trial exists for ICHD-3 1.2.2 specifically.

**To proceed, the following is needed:**
- Prospective clinical study or pre-specified subgroup analysis in patients with confirmed MwBA (ICHD-3 1.2.2 criteria), to generate direct efficacy data
- Full MOA documentation from DrugBank or prescribing information (currently unavailable)
- Regulatory registration strategy for the target market
- Safety monitoring protocol incorporating baseline cerebrovascular and cardiovascular assessment, given MwBA's brainstem origin
- Investigation of cGMP-pathway-driven attack prevalence in MwBA to define the likely responder population and expected efficacy ceiling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

