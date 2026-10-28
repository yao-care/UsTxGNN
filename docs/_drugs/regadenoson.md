---
layout: default
title: Regadenoson
parent: Model Prediction Only (L5)
nav_order: 1114
evidence_level: L5
indication_count: 4
monitor_inn: "REGADENOSON"
predicted_indications: ["anaphylaxis", "food-dependent exercise-induced anaphylaxis", "esotropia", "pseudoallergy"]
last_modified_at: 2026-10-28
description: "Regadenoson: predicted new indication Anaphylaxis (evidence level L5). Approved use: Diagnostic agent for radionuclide myocardial perfusion imaging (MPI)"
---

# Regadenoson
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Regadenoson: From Diagnostic Pharmacologic Stress Agent to Anaphylaxis
{: .text-alpha }

## One-Sentence Summary

Regadenoson is a selective A2A adenosine receptor agonist, used as a diagnostic agent for radionuclide myocardial perfusion imaging (MPI).
The TxGNN model predicts it may be relevant to **anaphylaxis**, but **no clinical trials** and **no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic agent for radionuclide myocardial perfusion imaging (MPI) (the data compiled for this report contains no approved-indication text on the licenses; this is taken from pharmacology data) |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 12 of 12) |
| Number of NDAs | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Regadenoson is a selective A2A adenosine receptor agonist (it also binds A1, A2B and A3 receptors). Detailed mechanism-of-action text is not available in the data compiled for this report, but receptor binding data confirm that it acts on adenosine receptors. In preclinical models, A2A signaling generally has anti-inflammatory and mast cell-stabilizing effects, which offers a theoretical link to allergic reactions.

However, the prediction is weak from a clinical standpoint. Regadenoson causes vasodilation and hypotension, whereas anaphylaxis requires rapid vasopressor support such as epinephrine. A vasodilator would be expected to worsen, not treat, anaphylactic shock. Regadenoson itself also carries rare hypersensitivity warnings. The high TxGNN score is a purely computational result and is not backed by any clinical or literature data.

**Other predictions in the list (all L5, all Hold):**

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Food-dependent exercise-induced anaphylaxis | 0.9974 | The only plausible rationale is A2A modulation of mast cell activation. Its hemodynamic effects (vasodilation, tachycardia, hypotension) and use as a stress agent make it unsuitable for a condition triggered by exercise plus food. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| 3 | Esotropia | 0.9912 | No clear mechanistic link to ocular alignment disorders. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| 4 | Pseudoallergy | 0.9912 | A2A agonism could theoretically dampen mast cell degranulation, but this is speculative. Regadenoson's own flushing and hypersensitivity-like reactions argue for caution. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 12 licenses are valid. Approved-indication text is not available for any of them. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022161 | LEXISCAN (Astellas Pharma US, Inc.) | Injection, solution | Not available (status: valid) |
| ANDA213210 | Regadenoson (Dr. Reddy's Laboratories Inc.) | Injection | Not available (status: valid) |
| ANDA218054 | Regadenoson (Marlex Pharmaceuticals, Inc.) | Injection, solution | Not available (status: valid) |
| ANDA216437 | Regadenoson (Eugia US LLC) | Injection | Not available (status: valid) |
| ANDA207604 | Regadenoson (Apotex Corp.) | Injection, solution | Not available (status: valid) |

The remaining seven ANDAs (International Medication Systems, Hikma, Baxter, Gland Pharma, Accord, Meitheal, Hospira) are also cancelled. All products are injectable.

## Safety Considerations

- **Disease contraindications from the knowledge graph** (these come from drug-disease contraindication edges in the TxGNN knowledge graph, not from label text). Listed conditions include:
  - Cardiovascular: hypertension, hypotensive disorder, aortic stenosis and related valve disease, mitral valve stenosis, atrioventricular block, sick sinus syndrome, coronary artery disease, pericarditis, pericardial effusion, carotid stenosis and carotid artery thrombosis, transient ischemic attack, vertebrobasilar insufficiency
  - Respiratory: asthma (including allergic and intrinsic forms), chronic obstructive pulmonary disease, bronchial disease
  - Neurological: epilepsy, autonomic nervous system disease, Horner syndrome
- **Drug Interactions** (10 records found):
  - Moderate-level interactions (DDInter) with caffeine, dipyridamole, dyphylline, theophylline, aminophylline and oxtriphylline. Methylxanthines and dipyridamole act on the adenosine pathway and may alter the effect of regadenoson.
  - Pharmacology data show binding to A1, A2A, A2B and A3 adenosine receptors.
- **Other considerations**: Regadenoson causes vasodilation, hypotension, tachycardia and flushing, and rare hypersensitivity reactions have been noted. These effects are especially relevant to anaphylaxis-related indications.

Please refer to the package insert for official warnings and contraindications, as label text was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score (L5). No trials or publications exist, and the drug's vasodilatory and hypotensive effects work against the treatment needs of anaphylaxis. All 12 US licenses are valid.

**To proceed, the following is needed:**
- Preclinical evidence that A2A agonism can control mast cell activation or anaphylaxis without causing harmful hypotension
- FDA package insert warnings and contraindications for formal safety screening
- Detailed mechanism-of-action data
- Clarification of the regulatory status of the 12 valid US licenses
- Literature and trial searches that could support any of the four predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

