---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 650
evidence_level: L5
indication_count: 3
monitor_inn: "EMPAGLIFLOZIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
last_modified_at: 2026-10-14
description: "Empagliflozin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the approved-indication text was not available in the US license records; this is taken from the knowledge-graph indication data) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 3 listed authorizations are cancelled) |
| Number of NDAs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, empagliflozin is an SGLT2 inhibitor that lowers renal glucose reabsorption, and its efficacy in type 2 diabetes is established. However, nothing in the data compiled for this report supports a mechanistic link to stiff person syndrome.

Stiff person syndrome is an autoimmune neurological disorder, typically associated with anti-GAD65 antibodies and impaired GABAergic inhibition. Empagliflozin has no known action on these pathways. The only possible connection is that SGLT2 inhibitors might influence immune or metabolic pathways, and that stiff person syndrome often co-occurs with type 1 diabetes and other autoimmune conditions. This is speculative.

Two other predictions show the same weakness:
- **Focal stiff limb syndrome** (score 99.06%), a variant of the stiff person spectrum, received a score identical to classic stiff person syndrome. This suggests the prediction comes from shared disease-graph neighbours rather than independent evidence.
- **Opsismodysplasia** (score 99.03%) is a rare skeletal dysplasia linked to INPPL1 (SHIP2) mutations, which affect insulin and PI3K/AKT signalling. This gives a loose conceptual connection to glucose and insulin pathways, but no evidence shows empagliflozin modifies this pathology. The patient population is extremely small and mostly paediatric, which raises additional safety considerations.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204629 | JARDIANCE (A-S Medication Solutions) | Film-coated tablet | Not available (status: cancelled) |
| NDA208658 | Synjardy (Boehringer Ingelheim) | Extended-release tablet | Not available (status: cancelled) |
| NDA206111 | Synjardy (Boehringer Ingelheim) | Tablet | Not available (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs, mostly of Moderate severity and some Minor. The 20 shown in the data include:
  - **Moderate**: phenylephrine, acebutolol, acetazolamide, formoterol, pseudoephedrine, nifedipine, epinephrine, ethinylestradiol, hydrocortisone, salbutamol, ethanol, fosamprenavir, fosinopril, fosphenytoin, fostamatinib, fostemsavir, furosemide, gemifloxacin
  - **Minor**: topical hydrocortisone, topical alclometasone

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (99.06%), with no registered trials, no publications, and no plausible mechanistic link between SGLT2 inhibition and the autoimmune, GABAergic pathology of stiff person syndrome. The identical score for focal stiff limb syndrome suggests a graph-neighbour artefact. All US authorizations listed are cancelled.

**To proceed, the following is needed:**
- Mechanism of action data for empagliflozin
- Package insert warnings and contraindications, which are required for safety screening
- Preclinical or mechanistic evidence linking SGLT2 inhibition to stiff person syndrome pathology (for example, anti-GAD65 autoimmunity or GABAergic signalling)
- Confirmation of current US market and approval status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

