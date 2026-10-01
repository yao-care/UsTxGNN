---
layout: default
title: Fosphenytoin
parent: Model Prediction Only (L5)
nav_order: 739
evidence_level: L5
indication_count: 7
---

# Fosphenytoin
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

# Fosphenytoin: From Seizure Control to Conjunctivitis

## One-Sentence Summary

Fosphenytoin is an injectable prodrug of phenytoin, an anticonvulsant. The approved-indication text was not supplied in the data, so seizure use is inferred from its drug class. The TxGNN model predicts it may be effective for **conjunctivitis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 16 (the listed authorizations are ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied data. Fosphenytoin is a prodrug of phenytoin, a voltage-gated sodium channel blocker that dampens neuronal excitability. That is a plausible basis for seizure control.

**The mechanism does not support this prediction.** Nothing in the supplied data connects sodium channel blockade to conjunctival inflammation, which is typically infectious or allergic in origin. The high score (0.994) is a statistical output of the knowledge graph. The model ranks this pair 14,424th overall, and no trial or publication backs it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The supplied records give no approved-indication text, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA214926 | Fosphenytoin sodium | Injection, solution | Glenmark Pharmaceuticals Inc., USA |
| ANDA078765 | Fosphenytoin Sodium | Injection, solution | West-Ward Pharmaceuticals Corp |
| ANDA077989 | Fosphenytoin Sodium | Injection | Hikma Pharmaceuticals USA Inc. |
| ANDA078476 | Fosphenytoin Sodium | Injection | Amneal Pharmaceuticals LLC |
| ANDA214926 | Fosphenytoin Sodium | Injection, solution | Sagent Pharmaceuticals |

All listed forms are injectable. The data shows the same number (ANDA214926) under two manufacturers.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The conjunctivitis prediction has no supporting trials or literature, and no mechanistic link is apparent. It should not be pursued on the model score alone.

Among the other predictions, only **manic bipolar affective disorder** (score 99.18%) has any supporting literature. That is one human study of IV fosphenytoin in acute mania ([PMID 12716241](https://pubmed.ncbi.nlm.nih.gov/12716241/), *J Clin Psychiatry*, 2003). Its design and results could not be verified from the supplied abstract, so the provisional L3 grade could change. It is a better-supported research question than conjunctivitis.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently blocking safety screening)
- Mechanism-of-action data from DrugBank
- A literature search focused on fosphenytoin or phenytoin in conjunctivitis
- If the team wants a stronger lead, full-text review of PMID 12716241 to confirm study design and outcomes

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

