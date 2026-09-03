---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 1045
evidence_level: L5
indication_count: 4
---

# Pimecrolimus
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

> Pimecrolimus is a topical calcineurin inhibitor originally developed and marketed (as Elidel) for atopic dermatitis.
> The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
> with **1 completed Phase 2 RCT** and **18 supporting publications** (including two independent systematic reviews of RCTs) currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis (known global approved indication for pimecrolimus/Elidel; no local regulatory license record found — see below) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available in this evidence pack (data gap, DG002). Based on the pharmacological information captured in the evidence, Pimecrolimus is a topical calcineurin inhibitor that selectively inhibits T-cell activation and blocks release of pro-inflammatory cytokines including IL-2, IL-4, IFN-γ, and TNF-α. It also inhibits mast cell degranulation. This mechanism was developed specifically for inflammatory skin disease and underlies its approved use in atopic dermatitis.

Atopic dermatitis and seborrheic dermatitis are both chronic, T-cell-mediated inflammatory skin conditions, though seborrheic dermatitis additionally involves an immune response to *Malassezia* yeast on the skin. Because pimecrolimus's anti-inflammatory action is not corticosteroid-based, it avoids the skin-atrophy risk associated with long-term topical steroid use — a major unmet need in seborrheic dermatitis management, where facial and scalp skin is particularly steroid-sensitive.

This mechanistic overlap is not merely theoretical: pimecrolimus 1% cream has already been directly studied in seborrheic dermatitis in a dedicated Phase 2 RCT and in multiple independent randomized trials against active comparators (ketoconazole, sertaconazole), with two systematic reviews of RCTs concluding comparable efficacy to standard antifungal/corticosteroid therapy. This makes the TxGNN prediction a reasonable extension of an already-validated mechanism rather than a speculative new hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | Randomized, double-blind, active-comparator-controlled, 4-week study evaluating Elidel (pimecrolimus) for treatment of seborrheic dermatitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT (active comparator) | Clinical and Experimental Dermatology | Randomized blinded trial comparing pimecrolimus 1% cream vs. sertaconazole 2% cream for facial seborrheic dermatitis. |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic Review (RCTs) | Expert Review of Clinical Pharmacology | Pimecrolimus 1% cream is well-tolerated and effective for seborrheic dermatitis, with efficacy comparable to corticosteroids and antimycotics. |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | American Journal of Clinical Dermatology | Reviews topical treatment options for facial seborrheic dermatitis, including calcineurin inhibitors as an alternative to steroids/antifungals. |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic Review | Cureus | Critical review of RCT efficacy and safety data for pimecrolimus in facial seborrheic dermatitis. |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | Open randomized comparative study | Journal of Dermatological Treatment | Pimecrolimus 1% cream compared with ketoconazole 2% cream shows pimecrolimus used successfully in seborrheic dermatitis. |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Review | International Journal of Clinical Practice | Reviews pimecrolimus mechanism (T-cell/mast-cell modulation) and its dermatological uses "beyond" atopic dermatitis. |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Seminars in Cutaneous Medicine and Surgery | Early review identifying seborrheic dermatitis among off-label uses of topical calcineurin inhibitors due to their favorable safety profile. |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | Journal of Drugs in Dermatology | Discusses therapeutic horizons for facial seborrheic dermatitis, including immunomodulator options. |
| [36174707](https://pubmed.ncbi.nlm.nih.gov/36174707/) | 2023 | Review | Actas Dermo-Sifiliográficas | Reviews sensitive scalp conditions, including seborrheic dermatitis, and relevant topical management strategies. |
| [31053034](https://pubmed.ncbi.nlm.nih.gov/31053034/) | 2019 | Review | Journal of Cutaneous Medicine and Surgery | Reviews off-label uses of topical pimecrolimus, with focus on published RCTs supporting efficacy in non-AD dermatoses. |

---

## US Market Information

Pimecrolimus currently has **0 regulatory licenses on record** in the tracked dataset (`market_status: 未上市 / Not Marketed`). No NDA/authorization entries are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A dedicated Phase 2 RCT plus two independent systematic reviews of RCTs and multiple active-comparator trials consistently support pimecrolimus's efficacy in seborrheic dermatitis, and the mechanism directly extends its already-validated anti-inflammatory action in atopic dermatitis. Evidence level L2 is sufficient to proceed cautiously, but formal safety and regulatory documentation are currently missing.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (currently blocking data gap, DG001)
- Formal DrugBank mechanism-of-action documentation (high-priority data gap, DG002)
- Confirmation of current market/licensing status, since 0 local licenses are on record despite this being an internationally marketed drug (Elidel)
- A drug-drug interaction (DDI) review, since none was found in the current query
- A structured safety monitoring plan specific to seborrheic dermatitis use (e.g., application-site reactions, long-term facial-use surveillance)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

