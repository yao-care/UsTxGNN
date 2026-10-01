---
layout: default
title: Diazoxide
parent: Model Prediction Only (L5)
nav_order: 601
evidence_level: L5
indication_count: 10
---

# Diazoxide
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

# Diazoxide: From Hyperinsulinemic Hypoglycemia to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diazoxide is an oral KATP channel opener marketed in the US, and it is best known for treating hypoglycemia caused by excess insulin. The TxGNN model predicts it may help with **hypotrichosis simplex of the scalp**, a rare genetic hair-loss disorder. **No clinical trials and no publications** support this specific prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperinsulinemic hypoglycemia (from general drug knowledge; the US license records supplied contain no indication text) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (1 NDA and 2 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied record. Diazoxide is known to open ATP-sensitive potassium (KATP) channels. This suppresses insulin release, which explains its use in hyperinsulinism. Hypertrichosis (excess hair growth) is a well-recognized effect of the drug, and minoxidil, another KATP opener, is used for hair loss.

On this basis, promoting hair growth in a hair-deficiency disorder is biologically plausible. There are two important caveats:

- Hypotrichosis simplex is genetic, and its cause is not related to KATP signaling. A hair-growth stimulant would at best act symptomatically.
- The high score is likely driven by shared hair-related phenotype labels in the knowledge graph, not by direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Holder |
|---------|------|------|------|
| NDA017453 | Proglycem | Suspension | Teva Pharmaceuticals USA, Inc. |
| ANDA210799 | Diazoxide | Suspension | Par Health USA, LLC |
| ANDA211050 | Diazoxide | Suspension | e5 Pharma, LLC |

All three products are oral suspensions. No topical product is listed.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the supplied data.

Published reports in the supplied literature describe hypertrichosis, fluid retention, cardiac failure-related events and, in neonates, necrotizing enterocolitis during diazoxide treatment. These come from studies in other indications and are not a full safety profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no direct mechanistic link to the genetic cause of this disorder. It stays at L5, model prediction only.

**Other predictions in the same set (context only):**
- **Alopecia (rank 4)** is the closest to a testable idea, at L4 as a research question. Topical diazoxide stimulated hair regrowth in bald stumptailed macaques (PMID 2085505). There is no human efficacy data, and only a topical route would be sensible to explore because systemic exposure carries cardiovascular and metabolic risks.
- **Hypertrichosis (rank 7)** is an inverted association. Diazoxide causes hypertrichosis, so this should not be pursued as a treatment.
- **Autosomal dominant hyperinsulinism due to Kir6.2 deficiency (rank 10)** has the strongest mechanistic fit, but it may overlap with existing labeled use. Response depends on the variant and needs checking against variant-level literature.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text (currently a blocking gap for safety screening)
- Detailed mechanism of action data
- Any human evidence for topical diazoxide in hair disorders, or a decision to prioritize the alopecia indication instead
- Route compatibility assessment, since the only marketed forms are oral suspensions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

