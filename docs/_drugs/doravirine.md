---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 622
evidence_level: L5
indication_count: 3
---

# Doravirine
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

# Doravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) whose established use, based on the mechanistic notes in this evidence pack, is treatment of HIV-1 infection. The TxGNN model's top-ranked prediction for this drug is **feline acquired immunodeficiency syndrome (FIV)** — a veterinary, non-human indication — with **no clinical trials** and **no literature** currently supporting this specific link, and the evidence pack itself flags the underlying mechanism as unlikely to translate across species/viruses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (NNRTI; inferred from the repurposing rationale notes — not present as structured data, since `original_indications` and `licenses` are both empty) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (FIV) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap in this evidence pack (`original_moa: [Data Gap]`). Based on the mechanistic notes attached to the predicted indications, Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) whose proven efficacy is in human HIV-1 infection, acting by binding an allosteric pocket on the HIV-1 reverse transcriptase enzyme.

FIV (feline immunodeficiency virus) belongs to the same *Lentivirus* genus as HIV-1, and TxGNN's knowledge graph likely surfaced this candidate through a shared category association ("reverse transcriptase inhibitor" ↔ "lentiviral infection") rather than direct experimental evidence. However, the evidence pack's own mechanistic-link note is explicit that this analogy is weak: NNRTI binding pockets are highly virus/species-specific, and Doravirine — like other NNRTIs — is not known to inhibit reverse transcriptases from lentiviruses other than HIV-1. FIV is also a veterinary disease, which falls outside the standard human-drug repurposing pathway entirely.

For reference, the second-ranked prediction (simian immunodeficiency virus infection) carries a similarly high TxGNN score and is supported by one indirect review-level publication — but that publication discusses islatravir (a translocation inhibitor, mechanistically distinct from Doravirine's NNRTI action), not Doravirine itself. The third-ranked prediction (a rare neurodevelopmental disorder) has no plausible mechanistic link at all and is flagged in the source data as a likely embedding-proximity artifact. Taken together, the top three TxGNN predictions for this drug do not currently constitute an actionable human repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

*(Note: one review-level publication, PMID [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/), was found for the related rank-2 prediction — simian immunodeficiency virus infection — but it discusses islatravir, not Doravirine, and does not support the FIV indication above.)*

---

## US Market Information

No marketing authorizations are on record for this drug. Market status: **Not Marketed** (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `safety.key_warnings`, `safety.contraindications`, and DDI query results are all empty/not found in this evidence pack. This corresponds to data gap DG001 — TFDA label warnings/contraindications — flagged as **Blocking severity**, meaning this candidate cannot proceed to the S1 safety pre-screening stage until resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) with zero clinical trials and zero literature directly supporting Doravirine for FIV, the top-ranked disease is a veterinary indication outside standard human drug development, and the mechanistic rationale attached to this prediction itself assesses the cross-species/cross-virus extrapolation as biologically weak.
- A Blocking-severity data gap (DG001 — TFDA warnings/contraindications) independently prevents this candidate from entering the S1 safety pre-screening stage regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) to resolve DG001 and enable S1 safety screening
- Confirmed mechanism-of-action data via DrugBank API to resolve DG002 and support a rigorous mechanistic-link analysis
- Direct experimental or clinical evidence of Doravirine activity against non-HIV-1 lentiviral reverse transcriptases, if this indication is to be pursued further
- Re-evaluation of whether TxGNN's top-ranked candidates for this drug reflect a genuine repurposing signal or a knowledge-graph category artifact, given all three top predictions currently lack direct supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

