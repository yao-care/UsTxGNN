---
layout: default
title: Dalteparin
parent: Model Prediction Only (L5)
nav_order: 566
evidence_level: L5
indication_count: 5
---

# Dalteparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Dalteparin: From Anticoagulant Therapy to Autosomal Recessive Protein C Deficiency Thrombophilia

## One-Sentence Summary

Dalteparin is a low-molecular-weight heparin marketed in the US as Fragmin. The Evidence Pack does not list a specific approved indication for it.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency, autosomal recessive**, with a very high score of **99.88%**.
This is a model prediction only: **0 clinical trials** and **0 publications** currently support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in the input (the approved indication text on all listed licenses is empty) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 license records (the entries provided all carry NDA020287) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Dalteparin is a low-molecular-weight heparin. Drugs of this class potentiate antithrombin and inhibit factor Xa, which reduces clot formation.

Autosomal recessive protein C deficiency removes a key natural anticoagulant pathway and leaves patients prone to thrombosis. An anticoagulant such as dalteparin could plausibly offset that hypercoagulable state, and this is the likely basis for the model's high score.

This link is **plausible but unverified**. No trial or publication was supplied to support it, and because the drug's original mechanism and indications are missing from the input, the argument cannot be cross-checked. The score reflects graph proximity in the knowledge graph, not clinical proof.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020287 | Fragmin | Injection | Pfizer Laboratories Div Pfizer Inc |

The five license entries provided were identical, so they are shown as one row. Approved indication text was not supplied for any of them. Route: injectable only.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the input.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). The rank 1 indication has no registered trials or literature, and the supplied package insert and mechanism data are missing. The other four predictions (primary release disorder of platelets, pseudo-von Willebrand disease, atypical hemolytic-uremic syndrome with thrombomodulin anomaly, painful neuropathy) have no credible support either. The three bleeding-related ones are mechanistically unlikely or contraindicated in principle for an anticoagulant.

**To proceed, the following is needed:**
- The FDA package insert (approved indications, warnings, contraindications), which blocks safety screening
- Mechanism of action data from DrugBank
- A targeted search for case reports, registries or trials of low-molecular-weight heparin in protein C deficiency
- A bleeding-risk assessment and dosing rationale for this rare population
- Confirmation of route compatibility (injectable only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

