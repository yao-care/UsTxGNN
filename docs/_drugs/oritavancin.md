---
layout: default
title: Oritavancin
parent: 僅模型預測 (L5)
nav_order: 995
evidence_level: L5
indication_count: 3
---

# Oritavancin
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

# Oritavancin: From Gram-Positive Bacterial Infections to Bacteroidaceae Infectious Disease (Low-Confidence Prediction)

## One-Sentence Summary

> Oritavancin is a lipoglycopeptide antibiotic whose detailed mechanism-of-action record is currently missing from DrugBank, and it holds no market authorization in Taiwan.
> TxGNN's top prediction suggests possible activity against **Bacteroidaceae infectious disease**, but this candidate — along with two other top-ranked predictions — is supported by **zero clinical trials and zero publications**, and the model's own mechanistic rationale flags all three as pharmacologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license records; drug class (per mechanistic evidence) is a Gram-positive-targeting lipoglycopeptide antibiotic |
| Predicted New Indication | Bacteroidaceae infectious disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | ✗ 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for oritavancin is currently marked as a data gap in DrugBank. However, the TxGNN rationale text itself supplies mechanistic context: oritavancin is a **lipoglycopeptide antibiotic** that inhibits peptidoglycan (cell wall) synthesis in Gram-positive bacteria by binding the D-Ala-D-Ala terminus of the peptidoglycan precursor, while also disrupting bacterial membrane integrity.

None of the three top-ranked predictions in this evidence pack fit that mechanism:

- **Bacteroidaceae infectious disease** — *Bacteroides* spp. are Gram-negative anaerobes. Their outer membrane physically blocks glycopeptide penetration, and oritavancin has no established clinical activity against Gram-negative organisms.
- **Ophthalmic herpes zoster** — caused by Varicella-zoster virus, a viral pathogen. Oritavancin has no antiviral mechanism whatsoever; this pairing is categorically mismatched (antibacterial vs. antiviral).
- **Mycoplasma pneumoniae pneumonia** — *M. pneumoniae* lacks a cell wall entirely, and is intrinsically resistant to all cell-wall-targeting agents, including glycopeptides.

In all three cases, the repurposing rationale supplied alongside the TxGNN score explicitly concludes that the high prediction score likely reflects knowledge-graph co-occurrence or embedding similarity rather than genuine pharmacological plausibility — i.e., these are probable false positives rather than credible repurposing leads.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

---

## Additional Predicted Indications (Ranks 2–3, Not Recommended)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Mechanistic Assessment | Decision |
|------|----------------------|-------------|-----------------|--------------------------|----------|
| 2 | Ophthalmic herpes zoster | 99.03% | L5 | Viral pathogen — no antibacterial mechanism applies | Hold |
| 3 | Mycoplasma pneumoniae pneumonia | 99.01% | L5 | Cell-wall-deficient organism — intrinsic resistance to glycopeptides | Hold |

All three top TxGNN candidates (including rank 1 above) share the same evidence profile: no clinical trials, no literature, and a mechanistic rationale that argues against — rather than for — biological plausibility.

---

## US Market Information

Oritavancin currently has **no Taiwan market authorization** (0 NDA/license records; market status: 未上市/Not Marketed). No product, dosage form, or approved-indication data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are currently unavailable — TFDA label data is a blocking data gap [DG001] for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predicted indications are at the earliest evaluation stage (S0/L5 — model prediction only, no clinical or literature support), and mechanistic review indicates each is likely a false positive: Gram-negative outer membrane exclusion (Bacteroidaceae), wrong drug class entirely (antiviral need vs. antibacterial drug — herpes zoster), and intrinsic target absence (cell-wall-deficient *M. pneumoniae*). Combined with the absence of any Taiwan market presence and missing core safety data, there is no basis to advance any of these candidates.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap — required before any S1 safety screening)
- Confirmed mechanism of action and approved indication(s) for oritavancin via DrugBank/FDA labeling
- If repurposing evaluation continues for this drug, redirect candidate screening toward Gram-positive pathogen indications consistent with its actual glycopeptide mechanism, rather than the three mechanistically incompatible candidates identified here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

