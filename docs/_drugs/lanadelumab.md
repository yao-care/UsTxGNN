---
layout: default
title: Lanadelumab
parent: Model Prediction Only (L5)
nav_order: 832
evidence_level: L5
indication_count: 9
monitor_inn: "LANADELUMAB"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pancreatitis", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "Glanzmann thrombasthenia", "antisynthetase syndrome", "focal myositis", "Scott syndrome"]
last_modified_at: 2026-11-20
description: "Lanadelumab: predicted new indication Serpinopathy with toxic serpin polymerization (evidence level L5). In the US: 1 FDA application (1 active)"
---

# Lanadelumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Lanadelumab: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## One-Sentence Summary

Lanadelumab is a monoclonal antibody that inhibits plasma kallikrein and is already marketed in the US.
The TxGNN model predicts it may be effective for **serpinopathy with toxic serpin polymerization**, with a score of 0.9999.
No clinical trials or publications supporting this prediction were found, so it rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Serpinopathy with toxic serpin polymerization |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for lanadelumab: "Lanadelumab-flyo is a fully human monoclonal antibody (IgG1/κ-light chain) that binds plasma kallikrein and inhibits its proteolytic activity. Plasma kallikrein is a protease that cleaves high-molecular-weight-kininogen (HMWK) to generate cleaved HMWK (cHMWK) and bradykinin, a potent vasodilator that increases vascular permeability resulting in swelling and pain associated with HAE." ([DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8), label version 2026-09-18; accessed 2026-11-19.) Pharmacology data shows that lanadelumab is an antibody directed at plasma kallikrein (KLKB1), the target of its inhibitory action.

The prediction most likely reflects the model's association between the drug's biology and the serpin protein family. Its only support is the high score.

The mechanistic fit is weak. Toxic serpin polymerization is a gain-of-function, proteotoxic process, and inhibiting plasma kallikrein would not be expected to correct it. The link should therefore be treated as a hypothesis from the model, not as an established pharmacological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761090 | TAKHZYRO (Takeda Pharmaceuticals America, Inc.) | Solution (injection, solution) | Not specified in the data; status: valid |

The local data lists one valid biologics licence, and the market status is marketed.

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacology entry. It identifies kallikrein B1 (KLKB1) as the drug's intended target, not a separate interacting drug. No graded drug-drug interactions are listed.

Please refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or publications, and a plausible mechanistic link to plasma kallikrein inhibition is lacking.

**To proceed, the following is needed:**
- Mechanistic evidence that plasma kallikrein inhibition affects serpin polymerization or its downstream effects
- Preclinical studies, such as disease models or patient-derived cells, testing the hypothesis
- Package insert warnings and contraindications for safety screening
- Detailed mechanism-of-action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

