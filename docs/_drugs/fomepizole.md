---
layout: default
title: Fomepizole
parent: 僅模型預測 (L5)
nav_order: 734
evidence_level: L5
indication_count: 1
---

# Fomepizole
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

# Fomepizole: From Methanol/Ethylene Glycol Poisoning to Sclerosing Cholangitis

## One-Sentence Summary

Fomepizole is an alcohol dehydrogenase (and partial CYP2E1) inhibitor originally approved as an antidote for methanol and ethylene glycol poisoning. The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, with a prediction score of **99.28%**, but currently **no clinical trials or publications** support this direction — the signal is model-derived only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Methanol / ethylene glycol poisoning (antidote) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, confirmed mechanism of action (MOA) data from DrugBank is not yet available for this candidate (flagged as a data gap). Based on known pharmacology, fomepizole inhibits alcohol dehydrogenase and, to a lesser extent, CYP2E1 — the mechanism underlying its established use as an antidote in methanol and ethylene glycol poisoning.

The predicted link to sclerosing cholangitis appears to stem from knowledge-graph node similarity — plausibly connecting to the hypothesis that secondary sclerosing cholangitis in critically ill patients (SC-CIP) involves toxic bile acid and oxidative metabolism pathways that could theoretically intersect with alcohol/aldehyde dehydrogenase activity. However, this is a model-inferred association only: the underlying dataset contains no clinical trials or literature records connecting fomepizole to sclerosing cholangitis, so there is currently no direct pharmacological or clinical evidence supporting this mechanistic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

Fomepizole is not currently marketed in the US under this evidence pack, with no NDAs or license records on file.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with zero supporting clinical trials or literature, and a blocking data gap on TFDA/US label warnings and contraindications prevents any preliminary safety assessment (S1).

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) to clear the safety-review blocker
- Confirmed mechanism-of-action data from DrugBank to validate the mechanistic rationale
- Targeted literature or preclinical search for fomepizole in sclerosing cholangitis or related hepatobiliary/oxidative-stress models
- If preclinical or mechanistic support emerges, initiation of exploratory clinical evidence generation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

