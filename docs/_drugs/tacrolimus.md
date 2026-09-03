---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 1191
evidence_level: L5
indication_count: 3
---

# Tacrolimus
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

# Tacrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus ointment (Protopic®) is an established topical calcineurin inhibitor for atopic dermatitis. The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**, with **2 clinical trials** and **20 publications** currently supporting this direction — much of which already reflects real-world off-label and even on-label dermatology practice.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis (topical formulation; per literature evidence — no formal license/regulatory record available in this evidence pack) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (`original_moa: [Data Gap]`). However, the supporting literature within this evidence pack consistently describes tacrolimus as a **calcineurin inhibitor**: it suppresses antigen-specific T-cell activation and downregulates the pro-inflammatory cytokine cascade (PMID 15819596, 12125507, 11145792). This anti-inflammatory, non-steroidal mechanism is the basis for its established use in topical treatment of atopic dermatitis (Protopic ointment), where it has been studied in over 16,000 patients across 20+ years of trials referenced here (e.g., NCT00480896, NCT00480610, NCT02601703).

Seborrheic dermatitis (SD) shares a similar inflammatory, T-cell-mediated pathophysiology with atopic dermatitis, occurring in sebaceous-rich areas and often exacerbated by *Malassezia* yeast colonization (PMID 16094289, 28685715). Because tacrolimus's anti-inflammatory action is not steroid-dependent, it avoids the skin atrophy and rebound risk associated with long-term topical corticosteroid use — a specific concern in facial SD, where corticosteroids are otherwise first-line (PMID 19213227, 27804089). This mechanistic overlap explains why dermatologists have already tested tacrolimus in SD for over two decades, from early open-label pilot work (PMID 12833030, 2003) through to multicenter randomized controlled trials (PMID 33010323, JAAD 2021).

Two additional TxGNN-predicted indications from the same evidence pack — **parapsoriasis** (rank 2, score 99.24%) and general **dermatitis** (rank 3, score 99.17%) — reinforce this signal. Both are also T-cell-mediated inflammatory dermatoses with published case reports and reviews supporting topical tacrolimus use (e.g., PMID 15149526, 12823321 for pityriasis lichenoides/parapsoriasis). Taken together, the model is largely re-identifying and quantifying a coherent, mechanistically consistent cluster of inflammatory skin conditions already responsive to calcineurin inhibition, rather than proposing an unrelated new indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated tacrolimus ointment (Protopic®) for maintenance treatment of severe facial seborrheic dermatitis in adults, aiming to reduce relapse frequency and prolong remission versus topical steroids. |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed whether proactive once/twice-weekly application of 0.1% tacrolimus ointment maintains remission and reduces exacerbation incidence in adult facial SD. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter, double-blind RCT: tacrolimus 0.1% vs. ciclopiroxolamine 1% for maintenance therapy in severe facial SD — first long-term maintenance comparison in this disease. |
| [22101215](https://pubmed.ncbi.nlm.nih.gov/22101215/) | 2012 | RCT | J Am Acad Dermatol | Single-blind RCT comparing hydrocortisone 1% ointment vs. tacrolimus 0.1% ointment for facial SD in adults. |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT | Ann Parasitol | Compared sertaconazole 2% cream vs. tacrolimus 0.03% cream in 60 SD patients. |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | RCT | Indian J Dermatol Venereol Leprol | Oral itraconazole (2 days) plus topical tacrolimus vs. topical tacrolimus alone for maintenance treatment of SD in Vietnam. |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical study | Ann Dermatol | Maintenance therapy of facial SD with 0.1% tacrolimus ointment, applying the intermittent maintenance model established in atopic dermatitis. |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open-label pilot | J Am Acad Dermatol | First pilot study of 0.1% tacrolimus in 18 SD patients; 61% achieved complete clearance within 28 days. |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids) for facial SD, situating calcineurin inhibitors among first-line options. |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Review of pathophysiology, safety, and efficacy of topical calcineurin inhibitors specifically in SD. |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Overview of facial SD status and therapeutic horizons, including sebaceous/hormonal and *Malassezia*-related mechanisms. |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | Early review of topical tacrolimus/pimecrolimus future directions, including SD, psoriasis, and lichen planus. |

---

## US Market Information

Tacrolimus is recorded as **not marketed** in this jurisdiction, with **0 license/NDA records** in the evidence pack. No authorization table can be generated from `taiwan_regulatory.licenses`.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** The evidence pack flags a **blocking data gap (DG001)** — TFDA/FDA label warnings and contraindications are unavailable — which prevents a formal safety (S1) assessment at this time. Drug-drug interaction data was also queried but not found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for seborrheic dermatitis is reasonably strong for a repurposing candidate — one completed Phase 3 RCT, one completed Phase 4 maintenance study, and multiple additional RCTs/reviews spanning two decades (L2 evidence level) — and the mechanism is biologically coherent with tacrolimus's established anti-inflammatory action in atopic dermatitis. However, the drug is not currently marketed in this jurisdiction, and critical safety data (label warnings, contraindications, DDI) is completely missing, blocking initial safety review.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) — resolve DG001 (Blocking)
- Confirmed mechanism of action from DrugBank — resolve DG002
- Drug-drug interaction profile for topical calcineurin inhibitors
- Clarification of regulatory/market status and any pathway for formulation-specific approval (topical ointment) for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

