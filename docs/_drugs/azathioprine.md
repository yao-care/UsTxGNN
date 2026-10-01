---
layout: default
title: Azathioprine
parent: High Evidence (L1-L2)
nav_order: 434
evidence_level: L1
indication_count: 10
---

# Azathioprine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Azathioprine: From Immunosuppression to Inflammatory Bowel Disease

> **Note on indication selection:** The top-ranked prediction (rank 1) is *colobomatous microphthalmia-rhizomelic dysplasia syndrome*. It has no trials or literature, and no plausible mechanism. This report therefore focuses on **inflammatory bowel disease (IBD, rank 5)**, the highest-ranked prediction with real evidence. Ulcerative colitis (rank 9) is covered within it.

## One-Sentence Summary

Azathioprine is an oral thiopurine immunosuppressant with 20 US generic licenses. The pack does not record its original indication.
The TxGNN model predicts it may be effective for **inflammatory bowel disease**.
**50 clinical trials** and **20 publications** are retrieved, including at least two completed Phase 3 trials with an azathioprine arm and several Cochrane reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (`original_indications` and license indication text are empty in the record) |
| Predicted New Indication | Inflammatory bowel disease (UC and Crohn's disease) |
| TxGNN Prediction Score | 99.52% (UC: 99.33%) |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of Licenses | 20 (the 5 listed below are all ANDA generics, no NDA) |
| Recommended Decision | Proceed with Guardrails (IBD/UC); Hold for all other predictions |

## Why is This Prediction Reasonable?

DrugBank mechanism-of-action data is not in the record. The mechanism below comes from the pack's rationale. Azathioprine is a prodrug of 6-mercaptopurine. Its thioguanine nucleotide metabolites inhibit purine synthesis and induce T-cell apoptosis via Rac1 blockade. This dampens the mucosal immune activation that drives IBD, and it is why the drug is used for steroid-sparing maintenance of remission.

IBD is driven by chronic immune-mediated mucosal inflammation, so a lymphocyte-suppressing antimetabolite fits the biology. The literature describes decades of clinical use, and the retrieved trials use azathioprine as a standard comparator arm. The L1 rating for UC rests on pooled randomized evidence in the literature (Cochrane reviews and a meta-analysis). None of the retrieved records is a UC-specific Phase 3 azathioprine trial.

The other predictions are not supported:
- **Ranks 1, 2, 10** (skeletal and developmental syndromes): no immune mechanism, likely graph artifacts.
- **Rank 3** (osteoarthritis susceptibility): a genetic label, not a treatable clinical entity.
- **Rank 7** (osteoarthritis): only indirect evidence from RA and lupus, and toxicity likely outweighs benefit.
- **Ranks 4, 6, 8** (WHIM syndrome, chronic granulomatous disease variants): immunodeficiencies where further immunosuppression could worsen infection or leukopenia.

## Clinical Trial Evidence

50 IBD-related trials were retrieved. The 10 most relevant are listed.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | Double-blind RCT of infliximab vs infliximab + azathioprine vs azathioprine in immunomodulator- and biologic-naive Crohn's disease |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | Completed | 78 | Azathioprine vs mesalazine to prevent relapse in postoperative Crohn's disease with endoscopic recurrence |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminated | 242 | Infliximab alone or with azathioprine vs azathioprine alone in moderate-to-severe active UC |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Unknown | 84 | Low-dose azathioprine + allopurinol vs azathioprine alone in UC |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | Completed | 65 | Early infliximab + azathioprine vs steroids + azathioprine in acute severe UC |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | Completed | 192 | Methotrexate vs azathioprine/6-MP (low risk) or adalimumab (high risk) for remission in paediatric Crohn's disease |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | Completed | 211 | Infliximab-antimetabolite combination vs antimetabolite alone vs infliximab alone in Crohn's patients in steroid-free remission |
| [NCT00113503](https://clinicaltrials.gov/study/NCT00113503) | Phase 2 | Terminated | 50 | Weight-based vs metabolite-guided (6-TGN) azathioprine dosing in Crohn's disease |
| [NCT00984568](https://clinicaltrials.gov/study/NCT00984568) | Phase 3 | Terminated | 28 | Conventional step-up (prednisolone + 5-ASA or azathioprine) vs early infliximab in UC. Small (n=28), weak evidence |
| [NCT07248644](https://clinicaltrials.gov/study/NCT07248644) | Phase 4 | Not yet recruiting | 304 | Switching to mesalazine vs continuing thiopurines in older UC patients in sustained remission |

Several other retrieved trials are outside efficacy: TPMT genotyping (NCT00521950, n=853), vaccine response, and trials of other drugs where azathioprine is only background therapy.

## Literature Evidence

20 publications were retrieved. The 10 most relevant are listed, with randomized and pooled evidence first. Cochrane abstracts in the pack show only the background, not the pooled results.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: top-down infliximab + azathioprine vs azathioprine alone in acute severe UC responsive to IV steroids |
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane systematic review | Cochrane Database Syst Rev | Update of the review of azathioprine/6-MP for maintenance of remission in UC |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane systematic review | Cochrane Database Syst Rev | Earlier version of the same UC maintenance review (also 2012: [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/)) |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | Tests whether thiopurines are as effective in UC as in Crohn's disease |
| [40538240](https://pubmed.ncbi.nlm.nih.gov/40538240/) | 2025 | Not classified in pack | Aliment Pharmacol Ther | Azathioprine or tofacitinib as maintenance in corticosteroid-responsive acute severe UC |
| [24117596](https://pubmed.ncbi.nlm.nih.gov/24117596/) | 2013 | Observational study + meta-analysis | Aliment Pharmacol Ther | Trial of mercaptopurine is a safe strategy in IBD patients intolerant to azathioprine |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohns Colitis | Expert overview of thiopurines, mainly used to maintain steroid-free remission in IBD |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol Hepatol | Reports strong trial and meta-analysis data on thiopurine efficacy in IBD, with molecular mechanism insights |
| [39921705](https://pubmed.ncbi.nlm.nih.gov/39921705/) | 2025 | Retrospective cohort | Expert Rev Clin Pharmacol | Effectiveness and safety of thiopurines in IBD patients with NUDT15 polymorphism (leukopenia risk) |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Translational/mechanistic | Cell Rep Med | *Blautia wexlerae* in the gut linked to azathioprine failure by lowering 6-MP bioavailability |

## US Market Information

5 of 20 licenses are shown. All are oral tablets. The record contains no approved-indication text, so the manufacturer is shown instead.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA077621 | Azathioprine | Tablet | NuCare Pharmaceuticals, Inc. |
| ANDA074069 | Azathioprine | Tablet | Amneal Pharmaceuticals NY LLC |
| ANDA074069 | Azathioprine | Tablet | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA077621 | Azathioprine | Tablet | Zydus Lifesciences Limited |
| ANDA208687 | Azathioprine | Tablet | Ascend Laboratories, LLC |

## Safety Considerations

Package insert warnings, contraindications and DDI data are not available in the record. Please refer to the package insert for safety information.

The pack's rationale and the retrieved literature point to these guardrails:
- **TPMT/NUDT15:** test genotype or activity before starting. Polymorphisms predispose to leukopenia.
- **Monitoring:** blood counts, liver enzymes and metabolite levels (6-TGN/6-MMP).
- **Infection and lymphoma risk:** weigh these, especially in combination with biologics.
- **Immunodeficiency states:** WHIM syndrome and chronic granulomatous disease carry an unfavorable safety direction.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (IBD/UC). **Hold** for the other nine predictions, including rank 1.

**Rationale:**
IBD has the strongest support: at least two completed Phase 3 trials with an azathioprine arm, Cochrane reviews and a meta-analysis for UC, and a 2025 RCT. This supports L1. No UC-specific Phase 3 azathioprine trial was retrieved, so that L1 rating rests on the pooled literature.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap DG001), which are required before safety screening.
- DrugBank mechanism-of-action data (DG002).
- Confirmation of the US labeled indications for azathioprine, since the record has no indication text. Whether IBD is labeled or off-label should be checked against the label.
- A TPMT/NUDT15 testing and blood-count/liver monitoring plan.
- Route compatibility and similarity-to-original assessment (both still pending in the record).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

