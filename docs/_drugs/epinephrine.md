---
layout: default
title: Epinephrine
parent: Model Prediction Only (L5)
nav_order: 660
evidence_level: L5
indication_count: 4
---

# Epinephrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Epinephrine: From Original Indication (Not Recorded) to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine is a non-selective adrenergic agonist that is already marketed in the US in injectable, nasal spray and other forms, but the source data does not record its original approved indication.
The TxGNN model predicts it may be effective for **obstructive lung disease**.
This is supported by **several epinephrine-related clinical trials (including 3 completed Phase 3 studies)** and **a body of literature that includes 2 Cochrane reviews**, though this may partly reflect established use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (all approved-indication fields are empty) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L2 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

*Evidence level note: the L2 level follows the Evidence Pack scoring. Three completed Phase 3 studies involve epinephrine products (NCT01460511, NCT01737905, NCT00116584). They are small, they cover pediatric asthma and bronchiolitis, and no results were supplied. Their relevance grading is still pending, so I did not upgrade to L1.*

---

## Why is This Prediction Reasonable?

Epinephrine stimulates both alpha and beta adrenergic receptors. Beta-2 stimulation relaxes bronchial smooth muscle, and alpha-1 stimulation reduces mucosal swelling. Together these effects address the main problems of airway obstruction. Detailed mechanism data from DrugBank was not available, so this description rests on well-established pharmacology.

Airway obstruction diseases such as asthma and bronchiolitis involve narrowed airways from muscle spasm and swelling. This matches what epinephrine does, and the literature shows a long history of use, including older bronchodilator studies, nebulized use in infants, and the return of an over-the-counter epinephrine inhaler in 2019.

Two cautions apply. First, because no original indication is recorded, this prediction may reflect existing use rather than a new discovery. Second, the evidence for bronchiolitis is mixed. Cochrane-type reviews of epinephrine for bronchiolitis exist, but the supplied data contains no clear Phase 3 evidence that settles the question.

---

## Clinical Trial Evidence

The Evidence Pack does not include results for these trials, so the findings below describe study design and purpose only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | Completed | 70 | Epinephrine inhalation aerosol (E004) vs placebo, 4-week parallel study in children aged 4-11 with asthma |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Completed | 28 | Single-dose E004 vs placebo crossover in children aged 4-11 with asthma |
| [NCT00116584](https://clinicaltrials.gov/study/NCT00116584) | Phase 3 | Completed | 72 | Racemic epinephrine nebulized with heliox vs air-oxygen in moderate to severe bronchiolitis |
| [NCT03614273](https://clinicaltrials.gov/study/NCT03614273) | NA | Completed | 60 | Nebulized 3% hypertonic saline vs nebulized adrenaline in bronchiolitis (randomized) |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | Completed | 120 | Pilot randomized trial of epinephrine, dexamethasone and hypertonic saline in bronchiolitis |
| [NCT01300325](https://clinicaltrials.gov/study/NCT01300325) | Phase 4 | Completed | 136 | Nebulized hypertonic saline vs normal saline, each with epinephrine, in hospitalized infants with bronchiolitis |
| [NCT05363670](https://clinicaltrials.gov/study/NCT05363670) | Phase 2 | Completed | 18 | Intranasal epinephrine (ARS-1) vs albuterol vs placebo in persistent asthma (crossover) |
| [NCT01025648](https://clinicaltrials.gov/study/NCT01025648) | Phase 1/2 | Terminated | 9 | Dose-ranging crossover of epinephrine HFA-MDI (E004) vs placebo and epinephrine CFC-MDI in asthma |
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | Completed | 24 | Pharmacokinetics and safety of epinephrine inhalation aerosol (E004) in healthy adults |
| [NCT01216553](https://clinicaltrials.gov/study/NCT01216553) | Phase 4 | Unknown | 135 | Home oxygen in bronchiolitis, with nebulized 0.1% epinephrine as one standard nebulized therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Epinephrine for bronchiolitis, examining whether bronchodilators help despite uncertain effectiveness |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Systematic Review (Cochrane, earlier version) | Cochrane Database Syst Rev | Earlier version of the epinephrine-for-bronchiolitis review |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | Reviews racemic epinephrine, systemic corticosteroids, hypertonic saline and high-flow oxygen in infant bronchiolitis |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | Pediatr Clin North Am | Nebulized adrenaline gives temporary symptomatic benefit in croup; bronchiolitis evidence limited by unclear diagnostic definition |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clin Evid | Overview of bronchiolitis, the most common lower respiratory infection in infants |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clin Evid | Earlier overview of bronchiolitis |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Not classified | Clin Pharmacol Ther | Bronchodilator effects of terbutaline and epinephrine in obstructive lung disease (no abstract supplied) |
| [4551435](https://pubmed.ncbi.nlm.nih.gov/4551435/) | 1972 | Not classified | Ann Allergy | Nebulized bronchodilators in obstructive lung disease (no abstract supplied) |
| [6107058](https://pubmed.ncbi.nlm.nih.gov/6107058/) | 1980 | Review | Anaesth Intensive Care | Sympathomimetic amines; choice of agent should follow data from relevant clinical settings |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | News/Commentary | Med Lett Drugs Ther | Return of the OTC epinephrine inhaler (Primatene Mist) |

---

## US Market Information

The Evidence Pack shows 20 licenses and lists 5 of them. None of the listed entries include approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 214697 | neffy | Spray | Not listed in source data |
| NDA 205029 | Epinephrine | Injection, solution, concentrate | Not listed in source data |
| NDA 020800 | epinephrine | Injection | Not listed in source data |
| NDA 205029 | Epinephrine | Injection, solution, concentrate | Not listed in source data |
| NDA 209359 | EPINEPHRINE | Injection, solution | Not listed in source data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and well established, and completed Phase 3 studies of epinephrine products exist in pediatric asthma and bronchiolitis. However, no results were supplied, the bronchiolitis evidence is mixed, and the original indication and package insert safety data are missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, downloaded and parsed from the FDA website
- The approved indications for each US product, to separate true repurposing from existing labeled use
- Detailed mechanism of action data from DrugBank
- Outcome data from the completed Phase 3 studies (NCT01460511, NCT01737905, NCT00116584)
- A review of the Cochrane conclusions on epinephrine for bronchiolitis against the specific obstructive lung disease target

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

