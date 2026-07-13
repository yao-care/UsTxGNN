---
layout: default
title: Terlipressin
parent: 僅模型預測 (L5)
nav_order: 635
evidence_level: L5
indication_count: 7
---

# Terlipressin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Terlipressin: From Portal Hypertension to Pulmonary Hypertension

## One-Sentence Summary

Terlipressin is a synthetic vasopressin analogue with established use in portal hypertension complications — including acute variceal hemorrhage and hepatorenal syndrome (HRS) — acting via V1 receptor-mediated splanchnic vasoconstriction to reduce portal venous inflow.
The TxGNN model's highest-ranked prediction is **open-angle glaucoma** (score 99.78%), but this indication has zero supporting evidence and is assessed as a graph-network false positive; the most clinically meaningful prediction is **Pulmonary Hypertension** (rank #3, score 99.56%), supported by **4 clinical trials** and **20 publications** — primarily hemodynamic studies in cirrhosis-associated pulmonary hypertension and neonatal rescue cases.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Portal hypertension (variceal hemorrhage, hepatorenal syndrome) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.56% (Rank #3) |
| Evidence Level | L4 |
| US Market Status | Not Marketed (0 active licenses in evidence pack) |
| Number of NDAs | 0 |
| Recommended Decision | Hold (Research Question) |

## Why is This Prediction Reasonable?

Terlipressin is a triglycyl prodrug of lysine-vasopressin that is enzymatically cleaved in vivo to release active lysine-vasopressin. Its primary pharmacological action is agonism at V1a receptors on vascular smooth muscle, inducing potent splanchnic vasoconstriction. This reduces mesenteric blood flow and portal venous inflow, thereby lowering portal pressure — the basis for its clinical use in variceal bleeding and hepatorenal syndrome. Detailed MOA data was not available in this evidence pack; the above is inferred from the drug's pharmacological class and the clinical literature retrieved.

The link to pulmonary hypertension is most coherent in the context of **portopulmonary hypertension (PoPH)** — a recognized WHO Group 1.4 subtype that develops as a complication of portal hypertension, in which portal-to-pulmonary shunting of vasoactive mediators drives pulmonary vascular remodeling. In this subtype, reducing portal pressure pharmacologically can indirectly alleviate right-heart afterload. Small hemodynamic studies (Kalambokis et al., 2004, 2008, 2012) demonstrated that terlipressin selectively reduces pulmonary vascular resistance (PVR) in cirrhotic patients with elevated PVR, while simultaneously decreasing portal pressure — a dual benefit not seen with conventional vasoconstrictors such as norepinephrine, which can worsen PH.

A distinct body of evidence comes from **neonatal medicine**, where terlipressin has been used as rescue therapy for persistent pulmonary hypertension of the newborn (PPHN) in congenital diaphragmatic hernia and sepsis-related cases. Here the proposed mechanism differs: vasopressin receptor activation may support systemic blood pressure without increasing PVR, thereby maintaining right-to-left pressure gradients. One RCT in adult cardiac surgery patients (Abdelazziz & Abdelhamid, 2019) found terlipressin did not increase mean pulmonary artery pressure (MPAP) when used to counteract milrinone-induced hypotension, unlike norepinephrine. Collectively, this evidence positions terlipressin as a vasopressor with favorable pulmonary hemodynamic properties in specific secondary PH contexts — but it does not support use in primary or idiopathic PAH, where systemic vasoconstriction may be detrimental.

## Clinical Trial Evidence

> All retrieved trials are graded **C relevance** (indirect) — none specifically investigates terlipressin as a treatment for pulmonary hypertension.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03584087](https://clinicaltrials.gov/study/NCT03584087) | Phase 4 | Completed | 74 | Terlipressin vs. standard of care after endoscopic variceal ligation in acute variceal hemorrhage; completed trial providing portal pressure reduction data with systemic hemodynamic readouts |
| [NCT06027970](https://clinicaltrials.gov/study/NCT06027970) | Phase 3 | Unknown | 165 | Continuous terlipressin infusion post-EVL for acute variceal hemorrhage; cardiopulmonary hemodynamic safety data may be extractable as secondary outcome |
| [NCT05315557](https://clinicaltrials.gov/study/NCT05315557) | N/A | Unknown | 100 | Vasopressin vs. terlipressin as second-line vasopressor in cirrhotic patients with septic shock; provides comparative pulmonary safety profiling across both agents in a high-risk population |
| [NCT06256432](https://clinicaltrials.gov/study/NCT06256432) | Phase 2 | Active, not recruiting | 54 | Ambrisentan (ERA approved for PAH) in hepatorenal syndrome — terlipressin used as background therapy; highlights the mechanistic overlap between PoPH and HRS management, with ERA as potential combination partner |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30971593](https://pubmed.ncbi.nlm.nih.gov/30971593/) | 2019 | RCT | Ann Cardiac Anaesthesia | Terlipressin vs. norepinephrine to reverse milrinone-induced hypotension in cardiac surgery patients with pre-existing PH; terlipressin restored systemic BP without increasing PVR or MPAP — unlike norepinephrine |
| [22893473](https://pubmed.ncbi.nlm.nih.gov/22893473/) | 2012 | Hemodynamic observational | Hepatobiliary Pancreatic Dis Int | Single terlipressin dose (2 mg IV) reduced PVR and improved pulmonary hemodynamics in 7 cirrhotic patients with PH presenting with variceal bleeding or HRS; PVR decreased from 186.5 to 158.8 dyne·s·cm⁻⁵ |
| [21733953](https://pubmed.ncbi.nlm.nih.gov/21733953/) | 2012 | Hemodynamic study | Angiology | Terlipressin selectively reduced PVR in cirrhosis patients with elevated PVR (>120 dyne·s·cm⁻⁵) but not in those with normal PVR; supports a differential vasodilatory effect on pulmonary vs. systemic vasculature in PH-subset |
| [18280605](https://pubmed.ncbi.nlm.nih.gov/18280605/) | 2008 | Case report | J Hepatology | Significant reduction in pulmonary arterial pressure after 1-week terlipressin treatment in a cirrhotic patient with moderate-to-severe portopulmonary hypertension; faster onset than prostacyclin analogues or endothelin receptor antagonists |
| [15259082](https://pubmed.ncbi.nlm.nih.gov/15259082/) | 2004 | Observational | World J Gastroenterology | Echocardiographic assessment showing terlipressin reduced systolic pulmonary artery pressure in cirrhotic patients; among the earliest reports linking terlipressin to pulmonary pressure reduction |
| [34179513](https://pubmed.ncbi.nlm.nih.gov/34179513/) | 2021 | Systematic review protocol | BMJ Paediatrics Open | Protocol for systematic review of vasopressin/terlipressin in preterm neonates with hypotension or persistent PH; acknowledges increasing off-label use and calls for formal evidence synthesis |
| [32999121](https://pubmed.ncbi.nlm.nih.gov/32999121/) | 2020 | Case report | Indian Pediatrics | Terlipressin rescue therapy for refractory PPHN and shock in a preterm infant; pulmonary vasodilatory effect achieved where inhaled NO and other therapies failed |
| [21292065](https://pubmed.ncbi.nlm.nih.gov/21292065/) | 2011 | Case report | J Pediatric Surgery | Terlipressin as rescue in neonatal refractory PPHN with congenital diaphragmatic hernia; rationale based on V1 receptor analogy to vasopressin's known pulmonary vasodilatory mechanism |
| [23128058](https://pubmed.ncbi.nlm.nih.gov/23128058/) | 2012 | Case report | J Perinatology | Asphyxiated septic infant with PH and catecholamine-resistant hypotension; terlipressin addition reduced pulmonary artery pressures on echocardiographic reassessment within 10 minutes |
| [19624374](https://pubmed.ncbi.nlm.nih.gov/19624374/) | 2009 | Case series | Paediatric Anaesthesia | Role of terlipressin in severe PH complicating congenital diaphragmatic hernia in neonates; supports a distinct neonatal PPHN use-case as part of rescue vasopressor strategy |

## Safety Considerations

Please refer to the package insert for safety information.

> No structured warning, contraindication, or drug-drug interaction data was available in this evidence pack. Based on the pharmacological class (vasopressin V1 agonist), clinical teams should be alert to: systemic vasoconstriction with risk of peripheral and mesenteric ischemia; bradycardia and cardiac arrhythmia; hyponatremia (ADH-like antidiuretic effect); and potential worsening of pulmonary hypertension in non-portal contexts. Formal safety assessment requires review of the prescribing information.

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The evidence base for terlipressin in pulmonary hypertension is mechanistically plausible but confined to secondary PH in cirrhosis (portopulmonary hypertension) and neonatal rescue cases — there are no prospective trials designed to test terlipressin as a PH-specific therapy, and none of the four retrieved clinical trials targets PH as the primary outcome. The signal is sufficient to formulate a research question, but not to support a development decision. Critically, the TxGNN top-ranked predictions (open-angle glaucoma, primary hereditary glaucoma, kyphoscoliotic heart disease, esotropia) all score L5 with zero supporting evidence and are assessed as graph-network false positives arising from non-specific vascular regulation node co-activation.

**To proceed, the following is needed:**
- Define the target PH subtype: portopulmonary hypertension (PoPH, WHO Group 1.4) is the most mechanistically justified sub-indication and should be scoped separately from idiopathic PAH
- Commission a formal hemodynamic feasibility study in PoPH patients with pulmonary artery catheterization as the primary measurement endpoint
- Retrieve and review full mechanism of action data from DrugBank (DG002 remediation)
- Obtain Taiwan FDA / target-market prescribing information to complete safety pre-screening (DG001 remediation)
- Verify current regulatory status: Terlipressin (Terlivaz®) received US FDA approval in 2022 for HRS-1; this may not be reflected in the evidence pack's 0-license readout and should be confirmed before any US-market development planning
- Assess route-of-administration compatibility for a pulmonary hypertension indication (current IV formulation vs. inhaled/alternative delivery)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

