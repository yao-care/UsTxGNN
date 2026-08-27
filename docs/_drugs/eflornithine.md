---
layout: default
title: Eflornithine
parent: 僅模型預測 (L5)
nav_order: 643
evidence_level: L5
indication_count: 2
---

# Eflornithine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Eflornithine: From African Trypanosomiasis/Hirsutism to Esotropia

## One-Sentence Summary

> Eflornithine is an irreversible ornithine decarboxylase (ODC) inhibitor known for treating African trypanosomiasis (sleeping sickness) and topical hirsutism (Vaniqa).
> The TxGNN model predicts it may be effective for **Esotropia**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph inference with no direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | African trypanosomiasis (systemic); topical hirsutism (Vaniqa) — no Taiwan marketing license on file |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eflornithine works by irreversibly inhibiting ornithine decarboxylase (ODC), blocking polyamine synthesis. This mechanism underlies its approved uses — systemic treatment of African trypanosomiasis and topical suppression of facial hair growth (Vaniqa) — both of which depend on halting cell proliferation in parasites or hair follicles.

Esotropia (inward eye deviation) is a neuromuscular/ocular-alignment disorder typically managed with prism correction, botulinum toxin, or surgery. There is no known physiological link between the ODC/polyamine pathway and extraocular muscle tone or neural control of eye position. The high TxGNN score most likely reflects an indirect graph relationship (e.g., shared genes or co-occurring nodes) rather than a pharmacological rationale, and should be treated as a low-confidence signal requiring manual expert review.

For context, the evidence pack's second-ranked candidate, neurotrophic keratopathy (score 99.38%), is arguably even less plausible: this condition requires *promoting* corneal epithelial repair, whereas eflornithine's antiproliferative mechanism (blocking polyamine synthesis) would theoretically work *against* that goal. Both candidates illustrate the same limitation — model-only predictions without any mechanistic or clinical corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Eflornithine currently holds no marketing authorization in Taiwan (0 licenses on file; market status: 未上市).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it is unsupported by any clinical trials, literature, or plausible mechanistic rationale, and a Blocking data gap (TFDA label warnings/contraindications) prevents even an initial safety assessment.

**To proceed, the following is needed:**
- TFDA/DrugBank-sourced labeling data (warnings, contraindications) to clear the current Blocking data gap
- Confirmed mechanism of action documentation to properly evaluate mechanistic plausibility for esotropia (and to resolve the apparent contradiction for neurotrophic keratopathy)
- Preclinical or observational evidence establishing any biological link between ODC/polyamine inhibition and either candidate indication before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

