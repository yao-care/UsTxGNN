---
layout: default
title: Dronedarone
parent: Model Prediction Only (L5)
nav_order: 629
evidence_level: L5
indication_count: 10
---

# Dronedarone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dronedarone: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dronedarone is a marketed antiarrhythmic drug used to control rhythm in atrial fibrillation (AF).
The TxGNN model predicts it may help with **stroke disorder**, and the literature suggests this would mean lowering stroke risk within selected AF patients, not treating stroke itself.
The search returned **19 clinical trials** and **20 publications**. Only a few are dronedarone-specific, and the key Phase 3 trial (PALLAS) showed harm in permanent AF.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (the license records list no indication text, so this comes from the evidence pack's repurposing rationale) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 (per the evidence pack scoring; the evidence is indirect and mixed, see the conclusion) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both records carry the same NDA number, NDA022425) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the record. Dronedarone is known as a multichannel-blocking antiarrhythmic (a non-iodinated amiodarone analogue) that controls rhythm and rate in AF and atrial flutter.

AF is a leading cause of cardioembolic stroke. If a drug lowers AF burden, it could plausibly lower stroke risk.
- Post-hoc analyses of the ATHENA trial suggested fewer strokes in paroxysmal or persistent AF.
- A meta-analysis of randomized trials (PMID 22149318) points the same way.
- EAST-AFNET 4, in which dronedarone was one of the drug options, supports early rhythm control on a composite outcome that includes stroke.
- A preclinical study (PMID 28992468) reported anticoagulant and antiplatelet effects independent of rhythm control. This is hypothesis-generating only.

The effect depends on the population. PALLAS, a Phase 3 trial in permanent AF with additional risk factors, was terminated. The drug was harmful there, with more stroke, heart failure, and cardiovascular death. The evidence therefore supports "stroke-risk reduction within appropriate AF patients," not a standalone cerebrovascular indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3236 | PALLAS: placebo-controlled RCT of dronedarone 400 mg BID in permanent AF with risk factors. Stroke was part of the composite outcome. The drug was harmful and the trial was stopped. |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2789 | EAST-AFNET 4: early rhythm control (ablation or antiarrhythmic drugs, including dronedarone) vs usual care. Composite outcome includes stroke. |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic RCT of early dronedarone vs usual care in first-detected AF. Small, and stroke is probably not the primary endpoint. |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1746 | Early rhythm control for stroke prevention in acute ischemic stroke with AF. Stroke-directed, but not dronedarone-specific. |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A (observational) | Completed | 1015 | Real-world comparison of dronedarone vs other AF treatments in Germany, Spain, Italy, and the USA. Subject to confounding. |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not yet recruiting | 1898 | Dronedarone for early rhythm control in AF: efficacy, safety, and quality of life. No stated stroke endpoint. |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A (SLR/NMA) | Completed | 87810 | Systematic review and network meta-analysis of dronedarone (Multaq) vs sotalol safety and effectiveness in AF. |
| [NCT04704050](https://clinicaltrials.gov/study/NCT04704050) | Phase 4 | Terminated | 22 | EDORA: dronedarone vs placebo after ablation, looking at atrial fibrosis and AF recurrence. Too small to be informative. |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Unknown | 100 | Amiodarone vs dronedarone for maintaining sinus rhythm after cardioversion. No stroke endpoint. |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2204 | CABANA: catheter ablation vs drug therapy for AF. Dronedarone is not the specific comparator, so the evidence is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | N Engl J Med | Tested whether dronedarone reduces major vascular events in high-risk permanent AF. Harm was seen in this population, so the drug should not be used there. |
| [22149318](https://pubmed.ncbi.nlm.nih.gov/22149318/) | 2011 | Meta-analysis | Am J Cardiovasc Drugs | Systematic review of randomized trials on stroke incidence with dronedarone in paroxysmal or persistent AF. Built on the ATHENA post-hoc signal of reduced stroke. |
| [40295782](https://pubmed.ncbi.nlm.nih.gov/40295782/) | 2025 | Post-hoc RCT analysis | Europace | ATHENA re-analyzed with EAST-AFNET 4 criteria. Assessed whether dronedarone improves cardiovascular outcomes in early AF with comorbidities. |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | Post-hoc RCT analysis | Clin Res Cardiol | Long-term safety and efficacy of amiodarone and dronedarone for early rhythm control in EAST-AFNET 4. |
| [30528621](https://pubmed.ncbi.nlm.nih.gov/30528621/) | 2019 | Cohort | Int J Cardiol | Analysis of myocardial infarction and stroke risk with dronedarone in AF patients in German general practices. |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | J Atr Fibrillation | Real-world US cohort (10,455 adults) comparing risk of cardiovascular events, stroke, heart failure, interstitial lung disease, and liver injury for dronedarone vs amiodarone and other antiarrhythmics. |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Dronedarone vs sotalol in antiarrhythmic-drug-naive veterans with AF: effectiveness and safety. |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | FDA approval in 2009 followed ATHENA. A post-hoc analysis suggested lower stroke risk, but safety concerns remain. |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic/experimental | Atherosclerosis | Investigated direct anticoagulant and antiplatelet effects of dronedarone independent of its antiarrhythmic action. |
| [31898737](https://pubmed.ncbi.nlm.nih.gov/31898737/) | 2020 | Hypothesis paper | Europace | Proposes that amiodarone and dronedarone may prevent stroke by treating atrial myopathy. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022425 | Multaq (Sanofi-Aventis U.S. LLC) | Tablet, film coated (oral) | Not provided in the license record |
| NDA022425 | Multaq (Cardinal Health 107, LLC) | Tablet, film coated (oral) | Not provided in the license record |

---

## Safety Considerations

The structured warning, contraindication, and interaction fields are empty. Please refer to the package insert for full safety information. The following signals come from the trial and literature evidence:

- **Key Warnings**:
  - PALLAS showed harm (more stroke, heart failure, and cardiovascular death) in permanent AF with additional risk factors.
  - Dronedarone slows heart rate and conduction, so it is expected to worsen sinus node disease.
- **Contraindications**: Decompensated heart failure (per the repurposing rationale). Permanent AF is a population where the drug should not be used.
- **Drug Interactions**:
  - Dronedarone may raise digoxin levels through P-glycoprotein inhibition (PMID 33888353).
  - Concomitant use with direct oral anticoagulants is discussed in the literature (PMIDs 27693025, 41152878).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The stroke signal is indirect, coming from post-hoc analyses and rhythm-control strategy trials rather than a dronedarone trial with stroke as its primary endpoint. PALLAS showed real harm in permanent AF. The package insert safety data are also missing, which blocks the safety screening step.
No completed Phase 3 dronedarone RCT supports stroke prevention, so the L2 label is generous. The other nine predictions (for example obsolete susceptibility to ischemic stroke, ABri amyloidosis, sarcoglycanopathy) are L4–L5 with no supporting evidence and should stay on hold. Cerebrovascular disorder (rank 4) is the same AF-embolism route as stroke and should be merged with it.

**To proceed, the following is needed:**
- Package insert warnings, contraindications, and approved-indication text (NDA022425)
- Mechanism-of-action data from DrugBank
- Stroke as a prespecified endpoint in dronedarone-specific data, such as a re-analysis of ATHENA and EAST-AFNET 4 restricted to paroxysmal or persistent AF
- A defined eligible population that excludes permanent AF, decompensated heart failure, and sinus node disease
- Review of interaction risks with digoxin and direct oral anticoagulants

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

