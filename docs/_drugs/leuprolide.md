---
layout: default
title: Leuprolide
parent: Model Prediction Only (L5)
nav_order: 849
evidence_level: L5
indication_count: 2
---

# Leuprolide
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

# Leuprolide: From an Unrecorded Original Indication to Osteoarthritis

## One-Sentence Summary

Leuprolide is a GnRH agonist, marketed in the US as several extended-release injectable products. The Evidence Pack does not record its approved indications.
The TxGNN model predicts it may be effective for **osteoarthritis**, but this is a model prediction only.
**1 clinical trial** and **1 publication** were retrieved, and neither studies osteoarthritis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the provided data |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Leuprolide is a GnRH agonist that suppresses gonadal sex steroids after an initial stimulation phase. A speculative link to osteoarthritis is hormonal influence on cartilage and subchondral bone.

No evidence in this package supports that link. The original indication is also not recorded, so the relationship between the original and predicted indications cannot be assessed. The high TxGNN score (0.997) should be treated as a hypothesis-generating signal, not as support for efficacy.

The second-ranked prediction, pseudoachondroplasia (score 99.69%), is also L5 with no trials or literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002881](https://clinicaltrials.gov/study/NCT00002881) | Phase 3 | Completed | Not reported | Randomized trial in metastatic prostate cancer of orchiectomy/LHRH analog + flutamide, with or without suramin and hydrocortisone. It does not study osteoarthritis and was likely matched only through the drug name (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Case report | Clinical Breast Cancer | Metastatic prostatic adenocarcinoma presenting with skin changes that mimicked inflammatory breast carcinoma. Not relevant to osteoarthritis. |

---

## US Market Information

Five of the 11 authorizations are listed. The Evidence Pack contains no approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021488 | Eligard (TOLMAR Inc.) | Injection, suspension, extended release | Not listed |
| NDA021343 | Eligard (TOLMAR Inc.) | Injection, suspension, extended release | Not listed |
| NDA021379 | Vabrinty (Uronova Pharmaceuticals, Inc.) | Injection, suspension, extended release | Not listed |
| NDA021731 | Vabrinty (Uronova Pharmaceuticals, Inc.) | Injection, suspension, extended release | Not listed |
| NDA211488 | CAMCEVI (Accord BioPharma, Inc.) | Injection, emulsion | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN score. The one trial and one publication found concern prostate cancer, not osteoarthritis. There is no supported mechanistic link, and neither the mechanism of action nor the safety data are available.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, to allow safety screening
- Mechanism of action data (e.g., from DrugBank) and the approved indications
- Preclinical or clinical evidence specific to osteoarthritis
- An assessment of route and dosage-form compatibility, since all marketed forms are extended-release injectables
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

