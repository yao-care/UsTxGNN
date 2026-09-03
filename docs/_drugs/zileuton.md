---
layout: default
title: Zileuton
parent: 僅模型預測 (L5)
nav_order: 1305
evidence_level: L5
indication_count: 10
---

# Zileuton
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

# Zileuton: From Asthma to Chronic Obstructive Pulmonary Disease (COPD)

## One-Sentence Summary

> Zileuton is a 5-lipoxygenase (5-LOX) inhibitor already established for asthma management (marketed in the US as Zyflo/Zyflo CR), though it is currently **not marketed** in this jurisdiction and holds no active local license.
> The TxGNN model's raw top hit ("bronchitis") had **zero supporting evidence**, so this report focuses on the highest-scoring candidate that is actually backed by real data: **Obstructive Lung Disease (COPD)**,
> supported by **8 clinical trials** (including one Phase 3 COPD-exacerbation trial) and **20 publications**, though evidence remains preliminary (L2) and a critical safety data gap blocks any safety screening.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (established off-pack via trial descriptions confirming FDA-approved use; not present in the formal license registry because the drug is unmarketed here) |
| Predicted New Indication | Obstructive Lung Disease (COPD) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Market Status | ✗ Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

**Note on indication selection**: TxGNN's #1 raw-score prediction was "bronchitis" (99.99%), but that candidate has **no clinical trials or literature at all** (L5, flagged in the model's own rationale as "僅為知識圖譜高分預測" — a high score with no supporting evidence). We instead lead with COPD/Obstructive Lung Disease, the strongest **evidence-backed** new-indication candidate in this pack.

---

## Why is This Prediction Reasonable?

Zileuton is a selective inhibitor of 5-lipoxygenase (5-LOX), the enzyme responsible for the first committed step in converting arachidonic acid into leukotrienes (LTB4 and the cysteinyl leukotrienes LTC4/D4/E4). These leukotrienes drive bronchoconstriction, airway inflammation, mucus hypersecretion, and eosinophil recruitment — the mechanism underlying zileuton's established use in asthma. (This mechanistic detail is drawn from the evidence pack's literature and trial rationale text, since the structured `original_moa` field itself is a data gap.)

Asthma and COPD are both obstructive airway diseases sharing the leukotriene inflammatory pathway, which is why the model surfaces COPD as a plausible extension. However, the pack's own rationale flags an important caveat: COPD inflammation is predominantly **neutrophil**-driven, while asthma is predominantly **eosinophil**-driven — a mechanistic difference that weakens the strength of direct extrapolation. This is consistent with the clinical evidence: a Phase 3 trial testing zileuton specifically for COPD exacerbations (NCT00493974) was **terminated**, leaving the COPD hypothesis mechanistically plausible but clinically unconfirmed.

For context, the same evidence pack shows **asthma itself** re-emerging as a top TxGNN candidate with the strongest evidence of any indication in the set (L1, multiple completed Phase 2–4 RCTs) — effectively validating that the 5-LOX/leukotriene mechanism captured by the model matches zileuton's known real-world use. Two other exploratory signals are also worth noting at lower confidence: lung cancer chemoprevention in patients with bronchial dysplasia (L2, including a completed Phase 2 chemoprevention trial, NCT00056004) and atopic dermatitis (L3, small pilot studies). Several other top-ranked predictions (bronchitis, "asthma-related traits, susceptibility to," Laubry-Pezzi syndrome, interventricular septum aneurysm, Pierre Robin syndrome) have **no supporting evidence whatsoever** and are assessed as likely knowledge-graph noise.

---

## Clinical Trial Evidence

*(Evidence for Obstructive Lung Disease / COPD)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00493974](https://clinicaltrials.gov/study/NCT00493974) | Phase 3 | Terminated | 119 | Direct test of zileuton for reducing hospital stay in COPD exacerbations; trial stopped early, efficacy inconclusive |
| [NCT00486343](https://clinicaltrials.gov/study/NCT00486343) | Phase 4 | Terminated | 400 | Zileuton CR vs. placebo in poorly controlled asthma on moderate-dose ICS; terminated |
| [NCT00575861](https://clinicaltrials.gov/study/NCT00575861) | Phase 4 | Completed | 19 | Additive effect of zileuton to Advair on exhaled/bronchial/alveolar nitric oxide in asthmatics |
| [NCT00595114](https://clinicaltrials.gov/study/NCT00595114) | N/A | Completed | 43 | Ancillary study of oxidative stress and anti-inflammatory lipids in airway disease (COPD and asthma) |
| [NCT00299065](https://clinicaltrials.gov/study/NCT00299065) | Phase 1/2 | Completed | 60 | Safety, tolerability, and PK of IV zileuton in asthma patients |
| [NCT00723021](https://clinicaltrials.gov/study/NCT00723021) | Phase 2a | Completed | 15 | Bronchodilatory action, safety, and PK of PF-04191834 vs. zileuton in asthmatics |
| [NCT00534625](https://clinicaltrials.gov/study/NCT00534625) | Phase 2 | Completed | 36 | Pulmonary function, safety, and PK of IV zileuton in chronic stable asthma |
| [NCT01805687](https://clinicaltrials.gov/study/NCT01805687) | Phase 4 | Completed | 25 | Duration and extent of bronchodilation with Zyflo CR 1200 mg in stable chronic asthma |

---

## Literature Evidence

*(Evidence for Obstructive Lung Disease / COPD, prioritized by relevance)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10421833](https://pubmed.ncbi.nlm.nih.gov/10421833/) | 1999 | Review | Clin Exp Allergy | Reviews leukotriene pathway inhibitors, including zileuton, across both asthma and COPD |
| [33446622](https://pubmed.ncbi.nlm.nih.gov/33446622/) | 2020 | Review | Medical Letter on Drugs and Therapeutics | Overview of current asthma drug classes including leukotriene modifiers |
| [8826571](https://pubmed.ncbi.nlm.nih.gov/8826571/) | 1996 | Review | Ann Pharmacother | Introduces zileuton as the first 5-LOX inhibitor approved for asthma |
| [31841698](https://pubmed.ncbi.nlm.nih.gov/31841698/) | 2020 | Clinical Study | Pulm Pharmacol Ther | Zileuton response varies by asthma phenotype; modest overall response rates |
| [37253655](https://pubmed.ncbi.nlm.nih.gov/37253655/) | 2023 | Preclinical | Am J Physiol Lung Cell Mol Physiol | 5-LOX pathway elevated in severe/fungal-associated asthma; zileuton is an FDA-approved therapeutic targeting this pathway |
| [26385352](https://pubmed.ncbi.nlm.nih.gov/26385352/) | 2015 | Review | Curr Allergy Asthma Rep | Reviews antileukotriene efficacy across upper/lower airway inflammatory diseases |
| [11527015](https://pubmed.ncbi.nlm.nih.gov/11527015/) | 2001 | Review | Curr Opin Investig Drugs | Discusses zileuton's successor compound (ABT-761), context on 5-LOX inhibition potency |
| [9042024](https://pubmed.ncbi.nlm.nih.gov/9042024/) | 1997 | Review | Chest | Leukotrienes' role in airflow obstruction mechanisms relevant to both asthma and COPD |
| [32000655](https://pubmed.ncbi.nlm.nih.gov/32000655/) | 2020 | Review | Recent Pat Inflamm Allergy Drug Discov | Role of leukotriene inhibitors across chronic inflammatory diseases |
| [16894531](https://pubmed.ncbi.nlm.nih.gov/16894531/) | 2007 | Review | Med Res Rev | Critical update on cysteinyl-leukotrienes and receptors in asthma and other inflammatory diseases |

---

## Market Information

No license records are available — `taiwan_regulatory.licenses` is empty and `total_licenses = 0`. Zileuton is currently **not marketed** in this jurisdiction; any repurposing pathway would require a new market authorization filing rather than a label extension.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Important note**: The evidence pack flags a **Blocking-severity data gap (DG001)** — TFDA label warnings/contraindications are unavailable, which means **this candidate cannot yet enter S1 safety screening**. This gap must be resolved before any further evaluation stage is attempted.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pivotal COPD-specific trial (NCT00493974) was terminated, evidence level is only L2, and — critically — a Blocking data gap in label warnings/contraindications prevents even a basic safety screening (S1). The drug is also not currently marketed in this jurisdiction, so a new indication would require a full new filing rather than a label extension.

**To proceed, the following is needed:**
- TFDA-equivalent package insert / warnings and contraindications (resolve DG001, currently Blocking)
- Confirmed mechanism-of-action documentation via DrugBank API (resolve DG002)
- Clarification of why NCT00493974 was terminated, and whether any completed/ongoing COPD trials exist elsewhere
- A market-entry assessment, since the drug currently holds zero local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

