---
layout: default
title: Lubiprostone
parent: Model Prediction Only (L5)
nav_order: 875
evidence_level: L5
indication_count: 10
---

# Lubiprostone
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

# Lubiprostone: From Constipation to Alopecia

## One-Sentence Summary

Lubiprostone is a ClC-2 chloride channel activator marketed in the US for constipation.
The TxGNN model predicts it may be effective for **alopecia**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation (per the mechanism notes; the license records contain no indication text) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Lubiprostone is a ClC-2 chloride channel activator that acts on the gut epithelium, and its efficacy in constipation is established.

No credible pathway links this mechanism to hair follicle biology. The high score (0.9993) reflects proximity in the knowledge graph, not documented biology. Systemic exposure to lubiprostone is also very low, which weakens any speculative link to a skin or hair target.

The other top predictions fall into two groups. The hair-related conditions are:

- Congenital hypotrichosis milia
- Hypotrichosis simplex of the scalp
- Diffuse alopecia areata

The vascular and cardiopulmonary conditions are:

- Pulmonary hypertension
- Raynaud disease
- Peripheral vascular disease

For the vascular group, lubiprostone is a prostone, a prostaglandin-related fatty acid derivative, so a vasodilation rationale is conceivable. It remains unsupported by data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

For reference, the only trial linked to any of the top 10 predictions is [NCT02813369](https://clinicaltrials.gov/study/NCT02813369), attached to pulmonary hypertension. It is a terminated observational safety study of naloxegol, a different drug, and provides no evidence for lubiprostone.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| NDA021908 | Amitiza | Capsule, gelatin coated | SpecGx LLC |
| ANDA218640 | Lubiprostone | Capsule | Northstar Rx LLC |
| ANDA214131 | Lubiprostone | Capsule | Zydus Pharmaceuticals USA Inc. |
| ANDA209920 | Lubiprostone | Capsule, gelatin coated | Teva Pharmaceuticals, Inc. |

All listed products are oral. The record contains no approved-indication text. ANDA214131 appears twice in the source and is shown once.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials, no literature, and no plausible mechanistic link between ClC-2 activation and hair loss disorders. Evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data from DrugBank
- A mechanistic hypothesis linking ClC-2 or prostone pharmacology to hair follicle biology, plus preclinical evidence
- A route-compatibility assessment, since only oral products are marketed and alopecia treatment would likely need topical or other delivery
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

