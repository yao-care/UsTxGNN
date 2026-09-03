---
layout: default
title: Nitroglycerin
parent: 僅模型預測 (L5)
nav_order: 973
evidence_level: L5
indication_count: 5
---

# Nitroglycerin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Nitroglycerin: From Angina Pectoris to Pulmonary Hypertension

## One-Sentence Summary

> Nitroglycerin is a classic nitrate vasodilator historically used for angina pectoris and acute cardiovascular vasospastic conditions.
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**,
> with **13 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris / acute vasodilator therapy (regulatory license text not available in this evidence pack) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data for nitroglycerin is not available in this evidence pack. Based on the mechanistic rationale generated alongside this prediction, nitroglycerin is metabolized within vascular smooth muscle cells to release nitric oxide (NO), which activates guanylate cyclase and raises intracellular cGMP, producing smooth muscle relaxation. In the pulmonary vascular bed, this pathway can trigger selective pulmonary vasodilation — the same NO/cGMP axis exploited by established pulmonary hypertension therapies such as inhaled nitric oxide (iNO) and PDE5 inhibitors (e.g., sildenafil).

Nitroglycerin's well-established original use as a systemic vasodilator in angina pectoris and acute coronary vasospasm shares direct mechanistic overlap with pulmonary vasodilation: both indications rely on nitrate-induced smooth muscle relaxation to relieve vascular resistance and improve perfusion. This shared pathway is why nitroglycerin has already been used off-label in acute settings — as a vasoreactivity testing agent in pulmonary arterial hypertension, and as a nebulized adjunct in persistent pulmonary hypertension of the newborn (PPHN) — providing real-world clinical precedent that reinforces the plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01120964](https://clinicaltrials.gov/study/NCT01120964) | Phase 1/2 | Completed | 22 | RCT of IV L-citrulline (NO precursor pathway) vs placebo in children with pulmonary hypertension after cardiopulmonary bypass |
| [NCT07214129](https://clinicaltrials.gov/study/NCT07214129) | N/A | Completed | 20 | Nebulized nitroglycerin evaluated directly as a vaso-reactivity testing agent in pulmonary arterial hypertension |
| [NCT05741229](https://clinicaltrials.gov/study/NCT05741229) | N/A | Completed | 80 | Nebulized nitroglycerin as adjuvant therapy for persistent pulmonary hypertension of the newborn (PPHN); echocardiographic and clinical endpoints |
| [NCT04594629](https://clinicaltrials.gov/study/NCT04594629) | Phase 1 | Unknown | 120 | Nebulized nitroglycerin vs nebulized PGI2 (epoprostenol) for pulmonary hypertension after valve replacement surgery |
| [NCT00449059](https://clinicaltrials.gov/study/NCT00449059) | Phase 4 | Completed | 20 | Acute IV nitroglycerin infusion effect on cyclosporine-induced hypertension after cardiac transplantation |
| [NCT03259165](https://clinicaltrials.gov/study/NCT03259165) | Phase 2 | Terminated | 52 | Nitroglycerin vs furosemide, lung ultrasound-guided pilot trial in acute heart failure/pulmonary congestion |
| [NCT06107465](https://clinicaltrials.gov/study/NCT06107465) | Phase 2/3 | Unknown | 60 | High- vs low-dose nitroglycerin in sympathetic crashing acute pulmonary edema |
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular endothelial function and vasomotor tone study in hypertension (indirect relevance) |
| [NCT05172739](https://clinicaltrials.gov/study/NCT05172739) | Phase 4 | Recruiting | 70 | Perioperative opioid-free anesthesia strategy in lung cancer surgery (nitroglycerin not primary intervention) |
| [NCT05373108](https://clinicaltrials.gov/study/NCT05373108) | Phase 4 | Completed | 19 | Endothelin-1 and vasomotor function in cardiac allograft vasculopathy after heart transplant |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40888971](https://pubmed.ncbi.nlm.nih.gov/40888971/) | 2025 | RCT | European Journal of Pediatrics | RCT (n=80) showing nebulized nitroglycerin improves echocardiographic/clinical parameters in persistent pulmonary hypertension of the newborn |
| [29880427](https://pubmed.ncbi.nlm.nih.gov/29880427/) | 2018 | RCT (Cohort) | J Cardiothorac Vasc Anesth | Randomized study: dobutamine + nitroglycerin vs milrinone for perioperative pulmonary hypertension in mitral valve surgery |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Clinical study | Bull Eur Physiopathol Respir | Sublingual nitroglycerin reduced pulmonary arterial pressure and pulmonary vascular resistance in COPD-related pulmonary hypertension |
| [34082850](https://pubmed.ncbi.nlm.nih.gov/34082850/) | 2021 | Cohort/Case series | Cardiology in the Young | Review/case series on nitroglycerin inhalation for acute pulmonary arterial hypertension in children with congenital heart disease |
| [6407380](https://pubmed.ncbi.nlm.nih.gov/6407380/) | 1983 | Clinical study | Annals of Internal Medicine | Nitroglycerin increased cardiac index, decreased pulmonary vascular resistance and mean pulmonary artery pressure in 9 patients with chronic pulmonary hypertension |
| [15947535](https://pubmed.ncbi.nlm.nih.gov/15947535/) | 2005 | Retrospective study | Congestive Heart Failure | Acute hemodynamic effects of IV nitroglycerin vs epoprostenol in pulmonary arterial hypertension (n=59) |
| [14508317](https://pubmed.ncbi.nlm.nih.gov/14508317/) | 2003 | Clinical study | Anesthesiology | Nitroglycerin inhalation improved postoperative hemodynamics in pulmonary hypertension patients undergoing mitral valve replacement |
| [10214095](https://pubmed.ncbi.nlm.nih.gov/10214095/) | 1999 | Case series | West Virginia Medical Journal | Nebulized nitroglycerin treated pulmonary hypertension in children with congenital heart disease |
| [3096761](https://pubmed.ncbi.nlm.nih.gov/3096761/) | 1986 | Clinical study | Eur J Respir Dis Suppl | Transdermal nitroglycerin patches produced sustained reduction in pulmonary artery pressure and vascular resistance over 4 weeks |
| [29096811](https://pubmed.ncbi.nlm.nih.gov/29096811/) | 2017 | Review | J Am Coll Cardiol | Comprehensive review of nitroglycerin/nitrogen oxide pharmacology and vasodilatory mechanism relevant to pulmonary and systemic circulation |

---

## US Market Information

Nitroglycerin is not currently marketed under the jurisdiction covered by this evidence pack (market status: Not Marketed, 0 licenses on file). No authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L2 is supported by a 2025 RCT in neonatal PPHN, several controlled/randomized perioperative studies, and decades of consistent hemodynamic data showing nitroglycerin reduces pulmonary artery pressure and pulmonary vascular resistance. However, most supportive studies are small, single-center, or focused on acute/perioperative settings rather than chronic pulmonary arterial hypertension, so confirmatory large-scale Phase 3 trials are still lacking.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (currently a **Blocking** data gap — required before any safety pre-assessment)
- Structured mechanism of action (MOA) data from DrugBank (High-priority gap)
- Drug-drug interaction (DDI) profile — current query returned no results
- A dedicated safety monitoring plan for hemodynamic effects (hypotension, reflex tachycardia, nitrate tolerance) if pulmonary hypertension use is pursued
- Consideration of confirmatory controlled trials specifically in chronic pulmonary arterial hypertension populations

*Note: Prinzmetal angina (rank 3, L2, Proceed with Guardrails) shows comparably strong mechanistic and historical clinical evidence and may warrant a parallel evaluation. Kyphoscoliotic heart disease, primary hereditary glaucoma, and congenital hypotrichosis milia (all L5, Hold) currently lack supporting clinical or literature evidence and are not recommended for further investment at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

