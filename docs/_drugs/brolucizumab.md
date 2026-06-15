---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 472
evidence_level: L5
indication_count: 4
---

# Brolucizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Brolucizumab: From Ophthalmic Anti-VEGF Use to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Brolucizumab is a humanized anti-VEGF-A single-chain antibody fragment (scFv) formulated as an intravitreal injection, used for the treatment of ophthalmic neovascular diseases (wet AMD and diabetic macular edema).
The TxGNN model predicts it may be effective for **Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies**,
however **no clinical trials or publications** currently support this direction, and the mechanistic plausibility is rated as extremely low.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ophthalmic neovascular diseases (wet AMD / diabetic macular edema) via intravitreal anti-VEGF injection |
| Predicted New Indication | Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory data on file. Based on context embedded in the Evidence Pack, Brolucizumab inhibits VEGF-A and is delivered as an intravitreal injection with very low systemic exposure (Cmax <1 ng/mL). Its established clinical role is in ocular angiogenesis — specifically the abnormal subretinal and choroidal neovascularization that drives vision loss in wet AMD and DME.

Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies is a rare, genetically defined disease caused by mutations in nuclear-encoded mitochondrial genes, resulting in impaired respiratory chain function and cellular energy failure. The pathophysiology is fundamentally metabolic and genetic in origin, with no established relationship to VEGF-mediated angiogenesis.

**The mechanistic link is extremely weak.** VEGF-A inhibition has no known capacity to correct nuclear DNA mutations or restore mitochondrial respiratory complex activity. The TxGNN knowledge graph may have connected these two entities through shared intermediate disease nodes (e.g., shared metabolic or vascular co-morbidity nodes) rather than a true biological pathway. This prediction is most likely a structural artifact of the graph topology and should not be interpreted as a biological signal. No clinical or preclinical evidence exists to support pursuing this hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Brolucizumab currently holds no drug licenses in Taiwan and is not marketed domestically. Regulatory approval and market entry would require a full NDA submission to the Taiwan FDA.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Taiwan regulatory labeling (包裝仿單) data was not retrieved in this Evidence Pack cycle. Full safety assessment — including warnings, contraindications, and special population precautions — cannot be completed until the TFDA product insert is parsed (Data Gap DG001, severity: Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN computational score (99.67%), there is no credible mechanistic basis connecting VEGF-A inhibition with mitochondrial nuclear DNA disorders. The intravitreal-only route of administration results in negligible systemic exposure, making systemic drug delivery to affected tissues physiologically implausible. With zero supporting clinical trials or publications (L5 evidence), this prediction does not meet the threshold for advancing to further evaluation.

**To proceed, the following is needed:**

- Identification of a plausible mechanistic bridge between VEGF-A inhibition and mitochondrial respiratory chain dysfunction (e.g., evidence involving mitophagy regulation, reactive oxygen species modulation, or vascular supply deficits in affected tissues)
- Preclinical in vitro or in vivo data demonstrating any effect of anti-VEGF agents in mitochondrial disease models
- A viable systemic delivery strategy, as the existing intravitreal formulation is pharmacokinetically unsuitable for treating a systemic mitochondrial disease
- Resolution of Data Gap DG001 (TFDA package insert) before any safety assessment can be initiated
- Resolution of Data Gap DG002 (full MOA characterization from DrugBank) to enable rigorous mechanistic analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

