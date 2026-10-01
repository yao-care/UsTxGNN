---
layout: default
title: Glycine
parent: Model Prediction Only (L5)
nav_order: 757
evidence_level: L5
indication_count: 2
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

# Glycine: From Marketed Irrigant/Solution Products to Nasal Cavity Disease

## One-Sentence Summary

Glycine is a simple amino acid marketed in the US mainly as irrigation and solution products, but the records give no approved indication text.
The TxGNN model predicts it may be relevant to **Nasal Cavity Disease**, but the only registered trial found (**1**) does not test glycine, and there are **0 publications** for this indication.
This is a model-only prediction with no clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the approval records (all approved indication fields are empty) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The marketed glycine products are irrigants and solutions, and their approved indications are not recorded, so the link between the original use and nasal cavity disease cannot be established from this data.

One speculative link is glycine's cytoprotective and anti-inflammatory activity. It is thought to act through glycine-gated chloride channels on macrophages and neutrophils, which could matter in mucosal inflammation. No evidence ties this to nasal cavity disease, and the mechanism is a hypothesis only.

The high score (99.85%) comes from the knowledge-graph model alone and has not been corroborated by clinical or preclinical studies. Similarity between the original and new indication has not been assessed. Route compatibility is also unassessed, and no nasal or inhaled glycine product appears among the listed dosage forms.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | PET/CT or PET/MRI imaging of a new tracer (18F-FPPRGD2) as an angiogenesis biomarker in glioblastoma, gynecological cancers and renal cell carcinoma. It tests a diagnostic tracer, not glycine, so it gives no efficacy or safety evidence for nasal cavity disease (relevance grade: C). |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 018315 | Glycine (ICU Medical) | Irrigant | Not stated in the record |
| NDA 017865 | Glycine (Baxter Healthcare) | Solution | Not stated in the record |
| NDA 016784 | Glycine (B. Braun Medical) | Irrigant | Not stated in the record |
| M020 | OUHOE Bean Sunscreen (Shantou Ouhoe Technology) | Cream | Not stated in the record |
| No number listed | HGH COMPLEX (ProBlen) | Spray | Not stated in the record |

Only 5 of the 20 authorizations are shown. The sunscreen and spray entries are not NDA-numbered products.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score. The single registered trial is an imaging-tracer study unrelated to glycine therapy, and there is no supporting literature, no MOA data and no safety data. Evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data for glycine (DrugBank query)
- FDA package insert warnings and contraindications, which are needed before any safety screening
- Preclinical or clinical studies of glycine in nasal or upper-airway mucosal disease
- Approved indication text for the existing glycine products, to define the original indication
- A route-compatibility assessment, since no nasal or inhaled glycine formulation is currently listed

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

