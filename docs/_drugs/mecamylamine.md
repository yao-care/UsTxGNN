---
layout: default
title: Mecamylamine
parent: Model Prediction Only (L5)
nav_order: 890
evidence_level: L5
indication_count: 4
---

# Mecamylamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Mecamylamine: From an Unrecorded Original Indication to Malignant Renovascular Hypertension

## One-Sentence Summary

Mecamylamine is an oral tablet marketed in the US as Vecamyl, but the supplied label data does not record its approved indication.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**.
There are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model-only hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both listed under ANDA204054) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Based on general pharmacology, mecamylamine is a nicotinic ganglionic blocker. It lowers blood pressure by reducing autonomic vascular tone, so an antihypertensive effect is mechanistically plausible.

The fit with this particular indication is only partial. Renovascular malignant hypertension is driven largely by renin-angiotensin system activation, which ganglionic blockade does not directly target. It is also a hypertensive emergency, so any use would need to be compared against modern, better-characterized treatments.

The same model score (99.14%) was given to "malignant hypertensive renal disease", which suggests the two predictions share a graph neighborhood. The high score most likely reflects a generic "hypertension" association rather than disease-specific evidence.

## Other Predicted Indications

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Malignant hypertensive renal disease | 99.14% | L5 | Research question. Blood pressure lowering may reduce renal injury, but ganglionic blockers can cause orthostatic hypotension and reduced renal perfusion. |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.09% | L5 | Hold. There is no known selective pulmonary vasodilator action, and systemic hypotension could compromise right ventricular perfusion. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.09% | L5 | Hold. The retrieved literature is not relevant (see below). |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction.

For the fourth-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), 20 records were retrieved, but only 10 were provided. Those 10 are general hypoxia papers on brain aging, tumor HIF signaling, altitude, and multiple sclerosis. None mentions mecamylamine or pulmonary hypertension treatment, so the retrieval appears to have matched on the keyword "hypoxia" alone. The other 10 records were not provided and could not be assessed. This material is not counted as supporting evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA204054 | Vecamyl | Tablet (oral) | TILDE Sciences LLC |
| ANDA204054 | Vecamyl | Tablet (oral) | Vyera Pharmaceuticals, LLC |

The approved indication text is not provided in the source data.

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records (not found). This is not evidence of no interactions.
- **Class-level concerns from the prediction analysis**: Ganglionic blockade can cause orthostatic hypotension and reduced renal perfusion, which are key open questions for the renal and pulmonary hypertension indications.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or drug-specific literature. The mechanistic link is inferred from general pharmacology, and it is weak for renovascular disease (renin-driven) and for pulmonary hypertension.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data and the approved indication
- A targeted literature search on mecamylamine in malignant or renovascular hypertension
- Comparison against current standard-of-care antihypertensives for hypertensive emergency
- Assessment of renal perfusion and hypotension risk in the target populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

