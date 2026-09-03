---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 1052
evidence_level: L5
indication_count: 3
---

# Pitolisant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Pitolisant: From Narcolepsy to Insomnia (Disease)

## One-Sentence Summary

> Pitolisant is a selective histamine H3-receptor inverse agonist originally developed and approved (per literature evidence) for narcolepsy with or without cataplexy, where it works by *promoting* wakefulness.
> The TxGNN model predicts it may be effective for **Insomnia (disease)**, but the only directly designed clinical trial was withdrawn with zero enrollment, and the drug's known wake-promoting mechanism runs **opposite** to what insomnia treatment requires.
> Evidence for this specific prediction is weak (**1 withdrawn trial**, **8 indirect publications**, none an insomnia RCT) — this should be treated as a low-confidence, mechanistically questionable signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy (with or without cataplexy) — *inferred from literature evidence in this pack; Taiwan license/original_indications data unavailable* |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (未上市) in Taiwan |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data from DrugBank is not available (flagged as a High-severity data gap, DG002). Based on the mechanistic information available in this evidence pack, Pitolisant is a selective histamine H3-receptor inverse agonist/antagonist. It works by blocking presynaptic H3 autoreceptors, which increases histamine release and enhances wakefulness — this is precisely the mechanism used to treat excessive daytime sleepiness in narcolepsy and OSA-related residual sleepiness (as reflected in the literature evidence for this drug).

This creates a fundamental mechanistic concern for the "insomnia" prediction: insomnia treatment requires promoting sleep/sedation, while Pitolisant pharmacologically does the opposite — it promotes arousal. The evidence pack's own rationale explicitly flags this as a likely **false positive**, probably arising from proximity of "sleep disorder" nodes in the knowledge graph rather than a genuine pharmacological fit. Supporting this concern, the only clinical trial directly designed around a sleep/behavioral endpoint for Pitolisant beyond narcolepsy/OSA (NCT02800083, alcohol use disorder) was withdrawn with 0 patients enrolled, and none of the 8 literature citations report insomnia efficacy data — they instead describe narcolepsy, OSA/excessive daytime sleepiness (opposite direction), or general H3-receptor pharmacology reviews.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Withdrawn | 0 | Designed to evaluate Pitolisant for alcohol use disorder (heavy drinking days as primary endpoint); trial was withdrawn before enrollment began — no efficacy or safety data was generated. Relevance to insomnia graded **C** (indirect, no data produced). |

**Note:** No clinical trial in this evidence pack directly tests Pitolisant for insomnia. This is the only trial retrieved under this candidate, and it produced no usable data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT (narcolepsy, pediatric) | The Lancet. Neurology | Phase 3 RCT confirming safety/efficacy of Pitolisant in children with narcolepsy with/without cataplexy — supports wake-promoting profile, not insomnia. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT (OSA/EDS) | Chest | RCT showing Pitolisant reduces residual excessive daytime sleepiness in CPAP-adherent OSA patients — opposite therapeutic direction to insomnia. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT (OSA/EDS) | Am J Respir Crit Care Med | RCT of Pitolisant for daytime sleepiness in OSA patients refusing CPAP — again a wake-promoting, not sleep-promoting, effect. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Real-world cohort (narcolepsy) | Revista de neurología | Real-life "WAKE" study evaluating effectiveness/safety of Pitolisant in treatment-refractory type 1 narcolepsy patients. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | Overview of histamine receptor pharmacology (H1–H4) in health and disease; general mechanistic background only. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Design, Development and Therapy | Review of Pitolisant's development and therapeutic role in narcolepsy management. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | Reviews histaminergic system changes in neuropsychiatric disorders; mentions Pitolisant for narcolepsy alongside doxepin (H1 antagonist) for insomnia — highlighting these are pharmacologically distinct approaches. |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review | Clinical Neuropharmacology | Early review describing Pitolisant as a stimulant alternative for narcolepsy-cataplexy in adolescents. |

**Summary:** None of the 8 publications report insomnia efficacy data. The evidence base for this indication is entirely composed of narcolepsy/OSA studies (opposite pharmacological direction) and general H3-receptor mechanism reviews.

---

## US Market Information

Pitolisant currently holds **0 approved licenses** in Taiwan (market status: 未上市 / Not Marketed). No license records are available in this evidence pack to summarize approved indications or dosage forms.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed TFDA warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (flagged as a **Blocking** data gap, DG001) — this data must be obtained before any safety evaluation (S1 stage) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted mechanism directly contradicts the therapeutic need for insomnia (Pitolisant is wake-promoting, not sedating), and the only trial designed around this candidate's evidence trail was withdrawn with zero patients. No clinical or literature evidence supports efficacy for insomnia; this prediction is best treated as a likely knowledge-graph artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank (DG002) to formally validate the mechanistic mismatch noted above
- If pursued at all, a properly designed and completed insomnia-specific trial, since none currently exists
- Consider deprioritizing this candidate in favor of other TxGNN signals in this pack with stronger mechanistic plausibility (e.g., ADHD, rank 2 — H3-antagonism as a cognitive/attention enhancer — though this remains at "Research Question" stage with no clinical trial evidence either)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

