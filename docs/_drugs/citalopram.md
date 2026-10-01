---
layout: default
title: Citalopram
parent: Model Prediction Only (L5)
nav_order: 532
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Citalopram: From SSRI Antidepressant to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI) marketed in the US as generic tablets.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, supported by **30 clinical trials** and **16 publications**.
Most of these trials test escitalopram, a closely related molecule, rather than citalopram itself, so the evidence is strong at the class level but thin for citalopram specifically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided records (indication text is empty); citalopram is an SSRI antidepressant |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 (as assigned in the Evidence Pack; based mainly on class-level and escitalopram trials, not citalopram-specific RCTs) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations (mostly ANDA generics) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, citalopram belongs to the SSRI class. Serotonin reuptake inhibition is the best-established pharmacological mechanism in OCD, and SSRIs are a first-line drug class for it. This mechanism is inferred from drug class, not from a source record.

The clinical evidence follows the same pattern. Trials of escitalopram, the S-enantiomer of citalopram, are the largest body of OCD data in this pack. They include a randomized, double-blind, multi-center comparison of 20 mg versus 40 mg (NCT00723060) and a Phase 3 open-label high-dose study (NCT00305500). Two older publications look at citalopram directly in OCD, including treatment-resistant cases (PMIDs 10471169, 10572334). Together these support the class effect and a near-molecule effect, but not a definitive citalopram-specific efficacy claim.

Some OCD patients need higher SSRI doses than those used for depression. This makes the dose-related safety limits of citalopram, described in the Safety Considerations section, central to any repurposing plan.

## Clinical Trial Evidence

The Evidence Pack lists 30 trials for this prediction. The 10 most relevant are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Randomized, double-blind, multi-center comparison of escitalopram 20 mg vs 40 mg in OCD, with Y-BOCS efficacy and safety endpoints |
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label study of high-dose escitalopram (up to 50 mg/day) in adult OCD outpatients over 18 weeks |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Escitalopram efficacy and optimal dose in OCD |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | Completed | 14 | Pilot study of escitalopram safety and effectiveness for OCD symptoms |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Cognitive behavioral therapy added to serotonin reuptake inhibitor treatment in children with OCD who were partial responders |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Randomized open trial of group CBT vs fluoxetine in OCD, including patients with comorbid psychiatric disorders |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Exposure and response prevention, SSRIs, and their combination in OCD, with predictors of response in a Chinese population |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Completed | 21 | Open comparison of quetiapine vs clomipramine augmentation in SSRI-refractory OCD |
| [NCT00456937](https://clinicaltrials.gov/study/NCT00456937) | Phase 4 | Completed | 15 | Open-label escitalopram up to 20 mg/day in patients with schizophrenia and comorbid OCD |
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | Completed | 149 | Citalopram vs placebo in children with autism spectrum disorders and high levels of repetitive behavior (a related symptom domain, not OCD) |

## Literature Evidence

The Evidence Pack lists 16 publications. The 10 most relevant are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | J Affect Disord | Compares antidepressant and placebo responses in OCD with other anxiety disorders; OCD shows a reduced placebo response |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Meta-analysis | J Psychiatr Res | Network meta-analysis of drug, psychological, and combined treatment in children and adolescents with OCD |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Front Psychiatry | Reviews efficacy, tolerability, and suicidality of antidepressants across pediatric disorders, including OCD |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Review | Compr Psychiatry | Examines long-term safety and tolerability of off-label high-dose serotonin reuptake inhibitors in OCD |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Open-label trial | Eur Psychiatry | Randomized, open-label, 90-day trial in 16 treatment-resistant OCD patients comparing citalopram alone vs citalopram plus clomipramine |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Clinical report / Review | Int Clin Psychopharmacol | Reviews the use of citalopram in OCD and the link between serotonin reuptake inhibitors and OCD neurobiology |
| [32242450](https://pubmed.ncbi.nlm.nih.gov/32242450/) | 2020 | Systematic review | Nord J Psychiatry | Meta-analysis of fluoxetine efficacy, acceptability, and tolerability in pediatric OCD (a class-level reference) |
| [34313207](https://pubmed.ncbi.nlm.nih.gov/34313207/) | 2022 | Clinical study | CNS Spectr | Tests whether the BDNF Val66Met polymorphism affects response to escitalopram or paroxetine in OCD |
| [30973183](https://pubmed.ncbi.nlm.nih.gov/30973183/) | 2019 | Clinical study | Psychiatry Clin Neurosci | 1H-MRS study of brain neurochemistry in 28 unmedicated OCD patients and changes after 12 weeks of escitalopram |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clin Evid | Overview of OCD: about 1% of adult men and 1.5% of adult women are affected, and about 2.7% of children and adolescents |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078216 | Citalopram (Cardinal Health 107, LLC) | Tablet, film coated | Not listed in record |
| ANDA077031 | Citalopram (A-S Medication Solutions) | Tablet, film coated | Not listed in record |
| ANDA078216 | Citalopram (REMEDYREPACK INC.) | Tablet, film coated | Not listed in record |
| ANDA202389 | Escitalopram (NuCare Pharmaceuticals, Inc.) | Tablet, film coated | Not listed in record |
| Not listed | Citalopram (Hahnemann Laboratories, INC.) | Pellet | Not listed in record |

The pack records 20 authorizations in total; these 5 are shown. Dosage forms across the records include film-coated tablets, tablets, pellets, and solutions.

## Safety Considerations

Package insert warnings, contraindications, and drug-interaction data were not available in the Evidence Pack. Please refer to the package insert for full safety information.

The following guardrails come from the Evidence Pack's repurposing assessment:

- **QT prolongation**: Citalopram carries a dose-dependent QT-prolongation limit. The higher-than-depression doses often used in OCD (see PMID 38703743) call for ECG monitoring.
- **CYP2C19 metabolism**: Genotype and plasma-level information may help with dose personalization. NCT05210140 (n=148) studies this for escitalopram, which shares the CYP2C19 pathway.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The class-level rationale is strong: SSRIs are a first-line OCD drug class, and many trials of the near-molecule escitalopram are in this pack. Citalopram-specific OCD evidence is limited to two older publications, and the dose-dependent QT limit makes the higher doses used in OCD a real safety concern.

The other four TxGNN predictions for citalopram are histrionic, schizoid, schizotypal, and paranoid personality disorders. All are rated **Hold**. They share an identical score of 99.68%, which suggests a class-level graph artifact rather than independent signals, and they have no supporting clinical trials.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Evidence from citalopram-specific OCD trials, or a justification for extrapolating from escitalopram
- A dosing and monitoring plan for higher-dose use, covering ECG/QT surveillance and CYP2C19 considerations
- The approved indication text for the US licenses, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

