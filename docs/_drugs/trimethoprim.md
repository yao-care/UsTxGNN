---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 1264
evidence_level: L5
indication_count: 2
---

# Trimethoprim
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

# Trimethoprim: From Systemic Antibacterial Therapy to Bacterial Conjunctivitis

## One-Sentence Summary

> Trimethoprim is a DHFR-inhibiting antibacterial agent conventionally used for systemic and topical bacterial infections.
> The TxGNN model's #2-ranked prediction identifies **Conjunctivitis** as a target indication,
> supported by **3 clinical trials** (including one direct head-to-head RCT) and **20 publications**.
> Note: TxGNN's #1-ranked prediction — punctate epithelial keratoconjunctivitis (score 99.57%) — currently has **zero supporting evidence** (L5/Hold) and a mechanistically weak rationale (the condition is largely viral/immune-mediated, not bacterial), so it is not the focus of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (0 US licenses; product currently "未上市"/Not Marketed in this registry) |
| Predicted New Indication | Conjunctivitis (bacterial) |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug registry (flagged as a High-severity data gap). Based on the repurposing rationale accompanying this evidence pack, Trimethoprim inhibits bacterial dihydrofolate reductase (DHFR), blocking the folate synthesis pathway required for bacterial DNA synthesis. This antibacterial mechanism has well-established efficacy against Gram-positive and Gram-negative pathogens.

Bacterial conjunctivitis is caused by common ocular pathogens (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Staphylococcus aureus*) that are susceptible to trimethoprim's antifolate mechanism. This is not a purely computational hypothesis: trimethoprim combined with polymyxin B (marketed as Polytrim) is already an FDA-approved, clinically established topical treatment for bacterial conjunctivitis in the US, which strongly corroborates the TxGNN prediction with real-world precedent.

By contrast, the model's top-ranked candidate (punctate epithelial keratoconjunctivitis) lacks this mechanistic coherence — that condition is predominantly viral (e.g., adenoviral) or immune-mediated, so an antibacterial agent's applicability is speculative and currently unsupported by any trial or literature evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4 | Completed | 124 | Single-blind RCT directly comparing Polytrim (trimethoprim/polymyxin B) ophthalmic solution vs. moxifloxacin for treating pediatric conjunctivitis; direct efficacy comparison (Grade A relevance). |
| [NCT03187834](https://clinicaltrials.gov/study/NCT03187834) | Phase 4 | Completed | 252 | Population-level study of antibiotic resistance and microbiome changes in children after short-course antibiotic use; indirect safety/resistance evidence (Grade B). |
| [NCT00168532](https://clinicaltrials.gov/study/NCT00168532) | Phase 3 | Completed | 218 | Community-based double-blind placebo-controlled RCT of prophylactic antibiotics in measles (conjunctivitis is a common measles complication, but not the primary endpoint) (Grade B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | Multicenter comparison of polymyxin B/trimethoprim vs. 0.5% moxifloxacin on speed of clinical efficacy in bacterial conjunctivitis. |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | RCT | Am J Ophthalmol | Clinical evaluation of trimethoprim-containing ophthalmic solutions (with sulfacetamide or polymyxin B) in bacterial conjunctivitis/blepharitis. |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Review (systematic review/meta-analysis) | J Pediatr Infect Dis Soc | Systematic review of antibiotic treatments, including trimethoprim, for neonatal chlamydial conjunctivitis. |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Cohort | Clin Ther | Survey of children with acute bacterial conjunctivitis treated with trimethoprim-polymyxin B ophthalmic solution. |
| [21988450](https://pubmed.ncbi.nlm.nih.gov/21988450/) | 2011 | Clinical study | Curr Eye Res | Analysis of nontypeable *Streptococcus pneumoniae* in sporadic bacterial conjunctivitis cases (context for antibacterial targeting). |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Review | J Pediatr Ophthalmol Strabismus | Guidance on controlling contagious bacterial conjunctivitis outbreaks with antimicrobial therapy. |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Review | Paediatr Child Health | Review of etiology, clinical features, and management of acute infectious conjunctivitis in children. |
| [34943657](https://pubmed.ncbi.nlm.nih.gov/34943657/) | 2021 | Clinical study | Antibiotics (Basel) | Clinical/molecular characteristics of MSSA ocular infections in Taiwan, relevant to bacterial ocular pathogen susceptibility. |

---

## US Market Information

Currently not marketed under this registry — 0 NDA licenses on file (`market_status: 未上市 / Not Marketed`). No product/authorization data available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack; TFDA/FDA label review is a Blocking data gap for safety screening.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The conjunctivitis indication is backed by L1-level evidence, including a Grade A completed Phase 4 RCT (NCT00581542) directly comparing trimethoprim/polymyxin B to moxifloxacin, plus an existing FDA-approved precedent (Polytrim). This is a mechanistically coherent, clinically corroborated repurposing candidate — not a speculative model output.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal drug interaction (DDI) data — currently `not_found`
- Confirmation of route compatibility (ophthalmic formulation availability/status is marked "pending")
- Deprioritize or separately re-evaluate the higher-scored but evidence-free candidate (punctate epithelial keratoconjunctivitis, L5/Hold) before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

