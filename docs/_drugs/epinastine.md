---
layout: default
title: Epinastine
parent: Model Prediction Only (L5)
nav_order: 659
evidence_level: L5
indication_count: 2
---

# Epinastine
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

# Epinastine: From Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Epinastine is an antihistamine eye drop, originally used to treat allergic forms of conjunctivitis (atopic, papillary and vernal).
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but **0 clinical trials** and **0 publications** currently support this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 (an ANDA, cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Epinastine is a histamine H1 receptor antagonist with mast-cell stabilizing activity. Detailed mechanism of action data are not available in the data compiled for this report, so this description reflects its known drug class.

Its efficacy is established in allergic conjunctival conditions, where histamine and mast-cell mediators drive itching and surface inflammation. Ocular rosacea involves meibomian gland dysfunction, inflammation and ocular surface irritation. It may also have an allergic or histamine-mediated component. That gives a plausible but only indirect link.

The very high TxGNN score (99.57%) is a computational prediction. It most likely reflects network proximity to the existing conjunctivitis indications rather than direct evidence in rosacea. No trials or publications were found to confirm it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA090951 | Epinastine Hydrochloride (Somerset Therapeutics, LLC) | Solution / drops | Cancelled |

The only US license on record is cancelled, so the drug's practical availability would need verification.

---

## Safety Considerations

Please refer to the package insert for safety information. No warning, contraindication or drug-interaction data were available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for rosacea conjunctivitis rests only on a model score, with no registered trials or literature (evidence level L5). The drug's only US license is cancelled, and label-level safety and mechanism data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Targeted literature and trial searches on antihistamines or mast-cell stabilizers in ocular rosacea
- Confirmation of current US availability, since the only license is cancelled
- Consideration of the second-ranked prediction, **allergic urticaria** (score 99.28%, evidence level L3). It is supported by reviews and histamine wheal-and-flare studies in healthy volunteers, including a double-blind crossover RCT (PMID 10442525). These are surrogate pharmacodynamic data, not trials in urticaria patients, so it is best treated as a research question rather than a development candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

