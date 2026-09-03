---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 984
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Monoclonal Gammopathy

## One-Sentence Summary

> Ofloxacin is a fluoroquinolone antibiotic used broadly for bacterial infections, though it is not currently marketed in Taiwan.
> The TxGNN model predicts a repurposing opportunity in **Monoclonal Gammopathy** — specifically as prophylactic antibiotic therapy to prevent infection-related mortality in newly diagnosed multiple myeloma —
> supported by **19 publications**, including two completed Phase 3 RCTs, though the RCT evidence is for levofloxacin (a stereoisomer of ofloxacin) rather than ofloxacin itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone antibiotic class); no Taiwan license/indication text on file |
| Predicted New Indication | Monoclonal Gammopathy (infection prophylaxis in newly diagnosed multiple myeloma) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, ofloxacin is a second-generation **fluoroquinolone antibiotic** that inhibits bacterial DNA gyrase and topoisomerase IV, blocking DNA replication in susceptible gram-negative and gram-positive organisms. Its antimicrobial spectrum is essentially the same as that of levofloxacin, its more widely studied levo-isomer.

Multiple myeloma (the malignancy underlying monoclonal gammopathy) causes profound humoral immunodeficiency, and roughly a quarter of newly diagnosed patients experience a serious infection within three months of diagnosis. This is not a case of ofloxacin treating the malignancy itself — rather, the predicted benefit is **antibacterial prophylaxis** during the high-risk induction/transplant period, where fluoroquinolones reduce febrile neutropenia and bloodstream infection episodes.

The key caveat is that the strongest evidence (the TEAMM Phase 3 RCT) was conducted with **levofloxacin**, not ofloxacin. Since both drugs share the same core fluoroquinolone mechanism and overlapping spectrum, a class-effect extrapolation is mechanistically plausible, but it has not been directly validated for ofloxacin in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Supporting RCT evidence exists but is captured under Literature Evidence below — the pivotal TEAMM trial (PMID 31668592 / 31690402) was a registered multicentre Phase 3 RCT, but it was ingested via PubMed rather than as a clinical trial registry record in this evidence pack.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/) | 2019 | RCT | The Lancet Oncology | TEAMM trial: levofloxacin prophylaxis in newly diagnosed myeloma reduced serious infections vs. placebo in a multicentre, double-blind, Phase 3 RCT |
| [31690402](https://pubmed.ncbi.nlm.nih.gov/31690402/) | 2019 | RCT | Health Technology Assessment | Full TEAMM RCT report: prophylactic levofloxacin reduced febrile episodes/death in first 12 weeks post-diagnosis without significant increase in C. difficile infection |
| [37573150](https://pubmed.ncbi.nlm.nih.gov/37573150/) | 2023 | Cohort | Transplant Infectious Disease | Infectious complications after autologous HCT in myeloma patients; evaluated outcomes with/without levofloxacin prophylaxis |
| [32019731](https://pubmed.ncbi.nlm.nih.gov/32019731/) | 2020 | Cohort | Clin Lymphoma Myeloma Leuk | Real-world Asian cohort: bacterial infection rates during bortezomib-based induction without routine fluoroquinolone prophylaxis |
| [26150022](https://pubmed.ncbi.nlm.nih.gov/26150022/) | 2015 | Cohort | Biol Blood Marrow Transplant | Prophylactic levofloxacin reduced bloodstream infection and febrile neutropenia rates in autologous HSCT for myeloma |
| [25212681](https://pubmed.ncbi.nlm.nih.gov/25212681/) | 2014 | Cohort | Int J Hematol | Levofloxacin prophylaxis reduced severe infections in myeloma patients on bortezomib-based regimens |
| [29080369](https://pubmed.ncbi.nlm.nih.gov/29080369/) | 2018 | Cohort | Clinical Transplantation | Retrospective comparison of ciprofloxacin vs. levofloxacin prophylaxis in autologous HSCT for myeloma — similar breakthrough infection rates |
| [32304873](https://pubmed.ncbi.nlm.nih.gov/32304873/) | 2020 | Review | Biol Blood Marrow Transplant | Reviews controversy and evidence base for fluoroquinolone prophylaxis in autologous stem cell transplantation |
| [32172361](https://pubmed.ncbi.nlm.nih.gov/32172361/) | 2020 | Review | Curr Hematol Malig Rep | Supportive care review in multiple myeloma, including infection prevention strategies |
| [15791505](https://pubmed.ncbi.nlm.nih.gov/15791505/) | 2005 | Cohort | Clinical Infectious Diseases | Fluoroquinolone prophylaxis associated with reduced infection-related mortality in neutropenic hematologic malignancy patients |

---

## US Market Information

No Taiwan or US license records are available for ofloxacin in this evidence pack (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TEAMM Phase 3 RCT and multiple supporting cohort studies provide solid L2-level evidence that fluoroquinolone prophylaxis reduces infection-related mortality in newly diagnosed multiple myeloma. However, this evidence was generated with levofloxacin, not ofloxacin directly, so the class-effect assumption needs explicit validation before clinical application.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain TFDA/international package insert warnings and contraindications before any safety sign-off
- Resolve **DG002 (High)**: confirm ofloxacin's detailed MOA and pharmacokinetic comparability to levofloxacin to support class-effect extrapolation
- Direct evidence (even pharmacokinetic/PD bridging data) on ofloxacin specifically in neutropenic/myeloma populations, since current RCT support is for its levo-isomer
- A defined monitoring and antimicrobial stewardship plan given fluoroquinolone-class risks (e.g., C. difficile infection, resistance selection) noted in the supporting literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

