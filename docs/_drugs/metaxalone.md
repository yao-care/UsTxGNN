---
layout: default
title: Metaxalone
parent: Model Prediction Only (L5)
nav_order: 904
evidence_level: L5
indication_count: 3
monitor_inn: "METAXALONE"
predicted_indications: ["infectious otitis media", "endocarditis", "endocardial fibroelastosis"]
last_modified_at: 2026-10-14
description: "Metaxalone: predicted new indication Infectious otitis media (evidence level L5). Approved use: Not available in the compiled data (metaxalone is generally known as…"
---

# Metaxalone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Metaxalone: From Muscle Relaxation to Infectious Otitis Media

## One-Sentence Summary

Metaxalone is an oral skeletal muscle relaxant. The original indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **infectious otitis media**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on a graph-based computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (metaxalone is generally known as a skeletal muscle relaxant) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

Two other predictions were also reviewed: **endocarditis** (99.02%) and **endocardial fibroelastosis** (99.00%). Both are L5 with no trials or literature, and both are also recommended as Hold.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Metaxalone is a centrally acting skeletal muscle relaxant, and its mechanism is not well defined. It is thought to act through general central nervous system depression rather than a direct effect on muscle.

No established mechanistic link to infectious otitis media was identified. Metaxalone has no known antimicrobial, anti-inflammatory, or Eustachian tube-modulating activity. The high TxGNN score most likely reflects network proximity in the knowledge graph rather than biological plausibility. Standard otitis media therapy (antibiotics and analgesics) is well established, so there is no clear unmet need that metaxalone would address.

The other two predictions fare no better:
- **Endocarditis:** A serious infection treated with prolonged targeted antimicrobials and sometimes surgery. Metaxalone has no antimicrobial or cardiovascular activity, and its 53 recorded drug interactions would add complexity in the polypharmacy typical of these patients.
- **Endocardial fibroelastosis:** A rare pediatric condition. Metaxalone has no known antifibrotic or cardioprotective activity and is not recommended under age 12.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| ANDA203399 | Metaxalone (Advanced Rx of Tennessee, LLC) | Tablet | Not available | Cancelled |
| ANDA207466 | Metaxalone (ScieGen Pharmaceuticals, Inc.) | Tablet | Not available | Cancelled |
| ANDA204770 | Metaxalone (Doc Rx) | Tablet | Not available | Cancelled |
| ANDA203695 | Metaxalone (Sportpharm LLC) | Tablet | Not available | Cancelled |

All four authorizations are cancelled, and no valid single-ingredient or combination licenses remain.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not label text): liver failure, acute liver failure, hepatitis, and hemolytic anemia.
- **Drug Interactions:** 53 interactions are recorded in total. Major-level interactions include:
  - Morphine (including liposomal morphine)
  - Codeine
  - Hydrocodone

  Moderate-level interactions include:
  - Cannabinoids: dronabinol, nabilone
  - Opioid-related: naltrexone, opium
  - Antihistamines: promethazine, chlorpheniramine, cetirizine, brompheniramine, carbinoxamine, clemastine, mepyramine, doxylamine
  - Others: ethanol, metoclopramide, sibutramine, dextromethorphan

  Most of these involve additive central nervous system depression.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score, with no clinical trials, no literature, and no plausible mechanistic link to infectious otitis media. In addition, all US licenses are cancelled and well-established standard therapies already exist, so there is no practical development pathway.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to assess any biological link to the predicted indication
- Preclinical or mechanistic evidence supporting a role in otitis media
- Confirmation of the original approved indication and a feasible regulatory pathway given the cancelled licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

