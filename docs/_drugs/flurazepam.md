---
layout: default
title: Flurazepam
parent: 僅模型預測 (L5)
nav_order: 727
evidence_level: L5
indication_count: 1
---

# Flurazepam
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

# Flurazepam: From Insomnia to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Flurazepam is a first-generation benzodiazepine hypnotic; the literature evidence in this pack itself documents it as the original benzodiazepine developed for **insomnia (sleep induction and maintenance)**, dating to 1970. The TxGNN model predicts efficacy for **Sleep Disorder, Initiating and Maintaining Sleep**, essentially re-identifying this drug's own long-established use rather than a novel indication, supported by **0 registered clinical trials** and **20 publications** (mostly reviews and older comparative studies).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia (sleep induction and maintenance) — documented in the pack's own literature evidence (e.g. PMID 3332464, 1319429); no formal regulatory license record is present in this evidence pack |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (marked as a High-severity data gap). Based on known pharmacology, flurazepam is a benzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor, increasing chloride channel opening frequency and producing CNS depression, sedation, and hypnosis. A 2023 Cryo-EM structural study in the literature evidence (PMID 37730991) confirms this receptor mechanism for benzodiazepine-class hypnotics generally.

Critically, the predicted indication is not a distinct new disease area — it is the same clinical use flurazepam was originally developed for. Multiple items in the literature evidence explicitly state this: PMID 1319429 notes "the pharmacologic treatment of insomnia began in 1970 with the availability of flurazepam, the first of the benzodiazepine hypnotics," and PMID 3332464 states flurazepam "is effective for both sleep induction and maintenance." This means the TxGNN model has, in this case, recovered a known and already-proven use rather than surfaced a genuinely novel repurposing candidate.

The mechanistic plausibility is therefore self-evident (same drug, same receptor target, same clinical use), but the practical value of this prediction depends on regulatory status: this evidence pack shows flurazepam as **not currently marketed** with **zero license records**, so any "repurposing" action here is really a market re-entry/reformulation decision rather than a new-indication discovery.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | J Clin Psychiatry | Establishes flurazepam as the first benzodiazepine hypnotic (1970), foundational to insomnia pharmacotherapy |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Review | Seminars in Neurology | Flurazepam effective for both sleep induction and maintenance, retains efficacy over 4 weeks nightly use |
| [7792498](https://pubmed.ncbi.nlm.nih.gov/7792498/) | 1995 | Clinical study | Sleep | Compared flurazepam 30mg vs. zolpidem 10mg on sleep perception in insomniac patients |
| [7792497](https://pubmed.ncbi.nlm.nih.gov/7792497/) | 1995 | Clinical study | Sleep | Compared flurazepam vs. zolpidem effects on sleep perception in normal volunteers |
| [6120270](https://pubmed.ncbi.nlm.nih.gov/6120270/) | 1981 | Clinical/lab study | Methods Find Exp Clin Pharmacol | Sleep laboratory comparison of triazolam, flunitrazepam, and flurazepam in insomniac patients |
| [2671059](https://pubmed.ncbi.nlm.nih.gov/2671059/) | 1989 | Clinical study | J Clin Psychopharmacol | Compared brotizolam vs. flurazepam vs. placebo on sleep/performance in elderly patients (n=36) |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | Critical review of rebound insomnia following discontinuation of triazolam, temazepam, and flurazepam |
| [38401406](https://pubmed.ncbi.nlm.nih.gov/38401406/) | 2024 | Systematic review/NMA | Eur Neuropsychopharmacol | Network meta-analysis of hypnotics (incl. benzodiazepine class) on next-day driving impairment |
| [641469](https://pubmed.ncbi.nlm.nih.gov/641469/) | 1978 | Review | J Fam Pract | Early review of insomnia management referencing flurazepam use and tolerance concerns |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Therapeutics | Safety/efficacy review of sleep medications in older adults, including benzodiazepine hypnotics |

---

## US Market Information

Flurazepam is currently **not marketed** in this jurisdiction — the evidence pack contains no license/NDA records (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: a Blocking-severity data gap exists — official label warnings/contraindications for flurazepam could not be retrieved, which prevents completion of an initial safety assessment. See Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Regulatory label data (warnings, contraindications) is missing and flagged as a **Blocking** gap, which by itself prevents any safety sign-off.
- The predicted "new" indication overlaps with flurazepam's already well-established historical use for insomnia rather than representing genuine repurposing novelty, and the drug currently has zero active licenses/market presence, with no registered clinical trials to support renewed development.

**To proceed, the following is needed:**
- Official label/warnings and contraindications (TFDA/FDA label PDF)
- Confirmed mechanism of action documentation from DrugBank
- Clarification of current/historical regulatory status (why 0 licenses despite established clinical use)
- An explicit novelty assessment distinguishing this candidate from flurazepam's known indication before allocating repurposing resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

