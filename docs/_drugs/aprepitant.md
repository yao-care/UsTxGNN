---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is a selective NK1 (Neurokinin-1) receptor antagonist, widely used internationally for the prevention of chemotherapy-induced nausea and vomiting (CINV) and postoperative nausea and vomiting (PONV).
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chemotherapy-induced nausea/vomiting (CINV); Postoperative nausea/vomiting (PONV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Not marketed (no NDA data retrieved) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this Evidence Pack. Based on consistent references across all predicted indication rationales, Aprepitant acts as a selective Substance P / NK1 receptor antagonist. By blocking NK1 receptors in the central nervous system — primarily the area postrema and nucleus tractus solitarius — it interrupts the emetic signaling cascade triggered by chemotherapy, making it a cornerstone of CINV prophylaxis.

NSIAD is caused by a gain-of-function mutation in the **AVPR2** gene (V2 vasopressin receptor), which leads to constitutive receptor activation and chronic hyponatremia independent of ADH stimulation. While Substance P can indirectly modulate hypothalamic vasopressin secretion via NK1 receptors, there is **no established direct pathway** linking NK1 antagonism to AVPR2 gain-of-function signaling. These are mechanistically distinct receptor systems.

This prediction is best understood as a **knowledge graph topology inference**: Aprepitant and NSIAD share network neighbors in the TxGNN biological graph, but the mechanistic bridge is weak. The high TxGNN score (99.97%) reflects graph-structural proximity rather than demonstrated biological plausibility. No clinical trials or published literature support this application.

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
Despite a high TxGNN prediction score, the mechanistic connection between NK1 receptor antagonism and AVPR2 gain-of-function mutation is extremely weak — there is no known direct signaling pathway, and the prediction reflects knowledge graph topology inference rather than pharmacological plausibility. Without any supporting clinical trial or literature evidence (L5), this indication does not meet the threshold for further investment.

**To proceed, the following is needed:**

- **Confirm US authorization status**: Query the FDA Orange Book directly — Aprepitant (Emend®) is expected to hold an FDA NDA for CINV/PONV; the current zero-license result likely reflects a data pipeline gap
- **Retrieve prescribing information**: Obtain the full US label (warnings, contraindications, CYP3A4 drug interactions) to complete the safety profile before any indication expansion analysis
- **Prioritize mechanistically stronger candidates**: The following ranked indications carry a "Research Question" designation with better-reasoned mechanistic rationale and are recommended for next-stage evaluation:
  - **Pulmonary Arterial Hypertension** (Rank 3, score 99.90%): NK1 receptors expressed on pulmonary vascular endothelium; SP-driven vascular smooth muscle remodeling is a plausible target
  - **Subarachnoid Hemorrhage** (Rank 9, score 99.85%): Massive SP release post-hemorrhage activates NK1 receptors driving vasospasm and delayed cerebral ischemia; Aprepitant's established BBB penetration (required for its antiemetic mechanism) makes it a biologically credible candidate for investigating delayed ischemic neurological deficit
- **Focused mechanistic literature search**: For the two Research Question candidates above, conduct a targeted PubMed search combining Aprepitant/NK1 antagonist with pulmonary hypertension and cerebral vasospasm respectively before committing to preclinical studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

