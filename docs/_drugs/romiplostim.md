---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 1132
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: Research Signal for Primary Release Disorder of Platelets

*(Original approved indication is not recorded in this evidence pack — see note below)*

## One-Sentence Summary

> Romiplostim's original approved indication and market licensing data are not available in this evidence pack (the drug currently holds **no Taiwan/US license**, market status "Not Marketed").
> The TxGNN model predicts it may be relevant to **Primary Release Disorder of Platelets**, with a prediction score of **99.9998%**,
> but this signal is currently supported by only **1 clinical trial** (an observational cohort study, not an interventional romiplostim trial) and **2 review-level publications** — an early-stage research signal rather than established clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication or license record in this evidence pack) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank for this record. However, clinical trial descriptions embedded in the evidence pack consistently identify romiplostim as a **thrombopoietin (TPO) receptor agonist** — for example, NCT02335268 describes it explicitly as "romiplostim (a TPO receptor agonist)." Its known pharmacology stimulates megakaryocyte proliferation and differentiation, thereby increasing circulating platelet production.

The predicted indication, *primary release disorder of platelets*, is a disorder rooted in insufficient platelet production or release from megakaryocytes. This is mechanistically well aligned with romiplostim's core pharmacology of driving megakaryocytopoiesis — the same mechanism already exploited for immune thrombocytopenia (ITP) and related platelet-production disorders that recur throughout this evidence pack's broader trial and literature base.

That said, the one clinical trial currently linked specifically to this predicted indication (NCT03820960) is an observational risk-factor study on thrombosis in ITP patients, not an interventional trial of romiplostim itself. The mechanistic rationale is therefore currently stronger than the direct clinical evidence for this specific disease label.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Completed | 10,039 | Observational cohort study on thrombosis risk factors in immune thrombocytopenia (ITP); not an interventional romiplostim trial, but establishes disease-background relevance for platelet-release/production disorders. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Reviews megakaryocytopoiesis and thrombopoiesis biology, describing thrombopoietin (TPO) as the primary growth factor for the megakaryocyte lineage. |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Review | Haematologica | Shows antiplatelet autoantibodies in ITP inhibit proplatelet formation by megakaryocytes and impair platelet production in vitro, supporting the production-deficit mechanism relevant to TPO receptor agonist therapy. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial currently linked to this specific predicted indication is observational (not an interventional romiplostim study), and supporting literature is limited to two review articles. While the mechanistic rationale (TPO-RA → increased megakaryocytopoiesis → platelet production) is sound, direct clinical evidence for *primary release disorder of platelets* specifically is insufficient to move beyond a research question at this stage.

**To proceed, the following is needed:**
- Original indication and drug licensing/regulatory history (currently absent from this evidence pack)
- Detailed mechanism-of-action data from DrugBank
- TFDA/FDA labeling data (warnings, contraindications, drug interactions) — currently flagged as blocking data gaps
- A dedicated interventional trial evaluating romiplostim specifically in this disease population, rather than relying on adjacent-disease observational data

**Note for reviewers:** within the same evidence pack, a related predicted indication — *platelet-type bleeding disorder* (rank 8) — has substantially stronger supporting evidence, including a **completed Phase 3 RCT** (NCT03362177, RECITE) and an evidence level of **L1** with a "Proceed with Guardrails" recommendation. If the goal is to identify the strongest near-term repurposing candidate for romiplostim in this pack, that indication warrants separate, prioritized review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

