---
layout: default
title: Miconazole
parent: 僅模型預測 (L5)
nav_order: 925
evidence_level: L5
indication_count: 1
---

# Miconazole
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

# Miconazole: From Fungal Infections to Acne

## One-Sentence Summary

Miconazole is an antifungal agent of the imidazole class, originally used to treat fungal infections. The TxGNN model predicts it may be effective for **Acne**, but this direction is currently supported by only **1 clinical trial (indirect relevance)** and **4 publications**, none of which are direct RCTs of miconazole in acne patients.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (imidazole/azole antifungal class) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, miconazole is part of the imidazole/azole antifungal class; its efficacy in fungal skin infections has been established, and mechanistically it may be applicable to acne.

Miconazole inhibits lanosterol 14-α-demethylase, a mechanism traditionally associated with antifungal activity but that also confers direct antibacterial activity. In vitro data (PMID 20045949) show azole antifungal agents, including miconazole, are active against *Propionibacterium (Cutibacterium) acnes*, the bacterium implicated in acne pathogenesis. This suggests a plausible dual mechanism: (1) reduction of *P. acnes* burden through direct antibacterial action, and (2) treatment of *Malassezia (Pityrosporum)* folliculitis, a condition frequently misdiagnosed as acne vulgaris and for which miconazole has established antifungal efficacy (PMID 8593718).

This mechanistic rationale is biologically plausible but remains preclinical/in vitro in nature — no direct clinical evidence yet confirms miconazole's efficacy against acne vulgaris itself, as distinct from its efficacy against *Malassezia* folliculitis (a clinical mimic of acne).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Evaluated a combination cream (beclomethasone + gentamicin + **clotrimazole**, not miconazole) in patients with contaminated dermatosis/acne-like lesions. Relevance graded **C**: the tested drug is clotrimazole (a different azole), the trial was suspended, and enrollment figures are inconsistent with registry data — only indirectly supports the azole-class mechanistic rationale, not miconazole specifically. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Controlled clinical trial (split-face, n=35) | Skin Research and Technology | Assessed catamenial acne management; notes oral contraceptives may help without fully clearing skin lesions (does not directly test miconazole). |
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opinion on Pharmacotherapy | Reviews the multifaceted effects of miconazole nitrate, a "time-honored" imidazole antifungal, on various skin disorders. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Case series / therapeutic trial | Clinical and Experimental Dermatology | 62 patients with *Pityrosporum* folliculitis — frequently misdiagnosed as acne vulgaris — evaluated and treated; supports miconazole's role in an acne-mimicking condition. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro study | Biological & Pharmaceutical Bulletin | Azole antifungal agents, including miconazole, tested in vitro against *P. acnes* isolates from acne vulgaris patients, showing anti-bacterial activity. |

## US Market Information

Miconazole is currently **not marketed** under any NDA in the available Taiwan/US regulatory data (0 licenses on record). No product or dosage form information is available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (in vitro anti-*P. acnes* activity and treatment of the acne-mimicking *Malassezia* folliculitis) is plausible, but no direct clinical trial or RCT has tested miconazole in acne vulgaris — the only registered trial actually studied a different drug (clotrimazole) and was suspended. Combined with a blocking data gap on TFDA safety information and the drug's current unmarketed status, evidence is insufficient to proceed.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap, required for S1 safety screening)
- Confirmed mechanism of action data from DrugBank
- A direct clinical trial of miconazole (not a related azole) in acne vulgaris patients
- Clarification of whether the target indication is acne vulgaris specifically or *Malassezia* folliculitis (often conflated in the literature)
- Topical formulation/route data if pursuing dermatologic development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

