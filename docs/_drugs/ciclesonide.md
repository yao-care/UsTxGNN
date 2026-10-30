---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 528
evidence_level: L5
indication_count: 5
monitor_inn: "CICLESONIDE"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis"]
last_modified_at: 2026-10-30
description: "Ciclesonide: predicted new indication atopic eczema (evidence level L5). Approved use: Not recorded in the local data"
---

# Ciclesonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ciclesonide: inhaled corticosteroid (glucocorticoid receptor agonist prodrug) → atopic eczema
{: .text-alpha }

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid prodrug that is converted to its active form, des-ciclesonide, a glucocorticoid receptor agonist with anti-inflammatory activity.
The TxGNN model predicts it may be effective for **atopic eczema**, with a score of 0.9996.
Currently **no clinical trials and no publications** directly study this use, so the prediction rests on the model and mechanistic reasoning alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | atopic eczema |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ciclesonide is a prodrug that is activated to des-ciclesonide, which binds the glucocorticoid receptor and suppresses inflammatory signalling. Detailed mechanism of action data is not otherwise available in the data compiled for this report.

Topical corticosteroids are standard therapy for atopic eczema, a chronic inflammatory skin disease. A glucocorticoid-receptor-mediated anti-inflammatory action is therefore plausible in this condition.

However, this is a computational prediction only. No studies of ciclesonide in atopic eczema were found, and route compatibility (an inhaled or nasal product versus a skin product) has not been assessed. The model also lists "dermatitis, atopic" among its predictions, which is essentially the same disease and is not a separate line of evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for atopic eczema.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021658 | Alvesco | Metered aerosol | Not recorded in the local data |
| NDA022004 | Omnaris | Nasal spray | Not recorded in the local data |

Both are single-ingredient products from Covis Pharma US, Inc.

---

## Safety Considerations

- **Drug Interactions**: 63 interactions were recorded. Notable examples:
  - **Major**: cladribine.
  - **Moderate**: clarithromycin, miconazole, cobicistat, atazanavir, fosamprenavir, amprenavir, boceprevir, ceritinib, conivaptan, fostamatinib, inhaled rapid-acting human insulin, topical abametapir.
  - **Minor**: formoterol, salbutamol, arformoterol.
- **Conditions flagged as contraindicated in the data compiled for this report (not label text)**: herpes simplex virus keratitis, adrenocortical insufficiency, Addison disease, osteoporosis, postmenopausal osteoporosis, fungal infectious disease, dermatophytosis, ocular hypertension, glaucoma, and parasitic infection.
- **Related hypersensitivity signal**: a published case report describes systemic allergic dermatitis from inhaled budesonide with cross-reactivity to ciclesonide on patch testing, so corticosteroid contact allergy is a consideration.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9996), but there are no clinical trials or publications for ciclesonide in atopic eczema, so the evidence level is L5. The mechanism is plausible, yet established topical corticosteroids already exist for this disease. Whether a ciclesonide product could be delivered to the skin has not been assessed.

**To proceed, the following is needed:**
- Preclinical or early clinical data for ciclesonide in atopic eczema
- Route and formulation compatibility assessment (inhaled or nasal versus topical)
- Complete mechanism of action data
- Package insert warnings and contraindications, including the cross-reactivity and systemic corticosteroid effects
- A comparison against existing topical corticosteroids to show added value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

