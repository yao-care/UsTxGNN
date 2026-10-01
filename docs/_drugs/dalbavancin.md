---
layout: default
title: Dalbavancin
parent: Model Prediction Only (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
---

# Dalbavancin
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

# Dalbavancin: From Gram-Positive Bacterial Infections to Postinfectious Vasculitis

## One-Sentence Summary

Dalbavancin is a long-acting intravenous lipoglycopeptide antibiotic used against Gram-positive bacterial infections.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (the approved indication text was not provided; this is inferred from the drug class and the registered trials) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 authorizations (1 NDA and 3 generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Dalbavancin belongs to the lipoglycopeptide class, and its known activity is against Gram-positive bacteria. It is used against active infections such as skin and soft tissue infection.

The link to the predicted indication is weak. Postinfectious vasculitis is usually immune-complex mediated, so it is driven by the immune response after an infection rather than by persistent bacteria. No antibacterial mechanism clearly applies, and the high graph score may reflect a knowledge-graph association rather than real biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for postinfectious vasculitis.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021883 | DALVANCE | Injection, powder, for solution | Allergan, Inc. |
| ANDA217591 | Dalbavancin Hydrochloride | Injection, powder, for solution | Fresenius Kabi USA, LLC |
| ANDA219465 | Dalbavancin | Injection, powder, for solution | Teva Pharmaceuticals, Inc. |
| ANDA218929 | Dalbavancin | Injection, powder, lyophilized, for solution | Meitheal Pharmaceuticals Inc |

All products are injectables. The approved indication text was not included in the source record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the disease is immune-mediated, so an antibacterial mechanism is not evident. The approval history supports use in active Gram-positive infections only.

**Other predictions in the list (not part of this decision):**
- **Post-bacterial disorder** (rank 2) has 13 dalbavancin trials, including several Phase 3 RCTs. These test active Gram-positive infection, not post-infectious sequelae, so the link is indirect.
- **Orbital cellulitis** (rank 10) is the most mechanistically plausible of the ten, because S. aureus and streptococci are within dalbavancin's spectrum. It is flagged as a research question, but it has no orbital-specific evidence and tissue penetration is unknown.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence that dalbavancin affects immune-mediated vasculitis
- A decision on whether to reprioritize toward an infection-based candidate, such as orbital cellulitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

