---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 723
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: From Antimetabolite Chemotherapy to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil is an antimetabolite chemotherapy drug that is marketed in the United States as an injection and a topical cream.
The TxGNN model predicts it may be effective for **botryoid-type embryonal rhabdomyosarcoma of the vagina**.
This prediction currently has **0 clinical trials** and **0 publications** supporting it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDAs, i.e., generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Fluorouracil is a thymidylate synthase inhibitor and antimetabolite that acts on rapidly dividing tumor cells. Mechanistically, it could plausibly act on a fast-proliferating pediatric sarcoma.

However, no trial or publication links fluorouracil to this subtype, and it is not part of standard rhabdomyosarcoma regimens. The high score most likely reflects the shared rhabdomyosarcoma neighborhood in the knowledge graph rather than site-specific evidence. It should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA217295 | Fluorouracil | Injection, solution |
| ANDA210124 | Fluorouracil | Injection, solution |
| ANDA040278 | Fluorouracil | Injection, solution |
| ANDA090368 | Fluorouracil | Cream |

ANDA217295 is held by two manufacturers (Alembic Pharmaceuticals and BluePoint Laboratories). Approved indication text was not available in the source data.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Moderate to high (general class knowledge; drug-specific toxicity data not provided) |
| Emetogenicity Classification | Low to moderate (general class knowledge) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for drug-specific details.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by the model score, with no trials or publications, and fluorouracil is not part of standard rhabdomyosarcoma treatment. Among the other predicted indications, liver sarcoma (rank 7) has the most indirect evidence and could be a candidate for a focused retrospective review.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Subtype-specific preclinical or clinical evidence for rhabdomyosarcoma
- Comparison against current standard-of-care rhabdomyosarcoma regimens
- Route compatibility assessment (injectable vs. topical) for the target disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

