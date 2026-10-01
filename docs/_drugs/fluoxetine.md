---
layout: default
title: Fluoxetine
parent: Model Prediction Only (L5)
nav_order: 724
evidence_level: L5
indication_count: 10
---

# Fluoxetine
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

# Fluoxetine: From Depression to Histrionic Personality Disorder

## One-Sentence Summary

Fluoxetine is a selective serotonin reuptake inhibitor (SSRI) antidepressant that is widely marketed in the US.
The TxGNN model predicts it may be effective for **histrionic personality disorder** (score 99.92%), but there are **0 clinical trials** and only **3 loosely related publications**, none specific to this condition.
This is a model-only prediction and is not supported by disease-specific evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (from the literature in the pack; the US label text in the pack is blank) |
| Predicted New Indication | Histrionic personality disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general SSRI pharmacology, fluoxetine blocks the serotonin transporter (SERT). Over time this increases serotonergic signalling and leads to downstream receptor adaptation.

Histrionic personality disorder is characterised by emotional lability, attention-seeking and impulsivity. A serotonergic drug might plausibly dampen affective lability and impulsivity, which is the only link between this drug and the prediction.

This is an extrapolation. No histrionic-specific data support it, and any benefit would more likely come from treating comorbid depression or anxiety than from changing the personality pattern itself. The high score may partly reflect graph-neighbourhood effects in the knowledge graph rather than a true biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22075735](https://pubmed.ncbi.nlm.nih.gov/22075735/) | 2011 | Cohort | Psychiatria Danubina | Links MMPI-2 neurotic-triad scores (hypochondria, depression, hysteria) to depression levels after drug treatment in depressive disorders. It does not study histrionic personality disorder. |
| [11865567](https://pubmed.ncbi.nlm.nih.gov/11865567/) | 2001 | Review / case report | L'Encephale | Psychiatric manifestations of lupus and Sjögren's syndrome, treated with cyclophosphamide. Not relevant to fluoxetine. |
| [28791577](https://pubmed.ncbi.nlm.nih.gov/28791577/) | 2018 | Case report | Neuropsychiatrie | A case of body dysmorphic disorder with an eating disorder. Not relevant to fluoxetine for this indication. |

All three papers are only tangentially related (psychiatric comorbidity or personality-related topics). None tests fluoxetine in histrionic personality disorder.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA078619 | Fluoxetine | Capsule | Aurobindo Pharma Limited |
| ANDA078619 | Fluoxetine | Capsule | Bryant Ranch Prepack |
| ANDA078619 | Fluoxetine | Capsule | NorthStar Rx LLC |
| ANDA078619 | Fluoxetine | Capsule | Major Pharmaceuticals |
| ANDA078619 | Fluoxetine | Capsule | American Health Packaging |

The record lists 20 licenses in total. Marketed dosage forms are capsule, tablet (including coated and film-coated) and solution, all oral. Approved indication text is not included in the source record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials and no publications that test fluoxetine in histrionic personality disorder. The mechanistic link is speculative, so this is a hypothesis only.

Other predicted indications for fluoxetine have much stronger support. Agoraphobia and melancholia are both graded L2 with a "Proceed with Guardrails" recommendation, and are better candidates to prioritise.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Disease-specific studies of SSRIs in histrionic personality disorder, such as a systematic literature review or a pilot trial
- A drug interaction check, since no interaction data were found

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

