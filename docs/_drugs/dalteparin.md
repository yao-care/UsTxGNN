---
layout: default
title: Dalteparin
parent: 僅模型預測 (L5)
nav_order: 566
evidence_level: L5
indication_count: 5
---

# Dalteparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Dalteparin: From Anticoagulation (LMWH) to Thrombophilia due to Protein C Deficiency

## One-Sentence Summary

Dalteparin is a low molecular weight heparin (LMWH) anticoagulant, established in clinical practice for the prevention and treatment of venous thromboembolism (VTE) and cancer-associated thrombosis.
The TxGNN model predicts it may be effective for **Thrombophilia due to Protein C Deficiency, Autosomal Recessive**,
with **no clinical trials** and **no publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No market authorization data available |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological class, dalteparin is a low molecular weight heparin (LMWH) that exerts its anticoagulant effect primarily through potentiation of antithrombin III, leading to selective inhibition of Factor Xa. This suppresses thrombin generation and prevents clot propagation without directly affecting platelet function or fibrinolysis.

Protein C deficiency (autosomal recessive form) is a rare hereditary thrombophilia in which the natural anticoagulation pathway is critically impaired. Under normal physiology, activated Protein C inactivates coagulation Factors Va and VIIIa, limiting thrombin generation. In the homozygous recessive form, complete or near-complete Protein C deficiency leads to neonatal purpura fulminans and life-threatening thrombotic crises. Dalteparin's Factor Xa inhibition could theoretically provide exogenous anticoagulation that partially compensates for the absent Protein C pathway.

However, the mechanistic fit has significant limitations. The established standard of care for severe Protein C deficiency is Protein C concentrate replacement therapy, supplemented by long-term vitamin K antagonists (warfarin). LMWHs such as dalteparin are used only during acute bridging phases, and their role is not well-defined in the hereditary form of this condition. The TxGNN high score (99.88%) most likely reflects topological proximity in the knowledge graph — the edge "thrombophilia ← anticoagulant" — rather than a novel, clinically actionable therapeutic signal. No clinical trials or published literature were identified to support this repurposing direction.

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
This prediction rests entirely on model inference (L5 — no clinical study support). While anticoagulation is conceptually rational in a pro-thrombotic condition such as Protein C deficiency, the disease has well-established standard therapies (Protein C concentrate, warfarin), and LMWH's role is limited to acute bridging. The absence of any supporting trial or literature, combined with the drug's current non-marketed status in this jurisdiction, leaves insufficient basis to proceed.

**To proceed, the following is needed:**
- Mechanism of action data via DrugBank API (DG002 remediation) to confirm Factor Xa inhibition profile and any non-anticoagulant effects (e.g., anti-inflammatory, antineoplastic)
- Package insert safety data (DG001 remediation) — warnings, contraindications, and major drug interactions are essential before any S1 safety evaluation
- Targeted literature search for LMWH use specifically in hereditary thrombophilias (Protein C deficiency, homozygous and heterozygous forms)
- Comparative assessment against standard of care (Protein C concentrate, warfarin) to identify whether dalteparin offers any clinically meaningful advantage or niche role
- Regulatory feasibility assessment, given the drug is not currently authorized in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

