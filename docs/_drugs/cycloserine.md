---
layout: default
title: Cycloserine
parent: Model Prediction Only (L5)
nav_order: 557
evidence_level: L5
indication_count: 7
---

# Cycloserine
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

# Cycloserine: From an Unrecorded Original Indication to Irritable Bowel Syndrome

## One-Sentence Summary

Cycloserine is an oral capsule drug marketed in the United States, but the Evidence Pack does not record its original approved indication.
The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome**, with a very high score (99.95%).
However, **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The Evidence Pack contains no MOA entry for cycloserine, and its original indication text is empty. No established mechanism links cycloserine to irritable bowel syndrome.

The high score comes from the knowledge graph alone. Neither trials nor literature were retrieved to support it, so the score should be treated as a hypothesis-generating signal, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA060593 | Cycloserine (Dr. Reddy's Laboratories, Inc.) | Capsule (oral) | Not listed in the source data |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction records were found in the query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The irritable bowel syndrome prediction is Evidence Level L5, meaning a model prediction only. It has no registered trials, no literature and no mechanistic rationale, and the safety data is incomplete.

Other candidates on the list have somewhat more support, but all remain at Hold or "Research Question":
- **Insomnia (L4):** three Phase 2/3 trials of D-cycloserine, all in neuropsychiatric settings (PTSD, fibromyalgia with brain stimulation, bipolar depression). None targets insomnia, and two did not complete. It is flagged as a "Research Question".
- **Conjunctivitis (L4):** only three papers from 1963–1969 on antibiotic treatment of chlamydial infection and an animal model, so the evidence is indirect and dated.

**To proceed, the following is needed:**
- The original approved indication of cycloserine and its mechanism of action (from DrugBank)
- The package insert warnings and contraindications (from the FDA label), which block safety screening
- A literature and trial search specific to irritable bowel syndrome, plus a mechanistic rationale
- Route compatibility and similarity-to-original-indication assessments, both still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

