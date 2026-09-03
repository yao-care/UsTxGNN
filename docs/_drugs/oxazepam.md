---
layout: default
title: Oxazepam
parent: 僅模型預測 (L5)
nav_order: 1001
evidence_level: L5
indication_count: 1
---

# Oxazepam
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

# Oxazepam: From Anxiety Disorder to Insomnia

## One-Sentence Summary

> Oxazepam is a benzodiazepine anxiolytic/sedative, classically used to manage anxiety and related conditions.
> The TxGNN model predicts it may also be effective for **Insomnia**,
> with **0 registered clinical trials** and **11 supporting publications** (including 2 RCTs) currently available, though the drug is not currently marketed in this jurisdiction and key safety documentation is still missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no license record on file; drug is classically categorized as a benzodiazepine anxiolytic) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is flagged as a data gap in the evidence pack. Based on known pharmacology, however, Oxazepam is a benzodiazepine that acts at the benzodiazepine binding site of the GABA-A receptor, enhancing inhibitory GABAergic neurotransmission. This produces sedative, anxiolytic, and hypnotic effects.

This mechanism is the well-established pharmacological basis for benzodiazepine use in insomnia — it is not a novel repurposing hypothesis but rather an extension of a mechanism already widely applied in clinical practice. The predicted link between an anxiolytic/sedative agent and insomnia is therefore mechanistically coherent rather than speculative.

Supporting literature spans four decades (1983–2024) and includes head-to-head hypnotic comparisons (e.g., oxazepam vs. flurazepam in chronic insomnia), use in elderly populations with comorbid insomnia, and use in special clinical contexts such as alcohol withdrawal-related insomnia and perioperative anxiety/sleep disturbance in STEMI patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | RCT | Am J Psychiatry | Oxazepam improved polysomnographic sleep measures in chronic insomnia without the daytime sleepiness seen with flurazepam |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | RCT | Ann Pharmacother | Compared oxazepam vs. melatonin for anxiety and sleep quality in STEMI patients post-PCI |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Review | Arch Gerontol Geriatr | Effectiveness/safety of hypnotics, including benzodiazepines, for insomnia in patients over 70 |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Review | J Clin Exp Hepatol | Insomnia as an early symptom of alcohol withdrawal syndrome; benzodiazepine management in liver disease |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs, including benzodiazepines used for sleep/anxiety |
| [15633073](https://pubmed.ncbi.nlm.nih.gov/15633073/) | 2005 | Review | Psychiatr Prax | Practice patterns for managing behavioral/sleep symptoms in dementia, including benzodiazepine use |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Review | CNS Drugs | Review of anxiolytic pharmacology relevant to panic/anxiety-related sleep disturbance |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Cohort | PeerJ | Factors associated with long-term benzodiazepine/z-drug use (incl. for insomnia) in older adults |
| [39544757](https://pubmed.ncbi.nlm.nih.gov/39544757/) | 2024 | Case report | Am J Transl Res | Adverse sensory event associated with a sedative/hypnotic-class agent (agomelatine); relevant to comparative hypnotic safety |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Case report | JAMA | Withdrawal syndrome after substituting oxazepam (short-acting) for a long-acting benzodiazepine |

---

## US Market Information

This drug currently has **no license records** on file (`total_licenses: 0`) and market status is listed as **not marketed**. No authorization/product table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the evidence pack flags a **Blocking** data gap — TFDA label warnings/contraindications are not yet available — which must be resolved before any safety-related determination can be finalized.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong (well-established benzodiazepine GABA-A pharmacology) and is supported by decades of published literature including two RCTs, but there are no dedicated clinical trials for this specific repurposing use, and the drug is not currently marketed in this jurisdiction with a **Blocking** data gap on TFDA label warnings/contraindications.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — download and parse the official package insert from the TFDA website
- Formal mechanism of action documentation from DrugBank (DG002, High) to support the mechanistic-link analysis
- Confirmation of local market/licensing status before any regulatory pathway can be pursued
- Dedicated safety review given known benzodiazepine risks (dependence, withdrawal, elderly fall risk) once label data is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

