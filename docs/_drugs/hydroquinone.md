---
layout: default
title: Hydroquinone
parent: 僅模型預測 (L5)
nav_order: 778
evidence_level: L5
indication_count: 4
---

# Hydroquinone
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

# Hydroquinone: From Topical Skin Depigmentation (Hyperpigmentation/Melasma) to Seborrheic Keratosis

## One-Sentence Summary

Hydroquinone is a topical tyrosinase inhibitor long used internationally as a skin-lightening agent for hyperpigmentation and melasma, though it currently holds **no TFDA marketing license in Taiwan**. The TxGNN model predicts it may be effective for **Seborrheic Keratosis**, but this direction is currently supported only by **0 clinical trials** and **2 publications**, placing the evidence at the mechanistic/preclinical level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not TFDA-licensed in Taiwan. Internationally recognized use: topical depigmenting agent for hyperpigmentation/melasma (per trial context in this evidence pack) |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Market Status (Taiwan) | 未上市 (Not Marketed) |
| Number of Licenses (TFDA) | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for hydroquinone is flagged as a data gap in this evidence pack (DG002). However, based on information referenced across the associated clinical-trial evidence (e.g. NCT00669071, NCT05969587, NCT00616239 — all comparator/combination studies for melasma), hydroquinone's well-established pharmacology is as a **tyrosinase inhibitor**: it blocks the enzyme responsible for melanin synthesis, giving it a classic role as a topical skin-lightening/bleaching agent.

Seborrheic keratosis is a benign epidermal proliferation of keratinocytes that frequently presents with, or is cosmetically compounded by, hyperpigmented lesions. Hydroquinone's depigmenting action could theoretically lighten the pigmentation associated with these lesions, but it has no known effect on the underlying keratinocyte proliferation itself.

This means the mechanistic link is indirect: hydroquinone may address the **pigmentary symptom** that often accompanies seborrheic keratosis, not the **disease process** (benign keratotic hyperplasia) itself. The prediction is plausible from a symptom-management standpoint but does not yet constitute evidence of disease-modifying efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Cohort (prospective observational) | J Plast Reconstr Aesthet Surg | Proposes a combination-treatment algorithm for facial pigmentary disorders in Asian patients, noting most patients present with overlapping pigmentary conditions and no single definitive treatment addresses all of them simultaneously |
| [17373158](https://pubmed.ncbi.nlm.nih.gov/17373158/) | 2007 | Review | J Drugs Dermatol | Reviews treatment options for dermatosis papulosa nigra (DPN), a condition histologically similar to seborrheic keratosis; focuses on aesthetic lesion removal rather than pharmacologic depigmentation |

---

## US Market Information

Hydroquinone is currently **not licensed or marketed in Taiwan** (0 TFDA licenses on record). No product authorization, dosage form, or approved-indication data is available for this evidence pack.

---

## Safety Considerations

Safety data (key warnings, contraindications, drug-drug interactions) could not be retrieved for this evidence pack — TFDA labeling data was flagged as a **Blocking** data gap (DG001), which by itself prevents this candidate from completing a formal S1 safety screen. Please refer to the official package insert once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for seborrheic keratosis is limited to two mechanistic/observational publications (L4) with no clinical trials directly testing this indication, and the mechanistic link is indirect (pigment lightening, not lesion resolution). Compounding this, hydroquinone has no current Taiwan market license and its safety labeling is a Blocking data gap, so it cannot yet clear a basic S1 safety review.

**To proceed, the following is needed:**
- TFDA package insert / safety label (warnings, contraindications) to resolve DG001
- Formal DrugBank/mechanism-of-action documentation to resolve DG002
- Clinical or case-series evidence evaluating hydroquinone's effect on seborrheic keratosis lesions themselves, not only associated pigmentation
- A Taiwan licensing pathway assessment, given the drug is currently unmarketed here

*Note: Three other TxGNN-predicted indications for this drug (vulvar inverted follicular keratosis, exanthem, lichen disease) were also screened but scored L5/S0 "Hold" — the "exanthem" candidate in particular appears to be a knowledge-graph disease-mapping artifact, as all supporting trials/literature actually concern melasma/hyperpigmentation rather than exanthem, and is not recommended for further pursuit without a data-layer correction.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

