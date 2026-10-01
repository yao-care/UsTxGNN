---
layout: default
title: Calaspargase Pegol
parent: Model Prediction Only (L5)
nav_order: 485
evidence_level: L5
indication_count: 4
---

# Calaspargase Pegol
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

# Calaspargase Pegol: From Acute Lymphoblastic Leukemia to Insomnia

## One-Sentence Summary

Calaspargase pegol is a pegylated asparaginase that depletes circulating asparagine. It is an antileukemic enzyme, and its labeled use is acute lymphoblastic leukemia (ALL) per public labeling, since the source data gives no indication text.
The TxGNN model predicts it may be effective for **insomnia** with a very high score, but **0 clinical trials** and **0 publications** support this prediction.
The mechanism gives no plausible basis for it, so this is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in the source data (labeled use is ALL per public labeling; not confirmed in the Evidence Pack) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761102) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Calaspargase pegol is a pegylated asparaginase that depletes circulating asparagine. Its effect in leukemia comes from starving malignant lymphoblasts of this amino acid.

This mechanism has no known action on sleep-wake regulation, so we found no plausible link between the original indication and insomnia. The high score (99.80%, rank 5683) comes from graph-based inference and is not backed by any trial or literature. Because the drug's mechanism is undocumented in the input, the prediction cannot be checked against a known pathway.

The other three top predictions (factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency, antithrombin deficiency type 2) look like safety-signal artifacts, not therapeutic leads. Asparaginase-class drugs are associated with thrombosis and reduced synthesis of anticoagulant proteins. The graph is probably picking up an adverse-effect association, which points in the opposite direction from benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761102 | Asparlas (Servier Pharmaceuticals LLC) | Injection, solution | Not provided in source data |

## Cytotoxicity

Asparaginase is an antineoplastic enzyme therapy, so this section applies. The Evidence Pack has no toxicity or handling data.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Enzyme-based antineoplastic (asparagine depletion), not a conventional DNA-damaging cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Coagulation-related parameters (antithrombin, fibrinogen), given the thrombosis association noted above; other items per package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

The prediction analysis notes that asparaginase products are associated with thrombosis, thought to result from reduced hepatic synthesis of anticoagulant proteins and fibrinogen. Using this drug for a sleep disorder would expose patients to this risk with no known benefit.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no trials, no literature, and no plausible mechanistic link between asparagine depletion and sleep regulation. The exposure carries serious safety concerns, notably thrombosis.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank, to check whether any biological pathway connects the drug to insomnia
- Package insert warnings and contraindications from the FDA label, which are currently missing and block safety screening
- The approved indication text for BLA761102, to confirm the original indication
- Any preclinical or clinical signal for insomnia; without it, deprioritize this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

