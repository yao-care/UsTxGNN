---
layout: default
title: Pentobarbital
parent: Model Prediction Only (L5)
nav_order: 1028
evidence_level: L5
indication_count: 10
---

# Pentobarbital
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

# Pentobarbital: From Sedative-Hypnotic to Obesity Disorder

## One-Sentence Summary

Pentobarbital is a barbiturate that enhances GABA-A receptor signaling and is marketed in the US as an injectable solution. The TxGNN model predicts it may be useful for **obesity disorder**, but this rests on a graph-based score alone: **1 clinical trial** was retrieved, and it is a pharmacokinetic study that does not test obesity. The **19 publications** retrieved mostly use pentobarbital as an anesthetic in animal obesity models rather than as a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Obesity disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both ANDAs) |
| Recommended Decision | Hold |

The source data does not include approved indication text for either license, so the original indication is not listed here.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank field. Pentobarbital is a GABA-A receptor positive modulator with sedative-hypnotic effects.

No credible mechanistic link to obesity was identified. The retrieved papers use pentobarbital as an anesthetic or sedative tool in rodent, rabbit and chicken obesity models, for example to anesthetize animals before surgery or perfusion. None tests pentobarbital as an obesity therapy. The high TxGNN score (0.9999) is a graph-based prediction only and should not be read as clinical support.

Barbiturate risks also weigh against pursuing this direction: dependence, respiratory depression and a narrow therapeutic index.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3,520 | Pharmacokinetics of understudied drugs given to children as standard of care. It is not an obesity efficacy trial, and pentobarbital's role and any obesity relevance are unclear (relevance grade C). |

## Literature Evidence

No randomized controlled trials were found. The 10 most relevant of 19 retrieved publications are listed below; none evaluates pentobarbital as an obesity treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [5694866](https://pubmed.ncbi.nlm.nih.gov/5694866/) | 1968 | Review | JAMA | Anesthesia considerations in obese patients (no abstract available). |
| [4983481](https://pubmed.ncbi.nlm.nih.gov/4983481/) | 1970 | Clinical report | Curr Ther Res | Overweight relapse: effects of training and methamphetamine with pentobarbital (no abstract available). |
| [34072024](https://pubmed.ncbi.nlm.nih.gov/34072024/) | 2021 | Preclinical | Molecules | Brazil nut seed extract reduced anxiety-like behavior, lipids and overweight in mice; pentobarbital was used only as a hypnosis test. |
| [34445005](https://pubmed.ncbi.nlm.nih.gov/34445005/) | 2021 | Preclinical | Nutrients | Garcinia cambogia peel extract had an arousal effect in the pentobarbital sleep test. |
| [19321699](https://pubmed.ncbi.nlm.nih.gov/19321699/) | 2009 | Preclinical | Am J Physiol Regul Integr Comp Physiol | Renal nerve responsiveness in fat-fed rabbits, studied under pentobarbital anesthesia. |
| [28347670](https://pubmed.ncbi.nlm.nih.gov/28347670/) | 2017 | Preclinical | Brain Res | Oral leptin-mimetic peptides localized in the mouse hypothalamus; pentobarbital was used only for terminal perfusion. |
| [30679938](https://pubmed.ncbi.nlm.nih.gov/30679938/) | 2019 | Preclinical | Nutr Metab | Smilax china extract reduced lipid accumulation in high-fat-diet mice via AMPK. |
| [9145938](https://pubmed.ncbi.nlm.nih.gov/9145938/) | 1997 | Preclinical | Physiol Behav | Ventromedial hypothalamus lesions reduced post-meal thermogenesis in rats; pentobarbital was the surgical anesthetic. |
| [15893702](https://pubmed.ncbi.nlm.nih.gov/15893702/) | 2005 | Preclinical | Auton Neurosci | Gastric electrical stimulation modulated neuronal activity in rats, in animals anesthetized with pentobarbital. |
| [7649094](https://pubmed.ncbi.nlm.nih.gov/7649094/) | 1995 | Preclinical | Endocrinology | Insulin turnover in lean and obese Zucker rats under pentobarbital anesthesia. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA206404 | pentobarbital sodium | Injection, solution | Sagent Pharmaceuticals |
| ANDA203619 | Pentobarbital Sodium | Injection, solution | Hikma Pharmaceuticals USA Inc. (dba Leucadia Pharmaceuticals) |

Approved indication text was not provided for either license. Both products are injectable only.

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source (0 entries).

Please refer to the package insert for warnings and contraindications. That information was not available in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The obesity prediction is supported only by a graph-model score. The single trial is a pediatric pharmacokinetic study unrelated to obesity, and the literature uses pentobarbital as a laboratory anesthetic rather than a therapy. Its dependence and respiratory-depression risks make a weight-management use unattractive.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which block any safety screening.
- Original indication text from the current labels.
- Mechanistic data (DrugBank MOA) and any direct evidence of pentobarbital affecting body weight or energy balance.

**Other predictions:** Among the other nine predicted indications, only *sleep disorder, initiating and maintaining sleep* (rank 5, L4) has a biologically coherent rationale. It may already be a labeled sedative-hypnotic use rather than a true repurposing, so check it against the current label. The literature retrieved for it consists of rodent screening studies of other compounds, not evidence about pentobarbital itself.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

