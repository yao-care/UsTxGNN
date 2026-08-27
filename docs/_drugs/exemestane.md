---
layout: default
title: Exemestane
parent: 僅模型預測 (L5)
nav_order: 689
evidence_level: L5
indication_count: 7
---

# Exemestane
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

# Exemestane: From Breast Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane is a steroidal aromatase inhibitor historically used in hormone receptor-positive breast cancer (inferred from literature context in this evidence pack; not present in the structured indication field). The TxGNN model's top-ranked prediction for this drug is **Antithrombin Deficiency Type 2**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only association.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (hormone receptor-positive) — inferred from literature context; not recorded in structured data |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for exemestane is not available in this evidence pack (data gap DG002, High severity). Based on information embedded in this same batch's supporting literature (see the amenorrhea candidate below), exemestane is a steroidal aromatase inhibitor that suppresses estrogen synthesis and has established use in hormone receptor-positive breast cancer.

For the top-ranked candidate itself, **Antithrombin Deficiency Type 2**, the evidence pack's own mechanistic rationale states there is no known biological connection between aromatase inhibition/estrogen suppression and this inherited anticoagulant-factor disorder. Searches of ClinicalTrials.gov, ICTRP, and PubMed for this drug-disease pair returned zero results. This candidate reflects a TxGNN graph-embedding association rather than a pharmacologically grounded hypothesis.

For context, the same batch scored six additional candidates (ranks 2–7), all rated L5/Hold except amenorrhea (rank 2, L4). Even there, the underlying literature describes AI-induced ovarian suppression as a *cause* of amenorrhea in premenopausal breast cancer patients — the opposite of a therapeutic relationship. None of the seven candidates in this evidence pack currently support advancing past a preliminary hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No license records found. Exemestane is currently not marketed in the surveyed jurisdiction (0 approvals on file).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal/endocrine therapy (steroidal aromatase inhibitor) — not conventional cytotoxic chemotherapy; does not map cleanly onto the standard cytotoxic/targeted/immunotherapy categories |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (Antithrombin Deficiency Type 2) has zero clinical trial or literature support and no stated mechanistic link — evidence level L5 reflects a model-score-only prediction. A blocking data gap on TFDA safety labeling (DG001) and a complete absence of MOA data (DG002) further preclude any safety-informed decision at this stage.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — blocking gap DG001
- Exemestane MOA/DrugBank profile confirmation — data gap DG002
- A dedicated mechanistic/literature search specifically testing an aromatase–antithrombin pathway link, if one exists
- If pursuing amenorrhea (rank 2) as an alternative, resolve the therapeutic-direction mismatch — current evidence describes AI-induced amenorrhea, not AI as an amenorrhea treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

