---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 629
evidence_level: L5
indication_count: 10
---

# Dronedarone
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

# Dronedarone: From Atrial Fibrillation/Flutter to Stroke

## One-Sentence Summary

Dronedarone is a Class III antiarrhythmic used to control heart rhythm in atrial fibrillation/flutter (AF/AFL). The TxGNN model predicts it may also reduce **stroke** risk, and this direction is already supported by **19 clinical trials** and **20 publications** — including both a positive pivotal signal (ATHENA) and a critical negative safety signal (PALLAS) that must bound any use case.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial Fibrillation / Atrial Flutter (AF/AFL) — extracted from evidence-pack literature; TFDA license data is unavailable because the drug is not marketed in Taiwan |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed formal MOA data for dronedarone is not available in DrugBank per this evidence pack (data gap DG002). Based on information embedded in the evidence base itself, dronedarone is a multi-ion-channel-blocking Class III antiarrhythmic, structurally related to but non-iodinated compared with amiodarone. It was developed for rhythm/rate control in AF/AFL, and there is mechanistic evidence that it also exerts direct anticoagulant and antiplatelet effects independent of its antiarrhythmic action (PMID 28992468).

The link between AF/AFL and stroke is well established: AF is a major driver of cardioembolic stroke, and effective rhythm control that reduces AF burden can lower thromboembolic risk. The pivotal ATHENA trial (summarized in PMID 20730068) showed dronedarone reduced cardiovascular hospitalization/death in paroxysmal or persistent AF, with a post-hoc signal of reduced stroke risk — this is the mechanistic basis for the TxGNN prediction.

Critically, this relationship is not unconditional. The PALLAS trial ([NCT01151137](https://clinicaltrials.gov/study/NCT01151137), PMID 22082198), conducted specifically in **permanent** AF patients, was terminated early because dronedarone *increased* stroke, MI, and cardiovascular death. So the evidence bifurcates by AF subtype: protective in paroxysmal/persistent AF, harmful in permanent AF. Any repurposing pathway must explicitly exclude permanent AF patients.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3,236 | PALLAS: dronedarone 400mg BID in permanent AF with additional risk factors — terminated early due to increased stroke, MI, and CV death; defines the contraindication boundary. |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST-AFNET4: early structured rhythm-control therapy (including dronedarone) vs usual care reduced AF-related cardiovascular complications, including stroke. |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | CABANA: catheter ablation vs antiarrhythmic drug therapy (including dronedarone) for AF; indirect comparator evidence. |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A | Completed | 1,015 | Real-world observational study comparing dronedarone's effectiveness vs other antiarrhythmics in AF (Germany, Spain, Italy, USA). |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A | Completed | 87,810 | Systematic literature review/NMA comparing dronedarone (Multaq) vs sotalol safety, including stroke outcomes, in AF. |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic RCT of early dronedarone vs usual care in first-detected AF; supports an early rhythm-control strategy. |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1,746 | Tests whether early rhythm-control therapy prevents adverse cardiovascular outcomes in patients with acute ischemic stroke and AF. |
| [NCT02618577](https://clinicaltrials.gov/study/NCT02618577) | Phase 3 | Terminated | 2,608 | NOAH-AFNET6: oral anticoagulation vs current therapy to prevent stroke/systemic embolism/CV death in atrial high-rate episodes — context trial for AF-stroke prevention strategy. |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Unknown | 100 | Amiodarone vs dronedarone for maintenance of sinus rhythm post-cardioversion in persistent AF; low certainty (status unknown). |
| [NCT05939076](https://clinicaltrials.gov/study/NCT05939076) | Phase 3 | Not yet recruiting | 220 | Compares early cryoballoon ablation vs antiarrhythmic drug therapy (including dronedarone) in persistent AF. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | New England Journal of Medicine | Dronedarone in high-risk permanent AF increased major vascular events (stroke, MI, CV death); trial terminated early — key negative safety signal. |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT post-hoc (EAST-AFNET4) | Clinical Research in Cardiology | Long-term safety/efficacy of amiodarone and dronedarone for early rhythm control within EAST-AFNET4; reassuring long-term outcome data. |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review (approval) | Vascular Health and Risk Management | Reviews dronedarone's FDA approval based on the ATHENA trial (reduced CV hospitalization/death); post-hoc analysis suggested reduced stroke risk, but PALLAS later raised safety concerns in permanent AF. |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort (safety) | Journal of Atrial Fibrillation | Real-world retrospective cohort comparing risk of stroke, CV events, CHF, and other adverse events between dronedarone, amiodarone, and other antiarrhythmics. |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic | Atherosclerosis | Shows dronedarone exerts direct anticoagulant/antiplatelet effects independent of its antiarrhythmic action — a mechanistic explanation for ATHENA's stroke/TIA reduction. |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort (veterans) | Circulation: Arrhythmia and Electrophysiology | Retrospective comparison of dronedarone vs sotalol effectiveness/safety in AF patients within the VA healthcare system. |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Review/subgroup (ATHENA post-hoc) | European Journal of Heart Failure | Dronedarone's cardiovascular risk reduction in AF/AFL patients with concomitant HFpEF/HFmrEF, a population with elevated stroke risk. |
| [33888353](https://pubmed.ncbi.nlm.nih.gov/33888353/) | 2021 | Cohort (DDI) | Clinical Therapeutics | Real-world evaluation of digitalis intoxication risk with concomitant dronedarone + digoxin use — a relevant drug-interaction safety signal. |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | General review of AF management, including stroke risk stratification and evolution of antithrombotic therapy. |
| [22920480](https://pubmed.ncbi.nlm.nih.gov/22920480/) | 2012 | Review | Current Cardiology Reviews | Reviews stroke prevention concepts and controversies in AF, contextualizing rhythm-control agents such as dronedarone. |

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: formal DDI/warning/contraindication fields in this evidence pack are data gaps — TFDA label data has not yet been retrieved, flagged as blocking gap DG001. However, evidence-base rationale text does surface two safety signals worth carrying forward: dronedarone is contraindicated in **permanent AF** per the PALLAS trial, and is contraindicated in **sick sinus syndrome/bradycardia** due to known sinus node effects.)*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The paroxysmal/persistent-AF evidence line (ATHENA, EAST-AFNET4) supports a plausible stroke-risk-reduction effect at L2 evidence strength, but the PALLAS trial shows the opposite effect in permanent AF, and formal Taiwan safety/label data is entirely missing (drug not currently marketed, 0 NDAs). This combination — real signal, real contraindication boundary, and a blocking data gap — means the candidate should advance only under explicit guardrails, not as a straightforward "Go."

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, blocking — required before any S1 safety assessment)
- Formal DrugBank MOA record (DG002)
- Confirmation of Taiwan import/market pathway, since the drug currently has 0 licenses and is not marketed
- A completed DDI database query (current status: not_found)
- An explicit protocol excluding permanent AF patients, consistent with the PALLAS safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

