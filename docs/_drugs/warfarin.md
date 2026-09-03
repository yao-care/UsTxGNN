---
layout: default
title: Warfarin
parent: 僅模型預測 (L5)
nav_order: 1298
evidence_level: L5
indication_count: 7
---

# Warfarin
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

# Warfarin: From Original Indication (Not Recorded) to Heparin Cofactor II Deficiency

## One-Sentence Summary

> The evidence pack does not record Warfarin's original approved indication or mechanism of action for this jurisdiction (market status: not marketed, 0 licenses on file).
> The TxGNN model predicts it may be effective for **Heparin Cofactor II Deficiency**,
> with **0 clinical trials** and **5 publications** (case reports/reviews only) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (no `original_indications` or license data available) |
| Predicted New Indication | Heparin Cofactor II Deficiency |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Warfarin in this evidence pack (flagged as a High-severity data gap, DG002). Based on the repurposing rationale provided by the model, Warfarin acts as a vitamin K antagonist that suppresses synthesis of coagulation factors II, VII, IX, and X, and is already used broadly in clinical practice for long-term anticoagulation in hereditary thrombophilias.

Heparin cofactor II deficiency is a rare hereditary thrombophilia in which patients lack sufficient natural anticoagulant activity and are predisposed to venous thromboembolism. Mechanistically, extending Warfarin's established anticoagulant use in thrombophilic conditions to this specific deficiency is plausible, but the supporting evidence is indirect: no literature identified specifically evaluates Warfarin therapy in patients with confirmed heparin cofactor II deficiency. The available publications instead describe the disease itself (diagnosis, case reports, laboratory methods) or Warfarin use in adjacent thrombophilic conditions, making this a mechanism-driven hypothesis rather than a disease-specific evidence base.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11177584](https://pubmed.ncbi.nlm.nih.gov/11177584/) | 2001 | Review | AIDS Patient Care and STDs | Review of HIV-associated thrombotic risk, including hypercoagulable states from deficiencies of protein C/S and related natural anticoagulants |
| [3778142](https://pubmed.ncbi.nlm.nih.gov/3778142/) | 1986 | Review/Method | Arch Pathol Lab Med | Laboratory method for determining heparin cofactor II activity; low levels linked to liver disease, consumptive coagulopathy, and preeclampsia |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case Series | Journal of UOEH | Family with multiple thrombotic events, including infancy onset; known hereditary thrombophilias (including HC II deficiency work-up) were investigated |
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case Report | Kyobu Geka | Right ventricular thrombus in a 14-year-old with familial heparin cofactor II deficiency, surgically removed |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case Report | Nihon Kyobu Shikkan Gakkai Zasshi | Congenital antithrombin deficiency with pulmonary infarction; patient treated with Warfarin for 7 years before switching to heparin |

---

## US Market Information

No market authorization records are available in the evidence pack — Warfarin's market status is recorded as **未上市 (Not marketed)** with **0 licenses** on file for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/FDA labeling warnings, contraindications, and drug-drug interaction data are recorded as a **Blocking** data gap — DG001 — meaning safety review cannot currently proceed to Stage S1.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (heparin cofactor II deficiency) is supported only by L4 evidence — case reports and general reviews describing the disease, with no clinical trials or disease-specific therapeutic studies of Warfarin. Combined with the Blocking data gap on safety labeling and the absence of any market authorization record, the candidate cannot advance past the research-question stage at this time.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings and contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Warfarin mechanism of action documentation from DrugBank (DG002, High)
- Disease-specific interventional or observational studies in confirmed heparin cofactor II deficiency patients
- Confirmation of Warfarin's regulatory/market status in this jurisdiction

**Note:** Within this same evidence pack, a lower-ranked predicted indication — **thrombophilia** (rank 4, score 99.75%) — carries substantially stronger evidence (Evidence Level L1, Decision Stage S3, multiple completed trials including RCTs, recommendation "Proceed with Guardrails"). If a broader repurposing signal is the goal, that candidate may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

