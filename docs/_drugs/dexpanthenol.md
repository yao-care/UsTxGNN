---
layout: default
title: Dexpanthenol
parent: Model Prediction Only (L5)
nav_order: 596
evidence_level: L5
indication_count: 7
---

# Dexpanthenol
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

# Dexpanthenol: From Skin and Gastrointestinal Motility Conditions to Anorectal Stricture

## One-Sentence Summary

Dexpanthenol is a pantothenic acid (vitamin B5) precursor, originally used for skin conditions (dermatitis, eczema, keratoses) and gastrointestinal motility disorders such as paralytic ileus and gastroparesis.
The TxGNN model predicts it may be effective for **anorectal stricture**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paralytic ileus, intestinal obstruction, gastroparesis, skin diseases (dermatitis, atopic eczema, actinic and seborrheic keratosis). These come from knowledge-graph indication edges, not from approved label text. |
| Predicted New Indication | Anorectal stricture |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, dexpanthenol is converted in the body to pantothenic acid, a precursor of coenzyme A. Coenzyme A supports epithelial repair and wound healing, and dexpanthenol may also stimulate gut motility. This is consistent with its use in skin conditions and in ileus-type disorders.

Anorectal stricture is a narrowing of the anorectal canal, usually from scarring, inflammation, or surgery. The proposed link is that mucosal and epithelial repair support could help the affected tissue. However, this is not established for fibrotic stricture, where excessive scarring is the core problem, and repair support could even be unhelpful. The high score likely reflects proximity in the knowledge graph to gastrointestinal motility indications rather than a proven biological pathway.

Other top-ranked predictions show similar patterns. The table below gives an overview of the other predictions, none of which has meaningful evidence:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Imperforate anus | 99.71% | L5 | Congenital malformation requiring surgery; at most a speculative supportive role in postoperative care |
| 3 | Anal polyp | 99.62% | L5 | No plausible mechanism; managed by resection |
| 4 | Vulvar inverted follicular keratosis | 99.60% | L5 | Link by disease-class similarity to keratoses only |
| 5 | Proctitis | 99.60% | L5 | Theoretical mucosal-protective rationale (e.g. radiation proctitis) |
| 6 | Exanthem | 99.60% | L4 | One Phase 3 trial, but indirect evidence (see below) |
| 7 | Punctate epithelial keratoconjunctivitis | 99.34% | L5 | Plausible link through ophthalmic corneal-healing use, but no data supplied |

## Clinical Trial Evidence

For the lead prediction (anorectal stricture), currently no related clinical trials are registered.

The only trial found across the predictions relates to the rank 6 prediction, exanthem:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Completed | 160 | Randomized, double-blind comparison of Bepanthen cream vs cetomacrogol cream for preventing papulopustular (acneiform) eruption in patients receiving EGFR inhibitors. This is a related drug-induced skin reaction, not exanthem itself, so the evidence is indirect. No outcome data were available. |

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M018 | Eyelash Serum (FlexiGo Inc) | Liquid | Not specified (status: cancelled) |
| Not available | ReOrganic Eyelash Growth Boosting Serum (LAON COMMERCE co ltd) | Liquid | Not specified (status: cancelled) |

Both authorizations are cancelled, so no active US-marketed product was identified in the data compiled for this report.

## Safety Considerations

- **Contraindications (knowledge-graph based, not label text)**: Hemophilia is listed as a contraindicated condition in the TxGNN knowledge graph.

No drug-interaction records were found. For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The anorectal stricture prediction has a high model score (99.72%) but no clinical trials or literature, so it sits at evidence level L5. The mechanism is plausible only in a general sense (epithelial repair), and it is unclear whether it applies to fibrotic stricture. Package insert safety data and mechanism of action data are also missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- A literature and trial search for dexpanthenol in anorectal stricture, proctitis, and post-surgical anorectal healing
- Preclinical or pilot evidence that repair support helps rather than worsens fibrotic narrowing
- Route and formulation assessment (topical, rectal, or other), as route compatibility has not been evaluated
- If a more promising lead is wanted, consider the proctitis and punctate epithelial keratoconjunctivitis predictions, where the mechanistic rationale is more plausible, and review the outcome data of NCT01136005 for skin-reaction prevention
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

