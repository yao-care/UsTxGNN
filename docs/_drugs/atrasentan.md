---
layout: default
title: Atrasentan
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 1
---

# Atrasentan
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

The `txgnn-pipeline` skill confirms this is a standard TxGNN pipeline report task. The Evidence Pack is for an L5, Hold-recommendation case with no clinical trials or literature. Generating the report now:

---

# Atrasentan: From No Approved Indication to Amenorrhea

## One-Sentence Summary

Atrasentan is a selective endothelin A (ETA) receptor antagonist with no approved indication or marketing authorization in the United States.
The TxGNN model predicts it may be effective for **Amenorrhea**, based on its theoretical role in regulating vascular tone along the hypothalamic–ovarian axis.
There are currently **no clinical trials** and **no publications** directly supporting this direction — this remains a model-prediction-only finding (Evidence Level L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atrasentan is a selective endothelin A (ETA) receptor antagonist. Endothelin-1 (ET-1), acting through ETA receptors, is one of the body's most potent vasoconstrictors — it regulates ovarian blood flow, endometrial perfusion, and hypothalamic GnRH pulse secretion. Blocking ETA receptors could theoretically relieve vasoconstriction-driven ischemia in the ovaries or restore disrupted hypothalamic signaling, both of which are recognized contributors to amenorrhea.

However, this mechanistic link is an indirect inference drawn from known ET-1 physiology in the reproductive axis — it is not supported by direct preclinical or clinical data targeting amenorrhea. The TxGNN prediction is derived from drug–disease topological proximity within the knowledge graph, not from empirical observation. The signal reflects biological plausibility, not clinical validation.

No original approved indication data is available for atrasentan in this Evidence Pack. With mechanism of action data still pending confirmation, evaluating the full translational pathway from ETA antagonism to amenorrhea relief requires foundational pharmacological investigation before further steps can be planned.

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
This prediction is based solely on TxGNN knowledge graph inference with zero supporting clinical trials or publications (L5). There is currently no empirical basis — preclinical or clinical — linking atrasentan to amenorrhea, and safety data is unavailable, making any forward progression premature.

**To proceed, the following is needed:**
- **Mechanism of action confirmation** — verify ETA receptor selectivity and downstream effects on the hypothalamic–pituitary–ovarian axis
- **Safety and warnings data** — TFDA/FDA package insert review or DrugBank query to establish contraindications and key risks
- **Preclinical evidence** — in vitro or animal model studies investigating ETA antagonism in amenorrhea or ovarian ischemia models
- **Drug-drug interaction data** — currently no DDI records available
- **Regulatory history review** — confirm whether atrasentan has been studied in any indication (prostate cancer, nephropathy, pulmonary hypertension) that could inform safety extrapolation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

