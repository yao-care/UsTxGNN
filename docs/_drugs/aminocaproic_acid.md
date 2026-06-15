---
layout: default
title: Aminocaproic Acid
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 1
---

# Aminocaproic Acid
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

The data-report skill applies to CLI output — not applicable here. Proceeding to generate the structured evaluation report from the Evidence Pack JSON.

---

# Aminocaproic Acid: From Hemorrhage Control to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Aminocaproic acid is an antifibrinolytic agent that prevents excessive bleeding by inhibiting plasminogen activators and plasmin activity, thereby blocking thrombus dissolution.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy (SNPDR)**,
however, **0 clinical trials** and **0 publications** currently support this direction — the prediction is based on model inference alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in queried regulatory data |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the sources queried. Based on known pharmacological information, aminocaproic acid is an antifibrinolytic agent — it works by inhibiting plasminogen activators and plasmin, thereby preventing fibrin clots from breaking down prematurely. It is classically indicated for hemorrhagic conditions where excessive fibrinolysis drives bleeding.

The theoretical mechanistic link to SNPDR runs as follows: diabetic retinopathy involves retinal microvessel hemorrhage, and elevated fibrinolytic activity has been proposed to contribute to hemorrhagic progression. Suppressing fibrinolysis could, in theory, reduce this hemorrhagic component. However, the dominant pathological drivers of SNPDR are hyperglycemia-induced endothelial damage, VEGF-mediated vascular hyperpermeability, and pericyte loss — none of which are primarily fibrinolysis-driven. The antifibrinolytic mechanism therefore addresses a secondary rather than a central feature of this disease.

The TxGNN score of 0.993 is high, but in the absence of any clinical or preclinical studies, this score most likely reflects knowledge graph network topology associations — for example, indirect graph paths such as "antifibrinolytic → hemorrhagic disease → retinal hemorrhage → diabetic retinopathy" — rather than direct biological evidence. This prediction should be interpreted with considerable caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
With zero clinical trials and zero publications, this prediction rests entirely on TxGNN knowledge graph inference. The mechanistic connection between aminocaproic acid's antifibrinolytic action and the primary pathophysiology of SNPDR is indirect and speculative — fibrinolysis suppression does not address the core disease drivers of SNPDR.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank API to confirm pharmacological basis
- Safety profile including key warnings, contraindications, and drug interactions (obtain from package insert PDF)
- Preclinical evidence demonstrating antifibrinolytic effects specifically in diabetic retinopathy animal models
- Pharmacokinetic data confirming whether systemic or intravitreal administration can achieve therapeutic concentrations in retinal tissue
- Expert ophthalmology consultation to assess pathophysiological plausibility and whether fibrinolysis plays a measurable role in SNPDR progression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

