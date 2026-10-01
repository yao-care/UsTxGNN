---
layout: default
title: Flecainide
parent: Moderate Evidence (L3-L4)
nav_order: 710
evidence_level: L4
indication_count: 10
---

# Flecainide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Flecainide: From Cardiac Arrhythmias to Stroke Disorder

## One-Sentence Summary

Flecainide is an oral class Ic sodium channel blocker, originally used to treat cardiac arrhythmias such as atrial fibrillation (AF) and supraventricular tachycardia.
The TxGNN model predicts it may be useful for **Stroke Disorder**, but the link is indirect (stroke prevention through AF rhythm control, not stroke treatment).
The search returned **19 clinical trials** and **20 publications**, but none tests flecainide against a stroke outcome.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cardiac arrhythmias such as AF and paroxysmal supraventricular tachycardia (taken from the literature; the license records carry no indication text) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed entries are ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on the literature, flecainide is a class Ic antiarrhythmic that blocks sodium channels. Its efficacy in maintaining sinus rhythm in AF is established. It has no known action on the cerebral ischemia pathway itself.

The link between the original and new indication is indirect. AF raises stroke risk about fivefold. Early rhythm control with antiarrhythmic drugs, including flecainide, may lower AF-related cardiovascular events. The strongest support is the EAST-AFNET 4 trial (n=2,789), and it is class-level evidence, not a flecainide-specific test. Any benefit would be stroke prevention in AF patients, not treatment of established stroke.

Safety is the main obstacle. Flecainide is contraindicated in structural heart disease and coronary artery disease (per the CAST findings), and many stroke patients have these conditions.

The other predicted entries add little. "Cerebrovascular disorder" (rank 9) and "obsolete susceptibility to ischemic stroke" (rank 2) overlap with the stroke concept and are not independent evidence. The remaining predictions (for example ABri amyloidosis, sarcoglycanopathy, duodenal obstruction) have no trials, no literature and no plausible mechanism. Sick sinus syndrome 2 (rank 3) is an SCN5A sodium channel disorder, where flecainide may cause harm rather than benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2789 | EAST-AFNET 4: early rhythm control (antiarrhythmic drugs or ablation) vs usual care to prevent AF-related complications. Strongest evidence, but class-level and preventive |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1746 | Early rhythm control in patients with acute ischemic stroke and AF. Directly stroke-related, but flecainide is not tested specifically and there are no results |
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | Active, not recruiting | 186 | Flecainide after patent foramen ovale closure in cryptogenic stroke patients. The endpoint is atrial arrhythmia, not stroke |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | Not yet recruiting | 988 | Flecainide vs sotalol or amiodarone for safety in AF with stable coronary artery disease. Relevant to the safety guardrail |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Not yet recruiting | 100 | Neurological outcomes after AF ablation vs medication in recent stroke. A procedure trial, not flecainide-specific |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2204 | CABANA: catheter ablation vs rate or rhythm control drugs in AF. Drugs are the comparator and it is not flecainide-specific |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Phase 4 | Unknown | 70 | Vernakalant and flecainide effects on atrial contractility after cardioversion. Decreased contractility is linked to stroke risk |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Phase 3 | Completed | 245 | STOP AF: cryoablation vs antiarrhythmic drugs (flecainide, propafenone or sotalol) in paroxysmal AF. Not a stroke endpoint |
| [NCT02389218](https://clinicaltrials.gov/study/NCT02389218) | Phase 4 | Completed | 13 | Medical therapy vs cryoballoon ablation in persistent AF. Very small, no stroke endpoint |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, not recruiting | 484 | Pulsed field ablation vs antiarrhythmic drugs as first-line treatment for persistent AF. Not flecainide-specific and not stroke-focused |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | RCT (secondary analysis) | Europace | EAST-AFNET 4 analysis of flecainide and propafenone for early rhythm control, addressing concerns about proarrhythmic effects in patients with cardiovascular disease |
| [25820938](https://pubmed.ncbi.nlm.nih.gov/25820938/) | 2015 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Antiarrhythmics for maintaining sinus rhythm after AF cardioversion. Effect on mortality and other clinical outcomes was unclear |
| [27159789](https://pubmed.ncbi.nlm.nih.gov/27159789/) | 2016 | Review | Nat Rev Dis Primers | AF is the most common sustained rhythm disorder, with increased stroke risk |
| [8729366](https://pubmed.ncbi.nlm.nih.gov/8729366/) | 1995 | Electrophysiology study | Arch Mal Coeur Vaiss | 38 patients with unexplained ischemic cerebrovascular events: atrial vulnerability testing and effects of IV flecainide on atrial arrhythmia induction |
| [23871349](https://pubmed.ncbi.nlm.nih.gov/23871349/) | 2013 | Trial analysis | Int J Cardiol | Flec-SL analysis of stroke risk after elective cardioversion of AF (low stroke risk reported in the title) |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohort | BMC Med | Multinational cohort of concomitant DOAC and interacting antiarrhythmic use in non-valvular AF, assessing stroke and bleeding |
| [37000581](https://pubmed.ncbi.nlm.nih.gov/37000581/) | 2023 | Cohort | Europace | Cardiovascular outcomes in AF patients on antiarrhythmic drugs plus non-vitamin K oral anticoagulants |
| [35114252](https://pubmed.ncbi.nlm.nih.gov/35114252/) | 2022 | Preclinical | J Mol Cell Cardiol | Atrial sodium channel properties explain flecainide's greater atrial effectiveness and relative ventricular safety in AF |
| [40800559](https://pubmed.ncbi.nlm.nih.gov/40800559/) | 2025 | Case report | Eur Heart J Case Rep | Refractory ventricular tachycardia with flecainide. QRS widening raises proarrhythmia risk in structural heart disease or ischemia |
| [27884575](https://pubmed.ncbi.nlm.nih.gov/27884575/) | 2017 | Case report | J Emerg Med | Brugada pattern unmasked by flecainide overdose |

---

## US Market Information

The 20 US licenses are all generic flecainide acetate tablets (oral). Approved indication text is not recorded for any of them. Below are 4 of the 5 main entries shown; the fifth is a duplicate of ANDA075442.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA075882 | Flecainide Acetate | Tablet | Golden State Medical Supply, Inc. |
| ANDA202821 | Flecainide Acetate | Tablet | Aurobindo Pharma Limited |
| ANDA075442 | Flecainide Acetate | Tablet | Amneal Pharmaceuticals LLC |
| ANDA079164 | Flecainide Acetate | Tablet | Chartwell RX, LLC |

---

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the record. Please refer to the package insert for safety information.

The prediction analysis flags these guardrails:
- **Structural heart disease and coronary artery disease**: flecainide is contraindicated (CAST), and many stroke patients have these conditions. The pending trial NCT07405671 will test flecainide safety in AF with stable coronary artery disease.
- **Sick sinus syndrome**: flecainide can worsen sinus node dysfunction and conduction, so it is generally contraindicated without pacing.
- **Anticoagulant co-therapy**: patients who need anticoagulation for stroke prevention require interaction review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted link is indirect and class-level. The best evidence (EAST-AFNET 4) tests early rhythm control in general, not flecainide for stroke, and no flecainide-specific trial has a stroke endpoint. The main safety guardrails (structural heart disease, coronary artery disease) overlap heavily with the likely stroke population.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and drug interaction data
- A flecainide-specific analysis of stroke outcomes from EAST-AFNET 4 or similar cohorts
- Results from NCT05293080 (early rhythm control in acute stroke with AF) and NCT07405671 (flecainide safety in AF with coronary artery disease)
- Merge the duplicate stroke entries (stroke disorder, cerebrovascular disorder, obsolete susceptibility to ischemic stroke) and define the target population, likely AF patients without structural heart disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

