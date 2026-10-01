---
layout: default
title: Diethylpropion
parent: Model Prediction Only (L5)
nav_order: 604
evidence_level: L5
indication_count: 4
---

# Diethylpropion
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

# Diethylpropion: From Obesity Management to Hypervitaminosis

## One-Sentence Summary

Diethylpropion is a sympathomimetic appetite suppressant, marketed in the US as an anti-obesity drug.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but **0 clinical trials** and **0 publications** currently support this prediction.
It is a model-only signal (Evidence Level L5), and no plausible mechanistic link has been found.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Appetite suppression / obesity management (the license records list no indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Diethylpropion is a sympathomimetic amine appetite suppressant that acts through catecholamine (noradrenaline and dopamine) release. Its use is established for weight management, but that does not extend to hypervitaminosis.

Hypervitaminosis is a toxicity state. It is managed by stopping the vitamin and giving supportive care, and an appetite suppressant has no known role in that. The 99.99% score is a model output only. It is not backed by any trial, publication, or mechanistic evidence, so it should not be read as a therapeutic signal.

The other top predictions show the same pattern:
- **Proximal 16p11.2 microdeletion syndrome:** the only tenuous link is that the syndrome is associated with early-onset obesity. Diethylpropion might help with symptom-level weight control, but it would not treat the genetic syndrome. The syndrome also has neurodevelopmental and psychiatric features, so a stimulant raises safety concerns.
- **Obsolete hypertelorism (disease):** hypertelorism is a structural craniofacial anomaly that a drug cannot correct. The ontology term is marked obsolete, which suggests a knowledge-graph artifact.
- **Frontorhiny:** this is a congenital developmental malformation with no known pathway to diethylpropion's pharmacology. The high score most likely reflects graph proximity through shared genetic-syndrome nodes.

None of the four predictions has clinical trial or literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The table lists 5 of the 20 authorizations. All are ANDAs, and none of the records includes approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA091680 | Diethylpropion Hydrochloride ER | Tablet, extended release | Chartwell RX, LLC. |
| ANDA200177 | Diethylpropion | Tablet | Chartwell RX, LLC. |
| ANDA091680 | Diethylpropion Hydrochloride | Tablet, extended release | Proficient Rx LP |
| ANDA201212 | Diethylpropion Hydrochloride | Tablet | Bryant Ranch Prepack |
| ANDA200177 | Diethylpropion Hydrochloride | Tablet | PD-Rx Pharmaceuticals, Inc. |

Both available forms (immediate-release tablet and extended-release tablet) are oral.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found. As a sympathomimetic stimulant, diethylpropion would need particular caution in any population with neurodevelopmental or psychiatric features, such as the 16p11.2 microdeletion syndrome.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no publications, and no plausible mechanistic link to hypervitaminosis. Mechanism of action and safety data are also missing. The evidence is not sufficient to move forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap, so safety screening cannot start without them)
- Detailed mechanism of action data (for example, from DrugBank)
- A credible pharmacological rationale linking catecholamine release to hypervitaminosis, plus any supporting preclinical or clinical evidence
- Confirmation of the approved indication text for the US labels, which is empty in the current records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

