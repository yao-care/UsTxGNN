---
layout: default
title: Triazolam
parent: 僅模型預測 (L5)
nav_order: 1259
evidence_level: L5
indication_count: 1
---

# Triazolam
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

# Triazolam: From Undocumented Original Indication to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

> Triazolam (DB00897) has no original indication recorded in the Taiwan regulatory registry (the drug is currently **not marketed** in Taiwan), so its documented clinical history is limited in this evidence pack.
> The TxGNN model predicts it may be effective for **Sleep Disorder, Initiating and Maintaining Sleep (Insomnia)**, with a prediction score of **99.72%**,
> supported by **0 registered clinical trials** but **20 publications**, including an AASM clinical practice guideline based on pooled RCT evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license or `original_indications` data recorded in this evidence pack |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep (Insomnia) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed `original_moa` data is not available for triazolam in this evidence pack. However, the repurposing rationale supplied alongside the prediction describes a well-characterized mechanism: triazolam is a short-acting benzodiazepine (BZD) that acts as a **positive allosteric modulator at the α1 subunit of the GABA-A receptor**, enhancing GABAergic inhibitory neurotransmission and prolonging chloride channel opening. This produces sedative, anxiolytic, muscle-relaxant, and hypnotic effects.

No original indication is documented in the Taiwan regulatory dataset for this drug, so a direct "original indication → new indication" comparison cannot be made from the evidence pack alone. That said, triazolam's GABA-A-mediated mechanism is the classic, long-established pharmacological basis for treating insomnia — it is not a speculative or novel mechanistic link. In effect, the TxGNN prediction here reconstructs a well-known clinical use case from the knowledge graph rather than proposing a genuinely new therapeutic hypothesis, which is consistent with the strong prediction score and abundant supporting literature.

Because the mechanism is already the accepted pharmacological rationale for BZD hypnotics in insomnia, the plausibility of this prediction is high. The main open question is not "does the mechanism fit" but rather what registrational and safety data (TFDA label, DDI profile) would be required before any regulatory or clinical action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical Practice Guideline (based on pooled RCTs) | J Clin Sleep Med | AASM guideline establishing pharmacologic treatment recommendations for chronic insomnia in adults, including drugs used off-label for this indication |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic Review / Network Meta-analysis | Sleep | Compares efficacy and safety of hypnotics (including BZDs) for insomnia in older adults |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Systematic Review / Meta-analysis | Psychiatry Clin Neurosci | Efficacy/safety of sleep medication classes (including benzodiazepines) combined with antidepressants for MDD with insomnia |
| [39932761](https://pubmed.ncbi.nlm.nih.gov/39932761/) | 2025 | Review | Minerva Medica | Overview of insomnia disorder diagnosis and management, contextualizing pharmacologic options |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review (elderly population) | Drugs & Aging | Pharmacological management recommendations for chronic insomnia in elderly patients |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review (safety/efficacy) | Clin Therapeutics | Reviews safety and efficacy of sleep medications, including BZDs, in older adults |
| [19682231](https://pubmed.ncbi.nlm.nih.gov/19682231/) | 2010 | Experimental / Human Cohort | J Sleep Res | Compares retrograde effects of triazolam and zolpidem on sleep-dependent motor learning |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Critical Review | J Clin Psychopharmacol | Reviews rebound insomnia risk following discontinuation of triazolam and other short half-life BZDs |
| [6120270](https://pubmed.ncbi.nlm.nih.gov/6120270/) | 1981 | Sleep Laboratory / Clinical Study | Methods Find Exp Clin Pharmacol | Polysomnographic study of triazolam, flunitrazepam, and flurazepam effects in insomniac patients |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Comparative Pharmacology Review | Ann Pharmacother | Compares zolpidem and triazolam in efficacy and safety for insomnia treatment |

---

## Taiwan Market Information

Triazolam is currently not marketed in Taiwan (0 licenses on record); no authorization or product data is available.

---

## Safety Considerations

Detailed TFDA label warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (`safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all empty or unresolved). Please refer to the package insert for safety information.

⚠️ Note: this data gap (DG001 — TFDA 仿單警語/禁忌) is flagged as **Blocking** severity in the source evidence pack, meaning it currently prevents a full S1 safety initial assessment. This should be resolved before any clinical or regulatory action is taken, given triazolam's known BZD-class risks (sedation, dependence, rebound insomnia, CNS depressant interactions).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is mechanistically well-supported (classic GABA-A-mediated BZD hypnotic action) and backed by strong literature evidence including an AASM clinical practice guideline, but there are no registered clinical trials specific to this candidate, no Taiwan market presence, and a Blocking-severity data gap on TFDA label safety information.

**To proceed, the following is needed:**
- TFDA 仿單警語與禁忌資料 (Blocking — required before S1 safety clearance; source: TFDA official label PDF)
- Confirmed MOA data via DrugBank API (currently marked as Data Gap despite mechanistic description being available from the repurposing rationale)
- Drug-drug interaction (DDI) profile (`safety.ddi.query_status` = not_found)
- Route compatibility assessment (currently `pending`, no available/required routes documented)
- Clarification of original indication history, since no data is currently recorded in `taiwan_regulatory.licenses` or `drug.original_indications`
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

