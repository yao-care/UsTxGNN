---
layout: default
title: Terbutaline
parent: 僅模型預測 (L5)
nav_order: 631
evidence_level: L5
indication_count: 3
---

# Terbutaline
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

# Terbutaline: From Bronchospasm to Obstructive Lung Disease

## One-Sentence Summary

Terbutaline is a selective β2-adrenergic receptor agonist globally recognized as a first-line bronchodilator for bronchospasm in asthma and COPD, though no active US market registrations are currently on record in the database.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease**,
with **48 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bronchospasm (asthma, COPD) — internationally recognized; no active US licenses found in current dataset |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (0 active licenses on record) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Terbutaline is a selective β2-adrenergic receptor (β2-AR) agonist. When inhaled or administered systemically, it binds to β2-ARs on bronchial smooth muscle cells, triggering an increase in intracellular cyclic AMP (cAMP). This cascade leads to smooth muscle relaxation, dilation of the bronchial lumen, and a consequent reduction in airway resistance — the core pathophysiological mechanism directly targeting obstructive lung disease.

Obstructive lung disease encompasses conditions such as asthma and COPD, both characterized by reversible or partially reversible airflow limitation. Terbutaline's mechanism is not merely plausible for this indication — it represents the gold-standard therapeutic rationale underpinning the entire short-acting β2-agonist (SABA) drug class, of which terbutaline (Bricanyl®/Brethine®) is a canonical member approved in numerous international markets. The TxGNN prediction therefore reflects biological and pharmacological reality rather than a speculative mechanistic leap.

The strength of this prediction is further validated by the breadth and quality of supporting evidence: multiple completed Phase 3 randomized controlled trials directly involving terbutaline in asthma and COPD, spanning rescue bronchodilation, maintenance therapy comparison, and acute exacerbation management. The absence of current US market registration in the database most likely reflects a data collection gap, rather than a lack of clinical utility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01944033](https://clinicaltrials.gov/study/NCT01944033) | Phase 3 | Completed | 250 | Directly compared β2-agonists alone versus β2-agonists combined with ipratropium bromide for COPD acute exacerbation in the emergency department; assessed clinical outcomes and arterial blood gas parameters. |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Completed | 120 | Head-to-head RCT comparing IV magnesium sulfate versus IV terbutaline in children with acute asthma exacerbations in the emergency setting; directly evaluates terbutaline efficacy as standard care. |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Completed | 3,850 | Three-arm study comparing Symbicort as-needed, terbutaline as-needed, and Pulmicort twice daily plus terbutaline as-needed in mild-to-moderate asthma; terbutaline serves as active comparator defining SABA standard of care. |
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Completed | 4,215 | Compared Symbicort as-needed versus Pulmicort twice daily plus terbutaline as-needed in mild asthma patients; large multinational trial validating terbutaline as the gold-standard rescue comparator. |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Completed | 2,091 | Compared Symbicort SMART (maintenance and reliever) with Symbicort fixed-dose plus terbutaline as-needed; demonstrated terbutaline as the benchmark rescue inhaler in asthma management over 12 months. |
| [NCT00421122](https://clinicaltrials.gov/study/NCT00421122) | Phase 3 | Completed | 315 | Evaluated efficacy and safety of Symbicort Turbuhaler versus Bricasol® pMDI (terbutaline) in Chinese COPD patients per GOLD guidelines; supports terbutaline's role as a rescue bronchodilator in COPD. |
| [NCT00326053](https://clinicaltrials.gov/study/NCT00326053) | Phase 3 | Completed | 600 | Compared budesonide/formoterol combination with budesonide plus terbutaline as-needed for prevention of asthma relapse post-emergency discharge; directly positions terbutaline as active rescue control. |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Completed | 24 | Single-blind crossover study directly evaluating relative efficacy of terbutaline Turbuhaler 0.4 mg versus salbutamol pMDI 200 µg in Japanese adult asthmatic patients; also assessed safety via adverse events and vital signs. |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Completed | 95 | Double-blind crossover pharmacodynamic study evaluating Bricanyl (terbutaline) Turbuhaler M3 versus M2 formulations via methacholine-induced bronchoconstriction protection; directly assesses terbutaline device performance. |
| [NCT00242775](https://clinicaltrials.gov/study/NCT00242775) | Phase 3 | Completed | 2,100 | Compared Symbicort variable dose with Seretide plus terbutaline as-needed rescue in persistent asthma patients over 6 months; large multinational trial providing indirect safety and efficacy reference for terbutaline in obstructive lung disease. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | RCT | Academic Emergency Medicine | Randomized double-blind trial comparing nebulized terbutaline alone versus terbutaline plus ipratropium in hypercapnic AECOPD patients requiring non-invasive ventilation; SABA (terbutaline) established as mainstay of ED treatment. |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | British Journal of Diseases of the Chest | Double-blind crossover RCT in 10 moderate-to-severe COPD patients; oral terbutaline (2.5 mg TID × 1 week) significantly increased peak inspiratory mouth pressure (+5.8 cmH₂O) and transdiaphragmatic pressure (+5.0 cmH₂O) versus placebo. |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | International Journal of Clinical Pharmacology | Double-blind two-week trial comparing clenbuterol (30 µg TID) with terbutaline sulfate (5 mg TID) in 24 COLD patients with partially reversible obstruction; both agents improved FEV₁, sRaw, and V50% VC, demonstrating terbutaline's bronchodilator efficacy in COLD. |
| [2031046](https://pubmed.ncbi.nlm.nih.gov/2031046/) | 1991 | RCT | Pneumologie | Randomized crossover study in 10 COPD patients evaluating nebulized terbutaline (5 mg TID) with and without positive expiratory pressure (PEP); both terbutaline arms demonstrated improvements in symptom scores and peak expiratory flow versus placebo. |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Clinical Study | Annals of Palliative Medicine | Investigated clinical value of N-acetylcysteine combined with terbutaline sulfate in elderly COPD patients; also analyzed effects on apoptosis/anti-apoptosis mechanisms, demonstrating that the combination improved clinical outcomes beyond bronchodilation alone. |
| [18761816](https://pubmed.ncbi.nlm.nih.gov/18761816/) | 2008 | Clinical Study | Cellular & Molecular Immunology | Atomization inhalation of budesonide combined with terbutaline plus conventional therapies in AECOPD patients; demonstrated improvements in airway hyperreactivity (AHR) and immune parameters compared to standard care alone. |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | Clinical Study | Respiratory Medicine | Double-blind placebo-controlled crossover study evaluating terbutaline via Turbuhaler in COLD patients; assessed spirometry (FEV₁, FVC), 6-minute walking distance, and dyspnoea during exercise. |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | Clinical Study | Lung | Double-blind placebo-controlled crossover study in 26 COPD patients (FEV₁ 40–70% predicted); single-dose terbutaline Turbuhaler improved resting lung function and exercise capacity versus placebo. |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | Clinical Study | Chest | Double-blind crossover study in 35 COLD patients with concurrent ischemic heart disease or hypertension; evaluated interaction between β-blockers (metoprolol, propranolol) and terbutaline, demonstrating that terbutaline maintained bronchodilator efficacy even in this high-risk population. |
| [8882073](https://pubmed.ncbi.nlm.nih.gov/8882073/) | 1996 | Clinical Study | Thorax | Evaluated whether cessation of regular inhaled terbutaline therapy in COPD patients causes rebound airway responsiveness or bronchoconstriction; provided important data on dose dependency and withdrawal effects relevant to long-term COPD management. |

---

## Market Authorization Information

No active US market authorizations were found in the current dataset (0 licenses recorded). This may reflect a data collection gap, as terbutaline (Brethine®) has historically held FDA approval for bronchospasm in obstructive pulmonary diseases including asthma and COPD. Verification against the FDA Orange Book is recommended before regulatory decisions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Terbutaline's mechanism of action (selective β2-AR agonism → smooth muscle relaxation → airway dilation) directly targets the pathophysiology of obstructive lung disease, and the evidence base is exceptional — multiple completed Phase 3 RCTs involving tens of thousands of patients, in which terbutaline consistently functions as the gold-standard active comparator. The L1 evidence level reflects genuine clinical validation, not merely model prediction.

**To proceed, the following is needed:**

- **Regulatory clarification**: Verify current FDA Orange Book status; the 0-license finding likely reflects a data collection gap and should be confirmed before any filing or market-entry decision
- **Safety data retrieval**: Obtain full prescribing information (package insert warnings, contraindications, black box warnings) from FDA label — particularly important given known cardiovascular effects of β2-agonists at higher doses
- **Drug interaction profile**: Query DDI databases for clinically significant interactions (β-blockers, MAOIs, diuretics, sympathomimetics), as no interaction data was retrieved in this Evidence Pack
- **US-specific indication scoping**: Clarify whether the target indication is asthma, COPD, or the broader "obstructive lung disease" umbrella, as regulatory pathways and comparator requirements differ
- **Formulation and route strategy**: Define target formulation (inhaled Turbuhaler, pMDI, nebulized, IV/SQ) and route based on intended patient population and indication, as evidence supports multiple routes with differing safety profiles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

