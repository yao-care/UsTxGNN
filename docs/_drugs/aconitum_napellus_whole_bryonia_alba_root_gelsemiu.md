---
layout: default
title: Aconitum Napellus Whole Bryonia Alba Root Gelsemiu
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Bryonia Alba Root Gelsemiu
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# ACONITUM NAPELLUS / BRYONIA / GELSEMIUM / Meningococcal-Streptococcal Complex: Insufficient Data for Repurposing Assessment

## One-Sentence Summary

This submission contains a seven-component mixture combining homeopathic botanicals (Aconitum napellus, Bryonia alba, Gelsemium sempervirens), bacterial antigens (Neisseria meningitidis Group A polysaccharide, Streptococcus pyogenes), and pharmaceutical excipients (silicon dioxide, sodium carbonate).
The TxGNN model was **unable to generate repurposing predictions** for this compound due to the absence of a DrugBank ID and unresolvable multi-component identity.
No original approved indication, no predicted new indication, and no supporting clinical or literature evidence are available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None (TxGNN prediction not generated) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only; no actual studies identified |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction was generated for this compound. The primary reasons are:

**Identity resolution failure.** The submitted INN string is a semicolon-delimited list of seven distinct substances. TxGNN requires a single DrugBank-resolvable entity to traverse the knowledge graph. A multi-component mixture of this nature — particularly one combining homeopathic plant materials, bacterial polysaccharide antigens, and inert excipients — does not correspond to any single node in the DrugBank or knowledge graph vocabulary. DrugBank query returned one result but did not yield a valid `drugbank_id`, indicating a partial or ambiguous match.

**Mechanistic incompatibility with standard pipeline.** The mixture spans mechanistically unrelated categories: (1) Aconitum, Bryonia, and Gelsemium are classical homeopathic materia medica with no accepted pharmacokinetic or pharmacodynamic profile in evidence-based databases; (2) Neisseria meningitidis Group A capsular polysaccharide antigen and Streptococcus pyogenes lysate are immunological components typically found in vaccines or nosodes; (3) silicon dioxide and sodium carbonate are standard pharmaceutical excipients. Without a unified MOA or target protein, the repurposing algorithm cannot assign disease-node probabilities.

**Regulatory status.** This combination has no approved indication in any jurisdiction captured by the TxGNN data pipeline (US FDA, Taiwan FDA), which removes the anchor point normally used to contextualize predicted new indications.

---

## US Market Information

No approved licenses found. This compound is not registered with the US FDA or Taiwan TFDA.

---

## Safety Considerations

Please refer to the package insert for safety information. No DDI records, key warnings, or contraindication data were returned for this compound.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline cannot evaluate a multi-component mixture lacking a unified DrugBank identity and approved indication anchor. There is currently no evidence base — clinical, observational, or mechanistic — that would support a repurposing recommendation.

**To proceed, the following is needed:**

- **Clarify product identity**: Determine whether this is a registered homeopathic preparation, a nosode vaccine, or an experimental immunostimulant, and obtain the corresponding regulatory product code or DrugBank ID for each active component.
- **Decompose and run per-component**: If repurposing analysis is desired, submit each pharmacologically active ingredient (e.g., Aconitum napellus alkaloids such as aconitine, Gelsemium alkaloids such as gelsemine) as a separate TxGNN query with individual DrugBank IDs.
- **Clarify therapeutic intent**: Establish the original clinical context (homeopathic indication, immunotherapy, adjuvant) before any mechanistic or repurposing analysis is attempted.
- **Obtain package insert**: If a product under this formulation exists in any jurisdiction, retrieve the prescribing information to document safety profile and approved use.
- **YMYL note**: All outputs from this pipeline are for research reference only and do not constitute medical advice. Any repurposing candidate requires prospective clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

