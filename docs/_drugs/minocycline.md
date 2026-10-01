---
layout: default
title: Minocycline
parent: Model Prediction Only (L5)
nav_order: 932
evidence_level: L5
indication_count: 2
---

# Minocycline
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

# Minocycline: From Tetracycline Antibiotic to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Minocycline is a tetracycline-class antibiotic marketed in the US as oral capsules, tablets and extended-release tablets, plus a topical foam.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but this rests on a computational prediction alone.
There are currently **0 clinical trials** and **0 publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US license records (minocycline is a tetracycline-class antibiotic) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Minocycline is a tetracycline-class drug. Tetracyclines are generally described as having anti-inflammatory and matrix metalloproteinase (anti-collagenase) effects. These could plausibly relate to inflammation on the eye surface, which is a feature of punctate epithelial keratoconjunctivitis.

This is background reasoning, not evidence from the supplied dataset, and it needs independent verification. The only support in the record is the high TxGNN knowledge-graph score, which is a computational prediction without clinical validation.

The model also ranks a second ocular indication, **exposure keratitis** (score 99.20%), at the same evidence level (L5) with a Hold recommendation. This condition is driven mainly by incomplete lid closure and tear-film failure, so the chance of a drug-specific benefit is more uncertain.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Minocycline has 20 US licenses. Five main authorizations are listed below. All are ANDAs (generic approvals), and the records do not include approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA065062 | Minocycline Hydrochloride | Capsule | A-S Medication Solutions |
| ANDA065470 | Minocycline Hydrochloride | Capsule | Advanced Rx Pharmacy of Tennessee, LLC |
| ANDA203553 | Minocycline Hydrochloride | Tablet, extended release | Zydus Pharmaceuticals (USA) Inc. |
| ANDA204453 | Minocycline Hydrochloride | Tablet, film coated, extended release | Bryant Ranch Prepack |
| ANDA063065 | Minocycline Hydrochloride | Capsule | Actavis Pharma, Inc. |

Across all licenses, the marketed forms are oral (capsule, tablet, extended-release tablet) and a foam aerosol. No ophthalmic form appears in the record, so route compatibility with an eye-surface indication is unresolved.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score (99.63%) but no supporting clinical trials or literature (Evidence Level L5). The mechanism and safety data are also missing from the record, so the case cannot advance beyond initial screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- A literature and trial search for minocycline or tetracyclines in punctate epithelial keratoconjunctivitis, and in exposure keratitis as a second candidate
- Route and formulation assessment, since only oral and foam forms are marketed and an ocular indication may need a different route
- Confirmation of the original approved indications from the license labels

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

