---
layout: default
title: Lemborexant
parent: 僅模型預測 (L5)
nav_order: 843
evidence_level: L5
indication_count: 1
---

# Lemborexant
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

# Lemborexant: From an Unrecorded Original Indication to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

> Lemborexant (DrugBank DB11951) has no recorded original approved indication or marketing license in this dataset, and its mechanism of action is not formally documented here.
> The TxGNN model's top prediction is **Sleep Disorder, Initiating and Maintaining Sleep** (insomnia),
> a direction already backed by **1 registered clinical trial** and **20 publications**, several of which are completed Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license records or original indication data in this dataset |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs identified in literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a formal mechanism-of-action record is not available for this candidate in the dataset. However, the collected literature evidence consistently and independently describes lemborexant as a **dual orexin receptor antagonist (DORA)**, acting on OX1R and OX2R to suppress wake-promoting neurotransmission and facilitate sleep onset and maintenance (e.g., PMID 35972717 "Orexin Receptor Antagonists and Insomnia"; PMID 37086045 "The orexin story and orexin receptor antagonists for the treatment of insomnia"; PMID 32096020 "Lemborexant: First Approval").

Because this mechanism is inherently sleep-promoting, the TxGNN-predicted indication — Sleep Disorder, Initiating and Maintaining Sleep (i.e., insomnia) — is directly consistent with the pharmacology reported in the literature evidence, rather than representing a distant or unexpected repurposing target.

It is worth noting that this appears less like a novel "repurposing" signal and more like the model correctly recovering the drug's core, well-established pharmacological use from the knowledge graph — multiple completed Phase 3 RCTs (e.g., the SUNRISE-2 trial) already directly evaluate lemborexant for this exact indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06928766](https://clinicaltrials.gov/study/NCT06928766) | Phase 2 | Not Yet Recruiting | 15 | Double-blind, placebo-controlled RCT of eszopiclone vs. lemborexant in obstructive sleep apnoea (OSA) patients with a low arousal threshold who have difficulty maintaining or falling asleep (COMISA population) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Network Open | Lemborexant vs. placebo and zolpidem ER in older adults with insomnia disorder |
| [33636648](https://pubmed.ncbi.nlm.nih.gov/33636648/) | 2021 | RCT (Phase 3, SUNRISE-2) | Sleep Medicine | Long-term (12-month) effectiveness and safety of lemborexant in adults with insomnia disorder |
| [32585700](https://pubmed.ncbi.nlm.nih.gov/32585700/) | 2020 | RCT (Phase 3, SUNRISE-2) | Sleep | Long-term efficacy and tolerability of lemborexant vs. placebo in insomnia disorder |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | Post-hoc RCT analysis | Sleep Medicine | Effect of lemborexant on sleep architecture in patients with insomnia and mild OSA (COMISA) |
| [39120786](https://pubmed.ncbi.nlm.nih.gov/39120786/) | 2024 | Pooled trial analysis | Drugs & Aging | Efficacy and safety of lemborexant in older adults across three clinical trials |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network meta-analysis | J Managed Care Spec Pharm | Comparative efficacy of lemborexant vs. other insomnia treatments |
| [36701954](https://pubmed.ncbi.nlm.nih.gov/36701954/) | 2023 | Systematic review / NMA | Sleep Medicine Reviews | Efficacy and tolerability ranking of pharmacological insomnia treatments (20 drugs) |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic review / NMA | Lancet | Comparative effectiveness of pharmacological interventions for insomnia disorder |
| [32096020](https://pubmed.ncbi.nlm.nih.gov/32096020/) | 2020 | Review | Drugs | Lemborexant (DAYVIGO) first approval profile — mechanism, development, indication |
| [35972717](https://pubmed.ncbi.nlm.nih.gov/35972717/) | 2022 | Review | Current Psychiatry Reports | Review of orexin receptor antagonists, including lemborexant, for insomnia |

---

## US Market Information

Currently no marketed authorization records are available — 0 NDAs on file and market status is recorded as Not Marketed in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this dataset (DDI query returned no results). This also constitutes a **Blocking**-severity data gap (TFDA label warnings/contraindications), which prevents a formal S1 safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Literature evidence strongly and consistently supports lemborexant's efficacy for this exact indication (multiple completed Phase 3 RCTs), but a Blocking data gap on label warnings/contraindications means initial safety screening (S1) cannot be completed, and the drug currently has no marketing license on record.

**To proceed, the following is needed:**
- TFDA/FDA package insert (warnings, precautions, contraindications) — remediation source already identified (TFDA official site, PDF parsing)
- Confirmed drug-drug interaction (DDI) data
- Formal mechanism-of-action record via DrugBank API
- Clarification of current marketing/licensing status in the target jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

