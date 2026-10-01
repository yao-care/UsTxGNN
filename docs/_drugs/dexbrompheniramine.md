---
layout: default
title: Dexbrompheniramine
parent: Model Prediction Only (L5)
nav_order: 591
evidence_level: L5
indication_count: 7
---

# Dexbrompheniramine
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

# Dexbrompheniramine: From an Antihistamine (Original Indication Not Recorded) to Allergic Urticaria

## One-Sentence Summary

Dexbrompheniramine is a first-generation H1 antihistamine marketed in the US as a tablet, but the supplied record lists no approved indication text.
The TxGNN model predicts it may be effective for **allergic urticaria**.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied record |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Dexbrompheniramine is generally known as an alkylamine H1 antihistamine. This is general pharmacology and is not taken from the supplied data.

Allergic urticaria is a histamine-mediated condition, with wheals and flare driven by mast-cell histamine release. H1 receptor blockade is therefore mechanistically consistent with symptom relief. The drug's own original indication is not recorded, so the link to its established use cannot be assessed here.

The high score (0.9999) reflects the model's ranking only. Without trials or literature, the prediction is unverified.

**Other predictions from the model** (all L5, all Hold):

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Cold urticaria | 99.97% | A histamine-mediated physical urticaria, so H1 blockade is plausible |
| 3 | Recalcitrant atopic dermatitis | 99.64% | Possible itch relief only. The disease is driven by Th2 inflammation and barrier dysfunction, and "recalcitrant" disease implies poor response to standard therapy |
| 4 | IgE responsiveness, atopic | 99.63% | A trait rather than a treatable indication |
| 5 | Nasal cavity disease | 99.34% | Too broad to assess. It needs to be narrowed to a specific condition |
| 6 | Acute laryngopharyngitis | 99.33% | Mostly infectious. Any benefit would be symptomatic and speculative |
| 7 | Pharyngitis | 99.23% | Mostly infectious. Any benefit would be symptomatic and speculative |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M012 | ALA-HIST IR (Poly Pharmaceuticals, Inc.) | Tablet (oral) | Not stated in the record |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were available in the supplied data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or literature. Neither the original indication nor the mechanism of action is documented in the record, and no safety data are available. Allergic and cold urticaria are the most mechanistically plausible candidates. The others are weak or too non-specific to assess.

**To proceed, the following is needed:**
- The package insert with warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and mechanism of action data (for example from DrugBank)
- Literature and trial searches for dexbrompheniramine in urticaria
- Narrowing of non-specific predictions (nasal cavity disease, IgE responsiveness) to assessable conditions
- Route compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

