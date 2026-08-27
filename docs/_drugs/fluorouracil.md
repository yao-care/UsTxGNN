---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 723
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: From Antineoplastic Chemotherapy to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil (5-FU) is a pyrimidine-analogue antimetabolite used broadly in cytotoxic chemotherapy; no confirmed original indication or Taiwan marketing data is available in this evidence pack. The TxGNN model predicts it may be effective for **botryoid-type embryonal rhabdomyosarcoma of the vagina**, but this is an ultra-rare disease subtype with **zero clinical trials** and **zero publications** currently supporting the specific prediction — the score reflects TxGNN's disease-ontology similarity only, not real-world evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no Taiwan license or original-indication data on file) |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the repurposing rationale accompanying this candidate, fluorouracil is a pyrimidine analogue that inhibits thymidylate synthase, blocking DNA synthesis and producing broad cytotoxicity against rapidly dividing cells — a mechanism consistent with its known role as a general-purpose cytotoxic chemotherapy agent.

The predicted link to this specific rhabdomyosarcoma (RMS) subtype is inferred purely from disease-ontology similarity to other RMS subtypes in the TxGNN knowledge graph, not from any direct study of this histology. A related, more general candidate in the same evidence pack — "rhabdomyosarcoma (disease)" — does have some supporting literature on cytotoxic chemotherapy in pediatric sarcomas, but 5-FU is not part of the standard RMS regimen (VAC: vincristine/actinomycin-D/cyclophosphamide), and none of that literature addresses the vaginal botryoid subtype specifically. For this exact indication, the mechanistic rationale remains theoretical only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No marketing authorizations on file — Taiwan regulatory status is "未上市" (not marketed) with 0 registered licenses.

## Cytotoxicity

Fluorouracil is a conventional cytotoxic chemotherapy agent (fluoropyrimidine/antimetabolite class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine/antimetabolite class; thymidylate synthase inhibition) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trials, no literature, and no Taiwan regulatory footprint — the 99.75% score reflects TxGNN disease-similarity to other rhabdomyosarcoma subtypes, not actual evidence for this ultra-rare histology. Evidence Level L5 (model prediction only) does not support any advancement decision at this time.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (blocking data gap — requires downloading and parsing the label PDF)
- Confirmed mechanism of action from DrugBank API (currently missing)
- Preclinical or case-level evidence specific to botryoid-type embryonal RMS of the vagina before this candidate can move past S0

**Note on related candidates in this evidence pack:** two other predicted indications for fluorouracil carry materially stronger evidence and may warrant separate evaluation — "rhabdomyosarcoma (disease)" (L4, 5 literature citations) and "liver sarcoma" (L3, 6 trials + 20 publications, though most trials matched on keyword rather than direct relevance to primary liver sarcoma). Neither reaches Go-level evidence, but both are better starting points than this specific vaginal-subtype candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

