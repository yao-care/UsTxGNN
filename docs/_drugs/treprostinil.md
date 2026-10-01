---
layout: default
title: Treprostinil
parent: Model Prediction Only (L5)
nav_order: 1256
evidence_level: L5
indication_count: 10
---

# Treprostinil
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

# Treprostinil: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Treprostinil is a prostacyclin analogue marketed in the US as an injection and an inhalant, and it is established in pulmonary arterial hypertension (PAH). The TxGNN model predicts it may be effective for **pulmonary arteriovenous malformation** with a score of 99.7%. **No clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license data (treprostinil is an established PAH therapy; confirm against the label) |
| Predicted New Indication | Pulmonary arteriovenous malformation |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known information, treprostinil is a prostacyclin analogue with vasodilatory and antiplatelet effects. Its efficacy in PAH is established, and a model that links it to other pulmonary vascular diseases could plausibly rank a pulmonary vascular malformation highly.

However, the mechanistic link here is weak and may even work against the drug. A pulmonary arteriovenous malformation is a structural vascular defect, and further vasodilation could worsen shunting rather than relieve it. The high score most likely reflects graph proximity to other pulmonary vascular diseases, not a real therapeutic rationale. The prediction should be treated as a hypothesis, not a candidate with supporting evidence.

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
| NDA021272 | Remodulin | Injection, solution | Not provided in data |
| NDA214324 | Tyvaso DPI | Inhalant | Not provided in data |
| ANDA210214 | Treprostinil (Dr. Reddy's) | Injection, solution | Not provided in data |
| ANDA211574 | Treprostinil (Alembic) | Injection, solution | Not provided in data |

Available routes across all 20 authorizations are injectable, inhaled, and oral (extended-release tablet and capsule forms).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it (L5). The pharmacology also raises a concern that vasodilation could worsen shunting in a structural malformation. It should not advance on the model score alone.

**To proceed, the following is needed:**
- A mechanistic or preclinical rationale showing that prostacyclin-pathway activity would not worsen shunting in pulmonary arteriovenous malformation
- FDA package insert warnings and contraindications (data gap DG001, blocking for safety screening)
- Mechanism of action data from DrugBank (data gap DG002)
- Confirmation of the labeled indications, since the license data contains no indication text

**Note on other predictions for this drug:** Several other predicted indications have stronger support than rank 1. PAH associated with connective tissue disease is L2 with a "Proceed with Guardrails" recommendation, and PAH associated with congenital heart disease is L3 (research question). These are better candidates to evaluate first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

