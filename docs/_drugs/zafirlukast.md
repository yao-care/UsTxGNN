---
layout: default
title: Zafirlukast
parent: 僅模型預測 (L5)
nav_order: 1300
evidence_level: L5
indication_count: 2
---

# Zafirlukast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Zafirlukast: From Asthma to Obstructive Airway Disease (Bronchitis / COPD)

## One-Sentence Summary

> Zafirlukast is a cysteinyl leukotriene receptor (CysLT1/LTD4) antagonist originally developed and marketed for chronic asthma prophylaxis and treatment.
> TxGNN predicts potential efficacy in **bronchitis** (score 99.93%, no supporting evidence) and, with stronger real-world support, in **obstructive lung disease / COPD** (score 99.17%),
> with **0 clinical trials** but **20 publications** — including two small comparative/RCT studies — supporting the latter direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic asthma (prophylaxis and treatment) — based on literature (PMID 9463793); no structured Taiwan license record exists for this drug |
| Predicted New Indication | Bronchitis (rank 1, no evidence) / Obstructive Lung Disease (COPD, rank 2, literature-supported) |
| TxGNN Prediction Score | Bronchitis: 99.93% · Obstructive Lung Disease: 99.17% |
| Evidence Level | Bronchitis: L5 · Obstructive Lung Disease: L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`). However, the literature evidence consistently and independently confirms zafirlukast's known pharmacology: it is a competitive, selective cysteinyl leukotriene receptor (CysLT1/LTD4) antagonist that blocks leukotriene-mediated bronchoconstriction, airway inflammation, mucus hypersecretion, and vascular permeability (PMID 9463793, 10421833, 9042024). It was approved in the US (Accolate) for chronic asthma.

Bronchitis and COPD share the same downstream pathology — airway inflammation, bronchoconstriction, and mucus hypersecretion — that cysteinyl leukotrienes drive in asthma. This gives the TxGNN prediction a plausible mechanistic basis: a drug class effect (leukotriene receptor antagonism) extending from one obstructive airway disease (asthma) to pathophysiologically related ones (bronchitis, COPD).

For obstructive lung disease specifically, this mechanistic rationale is reinforced by direct clinical data: a randomized, double-blind, placebo-controlled crossover study in severe COPD patients (PMID 12877822) and a comparative study of zafirlukast combined with salmeterol in COPD (PMID 11694805) both demonstrated measurable bronchodilator effects. For bronchitis, no such direct clinical or preclinical data exists — the link is inferred purely from drug-class mechanism, and the TxGNN score alone does not constitute clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for either bronchitis or obstructive lung disease).

---

## Literature Evidence

*(Evidence shown for obstructive lung disease — the only predicted indication with literature support)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12877822](https://pubmed.ncbi.nlm.nih.gov/12877822/) | 2003 | RCT (crossover) | Pulm Pharmacol Ther | Randomized, double-blind, placebo-controlled crossover study; zafirlukast improved airway function in severe COPD patients |
| [23741166](https://pubmed.ncbi.nlm.nih.gov/23741166/) | 2013 | Clinical study | Med J Islam Repub Iran | Evaluated effect of zafirlukast on improving lung function in COPD patients |
| [11694805](https://pubmed.ncbi.nlm.nih.gov/11694805/) | 2001 | Cohort/Comparative | Respiration | Compared bronchodilating effect of salmeterol + zafirlukast combination vs. single agents in asthma and COPD |
| [9463793](https://pubmed.ncbi.nlm.nih.gov/9463793/) | 1998 | Review | Drugs | Comprehensive pharmacology/therapeutic review; confirms CysLT1 antagonism as core mechanism |
| [10421833](https://pubmed.ncbi.nlm.nih.gov/10421833/) | 1999 | Review | Clin Exp Allergy | Reviews leukotriene pathway inhibitors in both asthma and COPD |
| [31544544](https://pubmed.ncbi.nlm.nih.gov/31544544/) | 2019 | Review | Expert Rev Respir Med | Update on leukotriene receptor antagonist treatments in obstructive airway disease |
| [27826703](https://pubmed.ncbi.nlm.nih.gov/27826703/) | 2017 | Review | Handb Exp Pharmacol | Reviews LTRA class pharmacology and clinical use, including airway obstruction |
| [11888331](https://pubmed.ncbi.nlm.nih.gov/11888331/) | 2002 | PK Review | Clin Pharmacokinet | Pharmacokinetic profile of zafirlukast relevant to dosing in airway disease |
| [10023966](https://pubmed.ncbi.nlm.nih.gov/10023966/) | 1999 | Review | Lancet | Overview of leukotriene-receptor antagonists as a hybrid anti-inflammatory/bronchodilator class |
| [33446622](https://pubmed.ncbi.nlm.nih.gov/33446622/) | 2020 | Review | Med Lett Drugs Ther | Current drug-class summary for asthma/airway obstruction management |

---

## US Market Information

Zafirlukast holds **no Taiwan license/NDA** in this evidence pack (`total_licenses: 0`, market status: 未上市/Not marketed). No product records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No key warnings, contraindications, or drug interaction data are currently available in this evidence pack. A DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The higher-scoring prediction (bronchitis, TxGNN 99.93%) has **zero supporting clinical or literature evidence** (L5) and is a pure mechanism-extrapolation.
- The evidence-backed prediction (obstructive lung disease/COPD, L3) is supported only by small comparative/crossover studies, not confirmatory RCTs, and the drug is **not currently marketed in Taiwan** (no NDA, no local safety labeling).
- A **Blocking** data gap exists (DG001: TFDA warnings/contraindications unavailable), which by itself prevents progression past the initial safety screening (S1) regardless of efficacy evidence.

**To proceed, the following is needed:**
- Obtain TFDA (or equivalent) product labeling — warnings, contraindications, hepatotoxicity data (zafirlukast carries known hepatotoxicity signals per PMID 12879996) — to resolve DG001
- Confirm structured MOA data via DrugBank API to resolve DG002
- Design or identify dedicated, adequately powered RCTs for bronchitis and COPD as primary endpoints, rather than relying on asthma-derived mechanistic reasoning
- Evaluate feasibility/rationale for local market entry, since the drug currently has no Taiwan license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

