---
layout: default
title: Tranexamic Acid
parent: 僅模型預測 (L5)
nav_order: 1248
evidence_level: L5
indication_count: 1
---

# Tranexamic Acid
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

# Tranexamic Acid: From Abnormal Uterine Bleeding to Amenorrhea

## One-Sentence Summary

> Tranexamic acid is a well-known antifibrinolytic agent used to **reduce** excessive menstrual/surgical bleeding; it is not marketed in this jurisdiction and no official original-indication text is on file in this evidence pack.
> The TxGNN model predicts a possible link to **Amenorrhea**, but the only two supporting publications discuss bleeding *suppression/prophylaxis* in cancer patients — not amenorrhea treatment — and the mechanistic rationale itself flags a likely **disease-entity mapping error** between "abnormal uterine bleeding" and "amenorrhea."
> With **0 clinical trials** and **2 tangentially relevant reviews**, this candidate does not currently meet the bar to advance past screening.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug is not marketed in this jurisdiction; no license records on file) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| Market Status | ✗ Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap in this evidence pack. Based on general pharmacology, tranexamic acid is a **plasminogen activator inhibitor (antifibrinolytic)**: it blocks the conversion of plasminogen to plasmin, thereby reducing fibrin breakdown and **decreasing bleeding**. Its established clinical use is to *reduce* excessive bleeding — e.g., abnormal uterine bleeding (AUB)/menorrhagia, surgical bleeding, and trauma-related hemorrhage.

**This creates a directional inconsistency with the predicted indication.** Amenorrhea is the *absence* of menstrual bleeding, which is pharmacologically the opposite problem tranexamic acid is designed to address. The two literature sources retrieved for this candidate both discuss AUB pharmacotherapy and menstrual *suppression/prophylaxis strategies in bleeding-risk cancer patients* — a different clinical concept than TXA causing or treating amenorrhea. The evidence pack's own rationale explicitly flags this as a likely **knowledge-graph disease node confusion** (AUB/menorrhagia vs. amenorrhea), rather than a genuine novel mechanistic hypothesis.

Given this, the prediction should be treated as a candidate for **disease-entity verification** before any further evaluation, not as a validated mechanistic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause (New York, N.Y.) | Reviews pharmacological therapy for **abnormal uterine bleeding** (not amenorrhea); antifibrinolytics reduce excessive bleeding by 25–35%. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Discusses menses **prophylaxis and suppression** strategies in pre-menopausal hematologic cancer patients with treatment-related cytopenias — a bleeding-risk-management context, not amenorrhea treatment. |

---

## US Market Information

No license/authorization records are available — the drug is not marketed in this jurisdiction (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: TFDA/local labeling data (warnings, contraindications, DDI) is marked as a **Blocking** data gap (DG001) in this evidence pack and could not be retrieved. This gap alone prevents progression to the S1 safety review stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trial evidence exists for this indication, and the two available literature sources describe bleeding suppression/management contexts rather than amenorrhea treatment — the predicted indication is mechanistically inverted relative to tranexamic acid's known antifibrinolytic action, suggesting a likely disease-entity mapping error in the knowledge graph.
- A Blocking safety data gap (DG001: local warnings/contraindications) independently prevents advancing to safety screening regardless of the indication question.

**To proceed, the following is needed:**
- Verify whether the TxGNN disease node "amenorrhea (disease)" was correctly mapped, or whether it should map to "abnormal uterine bleeding / menorrhagia" — this is a prerequisite before any further scientific review.
- Retrieve TFDA/local package insert warnings, contraindications, and DDI data (DG001).
- Retrieve confirmed MOA and original approved indication from DrugBank/regulatory sources (DG002).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

