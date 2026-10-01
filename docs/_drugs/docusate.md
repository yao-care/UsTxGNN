---
layout: default
title: Docusate
parent: Model Prediction Only (L5)
nav_order: 618
evidence_level: L5
indication_count: 2
---

# Docusate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Docusate: From Stool Softening (Constipation) to Plummer-Vinson Syndrome

## One-Sentence Summary

Docusate is an over-the-counter stool softener (an anionic surfactant) used for constipation.
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on a model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Stool softener (inferred from product names; the label indication text is not recorded in the input) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, docusate is an anionic surfactant stool softener with minimal systemic absorption. Its use is for softening stool, and there is no mechanistic basis for applying it to Plummer-Vinson syndrome.

Plummer-Vinson syndrome involves iron-deficiency anemia, difficulty swallowing (dysphagia) and esophageal webs. Nothing links docusate to any of these. The high score (0.992) is a knowledge-graph proximity result only. The one speculative idea is that a surfactant could alter mucosal permeability and so affect iron absorption. That idea is unsupported, and the effect could just as plausibly be harmful as helpful.

A second prediction, **vitamin B12- and folate-independent constitutional megaloblastic anemia** (score 99.15%), also has no supporting trials, literature or interaction data. Docusate has no known action on nucleotide synthesis, blood-cell formation or vitamin metabolism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Docusate is marketed in the US through 20 authorizations. Five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M007 | Stool Softener | Capsule, liquid filled | Strategic Sourcing Services LLC |
| M007 | DOCUSATE SODIUM 100mg Two-Tone | Capsule, liquid filled | Humanwell PuraCap Pharmaceutical (Wuhan), Ltd. |
| M007 | DOCUSATE SODIUM 100mg Two-Tone | Capsule, liquid filled | Discount Drug Mart, Inc |
| M007 | DOCUSATE SODIUM, EXTRA STRENGTH | Capsule, gelatin coated | Advanced Rx LLC |
| M007 | Stool Softener | Capsule, liquid filled | EQUATE (Wal-Mart Stores, Inc.) |

Available forms include oral capsules (liquid filled, gelatin coated) and a liquid.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no trials or publications, and no plausible mechanism connects a minimally absorbed stool softener to Plummer-Vinson syndrome. Potential harm to iron absorption cannot be excluded.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block any safety screening
- Mechanism of action data (for example from DrugBank) to test whether any biological link exists
- A literature search for any evidence linking docusate to iron absorption or esophageal disease
- Review of route compatibility, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

