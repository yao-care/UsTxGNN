---
layout: default
title: Aflibercept
parent: Model Prediction Only (L5)
nav_order: 217
evidence_level: L5
indication_count: 1
---

# Aflibercept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Aflibercept: From Ocular Anti-VEGF Therapy to Esotropia

## One-Sentence Summary

Aflibercept is a VEGF trap given by injection into the eye and marketed in the US under several biologic licenses. The TxGNN model predicts it may be effective for **esotropia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is model-only and no mechanistic link has been established, so it should be treated as a low-confidence signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data provided (the mechanism notes describe intravitreal use for retinal vascular diseases) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 (all listed licenses are BLAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Based on known information, aflibercept is a trap for VEGF-A, VEGF-B and placental growth factor (PlGF). It is used in the eye for retinal vascular diseases.

Esotropia is inward misalignment of the eye. It usually arises from extraocular muscle, neural or refractive problems rather than from abnormal blood vessel growth. No pathway from VEGF inhibition to correcting this misalignment is supported by the provided data.

The high score (0.994) is a knowledge-graph output only. It may reflect the drug's general ophthalmic associations rather than a real therapeutic relationship. Strabismus is sometimes seen after retinopathy of prematurity, which anti-VEGF agents treat. That is a different indication and does not show that aflibercept treats esotropia itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761378 | AHZANTIVE (Valorum Biologics) | Injection, solution | Not listed in the data provided |
| BLA761377 | EYDENZELT (Celltrion USA) | Injection | Not listed in the data provided |
| BLA125387 | EYLEA (Regeneron) | Injection, solution | Not listed in the data provided |
| BLA761355 | EYLEA HD (Regeneron) | Injection, solution | Not listed in the data provided |
| BLA761298 | PAVBLU (Amgen) | Injection, solution | Not listed in the data provided |

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no supported mechanistic link between VEGF inhibition and esotropia. Safety data are also missing, so there is no basis to advance.

**To proceed, the following is needed:**
- Obtain the FDA package insert (warnings and contraindications), which is blocking for safety screening
- Obtain mechanism of action data from DrugBank
- Find any preclinical or clinical evidence linking anti-VEGF therapy to esotropia or strabismus
- Assess whether intravitreal delivery is compatible with a strabismus indication (route compatibility is still pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

