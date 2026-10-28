---
layout: default
title: Cyclopentolate
parent: Model Prediction Only (L5)
nav_order: 555
evidence_level: L5
indication_count: 3
monitor_inn: "CYCLOPENTOLATE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
last_modified_at: 2026-10-28
description: "Cyclopentolate: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Cyclopentolate
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

## Cyclopentolate: Cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

Cyclopentolate is an ophthalmic anticholinergic agent, originally used to induce cycloplegia (paralysis of the eye's focusing muscle) for eye examinations.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 5 of 5) |
| Number of NDAs | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cyclopentolate is a muscarinic antagonist (anticholinergic). Its efficacy in producing cycloplegia and pupil dilation when applied to the eye is well established.

The possible link to cauda equina syndrome is bladder dysfunction. Nerve root compression can cause detrusor overactivity or other bladder problems, and antimuscarinic drugs are a recognised class for such symptoms. However, cauda equina syndrome is mainly a surgical emergency caused by nerve root compression, and an anticholinergic would at most address a downstream symptom, not the underlying condition. Cyclopentolate is formulated only as an eye drop, and systemic exposure at therapeutic anticholinergic levels would raise safety concerns. The high TxGNN score is a computational prediction with no clinical or mechanistic data behind it.

Two other predictions were also generated, and both are likewise supported only at the drug-class level:

- **Neurogenic bladder (obsolete ontology term, score 0.9940)**: Antimuscarinics are established for neurogenic detrusor overactivity, but nothing is specific to cyclopentolate. Better-characterised agents (oxybutynin, tolterodine, solifenacin, trospium) already exist. The term should be mapped to current neurogenic lower urinary tract dysfunction terminology before further assessment.
- **Irritable bowel syndrome (score 0.9927)**: Antispasmodics such as dicyclomine and hyoscyamine are used for IBS abdominal pain. Cyclopentolate has no oral formulation, and systemic anticholinergic effects such as constipation could worsen constipation-predominant IBS.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status | Manufacturer |
|---------|------|------|-----------|------|
| ANDA040075 | Cyclopentolate Hydrochloride | Solution/drops | Valid | Bausch & Lomb Incorporated |
| ANDA084110 | Cyclogyl | Solution/drops | Valid | Alcon Laboratories, Inc. |
| ANDA084108 | Cyclogyl | Solution/drops | Valid | Alcon Laboratories, Inc. |
| ANDA084109 | Cyclogyl | Solution/drops | Valid | Alcon Laboratories, Inc. |
| ANDA084300 | Cyclomydril | Solution/drops | Valid | Alcon Laboratories, Inc. |

All five authorizations are valid, and no approved indication text is recorded for them.

## Safety Considerations

- **Disease contraindications from the knowledge graph** (these come from a computational knowledge graph, not from label text): hypertension, diabetes mellitus, diabetic ketoacidosis, benign prostatic hyperplasia, heart disease and cardiovascular disease, coronary artery disease, sudden cardiac arrest, heart conduction disease, angle-closure glaucoma, hyperthyroidism (including Graves disease and thyrotoxicosis), arteriosclerosis and atherosclerosis, brain injury, brain disease, and Down syndrome.
- Several of these conditions (for example benign prostatic hyperplasia and cardiovascular disease) are relevant to the urinary and gastrointestinal uses suggested above, since systemic anticholinergic exposure would be required.

Please refer to the package insert for further warnings, contraindications, and drug interaction information. No interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score and class-level plausibility. No clinical trials or literature exist for cyclopentolate in this indication. Established alternatives already exist for the related bladder and bowel indications.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Mapping of the obsolete neurogenic bladder term to current terminology
- Route-of-administration feasibility assessment, since only ophthalmic forms exist
- Preclinical or mechanistic evidence specific to cyclopentolate in the predicted conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

