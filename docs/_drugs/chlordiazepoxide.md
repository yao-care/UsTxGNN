---
layout: default
title: Chlordiazepoxide
parent: 僅模型預測 (L5)
nav_order: 435
evidence_level: L5
indication_count: 10
---

# Chlordiazepoxide
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

The txgnn-pipeline skill confirms this is a standard report-generation task within the TxGNN framework. No special pipeline steps are needed — I'll proceed directly with generating the evaluation report from the Evidence Pack.

---

# Chlordiazepoxide: From Anxiety & Alcohol Withdrawal to Insomnia

## One-Sentence Summary

Chlordiazepoxide (Librium) is the first benzodiazepine ever developed, historically used for anxiety disorders and alcohol withdrawal management.
The TxGNN model predicts it may be effective for **Insomnia**, with **no directly relevant clinical trials** and **6 publications** currently identified in support of this direction.
Evidence is predominantly observational and review-level, placing this at **Evidence Level L3** — with a **Hold** recommendation given the drug's unfavorable pharmacokinetic profile and modern clinical guidelines that explicitly discourage long-acting benzodiazepines for insomnia.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders; alcohol withdrawal (historical class use — no regulatory records found in database) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L3 |
| US Market Status | No records retrieved (0 NDAs in database) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, chlordiazepoxide — the prototypical benzodiazepine — acts as a positive allosteric modulator of the GABA-A receptor. It enhances the inhibitory effect of γ-aminobutyric acid (GABA), producing sedation, anxiolysis, muscle relaxation, and anticonvulsant activity. This GABA-A enhancement can shorten sleep onset latency and increase NREM sleep proportion, forming the mechanistic basis for the TxGNN insomnia prediction.

Anxiety and insomnia are neurobiologically intertwined. Chronic hyperarousal — a core feature of anxiety disorders — directly impairs both sleep initiation and sleep maintenance. Chlordiazepoxide's broad CNS depressant effects naturally extend to sleep induction, and the benzodiazepine class as a whole was the dominant pharmacological treatment for insomnia for decades before Z-drugs (zolpidem, eszopiclone) and orexin receptor antagonists became available. Controlled studies confirm that benzodiazepines as a class produce short-term improvements in sleep latency and total sleep time (PMID 2883822). It is also noteworthy that TxGNN independently ranked "sleep disorder, initiating and maintaining sleep" (DIMS — the historical ICD classification for insomnia) at rank 6, with a largely overlapping evidence base including two direct RCTs involving chlordiazepoxide in sleep-related contexts, further corroborating the model's signal.

However, the clinical case for chlordiazepoxide *specifically* in insomnia is substantially weakened by its pharmacokinetic profile. Its half-life of 5–30 hours — compounded by active metabolites (desmethylchlorodiazepoxide, demoxepam) with even longer half-lives — causes significant next-day residual sedation and drug accumulation with repeated nightly dosing. Current sleep medicine guidelines explicitly recommend against long-acting benzodiazepines as first-line insomnia therapy. The risk of falls, cognitive impairment, delirium, tolerance, and physical dependence is particularly high in elderly patients, who appear on the Beers Criteria as a protected population. These factors collectively explain the **Hold** recommendation despite a near-perfect TxGNN prediction score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

> **Note:** One trial was retrieved (NCT01109030: Pioglitazone as adjunct for moderate-to-severe depression, Phase 2/3, n=50). This was assessed as a pipeline mismatch (Grade C relevance — different drug and unrelated indication) and is not counted as supporting evidence for chlordiazepoxide in insomnia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4628683](https://pubmed.ncbi.nlm.nih.gov/4628683/) | 1972 | Clinical Trial | Current Therapeutic Research | Clinical evaluation of chlordiazepoxide efficacy in anxious outpatients; demonstrates anxiolytic and sedative effects with indirect relevance to sleep-onset difficulty |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Review | Acta Psychiatrica Scandinavica (Suppl) | Pharmacodynamic review of benzodiazepine hypnotics in elderly; controlled studies show 2–3× increased sensitivity in older adults; elevated fall and cognitive impairment risk with long-acting agents |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacokinetic review of anxiolytic drugs; highlights implications of long half-lives and active metabolites for dosing and tolerability in anxiety/sleep disorders |
| [6111745](https://pubmed.ncbi.nlm.nih.gov/6111745/) | 1981 | Review | The Medical Letter | Comparative guidance on benzodiazepine selection; discusses trade-offs between long-acting and short-acting agents for anxiolytic and sedative-hypnotic use |
| [30680986](https://pubmed.ncbi.nlm.nih.gov/30680986/) | 2019 | Cross-sectional | Medicinski Glasnik | Prevalence of potentially inappropriate medications (PIMs) in elderly Iranians; chlordiazepoxide flagged per Beers Criteria 2012, underscoring ongoing safety concerns in routine clinical practice |
| [14085195](https://pubmed.ncbi.nlm.nih.gov/14085195/) | 1963 | Case Series | Acta Psychiatrica Scandinavica | Early case series of a Librium metabolite (Ro 4-5360) in anxiety neuroses and psychosomatic syndromes; historical context only, no modern insomnia endpoints |

---

## Safety Considerations

Please refer to the package insert for safety information.

The following signals are identified from available literature and known pharmacology:

- **Elderly Population Risk**: Chlordiazepoxide is listed on the American Geriatrics Society Beers Criteria as a potentially inappropriate medication (PIM) for older adults. Elderly patients show 2–3× increased pharmacodynamic sensitivity compared to younger adults, with significantly elevated risk of falls, hip fractures, cognitive impairment, and delirium (PMID 2883822; PMID 30680986).
- **Dependence and Withdrawal**: Long-term benzodiazepine use carries substantial risk of physical dependence. Abrupt discontinuation may precipitate a clinically significant withdrawal syndrome, including rebound insomnia, anxiety, tremor, and seizures — paradoxically worsening the very condition being treated.
- **Next-Day Residual Effects**: Due to the long half-life and active metabolites, repeated nightly dosing is expected to cause daytime sedation, psychomotor impairment, and anterograde memory impairment — particularly problematic in occupational and driving safety contexts.
- **Drug Interactions**: No DDI data was retrieved from the database. Clinically, additive CNS depression is expected with opioids, alcohol, antipsychotics, antihistamines, and other sedative-hypnotics — a combination that substantially increases respiratory depression risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although chlordiazepoxide's GABA-A mechanism provides a biologically plausible basis for insomnia management, its long half-life, accumulating active metabolites, unfavorable risk profile in elderly patients, and explicit deprioritization in modern insomnia clinical guidelines make it a poor repurposing candidate. No directly relevant RCTs exist, and the available literature is predominantly historical, observational, or review-level.

**To proceed, the following is needed:**
- Verify US FDA regulatory status directly via the FDA Orange Book and DailyMed (current database shows 0 records, which likely reflects a data retrieval gap rather than true non-approval)
- Retrieve and parse the full package insert to complete the safety profile (DG001: TFDA/FDA warnings and contraindications)
- Obtain complete mechanism of action data from DrugBank API (DG002: MOA description)
- Define a specific clinical niche where chlordiazepoxide's profile might offer a genuine advantage — for example, short-term management of insomnia comorbid with acute anxiety in non-elderly adults, where anxiolytic and hypnotic effects can be leveraged together
- If pursuing further, conduct a systematic comparison of safety outcomes between chlordiazepoxide and shorter-acting benzodiazepines (temazepam, triazolam) or Z-drugs in insomnia before any development investment is made
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

