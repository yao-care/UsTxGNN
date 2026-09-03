---
layout: default
title: Suvorexant
parent: 僅模型預測 (L5)
nav_order: 1190
evidence_level: L5
indication_count: 1
---

# Suvorexant
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

# Suvorexant: From Undetermined Original Indication to Insomnia (Sleep Initiation and Maintenance Disorder)

## One-Sentence Summary

> The evidence pack does not specify Suvorexant's original approved indication or mechanism of action (both flagged as data gaps).
> The TxGNN model predicts it may be effective for **Insomnia (Sleep Disorder, Initiating and Maintaining Sleep)**,
> with **1 clinical trial** (withdrawn) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack |
| Predicted New Indication | Insomnia (Sleep Disorder, Initiating and Maintaining Sleep) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Suvorexant is not available in the evidence pack. However, the supporting literature consistently identifies Suvorexant as a **dual orexin receptor antagonist (DORA)**, blocking OX1R/OX2R signaling to suppress the wake-promoting orexin system and thereby facilitate sleep onset and maintenance (see Muehlan et al. 2023; Wu et al. 2022; Żełabowski et al. 2025).

The predicted indication — sleep disorder, initiating and maintaining sleep — aligns directly with this orexin-antagonist mechanism, and the literature evidence includes what appears to be the original pivotal Phase 3 program for Suvorexant in insomnia (Herring et al. 2016, "Results From Two 3-Month Randomized Controlled Clinical Trials"). This, combined with over a dozen subsequent systematic reviews and network meta-analyses comparing Suvorexant against other DORAs (lemborexant, daridorexant) and standard hypnotics, indicates the mechanism-indication link is well established in the published literature, even though structured MOA and original-indication fields were not populated in this evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03764683](https://clinicaltrials.gov/study/NCT03764683) | Phase 4 | Withdrawn | 0 | Planned double-blind study of Suvorexant (Belsomra) added to usual treatment for insomnia in bipolar depression; trial was withdrawn with zero enrollment, so no efficacy/safety data were generated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25526970](https://pubmed.ncbi.nlm.nih.gov/25526970/) | 2016 | RCT | Biological Psychiatry | Reports results from two pivotal 3-month Phase 3 RCTs establishing Suvorexant's efficacy as an orexin receptor antagonist for insomnia. |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | Systematic Review/NMA | Translational Psychiatry | Network meta-analysis comparing efficacy/safety of daridorexant, lemborexant, and suvorexant for insomnia. |
| [36947394](https://pubmed.ncbi.nlm.nih.gov/36947394/) | 2023 | Systematic Review/NMA | Drugs | Large-scale NMA of 153 RCTs comparing effectiveness, safety, and tolerability of insomnia drugs including suvorexant. |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic Review/NMA | The Lancet | Comparative effectiveness of pharmacological interventions, including suvorexant, for acute and long-term insomnia management. |
| [39277609](https://pubmed.ncbi.nlm.nih.gov/39277609/) | 2024 | Systematic Review | Translational Psychiatry | Reviews evidence for lemborexant and suvorexant as treatments for insomnia comorbid with psychiatric disorders (depression, bipolar disorder). |
| [37257468](https://pubmed.ncbi.nlm.nih.gov/37257468/) | 2023 | Systematic Review/NMA | Arquivos de Neuro-Psiquiatria | Confirms efficacy of dual orexin receptor antagonists, including suvorexant, for chronic insomnia via RCT-based network meta-analysis. |
| [32531478](https://pubmed.ncbi.nlm.nih.gov/32531478/) | 2020 | Systematic Review/NMA | Journal of Psychiatric Research | NMA of 4 double-blind RCTs (n=3237) comparing lemborexant vs suvorexant efficacy and safety outcomes. |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Systematic Review/NMA | J Managed Care & Specialty Pharmacy | Compares efficacy/safety of lemborexant and suvorexant against other insomnia treatments via NMA. |
| [38460107](https://pubmed.ncbi.nlm.nih.gov/38460107/) | 2024 | Open-label Clinical Study | Advances in Therapy | Multicenter study evaluating transition from suvorexant (and other agents) to lemborexant in Japanese insomnia patients. |
| [37086045](https://pubmed.ncbi.nlm.nih.gov/37086045/) | 2023 | Review | Journal of Sleep Research | Reviews orexin biology and orexin receptor antagonists, including suvorexant, in insomnia treatment. |

---

## US Market Information

Suvorexant is currently **not marketed** in this jurisdiction — the evidence pack contains no license or NDA records (0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug interaction data were available in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for the predicted indication is strong (L1 — established Phase 3 RCT evidence plus extensive corroborating systematic reviews/network meta-analyses), but a **Blocking** data gap exists: TFDA-equivalent label warnings and contraindications are entirely unavailable, which prevents completion of the S1 safety pre-assessment. The drug also has zero existing domestic marketing authorizations.

**To proceed, the following is needed:**
- Official package insert / label data (warnings, contraindications, DDI) — download and parse from the relevant regulatory agency (resolves DG001, Blocking)
- Confirmed mechanism of action via DrugBank API query (resolves DG002)
- Clarification of Suvorexant's originally approved indication(s), whether domestic or reference-market
- Regulatory pathway assessment given current zero-license market status before any repurposing submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

