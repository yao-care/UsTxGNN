---
layout: default
title: Pegloticase
parent: Model Prediction Only (L5)
nav_order: 1022
evidence_level: L5
indication_count: 1
monitor_inn: "PEGLOTICASE"
predicted_indications: ["severe nonproliferative diabetic retinopathy"]
last_modified_at: 2026-10-14
description: "Pegloticase: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Gout"
---

# Pegloticase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Pegloticase: From Gout to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegloticase is a PEGylated uricase enzyme originally used to treat gout.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA 125293) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, pegloticase is a PEGylated recombinant uricase that converts uric acid to allantoin, lowering serum urate. Its efficacy in gout is the basis of its original use.

A possible indirect link is that hyperuricemia and xanthine oxidase-related oxidative stress have been proposed as contributors to diabetic microvascular injury, including retinopathy. This link is speculative and has not been validated here.

There are also practical concerns for this new use:
- The drug is given systemically by intravenous infusion, while the target disease is ocular.
- Immunogenicity (anti-drug antibodies, infusion reactions, anaphylaxis) is a known issue with this class of drug.
- Route compatibility and similarity to the original indication have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA 125293 (cancelled) | Krystexxa (Horizon Therapeutics USA, Inc.) | Injection, solution | Not listed in the compiled data |

## Safety Considerations

- **Drug Interactions**: Seven moderate-level interactions were identified, all with other PEGylated products:
  - Pegvaliase
  - Pegvisomant
  - Pegademase
  - Pegaspargase
  - Pegfilgrastim
  - Peginterferon alfa-2a
  - Peginterferon alfa-2b

Please refer to the package insert for other safety information, including warnings and contraindications. Package insert details were not available in the compiled data. Known class concerns noted in the evaluation include anaphylaxis and infusion reactions, and hemolysis and methemoglobinemia risk in G6PD deficiency.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is a high TxGNN score. There are no clinical trials or publications, the mechanistic link is speculative, and the drug is delivered systemically for an eye disease. The only US license is cancelled, which further limits availability.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Preclinical or mechanistic evidence linking urate lowering or uricase activity to diabetic retinopathy
- Assessment of route compatibility (systemic IV versus ocular delivery) and immunogenicity risk
- Clarification of current availability, given the cancelled US license status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

