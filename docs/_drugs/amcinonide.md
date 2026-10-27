---
layout: default
title: Amcinonide
parent: Model Prediction Only (L5)
nav_order: 323
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Amcinonide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Corticosteroid-responsive dermatoses (e.g., atopic eczema…"
monitor_inn: "AMCINONIDE"
predicted_indications: ["vulvar inverted follicular keratosis", "hypertrophic lichen planus", "lichen planus pigmentosus", "annular atrophic lichen planus", "lichen planus pemphigoides", "primary cutaneous B-cell lymphoma", "2-hydroxyethyl methacrylate sensitization"]
---

# Amcinonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Amcinonide: From Corticosteroid-Responsive Dermatoses to Vulvar Inverted Follicular Keratosis
{: .text-alpha }

## One-Sentence Summary

Amcinonide is a topical corticosteroid, originally used for inflammatory skin conditions such as atopic, contact and seborrheic dermatitis.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Corticosteroid-responsive dermatoses (e.g., atopic eczema, contact dermatitis, seborrheic dermatitis) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorization) |
| Number of NDAs | 4 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amcinonide is a mid-to-high potency topical corticosteroid. Its efficacy in inflammatory dermatoses is established, and it is also listed for seborrheic keratosis, a related benign keratinocytic lesion. The model's prediction likely extends from that link.

The mechanistic case is weak, however. Inverted follicular keratosis is a keratinocytic proliferation that is usually treated by excision. An anti-inflammatory steroid is unlikely to resolve it. Applying a potent steroid to vulvar mucosa also increases absorption and the risk of local skin atrophy. The high score (99.82%) therefore reflects a statistical association in the knowledge graph, not demonstrated biology or clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this predicted indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA076229 | Amcinonide | Cream | INA Pharmaceutics Inc. | Cancelled |
| ANDA076065 | Amcinonide | Cream | Fougera Pharmaceuticals Inc. | Cancelled |
| ANDA076367 | Amcinonide | Ointment | Sun Pharmaceutical Industries, Inc. | Cancelled |
| ANDA076096 | Amcinonide | Ointment | Ayurax, LLC | Cancelled |

All four authorizations are cancelled, so there is currently no marketed amcinonide product in the US. Approved indication text was not available for these entries.

## Safety Considerations

- **Conditions flagged as contraindications or cautions** (from the drug-disease knowledge graph, not from label text): type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, glaucoma, skin atrophy, peripheral vascular disease (including intermittent claudication and peripheral arterial disease), and cutaneous tuberculosis. Skin atrophy is especially relevant to a vulvar application site.
- **Drug Interactions**: 44 interactions were identified. The 20 detailed entries are all rated **Minor** and involve antidiabetic agents:
  - Metformin, pioglitazone, acarbose and sitagliptin
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
  - GLP-1 agonists (semaglutide, dulaglutide, albiglutide)
  - Chlorpropamide and many insulin products

  This is consistent with corticosteroids potentially raising blood glucose.
- **Sensitization**: Published case reports document allergic contact dermatitis to amcinonide itself, with cross-reactions to other corticosteroids such as budesonide and triamcinolone.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or literature. Inverted follicular keratosis is typically managed surgically, and steroid use on the vulva carries atrophy risk. Amcinonide currently has no valid US authorization.

**To proceed, the following is needed:**
- Any clinical or case-level evidence of topical corticosteroids in inverted follicular keratosis
- Mechanism of action data and the package insert warnings and contraindications
- Confirmation of product availability, given that all US authorizations are cancelled

**Other predictions for this drug:**
- **Dermatitis** (score 99.30%) has the strongest support at L3. It rests on historical double-blind comparisons against halcinonide and betamethasone valerate in eczematous dermatitis. This is essentially an existing labeled use, with a contact-sensitization guardrail needed (Proceed with Guardrails).
- **Hypertrophic lichen planus**, **lichen planus pigmentosus** and **annular atrophic lichen planus** (each 99.73%) are plausible within the corticosteroid class, but have no amcinonide-specific data (Research Question).
- **Lichen planus pemphigoides**, **primary cutaneous B-cell lymphoma** and **2-hydroxyethyl methacrylate sensitization** are low-priority (Hold).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

