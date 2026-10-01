---
layout: default
title: Adenosine
parent: Model Prediction Only (L5)
nav_order: 216
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Adenosine: From an Unlisted Original Indication to Obsolete Bundle Branch Block (Secondary Candidate: CPVT)

## One-Sentence Summary

The available regulatory data do not list an approved indication for adenosine, which is marketed in the US mainly as an injectable.
The TxGNN model's top prediction is **obsolete bundle branch block**, but it has **0 clinical trials and 0 publications**, and the disease label is an outdated ontology term.
The second prediction, **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, has **1 early-phase trial** and **13 publications**. However, only 1 case report (with ATP, not adenosine) is a direct clinical signal, so this remains a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available regulatory data (all approved-indication fields are empty) |
| Predicted New Indication | Obsolete bundle branch block (rank 1); catecholaminergic polymorphic ventricular tachycardia (rank 2) |
| TxGNN Prediction Score | 99.94% (bundle branch block); 99.42% (CPVT) |
| Evidence Level | L5 (bundle branch block); L4 (CPVT) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations on record |
| Recommended Decision | Hold (both candidates) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data are not available for this drug. Adenosine is known to slow conduction through the atrioventricular (AV) node, but the evidence pack cannot confirm this or link it to the predicted diseases.

**Obsolete bundle branch block (rank 1):** This prediction is hard to defend.
- The disease label is an obsolete ontology term, so the high score of 99.94% cannot be tied to a defined clinical entity.
- Slowing AV nodal conduction is not a plausible treatment for a conduction block below the AV node, within the ventricles.
- No mechanistic cross-check was possible.

**CPVT (rank 2):** This is plausible but unproven.
- Activating the adenosine A1 receptor lowers cAMP and opposes beta-adrenergic stimulation. This could suppress the catecholamine-driven triggered activity that underlies CPVT.
- The only direct clinical signal is a single case report in which ATP terminated bidirectional ventricular tachycardia in a CPVT patient. ATP is an adenosine precursor, not adenosine itself.
- Adenosine can also provoke arrhythmias in some settings, so its safety in this population is unresolved.

## Clinical Trial Evidence

**Obsolete bundle branch block:** Currently no related clinical trials registered.

**CPVT:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2 | Recruiting | 10 | Phase 2a study (PACE-CPVT) of AGP100 in CPVT, assessing safety, tolerability and exploratory efficacy. The data do not link AGP100 to adenosine, so this is not usable as direct evidence (relevance grade C). |

## Literature Evidence

**Obsolete bundle branch block:** Currently no related literature available.

**CPVT** (no RCTs found; ordered by study type and relevance):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case report | Heart Rhythm | ATP terminated bidirectional ventricular tachycardia in a CPVT patient. This is the only direct clinical signal, and it involves ATP rather than adenosine. |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Review (consensus statement) | Europace | European Heart Rhythm Association-led consensus on pharmacological provocation testing in cardiac electrophysiology for sudden cardiac death, arrhythmias and ECG abnormalities. |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | J Assoc Physicians India | Classification and management of ventricular tachycardia in structurally normal hearts. |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Review | Paediatr Anaesth | Overview of pediatric arrhythmias for anesthesiologists, including patients with inherited channelopathies. |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Clinical study (design unverified) | Heart Rhythm | Postpacing abnormal repolarization in CPVT with a cardiac ryanodine receptor mutation. |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | Preclinical (in vitro) | J Physiol | Human cardiac-neural microtissues suggest CPVT also involves the sympathetic neuron. |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclinical (animal) | Cardiovasc Res | PDE2A and PDE4B gene therapy improved heart failure and arrhythmias in mice by improving cAMP compartmentation. |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Preclinical (animal) | Sci Transl Med | Sarcoplasmic reticulum calcium leak contributes to arrhythmia but not to heart failure progression. |

Most of these papers concern CPVT biology rather than adenosine. Their relevance to adenosine has not been assessed.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090212 | Adenosine (Mylan Institutional LLC) | Injection, solution | Not listed |
| ANDA077425 | Adenosine (Meitheal Pharmaceuticals Inc.) | Injection, solution | Not listed |
| ANDA206778 | Adenosine (Gland Pharma Limited) | Solution | Not listed |
| No number listed | The Skinhouse Wrinkle Collagen (NOKSIBCHO cosmetic Co., Ltd.) | Cream | Not listed |
| No number listed | Tenue 24k gold ampoule (LAON COMMERCE co ltd) | Liquid | Not listed |

The table shows 5 of 20 authorizations. The two products without authorization numbers are cosmetics, not drug approvals.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, obsolete bundle branch block, has no supporting studies and is mechanistically implausible, so its high score is not actionable. The CPVT prediction is a reasonable research question (L4), but the only direct clinical signal is a single ATP case report, and adenosine may itself provoke arrhythmias.

**To proceed, the following is needed:**
- Package insert warnings and contraindications. This is a blocking gap, so the candidate cannot proceed to safety screening without it.
- Mechanism of action data from DrugBank, to support a mechanistic-link analysis.
- Confirmation of the original approved indication, since all indication fields are empty.
- For CPVT: a literature search for adenosine-specific (not ATP) evidence in CPVT, and a safety assessment of proarrhythmic risk in this population.
- Replacement of the obsolete bundle branch block label with a current disease term before any re-evaluation.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

