---
layout: default
title: Avatrombopag
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

Using `txgnn-pipeline` to guide report generation, and following the Drug Repurposing Evaluation Report Prompt (v5) format.

---

# Avatrombopag: From Immune Thrombocytopenia to Macrothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Avatrombopag (Doptelet®) is a thrombopoietin receptor agonist (TPO-RA) established for treating thrombocytopenia in adults with chronic liver disease (CLD) scheduled for a procedure, and for chronic immune thrombocytopenia (ITP).
The TxGNN model predicts it may be effective for **Macrothrombocytopenia with Mitral Valve Insufficiency**, a rare platelet disorder compounded by a cardiac comorbidity.
Currently, **0 clinical trials** and **0 publications** specifically support this repurposing direction, placing confidence entirely at the model-prediction tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in evidence pack (data gap; avatrombopag is publicly known to be FDA-approved for CLD-associated thrombocytopenia and chronic ITP) |
| Predicted New Indication | Macrothrombocytopenia with Mitral Valve Insufficiency |
| TxGNN Prediction Score | 99.9954% |
| Evidence Level | L5 |
| US Market Status | Not captured (evidence pack shows 0 licenses; see note below) |
| Number of NDAs | 0 (not captured in evidence pack) |
| Recommended Decision | Hold |

> **Data Gap Notice**: The evidence pack reports 0 US licenses and "未上市" (not marketed). This appears to be a data collection issue rather than a reflection of actual approval status. Publicly available records show Doptelet® (avatrombopag) received FDA approval in May 2018 (CLD thrombocytopenia) and June 2019 (chronic ITP). The NDA and safety data should be retrieved from FDA records to complete this evaluation.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (identified as Data Gap DG002). Based on established pharmacological knowledge, avatrombopag is a small-molecule thrombopoietin receptor agonist (TPO-RA) that binds to and activates the TPO receptor (c-Mpl) on megakaryocytes, stimulating their proliferation and differentiation to increase platelet production. It belongs to the same drug class as eltrombopag and romiplostim, and its efficacy in raising platelet counts across multiple thrombocytopenic conditions has been confirmed in Phase 3 trials.

Macrothrombocytopenia with mitral valve insufficiency is a rare syndrome characterised by chronically low platelet counts with abnormally large platelets — often reflecting a megakaryocyte maturation defect — accompanied by structural mitral valve disease. For production-deficiency subtypes (where megakaryocytes fail to generate adequate platelets), TPO-RA stimulation provides a pharmacologically coherent rationale: boosting upstream megakaryocyte output may compensatorily restore platelet numbers toward hemostatic adequacy. Prior TPO-RA experience in related hereditary thrombocytopenias (romiplostim in MYH9-related disease, eltrombopag in ANKRD26-related thrombocytopenia) lends indirect support.

However, the mechanistic link carries important caveats. If the macrothrombocytopenia arises from a structural platelet defect rather than insufficient production — as in MYH9-related disorders — increasing platelet numbers does not repair platelet function. The concurrent mitral valve insufficiency introduces additional complexity: cardiac status, procedural bleeding risk, and potential interaction with anticoagulation must be independently assessed. Of all ten TxGNN predictions in this evidence pack, this is the most mechanistically grounded; the remaining eight predictions (ranks 5–10) cluster around motor neuron diseases (ALS and related syndromes) and neurological malformations, which have no known pharmacological link to TPO-RA and likely reflect knowledge-graph topological proximity rather than biological relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for avatrombopag in macrothrombocytopenia with mitral valve insufficiency.

---

## Literature Evidence

Currently no related literature available for avatrombopag in macrothrombocytopenia with mitral valve insufficiency.

---

## US Market Information

No license records are captured in the current evidence pack. FDA NDA data should be retrieved directly to complete this section.

> Based on publicly available information: avatrombopag (Doptelet®, AkaRx/Swedish Orphan Biovitrum) holds FDA approval under NDA 210238 (CLD thrombocytopenia, 2018) and NDA 210239 (chronic ITP, 2019). These should be formally verified and added to the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields in the current evidence pack are absent (key warnings, contraindications, and drug interaction data were not retrieved). Remediation identified in the evidence pack:

- **TFDA label / US FDA label**: Download and parse the full prescribing information (NDA label) to extract boxed warnings, contraindications, and special population precautions (Data Gap DG001).
- **Drug interactions**: DDI query returned no results; re-query using the US FDA label and DrugBank interaction database.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on model output (L5) with zero supporting clinical trials or publications. While a mechanistic rationale exists for production-deficiency subtypes of macrothrombocytopenia, no empirical evidence has yet tested this hypothesis, and the mitral valve comorbidity introduces safety uncertainties that cannot be assessed without a complete label review.

**To proceed, the following is needed:**

- **Close data gaps first**: Retrieve FDA NDA records (DG001) to confirm approved indications, boxed warnings, and contraindications; retrieve MOA details from DrugBank (DG002)
- **Patient subtype stratification**: Determine whether the target population represents production-deficient (TPO-responsive) vs. structurally-defective macrothrombocytopenia before designing any study
- **Precedent search**: Search for romiplostim and eltrombopag use in macrothrombocytopenia subtypes — positive signals from sister TPO-RAs would upgrade confidence even without avatrombopag-specific data
- **Cardiac safety assessment**: Evaluate avatrombopag's risk-benefit profile in patients with mitral valve insufficiency, including thrombotic risk at higher platelet counts and anticoagulation interaction potential
- **Flag neurological predictions (ranks 5–10) as topological artifacts**: ALS, lower motor neuron syndrome, Mills syndrome, monomelic amyotrophy, and bilateral polymicrogyria predictions show no pharmacological plausibility for a TPO-RA and should be deprioritised without further investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

