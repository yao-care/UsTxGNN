---
layout: default
title: Latanoprostene Bunod
parent: Model Prediction Only (L5)
nav_order: 840
evidence_level: L5
indication_count: 10
---

# Latanoprostene Bunod
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

# Latanoprostene Bunod: From Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

Latanoprostene bunod is a topical eye drop that lowers intraocular pressure. It is marketed in the US for open-angle glaucoma and ocular hypertension, though the license data supplied here does not state the indication text.
The TxGNN model ranks **visceral calciphylaxis** as its top prediction, but there are **0 clinical trials** and **0 publications** for it, so this is a graph-based signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied license data (the drug is known to be marketed for open-angle glaucoma and ocular hypertension) |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (1 NDA plus 1 ANDA, the latter listed twice) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

It is not well supported. Detailed mechanism of action data is not available in the supplied data. Latanoprostene bunod is a nitric-oxide-donating prostaglandin F2-alpha analog. Its known effect is lowering intraocular pressure by increasing aqueous outflow through the uveoscleral pathway (latanoprost acid) and the trabecular meshwork (nitric oxide).

Visceral calciphylaxis (calcific uremic arteriolopathy) is a systemic small-vessel calcification disorder. No mechanistic link to a topical ocular drug is evident. Systemic exposure after eye-drop use is minimal. The high score (0.998) most likely reflects vascular-tone associations in the knowledge graph, not a pharmacological rationale.

Other predictions in the list are better supported:
- **Primary hereditary glaucoma** (99.71%, L4) is mechanistically plausible but probably reflects the existing label class, not true repurposing. Its pediatric and hereditary subtypes still need a targeted literature check.
- **Vascular disease** (99.53%, L4) has two completed studies on microcirculation surrogates. They are indirect evidence only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA207795 | Vyzulta | Solution/drops | Bausch & Lomb Incorporated |
| ANDA217387 | Latanoprostene Bunod Ophthalmic Solution, 0.024% | Solution/drops | Gland Pharma Limited |

Approved indication text is not included in the supplied license records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible mechanism for a topical ocular drug in a systemic calcification disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any mechanistic or preclinical evidence linking the drug to calcific uremic arteriolopathy
- Consideration of the better-supported directions (hereditary glaucoma subtypes, vascular microcirculation) instead
- Note on safety: a 2023 case report (PMID 38113361) describes serous retinal detachment with prostaglandin analog use in a patient with a vascular malformation, which argues for caution in that setting

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

