---
layout: default
title: Clobazam
parent: Model Prediction Only (L5)
nav_order: 536
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam: Repurposing Prediction for Febrile Infection-Related Epilepsy Syndrome (FIRES)

## One-Sentence Summary

Clobazam is a benzodiazepine anti-seizure medication marketed in the US as tablets, oral suspension, and oral film. The TxGNN model predicts it may be useful for **febrile infection-related epilepsy syndrome (FIRES)**, but there are **0 clinical trials** and only **2 publications**, and neither studies clobazam (they cover lorazepam and perampanel). This is a model-only signal with no direct clinical support.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (the Evidence Pack lists L4, but neither retrieved paper studies clobazam) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank field. The Evidence Pack's rationale describes clobazam as a GABA-A positive allosteric modulator (a benzodiazepine). This mechanism is plausible for refractory status epilepticus, and FIRES is a form of new-onset refractory status epilepticus in previously healthy children.

The data does not state clobazam's original approved indication, and the US license records carry no indication text. The relationship between the original and new indication therefore cannot be assessed here.

The two retrieved papers support only the general benzodiazepine-class idea. One is a case series on enteral lorazepam for weaning midazolam-dependent patients. The other is a case report on perampanel for reducing barbiturate dependency. Neither contains clobazam-specific data, so the high TxGNN score remains a prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case series | Epileptic Disorders | Enteral lorazepam worked as a weaning substitute in midazolam-dependent FIRES patients. Lorazepam, not clobazam. |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case report | Cureus | A 13-year-old with FIRES; perampanel may reduce barbiturate dependency. Perampanel, not clobazam. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA210833 | SYMPAZAN | Film | Aquestive Therapeutics |
| NDA202067 | Onfi | Tablet | Lundbeck Pharmaceuticals LLC |
| ANDA210978 | Clobazam | Suspension | Taro Pharmaceuticals U.S.A., Inc. |
| ANDA213039 | Clobazam | Suspension | Ascend Laboratories, LLC |

The data lists 20 licenses in total; 4 distinct ones are shown here (Onfi appears twice in the source). Approved indication text is not included in the records.

## Safety Considerations

Please refer to the package insert for safety information.

The Evidence Pack's rationale for other predicted indications mentions sedation, behavioral adverse events, tolerance, and CYP2C19/CYP3A4 interactions as points to watch. This is not label-sourced data. No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The FIRES prediction rests on the model score and class-level reasoning alone. There are no trials, and neither paper studies clobazam.

**To proceed, the following is needed:**
- Clobazam-specific evidence in FIRES or refractory status epilepticus, such as case series or registry data
- The clobazam package insert (warnings, contraindications, approved indications) to confirm labeled uses and safety
- Mechanism of action data from DrugBank
- Better-supported indications in the same list. "Childhood onset epileptic encephalopathy" (rank 6) has the most literature, including Lennox-Gastaut reviews. Clobazam may already be labeled for it, which would make it a non-repurposing signal. Verify this against the label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

