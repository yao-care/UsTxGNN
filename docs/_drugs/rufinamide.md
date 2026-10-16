---
layout: default
title: Rufinamide
parent: Model Prediction Only (L5)
nav_order: 1138
evidence_level: L5
indication_count: 5
monitor_inn: "RUFINAMIDE"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "photosensitive occipital lobe epilepsy", "cryptogenic late-onset epileptic spasms", "atypical childhood epilepsy with centrotemporal spikes"]
last_modified_at: 2026-10-14
description: "Rufinamide: predicted new indication Febrile infection-related epilepsy syndrome (evidence level L5). Approved use: Lennox-Gastaut syndrome"
---

# Rufinamide
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

# Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Rufinamide is an anti-seizure medicine originally used to treat Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**,
but the data compiled for this report contain **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lennox-Gastaut syndrome (from the knowledge graph; no approved-indication text is available in the US license records) |
| Predicted New Indication | Febrile infection-related epilepsy syndrome |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | ✗ Cancelled only (all licenses cancelled) |
| Number of NDAs | 12 (1 NDA and 11 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on general pharmacological knowledge, rufinamide is a sodium channel modulator that prolongs the inactive state of voltage-gated sodium channels. Its efficacy in Lennox-Gastaut syndrome has been established, so it may plausibly provide broad anti-seizure activity in other severe epilepsies.

The link to FIRES is weak, however. FIRES is a refractory status epilepticus driven largely by neuroinflammation, and sodium channel blockers generally offer limited benefit in it. No trials or literature were found to support the prediction, so the high score (0.996) cannot yet be tied to a credible mechanism.

Other top-ranked predictions are also epilepsy syndromes with equally high scores and no supporting evidence:

| Rank | Predicted Indication | Score | Mechanistic Comment |
|------|------|------|------|
| 2 | Perioral myoclonia with absences | 99.51% | Sodium channel blockers can aggravate absence-type seizures, so this is a safety concern |
| 3 | Photosensitive occipital lobe epilepsy | 99.44% | Plausible, since focal seizures are commonly treated with sodium channel blockers; theoretical only |
| 4 | Cryptogenic late-onset epileptic spasms | 99.44% | Some biological proximity to Lennox-Gastaut syndrome; inferential only |
| 5 | Atypical childhood epilepsy with centrotemporal spikes | 99.44% | Some sodium channel blockers can worsen atypical forms, so the fit is uncertain |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 12 US licenses are cancelled; none are currently valid. The data compiled for this report do not include approved-indication text. Up to 5 of the licenses are listed below.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA021911 | Banzel (Tjoapack LLC) | Film-coated tablet | Cancelled |
| ANDA204988 | Rufinamide (Hikma) | Film-coated tablet | Cancelled |
| ANDA204993 | Rufinamide (Camber) | Film-coated tablet | Cancelled |
| ANDA205075 | Rufinamide (Glenmark) | Film-coated tablet | Cancelled |
| ANDA211388 | Rufinamide (Bionpharma) | Suspension | Cancelled |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** liver failure, liver disease, gallbladder disease, leukopenia, anxiety disorder, neurotic disorder and dysthymic disorder. These come from knowledge-graph contraindication edges and should be verified against the package insert.
- **Drug Interactions:** 100 interactions were found, and the 20 reviewed are all rated Moderate. Examples include:
  - Corticosteroids (hydrocortisone, prednisone, betamethasone, triamcinolone)
  - Vitamin D analogues (cholecalciferol, calcifediol, calcitriol)
  - Bupropion
  - Pioglitazone
  - Morphine
  - Ondansetron
  - Metoclopramide
- **Class-level concern:** For some of the predicted indications (perioral myoclonia with absences, atypical childhood epilepsy with centrotemporal spikes), sodium channel blockers may aggravate seizures. This needs review before any further consideration.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score (L5) behind it, with no clinical trials or publications. The mechanistic link to FIRES is weak, and all US licenses are currently cancelled.

**To proceed, the following is needed:**
- A systematic search of clinical trials and literature for rufinamide in FIRES and the other predicted epilepsy syndromes
- Detailed mechanism-of-action data, and an assessment of whether sodium channel modulation is relevant to neuroinflammatory epilepsy
- The package insert warnings and contraindications, for a formal safety screen
- Clarification of the cancelled US license status and the commercial availability of rufinamide
- A seizure-aggravation risk review for the absence-type and atypical epilepsy predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

