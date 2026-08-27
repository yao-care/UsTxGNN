---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 687
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From mTOR-Driven Malignancies to Liposarcoma

## One-Sentence Summary

Everolimus is an mTOR inhibitor whose original approved indications are not recorded in this evidence pack (data gap). The TxGNN model predicts it may be effective for **liposarcoma** (specifically dedifferentiated liposarcoma), with **1 clinical trial** and **5 publications** currently supporting this direction, though most evidence involves combination therapy rather than monotherapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (licenses and original_indications both empty — data gap) |
| Predicted New Indication | Liposarcoma (dedifferentiated liposarcoma / leiomyosarcoma) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on generally known pharmacology, everolimus is an mTOR (mechanistic target of rapamycin) inhibitor of the rapalog class, with established oncology use where mTOR pathway activation drives tumor growth.

Dedifferentiated liposarcoma has documented activation of the Akt-mTOR and MAPK pathways (PMID 26518767), providing a direct mechanistic rationale for mTOR-targeted therapy in this tumor type. This is consistent with the biologic hypothesis behind the ongoing SAR-096 trial, which combines everolimus with the CDK4 inhibitor ribociclib specifically because CDK4/6 dysregulation and mTOR pathway activation co-occur in dedifferentiated liposarcoma and leiomyosarcoma.

Because current supporting evidence centers on combination therapy (everolimus + ribociclib) rather than everolimus monotherapy, the mechanistic link is plausible but not yet demonstrated as a standalone effect — this tempers confidence relative to a single-agent efficacy signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Two-arm study of ribociclib + everolimus in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B) in patients with ≥1 prior systemic therapy; evaluates antitumor activity of the combination. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT/Trial Report | Clinical Cancer Research | Reports the SAR-096 Phase II trial of ribociclib + everolimus in DDL/LMS; notes synergistic growth inhibition of CDK4 inhibition (ribociclib) combined with mTOR inhibition (everolimus) in preclinical tumor models, forming the rationale for the combination. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | Review of patient-derived orthotopic xenograft (PDOX) sarcoma models identifying effective combination therapies with the CDK inhibitor palbociclib, supporting CDK/mTOR pathway co-targeting as a sarcoma treatment strategy. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanistic/Preclinical | Tumour Biology | Immunohistochemical analysis of 99 dedifferentiated liposarcoma specimens showing activation of the Akt-mTOR and MAPK pathways, with in vitro antitumor effects from an mTOR inhibitor. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Research | Broad-spectrum preclinical evaluation of eribulin combined with mechanistically distinct anticancer agents in liposarcoma and breast cancer xenograft models. |

## Cytotoxicity

Everolimus is used for oncology indications and is classified pharmacologically as a targeted agent rather than conventional cytotoxic chemotherapy, so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) — not a conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack — DG001, blocking severity — and a DDI query returned no results.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A mechanistically coherent rationale (Akt-mTOR pathway activation in dedifferentiated liposarcoma) is supported by an ongoing Phase 2 trial and consistent preclinical/mechanistic literature, but the strongest clinical evidence is for an everolimus + ribociclib combination, not monotherapy, and the trial has not yet reported final results (completion 2025-12).

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain regulatory label warnings/contraindications before any safety evaluation
- Resolve DG002: confirm mechanism of action from DrugBank or primary literature
- Await NCT03114527 completion/results to determine whether efficacy holds for everolimus's contribution specifically
- Clarify regulatory pathway, since the drug currently shows no marketed license status in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

