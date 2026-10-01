---
layout: default
title: Terazosin
parent: Model Prediction Only (L5)
nav_order: 1211
evidence_level: L5
indication_count: 10
---

# Terazosin
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

# Terazosin: From Alpha-1 Blocker Use (Hypertension/BPH) to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Terazosin is an oral alpha-1 adrenergic blocker, generally used for hypertension and benign prostatic hyperplasia.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but this is a **model prediction only**, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US license records; generally hypertension and benign prostatic hyperplasia (general pharmacological knowledge) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed records are generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, terazosin is an alpha-1 adrenergic antagonist that relaxes vascular and prostatic smooth muscle.

The link to the predicted indication is weak. Hypotrichosis simplex is a monogenic hair-follicle disorder, and a vasodilator or alpha-1 antagonist is unlikely to address the underlying defect. The high score most likely reflects knowledge-graph proximity to other hair-loss conditions rather than a validated biological effect.

The most an analyst could suggest is an indirect effect through improved scalp microcirculation, as discussed for some vasoactive drugs. Alpha-1 blockade has not been shown to promote hair growth.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The `approved_indication_text` field is empty for all listed records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075317 | Terazosin (Jubilant Cadista) | Capsule | Not listed |
| ANDA074823 | Terazosin Hydrochloride (Aphena Pharma Solutions) | Capsule | Not listed |
| ANDA075317 | Terazosin (Aphena Pharma Solutions) | Capsule | Not listed |
| ANDA075667 | Terazosin (Bionpharma) | Capsule | Not listed |
| ANDA075614 | Terazosin (Chartwell RX) | Capsule | Not listed |

Only the oral capsule route is available (5 of 20 authorizations shown).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model prediction (L5) with no trials, no literature, and no plausible mechanism for a monogenic hair-follicle disorder. Nothing supports moving forward on this indication.

**To proceed, the following is needed:**
- The US package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example, from DrugBank)
- Any preclinical evidence of a hair-follicle effect of alpha-1 blockade

**Other predictions for this drug:** The pack's other predicted indications look more credible than this top-ranked one. **Raynaud disease** (a 1997 clinical study) and **migraine disorder** (a 1994 small open study and a 1997 review) are both rated L3 and flagged as "Research Question". Both are old, small, and uncontrolled, so a modern controlled trial would be needed, with attention to hypotension and dizziness. Consider prioritizing those two over the hair-related predictions.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

