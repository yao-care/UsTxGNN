---
layout: default
title: Dronabinol
parent: Moderate Evidence (L3-L4)
nav_order: 628
evidence_level: L3
indication_count: 9
monitor_inn: "DRONABINOL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "headache disorder", "trigeminal autonomic cephalalgia", "pulmonary hypertension", "hypertrichosis (disease)", "kyphoscoliotic heart disease", "Ambras type hypertrichosis universalis congenita", "atrophoderma vermiculata"]
last_modified_at: 2026-10-28
description: "Dronabinol: predicted new indication Migraine disorder (evidence level L3). Approved use: Not recorded in the local data"
---

# Dronabinol
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **9** 
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

## Dronabinol: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Dronabinol is a synthetic delta-9-tetrahydrocannabinol (THC). The data compiled for this report do not list its original approved indication.
The TxGNN model predicts it may be effective for **migraine disorder**, with **1 completed Phase 2 clinical trial (no results available)** and **1 publication (a survey)** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L3 |
| US Market Status | Marketed (valid licenses on record: at least 4) |
| Number of NDAs | 4 authorizations (2 NDAs, 2 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known pharmacology, dronabinol is a CB1/CB2 cannabinoid receptor agonist.

The endocannabinoid system is thought to modulate trigeminovascular pain signalling, serotonergic signalling and CGRP release. These are all pathways involved in migraine, which provides a plausible mechanistic basis for the prediction.

The very high TxGNN score (0.9992) is consistent with this reasoning, but it is a computational prediction only. The relationship between the original indication and migraine cannot be assessed because the original indication is missing from the data.

Related predictions in the same area include headache disorder (0.9987), trigeminal autonomic cephalalgia (0.9979) and migraine with brainstem aura (0.9989). Some other top-ranked predictions, such as pulmonary hypertension, hypertrichosis and kyphoscoliotic heart disease, have no supporting evidence and no plausible mechanism. They are most likely network artifacts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00123201](https://clinicaltrials.gov/study/NCT00123201) | Phase 2 | Completed | Not reported | Multicenter, randomized, double-blind, placebo-controlled trial of dronabinol MDI (metered-dose inhaler) for acute treatment of moderate to severe migraine headache (2005-09 to 2007-03). No results are available. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10575286](https://pubmed.ncbi.nlm.nih.gov/10575286/) | 1999 | Survey | Forschende Komplementarmedizin | Standardized survey on the medical use of cannabis products in German-speaking countries. It is a general survey, not migraine-specific efficacy evidence. |

Additional literature relates to the broader headache prediction. These are a 2017 review on cannabis for pain and headaches ([28281107](https://pubmed.ncbi.nlm.nih.gov/28281107/)) and a 2009 case report of cluster headache responding to dronabinol ([19220500](https://pubmed.ncbi.nlm.nih.gov/19220500/)). Both are low-level evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018651 | Dronabinol (Major Pharmaceuticals) | Capsule | Not available (valid) |
| ANDA078292 | Dronabinol (Rhodes Pharmaceuticals) | Capsule | Not available (valid) |
| NDA205525 | SYNDROS (Benuvia Operations) | Solution | Not available (valid) |
| ANDA207421 | Dronabinol (Camber Pharmaceuticals) | Capsule | Not available (valid) |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): hypertension and hypertensive disorder, hypotensive disorder, epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, bipolar disorder, major affective disorder, schizophrenia, substance abuse/dependence and substance-related disorder.
- **Drug Interactions**: 100 interactions were identified. Most are Moderate. The one Major interaction in the listed sample is **tramadol**. Other Moderate interactions include fentanyl, codeine, dihydrocodeine, alfentanil, ethanol, butalbital, chlorpheniramine, gabapentin, fluvoxamine, nifedipine, furosemide and fosphenytoin. Many of these involve additive central nervous system depression.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial is a completed Phase 2 study with no available results or enrollment data, and the literature consists of a survey, a review and a case report. The original indication and label safety data are missing, and the drug is marketed in the US with 4 valid licenses. The mechanistic rationale is plausible, but the evidence is too weak to advance beyond a research question.

**To proceed, the following is needed:**
- Results of NCT00123201 (efficacy, safety and enrollment), from the registry or publications
- FDA package insert warnings and contraindications, and the original approved indication
- Mechanism of action data confirmed from DrugBank
- An assessment of the knowledge-graph contraindication signals (cardiovascular and psychiatric) in a migraine population
- A review of the route of administration, since the trial used an inhaler while the US products were oral capsules and solution
- Clarification of why the US authorizations were cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

