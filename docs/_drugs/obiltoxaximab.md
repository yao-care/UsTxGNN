---
layout: default
title: Obiltoxaximab
parent: Model Prediction Only (L5)
nav_order: 979
evidence_level: L5
indication_count: 8
monitor_inn: "OBILTOXAXIMAB"
predicted_indications: ["postinfectious vasculitis", "post-infectious syndrome", "post-bacterial disorder", "infective urethral stricture", "otitis externa", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "drug-induced osteoporosis"]
last_modified_at: 2026-10-14
description: "Obiltoxaximab: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Inhalational anthrax (anthrax infection)"
---

# Obiltoxaximab
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

# Obiltoxaximab: From Inhalational Anthrax to Postinfectious Vasculitis

## One-Sentence Summary

Obiltoxaximab is a monoclonal antibody originally used to treat inhalational anthrax.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inhalational anthrax (anthrax infection) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 (BLA, cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known information, obiltoxaximab is a monoclonal antibody that binds the *Bacillus anthracis* protective antigen (PA) and blocks entry of anthrax toxin into host cells. Its activity is therefore specific to anthrax toxin neutralization.

Postinfectious vasculitis is typically immune-complex mediated and is not driven by anthrax toxin. No plausible mechanistic link was identified. The high TxGNN score (99.74%) is a graph-based association only. It likely reflects the shared "infection" category in the knowledge graph rather than a biological rationale.

Other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Post-infectious syndrome | 99.74% | No toxin-neutralization target; computational association only |
| 3 | Post-bacterial disorder | 99.74% | Only the shared bacterial-origin category; no clinical support |
| 4 | Infective urethral stricture | 99.74% | Fibrosis and scarring process; PA neutralization has no known role |
| 5 | Otitis externa | 99.71% | Caused by other organisms and managed topically; no biological basis |
| 6 | Chagas cardiomyopathy | 99.71% | Parasitic disease; the target is absent |
| 7 | Infection-related hemolytic uremic syndrome | 99.70% | Loose antitoxin analogy only; the drug does not cross-react with Shiga toxin |
| 8 | Drug-induced osteoporosis | 99.13% | Unrelated to toxin neutralization; likely a graph artifact |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125509 (cancelled) | Anthim | Solution | Not specified in the compiled data |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (evidence level L5) and no plausible biological link. The only US license is cancelled. The prediction should not advance on the model score alone.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting anthrax protective antigen neutralization to postinfectious vasculitis
- Supporting preclinical or clinical evidence
- Package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism-of-action data
- Clarification of the cancelled US regulatory status and the route of administration needed for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

