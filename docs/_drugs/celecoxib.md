---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Osteoarthritis to Inflammatory Spondylopathy

## One-Sentence Summary

Celecoxib (Celebrex®) is a first-in-class selective COX-2 inhibitor with established global indications for osteoarthritis, rheumatoid arthritis, and acute pain management; it is currently not registered in Taiwan.
The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** (encompassing ankylosing spondylitis and axial spondyloarthritis),
with **19 clinical trials** and **20 publications** currently supporting this direction — including multiple Phase 3 RCTs that have already led to regulatory approval in the United States and European Union.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not marketed in Taiwan; globally indicated for osteoarthritis, rheumatoid arthritis, and acute pain |
| Predicted New Indication | Inflammatory Spondylopathy (Ankylosing Spondylitis / Axial Spondyloarthritis) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| TW Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from our database. Based on the extensive published literature included in this evidence pack, Celecoxib is the first and most well-characterized selective cyclooxygenase-2 (COX-2) inhibitor (coxib) to enter clinical practice. It selectively blocks the COX-2 enzyme, reducing the synthesis of prostaglandin E2 (PGE2) and prostacyclin to alleviate inflammation and pain — while largely sparing the gastroprotective COX-1 pathway that conventional NSAIDs suppress.

The core pathology of inflammatory spondylopathy — including ankylosing spondylitis (AS) and axial spondyloarthritis (axSpA) — involves TNF-α and IL-17–driven inflammation of the spine and sacroiliac joints, leading to progressive new bone formation and functional restriction. NSAIDs targeting the prostaglandin pathway are the cornerstone of first-line therapy in all major AS/axSpA treatment guidelines. Celecoxib's selective COX-2 inhibition directly addresses this inflammatory pathway, reducing PGE2-mediated synovial and entheseal inflammation while offering a more favorable gastrointestinal safety profile compared to non-selective NSAIDs.

Critically, a 2025 systematic review (PMID 39757202) identified Celecoxib as the **only NSAID proven to inhibit radiographic bone progression** in spondyloarthritis — a disease-modifying property beyond simple analgesia, potentially involving Wnt signalling pathway regulation and osteoclast activity suppression. This is not a speculative repurposing proposal: Celecoxib already holds regulatory approval for AS in the United States (FDA), European Union (EMA), and multiple other markets. The TxGNN prediction is best interpreted as a **Taiwan market entry opportunity**, backed by a robust global evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week RCT comparing Celecoxib 200 mg QD, 200 mg BID vs Diclofenac 75 mg SR BID in AS; primary efficacy and safety evaluation |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | 6-week RDB study of Celecoxib vs Diclofenac SR specifically in Chinese AS patients, with 6-week extension phase |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | 12-week confirmatory RCT comparing Celecoxib 200 mg vs 400 mg QD vs Diclofenac TID in AS |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: Celecoxib + Golimumab vs Golimumab alone over 2 years; evaluated radiographic spinal progression in r-axSpA |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Etanercept vs Celecoxib vs combined treatment in active AS over 54 weeks; MRI SPARCC score as primary endpoint |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | NSAID (including Celecoxib) effects on MRI inflammatory lesions in axSpA; imaging endpoint study |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials comparing selective COX-2 vs non-selective COX inhibitors in axSpA; also evaluated HrQOL and proteomic biomarkers |
| [NCT02355236](https://clinicaltrials.gov/study/NCT02355236) | Phase 4 | Unknown | 106 | RDB multi-center study comparing Naxozol (naproxen+esomeprazole) vs Celecoxib in OA/RA/AS patients; gastroprotection comparison |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminated | 9 | Pilot 6-week RDB trial of 4 different NSAIDs in axSpA; terminated early due to low enrollment |
| [NCT02456363](https://clinicaltrials.gov/study/NCT02456363) | Phase 2 | Unknown | 300 | Adalimumab + NSAIDs vs Adalimumab monotherapy in AS; Celecoxib used as background NSAID comparator |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Systematic Review | BMB Reports | Celecoxib is the **only NSAID** demonstrated to inhibit radiographic bone progression in SpA; investigates unique COX-2–independent mechanism involving Wnt signalling |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Cohort Study | Scand J Rheumatology | Nationwide retrospective cohort comparing CVD and GIB risk between Celecoxib and nsNSAIDs in AS patients; comparable safety profile confirmed |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Umbrella Review | Drugs | Systematic synthesis of meta-analyses on Celecoxib safety across chronic musculoskeletal conditions |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT Analysis | Ann Rheum Dis | CONSUL trial results: Celecoxib + Golimumab vs Golimumab alone in r-axSpA; 2-year radiographic spinal progression outcomes |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | Comparative RCT | Clin Rheumatology | Imrecoxib vs Celecoxib in axSpA; changes in bone metabolism markers and sacroiliac joint inflammation after treatment |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | Comparative RCT | Med Sci Monitor | Imrecoxib vs Celecoxib in axSpA; DKK-1 levels and imaging scores at weeks 4 and 12 (60 patients) |
| [27603385](https://pubmed.ncbi.nlm.nih.gov/27603385/) | 2016 | Population Study | Medicine | **Taiwan NHI database study:** Celecoxib associated with reduced coronary artery disease risk in AS patients — locally relevant evidence |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | RCT | J Rheumatology | Pivotal RCT confirming Celecoxib is efficacious and well-tolerated in treating signs and symptoms of AS |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Review | Drugs | Comprehensive review confirming EU approval for Celecoxib in OA, RA, and AS; clinical evidence synthesis across all indications |
| [32955700](https://pubmed.ncbi.nlm.nih.gov/32955700/) | 2021 | Clinical Study | Irish J Med Sci | Serum IL-1β, IL-6, and IL-17A as predictive biomarkers for clinical response to Celecoxib in AS patients |

---

## Taiwan Market Information

No approved products are currently registered in Taiwan (0 registrations). Celecoxib is not marketed in Taiwan.

> **Global regulatory context:** Celecoxib (Celebrex®) holds US FDA approval for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, juvenile rheumatoid arthritis (≥2 years), and acute pain. EU (EMA) approval covers OA, RA, and AS in adults. These existing regulatory dossiers provide a substantial foundation for a potential Taiwan NDA submission under the 505(b)(2)–equivalent pathway.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Celecoxib holds FDA and EU approval for ankylosing spondylitis, backed by at least two completed Phase 3 RCTs and a 2025 systematic review establishing a unique disease-modifying property (bone progression inhibition) not demonstrated by any other NSAID. The evidence clearly meets the L1 threshold, and a Taiwan NHI population study (PMID 27603385) provides local cardiovascular safety data. This is primarily a regulatory and market-access question for Taiwan, not a de novo repurposing challenge.

**To proceed, the following is needed:**

- File a Taiwan NDA (新藥查驗登記) referencing the existing FDA/EMA approval packages for the AS/axSpA indication
- Obtain and review the Taiwan package insert (仿單) to fill the current gaps in key warnings, contraindications, and drug interaction data
- Establish a cardiovascular risk monitoring plan consistent with the COX-2 inhibitor drug class safety profile (particularly for patients with pre-existing cardiovascular risk factors)
- Confirm the complete drug interaction profile, especially for anticoagulants, ACE inhibitors, diuretics, and methotrexate
- Assess current off-label prescribing patterns for Celecoxib in Taiwan to quantify unmet clinical demand and guide market sizing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

