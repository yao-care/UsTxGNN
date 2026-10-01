---
layout: default
title: Norepinephrine
parent: Model Prediction Only (L5)
nav_order: 976
evidence_level: L5
indication_count: 3
---

# Norepinephrine
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

# Norepinephrine: From Original Indication (Not Recorded) to Obstructive Lung Disease

## One-Sentence Summary

Norepinephrine is the main sympathetic neurotransmitter, and its original approved indication is not recorded in the available data.
The TxGNN model predicts it may be relevant to **obstructive lung disease**, but **none of the 16 retrieved clinical trials and 20 publications tests norepinephrine as a treatment for this condition**.
The evidence supports biological plausibility only, so this is a model-driven hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the US license records) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (mechanism and physiology studies only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 records (license numbers not available) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Norepinephrine is the main sympathetic neurotransmitter. Systemic norepinephrine acts mainly on alpha-adrenergic receptors and causes vasoconstriction.

The literature supports a biological link between adrenergic signalling and the airways:
- Autonomic nerves influence airway calibre, airway blood vessels and mucous glands.
- Noradrenergic input modulates airway smooth muscle tone and airway vasculature.
- A 2024 mouse study identified brainstem Dbh+ (noradrenergic) neurons as controlling allergen-induced airway hyperreactivity.
- Small studies in COPD patients found raised plasma noradrenaline, related to hypoxaemia and haemodynamics.

These findings show that the noradrenergic system is involved in obstructive lung disease. They do **not** show that giving norepinephrine improves outcomes. Norepinephrine has no established bronchodilator role, and its vasoconstrictive action would not obviously benefit these patients. The very high TxGNN score is a knowledge-graph prediction and is not clinical evidence.

## Clinical Trial Evidence

The table lists the 10 most relevant of the 16 retrieved trials. All were graded C or left ungraded. None tests norepinephrine for obstructive lung disease.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02360865](https://clinicaltrials.gov/study/NCT02360865) | N/A | Completed | 18 | Mechanisms of exercise intolerance in COPD, including endothelial function and muscle sympathetic nerve activity. Norepinephrine is not the tested therapy. |
| [NCT01536587](https://clinicaltrials.gov/study/NCT01536587) | Phase 4 | Completed | 32 | Salmeterol in COPD, testing whether it reduces sympathetic activity (microneurography). Tests a bronchodilator, not norepinephrine. |
| [NCT01219738](https://clinicaltrials.gov/study/NCT01219738) | N/A | Completed | 20 | Inhaled budesonide and adrenergic agonist effects on airway vascular smooth muscle. Tests a corticosteroid. |
| [NCT02564406](https://clinicaltrials.gov/study/NCT02564406) | N/A | Completed | 35 | Extracorporeal CO2 removal in hypercapnic patients (COPD exacerbation) who failed non-invasive ventilation. Device study. |
| [NCT07332442](https://clinicaltrials.gov/study/NCT07332442) | Phase 3 | Not yet recruiting | 250 | CPAP and arousal threshold in obstructive sleep apnea. This is upper-airway obstruction, not obstructive lung disease. |
| [NCT05664204](https://clinicaltrials.gov/study/NCT05664204) | N/A | Recruiting | 200 | Systematic vs on-demand VA-ECMO during lung transplant. Norepinephrine is not the intervention. |
| [NCT02627378](https://clinicaltrials.gov/study/NCT02627378) | Phase 1 | Completed | 35 | ECMO for MERS-induced respiratory failure. Different disease and intervention. |
| [NCT05655065](https://clinicaltrials.gov/study/NCT05655065) | N/A | Recruiting | 30 | Effect of higher mean arterial pressure on renal function in shock. Not a lung disease study. |
| [NCT04280497](https://clinicaltrials.gov/study/NCT04280497) | N/A | Recruiting | 1800 | Hydrocortisone plus fludrocortisone in sepsis. No norepinephrine-specific arm for lung disease can be confirmed. |
| [NCT07022210](https://clinicaltrials.gov/study/NCT07022210) | N/A | Recruiting | 100 | Incidence of hypotension in the post-anesthesia care unit. Not a lung disease study. |

## Literature Evidence

The table lists 10 of the 20 retrieved publications. There are no RCTs. The evidence is preclinical, physiological, observational or review-level.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38987587](https://pubmed.ncbi.nlm.nih.gov/38987587/) | 2024 | Preclinical | Nature | Brainstem Dbh+ neurons control allergen-induced airway hyperreactivity in mice (lung-to-brainstem-to-lung circuit). |
| [2048831](https://pubmed.ncbi.nlm.nih.gov/2048831/) | 1991 | Review | Am Rev Respir Dis | Autonomic nerves (cholinergic, noradrenergic, peptidergic) influence airway calibre in asthma and COPD. |
| [1617386](https://pubmed.ncbi.nlm.nih.gov/1617386/) | 1992 | Review | Br Med Bull | Sympathetic nerves constrict the tracheobronchial vasculature via noradrenaline and neuropeptide Y. |
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Review | Pneumologie | Airway innervation in asthma and COPD, including noradrenergic fibres. |
| [9009625](https://pubmed.ncbi.nlm.nih.gov/9009625/) | 1996 | Cohort | Monaldi Arch Chest Dis | Plasma hormones, including adrenaline and noradrenaline, and haemodynamics in early COPD. |
| [35870527](https://pubmed.ncbi.nlm.nih.gov/35870527/) | 2022 | Cohort | Environ Pollut | Air pollution and neuroendocrine stress hormones in COPD and non-COPD participants (Beijing panel study). |
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | Physiology study | Am J Physiol Heart Circ Physiol | Muscle α-adrenergic responsiveness during exercise in COPD, using tyramine to evoke endogenous norepinephrine release. |
| [11099681](https://pubmed.ncbi.nlm.nih.gov/11099681/) | 2000 | Observational | Am J Med | Hypoxaemia, hypercapnia and hormones, including norepinephrine, in blood pressure regulation during COPD respiratory failure. |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Observational | Scand J Clin Lab Invest | Plasma noradrenaline was raised in nine patients with chronic obstructive lung disease and related to blood gases. |
| [3420304](https://pubmed.ncbi.nlm.nih.gov/3420304/) | 1988 | Clinical study | Respiration | Haemodynamic effects of dopamine and L-dopa in pulmonary hypertension secondary to chronic obstructive lung disease. Tests a related catecholamine, not norepinephrine. |

## US Market Information

The three listed records are norepinephrine liquid products from non-pharmaceutical manufacturers. No license numbers or approved indication text are available in the data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Norepinephrine (BioActive Nutritional, Inc.) | Liquid | Not available |
| Not available | Norepinephrine (BioActive Nutritional, Inc.) | Liquid | Not available |
| Not available | Norepinephrine (Professional Complementary Health Formulas) | Liquid | Not available |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a very high model score and on biological plausibility. No trial has tested norepinephrine for obstructive lung disease, and the literature contains no interventional evidence of benefit. Norepinephrine's vasoconstrictive profile also gives no clear reason to expect a therapeutic effect in this condition. The other two predicted indications are weaker still. Respiratory malformation is Level L5, with only tangential mechanistic and pregnancy-exposure literature. Rienhoff syndrome is Level L5, with no trials or literature at all. Both are also on Hold.

**To proceed, the following is needed:**
- Original indications and approved-indication text (US license data is currently blank).
- Mechanism of action data (DrugBank).
- Package insert warnings and contraindications, which block safety screening.
- Any clinical or preclinical study that actually administers norepinephrine in an obstructive lung disease model or population.
- Confirmation that the listed liquid products are the same pharmaceutical-grade compound as the intravenous vasopressor.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

