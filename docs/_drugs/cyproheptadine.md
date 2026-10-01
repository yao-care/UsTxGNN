---
layout: default
title: Cyproheptadine
parent: Model Prediction Only (L5)
nav_order: 559
evidence_level: L5
indication_count: 4
---

# Cyproheptadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Cyproheptadine: From First-Generation Antihistamine to Allergic Urticaria

## One-Sentence Summary

Cyproheptadine is a first-generation H1-antihistamine with serotonin-blocking activity, marketed in the US as generic tablets. The TxGNN model predicts it may be effective for **allergic urticaria**. This rests on the shared H1-blockade mechanism, with **0 clinical trials** and **0 publications** that directly study cyproheptadine in allergic urticaria; the supplied evidence covers other antihistamines.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (indirect class evidence only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations (generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on known information, cyproheptadine is a first-generation H1-receptor antagonist that also blocks serotonin. Histamine released from mast cells drives the wheals and itch of urticaria, and H1 blockade is the standard way to control them. The mechanistic link is therefore a class effect.

The record lists no original indications for cyproheptadine, which may be why a plausible on-label use appears as a "prediction". Most of the supplied literature is about other antihistamines: loratadine, desloratadine, rupatadine, bilastine and acrivastine. These support the antihistamine class in urticaria but say nothing directly about cyproheptadine.

A related signal appears for **cold urticaria**, the model's second-ranked prediction. Older comparative studies there include cyproheptadine directly, such as PMID 334082, PMID 6480953 and PMID 7488341. That subtype is a better-supported lead than allergic urticaria in general.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00762983](https://clinicaltrials.gov/study/NCT00762983) | N/A (observational) | Completed | 1003 | Post-marketing safety survey of loratadine in children. Cyproheptadine not studied. |
| [NCT07101445](https://clinicaltrials.gov/study/NCT07101445) | Phase 4 | Recruiting | 94 | Compares premedication with methylprednisolone vs dexamethasone to prevent allergic reactions to motixafortide in multiple myeloma. Different drug and setting. |

Neither trial studies cyproheptadine, and both were graded low relevance (C).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Double-blind crossover study | Asian Pac J Allergy Immunol | Cyproheptadine vs ketotifen in 6 Thai children with cold urticaria. The only item here that studies cyproheptadine, and in a related subtype. |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review (by title) | Clin Exp Allergy | How to choose the best H1-antihistamine for urticaria, especially chronic spontaneous urticaria. |
| [18339040](https://pubmed.ncbi.nlm.nih.gov/18339040/) | 2008 | Review | Allergy | Rupatadine in allergic rhinitis and chronic urticaria. Histamine is the primary mediator, so H1 antagonists are central. |
| [21162645](https://pubmed.ncbi.nlm.nih.gov/21162645/) | 2011 | Review | Expert Rev Clin Immunol | Rupatadine for allergic rhinitis and urticaria. Antihistamines differ in effect and safety profile. |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine, a second-generation antihistamine, for allergic rhinitis and urticaria. |
| [35396016](https://pubmed.ncbi.nlm.nih.gov/35396016/) | 2022 | Review | Profiles Drug Subst Excip Relat Methodol | Loratadine profile. Widely used for allergic diseases including chronic urticaria. |
| [20067329](https://pubmed.ncbi.nlm.nih.gov/20067329/) | 2010 | Post-marketing surveillance | Clin Drug Investig | Desloratadine safety and efficacy in seasonal allergic rhinitis or chronic urticaria (four surveillance studies). |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Pharmacokinetics and pharmacodynamics of desloratadine, fexofenadine and levocetirizine. Second-generation agents were developed to reduce adverse effects of first-generation ones. |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine. Double-blind trials show efficacy in chronic urticaria. |

Apart from PMID 7488341, none of these publications studies cyproheptadine. They support the antihistamine class only.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212491 | Cyproheptadine Hydrochloride (Bryant Ranch Prepack) | Tablet | Not listed |
| ANDA212491 | Cyproheptadine Hydrochloride (Quagen Pharmaceuticals) | Tablet | Not listed |
| ANDA212491 | Cyproheptadine Hydrochloride (RemedyRepack) | Tablet | Not listed |
| ANDA212491 | Cyproheptadine Hydrochloride (Bryant Ranch Prepack) | Tablet | Not listed |
| ANDA206553 | Cyproheptadine Hydrochloride (TruPharma) | Tablet | Not listed |

Other forms in the record include syrup and solution.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were retrieved.

The prediction notes suggest watching for sedation and anticholinergic effects, especially in children and older adults. These are known concerns with first-generation antihistamines, and are why second-generation agents are generally preferred today.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is supported only by the class-level H1-blockade mechanism. No supplied trial or publication studies cyproheptadine in allergic urticaria, and the package insert safety data is missing. Second-generation antihistamines are the usual first choice for urticaria.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, to complete safety screening
- Mechanism of action data for cyproheptadine
- Full-text review of the older cyproheptadine studies in cold urticaria (PMID 334082, 6480953, 7488341), which may be a more promising direction
- A comparison of cyproheptadine against second-generation antihistamines in urticaria, including the sedation and anticholinergic trade-off
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

