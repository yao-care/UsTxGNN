---
layout: default
title: Caffeine
parent: Model Prediction Only (L5)
nav_order: 484
evidence_level: L5
indication_count: 10
---

# Caffeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Caffeine: From an Unspecified Original Indication to Nasal Cavity Disease

## One-Sentence Summary

Caffeine is a long-marketed central nervous system stimulant, sold in the US as over-the-counter "Stay Awake" tablets, among other products. The license records give no approved indication text.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **0 clinical trials** and only **3 publications**, none of which tests caffeine as a treatment for a nasal condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data (products listed are "Stay Awake" tablets) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (preclinical and mechanism-level literature only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses on record (the five listed are all numbered M011) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available. Caffeine is generally known as an adenosine receptor antagonist. Its efficacy for alertness is well established, but no data in this pack links it mechanistically to a nasal disease.

The one plausible link comes from the literature. Caffeine is a bitter taste receptor (T2R) agonist. T2Rs are expressed in airway epithelium, including the nasal cavity, where they are involved in innate defense and ciliary responses. This is a reasonable hypothesis, but it is unproven and cannot be checked against a curated mechanism.

The only nasal-related paper describes a caffeine nasal gel, and it uses the nose purely as a delivery route for cognition after sleep deprivation. It does not treat a nasal condition. The high model score is therefore not backed by direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are found in airways, including the nasal cavity. Supports a possible T2R-mediated mechanism, but it is not caffeine-specific evidence. |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Formulation / preclinical | Current Drug Delivery | Nasal thermo-sensitive in situ caffeine gel for cognition after sleep deprivation. The nose is a delivery route only, not a treatment target. |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine inhibited NNK-induced lung tumors in rats. Not related to nasal disease. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M011 | Stay Awake (Rite Aid Corporation) | Tablet | Not stated in the record |
| M011 | Stay Awake (United Natural Foods, Inc. dba UNFI) | Tablet | Not stated in the record |
| M011 | Stay Awake (Discount Drug Mart) | Tablet | Not stated in the record |
| M011 | Stay Awake (AAA Pharmaceutical, Inc.) | Tablet | Not stated in the record |
| M011 | Stay Awake (Retail Business Services, LLC.) | Tablet | Not stated in the record |

Across all 20 licenses, the dosage forms include oral tablets (plain, coated, film coated), injection and injection solution, chewable gel, pellet, and solution.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. There are no trials, and the three papers do not test caffeine for any nasal condition. The one mechanistic idea (T2R agonism in airway epithelium) is untested.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or clinical work showing an effect of caffeine in a nasal disease model, and a defined nasal disease and route
- Note: hypnic headache, another predicted indication for this drug, has a stronger evidence signal (L4, S1) and may be a better candidate to pursue first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

