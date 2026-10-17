---
layout: default
title: Ferric Maltol
parent: Model Prediction Only (L5)
nav_order: 702
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Ferric Maltol: predicted new indication Plummer-Vinson syndrome (evidence level L5). Approved use: Iron deficiency anemia"
monitor_inn: "FERRIC MALTOL"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia"]
---

# Ferric Maltol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Ferric Maltol: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Ferric maltol is an oral iron replacement originally used to treat iron deficiency anemia.
The TxGNN model predicts it may be useful for **Plummer-Vinson syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on mechanistic inference alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia (the US license record has no indication text; this is taken from the drug's known indications in the knowledge graph) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferric maltol is an oral iron complex, its efficacy in iron deficiency anemia is established, and mechanistically it may be applicable to Plummer-Vinson syndrome.

Plummer-Vinson syndrome (also called Paterson-Brown-Kelly syndrome) is characterized by iron deficiency anemia, dysphagia caused by esophageal webs, and glossitis. Because iron deficiency anemia is a core feature of the condition, an oral iron that corrects the deficiency is a plausible treatment for that component.

Two caveats apply. First, this is a mechanistic inference only. The data compiled for this report do not show whether iron repletion resolves the esophageal webs. Second, the new indication overlaps closely with the existing one, so this is better seen as an extension of the original use than a true repurposing. The very high TxGNN score is a computational prediction, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212320 (cancelled) | ACCRUFER (Shield TX (UK) Ltd) | Capsule | Not listed in the data compiled for this report |

## Safety Considerations

- **Contraindicated conditions (from the knowledge graph, not label text)**: hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease. These are consistent with the risk of iron overload.

No drug-interaction records were found. For other safety information, please refer to the package insert.

## Other Predictions Considered

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Vitamin B12- and folate-independent constitutional megaloblastic anemia | 99.98% | L5 | Hold. Megaloblastic anemia stems from impaired DNA synthesis, not iron deficiency, so iron would not be expected to help unless iron deficiency coexists. The high score likely reflects network proximity to other anemia terms. |
| IRIDA syndrome | 99.33% | L5 | Hold. IRIDA is caused by TMPRSS6 mutations that raise hepcidin and block iron absorption, so oral iron is expected to have limited benefit. Parenteral iron is the more rational approach. |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Plummer-Vinson syndrome prediction has no supporting trials or publications (L5), and the drug has no active US license. The mechanistic link is plausible but largely overlaps with the existing indication. The other two predictions have weak or unfavorable mechanistic support.

**To proceed, the following is needed:**
- The FDA package insert, to obtain warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search on iron therapy in Plummer-Vinson syndrome, including whether iron repletion resolves esophageal webs
- Clarification of the cancelled US license status and whether the product is still marketed
- Confirmation of route compatibility (oral capsule) for the proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

