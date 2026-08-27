---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 776
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
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

# Hydrocortisone: From Corticosteroid Anti-Inflammatory Therapy to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a glucocorticoid corticosteroid; its original approved indications are not documented in the available data (TFDA license records for this ingredient are absent). The TxGNN model predicts it may be effective for **Alopecia Areata**, with **4 clinical trials** and **20 publications** currently supporting this direction, including a completed Phase 3 RCT that directly compared hydrocortisone to another topical corticosteroid in this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no TFDA license/approved-indication text on file for this ingredient) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on known drug class information, hydrocortisone is a glucocorticoid corticosteroid that acts by suppressing local immune and inflammatory activity.

Alopecia areata is an autoimmune, non-scarring hair loss disorder in which T-cell–mediated attack on hair follicles drives disease activity. Topical and intralesional corticosteroids are already an established, current standard-of-care treatment for this condition, which gives the TxGNN prediction a clear and clinically validated mechanistic basis: the drug's known anti-inflammatory/immunosuppressive action directly addresses the T-cell-driven follicular attack that characterizes alopecia areata, rather than relying on an indirect or speculative pathway.

This is further reinforced by a completed Phase 3 RCT (NCT01453686 / PMID 24226568) that directly compared hydrocortisone 1% cream against clobetasol propionate 0.05% cream for alopecia areata in children — i.e., hydrocortisone was already used as an active comparator arm in a head-to-head efficacy trial for this exact indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | RCT comparing clobetasol propionate 0.05% cream vs. hydrocortisone 1% cream in children with alopecia areata; direct head-to-head evidence for hydrocortisone in this indication (relevance grade A). |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | Completed | 18 | Evaluated adrenal function after intralesional triamcinolone (not hydrocortisone) in alopecia areata patients; same-indication but different drug — indirect supporting evidence (grade C). |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | N/A | Not yet recruiting | 72 | Four-arm dose-response study of hair growth product formulations vs. placebo in androgenic alopecia; design may include corticosteroid-class comparators but not yet recruited, no results available (grade B). |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Studied abnormal steroid metabolism and bone density/quality in patients with mild autonomous cortisol secretion; not a treatment trial and only weakly related to hydrocortisone use in alopecia areata (grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Randomized clinical trial: clobetasol propionate 0.05% vs. hydrocortisone 1% for alopecia areata in children (publication of NCT01453686). |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | Cohort | Clinical and Experimental Dermatology | Retrospective analysis of topical corticosteroid under occlusion for severe alopecia areata (including alopecia totalis/universalis) in children. |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | Review | Journal of Cosmetic Dermatology | Systematic review/meta-analysis on laser-based and adjunct therapies for alopecia areata, contextualizing corticosteroid treatment options. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case series | Medical Times | Early case series on treatment of alopecia areata, partialis, and totalis with cortisone, hydrocortisone, prednisone, and prednisolone. |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Case report | Der Hautarzt | Reports hair regrowth in alopecia areata and alopecia maligna following intracutaneous hydrocortisone injection. |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Case series | Vestnik Dermatologii i Venerologii | Treatment of alopecia areata and total alopecia with intracutaneous hydrocortisone injections. |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Case report | Actas Dermo-Sifiliográficas | Treatment of alopecia areata with intradermal hydrocortisone injections. |
| [5696522](https://pubmed.ncbi.nlm.nih.gov/5696522/) | 1968 | Case report | British Journal of Dermatology | Examined scalp blood vessel changes in alopecia areata patients before and after corticosteroid therapy. |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case series | Journal of the American Academy of Dermatology | Describes 4 cases of congenital alopecia areata with long-term follow-up and topical treatment history. |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Review | Journal of the European Academy of Dermatology and Venereology | Reviews evidence on HPA-axis activity and cortisol production in alopecia areata patients. |

---

## US Market Information

No NDA, marketing authorization, or license records for this ingredient are on file in the evidence pack (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (No warnings, contraindications, or drug interaction data are currently on file — TFDA label data is flagged as a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT directly compared hydrocortisone to another topical corticosteroid in alopecia areata, and the mechanistic rationale (glucocorticoid suppression of T-cell-mediated follicular attack) is well established and already reflected in current clinical practice for this autoimmune condition. However, the existing RCT evidence is limited to a pediatric population, and critical safety and regulatory data for this candidate are still missing.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) — currently a Blocking gap (DG001)
- Detailed mechanism of action documentation from DrugBank — currently a High-severity gap (DG002)
- Confirmation of market/license status for a hydrocortisone product suitable for dermatologic (topical/intralesional) use
- Additional RCT data in adult alopecia areata populations, since current direct trial evidence is pediatric-only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

