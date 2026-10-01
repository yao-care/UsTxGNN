---
layout: default
title: Amantadine
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 4
---

# Amantadine
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

# Amantadine: From Its Marketed Uses to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine is a long-marketed oral and solution product in the US, but the record does not list its approved indications.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. From general pharmacology, amantadine is a non-competitive NMDA receptor antagonist. This is not derived from the source record.

Rasmussen encephalitis is characterised by immune-mediated cortical inflammation together with glutamate-related excitotoxicity. Blocking NMDA receptors could plausibly reduce the excitotoxic component, which gives the prediction a mechanistic rationale.

This rationale is only plausible, not supported. No trial or publication in this dataset links amantadine to Rasmussen encephalitis. The high graph score is not clinical evidence, and any benefit would likely be symptomatic rather than disease-modifying.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA214178 | Amantadine Hydrochloride | Solution | Patrin Pharma, Inc. |
| ANDA210129 | Amantadine Hydrochloride | Capsule, gelatin coated | Marlex Pharmaceuticals Inc |
| ANDA209035 | Amantadine HCL | Tablet | Direct_Rx |
| ANDA074509 | Amantadine Hydrochloride | Solution | American Health Packaging |
| ANDA074509 | Amantadine Hydrochloride | Solution | Cardinal Health 107, LLC |

Other dosage forms in the record are oral capsule and liquid-filled capsule. The authorization records do not include approved-indication text.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5, model prediction only). The mechanistic link is general pharmacology rather than record-derived, and the package insert safety data are missing (a blocking data gap), so the candidate cannot advance past S0.

**To proceed, the following is needed:**
- FDA package insert (warnings, contraindications, approved indications), which is a blocking gap
- Mechanism of action data from DrugBank
- A targeted literature search on amantadine or NMDA antagonists in Rasmussen encephalitis
- Route and formulation compatibility assessment, which is still pending

**Note on other predictions in this pack:**
- **Myelitis (rank 3, L4):** This is the only prediction with a real evidence trail. It consists of post-polio syndrome fatigue studies, including one double-blind placebo-controlled trial (PMID 7611638, 1995). The link to myelitis is indirect, and the trial's population is unconfirmed from the title alone. It is worth a focused review as a research question.
- **PLA2G6-associated neurodegeneration (rank 4, L4):** The only evidence concerns a different disease, PKAN, and is likely a case-level report. Hold.
- **Transaldolase deficiency (rank 2, L5):** No plausible mechanistic bridge is evident, and it is likely a graph-topology artifact. Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

