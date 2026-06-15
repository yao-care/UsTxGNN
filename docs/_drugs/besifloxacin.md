---
layout: default
title: Besifloxacin
parent: 僅模型預測 (L5)
nav_order: 453
evidence_level: L5
indication_count: 8
---

# Besifloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

The skill confirms this is a TxGNN pipeline task. The system prompt already provides the full report generation specification (v5). I'll now generate the report directly from the Evidence Pack.

---

# Besifloxacin: From Bacterial Conjunctivitis to Bronchitis

## One-Sentence Summary

Besifloxacin (Besivance®) is a fourth-generation fluoroquinolone antibiotic, currently formulated exclusively as an ophthalmic suspension and clinically proven for bacterial conjunctivitis.
The TxGNN model predicts it may be effective for **Bronchitis** with a prediction score of **99.84%**,
however there are currently **0 clinical trials** and **0 publications** directly supporting this direction — evidence rests entirely on model prediction alone (Level L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial conjunctivitis (ophthalmic use; inferred from clinical trial context — no Taiwan registration found) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | Not marketed (0 registrations in queried database) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known clinical use, Besifloxacin belongs to the fluoroquinolone class of antibiotics — a drug class that inhibits bacterial DNA gyrase (topoisomerase II) and topoisomerase IV, two enzymes essential for bacterial DNA replication and repair. Its broad-spectrum antibacterial activity has been demonstrated through multiple completed Phase 3 and Phase 4 clinical trials, covering major gram-positive pathogens such as *Staphylococcus aureus* (including MRSA), *Streptococcus pneumoniae*, and gram-negative organisms such as *Haemophilus influenzae*.

Bacterial conjunctivitis and bronchitis share overlapping causative pathogens — particularly *S. pneumoniae* and *H. influenzae*. Other fluoroquinolones in the same class (levofloxacin, moxifloxacin) are guideline-recommended treatments for acute bacterial bronchitis and community-acquired pneumonia. The TxGNN model likely captured this class-level antibacterial activity profile and extrapolated it to bronchitis, which is mechanistically coherent at the drug-class level.

However, a critical practical barrier exists. Besifloxacin is available **only as a 0.6% ophthalmic topical suspension**, and a dedicated Phase 1 pharmacokinetic study (NCT00407589) confirmed that systemic plasma concentrations following topical ocular administration are negligibly low — far below any therapeutically relevant threshold for pulmonary or systemic infection. Besifloxacin currently has no oral, inhaled, or intravenous formulation. Without development of a new dosage form, this mechanistic potential cannot be translated into clinical use for bronchitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Besifloxacin in bronchitis.

---

## Literature Evidence

Currently no related literature available for Besifloxacin in bronchitis.

---

## US Market Information

No registrations found in the queried regulatory database (0 licenses as of data cutoff 2026-05-01).

> **Data Note:** Besivance® (besifloxacin ophthalmic suspension 0.6%) holds US FDA approval for bacterial conjunctivitis (NDA 022308, approved 2009, Bausch & Lomb). The zero-registration result reflects the scope of the queried Taiwan regulatory database (TFDA), where Besifloxacin has no approved product — not the absence of any global market authorization.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication (bronchitis) carries L5 evidence — no clinical trials or published literature exist to support it — and Besifloxacin's ophthalmic-only formulation with confirmed negligible systemic absorption creates a pharmacokinetic barrier that cannot be overcome without a new dosage form. Pursuing this indication as-is offers no viable development path.

**To proceed, the following is needed:**

- **Regulatory data**: Retrieve US FDA NDA 022308 (Besivance®) full label to populate the safety warnings, contraindications, and approved indication fields
- **MOA data**: Query DrugBank API (DB06771) for complete mechanism of action, pharmacodynamics, and pharmacokinetic parameters
- **Formulation strategy**: Any non-ophthalmic repurposing (bronchitis, urinary, systemic) requires first developing an oral or systemic formulation — a significant investment with uncertain advantage over generic fluoroquinolones already on the market
- **Alternative repurposing target**: Consider prioritizing **Otitis Externa (Rank 8)** instead. The mechanistic rationale is substantially stronger — fluoroquinolone ear drops are an established FDA-approved class, Besifloxacin's in vitro MIC against *Pseudomonas aeruginosa* and MRSA is superior to approved otic competitors, and conversion from ophthalmic suspension to otic suspension is a lower regulatory and formulation hurdle
- **Evidence gap on rank 3**: The **Post-Bacterial Disorder (Rank 3)** indication returned 6 clinical trials (all ophthalmic, L3 evidence). A focused mechanistic analysis of whether post-infectious ocular complications qualify as a distinct repurposing opportunity is warranted before broader claims are made
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

