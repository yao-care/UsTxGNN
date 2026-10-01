---
layout: default
title: Sucralfate
parent: Model Prediction Only (L5)
nav_order: 1184
evidence_level: L5
indication_count: 2
---

# Sucralfate
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

# Sucralfate: From Duodenal Ulcer to Duodenogastric Reflux

## One-Sentence Summary

Sucralfate is an oral mucosal-protective agent, generally used for duodenal ulcer. The TxGNN model predicts it may be effective for **duodenogastric reflux** (bile reflux into the stomach), but **0 clinical trials** and **0 publications** currently support this direction, so the prediction is model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duodenal ulcer (general labeling knowledge; the supplied US license records contain no indication text) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (NDA and ANDA combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Based on general pharmacology, sucralfate is a non-absorbed aluminum-containing complex that forms a protective barrier over injured mucosa. It is also reported to bind bile acids and pepsin. Its use in ulcer disease is well established.

Duodenogastric reflux exposes the gastric mucosa to bile and other duodenal contents. A barrier-forming agent that binds bile acids could plausibly protect the stomach lining in this setting. This is a hypothesis only. It rests on general pharmacology, not on the supplied data, and no trial or publication evidence has been retrieved to confirm it.

The model also predicted a second indication, **duodenal obstruction** (score 99.30%), but it is much weaker. A mucosal protectant has no clear mechanism for relieving a mechanical or functional obstruction. The prediction may simply reflect graph proximity to duodenal ulcer, which can cause stricture. Bezoar formation has also been reported with sucralfate, so use in obstruction could carry a safety concern. This report does not recommend pursuing it without further verification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Showing 5 of 20 authorizations. The supplied records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018333 | Sucralfate (Bryant Ranch Prepack) | Tablet | — |
| NDA019183 | Carafate (Allergan, Inc.) | Suspension | — |
| ANDA216726 | Sucralfate (Torrent Pharmaceuticals Limited) | Suspension | — |
| ANDA074415 | Sucralfate (Bryant Ranch Prepack) | Tablet | — |
| ANDA215705 | Sucralfate (Zydus Lifesciences Limited) | Tablet | — |

Available forms are oral tablets and suspension.

---

## Safety Considerations

Please refer to the package insert for safety information.

The drug-interaction query returned no results for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (evidence level L5), and the mechanism of action and package-insert safety data are both missing. The bile-binding rationale for duodenogastric reflux is plausible but unverified. The duodenal obstruction prediction has no clear mechanism and a possible safety concern.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Systematic searches of ClinicalTrials.gov, ICTRP, and PubMed for sucralfate in bile reflux or duodenogastric reflux
- Route and formulation compatibility assessment for the predicted indication
- Approved-indication text for the US licenses, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

