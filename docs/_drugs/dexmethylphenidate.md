---
layout: default
title: Dexmethylphenidate
parent: Model Prediction Only (L5)
nav_order: 595
evidence_level: L5
indication_count: 10
---

# Dexmethylphenidate
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

# Dexmethylphenidate: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

Dexmethylphenidate is a stimulant sold in the US as extended-release capsules and tablets. It is generally used for ADHD, though the license data provided does not list an approved indication.
The TxGNN model predicts it may be effective for **specific developmental disorder**, a broad category that covers learning and motor disorders as well as neurodevelopmental conditions.
Support is thin: **1 indirect clinical trial** (recruiting, no results) and **no publications** for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADHD (inferred from the drug class; no approved indication text in the license data) |
| Predicted New Indication | Specific developmental disorder |
| TxGNN Prediction Score | 99.9997% |
| Evidence Level | L4 (as assigned in the Evidence Pack) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (NDA and ANDA licenses combined) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank field. Based on known pharmacology, dexmethylphenidate is a dopamine/norepinephrine reuptake inhibitor, the class used to treat ADHD, which is a neurodevelopmental disorder.

The link to "specific developmental disorder" is plausible but indirect. That term covers learning and motor disorders, not ADHD alone. The original indication is not confirmed against labeled use, so the mechanistic argument rests on ADHD being a neurodevelopmental condition. It has not been shown for the broader category.

TxGNN scores for the top candidates are all close to 1.0, so the score alone does not separate strong predictions from weak ones.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Phase 4 | Recruiting | 500 | Pragmatic comparative-effectiveness trial in children and adolescents with ADHD and autism spectrum disorder. It compares methylphenidate and amphetamine, and also tests alpha-2 agonists, using a sequential, multiple assignment randomization (SMART) design. No results yet. Whether dexmethylphenidate is an arm is unconfirmed, and the population is ADHD in autism rather than the predicted disease, so this is indirect support only. |

## Literature Evidence

Currently no related literature available.

## US Market Information

The license records provided do not include approved-indication text, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA215523 | Dexmethylphenidate Hydrochloride | Capsule, extended release | Camber Pharmaceuticals, Inc. |
| NDA021802 | Focalin | Capsule, extended release | Sandoz Inc |
| ANDA213813 | Dexmethylphenidate Hydrochloride | Capsule, extended release | Granules Pharmaceuticals Inc. |
| ANDA210279 | Dexmethylphenidate Hydrochloride | Capsule, extended release | Lannett Company, Inc. |
| ANDA212631 | Dexmethylphenidate Hydrochloride | Tablet | Ascend Laboratories, LLC |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting study is a recruiting Phase 4 trial that does not clearly include dexmethylphenidate and targets ADHD in autism rather than the predicted category. There is no literature, and the package-insert safety data is missing, which blocks safety screening. This is best treated as a research question, not a development candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap)
- Mechanism-of-action data from DrugBank and the approved indication text from the labels
- Narrowing "specific developmental disorder" to a concrete condition, such as ADHD in autism, a specific learning disorder, or a motor disorder
- Confirmation of whether dexmethylphenidate is an arm in NCT05916339, and its results when available
- Literature review for the narrowed indication

Other predictions in the pack are weaker. Most have no trials or literature, and manic bipolar disorder has only indirect reviews on stimulants in comorbid ADHD.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

