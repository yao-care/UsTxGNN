---
layout: default
title: Regadenoson
parent: Model Prediction Only (L5)
nav_order: 1114
evidence_level: L5
indication_count: 4
---

# Regadenoson
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

# Regadenoson: From Pharmacologic Stress Agent for Cardiac Imaging to Anaphylaxis

## One-Sentence Summary

Regadenoson is a selective A2A adenosine receptor agonist marketed in the US as the injectable product LEXISCAN. The Evidence Pack does not list an approved indication, but it is known as a pharmacologic stress agent for cardiac perfusion imaging. The TxGNN model predicts it may be effective for **anaphylaxis**, but only **1 clinical trial** is linked (a cardiac imaging study, not a treatment trial) and **0 publications** support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided data (general knowledge: pharmacologic stress agent for myocardial perfusion imaging) |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 (includes ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Regadenoson is a selective A2A adenosine receptor agonist. In preclinical models, A2A signaling generally has anti-inflammatory effects. That is the only conceivable link to anaphylaxis, and no clinical evidence in the provided data supports it.

The prediction is weak. The drug label lists hypersensitivity reactions, including anaphylaxis, as an adverse reaction, so the drug is associated with anaphylaxis as a risk rather than a treatment. The very high score (0.998) is most likely a knowledge-graph association artifact rather than a therapeutic signal.

The other predictions are weaker still. Food-dependent exercise-induced anaphylaxis (score 99.74%) and pseudoallergy (99.12%) have no trials or literature and mirror the anaphylaxis association. Esotropia (99.12%) has no plausible mechanistic connection to A2A agonism. All are L5 and Hold.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | NA | Recruiting | 1000 | Multicenter stress cardiac MRI quantitative perfusion imaging study (SPINS2). Regadenoson is presumably the stress agent for diagnostic imaging. It does not test regadenoson as an anaphylaxis treatment (relevance grade C). |

## Literature Evidence

Currently no related literature available.

## US Market Information

The table shows 5 of the 17 authorizations. The Evidence Pack contains no approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022161 | LEXISCAN (Astellas Pharma US, Inc.) | Injection, solution | Not listed in provided data |
| ANDA213210 | Regadenoson (Dr. Reddy's Laboratories Inc.) | Injection | Not listed in provided data |
| ANDA218054 | Regadenoson (Marlex Pharmaceuticals, Inc.) | Injection, solution | Not listed in provided data |
| ANDA216437 | Regadenoson (Eugia US LLC) | Injection | Not listed in provided data |
| ANDA207604 | Regadenoson (Apotex Corp.) | Injection, solution | Not listed in provided data |

## Safety Considerations

Please refer to the package insert for safety information.

The prediction rationale notes that hypersensitivity reactions, including anaphylaxis, are a labeled adverse reaction. This is a safety concern for the drug, not a benefit.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5). The single linked trial is a diagnostic imaging study unrelated to treating anaphylaxis. The drug's own label lists anaphylaxis as an adverse reaction, so the score most likely reflects a knowledge-graph artifact rather than real therapeutic potential.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Preclinical or clinical evidence that A2A agonism benefits anaphylaxis or mast-cell-driven reactions
- Route compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

