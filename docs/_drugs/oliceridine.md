---
layout: default
title: Oliceridine
parent: Model Prediction Only (L5)
nav_order: 987
evidence_level: L5
indication_count: 4
---

# Oliceridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Oliceridine: From Acute Pain (Intravenous Opioid Analgesia) to Insomnia

## One-Sentence Summary

Oliceridine (brand name OLINVYK) is a G-protein-biased mu-opioid receptor agonist given by injection for acute pain.
The TxGNN model predicts it may be effective for **insomnia**, but this is a model prediction only, supported by **1 clinical trial that is not relevant to insomnia** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records; the evidence pack describes it as an IV analgesic for acute pain |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license entries (both are the same NDA210730) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, oliceridine is a G-protein-biased mu-opioid receptor agonist, developed as an intravenous analgesic for acute pain.

The link to insomnia is weak. Opioids cause sedation, but they generally fragment sleep and suppress REM and slow-wave sleep. They also carry respiratory-depression and dependence risks. No established mechanism supports treating insomnia with oliceridine.

The very high TxGNN score (0.998) comes from the knowledge-graph model alone. No clinical or literature evidence backs it, so the score should be read as a hypothesis-generating signal, not as evidence of efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07479446](https://clinicaltrials.gov/study/NCT07479446) | Not applicable | Not yet recruiting | 174 | Oliceridine vs sufentanil for patient-controlled IV analgesia, comparing postoperative nausea after cerebellopontine angle surgery. The endpoint is analgesia and opioid side effects, not insomnia. Relevance grade: C. No results yet. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210730 | OLINVYK (Trevena, Inc.) | Injection, solution | Not listed in the source record |

The source record lists this NDA twice with identical details, so it is shown once here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction has no supporting clinical trial or literature (L5, model prediction only). The mechanism argues against it, since opioids disrupt sleep architecture and carry respiratory-depression and dependence risks. The other three predictions (migraine, irritable bowel syndrome, neurocirculatory asthenia) are also L5 with no evidence and are also rated Hold.

**To proceed, the following is needed:**
- The full package insert, including warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Any preclinical or clinical evidence that oliceridine improves sleep outcomes
- Confirmation of the approved indication text for NDA210730
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

