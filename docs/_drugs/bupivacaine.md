---
layout: default
title: Bupivacaine
parent: Model Prediction Only (L5)
nav_order: 477
evidence_level: L5
indication_count: 4
---

# Bupivacaine
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

# Bupivacaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is an amide local anesthetic sold in the US as an injectable solution. The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans** (score 99.23%), but **no clinical trials and no publications** support this prediction. It is a model-only signal, and we recommend holding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided license records. Bupivacaine is a local anesthetic by drug class. |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (total licenses, including ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Bupivacaine is an amide local anesthetic that is generally understood to block voltage-gated sodium channels, which stops nerve signal conduction and produces local numbness.

Acrodermatitis chronica atrophicans is a late-stage skin manifestation of *Borrelia* infection (Lyme disease). It is driven by chronic infection and inflammation, not by nerve conduction. We found no plausible causal link between sodium channel blockade and this disease. The high score most likely reflects closeness in the knowledge graph, not pharmacology.

The other three top predictions are neonatal dermatomyositis (99.15%), secondary childhood interstitial lung disease associated with a connective tissue disease (99.11%), and amyopathic dermatomyositis (99.03%). All cluster around dermatomyositis and connective tissue disease, and none has trials or literature. This pattern points to a shared graph artifact, not independent pharmacological signals. At best, a local anesthetic might relieve pain symptomatically, which would not modify the disease. Neonatal use would also raise a separate safety concern for a systemically toxic anesthetic.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA204842 | Bupivacaine Hydrochloride (Asclemed USA, Inc.) | Injection, solution | Not listed |
| NDA016964 | Marcaine (Hospira, Inc.) | Injection, solution | Not listed |
| ANDA204842 | Bupivacaine Hydrochloride (Hikma Pharmaceuticals USA Inc.) | Injection, solution | Not listed |
| ANDA091487 | Bupivacaine Hydrochloride (Fosun Pharma USA Inc.) | Injection, solution | Not listed |
| ANDA070590 | 0.25% Bupivacaine HCl (HF Acquisition Co LLC, DBA HealthFirst) | Injection, solution | Not listed |

All listed products are injectables. No topical or oral formulation appears in the provided data, so route compatibility with a skin-related indication has not been assessed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or publications. No credible mechanism links a sodium channel blocker to a *Borrelia*-related skin disease. Standard treatment for this disease is antibiotics, which bupivacaine does not replace.

**To proceed, the following is needed:**
- The package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data from DrugBank, to support a mechanistic-link analysis
- The approved indication text from the US label
- Any preclinical or clinical evidence linking bupivacaine to the predicted disease
- A route and formulation assessment (all current products are injectables)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

