---
layout: default
title: Potassium Nitrate
parent: Model Prediction Only (L5)
nav_order: 1071
evidence_level: L5
indication_count: 2
---

# Potassium Nitrate
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

# Potassium Nitrate: From Marketed Topical Products (Original Indication Not Listed) to Meningococcal Infection

## One-Sentence Summary

Potassium nitrate is marketed in the US in products such as dentifrice pastes and gels and homeopathic pellets, but no approved indication text is on record.
The TxGNN model predicts it may be effective for **meningococcal infection**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed (approved indication text is empty in all records) |
| Predicted New Indication | Meningococcal infection |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Potassium nitrate is a marketed ingredient, mainly in topical dental products, but its original indication is not recorded, so no mechanistic link to the original use can be drawn.

One speculative link is the nitrate-nitrite-nitric oxide pathway. Acidified nitrite and nitric oxide show in vitro antimicrobial activity against some bacteria. There is no evidence that this applies to *Neisseria meningitidis*, that safe systemic doses would reach sufficient exposure, or that it could substitute for standard antibiotic therapy.

Meningococcal infection is life-threatening and already has effective antibiotics and vaccines. Any repurposing claim would need very strong evidence, and the score of 0.996 is a computational prediction with no supporting studies.

TxGNN also predicted sclerosing cholangitis as a second candidate (score 99.21%, also L5, Hold). It has no supporting trials or literature either, and the nitric oxide and microcirculation rationale is hypothesis-level only.

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
| M022 | SprinJene Natural | Paste, dentifrice | Not listed |
| Not listed | Kali Nitricum | Pellet | Not listed |
| M022 | Attitude Adult Fluoride-free - Sensitive - Spearmint | Gel, dentifrice | Not listed |
| Not listed | Kali Nitricum | Pellet | Not listed |
| Not listed | Kali Nitricum | Pellet | Not listed |

Showing 5 of 12 authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or literature. The mechanism is unvalidated, and meningococcal infection is a life-threatening disease with effective standard-of-care treatment. Safety data for systemic use is also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Preclinical evidence, such as in vitro activity against *N. meningitidis*
- A systemic safety assessment, including methemoglobinemia risk
- Confirmation of the original approved indications for the marketed products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

