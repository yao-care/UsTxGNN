---
layout: default
title: Tolcapone
parent: Model Prediction Only (L5)
nav_order: 1239
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapone: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Tolcapone is a COMT inhibitor used as an adjunct to levodopa in Parkinson's disease.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but this prediction currently has **0 clinical trials** and **0 publications** behind it. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (adjunct to levodopa; the license records supplied contain no indication text, so this comes from the prediction rationale) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 authorizations (NDA020697 appears twice, plus ANDA208937) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, tolcapone is a peripheral and central COMT inhibitor that acts on catecholamine metabolism. It prolongs the effect of levodopa in Parkinson's disease.

The link to the new indication is weak. Rasmussen encephalitis is a T-cell-mediated neuroinflammatory epilepsy, and COMT inhibition has no established role in immune-driven brain inflammation. The high TxGNN score comes from graph-based similarity and is not backed by any trial or publication. This prediction should be treated as a hypothesis with no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020697 | Tolcapone | Tablet, film coated | Oceanside Pharmaceuticals |
| ANDA208937 | Tolcapone | Tablet | Ingenus Pharmaceuticals, LLC |
| NDA020697 | Tasmar | Tablet, film coated | Bausch Health US LLC |

All products are oral. Approved indication text was not provided in the license records.

## Safety Considerations

- **Hepatotoxicity**: The prediction rationale notes a boxed hepatotoxicity warning for tolcapone. Any clinical exploration would need hepatic monitoring.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support (L5) and no plausible mechanistic link between COMT inhibition and Rasmussen encephalitis. The boxed hepatotoxicity warning adds risk without any known benefit.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank)
- Package insert warnings and contraindications, which are needed before any safety screening
- Any preclinical or clinical signal linking COMT inhibition to neuroinflammatory epilepsy

**Other candidates worth noting:**
- **Lewy body dementia** (score 99.64%, L4, Research Question): two preclinical papers support the dopamine and alpha-synuclein pathway, but there is no clinical evidence for tolcapone.
- **Juvenile parkinsonism of Hunt** (score 99.52%, L5, Research Question): mechanistically plausible given tolcapone's Parkinson's use, but no supporting trials or publications. Whether the existing label covers this population needs separate clinical and regulatory review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

