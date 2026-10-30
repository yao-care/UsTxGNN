---
layout: default
title: Ethosuximide
parent: Model Prediction Only (L5)
nav_order: 682
evidence_level: L5
indication_count: 1
monitor_inn: "ETHOSUXIMIDE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
last_modified_at: 2026-10-30
description: "Ethosuximide: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ethosuximide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ethosuximide: Nephrogenic syndrome of inappropriate antidiuresis
{: .text-alpha }

## One-Sentence Summary

Ethosuximide was originally used to treat absence epilepsy.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 6 of 7) |
| Number of FDA Applications | 7 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ethosuximide is generally known as a T-type calcium channel blocker acting on thalamic neurons, which is how it controls absence seizures.

NSIAD is a different kind of disease. It is caused by gain-of-function changes in the vasopressin V2 receptor (AVPR2), or in some cases by GNAS-related signaling. These changes make the kidney collecting duct reabsorb too much water. A link between T-type calcium channel blockade and V2 receptor signaling or aquaporin-2 regulation in the kidney is speculative and has not been demonstrated.

The very high TxGNN score (0.9991) comes from the TxGNN model (deep learning) and is a model prediction only. It may reflect similarities the model learned between related diseases, not biological evidence. This prediction should be treated as a hypothesis, not as supported evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All seven US authorizations are valid. The data compiled for this report contains no approved-indication text for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA210654 | Ethosuximide (Epic Pharma) | Capsule | Not available (valid) |
| ANDA200892 | Ethosuximide (Chartwell RX) | Capsule | Not available (valid) |
| NDA012380 | Zarontin (Parke-Davis/Pfizer) | Capsule | Not available (valid) |
| ANDA080258 | Zarontin (Parke-Davis/Pfizer) | Solution | Not available (valid) |
| ANDA040253 | Ethosuximide (PAI Pharma) | Solution | Not available (valid) |

Two further cancelled authorizations are not listed here: ANDA211928 (Strides Pharma, capsule) and ANDA040430 (Bryant Ranch Prepack, liquid-filled capsule).

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The knowledge graph links ethosuximide to contraindication-type relationships with the following conditions. These should be confirmed against the official label.
  - Blood and immune: hematologic disease, neutropenia, agranulocytosis, systemic lupus erythematosus (including the pediatric form)
  - Liver, kidney and biliary: liver disease, kidney disease, gallbladder disease, pyoureter
  - Metabolic: acute intermittent porphyria
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder
- **Drug Interactions:** 92 interactions were found. The 20 detailed in the data are all rated Moderate. Main ones include:
  - Central nervous system depressants and opioids: morphine (including liposomal), opium, ethanol, dronabinol, nabilone, promethazine, chlorpheniramine
  - Antiemetics and related drugs: aprepitant, metoclopramide, sibutramine
  - Antimalarials: chloroquine, mefloquine, hydroxychloroquine
  - Folate-related drugs: folic acid, leucovorin, levoleucovorin
  - Other: cobicistat, deferasirox, fostamatinib

The kidney disease association matters for this candidate, because the predicted indication is a kidney-related condition. Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it. The knowledge graph also flags kidney disease as a contraindication-type association.

**To proceed, the following is needed:**
- Detailed mechanism of action data, to test whether any plausible link to AVPR2/aquaporin-2 signaling exists
- FDA package insert warnings and contraindications, to complete the safety screening
- Preclinical or mechanistic studies, such as renal cell or animal models of V2 receptor gain-of-function
- A literature and trial registry search for any case reports linking ethosuximide to water balance or hyponatremia
- Assessment of route compatibility and formulation availability, given that all seven US authorizations are valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

