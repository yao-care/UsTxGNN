---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 1
---

# Adapalene
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Adapalene: From Acne Vulgaris to Zinc, Elevated Plasma

## One-Sentence Summary

Adapalene is a third-generation synthetic retinoid, recognized globally as a topical first-line treatment for acne vulgaris, but currently not registered or marketed in Taiwan.
The TxGNN model predicts it may have therapeutic relevance for **Zinc, Elevated Plasma** (hyperzincemia),
with **0 clinical trials** and **0 publications** currently supporting this direction — making this a pure model-driven prediction that requires substantial validation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally indicated for Acne Vulgaris (topical) |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Market Status (Taiwan TFDA) | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on publicly available pharmaceutical knowledge, Adapalene is a naphthoic acid derivative that selectively binds to nuclear retinoic acid receptors RAR-β and RAR-γ. It modulates genes involved in cellular differentiation, proliferation, and inflammatory signaling, and is established globally as a topical therapy for acne vulgaris (e.g., Differin® by Galderma, US FDA-approved in gel 0.1% and 0.3% formulations).

The potential mechanistic link to zinc metabolism is indirect but biochemically grounded: retinoic acid receptors (RARs) belong to the nuclear receptor superfamily and contain zinc finger structural domains essential for DNA binding. Zinc serves as a critical cofactor in retinoid receptor function, and there is known crosstalk between retinoid signaling pathways and cellular zinc homeostasis at the transcriptional level. The TxGNN knowledge graph may have identified this zinc–retinoid relationship as a shared biological node and inferred a repurposing signal.

However, "zinc, elevated plasma" as a distinct clinical condition (hyperzincemia) is rare, typically arising from industrial zinc exposure, excessive supplementation, or secondary metabolic disorders. The therapeutic application of a topical retinoid to a systemic zinc imbalance is mechanistically speculative and clinically non-intuitive. The prediction should be interpreted with significant caution and treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information (Taiwan TFDA)

Adapalene has no registered licenses with Taiwan's Food and Drug Administration and is currently not marketed in Taiwan.

> For reference: Adapalene is globally marketed as **Differin®** (Galderma) in the United States under US FDA approval, indicated for topical treatment of acne vulgaris. Taiwan market authorization is absent from this Evidence Pack. Detailed US market license data should be consulted separately if needed for regulatory cross-reference.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by the TxGNN model score (Evidence Level L5), with zero clinical trials and zero published literature connecting adapalene to zinc, elevated plasma. The mechanistic bridge is speculative, the predicted indication is a rare and clinically unusual metabolic condition, and adapalene carries no Taiwan regulatory history to anchor a safety assessment.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank or primary literature, specifically any role adapalene may play in zinc transporter regulation or systemic zinc homeostasis
- Preclinical evidence (in vitro or animal models) demonstrating adapalene's effect on plasma zinc levels
- Taiwan TFDA package insert (or equivalent) for complete safety, warning, and contraindication profiling
- Clinical plausibility review by an endocrinologist or metabolic disease specialist to assess whether hyperzincemia represents a realistic or meaningful therapeutic target for a retinoid compound
- Verification that the predicted indication ("zinc, elevated plasma") represents a true actionable disease entity in the knowledge graph rather than a graph topology artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

