---
layout: default
title: Lofexidine
parent: Model Prediction Only (L5)
nav_order: 866
evidence_level: L5
indication_count: 2
---

# Lofexidine
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

# Lofexidine: From Opioid Withdrawal to Migraine Disorder

## One-Sentence Summary

Lofexidine is an oral central alpha-2 adrenergic agonist, used in the US to mitigate opioid withdrawal symptoms.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **1 publication** (a drug news roundup, not a study) on this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mitigation of opioid withdrawal symptoms (general drug knowledge; the license records in the data do not list indication text) |
| Predicted New Indication | Migraine disorder (a second prediction: migraine with brainstem aura, 99.26%) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (1 NDA and 4 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source data. Lofexidine is a central alpha-2 adrenergic agonist and a structural and pharmacological analog of clonidine. Clonidine has been tested for migraine prophylaxis with modest and inconsistent results. A noradrenergic route to migraine modulation is therefore plausible, but speculative.

The TxGNN score of 99.42% is a knowledge-graph prediction only. No lofexidine-specific preclinical or clinical data support it. The missing original MOA also makes the prediction harder to interpret, and the link between opioid withdrawal and migraine is indirect.

The second prediction, migraine with brainstem aura, is likely inherited from the parent migraine disorder node. Any rationale would rest on speculative noradrenergic (locus coeruleus) modulation of brainstem and cortical excitability. The vasoactive and hypotensive effects of alpha-2 agonists could also be a theoretical concern in a subtype with brainstem symptoms.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30580925](https://pubmed.ncbi.nlm.nih.gov/30580925/) | 2019 | Drug news roundup (not a study) | J Am Pharm Assoc | Covers new drug approvals, including lofexidine hydrochloride, alongside baloxavir, fremanezumab and galcanezumab. No abstract is available and there is no migraine efficacy data for lofexidine. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209229 | Lofexidine hydrochloride (Prasco Laboratories) | Tablet, film coated | Not provided in source data |
| ANDA218699 | Lofexidine hydrochloride (Novadoz Pharmaceuticals) | Tablet, film coated | Not provided in source data |
| ANDA218613 | Lofexidine (Indoco Remedies; also listed under Florida Pharmaceutical Products) | Tablet, coated | Not provided in source data |
| ANDA219917 | Lofexidine (ANI Pharmaceuticals) | Tablet | Not provided in source data |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or studies (evidence level L5). The only publication is a news roundup with no relevant data. Clonidine's modest and inconsistent migraine results give only weak indirect support.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required for safety screening
- Mechanism of action data, for example from DrugBank
- Preclinical or clinical evidence for lofexidine in migraine, or a systematic review of alpha-2 agonists (clonidine, guanfacine) in migraine prophylaxis
- An assessment of hypotension and bradycardia risk in a migraine population, particularly for the brainstem aura subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

