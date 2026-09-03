---
layout: default
title: Sotalol
parent: 僅模型預測 (L5)
nav_order: 1178
evidence_level: L5
indication_count: 7
---

# Sotalol
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

# Sotalol: From Arrhythmia Management to Atrial Fibrillation-Related Stroke Risk Reduction

## One-Sentence Summary

> Sotalol is a non-selective beta-blocker with Class III antiarrhythmic activity; no approved-indication text or MOA record is available in this evidence pack (registry/label data gap). Among the seven TxGNN-predicted indications reviewed, the model's single highest-ranked candidate (sick sinus syndrome) is mechanistically implausible and possibly contraindicated, while the strongest-evidenced candidate is **rhythm control of atrial fibrillation/flutter for stroke risk reduction**, supported by **20 clinical trials** (including a completed Phase 3 RCT with 706 patients) and **20 publications**. This represents confirmation of an already-established antiarrhythmic use rather than a novel repurposing discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license records in this evidence pack (drug not marketed in this jurisdiction) |
| Predicted New Indication | Atrial fibrillation/flutter rhythm control for stroke risk reduction (mapped from TxGNN term "stroke disorder") |
| TxGNN Prediction Score | 99.44% (rank 4 of 7 candidates reviewed) |
| Evidence Level | L1 |
| Market Status | Not marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for sotalol in this evidence pack (data gap DG002). Based on the pharmacology reflected in the literature and trial evidence, sotalol combines non-selective beta-adrenergic blockade with Class III antiarrhythmic activity (IKr/repolarization prolongation), which underlies its established role in maintaining sinus rhythm in atrial fibrillation (AF) and treating ventricular arrhythmias.

TxGNN's top-ranked prediction by raw score was **sick sinus syndrome** (99.76%), but the drug's own repurposing rationale flags this as mechanistically backwards: sick sinus syndrome typically requires increasing heart rate (often with pacemaker support), whereas sotalol suppresses sinus node automaticity and conduction — a likely relative contraindication rather than a treatment opportunity. Similarly, **Wildervanck syndrome**, **sarcoglycanopathy**, **macrocephaly/dysmorphic facies/psychomotor retardation syndrome**, and **"obsolete susceptibility to ischemic stroke"** (a deprecated ontology term) have no supporting trials or literature and are best explained as knowledge-graph noise. **Manic bipolar affective disorder** is supported only by drug-interaction/safety literature warning that beta-blockade can *worsen* antipsychotic-associated QT prolongation risk — again a safety signal, not efficacy evidence.

By contrast, the "stroke disorder" prediction maps to a well-documented, evidence-backed application: AF is a major driver of ischemic stroke, and sotalol is used clinically to maintain sinus rhythm in AF/flutter, thereby indirectly reducing stroke risk. This is corroborated by a completed VA cooperative Phase 3 RCT (CSP #399, n=706) directly testing sotalol for AF rhythm control, plus a large systematic review/network meta-analysis (n=87,810) comparing sotalol against dronedarone in AF safety outcomes. This report therefore focuses on this best-evidenced candidate rather than the raw top-scored TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00007605](https://clinicaltrials.gov/study/NCT00007605) | Phase 3 | Completed | 706 | VA Cooperative Study (CSP #399): amiodarone vs. sotalol vs. class I agents for maintaining sinus rhythm in AF — direct RCT evidence for sotalol. |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A (SLR/NMA) | Completed | 87,810 | Systematic literature review/network meta-analysis comparing dronedarone (Multaq) vs. sotalol safety/effectiveness in AF patients. |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Phase 3 | Completed | 245 | STOP AF trial: cryoablation vs. antiarrhythmic drugs (flecainide, propafenone, or sotalol) in paroxysmal AF refractory patients. |
| [NCT02145546](https://clinicaltrials.gov/study/NCT02145546) | Phase 4 | Unknown | 600 | Compares amiodarone, sotalol, and propafenone for AF burden reduction in sick sinus syndrome patients post-pacing. |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | Not yet recruiting | 988 | Flecainide vs. standard rhythm-control drugs (sotalol/amiodarone) in AF with stable coronary artery disease. |
| [NCT02389218](https://clinicaltrials.gov/study/NCT02389218) | Phase 4 | Completed | 13 | Medical therapy vs. cryoballoon ablation in early persistent AF; small sample, drug regimen not sotalol-specific. |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | CABANA trial: catheter ablation vs. antiarrhythmic drug therapy (rate/rhythm control) for AF. |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A | Completed | 1,015 | Real-world observational study of dronedarone vs. other antiarrhythmic agents (including sotalol) for AF. |
| [NCT06322017](https://clinicaltrials.gov/study/NCT06322017) | N/A | Recruiting | 294 | Early pulmonary vein isolation vs. usual (drug) treatment in AF patients over age 75. |
| [NCT02459574](https://clinicaltrials.gov/study/NCT02459574) | N/A | Completed | 321 | AF ablation vs. antiarrhythmic drug therapy for reducing hospitalization from recurrent AF. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9576159](https://pubmed.ncbi.nlm.nih.gov/9576159/) | 1998 | Randomized, double-blind | Am J Cardiol | Low-dose amiodarone vs. sotalol for suppression of recurrent symptomatic AF (n=70). |
| [29954667](https://pubmed.ncbi.nlm.nih.gov/29954667/) | 2019 | Cohort | Int J Cardiol | Efficacy and adverse effects of sotalol in adults with congenital heart disease. |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort/Comparative | Circ Arrhythm Electrophysiol | Dronedarone vs. sotalol head-to-head effectiveness/safety in antiarrhythmic-naïve veterans with AF. |
| [1281807](https://pubmed.ncbi.nlm.nih.gov/1281807/) | 1992 | Clinical Study | Int J Cardiol | Efficacy and safety of sotalol in patients with complex ventricular arrhythmias (n=626 pooled). |
| [8346725](https://pubmed.ncbi.nlm.nih.gov/8346725/) | 1993 | Clinical Study | Am J Cardiol | Hemodynamic effects of oral sotalol during dose titration in patients with ventricular arrhythmias. |
| [7509121](https://pubmed.ncbi.nlm.nih.gov/7509121/) | 1994 | Clinical Study | Am J Cardiol | Response to sotalol predicts response to amiodarone in sustained ventricular tachycardia with CAD. |
| [25428811](https://pubmed.ncbi.nlm.nih.gov/25428811/) | 2015 | Cost-effectiveness analysis | Kardiol Pol | Cost-effectiveness of dronedarone vs. amiodarone, propafenone, and sotalol in AF. |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | J Atr Fibrillation | Cardiovascular/stroke/CHF/liver injury risk: dronedarone vs. amiodarone and other antiarrhythmics. |
| [38011245](https://pubmed.ncbi.nlm.nih.gov/38011245/) | 2023 | Review | Circulation | Contemporary AF management in hypertrophic cardiomyopathy, including antiarrhythmic drug options. |
| [39077579](https://pubmed.ncbi.nlm.nih.gov/39077579/) | 2023 | Review | Rev Cardiovasc Med | Management of AF during pregnancy, including antiarrhythmic drug risk-benefit considerations. |

---

## US Market Information

No marketing authorization records are present in this evidence pack (`total_licenses: 0`, market status: 未上市 / not marketed). Registry/label data will need to be sourced separately before this candidate can advance.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are available in this evidence pack (TFDA label data collection is flagged as a **Blocking** gap — DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The AF/stroke-risk-reduction indication is backed by L1-level evidence (≥2 completed Phase 3 trials plus a large comparative safety review), consistent with sotalol's known, already-established antiarrhythmic use rather than a speculative repurposing target. However, this is a confirmation of existing pharmacology, not a novel discovery, and a critical safety data gap remains unresolved.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/label warnings, contraindications, and QT-prolongation/proarrhythmia precautions before any S1 safety review
- Obtain original approved-indication text and MOA documentation (DG002) to complete mechanistic comparison
- Confirm route/dosage-form availability for the target population
- Disregard TxGNN's raw top-ranked candidates (sick sinus syndrome, Wildervanck syndrome, sarcoglycanopathy, macrocephaly/dysmorphic-facies syndrome, obsolete stroke-susceptibility term) — none have supporting evidence, and sick sinus syndrome specifically carries a plausible contraindication risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

