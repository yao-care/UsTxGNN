---
layout: default
title: Tropicamide
parent: Model Prediction Only (L5)
nav_order: 1269
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tropicamide: From Ophthalmic Antimuscarinic Use to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a short-acting antimuscarinic marketed in the US as an ophthalmic solution (eye drops).
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided US records (marketed as an ophthalmic solution) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tropicamide is a short-acting antimuscarinic agent. Its use in the eye is established, and mechanistically it could be relevant to conditions in which blocking muscarinic receptors helps.

The most plausible link to cauda equina syndrome is indirect. Antimuscarinic drugs treat the neurogenic bladder dysfunction that often accompanies the condition. That would address a symptom only. The underlying compressive nerve injury needs surgical decompression, and a drug would not treat it.

There are also practical doubts. Tropicamide is formulated as eye drops with minimal systemic exposure, so it is doubtful it could produce meaningful antimuscarinic effects at the bladder. The high score is not backed by any trial or publication in this evidence pack.

The model also ranked two other candidates just below this one:

- **Neurogenic bladder (score 99.13%)**: biologically coherent, since antimuscarinics such as oxybutynin are established therapy for neurogenic detrusor overactivity. However, the disease term is flagged as obsolete in the ontology and should be remapped to a current term (for example, neurogenic detrusor overactivity). Better-characterized antimuscarinics also already exist for this use.
- **Irritable bowel syndrome (score 99.12%)**: a class-level link exists, because antimuscarinic antispasmodics are used for IBS abdominal pain. There is no tropicamide-specific data, and the eye-drop route gives little gut exposure.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA040064 | Tropicamide | Solution/drops | Bausch & Lomb Incorporated |
| ANDA084306 | Mydriacyl | Solution/drops | Alcon Laboratories, Inc. |
| ANDA040067 | Tropicamide | Solution/drops | Bausch & Lomb Incorporated |
| ANDA084306 | Mydriacyl | Solution/drops | Alcon Laboratories, Inc. |
| ANDA207524 | Tropicamide | Solution/drops | Sportpharm LLC |

Approved indication text was not included in the provided records. The ANDA084306 entry appears twice in the source data. The pack reports 9 licenses in total; only 5 are shown above.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no trials or publications. The only plausible mechanism is symptomatic (bladder dysfunction), and an ophthalmic product is unlikely to reach the relevant tissues at effective levels.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- A literature and trial search for tropicamide or antimuscarinics in cauda equina syndrome and neurogenic bladder
- Remapping of the obsolete "neurogenic bladder" term to a current ontology term
- A feasibility assessment of whether a systemic or urological formulation or route is realistic, since route compatibility is still pending
- Consideration of whether established antimuscarinics should be prioritized over tropicamide for the bladder and gut candidates

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

