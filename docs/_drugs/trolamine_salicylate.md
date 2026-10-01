---
layout: default
title: Trolamine Salicylate
parent: Model Prediction Only (L5)
nav_order: 1267
evidence_level: L5
indication_count: 10
---

# Trolamine Salicylate
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

# Trolamine Salicylate: From Topical Musculoskeletal Pain Relief to Exostosis

## One-Sentence Summary

Trolamine salicylate is a topical salicylate, marketed in the US in creams and a spray sold as pain-relief and arthritis-relief products.
The TxGNN model predicts it may be effective for **exostosis** (a bony outgrowth), but **no clinical trials and no publications** currently support this prediction.
This is a model-only signal, and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (all license indication fields are empty). Product names such as "Arthritis Relief" and "Pain Relief" suggest topical musculoskeletal pain relief. |
| Predicted New Indication | Exostosis |
| TxGNN Prediction Score | 99.75% (rank 6719) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (the five listed include 505G(a)(3) and M017 entries, which are not standard NDA numbers) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Trolamine salicylate is a topical salicylate. Salicylates as a class act as local anti-inflammatory and analgesic agents by inhibiting cyclooxygenase (COX) and prostaglandin synthesis.

That mechanism can plausibly ease pain and inflammation around joints and soft tissue. Exostosis, however, is a structural bony outgrowth. An anti-inflammatory or analgesic agent would not be expected to change it, so any benefit would at best be symptomatic.

The high TxGNN score therefore likely reflects knowledge-graph proximity to musculoskeletal and bone-related terms. It is not evidence of a real therapeutic link. The related prediction "exostoses, multiple" is a genetic disorder (EXT1/EXT2, heparan sulfate synthesis) that the salicylate mechanism does not address.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 505G(a)(3) | MOBISYL | Cream | BF Ascher and Co Inc |
| M017 | Arthritis Relief | Cream | Geiss, Destin & Dunn, Inc |
| M017 | Tommie Copper Pain Relief | Cream | Tommie Copper, Inc. |
| M017 | Jointiva | Cream | Rising Pharma Holdings, Inc. |
| M017 | Aspercreme Pain Relieving | Cream | Chattem, Inc. |

Of the 20 licenses in total, only five are listed here. All are topical products, and a spray form also exists. Approved indication text is not recorded for any of them.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The exostosis prediction rests on the model score alone (L5), with no trials or literature. The salicylate mechanism is not expected to affect a structural bone lesion. The drug is already widely marketed as a topical pain product, so the question is whether the new indication is worth pursuing, not whether the drug can be supplied.

**To proceed, the following is needed:**
- Package insert warnings and contraindications. This is currently a blocking gap for safety screening.
- Mechanism of action data (for example from DrugBank).
- A targeted literature search on topical salicylates in exostosis, including pain related to osteochondroma.
- Confirmation of the approved indication text for each US product, since it is currently blank.
- Route compatibility assessment, since topical delivery to bone lesions is unverified.

**Other predictions worth a closer look:** Several other predicted indications have a more plausible rationale than exostosis.
- **Tendinitis** (99.70%) and **fibromyalgia** (99.59%) are marked "Research Question". The tendinitis rationale is plausible but class-level only. The fibromyalgia link is weak because NSAID-type agents generally show limited benefit there.
- **Rheumatoid arthritis** (99.25%) is the only prediction with any literature, at L4. It is a single 1982 tissue absorption study (PMID 6977559) showing topical triethanolamine salicylate penetrates knee joint tissue. This is indirect pharmacokinetic support, not efficacy evidence.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

