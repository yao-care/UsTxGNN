---
layout: default
title: Pentostatin
parent: 僅模型預測 (L5)
nav_order: 1030
evidence_level: L5
indication_count: 7
---

# Pentostatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Pentostatin: From Hairy Cell Leukemia to Rhabdomyosarcoma (Pediatric Sarcoma Cluster)

## One-Sentence Summary

> Pentostatin is an adenosine deaminase (ADA) inhibitor historically used in lymphoid malignancies such as hairy cell leukemia.
> The TxGNN model assigns high scores to **7 rhabdomyosarcoma/sarcoma subtypes**, but these predictions are supported by **zero clinical trials** and **zero publications**,
> and the model's own rationale flags this as likely graph-embedding artifact rather than genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indications recorded) |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, pentostatin is an irreversible adenosine deaminase (ADA) inhibitor that causes dATP accumulation, selectively toxic to high-turnover lymphocytes — this underlies its established use in lymphoid malignancies (e.g., hairy cell leukemia).

Rhabdomyosarcoma and related sarcoma subtypes are mesenchymal/muscle-derived solid tumors, mechanistically distinct from lymphoid malignancies. There is no known biological link between ADA/purine salvage pathway inhibition and rhabdomyosarcoma pathogenesis.

Notably, the model itself flags a significant caveat: **7 predicted indications are all rhabdomyosarcoma subtypes or related sarcomas**, clustered at very similar scores (rank 11185–13473) and nearly identical confidence (99.4–99.5%). This pattern — many closely related disease nodes scoring almost identically — is a classic signature of TxGNN capturing **disease-node embedding similarity** (i.e., these diseases sit close together in the knowledge graph's pediatric solid tumor cluster) rather than a real drug-disease pharmacological relationship. This should be treated as low-confidence output pending independent validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Pentostatin has no approved licenses in Taiwan (未上市 / Not marketed); no license records are available for this evidence pack.

---

## Cytotoxicity

Pentostatin is a purine analog / antineoplastic agent (ADA inhibitor), meeting antineoplastic classification criteria.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Purine analog / antimetabolite class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 7 predicted indications lack any clinical trial or literature support, and the mechanistic rationale explicitly identifies this cluster as a likely artifact of disease-embedding similarity rather than genuine drug repurposing signal. Additionally, the drug is not marketed in Taiwan and has no recorded approved indications, contraindications, or MOA data — leaving multiple blocking gaps.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap (DG001)
- Verified mechanism of action from DrugBank — currently a High-severity data gap (DG002)
- Original approved indication(s) to establish a baseline for similarity assessment
- Preclinical evidence (in vitro/in vivo) evaluating pentostatin activity in rhabdomyosarcoma cell lines or models, given the absence of any existing clinical/literature signal
- Independent confirmation that this prediction cluster is not solely driven by knowledge-graph disease-node proximity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

