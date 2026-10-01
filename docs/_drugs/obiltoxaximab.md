---
layout: default
title: Obiltoxaximab
parent: Model Prediction Only (L5)
nav_order: 979
evidence_level: L5
indication_count: 8
---

# Obiltoxaximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Obiltoxaximab: From Inhalational Anthrax to Postinfectious Vasculitis

## One-Sentence Summary

Obiltoxaximab (Anthim) is a monoclonal antibody marketed in the US for inhalational anthrax caused by *Bacillus anthracis*.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but **no clinical trials and no publications** currently support this prediction, so it rests on graph-based inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inhalational anthrax (inferred from trial records; the license record has no indication text) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125509) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not recorded in DrugBank for this entry. The mechanism below comes from the candidate's repurposing analysis. Obiltoxaximab neutralizes the protective antigen (PA) of *B. anthracis*, which blocks anthrax toxin from entering host cells.

The analysis found **no plausible link** between this mechanism and postinfectious vasculitis. That condition is an immune-complex or immune-mediated process that does not depend on PA. The high TxGNN score reflects proximity in the knowledge graph, not a biological or clinical rationale. Both conditions involve bacterial infection, but neutralizing an anthrax-specific toxin would not be expected to prevent or treat a post-infectious immune reaction.

The same picture holds for the other seven predictions for this drug, all at L4-L5 with a Hold recommendation. Only one of them, "post-bacterial disorder," has linked trials, and those are anthrax or healthy-volunteer studies rather than evidence for that condition.

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
| BLA125509 | Anthim (Elusys Therapeutics, Inc.) | Solution | Not listed in the license record |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.

Please refer to the package insert for warnings, contraindications, and other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score (99.74%), with no trial or literature support and no plausible mechanistic link between anthrax toxin neutralization and postinfectious vasculitis. Repurposing evidence is at L5, the weakest level.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently blocking safety screening)
- Mechanism-of-action data from DrugBank
- A biological hypothesis linking PA neutralization to vasculitis pathogenesis, plus preclinical evidence
- Route compatibility assessment (not yet performed)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

