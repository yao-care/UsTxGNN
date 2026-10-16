---
layout: default
title: Mafenide
parent: Model Prediction Only (L5)
nav_order: 881
evidence_level: L5
indication_count: 10
monitor_inn: "MAFENIDE"
predicted_indications: ["irritable bowel syndrome", "cauda equina syndrome", "panuveitis (disease)", "iris disease", "uveitis", "acne (disease)", "isolated iridoschisis", "abnormal pupillary function (disease)", "benign neoplasm of iris", "iris cancer"]
last_modified_at: 2026-10-14
description: "Mafenide: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Not stated in the available regulatory data"
---

# Mafenide
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

# Mafenide: From Burn Wound Infection to Irritable Bowel Syndrome

## One-Sentence Summary

Mafenide is a topical sulfonamide antimicrobial, sold in the US as a cream under the brand name Sulfamylon.
The TxGNN model predicts it may be effective for **irritable bowel syndrome**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available regulatory data (the license record has no indication text) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mafenide is a topical sulfonamide antimicrobial and carbonic anhydrase inhibitor. It is a topical agent, and the data compiled for this report do not state its original indication.

No mechanistic link to irritable bowel syndrome has been established. The high TxGNN score reflects a graph-based computational prediction only. A topical antimicrobial has no plausible rationale for a functional gut disorder, and the route of administration is also incompatible. The prediction should be treated as a weak, unsupported signal.

Other top-ranked predictions show the same pattern. These include cauda equina syndrome, panuveitis, iris disease, uveitis, acne and several iris-related conditions. Their scores are all between 99.92% and 99.97%. Acne is the most biologically plausible, since mafenide is a topical antibacterial. Even so, it is not established against *Cutibacterium acnes* and carries pain, burning and metabolic acidosis concerns. Many of the ocular predictions appear to reflect clustering of eye-disease nodes in the knowledge graph, not drug-specific biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016763 (cancelled) | SULFAMYLON (Rising Pharma Holdings, Inc.) | Cream | Not available |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): kidney disease, pyoureter, acidosis disorder, metabolic acidosis, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, lung disease, and an obsolete rare pulmonary disease category.
- No drug interactions were found in the queried data.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no mechanistic rationale. The only US license is cancelled, and mafenide is a topical product with notable tissue toxicity and metabolic acidosis risk. This makes it poorly suited to a gastrointestinal indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking mafenide to irritable bowel syndrome
- A route-of-administration assessment, since only a topical cream has been marketed
- If the team wants to pursue a more plausible direction, a separate assessment of acne, where a topical antibacterial rationale exists, compared with established alternatives
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

