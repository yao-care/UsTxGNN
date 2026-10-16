---
layout: default
title: Phentermine
parent: Model Prediction Only (L5)
nav_order: 1040
evidence_level: L5
indication_count: 4
monitor_inn: "PHENTERMINE"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny"]
---

# Phentermine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Phentermine: From Obesity to Hypervitaminosis

## One-Sentence Summary

Phentermine is a sympathomimetic appetite suppressant, originally used for obesity and related conditions (hypotensive disorder, monogenic obesity).
The TxGNN model predicts it may be effective for **Hypervitaminosis**,
but **0 clinical trials** and **0 publications** currently support this prediction, and no plausible pharmacological rationale has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder (hypotensive disorder and monogenic obesity are also listed as original indications; no approved indication text is available in the US license data) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 11 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, phentermine is a sympathomimetic amine that promotes norepinephrine release and suppresses appetite. Its use in obesity is well established.

However, hypervitaminosis results from excess vitamin intake or accumulation, and appetite suppression does not address it. No plausible mechanistic link was identified, and the high TxGNN score (99.57%) appears to be a graph-based prediction without pharmacological support. It should be treated as a hypothesis-generating signal only.

Other predictions from the model fall into two groups:
- **Proximal 16p11.2 microdeletion syndrome** (99.49%): This is an indirect and speculative link. The syndrome is associated with severe early-onset obesity, so symptomatic weight management is conceptually plausible, and this likely reflects the original monogenic obesity indication. The drug would treat only the obesity phenotype, not the underlying genetic disorder. Neurodevelopmental, cardiovascular and psychiatric comorbidities raise safety concerns for a stimulant.
- **Obsolete hypertelorism (disease)** (99.41%) and **frontorhiny** (99.04%): These are craniofacial structural anomalies with no mechanistic link. The first term is obsolete in the ontology, so its prediction may be an artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 11 US authorizations for phentermine hydrochloride are cancelled, and no approved indication text is available for them. Five of them are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA205019 | Phentermine Hydrochloride (Bryant Ranch Prepack) | Capsule | Not available |
| ANDA205008 | Phentermine Hydrochloride (Proficient Rx LP) | Tablet | Not available |
| ANDA202248 | Phentermine Hydrochloride (Bryant Ranch Prepack) | Capsule | Not available |
| ANDA040887 | Phentermine Hydrochloride (PD-Rx Pharmaceuticals) | Capsule | Not available |
| ANDA203436 | Phentermine Hydrochloride (KVK-TECH) | Tablet | Not available |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: Hypertension and hypertensive disorder, congestive heart failure, pulmonary hypertension, cardiovascular and heart disease, heart valve disease, heart conduction disease, sudden cardiac arrest, arteriosclerosis obliterans, psychotic and other mental disorders (schizophreniform and schizoaffective disorder), substance abuse/dependence, type 1 diabetes and diabetic ketoacidosis, glaucoma, hyperthyroidism (Graves disease, thyrotoxicosis), and preeclampsia.
- **Drug Interactions**: 100 interactions were found. Major interactions include **tramadol**, **bupropion** and **methylene blue**. Moderate interactions include other sympathomimetics (phenylephrine, pseudoephedrine, epinephrine, isometheptene), beta-agonists (salbutamol, formoterol, arformoterol), opioids (fentanyl, alfentanil), antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, albiglutide), amitriptyline, amifampridine and ethanol.

Please refer to the package insert for official warnings and contraindications, as label data was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials or literature, and no plausible mechanism links appetite suppression to hypervitaminosis. All US licenses are cancelled, and the drug's cardiovascular and psychiatric safety profile adds further caution.

**To proceed, the following is needed:**
- A documented mechanistic rationale for hypervitaminosis (or confirmation that the prediction is a graph artifact)
- Mechanism of action data for phentermine
- FDA package insert warnings and contraindications for safety screening
- Any supporting preclinical or clinical evidence
- If the 16p11.2 microdeletion syndrome direction is pursued instead, a dedicated cardiovascular and neuropsychiatric safety assessment for a stimulant in that population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

