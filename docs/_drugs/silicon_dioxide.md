---
layout: default
title: Silicon Dioxide
parent: Model Prediction Only (L5)
nav_order: 1159
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Silicon Dioxide: predicted new indication Active peptic ulcer disease (evidence level L5). Approved use: Peptic ulcer disease, GERD, esophagitis, dyspepsia"
---

# Silicon Dioxide
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

# Silicon Dioxide: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Silicon dioxide was originally associated with acid-related upper gastrointestinal conditions such as peptic ulcer disease, gastroesophageal reflux disease (GERD), esophagitis and dyspepsia.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is therefore a network-based inference only, and it largely re-labels an existing indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, GERD, esophagitis, dyspepsia (from the knowledge graph; no approved indication text is available in US licensing data) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, silicon dioxide is typically used as an excipient or as an anti-foaming/adsorbent agent. No pharmacological rationale for ulcer healing is documented in the data compiled for this report.

The very high score (99.93%) most likely reflects how close the predicted disease sits to the drug's existing indications in the knowledge graph. Active peptic ulcer disease overlaps heavily with peptic ulcer disease, GERD and dyspepsia, so this looks like a re-labeling of an existing indication rather than a true repurposing candidate.

The other predicted indications show the same pattern. They are peptic ulcer perforation (99.92%), gastrojejunal ulcer (99.92%) and gastric ulcer (99.83%). The identical scores for the first two suggest a shared graph neighborhood of ulcer-type disease nodes rather than disease-specific evidence. Peptic ulcer perforation is an acute surgical complication, so an oral agent with no known mechanism is not a plausible therapy for it. Any benefit in the other ulcer indications would be speculative, for example a physical protective or adsorptive effect, and nothing in the data supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | BM Silicea Icing Sugar (BM Private Limited) | Tablet | Not stated (status: cancelled) |

Other dosage forms recorded for silicon dioxide include oral soluble tablets, patches, pellets, liquids and topical creams. No valid single-ingredient or combination licenses are currently active.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not from label text): kidney disease, pyoureter, congestive heart failure, diarrheal disease, chronic diarrheal disease, constipation disorder, hypophosphatemia, intestinal impaction, hemorrhoid.

No drug-interaction records were found. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is based only on knowledge-graph proximity to the drug's existing indications. There are no clinical trials, no literature, no mechanism data and no active US marketing authorization, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data, to establish a plausible pharmacological link to ulcer healing
- FDA package insert warnings and contraindications, which block progression to safety screening
- Clinical or preclinical evidence for silicon dioxide in peptic ulcer disease
- Clarification of whether the prediction is a true new indication or only a re-labeling of existing indications
- Confirmation of the regulatory status, since the only US license is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

