---
layout: default
title: Auranofin
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 2
---

# Auranofin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

The skill confirms this is a TxGNN report generation task. Now I'll generate the full evaluation report based on the Evidence Pack.

---

# Auranofin: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Auranofin is a gold-based antirheumatic compound originally approved for the treatment of rheumatoid arthritis.
The TxGNN model predicts it may be effective for **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**,
however with **0 clinical trials** and **0 publications** currently supporting this direction — the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid Arthritis |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (not found in regulatory database) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, Auranofin is a gold(I) thiosugar compound classified as a disease-modifying antirheumatic drug (DMARD). Its primary mechanism involves inhibition of thioredoxin reductase (TrxR) and downstream suppression of NF-κB-mediated inflammatory signalling, which accounts for its efficacy in rheumatoid arthritis.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is an extremely rare developmental genetic disorder affecting ocular formation (coloboma, microphthalmia) and proximal limb bone growth. Its underlying pathology is driven by mutations affecting developmental gene pathways — including those related to COL11A2 and the STRA6 signalling axis — which govern embryonic organogenesis. There is no established or theoretical connection between TrxR inhibition or NF-κB anti-inflammatory activity and the correction of germline developmental gene defects.

The TxGNN model's high confidence score (0.9956) in this case is most likely an artefact of graph topology: skeletal and ophthalmic disease nodes in the knowledge graph may share structural similarity scores with other disease nodes for which Auranofin has been studied, rather than reflecting a genuine repurposing signal. The risk of a graph-structure false positive is considered high for this prediction type.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero empirical evidence — no clinical trials, no published literature — supporting Auranofin for colobomatous microphthalmia-rhizomelic dysplasia syndrome, and the mechanistic link between TrxR/NF-κB inhibition and this developmental genetic disorder is not plausible with current biological understanding. The high TxGNN score is attributed to knowledge graph structural effects rather than a true repurposing signal.

**To proceed, the following would be needed:**
- Identification of a plausible biological mechanism connecting Auranofin's known MOA (TrxR inhibition, redox modulation) to the developmental pathways disrupted in this syndrome
- Preclinical evidence (cell-line or animal model) demonstrating any phenotypic effect on ocular or skeletal development
- Regulatory clearance pathway assessment, given the drug is not currently marketed in this jurisdiction
- Expert consultation with rare disease geneticists and developmental biologists to evaluate biological plausibility before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

