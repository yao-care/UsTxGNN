---
layout: default
title: Emapalumab
parent: Model Prediction Only (L5)
nav_order: 648
evidence_level: L5
indication_count: 10
---

# Emapalumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Emapalumab: From Primary Hemophagocytic Lymphohistiocytosis to Autosomal Recessive Familial Mediterranean Fever

## One-Sentence Summary

Emapalumab is an anti-interferon-γ (IFN-γ) monoclonal antibody, marketed in the US as GAMIFANT and established for primary hemophagocytic lymphohistiocytosis (HLH).
The TxGNN model predicts it may be effective for **autosomal recessive familial Mediterranean fever (FMF)**, but this prediction has **0 clinical trials** and **0 publications** behind it, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary HLH (inferred from the mechanistic notes; the license records contain no indication text) |
| Predicted New Indication | Autosomal recessive familial Mediterranean fever |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 (all under BLA761107) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured record. Emapalumab is a fully human antibody that neutralizes IFN-γ, the central cytokine driving the hyperinflammation in HLH.

FMF is a different kind of disease. It is mainly driven by pyrin inflammasome activation and IL-1β, and it is treated with colchicine and IL-1 inhibitors. The mechanistic link to emapalumab is therefore weak. IFN-γ blockade could plausibly matter only in the rare FMF patients who develop macrophage activation syndrome (MAS) or HLH.

The high TxGNN score most likely reflects proximity in the knowledge graph (both are autoinflammatory conditions). It does not reflect any observed clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA761107 | GAMIFANT | Injection | Swedish Orphan Biovitrum AB (publ) |

The record contains 7 license entries, all under this same BLA and product. It lists no approved-indication text.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. FMF is driven by IL-1, not IFN-γ, and no trials or literature support it. There is no basis to advance it beyond the model output.

**To proceed, the following is needed:**
- Evidence that IFN-γ blockade helps in FMF, restricted to FMF complicated by MAS/HLH (case reports or a registry review would be a start)
- Mechanism-of-action data and package insert safety information
- A comparison against standard FMF therapy (colchicine and IL-1 inhibitors)

**Note on other predictions for this drug:** Among the 10 predicted indications, the best-supported is **hemophagocytic syndrome associated with an infection** (rank 3, L3, S2). It has one terminated Phase 2/3 trial (NCT03985423, 7 enrolled) and multiple case reports and small series, mostly in Epstein-Barr virus-associated HLH. Malignancy-associated HLH (rank 2) and X-linked lymphoproliferative disease (rank 6) are also mechanistically coherent, at L4. These are better candidates to evaluate first. Efficacy in infection-associated HLH is still not established.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

