---
layout: default
title: Isosorbide Dinitrate
parent: 僅模型預測 (L5)
nav_order: 815
evidence_level: L5
indication_count: 10
---

# Isosorbide Dinitrate
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

# Isosorbide Dinitrate: From Angina Pectoris to Alopecia

## One-Sentence Summary

Isosorbide dinitrate (ISDN) is a nitrate vasodilator that is standard therapy for angina pectoris and ischemic heart disease. The TxGNN model predicts it may be effective for **Alopecia**, but this is currently a **pure model-score prediction** — there are **no clinical trials** and **no published literature** supporting this specific link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris / ischemic heart disease (established nitrate vasodilator use; no Taiwan NDA on file) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ISDN is not available in this evidence pack. Based on known pharmacology, isosorbide dinitrate is a nitric oxide (NO) donor that relaxes vascular smooth muscle via the NO–cGMP pathway, and it is an established vasodilator used for angina/ischemic heart disease (this core use is corroborated elsewhere in the evidence pack — see the "vascular disease" candidate, rank 6, where the same NO-cGMP mechanism is described as ISDN's standard, already-approved application).

For alopecia specifically, the evidence pack's own rationale states that the high TxGNN score is likely driven by an analogy to minoxidil — another vasodilator used to promote follicular blood flow and hair regrowth — rather than any direct evidence for ISDN itself. No clinical trials, no ICTRP-registered trials, and no PubMed literature were found for ISDN in alopecia (query log entries #4–6 all returned zero results). The mechanistic link is therefore theoretical extrapolation only, not a validated pharmacological relationship.

Two related candidates in the same evidence pack (rank 2 "congenital hypotrichosis milia" and rank 3 "hypotrichosis simplex of the scalp") are genetic/structural hair-follicle disorders with no plausible connection to a vasodilator mechanism, suggesting the model may be clustering ISDN with vasodilators near hair-related disease nodes in the knowledge graph rather than capturing a specific causal mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Supplementary note (not disease-specific, drawn from other entries in this evidence pack rather than formal DDI records): ISDN, as a nitrate, is contraindicated with PDE5 inhibitors (e.g., sildenafil, tadalafil) due to risk of severe hypotension. This should be checked against concomitant medications in any patient considered for an ISDN-based intervention, regardless of indication.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for alopecia is very high, but there is zero clinical trial or literature evidence to support it — this is Evidence Level L5 (model prediction only, no actual studies). Two structurally similar candidates in the same result set (congenital/simple hypotrichosis) also lack any supporting mechanism, reinforcing that this cluster of predictions is not yet actionable.

**To proceed, the following is needed:**
- ISDN mechanism of action (MOA) documentation (currently a blocking-severity data gap, DG002)
- TFDA/regulatory label — warnings, contraindications (currently a blocking-severity data gap, DG001)
- Preclinical or mechanistic studies specifically linking ISDN (not minoxidil) to hair follicle/dermal blood flow effects
- If preclinical rationale is established, an initial pilot/observational study before any trial design work
- Note: since ISDN is not currently marketed in Taiwan (0 NDAs), any path forward would also require a market-entry/registration assessment independent of the repurposing question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

