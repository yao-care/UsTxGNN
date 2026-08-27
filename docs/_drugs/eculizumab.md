---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 640
evidence_level: L5
indication_count: 10
---

# Eculizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Eculizumab: From Complement-Mediated Diseases to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab is a complement C5 inhibitor; the evidence pack does not contain formal Taiwan approval records, but supporting literature references identify its established use in complement-mediated conditions such as PNH and aHUS. The TxGNN model's top prediction is **Cyclic Hematopoiesis**, a rare bone-marrow disorder driven by ELANE gene mutations — but **no clinical trials and no literature** currently support this specific link, and the model's own rationale flags it as lacking a known biological connection. Nine further candidates in this evidence pack (congenital neutropenia syndromes) show the same pattern: high TxGNN scores with no disease-specific evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license records exist (drug not currently marketed); literature references in this pack cite PNH and aHUS as established indications elsewhere |
| Predicted New Indication | Cyclic Hematopoiesis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is formally flagged as a data gap (DG002, High severity) in this evidence pack. Based on the literature references that did surface during evidence collection (though attached to a different candidate, rank 4), Eculizumab's known mechanism is inhibition of terminal complement component C5, blocking formation of the membrane attack complex — the basis for its established use in complement-mediated hemolytic and thrombotic conditions such as paroxysmal nocturnal hemoglobinuria (PNH) and atypical hemolytic uremic syndrome (aHUS).

Cyclic Hematopoiesis, however, is a distinct disease driven by *ELANE* gene mutations affecting neutrophil elastase and bone-marrow stem cell cycling — a mechanism unrelated to complement activation. The model's own repurposing rationale is explicit on this point: the high TxGNN score is attributed to knowledge-graph clustering around a shared "hematologic disease" node rather than to genuine mechanistic reasoning, and states there is "no known biological connection" between Eculizumab's complement-inhibition pathway and the pathophysiology of cyclic hematopoiesis.

Given this, the prediction should be treated as a hypothesis-generation signal only, not as mechanistically supported evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

No license records available — Eculizumab is not currently marketed in Taiwan (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warning/contraindication data and drug interaction data are both flagged as data gaps in this evidence pack — DG001, Blocking severity.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN score but zero supporting clinical trials or literature, and the model's own rationale explicitly states there is no known mechanistic link between Eculizumab's complement C5 inhibition and cyclic hematopoiesis's ELANE-driven pathophysiology. This is an L5, hypothesis-only signal likely driven by knowledge-graph node clustering rather than biology.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindication data (currently Blocking data gap)
- Confirmed mechanism of action documentation for Eculizumab (currently High-severity data gap)
- Preclinical or mechanistic studies specifically linking complement pathway activity to ELANE-related neutrophil cycling disorders
- Disease-specific case reports or trials before any further evaluation stage is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

