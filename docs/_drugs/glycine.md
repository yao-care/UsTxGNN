---
layout: default
title: Glycine
parent: Model Prediction Only (L5)
nav_order: 757
evidence_level: L5
indication_count: 2
monitor_inn: "GLYCINE"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis"]
last_modified_at: 2026-10-14
description: "Glycine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, rhinitis, pharyngitis…"
---

# Glycine
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

# Glycine: From Allergic Rhinitis and Upper Respiratory Conditions to Nasal Cavity Disease

## One-Sentence Summary

Glycine is an amino acid that appears in US-listed products such as irrigation solutions and parenteral nutrition, and the knowledge graph links it to upper respiratory indications such as allergic rhinitis, rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but the evidence is very thin: **1 clinical trial** (unrelated to glycine) and **2 publications** (neither evaluating glycine) are on record, so this remains a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, rhinitis, pharyngitis, common cold, nasopharyngitis (from knowledge graph indication edges; no approved indication text in the US license data) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 7 licenses (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, glycine is a simple amino acid used in irrigation solutions and parenteral nutrition products. The knowledge graph lists several upper respiratory indications for it, so no mechanistic rationale can be established from the data compiled for this report.

The most likely reason for the high prediction score is anatomical and disease-network proximity. Allergic rhinitis, vasomotor rhinitis, rhinitis and nasopharyngitis all involve the nasal passages, which overlap with "nasal cavity disease". This is a graph-based association only, not clinical or mechanistic evidence.

A second prediction, **acute laryngopharyngitis** (score 99.84%), likely arises from proximity to glycine's listed pharyngitis, common cold and nasopharyngitis indications. It has no clinical trials and no literature, and remains at the same L5 evidence level with a Hold recommendation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | PET/CT or PET/MRI imaging of a new radiotracer (18F-FPPRGD2) as an angiogenesis biomarker in glioblastoma, gynecological cancers and renal cell carcinoma. It does not test glycine and has no demonstrable link to nasal cavity disease. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preclinical / formulation research | Chemical & Pharmaceutical Bulletin | Oligoarginine-linked polymers as mucosal vaccine adjuvants in mouse nasal cavities. Does not evaluate glycine. |
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Basic research | Veterinary Pathology | Lectin histochemistry of normal and herpesvirus-infected bovine nasal mucosa. Does not evaluate glycine. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018315 | Glycine (ICU Medical Inc.) | Irrigant | Not available (cancelled) |
| NDA017865 | Glycine (Baxter Healthcare Corporation) | Solution | Not available (cancelled) |
| NDA016784 | Glycine (B. Braun Medical Inc.) | Irrigant | Not available (cancelled) |
| NDA018931 | Travasol (Baxter Healthcare Corporation) | Injection | Not available (cancelled) |
| NDA020734 | CLINIMIX (Baxter Healthcare Corporation) | Injection | Not available (cancelled) |

Two further cancelled entries exist (OUHOE Bean Sunscreen cream and HGH COMPLEX spray), for 7 licenses in total. None is currently valid.

## Safety Considerations

No package insert warnings, contraindications or drug interaction data were available for this report. Please refer to the package insert for safety information.

The knowledge graph does record disease associations flagged as contraindications (not label text), including:
- **Kidney disease**: chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
- **Calcium and phosphorus disorders**: hypercalcemia, hyperparathyroidism, hyperphosphatemia, sarcoidosis, osteitis fibrosa
- **Cardiovascular conditions**: heart disease, cardiovascular disease, ventricular fibrillation, digitalis poisoning
- **Metabolic disorders**: phenylketonuria and other disorders of phenylalanine metabolism
- **Others**: hypervitaminosis, constipation disorder, lytic metastatic bone lesion, pyoureter

These should be verified against official labeling before any use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there is no supporting clinical or mechanistic evidence. The only registered trial is unrelated to glycine, and the two publications do not evaluate it. All seven US licenses are cancelled, so there is no current regulatory pathway to build on.

**To proceed, the following is needed:**
- Mechanism of action data, to establish a plausible link to nasal cavity disease
- FDA package insert warnings and contraindications, which are a blocking gap for safety screening
- Drug interaction data
- Direct clinical or preclinical studies of glycine in nasal or upper respiratory disease
- Route and formulation compatibility assessment (e.g., whether a nasal or topical formulation is feasible), since no route data is available
- Clarification of the regulatory pathway, given that market status is cancelled only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

