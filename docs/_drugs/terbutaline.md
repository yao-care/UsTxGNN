---
layout: default
title: Terbutaline
parent: Model Prediction Only (L5)
nav_order: 1212
evidence_level: L5
indication_count: 3
---

# Terbutaline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Terbutaline: From Bronchodilator Use to Obstructive Lung Disease

## One-Sentence Summary

Terbutaline is a selective beta-2 agonist bronchodilator, marketed in the US as injection and tablets. The TxGNN model predicts it may be effective for **obstructive lung disease** (asthma and COPD). The prediction is backed by **48 clinical trials** and **20 publications**, but most of the trials use terbutaline as a reliever or comparator. This is probably an already-labeled use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided US license records (bronchospasm in asthma/COPD is likely, but must be checked against the label) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 (capped, because Phase 3 trials mostly use terbutaline as a comparator or reliever) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 (all listed licenses are ANDAs) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism data is not available in the source record. Terbutaline is a known selective beta-2 adrenergic agonist. It activates the beta-2 receptor, Gs protein, adenylyl cyclase and cAMP pathway, which relaxes bronchial smooth muscle. The result is bronchodilation and relief of airflow obstruction.

This matches the core pathophysiology of obstructive lung disease (asthma and COPD), so the mechanistic link is direct. The high TxGNN score likely reflects this close match.

Bronchospasm in asthma and COPD is very likely already a labeled use of terbutaline. The prediction therefore mostly confirms known pharmacology rather than identifying a new indication. The US license records contain no indication text, so this needs to be verified against the package insert.

---

## Clinical Trial Evidence

48 trials were retrieved. The 10 most relevant are listed below. Many are budesonide/formoterol (Symbicort) studies in which terbutaline is the reliever or comparator, so they give indirect evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Completed | 120 | IV magnesium sulfate vs terbutaline in children with acute asthma exacerbation (direct comparison) |
| [NCT01944033](https://clinicaltrials.gov/study/NCT01944033) | Phase 3 | Completed | 250 | Nebulized beta-2 agonist alone vs beta-2 agonist plus ipratropium in COPD exacerbation (the specific agent is not confirmed) |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Completed | 24 | Terbutaline Turbuhaler 0.4 mg vs salbutamol pMDI in Japanese adults with asthma (crossover) |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Completed | 3850 | Symbicort as-needed vs terbutaline as-needed vs budesonide plus terbutaline in mild asthma |
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Completed | 4215 | Symbicort as-needed vs budesonide twice daily plus terbutaline as-needed |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Completed | 2091 | Symbicort SMART vs Symbicort plus terbutaline as-needed over 12 months |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Completed | 860 | As-needed budesonide/formoterol vs regular budesonide/formoterol plus as-needed terbutaline |
| [NCT00326053](https://clinicaltrials.gov/study/NCT00326053) | Phase 3 | Completed | 600 | Symbicort vs budesonide plus terbutaline reliever for preventing asthma relapse after ER discharge |
| [NCT00837967](https://clinicaltrials.gov/study/NCT00837967) | Phase 3 | Completed | 25 | Tolerability of 10 inhalations of Symbicort vs terbutaline on top of Symbicort in Japanese adults with asthma |
| [NCT00750568](https://clinicaltrials.gov/study/NCT00750568) | N/A | Unknown | 36 | PK/PD of continuous IV terbutaline in children with severe status asthmaticus |

---

## Literature Evidence

20 publications were retrieved. The 10 most relevant, prioritizing randomized trials, are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | RCT | Acad Emerg Med | Nebulized terbutaline plus ipratropium vs terbutaline alone in acute COPD exacerbation needing noninvasive ventilation |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | Br J Dis Chest | Oral terbutaline vs placebo in COPD: increased inspiratory mouth pressure and transdiaphragmatic pressure |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | Int J Clin Pharmacol Ther Toxicol | Oral terbutaline vs clenbuterol in chronic obstructive lung disease over two weeks |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | RCT | Respir Med | Inhaled terbutaline vs placebo on FEV1, FVC, dyspnoea and walking distance in COPD |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | RCT | Lung | Single-dose terbutaline vs placebo on lung function and exercise capacity in 26 COPD patients |
| [3044105](https://pubmed.ncbi.nlm.nih.gov/3044105/) | 1988 | RCT | Am J Med Sci | Oral terbutaline improved cardiac performance in COPD (crossover) |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Clinical study | Ann Palliat Med | N-acetylcysteine plus terbutaline in elderly COPD patients, with effects on apoptosis mechanisms |
| [18761816](https://pubmed.ncbi.nlm.nih.gov/18761816/) | 2008 | Clinical study | Cell Mol Immunol | Nebulized terbutaline plus budesonide improved immunity and lung function in AECOPD |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | Controlled study | Chest | Interaction of oral terbutaline with beta-blockers in COPD patients with heart disease or hypertension |
| [2031046](https://pubmed.ncbi.nlm.nih.gov/2031046/) | 1991 | Clinical trial | Pneumologie | Nebulized terbutaline with and without positive expiratory pressure in COPD (crossover) |

---

## US Market Information

17 licenses are on record. The 5 main ones are listed below. The records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA078630 | Terbutaline Sulfate | Injection | Henry Schein, Inc. |
| ANDA078630 | Terbutaline Sulfate | Injection | Hikma Pharmaceuticals USA Inc. |
| ANDA075877 | Terbutaline Sulfate | Tablet | Amneal Pharmaceuticals of New York LLC |
| ANDA078630 | Terbutaline Sulfate | Injection | Medical Purchasing Solutions, LLC |
| ANDA211832 | Terbutaline Sulfate | Tablet | Upsher-Smith Laboratories, LLC |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism directly fits obstructive lung disease, and there are many Phase 3 trials plus decades of randomized studies in COPD and asthma. However, terbutaline is mostly the comparator or reliever in those trials, and this looks like an existing labeled use rather than a new indication.

The same run also produced two lower-ranked predictions, which should stay on hold:
- **Respiratory malformation (Hold):** it is supported only by indirect evidence, and bronchodilation cannot correct structural defects.
- **Rienhoff syndrome (Hold):** no trials or literature were found, and the TxGNN score is a knowledge-graph prediction only.

**To proceed, the following is needed:**
- Retrieve the package insert to confirm the labeled indications and to obtain warnings and contraindications. This is a blocking safety gap.
- Confirm whether obstructive lung disease is already a labeled use. If it is, reclassify the case as an existing indication rather than repurposing.
- Check full titles and arms of the Phase 3 trials to confirm terbutaline's role (comparator, reliever or investigational).
- Obtain detailed mechanism-of-action data from DrugBank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

