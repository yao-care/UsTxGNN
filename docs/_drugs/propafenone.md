---
layout: default
title: Propafenone
parent: Model Prediction Only (L5)
nav_order: 1090
evidence_level: L5
indication_count: 8
---

# Propafenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Propafenone: From Cardiac Arrhythmia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Propafenone is a class IC antiarrhythmic sodium channel blocker that is marketed in the US as generic tablets and extended-release capsules.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but there are **0 clinical trials** and only **3 publications**, and all three describe adverse effects or drug interactions rather than benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data provided (the literature describes propafenone as an antiarrhythmic) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (no evidence of benefit; the only literature is adverse-effect reports) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Propafenone is a class IC antiarrhythmic, and its established use is in cardiac rhythm disorders. No plausible therapeutic mechanism links it to mania or bipolar disorder.

The high graph score (99.80%) is not supported by clinical data. A 1985 case report describes mania that occurred **secondary to propafenone**. The author speculated that its chemical similarity to bupropion might give it antidepressant-like activity that triggers affective side effects. A 2001 case report describes an organic psychosis from a venlafaxine–propafenone interaction in a bipolar patient. A 2020 review covers interactions between antipsychotics and cardiovascular drugs. Together these point to potential harm rather than benefit, so the prediction is probably a graph artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Review | Pharmacol Rep | Evaluates harmful interactions between antipsychotics and cardiovascular drugs in patients with bipolar disorder or schizophrenia and comorbid cardiovascular disease |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case report | Int J Psychiatry Med | Organic psychosis caused by a venlafaxine–propafenone interaction in a patient with bipolar affective disorder |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case report | J Clin Psychiatry | Mania secondary to propafenone, a previously unrecognized complication |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202445 | Propafenone Hydrochloride (Aurobindo Pharma) | Tablet, film coated | Not specified in source data |
| ANDA213096 | Propafenone Hydrochloride (Aurobindo Pharma) | Capsule, extended release | Not specified in source data |
| ANDA214184 | Propafenone Hydrochloride (Zydus Lifesciences; also Zydus Pharmaceuticals USA) | Capsule, extended release | Not specified in source data |

---

## Safety Considerations

Structured warnings, contraindications and drug interaction data were not available. Please refer to the package insert for safety information.

The retrieved literature adds these signals:
- Propafenone has been associated with new-onset mania (case report, 1985).
- It has been associated with psychosis when combined with venlafaxine (case report, 2001).
- Interactions with antipsychotics are a concern in patients with bipolar disorder and cardiovascular comorbidity (review, 2020).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only retrieved evidence links propafenone to inducing mania and psychosis, not treating them. There are no trials and no plausible mechanism, so the high model score should not drive further investment for this indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking safety data gap)
- Mechanism of action data from DrugBank
- Any prospective evidence of therapeutic benefit in mania, which none of the retrieved papers provide

**Note:** In the same Evidence Pack, catecholaminergic polymorphic ventricular tachycardia (CPVT) is a more biologically plausible candidate. It is supported by preclinical RyR2 studies and a case report of 35 years of effective treatment, and is classed as a "Research Question". It merits a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

