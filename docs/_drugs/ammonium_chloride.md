---
layout: default
title: Ammonium Chloride
parent: Model Prediction Only (L5)
nav_order: 332
evidence_level: L5
indication_count: 2
monitor_inn: "AMMONIUM CHLORIDE"
predicted_indications: ["acute laryngopharyngitis", "nasal cavity disease"]
---

# Ammonium Chloride
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

# Ammonium Chloride: From Pharyngitis and Common Cold to Acute Laryngopharyngitis

## One-Sentence Summary

Ammonium chloride was originally associated with upper respiratory conditions such as pharyngitis, the common cold and nasopharyngitis.
The TxGNN model predicts it may be effective for **acute laryngopharyngitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold, nasopharyngitis (from the knowledge graph; no approved indication text is available in the US licence records) |
| Predicted New Indication | Acute laryngopharyngitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ammonium chloride is traditionally used as an expectorant, which could loosen secretions in upper airway inflammation. Its mechanism has not been verified from the data compiled for this report.

The original indications (pharyngitis, common cold, nasopharyngitis) are anatomically and clinically very close to acute laryngopharyngitis. The very high score therefore likely reflects overlap with the existing upper respiratory tract label rather than a genuinely new repurposing signal.

The second-ranked prediction, **nasal cavity disease** (score 99.94%), has the same limitations. It is a broad category overlapping with the common cold and nasopharyngitis, and it is too non-specific to define a trial endpoint or target population. Neither prediction has clinical trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 505G(a)(3) | LRNASH Smelling Salts | Granule | Not stated (cancelled) |
| M011 | Smelling Salt | Inhalant | Not stated (cancelled) |
| No number recorded | Bardown Smelling Salts | Liquid | Not stated (cancelled) |

All three authorizations are cancelled, and all are smelling-salt products rather than products for upper respiratory indications.

## Safety Considerations

- **Disease contraindications (knowledge graph, not label text)**: The knowledge graph links ammonium chloride to contraindications in many conditions. Main groups include:
  - Renal and hepatic: liver failure, impaired renal function, anuria
  - Cardiovascular: hypertension, hypertensive disorder, myocardial ischemia, coronary artery disease, sudden cardiac arrest, heart conduction disease, pulmonary edema
  - Endocrine and metabolic: adrenocortical insufficiency, Addison disease, hyperthyroidism, Graves disease, thyrotoxicosis, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease
  - Neurological and psychiatric: epilepsy, insomnia, anxiety disorder, agoraphobia, obsessive-compulsive disorder
  - Other: peptic ulcer disease, benign prostatic hyperplasia, bladder neck obstruction, ocular hypertension, angle-closure glaucoma, necrotizing enterocolitis
- **Drug Interactions**: 21 interactions were identified, none rated Major.
  - Moderate (5): amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine
  - Minor (16): ephedrine (including nasal), pseudoephedrine, tricyclic antidepressants (amitriptyline, clomipramine, desipramine, doxepin including topical, imipramine, nortriptyline, protriptyline, trimipramine), methadone, mexiletine, flecainide

Package insert warnings and contraindications were not available, so please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is model-derived only (evidence level L5), with no clinical trials or literature. The predicted indication largely overlaps with the existing upper respiratory label, and all US licences are cancelled, which weakens the practical case for development.

**To proceed, the following is needed:**
- Mechanism of action data, to allow assessment of the mechanistic link
- FDA package insert warnings and contraindications, to complete safety screening
- Literature and trial searches for ammonium chloride in laryngopharyngitis and upper airway disease
- A clearer indication definition, particularly for the non-specific "nasal cavity disease" prediction
- Route and formulation compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

