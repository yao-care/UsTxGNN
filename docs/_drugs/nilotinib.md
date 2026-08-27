---
layout: default
title: Nilotinib
parent: 僅模型預測 (L5)
nav_order: 965
evidence_level: L5
indication_count: 1
---

# Nilotinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Nilotinib: From Original Indication (Not Specified in Evidence Pack) to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nilotinib is a tyrosine kinase inhibitor (DrugBank DB04868); its original approved indication is not documented in this evidence pack (flagged as a data gap). The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, with **0 clinical trials** and **1 publication** currently supporting this direction, placing the candidate at an early, mechanism-driven research stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nilotinib is not available in this evidence pack (flagged as a High-severity data gap). Based on the repurposing rationale provided, nilotinib is a second-generation tyrosine kinase inhibitor with inhibitory activity against BCR-ABL, KIT, and PDGFR.

DFSP's characteristic molecular event is the COL1A1-PDGFB fusion gene, which drives constitutive activation of PDGFR-β and tumour proliferation. Because nilotinib directly inhibits PDGFR, it is mechanistically linked to the disease driver of DFSP.

Imatinib, a first-generation TKI with an overlapping target profile (including PDGFR), is already an approved/standard treatment for DFSP — this establishes a class-effect precedent supporting the plausibility of nilotinib's activity. However, direct clinical data for nilotinib specifically in DFSP remain very limited, largely confined to case-level reports in patients who failed or were intolerant to imatinib.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews the role of small-molecule PDGFR inhibitors (including nilotinib) in treating neoplastic disorders driven by PDGF/PDGFR signaling, supporting the mechanistic basis for PDGFR-driven tumours such as DFSP. |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BCR-ABL / PDGFR / KIT tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to a mechanistic rationale and a single review article (Evidence Level L4), with no clinical trials in DFSP; the model's own scoring places this candidate at decision stage S1 ("Research Question"). A blocking data gap on TFDA labeling (warnings/contraindications) also prevents a safety pre-assessment.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) to resolve the blocking safety data gap
- DrugBank-sourced mechanism of action (MOA) detail for nilotinib
- Confirmed original indication and DDI profile
- Case-series or trial-level clinical evidence of nilotinib specifically in DFSP (beyond the imatinib class-effect analogy)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

