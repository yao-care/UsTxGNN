---
layout: default
title: Peppermint Oil
parent: 僅模型預測 (L5)
nav_order: 1031
evidence_level: L5
indication_count: 10
---

# Peppermint Oil
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

# Peppermint Oil: From No Registered Indication to Cardiovascular Disease (Exploratory)

## One-Sentence Summary

Peppermint Oil (DrugBank DB11198) has no approved indication on record and is not currently marketed in Taiwan.
Among 10 TxGNN-predicted indications, the only one with any supporting clinical or literature evidence is **Cardiovascular Disease**,
backed by **2 completed early-phase human trials (n=36–40)**, **1 ongoing RCT protocol**, and **6 relevant publications** — evidence level **L3**.
Note: the model's single highest-scoring prediction (leprosy) and several others (pneumocystosis, coronary artery disease, myocardial ischemia, various polyp indications) currently have **zero supporting trials or literature** and are algorithmic associations only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication on record; drug not marketed in Taiwan |
| Predicted New Indication | Cardiovascular Disease |
| TxGNN Prediction Score | 99.13% (rank 9 of 10 by score, but the only prediction with real-world evidence) |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for peppermint oil as a whole product. Based on the evidence pack, the working hypothesis relies on menthol — its principal constituent — acting as a **TRPM8/TRPA1 receptor agonist** with known smooth-muscle-relaxant and vagal (parasympathetic) activating effects. One physiological study (PMID 30070742) found that gastric cooling and menthol stimulation increase cardiac parasympathetic efferent activity in healthy volunteers, providing a plausible mechanistic route from a gastrointestinal-acting compound to cardiovascular autonomic modulation.

Because no original approved indication exists in this evidence pack, the relationship between "original use" and "predicted new indication" cannot be formally established. What is available instead is early human interventional data: two completed, small, non-randomized (Phase NA) studies testing oral peppermint on blood pressure and cardiometabolic parameters, plus a newly registered placebo-controlled RCT protocol (PMID 40333716) specifically designed to test peppermint oil in pre-/stage-1 hypertension. This progression — mechanism study → small open-label studies → registered RCT — is why cardiovascular disease reaches decision stage S1 while the model's top-ranked prediction (leprosy) and most others remain at S0 with no evidence at all.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05561543](https://clinicaltrials.gov/study/NCT05561543) | N/A | Completed | 40 | Tested effects of oral peppermint on cardiometabolic outcomes in participants with mild–moderate hypertension; builds on prior trial showing peppermint improved systolic BP and lipids in healthy individuals |
| [NCT05071833](https://clinicaltrials.gov/study/NCT05071833) | N/A | Completed | 36 | Tested oral peppermint supplementation's effect on cardiometabolic parameters; first randomized follow-up to earlier non-randomized findings |

*Note: A third trial (NCT04966546, chronic subdural hematoma post-op) appeared in the evidence pack but was graded low-relevance (C) and withdrawn with zero enrollment — excluded here as not informative for this indication.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40333716](https://pubmed.ncbi.nlm.nih.gov/40333716/) | 2025 | RCT Protocol | PLoS ONE | Protocol for a placebo-controlled RCT testing peppermint oil (menthol/flavonoid-rich) in pre- and stage-1 hypertension |
| [30070742](https://pubmed.ncbi.nlm.nih.gov/30070742/) | 2018 | Mechanism Study | Experimental Physiology | Gastric cooling and menthol stimulation increase cardiac parasympathetic efferent activity in healthy adults |
| [25037671](https://pubmed.ncbi.nlm.nih.gov/25037671/) | 2014 | Review | Explore (NY) | Broad CAM review citing peppermint oil's established use for irritable bowel syndrome |
| [19198983](https://pubmed.ncbi.nlm.nih.gov/19198983/) | 2009 | Review | Internal and Emergency Medicine | General practice/cardiovascular medicine evidence update (abstract not available) |
| [27277875](https://pubmed.ncbi.nlm.nih.gov/27277875/) | 2016 | Pharmacokinetic/Analytical | Bioanalysis | Real-time breath monitoring after oral peppermint capsule ingestion; tracked menthone rise and fall over 10 hours |
| [17577363](https://pubmed.ncbi.nlm.nih.gov/17577363/) | 2007 | Case Report | Contact Dermatitis | Allergic contact dermatitis reaction to a topical peppermint foot spray (safety signal, non-cardiovascular) |

## US Market Information

Peppermint oil currently holds **zero licenses/NDAs** in the Taiwan regulatory dataset and is marked **未上市 (Not Marketed)**. No approved indication text, dosage form, or brand information is available in this evidence pack.

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) is currently available — all fields in the evidence pack are flagged as data gaps, and the drug interaction query returned no results. Because peppermint oil is not marketed in Taiwan, no local package insert exists to reference. This is recorded as a **Blocking** data gap (DG001) that must be resolved before any formal safety assessment (S1) can be completed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence is limited to two small (n=36–40), non-randomized/open-label studies and one not-yet-completed RCT protocol — insufficient for a Go decision at L3.
- The model's highest-scoring predictions (leprosy, pneumocystosis, coronary artery disease, etc.) have **no clinical or literature support whatsoever** and should not be prioritized over cardiovascular disease.
- A Blocking data gap on TFDA/regulatory warnings (DG001) prevents any formal safety sign-off regardless of efficacy evidence.

**To proceed, the following is needed:**
- Results from the ongoing/protocol-stage RCT (PMID 40333716) once completed
- Confirmed mechanism of action (MOA) documentation from DrugBank (DG002)
- TFDA (or equivalent) label warnings/contraindications and drug interaction data (DG001)
- A larger, adequately powered randomized controlled trial specifically in cardiovascular disease or hypertension populations
- Reassessment of whether the top TxGNN-scored predictions (e.g., leprosy) warrant continued tracking, or should be deprioritized given the complete absence of supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

