---
layout: default
title: Dimenhydrinate
parent: 僅模型預測 (L5)
nav_order: 610
evidence_level: L5
indication_count: 2
---

# Dimenhydrinate
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

# Dimenhydrinate: From Unspecified Original Indication (Not Marketed) to Allergic Urticaria

## One-Sentence Summary

> Dimenhydrinate (DrugBank DB00985) is **not currently marketed in Taiwan**, and this evidence pack contains no record of an approved original indication for the compound.
> The TxGNN model's top-ranked prediction identifies **Allergic Urticaria** as a candidate new indication, with a prediction score of **99.74%**.
> Supporting evidence is currently limited to **1 publication** (a pharmacokinetic study, not a clinical efficacy trial) and **0 registered clinical trials**, so this remains a hypothesis-generating signal rather than a clinically validated direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license records exist for this compound (`taiwan_regulatory.licenses` is empty) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 (mechanism/preclinical-level support only) |
| Market Status (Taiwan) | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for dimenhydrinate is flagged as a data gap in this evidence pack (DG002, High severity). Based on the literature evidence that *was* collected, dimenhydrinate is a salt combination of **diphenhydramine** and **8-chlorotheophylline**, where diphenhydramine is the pharmacologically active moiety and functions as a first-generation **H1 histamine receptor antagonist** (Ehling et al., 2019, PMID 30779257). The 8-chlorotheophylline component is added primarily to offset diphenhydramine's sedative effect and to improve oral absorption, rather than to contribute independent antihistaminic activity.

No original approved indication is on file for this compound in the current evidence pack — `taiwan_regulatory.licenses` is empty and the drug is not marketed in Taiwan, so a direct "original indication → new indication" comparison cannot be made from regulatory data alone. Instead, the rationale here is a **class-level mechanistic link**: allergic urticaria is a mast-cell-mediated condition in which histamine release drives vasodilation, increased vascular permeability, and pruritus — the exact pathway that H1 antagonists like diphenhydramine are designed to block. This is consistent with the well-established clinical use of first-generation antihistamines across the urticaria/allergic-dermatologic disease class.

The caveat is that the only literature currently linked to this prediction is a **pharmacokinetic study in dogs**, not a clinical efficacy trial in allergic urticaria patients. It supports plausibility of drug exposure and receptor engagement, but it is indirect evidence — it does not demonstrate therapeutic efficacy for this specific indication.

*For context, a related TxGNN candidate — cold urticaria (score 99.24%, rank 16816) — shares the same class-level mechanistic rationale (H1-mediated mast cell degranulation) but has zero supporting trials or literature (Evidence Level L5, recommendation: Hold) and is not pursued further in this report.*

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic Study | Veterinary Dermatology | Compared diphenhydramine PK after oral/IV diphenhydramine vs. oral dimenhydrinate in dogs; dimenhydrinate produced superior oral absorption of diphenhydramine and assessed pharmacodynamic effect on histamine-induced wheal formation. Supports H1-antagonist mechanism relevant to allergic/pruritic conditions but is not a clinical efficacy study in urticaria. |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a Blocking data gap (DG001) — this is required before any S1 safety pre-screen can proceed. No drug-drug interaction data was found in the queried source.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only supporting evidence is a single pharmacokinetic study, not a clinical trial or efficacy study in allergic urticaria; combined with the L4 evidence level, this is insufficient to advance beyond a research hypothesis.
- Core safety data (TFDA warnings/contraindications) is a **Blocking** gap (DG001), which by itself prevents any S1 safety pre-screen regardless of predicted indication strength.
- The compound is not currently marketed in Taiwan (0 licenses), so there is no existing regulatory or post-market safety foundation to build on locally.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA (or equivalent) label warnings/contraindications before any safety pre-screen can begin.
- Resolve DG002: confirm mechanism of action via DrugBank API query to formally support the class-level rationale used above.
- Generate or identify direct clinical evidence in allergic urticaria (efficacy trials or case series), since current support is limited to an indirect PK study.
- Obtain drug-drug interaction data (current query status: not found).
- Re-evaluate once original indication/regulatory history for dimenhydrinate (e.g., from a market where it is approved) is available, to properly assess similarity between original and new indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

