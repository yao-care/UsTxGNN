---
layout: default
title: Sulfasalazine
parent: 僅模型預測 (L5)
nav_order: 1187
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
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

# Sulfasalazine: From Rheumatoid Arthritis to Osteoarthritis

## One-Sentence Summary

Sulfasalazine is a long-established disease-modifying antirheumatic drug (DMARD), well known for treating rheumatoid arthritis and inflammatory bowel disease. The TxGNN model predicts it may also be effective for **Osteoarthritis**, and unlike the model's top-ranked candidates (mostly ultra-rare genetic syndromes with zero supporting evidence), this indication is backed by **2 clinical trials** and **20 publications** — making it the most credible repurposing signal in this evidence pack.

> **Note on selection**: Among the 10 TxGNN-predicted indications, ranks #1–4, #6–7, #9–10 are rare genetic/developmental syndromes (e.g., brachydactyly-syndactyly syndrome, WHIM syndrome) with **no clinical trials or literature at all** (Evidence Level L5, recommendation = Hold) — likely model noise rather than actionable signal. This report focuses on **Osteoarthritis (rank #5)**, the highest-ranked candidate with actual clinical and mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis / Ulcerative Colitis (well-established clinical use; no formal TFDA license record available in this evidence pack) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap — MOA not yet retrieved from DrugBank API). Based on known information, sulfasalazine is a combination molecule (sulfapyridine + 5-aminosalicylic acid) belonging to the DMARD class, with proven efficacy in rheumatoid arthritis and inflammatory bowel disease through anti-inflammatory and immunomodulatory action.

Multiple preclinical studies in this evidence pack suggest a mechanistic bridge to osteoarthritis: sulfasalazine appears to inhibit NF-κB signaling and pro-inflammatory cytokine (IL-1β/TNF-α)-induced cartilage degradation. In animal and ex-vivo cartilage models, it reduced proteoglycan and collagen loss and downregulated cartilage-degrading enzymes (MMPs/ADAMTS), suggesting chondroprotective potential.

However, this mechanistic evidence is largely an extension of rheumatoid arthritis-focused research rather than purpose-built osteoarthritis drug development. No trial in this evidence pack directly tests sulfasalazine as a monotherapy intervention in an OA patient population — the two identified clinical trials involve other drugs (tofacitinib/MTX, CRx-102) in adjacent rheumatic disease contexts. The prediction is therefore mechanistically plausible but clinically unproven.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A | Completed | 479 | Retrospective claims-database cohort comparing tofacitinib (Xeljanz) + MTX withdrawal vs. continuation in RA patients; sulfasalazine is not the intervention drug — relevance graded low (C) |
| [NCT00551707](https://clinicaltrials.gov/study/NCT00551707) | Phase 2 | Completed | 51 | Placebo-controlled RCT of CRx-102 (dipyridamole + low-dose prednisolone) in active RA; sulfasalazine not directly tested — relevance graded moderate (B), disease population uncertain |

**Note**: Neither trial directly evaluates sulfasalazine in an osteoarthritis population; both were captured via broader rheumatic-disease search overlap.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Preclinical (in vitro/animal) | Int J Biol Macromol | Sulfasalazine-hyaluronic acid sustained-release system reduced inflammation and cartilage degradation in an MIA-induced rat OA model |
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Preclinical (animal, ACLT+MMx) | J Orthop Res | Sulfasalazine attenuated cartilage destruction in a surgically-induced OA model via inhibition of the cystine/glutamate antiporter (system Xc−) |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | Preclinical (chondrocyte proteomics) | Mod Rheumatol | Sulfasalazine and tofacitinib altered protein profiles of articular chondrocytes |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | Preclinical (cartilage explant) | Rheumatology (Oxford) | Sulfasalazine blocked cytokine-stimulated release of proteoglycan/collagen fragments and downregulated MMPs/ADAMTS in cartilage explants |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | In vitro pharmacology | Wien Klin Wochenschr | Sulfasalazine and metabolites inhibited leukotriene release from synovial tissue of OA, chondrocalcinosis, and RA patients |
| [11478054](https://pubmed.ncbi.nlm.nih.gov/11478054/) | 2001 | Review | Hand Clin | Overview of pharmacologic treatment options across RA and OA |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Review | Front Immunol | Review of ferroptosis mechanisms across inflammatory arthritis subtypes including OA |
| [9567207](https://pubmed.ncbi.nlm.nih.gov/9567207/) | 1998 | Review | Curr Opin Rheumatol | Broader update on rheumatic disease clinical trials, including RA and OA therapeutics |

**Note**: All identified literature is preclinical, in vitro, or narrative review — no RCT or clinical outcome study of sulfasalazine specifically in OA patients was found.

---

## US Market Information

Sulfasalazine currently has **no license records** in this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No authorization data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: This evidence pack flags TFDA warnings/contraindications as a **Blocking** data gap (DG001) — meaning a formal safety pre-assessment (S1) cannot proceed until the package insert is retrieved and parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for sulfasalazine in osteoarthritis is limited to preclinical/mechanistic studies (Evidence Level L3), with no RCT directly testing the drug in OA patients — the two available clinical trials involve different drugs and only tangential disease overlap. Combined with a **Blocking** severity data gap on TFDA safety labeling, this candidate cannot yet advance past the research-question stage.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) to resolve the Blocking safety data gap (DG001)
- DrugBank MOA query to resolve the mechanism-of-action data gap (DG002)
- A dedicated clinical trial or observational study testing sulfasalazine specifically in an OA patient population
- Confirmation of regulatory/marketing status, since this drug currently shows 0 licenses in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

