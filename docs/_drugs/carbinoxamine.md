---
layout: default
title: Carbinoxamine
parent: Model Prediction Only (L5)
nav_order: 496
evidence_level: L5
indication_count: 7
---

# Carbinoxamine
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

# Carbinoxamine: From H1 Antihistamine to Allergic Urticaria

## One-Sentence Summary

Carbinoxamine is a first-generation H1 antihistamine that is currently marketed in the United States as oral tablets, solution, and extended-release suspension.
The TxGNN model predicts it may be effective for **allergic urticaria** with a very high score, but this is a model prediction only.
There are currently **0 clinical trials** and **0 publications** in the evidence pack supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the evidence pack (the approved indication text is empty for all listed licenses) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 10 licenses (NDA and ANDA combined) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, carbinoxamine is a first-generation H1 antihistamine. H1 receptor blockade is a biologically coherent mechanism for histamine-mediated wheal and itch, so the drug may be applicable to allergic urticaria.

Allergic urticaria is driven by mast-cell histamine release, and H1 antihistamines are the standard symptomatic drug class. The link is plausible at the class level. However, no carbinoxamine-specific clinical evidence was supplied, and the score of 0.9999 is not backed by any trial or publication.

Urticaria may already be within carbinoxamine's approved labeling. If so, this would be an on-label use rather than true repurposing. This must be verified against the current label.

The model also produced six other predictions, all at L5 with no supporting studies:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Cold urticaria | 99.96% | Plausible at the class level (histamine-driven physical urticaria); no drug-specific evidence |
| 3 | Nasal cavity disease | 99.88% | Term too broad; likely reflects allergic or vasomotor rhinitis, which may already be labeled |
| 4 | Pharyngitis | 99.87% | Mostly infectious; no disease-modifying mechanism, and the drying effect may worsen throat irritation |
| 5 | Acute laryngopharyngitis | 99.87% | Weak rationale; likely driven by graph proximity to related airway conditions |
| 6 | Recalcitrant atopic dermatitis | 99.73% | Limited itch relief at most; histamine is not the main driver |
| 7 | IgE responsiveness, atopic | 99.68% | A trait rather than a treatable indication; not actionable |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA040458 | Carbinoxamine Maleate (Genus Lifesciences) | Solution |
| ANDA207484 | Carbinoxamine Maleate (BluCrest Pharmaceuticals) | Tablet |
| NDA022556 | Carbinoxamine Maleate Extended-Release Oral Suspension (Neos Therapeutics) | Extended-release suspension |
| ANDA215476 | Carbinoxamine Maleate (Leading Pharma) | Tablet |
| ANDA040458 | CARBZAH (IPG Pharmaceuticals) | Solution |

The approved indication text is empty for all listed licenses, so the label indications could not be compared with the predicted indications.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction only (L5), with no trials or literature. Original indications, mechanism data, and package insert safety information are all missing. The top prediction, allergic urticaria, may already be an on-label use. Until that is checked, the candidate stays at the research-question stage.

**To proceed, the following is needed:**
- Retrieve the current US package insert to confirm approved indications, and check whether urticaria, rhinitis, or other predicted conditions are already on-label
- Package insert warnings and contraindications, which currently block safety screening
- Detailed mechanism of action data (MOA) from DrugBank
- A literature and trial search for carbinoxamine in urticaria (allergic and cold), and for other H1 antihistamines in the same conditions as class-level support
- Deprioritize the non-actionable predictions: IgE responsiveness, pharyngitis, and acute laryngopharyngitis

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

