---
layout: default
title: Sacrosidase
parent: Model Prediction Only (L5)
nav_order: 1142
evidence_level: L5
indication_count: 2
---

# Sacrosidase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Sacrosidase: From Congenital Sucrase-Isomaltase Deficiency to Cystinosis

## One-Sentence Summary

Sacrosidase is an oral enzyme replacement (marketed in the US as Sucraid) that replaces the sucrase-isomaltase enzyme missing in the gut. The TxGNN model predicts it may be effective for **cystinosis**, with a very high score. However, **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack's license record (Sucraid is generally known for congenital sucrase-isomaltase deficiency, which should be confirmed against the label) |
| Predicted New Indication | Cystinosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA020772) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Sacrosidase is an orally administered sucrase-isomaltase replacement. It acts in the intestinal lumen to break down dietary sucrose and is not meaningfully absorbed into the bloodstream.

The review found **no credible mechanistic link** to cystinosis. Cystinosis is a lysosomal storage disorder caused by a deficiency of the cystinosin (CTNS) transporter, which leads to cystine build-up inside cells. Sacrosidase has no known effect on cystine transport or lysosomal function. It also does not reach the tissues where the disease occurs.

The high score (0.994) is a graph-based prediction only. Both predicted indications are rare inherited metabolic diseases, so the score may reflect a shared "enzyme/metabolic" pattern in the knowledge graph rather than a real biological connection.

The second-ranked prediction, familial apolipoprotein C-II deficiency (score 99.05%), has the same problem. That disease is a cause of severe hypertriglyceridemia, caused by loss of the lipoprotein lipase cofactor apoC-II. Sacrosidase has no known interaction with lipoprotein metabolism. It also has no trials or literature.

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
| BLA020772 | Sucraid (QOL Medical, LLC) | Solution | Not stated in the record |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support (L5). Sacrosidase acts only in the gut and has no plausible connection to cystine transport or lysosomal function. The high TxGNN score is likely a knowledge-graph artifact, and there is no basis to advance this candidate.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Any preclinical or mechanistic evidence that sacrosidase affects cystine handling or lysosomal function
- Evidence that an oral, gut-restricted enzyme could reach the relevant tissues, or a different route of administration
- Any published or registered studies in cystinosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

