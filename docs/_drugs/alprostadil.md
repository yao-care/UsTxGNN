---
layout: default
title: Alprostadil
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
---

# Alprostadil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Alprostadil: From Ductus-Dependent Congenital Heart Disease to Aortic Malformation

## One-Sentence Summary

Alprostadil (Prostaglandin E1, PGE1) is a synthetic prostanoid clinically established as the preoperative bridge therapy for neonates with ductus-dependent congenital heart disease, maintaining patency of the ductus arteriosus (PDA) to preserve systemic or pulmonary perfusion until surgical correction.
The TxGNN model predicts it may be effective for **Aortic Malformation**,
with **2 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan (TFDA: 0 licenses); established clinical use: PDA maintenance in ductus-dependent congenital heart disease |
| Predicted New Indication | Aortic Malformation |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Market Status | Not marketed (Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Alprostadil is the synthetic form of prostaglandin E1 (PGE1), acting primarily through EP4 receptors on the smooth muscle of the ductus arteriosus to drive vasodilation and prevent spontaneous ductal closure. Since its clinical introduction in the late 1970s, PGE1 infusion has become the undisputed standard of care for preoperative stabilization of neonates with ductus-dependent cardiac lesions — effectively maintaining circulation until definitive surgical repair can be undertaken.

Aortic malformations — including interrupted aortic arch, aortic coarctation, aortic atresia, and critical aortic stenosis — represent the quintessential category of ductus-dependent *systemic* circulation disorders. In these conditions, perfusion of the descending aorta and lower body depends entirely or substantially on right-to-left flow through the PDA. Without an open ductus, neonates rapidly deteriorate into cardiogenic shock. Alprostadil restores and sustains this critical pathway, providing the hemodynamic stability necessary for pre-surgical resuscitation, diagnostic workup, and transfer to a cardiac surgery center.

Beyond ductal patency, one RCT (PMID 19080093) directly demonstrates that Lipo-PGE1 significantly attenuates the systemic inflammatory response and lung injury following cardiopulmonary bypass (CPB) in pediatric congenital heart disease patients — an anti-inflammatory pathway operating through prostaglandin-mediated suppression of neutrophil activation. This dual mechanistic rationale (EP4-mediated ductal vasodilation + post-CPB organ protection) substantially strengthens the biological basis for TxGNN's prediction, and is independently supported by a case report demonstrating PGE1 efficacy in coarctation even after spontaneous ductal closure (PMID 31010402), suggesting mechanisms beyond simple PDA dilation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Phase 1 | Terminated | 10 | Evaluated acute effects of alprostadil on cerebral and pulmonary blood flow after bidirectional cavopulmonary connection (BCPC) in single-ventricle palliation; confirmed biological plausibility of PGE1 in complex CHD hemodynamics, but terminated early (n=10) — provides Phase 1 safety signal only, no efficacy conclusion |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | N/A | Completed | 39 | Cross-sectional diagnostic comparison of Color Doppler Ultrasonography vs MR Angiography in systemic large vessel vasculitis; not a direct alprostadil treatment trial — limited relevance to repurposing hypothesis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | RCT | Zhonghua Yi Xue Za Zhi | Alprostadil (Lipo-PGE1) + ulinastatin significantly reduces post-CPB inflammatory cytokines and lung injury in pediatric CHD patients; highest-quality direct evidence |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Prospective Observational | Pharmacotherapy | Foundational report: PGE1 infusion dilates ductus, raises SaO₂, and improves systemic and pulmonary perfusion across multiple congenital cardiac malformations including aortic defects |
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | Review | Semin Thorac Cardiovasc Surg | PGE1 revolutionized interrupted aortic arch management; establishes multi-day preoperative PGE1 resuscitation followed by one-stage direct anastomosis as current standard |
| [31010402](https://pubmed.ncbi.nlm.nih.gov/31010402/) | 2020 | Case Report + Review | World J Pediatr Congenit Heart Surg | PGE1 successfully managed aortic coarctation with closed ductus; suggests direct aortic wall relaxation as mechanism independent of ductal patency |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | Clinical Practice Review | Cardiology in the Young | Comprehensive neonatal critical aortic stenosis management; PGE1 essential for stabilizing left ventricular wall stress and preserving coronary perfusion before intervention |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | Retrospective Cohort | Asian J Surg | Staged surgical repair for interrupted aortic arch (n not specified); PGE1 bridge is integral to achieving preoperative stability in all cases |
| [16368373](https://pubmed.ncbi.nlm.nih.gov/16368373/) | 2006 | Retrospective Cohort | Ann Thorac Surg | Outcomes after treatment of critical aortic stenosis in neonates; preoperative PGE1 protocol supports safe surgical timing |
| [1926911](https://pubmed.ncbi.nlm.nih.gov/1926911/) | 1991 | Review | DICP Ann Pharmacotherapy | Recommends initiating PGE1 at the referring hospital before neonatal transport for all suspected ductus-dependent defects including aortic lesions; defines standard of care |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | Case Series | Pediatric Cardiology | PGE1 infusion in 7 neonates with hypoplastic left ventricle and aortic atresia; transient metabolic and circulatory improvement demonstrated in 6 of 7 cases |
| [30347623](https://pubmed.ncbi.nlm.nih.gov/30347623/) | 2019 | Review | J Neonatal Perinat Med | Describes feeding strategies and NEC risk in infants on PGE1 for duct-dependent CHD; documents clinical management complexity during prolonged alprostadil infusions |

---

## Market Information (Taiwan TFDA)

No regulatory approvals found in the Taiwan FDA (TFDA) database for Alprostadil. The drug has **0 registered licenses** in Taiwan as of the data cutoff (June 2026).

> **Context note:** Alprostadil is approved by the US FDA under trade names Prostin VR Pediatric® (IV, for PDA maintenance in neonates), Caverject®, and MUSE® (for erectile dysfunction). The absence from Taiwan TFDA records represents a local registration gap rather than a global lack of regulatory approval.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alprostadil has a deeply established, mechanistically coherent role in aortic malformation — specifically ductus-dependent systemic circulation disorders — supported by over four decades of published clinical experience, one directly relevant Phase 1 trial, and an RCT demonstrating post-CPB organ protection benefit. The L3 evidence level reflects the absence of a dedicated Phase 2/3 RCT for this specific diagnostic label; however, the mechanistic basis is so well-characterized that this largely reflects standard-of-care practice documented in the literature rather than a novel repurposing hypothesis requiring de-novo proof-of-concept.

**To proceed, the following is needed:**
- **Taiwan regulatory pathway:** Identify compassionate-use, special import, or hospital-formulary approval mechanisms given zero TFDA registrations
- **Safety data completion:** Retrieve complete warnings, contraindications, and drug interaction profile from the TFDA or US FDA package insert (MOA and warnings are currently data gaps)
- **Indication stratification:** Define specific aortic malformation subtypes (interrupted aortic arch / coarctation / aortic atresia / critical aortic stenosis) for targeted evaluation, as PGE1 benefit and dosing protocol may differ across subtypes
- **Prospective validation design:** Consider a registry-based prospective cohort study to formally capture hemodynamic endpoints (ductal patency rate, pre-surgical SaO₂, time-to-surgery, post-CPB inflammatory markers) in a Taiwan pediatric population
- **Post-CPB lung protection protocol:** Evaluate whether the alprostadil + ulinastatin combination (PMID 19080093 RCT) can be formally adopted into the pediatric cardiac surgery pathway at local centers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

