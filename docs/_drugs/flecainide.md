---
layout: default
title: Flecainide
parent: 僅模型預測 (L5)
nav_order: 710
evidence_level: L5
indication_count: 10
---

# Flecainide
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

Using the report as a direct content-generation task (the full output template was supplied verbatim by the user); no additional skill applies here since this isn't model training/pipeline work, just report authoring from a provided Evidence Pack. I verified evidence_level, scores, and trial/literature counts against the JSON before writing.

# Flecainide: From Cardiac Arrhythmia to Stroke Disorder

## One-Sentence Summary

Flecainide is a Class Ic antiarrhythmic (sodium-channel blocker) whose established use is rhythm control in supraventricular arrhythmias, most notably atrial fibrillation (AF). The TxGNN model predicts a signal for **Stroke Disorder**, with **19 clinical trials** and **20 publications** currently available as supporting evidence — though the mechanism runs through AF rhythm control rather than a direct anti-stroke effect, and this distinction matters for how the signal should be interpreted.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the current regulatory dataset (drug is Not Marketed, 0 licenses on file); by established pharmacology, flecainide is indicated for paroxysmal supraventricular tachyarrhythmias and prevention/maintenance of sinus rhythm in atrial fibrillation |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the evidence pack. Based on known pharmacology, flecainide is a Class Ic antiarrhythmic that blocks fast inward sodium channels, slowing conduction in atrial and ventricular tissue. Its efficacy in maintaining sinus rhythm in atrial fibrillation and treating paroxysmal supraventricular tachycardia is well established.

The connection between flecainide and "stroke disorder" is **indirect, not direct**: flecainide does not have an antithrombotic, neuroprotective, or vascular mechanism. Instead, the link runs through its role as a rhythm-control agent for AF — AF is the leading cardioembolic risk factor for ischemic stroke, and trials of early rhythm-control strategies (in which flecainide is a commonly used agent) have shown reductions in a composite endpoint that includes stroke. This is best understood as "reducing downstream stroke risk by treating an upstream arrhythmia," rather than flecainide directly treating cerebrovascular disease.

This distinction is clinically important. The knowledge graph also surfaces a contraindication-direction signal for a related node (sick sinus syndrome, rank 3): as a sodium-channel blocker, flecainide can suppress sinus node conduction and is relatively contraindicated in patients with sinus node dysfunction or structural heart disease, historically associated with proarrhythmic mortality risk (Class Ic drugs) in populations with structural heart disease. Any pathway forward needs to explicitly frame the target population as "AF patients without significant structural heart disease, for stroke-risk reduction via rhythm control," not "stroke disorder" as a standalone indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST-AFNET4 — early, structured rhythm-control therapy (incl. flecainide) vs. usual care tested against a composite CV death/stroke/heart-failure hospitalization endpoint in AF patients; landmark trial for this pathway |
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | Active, not recruiting | 186 | Assesses flecainide's ability to lower arrhythmia/stroke risk after PFO closure in cryptogenic stroke patients — most direct flecainide-to-stroke-endpoint trial identified |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1,746 | Tests early comprehensive rhythm-control therapy for stroke prevention in patients with acute ischemic stroke and AF |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | CABANA — catheter ablation vs. antiarrhythmic drug therapy for AF; stroke tracked as a secondary safety endpoint |
| [NCT02459574](https://clinicaltrials.gov/study/NCT02459574) | N/A | Completed | 321 | Ablation vs. antiarrhythmic drugs for reducing AF-related hospital episodes |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, not recruiting | 484 | Pulsed field ablation vs. antiarrhythmic drug therapy as first-line treatment for persistent AF |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Phase 4 | Unknown | 70 | Compares vernakalant and flecainide effects on atrial contractility post-cardioversion, a mechanism linked to post-cardioversion stroke risk |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Not yet recruiting | 100 | SAVE STROKE Phase II — neurological outcomes after AF ablation for rhythm control vs. routine medication in patients with recent stroke |
| [NCT02389218](https://clinicaltrials.gov/study/NCT02389218) | Phase 4 | Completed | 13 | Cryoballoon ablation vs. standardized medication in early-onset persistent AF; small sample, supportive only |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | Not yet recruiting | 988 | Evaluates flecainide safety vs. standard rhythm-control drugs (sotalol/amiodarone) in AF patients with stable coronary artery disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | RCT | Europace | Safety/efficacy analysis of long-term sodium-channel blocker (flecainide/propafenone) therapy within EAST-AFNET4 for early rhythm control |
| [37109225](https://pubmed.ncbi.nlm.nih.gov/37109225/) | 2023 | RCT | J Clin Med | Multicenter RCT comparing carvedilol and flecainide for idiopathic PVC suppression (arrhythmia-focused, not stroke-specific) |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | J Atrial Fibrillation | Retrospective cohort comparing CV events, stroke, heart failure, and liver injury risk across antiarrhythmics (dronedarone vs. amiodarone and others) |
| [35114252](https://pubmed.ncbi.nlm.nih.gov/35114252/) | 2022 | Cohort | J Mol Cell Cardiol | Mechanistic/cohort study on atrial-selective biophysical properties of flecainide underlying its relative ventricular safety |
| [27159789](https://pubmed.ncbi.nlm.nih.gov/27159789/) | 2016 | Review | Nature Reviews Disease Primers | Comprehensive AF review noting stroke as a key complication and outlining rhythm/rate-control management principles |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Review | BMJ Clinical Evidence | Review of acute-onset AF management, including stroke risk and antiarrhythmic drug options |
| [39077579](https://pubmed.ncbi.nlm.nih.gov/39077579/) | 2023 | Review | Rev Cardiovasc Med | Review on managing AF during pregnancy, including antiarrhythmic and anticoagulant risk-benefit considerations |
| [21718559](https://pubmed.ncbi.nlm.nih.gov/21718559/) | 2011 | Review | BMJ Clinical Evidence | Earlier edition of acute AF review covering stroke and heart-failure risk |
| [19450312](https://pubmed.ncbi.nlm.nih.gov/19450312/) | 2008 | Review | BMJ Clinical Evidence | Review confirming stroke and heart-failure risk elevation with acute AF and outlining rate/rhythm control approaches |
| [11445058](https://pubmed.ncbi.nlm.nih.gov/11445058/) | 2001 | Review | Curr Treat Options Cardiovasc Med | Review of atrial flutter treatment goals, relevant to rhythm-control rationale shared with AF |

---

## US Market Information

Flecainide currently has no FDA/NDA authorization records in the reference dataset — the drug is classified as **Not Marketed** (0 licenses on file as of the 2026-07-14 data cutoff).

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data are currently available in this evidence pack (TFDA label data collection is flagged as a **Blocking** data gap — DG001).

Note: literature and knowledge-graph signals reviewed for this candidate (proarrhythmic risk in overdose, relative contraindication in sinus node dysfunction) point to safety considerations that should be formally verified once label data is obtained — see Next Steps.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic link to "Stroke Disorder" is indirect (via AF rhythm control, not a direct anti-stroke effect), and the strongest supporting trial (EAST-AFNET4) evaluated a rhythm-control strategy broadly rather than flecainide specifically.
- A **Blocking** data gap exists on TFDA label warnings/contraindications (DG001), which prevents even an initial safety screen (S1) from being completed — this alone precludes a "Go" or "Proceed with Guardrails" decision at this stage.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications, DDI) to resolve the Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Explicit reframing of the candidate indication as "AF-driven stroke-risk reduction via rhythm control" rather than "stroke disorder" as a standalone target, to avoid overstating direct efficacy
- Structural heart disease / sinus node function screening criteria, given known proarrhythmic risk in Class Ic antiarrhythmics
- Clarification of regulatory pathway, since the drug currently has no marketing authorization on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

