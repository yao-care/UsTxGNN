---
layout: default
title: Diethyltoluamide
parent: Model Prediction Only (L5)
nav_order: 605
evidence_level: L5
indication_count: 8
---

# Diethyltoluamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Diethyltoluamide (DEET): From Insect Repellent to Insomnia

## One-Sentence Summary

Diethyltoluamide (DEET) is a topical insect repellent and has no approved therapeutic indication in the data provided.
The TxGNN model predicts it may be relevant to **insomnia**, but there are **0 clinical trials** and **0 publications** supporting this, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None listed (marketed as an insect repellent, topical liquid) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. DEET is known as a topical insect repellent that acts on insect olfactory receptors. In vitro, it has shown weak cholinesterase inhibition.

The evidence does not support a therapeutic link to insomnia. Neurotoxicity (seizures, encephalopathy) has been reported mainly after massive exposure or ingestion, and nothing suggests a hypnotic or sleep-promoting effect. The very high TxGNN score most likely reflects proximity in the knowledge graph rather than real pharmacology.

The other top predictions show the same pattern. None has clinical or literature support, and each is best read as a computational artifact:

- **Neuro-behavioural:** ADHD (inattentive type and combined), migraine disorder, and specific developmental disorder. DEET has no known dopaminergic, noradrenergic or CGRP/serotonergic activity. Headache is a reported adverse effect of exposure, and animal developmental toxicity at high doses argues against a developmental benefit.
- **Coagulation-related:** factor 5 excess with spontaneous thrombosis, antithrombin deficiency type 2, and heparin cofactor 2 deficiency. There is no known effect of DEET on the coagulation cascade. These are hereditary protein defects that DEET would not correct, and topical use gives limited systemic exposure.

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
| Not recorded | MOSQUITO BUG OFF (Lydia Co., Ltd.) | Liquid | Not stated |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interactions were found in the queried data. Neurotoxicity after massive exposure or ingestion is described in the prediction rationale (see above).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All eight predictions are Level L5, meaning model output only, with no trials, no literature and no plausible mechanism. The high scores appear to be knowledge-graph artifacts. Given DEET's neurotoxicity in overdose, there is no basis to advance any of these indications.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- Package insert warnings and contraindications
- Any preclinical or clinical signal for the predicted indication, followed by a route compatibility assessment (DEET is topical, and the indication would need to be reachable by that route)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

