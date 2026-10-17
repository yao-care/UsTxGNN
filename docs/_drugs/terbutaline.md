---
layout: default
title: Terbutaline
parent: High Evidence (L1-L2)
nav_order: 1212
evidence_level: L1
indication_count: 3
monitor_inn: "TERBUTALINE"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome"]
last_modified_at: 2026-10-14
description: "Terbutaline: predicted new indication Obstructive lung disease (evidence level L1). Approved use: Asthma (also intrinsic and allergic asthma, bronchitis…"
---

# Terbutaline
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Terbutaline: From Asthma to Obstructive Lung Disease

## One-Sentence Summary

Terbutaline is a selective beta-2 adrenergic agonist bronchodilator, originally used for asthma, bronchitis, and emphysema.
The TxGNN model predicts it may be effective for **obstructive lung disease**, with **15 clinical trials** and **20 publications** compiled for this direction. This is largely an on-label or near-label indication, not a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (also intrinsic and allergic asthma, bronchitis, pulmonary emphysema) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 6 (all cancelled) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, terbutaline is a selective beta-2 adrenergic agonist. It relaxes bronchial smooth muscle and produces bronchodilation.

Asthma, bronchitis, and emphysema are all forms of obstructive lung disease. The predicted indication therefore overlaps almost completely with the original ones, and the same bronchodilator mechanism applies. This explains the very high TxGNN score.

The other two predictions are much weaker. "Respiratory malformation" (score 99.52%) has no literature showing that terbutaline works. Beta-2 agonism could at most relieve secondary bronchospasm, and the score likely reflects network proximity to airway disease. "Rienhoff syndrome" (score 99.38%) has no trial or literature evidence and no plausible mechanistic link. Both are rated Hold.

---

## Clinical Trial Evidence

Terbutaline mostly appears as a reliever or comparator arm in these trials, rather than as the primary test article. Of the 15 trials compiled, the 10 most relevant are listed below. Trials not listed include a withdrawn Phase 2/3 study with 0 enrolled (NCT04973345), a Phase 4 omalizumab add-on study with only an unclear terbutaline role (NCT00567476), a Phase 4 terbutaline blood and urine concentration study (NCT00914797), a Phase 3 Symbicort COPD study in Chinese patients (NCT00421122), and a Phase 3 Symbicort tolerability study in Japanese asthma patients (NCT00837967).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Completed | 4215 | Symbicort as needed vs. Pulmicort twice daily plus as-needed terbutaline in asthma |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Completed | 3850 | Symbicort as needed vs. as-needed terbutaline vs. Pulmicort plus terbutaline in asthma |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Completed | 120 | IV magnesium sulfate vs. terbutaline in children with acute asthma exacerbation |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Completed | 2091 | Symbicort SMART vs. Symbicort plus as-needed terbutaline 0.4 mg in asthma |
| [NCT00259766](https://clinicaltrials.gov/study/NCT00259766) | Phase 3 | Completed | 1970 | Real-life health-care cost comparison of Symbicort regimens vs. a free combination with Bricanyl (terbutaline) as needed |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Phase 3 | Completed | 1600 | Symbicort single inhaler therapy vs. conventional best practice in persistent asthma (indirect for terbutaline) |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Completed | 860 | As-needed budesonide/formoterol vs. regular budesonide/formoterol plus as-needed terbutaline |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Completed | 95 | Bricanyl Turbuhaler M3 vs. M2 on methacholine-induced bronchoconstriction in mild to moderate asthma |
| [NCT00244608](https://clinicaltrials.gov/study/NCT00244608) | Phase 3 | Completed | 100 | Inflammatory control with flexible-dose Symbicort vs. higher fixed dose plus terbutaline as needed |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Completed | 24 | Terbutaline Turbuhaler 0.4 mg vs. salbutamol pMDI 200 μg in Japanese adult asthma patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | RCT | N Engl J Med | As-needed budesonide-formoterol as an alternative to conventional treatment in mild asthma |
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | RCT | Acad Emerg Med | Nebulized terbutaline plus ipratropium vs. terbutaline alone in acute COPD exacerbation requiring noninvasive ventilation |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | Br J Dis Chest | Oral terbutaline increased diaphragmatic contraction force vs. placebo in COPD (10 patients) |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | Int J Clin Pharmacol Ther Toxicol | Oral clenbuterol vs. terbutaline bronchodilator effects in chronic obstructive lung disease |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | RCT (crossover) | Lung | Single-dose terbutaline Turbuhaler on lung function and exercise capacity in COPD (26 patients) |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Review | Am J Respir Crit Care Med | Beta-2 agonists, including terbutaline, provide rapid symptom relief in lung disease |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | Systematic Review | Naunyn Schmiedebergs Arch Pharmacol | Pharmacokinetics of terbutaline in humans; used for bronchospasm in asthma, bronchitis, emphysema, and COPD |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline | Basic Clin Pharmacol Toxicol | Finnish guideline for diagnosis and pharmacotherapy of stable COPD |
| [2951811](https://pubmed.ncbi.nlm.nih.gov/2951811/) | 1986 | Clinical study | Respiration | Fenoterol-ipratropium combination vs. inhaled terbutaline in COPD (20 patients) |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Clinical study | Ann Palliat Med | N-acetylcysteine plus terbutaline sulfate in elderly COPD patients |

---

## US Market Information

All six US authorizations are cancelled, and none is currently valid. The approved indication text is not available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017849 | Terbutaline Sulfate (ANI Pharmaceuticals) | Tablet | Not available |
| ANDA075877 | Terbutaline Sulfate (Amneal) | Tablet | Not available |
| ANDA211832 | Terbutaline Sulfate (Upsher-Smith) | Tablet | Not available |
| ANDA077152 | Terbutaline Sulfate (Chartwell RX) | Tablet | Not available |
| ANDA078630 | Terbutaline Sulfate (Henry Schein) | Injection | Not available |

A sixth authorization, ANDA076887 (Fresenius Kabi, injection solution), is also cancelled.

---

## Safety Considerations

**Contraindication-related diseases (from the knowledge graph, not label text):**
hypertension, epilepsy, hyperglycemia, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, sudden cardiac arrest, heart conduction disease, respiratory failure, hyperthyroidism (including Graves disease and thyrotoxicosis), pulmonary edema, myocardial ischemia, coronary artery disease, and placental abruption.

**Drug Interactions:** 100 interactions were found. Examples include:
- **Moderate:** epinephrine, isometheptene, famotidine, clarithromycin, loperamide, bisacodyl, and several antidiabetic drugs (acarbose, alogliptin, pioglitazone, canagliflozin, chlorpropamide, albiglutide)
- **Minor:** corticosteroids (hydrocortisone, dexamethasone, triamcinolone, budesonide, betamethasone, beclomethasone)

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple large, completed Phase 3 trials in asthma include terbutaline as an active reliever or comparator, and the predicted indication overlaps almost entirely with the existing ones. Still, most trials do not test terbutaline as the primary agent. All US authorizations are also cancelled, which limits near-term development.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Clarification of the reasons for the US license cancellations and the availability of any current marketed products
- Cardiovascular, metabolic, and potassium monitoring plans, given the contraindication-related diseases above
- Evidence where terbutaline is the primary test agent in COPD, since current COPD data are mostly older, small studies

**Other predictions:** Respiratory malformation and Rienhoff syndrome are both rated **Hold**, because there is no supporting efficacy evidence or plausible mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

