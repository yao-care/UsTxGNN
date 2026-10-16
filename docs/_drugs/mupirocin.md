---
layout: default
title: Mupirocin
parent: Model Prediction Only (L5)
nav_order: 945
evidence_level: L5
indication_count: 2
monitor_inn: "MUPIROCIN"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
---

# Mupirocin
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

# Mupirocin: From Impetigo to Pleural Empyema

## One-Sentence Summary

Mupirocin is a topical antibiotic originally used to treat impetigo and bullous impetigo.
The TxGNN model predicts it may be effective for **pleural empyema**,
but currently **0 clinical trials** and **0 publications** support this direction, so this is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Impetigo, bullous impetigo |
| Predicted New Indication | Pleural empyema |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, mupirocin inhibits bacterial isoleucyl-tRNA synthetase and is active against *Staphylococcus aureus* (including MRSA) and many streptococci. These organisms are common causes of pleural empyema, which gives a plausible antibacterial rationale linking the original skin infection indication to the predicted one.

However, the practical link is weak. Mupirocin is a topical agent with negligible systemic bioavailability because it is rapidly metabolized to inactive monic acid. It cannot reach therapeutic concentrations in the pleural space by either topical or systemic routes. Standard care for empyema (drainage plus systemic antibiotics) is well established, so the prediction has no realistic translational pathway.

The model's second-ranked prediction, punctate epithelial keratoconjunctivitis (score 99.10%), is also weak. That condition is often viral (e.g., adenovirus) or non-bacterial, and mupirocin has no antiviral activity. The commercial ointment is also not designed for ophthalmic use. Both predictions are at the L5 level and have been given a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA065170 | Mupirocin (Proficient Rx LP) | Ointment | Not stated; license cancelled |
| ANDA065123 | Mupirocin (Bryant Ranch Prepack) | Ointment | Not stated; license cancelled |
| ANDA065085 | Mupirocin (Teva Pharmaceuticals USA, Inc.) | Ointment | Not stated; license cancelled |
| ANDA090480 | Mupirocin (Preferred Pharmaceuticals Inc.) | Ointment | Not stated; license cancelled |
| ANDA217943 | Mupirocin (Encube Ethicals, Inc.) | Ointment | Not stated; license cancelled |

All five authorizations are single-ingredient ointments and all are cancelled.

## Safety Considerations

- **Disease-level contraindication signal (knowledge graph, not label text)**: dermatitis.
- **Drug Interactions**: The interaction screen returned 100 potential interacting drugs, but none has a severity grading (all "Unknown"). Examples include calcitriol, clotrimazole, morphine, metformin, pantoprazole, omeprazole, vancomycin, prednisone, simvastatin and rosuvastatin. These entries should not be read as confirmed clinically significant interactions. Given mupirocin's minimal systemic absorption, their relevance is likely limited, but this has not been verified.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials or literature behind it. Mupirocin's topical-only exposure and rapid inactivation make therapeutic levels in the pleural space implausible, and effective standard treatment already exists. All US licenses for the drug are also cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Evidence that a clinically relevant pleural or ocular exposure can be achieved, which would likely require a new formulation or route
- Any preclinical or clinical data supporting activity in pleural empyema
- For the ocular prediction, confirmation of a bacterial etiology and an ophthalmic-suitable formulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

