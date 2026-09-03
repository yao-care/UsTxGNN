---
layout: default
title: Prilocaine
parent: 僅模型預測 (L5)
nav_order: 1081
evidence_level: L5
indication_count: 10
---

# Prilocaine
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

# Prilocaine: From Local Anesthesia to Papillary Conjunctivitis

## One-Sentence Summary

Prilocaine is an amide-type local anesthetic, historically used for topical and infiltration anesthesia (e.g., combined with lidocaine in EMLA cream) for minor surgical, dental, and dermatologic procedures. The TxGNN model's top-ranked prediction for this drug is **Papillary Conjunctivitis**, but this specific candidate is currently supported by **zero clinical trials** and **zero publications** — it is a pure knowledge-graph embedding signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (topical/injectable) — not documented in the available regulatory dataset |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap in the evidence pack). Based on general pharmacological knowledge, prilocaine is an amide-type local anesthetic that blocks voltage-gated sodium (Nav) channels in peripheral nerves, reducing neuronal excitability and pain signal transmission. Its established use is in local/regional anesthesia — it has no known pharmacological pathway relevant to conjunctival inflammation.

The evidence pack's own rationale for this candidate is explicit: there is "no clinical trial or literature support, and no known mechanistic link to papillary conjunctivitis," and the prediction is judged to be a **low-confidence knowledge-graph embedding pairing** rather than a biologically grounded hypothesis. No plausible connection between sodium-channel blockade and papillary conjunctivitis pathophysiology (typically allergic/mechanical, e.g., contact lens-related) is presented anywhere in the supporting data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Prilocaine currently holds **no NDA licenses** in the reviewed regulatory dataset (market status: Not Marketed; 0 total licenses on file). No product-level authorization details are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-ranked prediction (Papillary Conjunctivitis) has no clinical trial or literature evidence and no established mechanistic rationale — the score reflects only knowledge-graph embedding similarity, not a validated biological hypothesis. This does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action via DrugBank API query
- Independent literature/mechanistic search specifically probing local anesthetics in ophthalmic/conjunctival inflammatory conditions
- If a mechanistic or clinical signal cannot be established, this candidate should be deprioritized in favor of other predictions in the same TxGNN batch for this drug

**Note:** Among the 10 TxGNN predictions generated for prilocaine, **neuralgia** (rank 5, score 99.34%) shows substantially stronger existing evidence — evidence level L2, decision stage S3, "Proceed with Guardrails" — supported by a completed Phase 2 trial directly testing lidocaine/prilocaine cream (NCT00916942) and a Tier-1 RCT (PMID 2493878) on lidocaine-prilocaine cream in postherpetic neuralgia. This candidate may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

