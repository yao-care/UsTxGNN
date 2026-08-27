---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 660
evidence_level: L5
indication_count: 4
---

# Epinephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Epinephrine: From Emergency Use (Anaphylaxis/Cardiac Arrest) to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine (adrenaline) is a catecholamine classically used for life-threatening emergencies such as anaphylactic shock and cardiac arrest; the evidence pack contains no formally documented original-indication text or Taiwan market license for this drug.
The TxGNN model predicts it may also be effective for **Obstructive Lung Disease**, with a prediction score of **99.71%**, supported by **2 completed Phase 3 clinical trials** of an epinephrine inhalation aerosol in asthma plus **20 supporting publications**.
However, a **Blocking** safety data gap (missing TFDA label/warnings) currently prevents this candidate from entering formal safety pre-assessment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no original-indication or TFDA license text on file) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available in this evidence pack (data gap DG002, severity High). Based on well-established pharmacology, epinephrine is an endogenous catecholamine and non-selective adrenergic agonist acting on α1, α2, β1, and β2 receptors. Its β2-agonist activity relaxes bronchial smooth muscle (bronchodilation), which is the pharmacological basis for its historical use as an emergency bronchodilator in acute bronchospasm and anaphylaxis.

This β2-mediated bronchodilation mechanism directly explains the model's prediction for obstructive lung disease — a category spanning asthma, COPD exacerbation, and bronchiolitis. In fact, this is less a novel repurposing hypothesis than a mechanistically confirmed, historically precedented use: an epinephrine inhalation aerosol (E004, later marketed OTC as Primatene Mist HFA) completed multiple Phase 3 clinical trials specifically in pediatric and adult asthma, and racemic epinephrine nebulization has long been used (with debated efficacy) in bronchiolitis. This convergence of mechanism, historical use, and completed Phase 3 trial data reinforces the plausibility of the model's high prediction score (99.71%).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | Completed | 70 | Multi-center RCT of epinephrine inhalation aerosol (E004) vs. placebo HFA-MDI in children 4-11y with asthma; evaluated bronchodilator efficacy and safety |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Completed | 28 | Randomized, double-blind, placebo-controlled crossover single-dose study of epinephrine (E004) in pediatric asthma |
| [NCT01025648](https://clinicaltrials.gov/study/NCT01025648) | Phase 1/2 | Terminated | 9 | Dose-ranging RCT comparing Armstrong's Epinephrine HFA-MDI (E004) vs. placebo and active control (Epinephrine CFC-MDI) in adult asthma |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Phase 2 | Completed | 24 | Crossover PK study using deuterium-labeled epinephrine to distinguish exogenous drug from endogenous epinephrine in healthy volunteers |
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | Completed | 24 | PK and safety study of epinephrine inhalation aerosol HFA-MDI (E004) under augmented dose conditions |
| [NCT00116584](https://clinicaltrials.gov/study/NCT00116584) | Phase 3 | Completed | 72 | RCT of heliox-driven racemic epinephrine nebulization vs. air-oxygen driven nebulization in moderate-severe pediatric bronchiolitis |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | Completed | 120 | RCT evaluating epinephrine, dexamethasone, and hypertonic saline in children with bronchiolitis |
| [NCT03614273](https://clinicaltrials.gov/study/NCT03614273) | NA | Completed | 60 | RCT comparing nebulized hypertonic saline (3%) vs. nebulized adrenaline (epinephrine) for bronchiolitis |
| [NCT01300325](https://clinicaltrials.gov/study/NCT01300325) | Phase 4 | Completed | 136 | RCT of nebulized hypertonic saline plus epinephrine vs. normal saline plus epinephrine in hospitalized infants with bronchiolitis |
| [NCT01216553](https://clinicaltrials.gov/study/NCT01216553) | Phase 4 | Unknown | 135 | Case-control study of home oxygen therapy vs. standard nebulized therapy (including 0.1% nebulized epinephrine) in bronchiolitis with hypoxia |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Systematic Review | Cochrane Database Syst Rev | Cochrane review on epinephrine bronchodilator use for bronchiolitis; effectiveness remains uncertain despite widespread use |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Systematic Review | Cochrane Database Syst Rev | Earlier Cochrane review finding bronchodilators (including epinephrine) produce modest short-term benefit in mild-moderate bronchiolitis |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Clinical Study | Clin Pharmacol Ther | Comparative study of bronchodilator effects of terbutaline and epinephrine in patients with obstructive lung disease (abstract not provided) |
| [4551435](https://pubmed.ncbi.nlm.nih.gov/4551435/) | 1972 | Clinical Study | Annals of Allergy | Nebulized bronchodilators, including epinephrine, in obstructive lung disease (Part II; abstract not provided) |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | Reviews the role of racemic epinephrine, corticosteroids, hypertonic saline, and HFOT in pediatric bronchiolitis (2009-2018 literature) |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | Review | Medical Letter Drugs Ther | Reports the return of OTC epinephrine inhaler (Primatene Mist) for asthma bronchospasm relief |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | Pediatr Clin North Am | Reviews acute bronchiolitis and croup treatment, including nebulized adrenaline for symptomatic relief |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | Overview of bronchiolitis as the most common lower respiratory infection in infants |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clinical Evidence | Earlier overview of bronchiolitis epidemiology and management |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Review | J Allergy Clin Immunol | Classic review characterizing childhood asthma as an obstructive pulmonary airway disease |

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available at this data cutoff (TFDA label not yet obtained; DDI query returned no results).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Clinical evidence is strong (L1: ≥2 completed Phase 3 RCTs of epinephrine inhalation aerosol in asthma, plus longstanding bronchodilator precedent), but the Blocking data gap — absence of TFDA-approved label warnings/contraindications — prevents the mandatory S1 safety pre-assessment, so the candidate must Hold until that gap is resolved.

**To proceed, the following is needed:**
- TFDA package insert (PDF) retrieval and parsing to obtain warnings/contraindications (DG001, Blocking)
- DrugBank API query for complete mechanism-of-action data (DG002, High)
- A working drug-drug interaction (DDI) data source (current query: not_found)
- Confirmation of Taiwan market/license status directly against TFDA records (currently: not marketed, 0 licenses on file)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

