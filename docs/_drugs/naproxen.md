---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 954
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Naproxen: From NSAID Therapy (Original Indication Not on Record) to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a long-established NSAID (COX-1/COX-2 inhibitor), though this evidence pack contains no recorded original indication or Taiwan/US license data for it. The TxGNN model predicts possible efficacy for **Brachydactyly-Syndactyly Syndrome**, a rare congenital limb malformation syndrome, but **0 clinical trials** and **0 publications** currently support this direction, and the model's own rationale notes no known biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license records or original indication data in this evidence pack |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% (rank 14,678 among candidates) |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for naproxen is flagged as a data gap in this evidence pack (High severity — DG002). However, the model's own repurposing rationale references naproxen's well-known pharmacology as a COX-1/COX-2 inhibitor that suppresses prostaglandin synthesis — the standard NSAID mechanism.

Brachydactyly-syndactyly syndrome is a rare congenital skeletal/limb malformation syndrome rooted in embryonic limb-patterning gene regulation, not in inflammation or prostaglandin-mediated pathology. The evidence pack's own rationale states explicitly that there is **no known mechanistic link** between COX-1/COX-2 inhibition and this disorder's developmental pathology, and that the high TxGNN score (0.9935) reflects knowledge-graph node-embedding similarity rather than any biological hypothesis.

The same pattern holds across the other top-ranked candidates in this pack (colobomatous microphthalmia-rhizomelic dysplasia syndrome, acromesomelic dysplasia Hunter-Thompson type, brachyolmia-amelogenesis imperfecta syndrome) — all are rare monogenic skeletal/structural developmental disorders with rationale text stating no known mechanistic connection to naproxen. This consistency across the top 4 predictions suggests the model signal here is not anchored to plausible biology for this drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Naproxen has 0 recorded licenses in this evidence pack, and market status is listed as Not Marketed. No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label/warning data is a Blocking-severity gap in this evidence pack — DG001 — and must be resolved before any safety review can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is an ultra-rare congenital skeletal syndrome with L5 evidence (model score only — zero trials, zero literature) and an explicit statement in the rationale that no biological mechanism connects naproxen's COX-1/COX-2 inhibition to this disorder. Combined with the absence of Taiwan/US market presence and unresolved MOA/label data gaps, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — currently a Blocking gap
- Confirmed MOA data via DrugBank API — currently a High-severity gap
- A biological or preclinical rationale linking NSAID/COX pathways to limb-patterning or skeletal dysplasia pathogenesis, which does not currently exist for this candidate
- Re-evaluation against lower-ranked, mechanistically plausible predicted indications if this pipeline continues for naproxen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

