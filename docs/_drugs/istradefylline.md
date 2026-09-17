---
layout: default
title: Istradefylline
parent: Model Prediction Only (L5)
nav_order: 818
evidence_level: L5
indication_count: 1
---

# Istradefylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Istradefylline: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Istradefylline is a selective adenosine A2A receptor antagonist used clinically as adjunct therapy for Parkinson's disease. The TxGNN model predicts a possible link to **Rasmussen Subacute Encephalitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on knowledge-graph similarity alone, and the model's own mechanistic rationale flags the biological direction as questionable.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (per mechanism description; drug is not currently licensed in Taiwan, so no formal approved-indication text is on file) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not Marketed (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Istradefylline is a selective adenosine A2A receptor antagonist. Its established clinical mechanism centers on modulating striatal dopamine/adenosine signaling, which underlies its use as an adjunct in Parkinson's disease.

Rasmussen encephalitis, by contrast, is a chronic, unilateral, T-cell–mediated autoimmune/inflammatory encephalitis — a pathology with no direct overlap with striatal A2A receptor signaling. Adenosine A2A receptors do have anti-inflammatory regulatory roles on immune cells, but this cuts against rather than for the prediction: antagonizing the receptor could theoretically *increase* T-cell activation and neuroinflammation, the opposite of what would be needed to treat an autoimmune encephalitis.

In short, this candidate is a knowledge-graph similarity output rather than a pharmacologically motivated hypothesis. The evidence pack itself flags the mechanistic link as weak and directionally uncertain, so it should be treated as an exploratory signal only, not a basis for clinical rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

This drug is not currently marketed in Taiwan (0 licenses on file); no authorization records are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is L5 (model output only), with zero clinical trials, zero literature, and a mechanistic rationale that the model itself identifies as weak and possibly working in the wrong direction. Combined with a Blocking data gap on Taiwan safety/warning information, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA (or manufacturer) package insert data on warnings and contraindications (currently a Blocking data gap)
- Detailed, sourced mechanism-of-action data confirming or refuting the A2A-antagonism hypothesis in autoimmune/inflammatory encephalitis
- Preclinical or case-level evidence testing istradefylline (or A2A antagonists generally) in Rasmussen encephalitis or comparable neuroinflammatory models
- Any emerging clinical trial or case-report data before reconsidering evidence level above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

