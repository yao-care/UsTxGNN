---
layout: default
title: Secretin Human
parent: Model Prediction Only (L5)
nav_order: 1149
evidence_level: L5
indication_count: 10
---

# Secretin Human
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

# Secretin Human: From Pancreatic Secretion Stimulation to Open-Angle Glaucoma

## One-Sentence Summary

Human secretin is a gastrointestinal peptide hormone that stimulates pancreatic bicarbonate secretion, and it is marketed in the US as ChiRhoStim.
The TxGNN model predicts it may be effective for **open-angle glaucoma**, but **0 clinical trials** and **0 publications** currently support this direction.
This is a model-only prediction with no mechanistic or clinical backing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed (approved indication text is empty in the source data) |
| Predicted New Indication | Open-angle glaucoma |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Human secretin acts on the secretin receptor, a Class B GPCR that signals through cAMP, to stimulate pancreatic bicarbonate secretion.

No established link connects this pathway to open-angle glaucoma, which involves impaired aqueous humour outflow and raised intraocular pressure. The high score most likely reflects proximity in the knowledge graph rather than a biological mechanism. Similarity to the original indication has not been assessed, and route compatibility is also pending. Human secretin is an injectable lyophilised powder, and no ocular delivery route has been evaluated.

The other top-ranked predictions are primary hereditary glaucoma, several hair disorders (alopecia, hypotrichosis, hypertrichosis) and rare congenital syndromes. None has trial or literature support, and the hair-disorder cluster looks like a graph-neighbourhood artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021256 | ChiRhoStim | Lyophilised powder for injection | Not listed |
| NDA021256 | ChiRhoStim 40 | Lyophilised powder for injection | Not listed |

Manufacturer for both products: ChiRhoClin, Inc.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials or relevant publications, and no plausible mechanism connects secretin receptor signalling to glaucoma. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block safety screening
- Mechanism of action data, for example from DrugBank
- Approved indication text, to establish the original indication
- A mechanistic rationale linking secretin receptor signalling to aqueous outflow or intraocular pressure, plus preclinical evidence
- A route and formulation assessment for ocular delivery

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

