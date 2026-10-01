---
layout: default
title: Besifloxacin
parent: Model Prediction Only (L5)
nav_order: 453
evidence_level: L5
indication_count: 8
---

# Besifloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Besifloxacin: From Bacterial Conjunctivitis to Bronchitis

## One-Sentence Summary

Besifloxacin is a fluoroquinolone antibacterial marketed as an ophthalmic suspension (Besivance) for eye infections. The TxGNN model predicts it may be effective for **bronchitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model prediction only, and the route of administration is a major obstacle.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular bacterial infection (bacterial conjunctivitis). The license record has no indication text, so this is inferred from the Besivance trials |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license entries (both under NDA022308, listed under two Bausch & Lomb entities) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, besifloxacin belongs to the fluoroquinolone class of broad-spectrum antibacterials. Its efficacy in ocular bacterial infection is established, and other fluoroquinolones are used systemically for respiratory infections. That class-level link may explain the high TxGNN score.

The link is weak in practice. Besifloxacin is marketed only as an ophthalmic suspension with minimal systemic absorption, so it is unlikely to reach bronchial tissue at useful concentrations. The score most likely reflects graph similarity within the fluoroquinolone class rather than a plausible route of exposure.

Route compatibility has not been assessed, and no besifloxacin trials or literature exist for bronchitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022308 | Besivance (Bausch & Lomb Americas Inc.) | Suspension | Not specified in the license record |
| NDA022308 | Besivance (Bausch & Lomb Incorporated) | Suspension | Not specified in the license record |

---

## Safety Considerations

Please refer to the package insert for safety information.

A Phase 1 pharmacokinetic study in bacterial conjunctivitis (NCT00407589) supports low systemic exposure after ophthalmic use. This also limits any relevance to a respiratory indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on class-level model similarity only (L5). No trials or literature support bronchitis, and the ophthalmic-only formulation makes therapeutic exposure in the bronchi implausible.

**To proceed, the following is needed:**
- The FDA package insert (warnings and contraindications), which blocks the safety screen
- Mechanism of action data (DrugBank)
- A route and formulation feasibility assessment. This would require a non-ophthalmic formulation, which does not currently exist
- A targeted literature search on besifloxacin in respiratory infection
- Note: among the other predictions, the rank 3 "post-bacterial disorder" has six besifloxacin trials, but all are ocular and indirect. Rank 8 "otitis externa" has a class-level rationale (topical fluoroquinolones), but no besifloxacin data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

