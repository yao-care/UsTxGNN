---
layout: default
title: Methsuximide
parent: 僅模型預測 (L5)
nav_order: 914
evidence_level: L5
indication_count: 10
---

# Methsuximide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Methsuximide: From Antiepileptic (Absence Seizures) to Insomnia

## One-Sentence Summary

> Methsuximide is a succinimide-class anticonvulsant, pharmacologically related to ethosuximide and historically used for absence seizures — though this evidence pack's `original_indications` field itself is empty (data gap).
> The TxGNN model's top-ranked prediction is **Insomnia**, but this candidate currently has **zero clinical trials** and **zero publications** in support — it is a pure model-score prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in dataset (no licenses on file); known pharmacological class is succinimide-type anticonvulsant, same class as ethosuximide |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query returned no MOA text). Based on known pharmacological information, methsuximide belongs to the succinimide class of antiepileptics, structurally and mechanistically related to ethosuximide, with T-type calcium channel inhibition believed to underlie its anticonvulsant effect.

Succinimide-class drugs are known to carry sedation as a side effect, which is the presumed rationale behind a sedation-adjacent indication like insomnia. However, per the evidence pack's own assessment: *"無直接機轉證據；succinimide 類藥物具鎮靜副作用是已知的，但未曾作為助眠適應症開發，純屬預測分數，無支持性資料"* — there is no direct mechanistic evidence, and methsuximide has never been developed for a sleep indication. This is a score-driven prediction only.

Consistent with this, targeted searches against ClinicalTrials.gov, ICTRP, and PubMed for "methsuximide + insomnia" all returned zero results (query log entries 4–6). No mechanistic, preclinical, or clinical data currently link this drug to insomnia beyond the class-level sedation side-effect association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Methsuximide is currently not marketed in the United States, and no active NDA/BLA licenses are on file in this dataset (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not available in this evidence pack; a DDI database query also returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction is supported only by a high TxGNN model score (99.97%) with no clinical trials, no literature, and no direct mechanistic evidence — this is an L5 (model-only) evidence level, which does not meet the threshold to advance.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) data from DrugBank (flagged as High-severity data gap, DG002)
- FDA/TFDA label warnings and contraindications, required before any Stage-1 safety screening can proceed (flagged as Blocking data gap, DG001)
- Drug interaction (DDI) data — current query returned no results
- Preclinical or mechanistic studies specifically linking methsuximide to sleep/insomnia pathways
- Consider prioritizing alternative candidates from this drug's own prediction set that carry stronger evidence: restless legs syndrome (rank 7, L4, 2 supporting publications) and childhood absence epilepsy (rank 6, L3) — the latter likely reflects methsuximide's actual known/approved use rather than a genuine repurposing candidate, given the missing `original_indications` field
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

