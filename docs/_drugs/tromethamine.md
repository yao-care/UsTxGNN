---
layout: default
title: Tromethamine
parent: 僅模型預測 (L5)
nav_order: 1268
evidence_level: L5
indication_count: 10
---

# Tromethamine
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

# Tromethamine: From Metabolic Acidosis to Allergic Urticaria

## One-Sentence Summary

Tromethamine (THAM, DrugBank DB03754) is a TRIS-buffer compound whose established clinical role is as a systemic alkalizing agent for metabolic acidosis; no formal indication record or mechanism-of-action data is currently available for this drug itself.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, but this prediction is currently supported by **0 clinical trials** and only **1 case-report publication** — and that publication actually describes an anaphylactic *adverse reaction* to a related compound (Ketorolac tromethamine), not a therapeutic benefit.
Evidence strength is minimal and the signal should be treated as exploratory only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this dataset; known clinical use is as a systemic alkalizing agent for metabolic acidosis |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for tromethamine itself. Based on known information, tromethamine is a proton-accepting buffer (TRIS) used clinically as a systemic alkalizing agent in metabolic acidosis; it has no established antihistaminic, mast-cell-stabilizing, or immunomodulatory mechanism that would plausibly explain efficacy in allergic urticaria.

The only literature evidence retrieved for this candidate (PMID 16831313) does not actually support the prediction: it is a case report of a **biphasic anaphylactic reaction caused by Ketorolac tromethamine**, an NSAID that happens to use tromethamine as its salt-forming counter-ion. This is a drug-safety case describing tromethamine's salt form as a *trigger* of a hypersensitivity reaction, not evidence that tromethamine treats urticaria. The direction of the association is therefore opposite to what would be needed to support repurposing.

Given the absence of a plausible mechanistic link, the absence of any clinical trial evidence, and a single piece of literature that points toward harm rather than benefit, this TxGNN signal should be interpreted as a graph-based statistical association rather than a clinically meaningful hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16831313](https://pubmed.ncbi.nlm.nih.gov/16831313/) | 2006 | Case Report | Int J Immunopathol Pharmacol | Describes a biphasic anaphylactic reaction following intramuscular Ketorolac tromethamine injection; illustrates a hypersensitivity risk associated with the tromethamine salt form rather than a therapeutic effect on urticaria |

---

## US Market Information

Tromethamine currently has no NDA/license records in this dataset (market status: Not Marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN graph score (L5) with no clinical trials and a single literature item that describes an adverse hypersensitivity reaction rather than therapeutic evidence. Combined with the lack of mechanism-of-action data and the drug's current non-marketed status, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for tromethamine (independent of its use as a salt-forming counter-ion in other drugs, e.g., Ketorolac tromethamine, Fosfomycin tromethamol)
- Original approved indication and labeling information (TFDA/FDA label warnings and contraindications — currently a blocking data gap)
- Any pharmacology or preclinical data specifically linking tromethamine (not its salt partners) to mast-cell/histamine pathways relevant to urticaria
- Re-screening of literature/trial evidence to exclude confounding from other tromethamine-salt drugs, which affected several lower-ranked candidates in this same evidence pack (e.g., post-bacterial disorder, post-infectious syndrome) and should be treated as a systematic data-quality caveat for this drug across all predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

