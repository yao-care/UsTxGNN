---
layout: default
title: Bismuth Subsalicylate
parent: Model Prediction Only (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
---

# Bismuth Subsalicylate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Bismuth Subsalicylate: From Digestive Symptom Relief to Paratyphoid Fever

## One-Sentence Summary

Bismuth subsalicylate is marketed in the US in products labelled for stomach and digestive relief, such as Pepto-Bismol. The TxGNN model predicts it may be effective for **paratyphoid fever**, but the prediction is model-only, with **0 clinical trials** and **0 publications** for this indication. The related prediction of salmonellosis has only indirect, dated supporting literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied label data (product names indicate stomach and digestive relief) |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Bismuth subsalicylate is a poorly soluble compound widely used for gastrointestinal complaints. Its efficacy for digestive symptoms is established by long use. Mechanistically, it has antimicrobial and anti-secretory activity against enteric pathogens, so a link to *Salmonella paratyphi* is plausible.

The link is weak, however. Paratyphoid fever is a systemic infection, while bismuth subsalicylate acts locally in the gut and is known for relieving diarrhea symptoms. Symptom relief would not treat systemic enteric fever. No trial or publication was supplied for this indication.

The nearby prediction of **salmonellosis** (rank 3) has indirect support. An in vitro study (PMID 2694949) shows the drug binds and kills bacteria. Older reviews from 1984–1991 describe its use in traveler's diarrhea and acute diarrhea. This evidence covers symptomatic diarrhea and prophylaxis, not treatment of Salmonella infection, and it may be a more realistic direction than paratyphoid fever itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M001 | Stomach | Liquid | Lil' Drug Store Products, Inc |
| M008 | Stomach Relief | Liquid | Harris Teeter, LLC |
| M008 | 5-Symptom Digestive Relief | Tablet | Target Corporation |
| M008 | Pepto Bismol | Capsule, liquid filled | The Procter & Gamble Manufacturing Company |
| M008 | Pepto-Bismol Chewable, TRAVEL BASIX | Tablet, chewable | Lil' Drug Store Products, Inc. |

The record lists 20 authorizations in total; the 5 above are shown. Approved indication text was not provided for any of them. Other listed forms include film-coated tablets and suspensions.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The paratyphoid fever prediction has a very high model score but no supporting trials or literature (L5). The mechanism is unlikely to fit a systemic infection. The adjacent salmonellosis prediction has only indirect, dated in vitro and review evidence (L4), which suggests a research question rather than a development candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data
- Approved indication text for the marketed products, to confirm the original indication
- Preclinical or clinical evidence for *Salmonella* enteric fever, such as in vitro activity against *S. paratyphi* and typhi and any systemic exposure data
- A focused evidence search on salmonellosis and enteric infection, which is a more plausible framing than paratyphoid fever alone

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

