---
layout: default
title: Ferric Maltol
parent: 僅模型預測 (L5)
nav_order: 702
evidence_level: L5
indication_count: 3
---

# Ferric Maltol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Ferric Maltol: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Ferric maltol is an oral iron-replacement therapy used to treat iron deficiency anemia in adults. The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, a rare iron-deficiency-related disorder, with a prediction score of **99.98%** — but currently **no clinical trials or published literature** support this direction in the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia in adults (not recorded in evidence pack — based on the drug's known public profile; `drug.original_indications` is empty) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only — zero clinical trials, zero literature) |
| US Market Status | Not marketed (0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap in the evidence pack). Based on known public drug information, ferric maltol is a non-salt, trivalent iron(III)-maltol complex designed for controlled, low-toxicity absorption of iron across the intestinal mucosa. It is used to correct iron deficiency anemia in adults, including patients with inflammatory bowel disease who cannot tolerate conventional iron salts.

Plummer-Vinson syndrome (also known as Paterson-Brown-Kelly syndrome) is a rare condition defined by the triad of iron deficiency anemia, dysphagia, and esophageal webs. Because its core pathology is iron deficiency, a drug whose entire therapeutic function is iron repletion has a plausible mechanistic rationale here — this is why the prediction is biologically sensible on its face, even though it currently lacks any direct clinical or literature support.

By contrast, the evidence pack itself notes that a second TxGNN-flagged candidate — vitamin B12/folate-independent constitutional megaloblastic anemia — is mechanistically implausible for ferric maltol, since that condition stems from DNA synthesis defects rather than iron deficiency, and is likely a knowledge-graph false positive driven by "anemia" node clustering. This contrast supports treating the Plummer-Vinson signal as the more credible of the two, while still requiring confirmatory evidence before any action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: full TFDA label warnings/contraindications data for this drug is currently a **blocking data gap (DG001)** — required before this candidate can enter safety pre-screening.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on the TxGNN model score (L5) with no supporting clinical trials or literature, and the drug is not currently marketed in this jurisdiction (0 licenses). A blocking safety data gap (missing TFDA label) also prevents any safety pre-screening at this stage.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — resolves DG001 (Blocking)
- Confirmed mechanism of action via DrugBank API — resolves DG002 (High)
- Case reports, preclinical, or registry evidence specifically linking iron therapy to Plummer-Vinson syndrome outcomes
- Regulatory pathway assessment, since the drug currently holds no local marketing authorization

*Note: TxGNN also flagged two lower-ranked candidates not evaluated further here — vitamin B12/folate-independent constitutional megaloblastic anemia (likely knowledge-graph false positive per mechanistic review) and IRIDA syndrome (score 99.33%, no supporting evidence).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

