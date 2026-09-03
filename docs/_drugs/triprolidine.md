---
layout: default
title: Triprolidine
parent: 僅模型預測 (L5)
nav_order: 1266
evidence_level: L5
indication_count: 7
---

# Triprolidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Triprolidine: From Antihistamine (Allergic Symptoms) to Allergic Urticaria

## One-Sentence Summary

> Triprolidine is a first-generation H1 antihistamine, but its original approved indication and market data are not available in this evidence pack.
> The TxGNN model predicts it may be effective for **Allergic Urticaria**,
> but this direction is currently supported by **0 clinical trials** and **0 direct publications** — evidence relies entirely on class-level (drug-class) mechanistic reasoning rather than triprolidine-specific data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license data in evidence pack) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (mechanism-level; no direct clinical/literature support for this specific indication) |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on known pharmacology, triprolidine is a first-generation H1-receptor antagonist (antihistamine), and H1-receptor blockade is the established, guideline-recognized (EAACI/GA2LEN) core mechanism for treating histamine-mediated urticaria and pruritus.

The mechanistic rationale connecting triprolidine to allergic urticaria is therefore a **class effect** argument: H1 antihistamines as a drug class are first-line urticaria therapy, so it is biologically plausible that triprolidine would also be effective. However, this evidence pack contains **no clinical trials and no literature specific to triprolidine** for allergic urticaria — the supporting logic is entirely mechanistic extrapolation from the drug class, not from triprolidine-specific data. This is the weakest tier of TxGNN-supported hypotheses and should be treated as a research question rather than a repurposing candidate ready for evaluation.

Notably, related literature does exist for a **triprolidine derivative** (acrivastine) in cold urticaria (see rank #2, PMID 2901993), and for triprolidine combinations (with pseudoephedrine) in a purulent nasopharyngitis trial (rank #4, PMID 6377256) — but neither directly addresses allergic urticaria, and neither constitutes triprolidine-specific efficacy evidence for the top-ranked indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for allergic urticaria specifically.

*Note: Related class-level evidence exists for other predicted indications in this pack (e.g., PMID 2901993 for cold urticaria using the triprolidine derivative acrivastine), but no literature directly supports the top-ranked allergic urticaria prediction.*

---

## US Market Information

No license/authorization records are available in this evidence pack (market status: 未上市 / Not marketed, 0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: This evidence pack flags a Blocking data gap — TFDA package insert warnings/contraindications are not yet available, which prevents completion of the S1 safety pre-screen. Key warnings, contraindications, and drug-drug interaction data are currently listed as data gaps and are omitted here per reporting policy.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the evidence level is only L4 and is based purely on drug-class mechanistic reasoning — there is no triprolidine-specific clinical trial or literature evidence for allergic urticaria, and a **Blocking** data gap (missing TFDA safety/label data) prevents even a baseline safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking gap
- Confirmed original approved indication(s) and MOA from DrugBank
- Triprolidine-specific clinical or observational evidence in allergic/chronic urticaria (not just class-level or derivative-drug data)
- Market/licensing status confirmation, since the drug currently shows as not marketed in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

