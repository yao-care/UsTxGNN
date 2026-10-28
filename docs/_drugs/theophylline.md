---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 1220
evidence_level: L5
indication_count: 6
monitor_inn: "THEOPHYLLINE"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-23
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma"
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Theophylline: From Asthma to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Theophylline is a bronchodilator originally used for asthma and other chronic airway diseases.
The TxGNN model predicts it may be effective for **thrombotic disease**,
but **no clinical trials** and **no publications that directly study theophylline in this disease** are currently available, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (other relations recorded in the knowledge graph: bronchitis, pulmonary emphysema, bronchial disease) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 13) |
| Number of NDAs | at least 13 |
| Number of approvals | At least 13 ANDAs (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, theophylline is a non-selective phosphodiesterase inhibitor and an adenosine receptor antagonist.

In theory, raising cAMP in platelets could inhibit platelet aggregation, which gives a plausible but unproven link between an airway drug and thrombosis. However, adenosine antagonism could offset this effect, and no clinical data support an antithrombotic benefit. The high TxGNN score is therefore not backed by clinical evidence.

Note that the asthma and related airway uses listed above are relations recorded in the knowledge graph; the licence records compiled for this report contain no approved-indication text.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the retrieved papers tests theophylline as a treatment for thrombotic disease. The items below are the closest by topic and are mostly reviews, laboratory methods or papers on other drugs.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clin Pharmacokinet | Pharmacokinetics of ticlopidine, an antiplatelet drug (not theophylline) |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Prostaglandins, platelets and atherosclerosis; prostacyclin acts through adenylate cyclase/cAMP in platelets |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | Gen Pharmacol | Milrinone and adenosine inhibit human platelet response via cAMP (not theophylline) |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Methods | Br J Haematol | Platelet factor 4 radioimmunoassay; theophylline used only as a component of the anticoagulant solution |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Methods | Platelets | Measurement of soluble CLEC-2 as a platelet activation marker |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohort | Inflamm Bowel Dis | Platelet-leukocyte aggregates in inflammatory bowel disease |
| [19897460](https://pubmed.ncbi.nlm.nih.gov/19897460/) | 2010 | Clinical study | Heart | Myocardial ischaemia and platelet reactivity in coronary artery disease |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical methods | Anal Chim Acta | Aptasensor for theophylline detection; confirms use for asthma, bronchitis and emphysema |

## US Market Information

Theophylline is marketed in the US as single-ingredient products. The records compiled for this report list 13 ANDAs, and the list may be partial. The records contain no approved-indication text. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090430 | Theophylline (Alembic) | Extended-release tablet | Not stated in the records |
| ANDA214806 | Theophylline (Sun Pharmaceutical) | Extended-release tablet | Not stated in the records |
| ANDA206344 | Theophylline (PAI Pharma) | Solution | Not stated in the records |
| ANDA087942 | Theo-24 (Endo) | Extended-release capsule | Not stated in the records |
| ANDA089763 | Theophylline (Chartwell RX) | Extended-release tablet | Not stated in the records |

## Safety Considerations

No label warnings or contraindications were available in the data compiled for this report. Please refer to the package insert for these.

**Contraindication relations recorded in the knowledge graph** (not label text): hypertension, liver failure and liver disease, epilepsy, anxiety and other mental disorders, porphyria, kidney disease, thrombocytopenia, hypothyroidism, peptic ulcer disease, open-angle glaucoma, diabetes and diabetic ketoacidosis, benign prostatic hyperplasia, neutropenia and agranulocytosis. Thrombocytopenia is relevant to a thrombosis setting.

**Drug interactions** (100 recorded; the main ones are shown):
- **Major**: bupropion
- **Moderate**: cimetidine, famotidine, ranitidine, omeprazole, rabeprazole, clarithromycin, doxycycline, minocycline, tetracycline, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), activated charcoal
- **Minor**: ephedrine

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9962), but there are no registered clinical trials and no study that directly tests theophylline against thrombotic disease. The mechanistic link (cAMP-mediated platelet inhibition) is only theoretical and may be offset by adenosine antagonism, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a focused platelet-function or antithrombotic study of theophylline
- Label warnings and contraindications from the FDA package insert, which are currently missing
- A safety review of the narrow therapeutic window and the interaction burden in patients likely to be on antithrombotic therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

