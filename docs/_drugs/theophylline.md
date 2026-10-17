---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 1220
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma, bronchitis, pulmonary emphysema and related airway diseases"
monitor_inn: "THEOPHYLLINE"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Theophylline: From Asthma and Chronic Airway Disease to Thrombotic Disease

## One-Sentence Summary

Theophylline is an oral bronchodilator, originally used for asthma, bronchitis and emphysema.
The TxGNN model predicts it may be effective for **thrombotic disease**, but **0 clinical trials** are registered and none of the **18 retrieved publications** tests theophylline as an antithrombotic. This prediction rests on model output and a plausible mechanism only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, pulmonary emphysema and related airway diseases (the US licence records contain no indication text) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 13 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the compiled drugbank record. Theophylline is a nonselective phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. Its efficacy in airway disease is well established.

Raising cAMP in platelets could, in principle, reduce platelet activation. This would link theophylline to thrombosis, which involves platelet aggregation. The link is plausible but unproven. Adenosine antagonism could act in the opposite direction, because adenosine itself inhibits platelet aggregation.

The retrieved literature does not resolve this question. Most papers concern platelet biomarker assays, the pharmacokinetics of a different antiplatelet drug (ticlopidine), or theophylline detection methods. No paper tests theophylline as an antithrombotic.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The retrieved papers are only loosely related. They are listed below by closeness to the topic.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | In vitro study | General Pharmacology | Milrinone (a different PDE inhibitor) reduced platelet aggregation and raised cAMP, and interacted with adenosine. This is the closest mechanistic parallel, but it does not involve theophylline. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Prostacyclin acts through adenylate cyclase to inhibit platelets. This is background on the cAMP pathway. |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Pharmacokinetic review | Clinical Pharmacokinetics | Concerns ticlopidine, a different antiplatelet drug. Not evidence for theophylline. |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Clinical report | Minerva Cardioangiologica | Haemodynamic and metabolic action of a theophylline nicotinate derivative in chronic obliterating peripheral arteriopathy. It is a different compound, and no abstract was available. |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | Clinical report | Cardiologia Pratica | Cardiocirculatory effects of a theophylline derivative in cerebral and peripheral angiopathies. It is a different compound, and no abstract was available. |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Observational study | Cor et Vasa | T-lymphocyte subsets, identified by theophylline resistance, in vascular disease. Theophylline was used as a laboratory tool, not as treatment. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Assay method | British Journal of Haematology | Theophylline is a component of the anticoagulant used to prepare plasma for platelet factor 4 measurement. |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Methods study | PLoS One | Plasma preparation for platelet-stored molecules. Not a treatment study. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method | Analytica Chimica Acta | An aptasensor for detecting theophylline. Not relevant to efficacy. |

## US Market Information

All 13 US licences for single-ingredient theophylline are cancelled. The five shown below are examples, and none of the records includes indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090430 | Theophylline (Alembic) | Extended-release tablet | Not stated in the data compiled |
| ANDA214806 | Theophylline (Sun Pharmaceutical) | Extended-release tablet | Not stated in the data compiled |
| ANDA206344 | Theophylline (PAI Pharma) | Solution | Not stated in the data compiled |
| ANDA087942 | Theo-24 (Endo) | Extended-release capsule | Not stated in the data compiled |
| ANDA218401 | Theophylline (Ajanta) | Extended-release tablet | Not stated in the data compiled |

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for them. The information below comes from other sources.

- **Knowledge-graph contraindication signals (not label text):** hypertension, liver failure and liver disease, kidney disease, epilepsy, anxiety and other mental disorders (including psychotic disorders), porphyria, hypothyroidism, peptic ulcer disease, open-angle glaucoma, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, thrombocytopenia, neutropenia and agranulocytosis, gallbladder disease, and dermatitis herpetiformis. Thrombocytopenia is especially relevant to any use in thrombotic disease.
- **Drug interactions:** 100 interactions were recorded.
  - **Major:** bupropion.
  - **Moderate:** the H2 blockers famotidine, ranitidine and cimetidine; the proton pump inhibitors omeprazole and rabeprazole; clarithromycin; the tetracyclines doxycycline, tetracycline and minocycline; the corticosteroids hydrocortisone, dexamethasone, betamethasone, triamcinolone and budesonide; activated charcoal; and some bowel preparations.
  - **Minor:** ephedrine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no registered trials and no published study of theophylline as an antithrombotic. The cAMP-based mechanism is plausible, yet adenosine antagonism may work against it. All US licences are cancelled, and the knowledge graph flags thrombocytopenia as a contraindication signal.

**To proceed, the following is needed:**
- Ex vivo or in vitro data on theophylline's effect on platelet aggregation, and a check of whether adenosine antagonism offsets any benefit
- Preclinical thrombosis model data, then early clinical signals
- Package insert warnings and contraindications to complete the safety screen
- Confirmation of current formulation availability, since all US licences are cancelled
- A therapeutic drug monitoring plan, given the interaction burden

**Other predicted indications in the same analysis:**
- **Nasal cavity disease (allergic rhinitis, L3):** a small clinical study and a completed Phase 2 trial (NCT01132781, n=28) exist. This is the most promising true repurposing direction. It is a research question and still needs confirmation.
- **Obstructive lung disease (L1):** this overlaps with theophylline's original indications, so it is confirmation of existing use and not repurposing. Several completed Phase 3 COPD trials exist, including NCT01599871 and NCT02340520.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

