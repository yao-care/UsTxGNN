---
layout: default
title: Entacapone
parent: Model Prediction Only (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Entacapone: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease (and related genetic parkinsonian syndromes)"
monitor_inn: "ENTACAPONE"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
---

# Entacapone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Entacapone: From Parkinson Disease to PLA2G6-Associated Neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Entacapone is a COMT inhibitor originally used as an add-on treatment in Parkinson disease and several related genetic parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (and related genetic parkinsonian syndromes) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 6 of 6) |
| Number of NDAs | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, entacapone inhibits catechol-O-methyltransferase (COMT). This extends the action of levodopa and supports dopaminergic signalling in Parkinson disease.

PLA2G6-associated neurodegeneration includes infantile neuroaxonal dystrophy and PLA2G6-related dystonia-parkinsonism. In the parkinsonian form, a COMT inhibitor could plausibly modulate dopaminergic signalling. However, this would be symptomatic at best. It would not address the underlying phospholipase defect.

The score is high, but the link is indirect. No studies were found that test entacapone in this condition.

Other predictions in the list vary in plausibility:
- **Closest to the original indication:** juvenile parkinsonism (paralysis agitans, juvenile, of Hunt; score 0.9960) and Lewy body dementia (0.9925). Both share dopaminergic or alpha-synuclein biology with Parkinson disease. Both are rated L4 (research question).
- **Weak or no mechanistic link:** Rasmussen encephalitis, myelitis, transaldolase deficiency, fructose-1,6-bisphosphatase deficiency, lethal infantile mitochondrial myopathy, and a polymicrogyria syndrome. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Limited rationale:** progressive supranuclear palsy-corticobasal syndrome. These atypical parkinsonian tauopathies respond poorly to levodopa, which weakens the case for a levodopa-extending drug.

## Clinical Trial Evidence

Currently no related clinical trials are registered for PLA2G6-associated neurodegeneration.

For the other predicted indications, only two loosely related studies were found. Neither tests entacapone as a treatment:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [18F]F-DOPA PET imaging in autonomic failure (alpha-synucleinopathies). Entacapone may serve as a tool to modify tracer kinetics. The study is diagnostic and does not evaluate efficacy in Lewy body dementia. |
| [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) | N/A | Active, not recruiting | 120 | Observational gait pattern analysis in neurological disease, including parkinsonian disorders. Does not evaluate entacapone. |

## Literature Evidence

Currently no related literature is available for PLA2G6-associated neurodegeneration.

Two preclinical publications relate to the Lewy body dementia prediction (rank 7):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preclinical (iPSC organoid model) | Science Advances | Cortical organoids with SNCA triplication reproduced alpha-synuclein pathology in Lewy body disease and were used to identify candidate therapeutic drugs. |
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | In vitro study | J Neurosci Res | Examined the effects of antiparkinsonian agents on β-amyloid and alpha-synuclein oligomer formation. Indirect and preclinical. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020796 | Entacapone (Aphena Pharma Solutions) | Tablet, film coated | Not specified; valid |
| ANDA203437 | Entacapone (Major Pharmaceuticals) | Tablet, film coated | Not specified; valid |
| ANDA212601 | Entacapone (Alembic Pharmaceuticals) | Tablet, film coated | Not specified; valid |
| ANDA205792 | Entacapone (Ajanta Pharma USA) | Tablet | Not specified; valid |
| ANDA207210 | Entacapone (Macleods Pharmaceuticals) | Tablet | Not specified; valid |

One further cancelled license is not shown: ANDA206669 (Lannett Company, tablet, film coated). All six licenses are for oral tablets and all are cancelled.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are graph-derived associations, not package insert text): multiple system atrophy, orthostatic hypotension, postural orthostatic tachycardia syndrome, drug-induced dyskinesia, epilepsy, peptic ulcer disease, anxiety and other mental disorders (including psychotic disorders and schizophreniform and schizoaffective disorders), kidney disease, liver disease, gallbladder disease, open-angle and angle-closure glaucoma, diabetes mellitus and diabetic ketoacidosis, melanoma, myocardial infarction and coronary thrombosis, sudden cardiac arrest, heart conduction disease, hemoglobinopathy, and diarrheal disease.
- **Drug interactions:** 82 interactions are recorded. The 10 listed as Moderate are:
  - epinephrine (systemic, ophthalmic and topical forms)
  - morphine (including liposomal)
  - opium
  - dronabinol
  - nabilone
  - metoclopramide
  - iron
  
  Others, such as pantoprazole, omeprazole, lansoprazole, doxycycline, metformin, atropine, lactulose, prednisone, simvastatin and potassium chloride, have an unclassified (Unknown) severity level.
- **Additional consideration:** hepatotoxicity concerns exist for the related COMT inhibitor tolcapone. This is relevant if entacapone is considered in mitochondrial or liver-involving diseases.

Please refer to the package insert for the official warnings and contraindications, as label text was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for PLA2G6-associated neurodegeneration rests on model score alone (L5). No trials or literature exist, and a COMT inhibitor would at most give symptomatic benefit in the parkinsonian phenotype. The drug is marketed in the US, with 6 of 6 licenses valid.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical or case-level evidence of entacapone in PLA2G6-related dystonia-parkinsonism
- Consideration of the juvenile parkinsonism and Lewy body dementia predictions as research questions, since both are closer to the approved indication
- Clarification of the regulatory and supply situation (6 of 6 US licenses are valid)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

