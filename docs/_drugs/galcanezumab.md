---
layout: default
title: Galcanezumab
parent: Model Prediction Only (L5)
nav_order: 744
evidence_level: L5
indication_count: 3
---

# Galcanezumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Galcanezumab: From Migraine to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Galcanezumab is a monoclonal antibody that neutralizes CGRP (calcitonin gene-related peptide), a class used for migraine. The source data does not list its approved indications, so migraine is inferred from the CGRP mechanism.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US license records (migraine inferred from the CGRP mechanism) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all entries are BLA761063) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known pharmacology, galcanezumab is a monoclonal antibody that neutralizes CGRP, a neuropeptide involved in migraine and vasodilation.

Heparin cofactor 2 is a serpin that inhibits thrombin, mainly through dermatan sulfate. CGRP signaling has no known role in this pathway, so **no plausible mechanistic link was identified**. The high score (0.995) is a graph-based prediction only. It cannot be checked against known pharmacology because the source lacks the drug's original indications and mechanism.

The two other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Antithrombin deficiency type 2 | 99.41% | No mechanistic link. Treatment is anticoagulation or antithrombin replacement, unrelated to CGRP blockade. |
| 3 | Factor 5 excess with spontaneous thrombosis | 99.41% | No mechanistic link. CGRP-pathway inhibitors also raise a vascular-tone and cardiovascular safety question in a thrombosis-prone population. |

All three predictions are likely knowledge-graph artifacts: they have no trials or literature, and all are graded L5 and Hold.

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
| BLA761063 | EMGALITY (Eli Lilly and Company) | Injection, solution | Not listed in source data |

The record contains three entries under the same authorization number, with the same product and dosage form. The only route is injectable.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The three predictions rest only on a graph-model score, with no trials, no literature, and no plausible mechanistic link to coagulation-pathway deficiencies. The safety data is also incomplete, so no safety screening is possible.

**To proceed, the following is needed:**
- The package insert (warnings, contraindications, approved indications), from the FDA website
- Mechanism of action data, from DrugBank
- Any preclinical or mechanistic evidence connecting CGRP blockade to the heparin cofactor 2 or antithrombin pathways
- A cardiovascular and thrombosis safety assessment before considering any use in thrombosis-prone populations

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

