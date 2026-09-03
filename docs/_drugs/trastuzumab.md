---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 1250
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

> Trastuzumab (Herceptin) is a monoclonal antibody long established for HER2-positive breast cancer (and HER2-positive gastric cancer). The TxGNN model predicts it may also be relevant to **normal breast-like subtype of breast carcinoma**, a PAM50 molecular subtype, but this is currently supported by only **12 clinical trials** (mostly on HER2+ breast cancer broadly, not this subtype specifically) and **1 publication** (a morphology/pathology study, not a treatment trial).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (well-established use; Evidence Pack does not contain Taiwan/US regulatory license text — see Data Gap below) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| US Market Status | 未上市 (Not marketed, per Evidence Pack) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on general public knowledge, trastuzumab is a humanized monoclonal antibody that binds the extracellular domain of HER2, blocking HER2-driven proliferation and mediating antibody-dependent cellular cytotoxicity (ADCC) — its efficacy in HER2-overexpressing breast (and gastric) cancer is well established.

The predicted new indication, "normal breast-like subtype of breast carcinoma," refers to one of the five PAM50 intrinsic molecular subtypes of breast cancer (Luminal A, Luminal B, HER2-enriched, Basal-like, Normal-like). This subtype is typically characterized by **low HER2 expression**, which weakens the direct mechanistic rationale for trastuzumab, since the drug's activity depends on HER2 overexpression.

The AI's own rationale for this candidate is explicit about this limitation: *"normal breast-like" is a PAM50 intrinsic subtype typically associated with low HER2 expression, which has a weak mechanistic link to trastuzumab's HER2-overexpression target; the listed trials largely study HER2+ breast cancer populations broadly rather than this subtype specifically, so the high TxGNN score likely reflects trastuzumab's broad association with breast cancer rather than a subtype-specific mechanism.* This should be read as a caution against over-interpreting the score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | Recruiting | 370 | ARIADNE: T-DXd vs. standard preoperative therapy in HER2+ breast cancer, using biology-driven (subtype) treatment selection |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Neoadjuvant weekly paclitaxel ± carboplatin in triple-negative breast cancer; not specific to trastuzumab or normal-like subtype |
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | Completed | 56 | Neratinib ± fulvestrant in HER2 non-amplified but HER2-mutant breast cancer — mechanistically opposite to trastuzumab's target population |
| [NCT05659056](https://clinicaltrials.gov/study/NCT05659056) | Phase 2 | Recruiting | 65 | Pyrotinib + trastuzumab + Abraxane neoadjuvant therapy in HER2-enriched early/locally advanced breast cancer, using PAM50/BluePrint subtyping |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | Recruiting | 25 | WOKVAC vaccine + neoadjuvant chemotherapy + HER2-targeted monoclonal antibody therapy |
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Phase 2 | Recruiting | 716 | FASCINATE-N: precision neoadjuvant therapy platform stratified by clinical/molecular subtype |
| [NCT06585969](https://clinicaltrials.gov/study/NCT06585969) | Phase 3 | Withdrawn | 0 | T-DXd vs. CDK4/6 inhibitors in non-Luminal A, ER+/HER2-low metastatic breast cancer (trial withdrawn) |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Phase 2 | Completed | 23 | Paclitaxel + trastuzumab + pertuzumab as preoperative therapy for inflammatory breast cancer |
| [NCT06328387](https://clinicaltrials.gov/study/NCT06328387) | Phase 1/2 | Unknown | 120 | Hydroxychloroquine + ADC vs. ADC alone in advanced breast cancer |
| [NCT04759248](https://clinicaltrials.gov/study/NCT04759248) | Phase 2 | Active, not recruiting | 55 | ATREZZO: atezolizumab + trastuzumab + vinorelbine in ER-negative or PAM50 non-luminal HER2+ advanced/metastatic breast cancer |

None of the above trials specifically enroll or report outcomes for the "normal breast-like" PAM50 subtype as a defined study population.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Pathology/Morphology study | Breast Cancer (Tokyo, Japan) | Describes morphological/cytopathological characteristics of PAM50 subtypes (including normal breast-like); does not report treatment outcomes with trastuzumab |

---

## Cytotoxicity

Trastuzumab is an antineoplastic (HER2-targeted monoclonal antibody), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (as an anti-HER2 agent, cardiac function/LVEF monitoring is a known clinical consideration for this drug class) |
| Handling Protection | Please refer to the package insert warnings and precautions |

No specific toxicity data was provided in this Evidence Pack (safety fields were flagged as Data Gaps).

---

## Safety Considerations

Please refer to the package insert for safety information. In addition, note that TFDA-specific warnings/contraindications for this drug are flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety (S1) assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between trastuzumab and the "normal breast-like" PAM50 subtype is weak, since this subtype typically has low HER2 expression. Evidence is limited to L2 (no trial directly tests this subtype) and the decision stage is S1 (Research Question), with the AI's own rationale flagging that the high TxGNN score likely reflects trastuzumab's general breast-cancer association rather than a subtype-specific mechanism.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (Blocking gap, DG001) before any safety review can begin
- Confirmed mechanism of action data from DrugBank (High-priority gap, DG002)
- A clinical trial or biomarker study specifically stratifying HER2/PAM50-normal-like patients and reporting trastuzumab outcomes in that subgroup
- Taiwan/US regulatory licensing data currently missing from this Evidence Pack

**Note:** Two other predicted indications in this candidate set — *progesterone-receptor positive breast cancer* and *progesterone-receptor negative breast cancer* — carry substantially stronger evidence (L1, multiple completed Phase 3 RCTs, decision stage S3, "Proceed with Guardrails") and largely represent confirmation of trastuzumab's existing HER2+ breast cancer indication rather than a novel repurposing hypothesis. These may warrant separate, higher-priority review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

