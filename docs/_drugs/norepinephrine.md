---
layout: default
title: Norepinephrine
parent: 僅模型預測 (L5)
nav_order: 976
evidence_level: L5
indication_count: 3
---

# Norepinephrine
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

# Norepinephrine: From Unspecified Original Indication to Obstructive Lung Disease

## One-Sentence Summary

The original indication and mechanism of action for norepinephrine are not documented in this evidence pack (data gap). The TxGNN model predicts a possible association with **Obstructive Lung Disease**, but this is currently supported only by indirect, mechanism-level evidence — **0 clinical trials directly test norepinephrine as a treatment for this condition**, and the supporting literature largely describes catecholamine physiology in COPD/asthma rather than therapeutic efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (mechanism/observational only) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for norepinephrine is not available in this evidence pack. Based on general pharmacological knowledge reflected in the supporting literature, norepinephrine is an endogenous catecholamine that acts as an agonist at α/β-adrenergic receptors, and sympathetic/noradrenergic tone is known to modulate airway smooth muscle and vascular caliber (e.g., PMID 2048831, PMID 21271508).

However, the repurposing rationale explicitly flags this as an **indirect, physiological association rather than a therapeutic hypothesis**. Norepinephrine is clinically used as a systemic vasopressor for shock and hypotension, not as an inhaled or targeted airway therapy. The clinical trials returned for this candidate mostly involve norepinephrine incidentally, as a standard-of-care vasopressor in ECMO, perioperative, or ICU contexts — not as an intervention being tested for obstructive lung disease. The literature evidence instead describes elevated plasma noradrenaline levels and autonomic dysregulation as **features of** COPD/asthma pathophysiology, which is a correlative finding, not evidence of therapeutic benefit.

Given this, the high TxGNN score likely reflects strong knowledge-graph connectivity between norepinephrine and respiratory-disease nodes (due to extensive co-occurrence in critical-care and physiology literature) rather than a validated treatment signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01219738](https://clinicaltrials.gov/study/NCT01219738) | N/A | Completed | 20 | Acute airway vascular smooth muscle response to inhaled budesonide; discusses non-genomic enhancement of endogenous norepinephrine effects at adrenergic receptors — mechanistic relevance, not a norepinephrine intervention trial |
| [NCT02360865](https://clinicaltrials.gov/study/NCT02360865) | N/A | Completed | 18 | Mechanisms of exercise intolerance in COPD; explores endothelial function and possible sympathetic/catecholamine involvement |
| [NCT05664204](https://clinicaltrials.gov/study/NCT05664204) | N/A | Recruiting | 200 | Intraoperative ECMO strategy in lung transplantation; norepinephrine used only as routine vasopressor support |
| [NCT07022210](https://clinicaltrials.gov/study/NCT07022210) | N/A | Recruiting | 100 | Incidence of post-anesthesia hypotension; no direct link to obstructive lung disease |
| [NCT07332442](https://clinicaltrials.gov/study/NCT07332442) | Phase 3 | Not yet recruiting | 250 | CPAP and arousal threshold in obstructive sleep apnea; norepinephrine not an intervention |
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular function/exercise rehabilitation in hypertension; not a lung-disease treatment study |
| [NCT02627378](https://clinicaltrials.gov/study/NCT02627378) | Phase 1 | Completed | 35 | ECMO support for MERS-induced respiratory failure; norepinephrine used only as standard vasopressor |
| [NCT06361420](https://clinicaltrials.gov/study/NCT06361420) | N/A | Recruiting | 43 | Lung-protective ventilation strategy in aortic dissection surgery; unrelated to obstructive lung disease treatment |
| [NCT02564406](https://clinicaltrials.gov/study/NCT02564406) | N/A | Completed | 35 | Extracorporeal CO2 removal in hypercapnic COPD exacerbation patients who refused intubation; non-pharmacological intervention |
| [NCT04280497](https://clinicaltrials.gov/study/NCT04280497) | N/A | Recruiting | 1800 | RCT on corticosteroid therapy in sepsis; norepinephrine mentioned only as a vasopressor endpoint component |

**Note:** None of the above trials test norepinephrine as a treatment for obstructive lung disease; relevance grading (mostly "C", two "B") reflects incidental/mechanistic association only.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9009625](https://pubmed.ncbi.nlm.nih.gov/9009625/) | 1996 | Cohort | Monaldi Arch Chest Dis | Elevated plasma noradrenaline and altered hemodynamic hormone levels in COPD patients |
| [2048831](https://pubmed.ncbi.nlm.nih.gov/2048831/) | 1991 | Review | Am Rev Respir Dis | Autonomic (noradrenergic/cholinergic) control of airway caliber in asthma and COPD |
| [1617386](https://pubmed.ncbi.nlm.nih.gov/1617386/) | 1992 | Review | Br Med Bull | Sympathetic (noradrenaline) constriction of tracheobronchial vasculature in asthma |
| [35870527](https://pubmed.ncbi.nlm.nih.gov/35870527/) | 2022 | Cohort | Environ Pollut | Air-pollution-associated neuroendocrine (SAM axis) stress hormone changes in COPD vs. non-COPD panel |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Unclassified | Scand J Clin Lab Invest | Increased plasma noradrenaline in COPD, correlated with hemodynamics and blood gases |
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Unclassified | Pneumologie | Review of airway innervation (including noradrenergic fibers) in asthma and COPD |
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | Unclassified | Am J Physiol Heart Circ Physiol | α-adrenergic responsiveness and functional sympatholysis during exercise in COPD |
| [11099681](https://pubmed.ncbi.nlm.nih.gov/11099681/) | 2000 | Unclassified | Am J Med | Mechanisms of hypertension in COPD with acute respiratory failure, including norepinephrine's role |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Unclassified | Crit Care Clin | Overview of catecholamines (norepinephrine, epinephrine, dopamine) in critical illness |
| [3420304](https://pubmed.ncbi.nlm.nih.gov/3420304/) | 1988 | Unclassified | Respiration | Hemodynamic effects of dopamine/L-dopa in pulmonary hypertension secondary to COLD |

**Note:** No RCTs were identified; all evidence is observational or mechanistic/review in nature, consistent with the L4 evidence level.

---

## US Market Information

No regulatory license records are available in the evidence pack — `taiwan_regulatory.licenses` is empty and `market_status` is reported as **Not Marketed** (0 NDAs on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for norepinephrine in obstructive lung disease consists entirely of mechanistic and observational studies describing catecholamine physiology in COPD/asthma, not therapeutic trials. No clinical trial directly tests norepinephrine as an intervention for this indication, and the evidence pack's own rationale explicitly characterizes the mechanistic link as correlative co-occurrence rather than causal support. The other two TxGNN-predicted indications (respiratory malformation, Rienhoff syndrome) have even weaker support (L5, no or near-no clinical/literature evidence) and are separately flagged as Hold.

**To proceed, the following is needed:**
- Original indication and mechanism of action (MOA) data for norepinephrine (currently a data gap)
- TFDA/US label warnings and contraindications — flagged as a **Blocking** data gap (DG001); required before any S1 safety pre-assessment
- Confirmed DrugBank-sourced MOA — flagged as **High** severity data gap (DG002)
- A dedicated preclinical or mechanistic study directly testing norepinephrine's effect on airway obstruction (rather than its role as a vasopressor in unrelated critical-care settings)
- Regulatory/marketing status confirmation, since no NDA or license record currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

