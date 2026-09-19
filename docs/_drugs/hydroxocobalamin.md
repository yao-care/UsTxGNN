---
layout: default
title: Hydroxocobalamin
parent: Model Prediction Only (L5)
nav_order: 779
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
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

# Hydroxocobalamin: From Cyanide Poisoning Antidote/Vitamin B12 Deficiency to Esophageal Varices with Bleeding

## One-Sentence Summary

Hydroxocobalamin (vitamin B12a, DrugBank ID: DB00200) is approved for treating cyanide poisoning and vitamin B12 deficiency. The TxGNN model predicts it may be effective for **Esophageal Varices with Bleeding**, but there are currently **no clinical trials** and **no literature support**, representing only algorithmic model prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Taiwan: Not marketed, no approved indication data (mechanism analysis references known uses as cyanide poisoning antidote and vitamin B12 deficiency treatment) |
| Predicted New Indication | Esophageal Varices with Bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Current mechanism of action (MOA) data is missing ([Data Gap], DG002), preventing direct explanation of pharmacological relevance. Hydroxocobalamin's approved uses are cyanide poisoning antidote and vitamin B12 deficiency treatment; neither shows direct pathophysiological overlap with esophageal varices with bleeding.

The only conceivable indirect hypothesis is that hydroxocobalamin possesses nitric oxide (NO) and hydrogen sulfide scavenging capacity and has been clinically used in vasoplegic shock to induce vasoconstriction. The pathophysiology of esophageal varices with bleeding involves NO-mediated splanchnic vasodilation, leading to portal hypertension; theoretically, NO scavengers might reduce splanchnic blood flow via mechanisms similar to approved hemostatic agents such as vasopressin, terlipressin, or octreotide. However, this is purely mechanistic speculation, and **no direct research** has been found applying hydroxocobalamin to variceal bleeding.

TxGNN assigns the same score (99.23%) to a second predicted indication, "Esophageal Varices without Bleeding," with the same mechanistic hypothesis but weaker evidence strength—there is no clinical analogy basis for acute vasoconstrictor use in the non-bleeding state. Both are purely algorithmic predictions, and the drug is not marketed in Taiwan, making it unsuitable for preliminary safety assessment (S1).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Market Information

This drug is not marketed in Taiwan (number of licenses: 0), and no information about marketed products is available.

## Safety Considerations

Please refer to the package insert for safety information. Currently, package insert warnings and contraindication data are missing (DG001, Blocking), identified as a critical gap before entering preliminary safety assessment (S1).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5, with no clinical trials or literature supporting this indication. The drug is not marketed in Taiwan, MOA and package insert safety data are missing, and there is no basis for proceeding to the next evaluation stage.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindication data (DG001, Blocking, requires downloading and parsing package insert PDF before entering S1 safety assessment)
- Detailed mechanism of action (MOA) data (DG002, requires querying the DrugBank API)
- Direct clinical trials or literature evidence for esophageal varices with or without bleeding
- If evaluating cross-border introduction, supplementary information on Taiwan (or target market) market authorization and approved indications is needed

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

