---
layout: default
title: Pegvaliase
parent: Model Prediction Only (L5)
nav_order: 1023
evidence_level: L5
indication_count: 3
monitor_inn: "PEGVALIASE"
predicted_indications: ["diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "diabetic cataract"]
last_modified_at: 2026-10-30
description: "Pegvaliase: predicted new indication Diabetic retinopathy (evidence level L5). Approved use: Not available in the compiled data (the label text is blank"
---

# Pegvaliase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pegvaliase: From Phenylketonuria to Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Pegvaliase is a PEGylated phenylalanine ammonia lyase enzyme therapy, marketed in the US as Palynziq. It is generally used to lower phenylalanine in phenylketonuria, but the label indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **diabetic retinopathy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the label text is blank; phenylketonuria is the generally known use) |
| Predicted New Indication | Diabetic retinopathy |
| TxGNN Prediction Score | 0.9917 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

Two other predicted indications are closely related diabetic eye conditions with nearly identical scores: severe nonproliferative diabetic retinopathy (0.9916) and diabetic cataract (0.9911). All three also have no trials or literature.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, pegvaliase is a PEGylated phenylalanine ammonia lyase that degrades phenylalanine, and it is used in phenylketonuria.

The data does not support a mechanistic link to diabetic retinopathy. This condition is a microvascular complication driven mainly by hyperglycemia, VEGF signaling, and inflammation, and pegvaliase has no known action on these pathways. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. A speculative connection through amino acid metabolism could be imagined, but nothing in the evidence supports it.

The three predicted indications (diabetic retinopathy, its severe nonproliferative subtype, and diabetic cataract) are closely related and have nearly identical scores. This suggests a single correlated signal from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, rather than three independent lines of evidence. Diabetic cataract is linked to polyol pathway activity, oxidative stress, and lens glycation, and pegvaliase has no known action on these processes either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761079 (cancelled) | Palynziq (BioMarin Pharmaceutical Inc.) | Injection, solution | Not available |

## Safety Considerations

- **Drug Interactions**: 16 moderate-level interactions were identified, all from DDInter. They fall mainly among PEGylated products and a few other agents:
  - PEGylated biologics: certolizumab pegol, pegaptanib (ophthalmic), pegloticase, pegademase, pegaspargase, pegfilgrastim, peginesatide, peginterferon alfa-2a, peginterferon alfa-2b, peginterferon beta-1a, pegvisomant
  - Others: antihemophilic factor (human recombinant), coagulation factor IX human, liposomal doxorubicin, medroxyprogesterone acetate, naloxegol
- **Other considerations**: The supporting analysis notes that pegvaliase carries a boxed warning for anaphylaxis and requires REMS-type risk management. This would weigh heavily in any benefit-risk assessment for a non-life-threatening eye indication.

Please refer to the package insert for the remaining safety information (warnings and contraindications).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score, with no clinical trials, no publications, and no supported mechanism (Evidence Level L5). Pegvaliase also has a serious anaphylaxis risk. The drug is marketed in the US, with 1 valid licence out of 1.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data, and a plausible biological rationale linking phenylalanine degradation to diabetic retinopathy
- Preclinical or mechanistic studies in retinal or diabetic models
- Clarification of the regulatory status of the cancelled BLA and its approved indication text
- A benefit-risk assessment against existing diabetic retinopathy therapies, given the anaphylaxis risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

