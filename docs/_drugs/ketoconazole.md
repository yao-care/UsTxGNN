---
layout: default
title: Ketoconazole
parent: 僅模型預測 (L5)
nav_order: 825
evidence_level: L5
indication_count: 1
---

# Ketoconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ketoconazole: From Fungal Infections to Acne

## One-Sentence Summary

Ketoconazole (DrugBank DB01026) is a broad-spectrum imidazole antifungal, classically used to treat fungal infections.
The TxGNN model predicts it may be effective for **Acne**, with a prediction score of **99.80%**,
currently supported by **1 clinical trial** and **15 relevant publications**, most of which are preclinical/mechanistic in nature rather than confirmatory clinical trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (no marketed license on record); ketoconazole is classically an antifungal agent |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (mechanism/preclinical evidence + one ongoing, non-randomized trial) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ketoconazole was not available in this evidence pack (data gap). Based on general pharmacological knowledge, ketoconazole is an imidazole antifungal that inhibits fungal cytochrome P450-dependent 14α-demethylase, blocking ergosterol synthesis in the fungal cell membrane. It also has recognized secondary anti-androgenic activity, which has historically been exploited off-label in conditions such as hirsutism and PCOS-related hyperandrogenism.

Acne pathogenesis is multifactorial, involving *Propionibacterium (Cutibacterium) acnes* lipase activity, sebum overproduction driven partly by androgens, and — in some presentations — co-existing *Malassezia* (fungal) folliculitis that clinically mimics acne. This creates two plausible mechanistic bridges from ketoconazole's known pharmacology to acne: an antimicrobial route and an anti-androgenic/anti-sebum route.

Supporting this rationale, literature evidence (PMID 28111792 and PMID 20045949) directly demonstrates that ketoconazole inhibits *P. acnes* lipase activity and possesses in vitro anti-*P. acnes* activity, positioning it as a possible non-antibiotic alternative in an era of rising antibiotic-resistant *P. acnes* strains. This mechanistic plausibility is further reflected by an active clinical trial directly comparing topical ketoconazole to a standard acne therapy (adapalene).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | NA | Active, not recruiting | 52 | Randomized comparison of topical ketoconazole 2% cream vs. topical adapalene 2% cream in mild comedonal and papulopustular acne, assessing whether ketoconazole is a viable alternative to topical retinoids with fewer side effects |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | In vitro study | Microbiology and Immunology | Ketoconazole directly inhibits *P. acnes* lipase activity, a key driver of acne inflammation, suggesting utility as an alternative acne treatment |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biological & Pharmaceutical Bulletin | Azole antifungals, including ketoconazole, show in vitro activity against *P. acnes* isolated from acne vulgaris patients |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | Dermatology (Basel) | Review of systemic acne treatment options, including antibiotic resistance concerns that motivate non-antibiotic alternatives |
| [32872149](https://pubmed.ncbi.nlm.nih.gov/32872149/) | 2020 | Review | Pharmaceuticals (Basel) | Review of adapalene (the active comparator in NCT07237763) as first-line acne therapy |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Case series | Clinical and Experimental Dermatology | *Pityrosporum* (Malassezia) folliculitis frequently misdiagnosed as acne vulgaris, relevant given ketoconazole's antifungal activity against Malassezia |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | The Keio Journal of Medicine | Review of *Pityrosporum ovale* as an opportunistic pathogen in skin conditions including folliculitis often confused with acne |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case report | Archives of Dermatology | Association between neonatal acne-like eruptions and *Malassezia furfur* infection |
| [23600337](https://pubmed.ncbi.nlm.nih.gov/23600337/) | 2013 | Review | FP Essentials | Review of infant skin rashes including neonatal and infantile acne differentials |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Clinical evidence review | BMJ Clinical Evidence | Review of PCOS, noting association with acne and hyperandrogenism |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Review | Polski Tygodnik Lekarski | Review of hyperandrogenic manifestations (including acne) in PCOS treatment |

---

## US Market Information

Ketoconazole currently has no active US marketing authorization on record (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A blocking data gap (DG001) exists — TFDA label warnings/contraindications could not be retrieved, which prevents a full S1 safety pre-assessment. Drug interaction (DDI) data was also queried but not found.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (anti-*P. acnes* and anti-*Malassezia* activity, plus known anti-androgenic effects) is biologically plausible and is being actively tested in one small trial, but current evidence is limited to preclinical/mechanistic literature and a single non-randomized, still-active trial with no completed results. A blocking safety data gap (missing TFDA warnings/contraindications) also prevents initial safety screening.

**To proceed, the following is needed:**
- TFDA product label with warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Completed results from NCT07237763
- Drug-drug interaction (DDI) data, currently not found
- Confirmation of original approved indication(s), which were not present in the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

