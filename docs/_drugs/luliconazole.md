---
layout: default
title: Luliconazole
parent: 僅模型預測 (L5)
nav_order: 876
evidence_level: L5
indication_count: 7
---

# Luliconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Luliconazole: From Topical Antifungal Therapy to Pityriasis Versicolor

## One-Sentence Summary

Luliconazole (DrugBank DB08933) is an imidazole-class topical antifungal not currently marketed in Taiwan (0 licenses on record).
The TxGNN model's top-ranked prediction is efficacy against **Pityriasis Versicolor**,
with **1 clinical trial** (not yet recruiting) and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — no Taiwan license history; drug is not yet marketed locally |
| Predicted New Indication | Pityriasis Versicolor |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for luliconazole is not available in the structured drug record (data gap DG002). Based on the literature evidence collected for this candidate, luliconazole is an imidazole antifungal that inhibits fungal sterol 14-α-demethylase (CYP51), blocking ergosterol biosynthesis and disrupting fungal cell membrane integrity. Supporting literature (PMID 29198426) describes broad-spectrum activity against dermatophytes, *Candida albicans*, and *Malassezia* species, and explicitly notes luliconazole "has been clinically used for the treatment of pityriasis versicolor" in other markets.

Pityriasis versicolor is caused by *Malassezia* species. An in vitro susceptibility study of the related imidazole compound NND-502 (luliconazole) against *Malassezia furfur*, *M. sympodialis*, and *M. slooffiae* (PMID 12636984) demonstrated potent inhibitory activity, mechanistically consistent with the TxGNN prediction. This mechanistic alignment, combined with an existing head-to-head comparative RCT of luliconazole vs. ketoconazole in pityriasis versicolor (PMID 27559523, 2016) and a newly registered Phase 4 confirmatory trial (NCT07333170), supports biological plausibility, though the drug currently has no Taiwan market presence to build on.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07333170](https://clinicaltrials.gov/study/NCT07333170) | Phase 4 | Not Yet Recruiting | 86 | Randomized comparison of topical luliconazole 2% cream vs. ketoconazole 1% cream for pityriasis versicolor; aims to test whether luliconazole offers improved efficacy and shorter treatment duration than ketoconazole. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27559523](https://pubmed.ncbi.nlm.nih.gov/27559523/) | 2016 | RCT (open-label) | Indian Dermatology Online Journal | Prospective randomized controlled trial comparing topical ketoconazole and topical luliconazole in pityriasis versicolor at a tertiary care hospital. |
| [29198426](https://pubmed.ncbi.nlm.nih.gov/29198426/) | 2018 | In vitro susceptibility | Journal de Mycologie Médicale | Confirms luliconazole's CYP51-inhibiting, broad-spectrum antifungal activity against dermatophytes, *Candida*, and *Malassezia*, and notes prior clinical use in pityriasis versicolor. |
| [12636984](https://pubmed.ncbi.nlm.nih.gov/12636984/) | 2003 | In vitro | International Journal of Antimicrobial Agents | In vitro activity of NND-502 (luliconazole) against three major *Malassezia* species, the causative organisms of pityriasis versicolor. |

---

## Taiwan Market Information

Currently not marketed in Taiwan — no license records available (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA label warnings/contraindications and DDI data are not currently available (data gap DG001, blocking further safety assessment).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mechanistic plausibility is well supported — luliconazole's CYP51-inhibition activity against *Malassezia* is documented in vitro, and an existing comparative RCT plus a newly registered Phase 4 trial target pityriasis versicolor directly — but the confirmatory Phase 4 trial has not yet started recruiting, and the drug has no current Taiwan market or safety-label presence.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (blocking gap DG001)
- Formal mechanism-of-action documentation from DrugBank (gap DG002)
- Monitoring of NCT07333170 as it moves to recruiting and reports results
- Assessment of the regulatory pathway for Taiwan market entry, since the drug currently holds no local license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

