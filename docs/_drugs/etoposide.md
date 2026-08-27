---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 685
evidence_level: L5
indication_count: 10
---

# Etoposide
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

# Etoposide: From Established Chemotherapy Use to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide (DrugBank DB00773) is a topoisomerase II inhibitor already used across multiple cytotoxic chemotherapy regimens; this evidence pack does not record its original TFDA/FDA-approved indications, as the drug is currently not marketed in Taiwan or the US under this dataset.
The TxGNN model predicts it may be effective for **well-differentiated fetal adenocarcinoma of the lung** (the epithelial component of pulmonary blastoma), but this is currently supported by only **0 clinical trials** and **1 case-report-level publication**, placing this specific candidate at the earliest research stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no Taiwan/US license data; drug not marketed) |
| Predicted New Indication | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, this evidence pack does not include a structured original mechanism-of-action (MOA) record for etoposide (`original_moa: [Data Gap]`). Based on mechanistic information captured elsewhere in this same evidence pack (see the rationale for related predicted indications), etoposide is a topoisomerase II inhibitor that induces DNA double-strand breaks, producing cytotoxic effects against rapidly proliferating tumor cells — the basis for its established role in combination chemotherapy regimens (e.g., platinum-etoposide).

Well-differentiated fetal adenocarcinoma is the epithelial component of classic biphasic pulmonary blastoma, a very rare lung malignancy with a mixed epithelial/mesenchymal histology. Per the evidence pack's rationale, "etoposide-platinum regimens have been used in case reports of related biphasic pulmonary blastoma, with a proposed mechanism of DNA damage being effective against rapidly proliferating mixed epithelial/mesenchymal tumors, though direct evidence remains extremely scarce."

Because this disease entity is exceptionally rare, no dedicated clinical trials exist, and the mechanistic rationale — while biologically plausible — is extrapolated from a single case report rather than from disease-specific investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case report/Review | The Journal of International Medical Research | Case of classic biphasic pulmonary blastoma (containing well-differentiated fetal adenocarcinoma component) treated with right upper lobe resection followed by nedaplatin plus paclitaxel adjuvant chemotherapy; no standard treatment guideline exists for this rare tumor. |

---

## Cytotoxicity

Etoposide is a conventional cytotoxic chemotherapy agent (topoisomerase II inhibitor, epipodophyllotoxin class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Topoisomerase II inhibitor / epipodophyllotoxin class) |
| Myelosuppression Risk | High — neutropenia is etoposide's principal, often dose-limiting toxicity; TFDA-specific label warnings could not be retrieved in this evidence pack (see Blocking data gap below) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. A Blocking-severity data gap was identified: TFDA package insert warnings/contraindications for etoposide could not be located, which prevents this candidate from entering the initial safety screening stage (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for this specific indication is limited to a single case-report-level publication with zero clinical trials (Evidence Level L4). Combined with a Blocking-severity gap in TFDA safety warnings/contraindications — which by definition prevents entry into the S1 safety screening stage — this candidate cannot currently advance.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently blocking (DG001)
- Structured mechanism-of-action documentation for etoposide (DG002)
- Additional clinical evidence beyond a single case report, given the extreme rarity of this histologic subtype (pulmonary blastoma accounts for <0.5% of primary lung malignancies)
- Taiwan/US market and licensing data, since the drug is currently not marketed in either jurisdiction per this evidence pack

**Note:** This evidence pack contains 9 other TxGNN-predicted indications for etoposide with markedly stronger evidence, notably **primary pulmonary lymphoma** and **rhabdomyosarcoma** (both L1, "Proceed with Guardrails," backed by dozens of trials including Phase 3 RCTs) and **Ewing sarcoma** (L1, "Proceed with Guardrails"). If a viable near-term repurposing candidate is the goal, one of those ranks may warrant a separate report rather than rank 1.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

