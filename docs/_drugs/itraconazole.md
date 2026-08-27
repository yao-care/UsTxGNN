---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 819
evidence_level: L5
indication_count: 1
---

# Itraconazole
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

# Itraconazole: From Fungal Infection Treatment to Pneumocystosis

## One-Sentence Summary

Itraconazole is a triazole antifungal agent; detailed original indication and mechanism-of-action data are not yet available in this evidence pack (Taiwan market records show no approved licenses). The TxGNN model predicts it may be effective for **Pneumocystosis**, with **no registered clinical trials** but **20 supporting publications**, including one randomized controlled trial of itraconazole prophylaxis in immunocompromised patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan regulatory license on record (drug not marketed; `original_indications` field empty in this evidence pack) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L2 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for itraconazole is not available in this evidence pack. Based on generally established pharmacology, itraconazole is a **triazole antifungal** agent that inhibits fungal cytochrome P450-dependent 14-α-demethylase, blocking ergosterol synthesis in the fungal cell membrane. Its established clinical use is the treatment and prophylaxis of systemic and opportunistic fungal infections.

*Pneumocystis jirovecii* (the causative organism of pneumocystosis) was historically classified as a protozoan but is now recognized taxonomically as a fungus, sharing structural and metabolic features — including membrane sterol pathways — with other fungal pathogens. This taxonomic and mechanistic proximity provides a plausible rationale for the TxGNN model's prediction linking itraconazole, a broad-spectrum antifungal, to pneumocystosis, particularly in the context of prophylaxis for immunocompromised patients (HIV, transplant recipients) where itraconazole is already used against overlapping opportunistic fungal pathogens.

Because original indication data was not captured for this drug in the current evidence pack, a direct comparison between the original and predicted indications cannot be made; the mechanistic link above is inferred from itraconazole's well-established antifungal drug class rather than from the pack's own MOA field.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Randomized, double-blind, placebo-controlled trial of itraconazole capsules for prevention of deep fungal infections in HIV-infected, immunodeficient patients |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Evidence summary of primary/secondary prophylaxis for opportunistic infections (up to 40% of HIV patients with CD4 <250) in the pre-HAART/HAART era |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Summarizes therapy and prophylaxis for systemic protozoan/opportunistic infections including *Pneumocystis carinii*, covering agent MOA, dosing, and toxicity |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Reviews prophylaxis/treatment strategies for infections, including fungal, in bone marrow transplant recipients |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Reviews infection (including fungal/PCP) as major cause of morbidity/mortality after lung transplantation |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Reviews pulmonary epithelial lining fluid penetration of antifungal agents including itraconazole, relevant to pulmonary fungal infection treatment |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Observational | Transplantation Proceedings | Single-center experience on invasive fungal infections after kidney transplantation, associated with increased mortality/graft dysfunction |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Observational | Indian Journal of Medical Microbiology | Compares respiratory fungal pathogen profile and susceptibility in immunocompetent vs immunocompromised hosts, correlated with CD4+ counts |
| [17594870](https://pubmed.ncbi.nlm.nih.gov/17594870/) | 2007 | Observational | Allergologia et Immunopathologia | 25-year experience of chronic granulomatous disease in pediatric patients, a population susceptible to fungal disease |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case Report | Frontiers in Immunology | Case of *Talaromyces marneffei* and *Pneumocystis jirovecii* coinfection in a child with STAT1 mutation |

---

## Taiwan Market Information

No licenses currently on record — 0 approved NDAs. This drug is marked as "未上市" (not marketed) in the Taiwan regulatory dataset, and `taiwan_regulatory.licenses` contains no entries to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI query all returned no data in this evidence pack — TFDA label data is flagged as a **Blocking** gap, DG001, preventing preliminary safety screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TFDA warnings/contraindications gap is flagged as Blocking (cannot proceed to S1 safety pre-screening), and the drug currently has zero Taiwan market authorizations. While literature evidence includes one relevant RCT and consistent supportive case/observational data on itraconazole's antifungal prophylactic use in immunocompromised populations, no dedicated clinical trials for pneumocystosis specifically are registered, so evidence remains preliminary.

**To proceed, the following is needed:**
- TFDA label (warnings, contraindications) — resolve DG001 via TFDA PDF label parsing
- Confirmed mechanism of action and original approved indication(s) — resolve DG002 via DrugBank API
- Drug-drug interaction (DDI) data (current query status: not found)
- Dedicated clinical trial data for itraconazole in pneumocystosis (currently none registered on ClinicalTrials.gov or ICTRP)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

