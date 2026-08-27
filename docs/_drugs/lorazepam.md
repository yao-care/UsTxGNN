---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 870
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

Lorazepam is a benzodiazepine (GABA-A receptor positive allosteric modulator) originally established for anxiety disorders, short-term insomnia, and status epilepticus. TxGNN's top-ranked prediction (**trigeminal nerve neoplasm**, 99.87%) has zero supporting trials or literature and is assessed as a likely model artifact with no biological plausibility. The best evidence-supported candidate is **insomnia**, scoring 99.80%, backed by **23 clinical trials** and **18 publications** — though this largely confirms an already-established secondary use rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no Taiwan/US license records; `original_indications` empty). Established pharmacology: anxiety disorders, short-term insomnia, status epilepticus, pre-anesthetic sedation |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| US/TW Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data is flagged as a data gap, but the repurposing rationale in the evidence pack consistently identifies lorazepam as a **GABA-A receptor positive allosteric modulator (PAM)**, which enhances inhibitory neurotransmission. This mechanism underlies its established sedative-hypnotic effect and is directly relevant to insomnia management — lorazepam has, in practice, long been used off-label/as a secondary agent for short-term insomnia. In this sense the "insomnia" prediction is less a novel repurposing hypothesis and more a confirmation of an already-recognized clinical use pattern, which is reflected in its comparatively strong evidence level (L3) relative to the other candidates.

By contrast, TxGNN's single highest-scoring prediction, trigeminal nerve neoplasm (99.87%), has no supporting clinical trials, ICTRP records, or literature, and the evidence pack's own rationale explicitly flags it as a probable false positive — lorazepam has no known antineoplastic or neuro-oncologic pharmacology. Several mid-ranked candidates (reading/thinking/audiogenic/startle/eating/micturition-induced seizures, trigeminal neoplasm, orgasm-induced seizures, AESD) cluster around reflex-epilepsy subtypes; while GABA-A potentiation is mechanistically plausible for seizure control in general, none of these rare subtypes have direct human efficacy data — evidence is limited to general status-epilepticus literature or unrelated animal-withdrawal studies. These were deprioritized in favor of the insomnia candidate for this report.

---

## Clinical Trial Evidence

(Extracted from the "insomnia (disease)" prediction; trials most directly involving lorazepam or its clinical use pattern)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03331042](https://clinicaltrials.gov/study/NCT03331042) | Phase 3 | Completed | 85 | 4-way crossover comparing SM-1 (diphenhydramine + zolpidem + delayed-release lorazepam) vs. diphenhydramine+zolpidem, diphenhydramine+lorazepam, and placebo in a phase-advance transient insomnia model |
| [NCT02671760](https://clinicaltrials.gov/study/NCT02671760) | Phase 2 | Completed | 39 | Combination product containing lorazepam evaluated for total sleep time in adults with short-term insomnia |
| [NCT04396327](https://clinicaltrials.gov/study/NCT04396327) | Phase 2 | Not yet recruiting | 14 | Pharmacodynamic crossover study of SM-1 (incl. lorazepam) vs. active comparator in a phase-advance transient insomnia model |
| [NCT03338764](https://clinicaltrials.gov/study/NCT03338764) | Phase 3 | Withdrawn | 0 | Planned double-blind RCT of SM-1 (incl. lorazepam) vs. placebo for transient insomnia; withdrawn before enrollment |
| [NCT06584513](https://clinicaltrials.gov/study/NCT06584513) | N/A | Recruiting | 470 | Patient-centred intervention (BE-SAFE) to reduce benzodiazepine/sedative-hypnotic (incl. lorazepam) use for sleep problems in older adults |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Electronically-delivered self-management packet to promote benzodiazepine (e.g., Ativan/lorazepam) cessation in Veterans |
| [NCT03405298](https://clinicaltrials.gov/study/NCT03405298) | N/A | Completed | 44 | Patient education intervention to reduce inappropriate chronic benzodiazepine (incl. lorazepam) use among older adults |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1400 | Prospective Taiwan cohort assessing hypnotic (incl. benzodiazepine) use patterns, efficacy, and safety in elderly patients with sleep disorders |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnography comparison of dexmedetomidine vs. GABA agonist sedatives (lorazepam class) on sleep architecture in mechanically ventilated ICU patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | RCT | Journal of Clinical Pharmacology | Double-blind crossover in 8 chronic insomniacs: lorazepam 2mg outperformed flurazepam 30mg on most sleep parameters |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | The Medical Letter on Drugs and Therapeutics | Review of pharmacologic options, including benzodiazepines, for chronic insomnia |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Review | Journal of Multidisciplinary Healthcare | Efficacy, safety, and drug-drug interactions of insomnia therapies in COVID-19 ("coronasomnia") patients |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacokinetics of anxiolytic drugs, including lorazepam, relevant to sedative-hypnotic dosing |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Cohort/Open-label | International Clinical Psychopharmacology | Comparison of lorazepam 0.5mg TID vs. 1.5mg HS dosing in chronic primary insomnia; TID regimen better addressed daytime fatigue |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Cohort | Sleep Medicine | Hypnotic prescription patterns in a large managed-care population, including lorazepam use for insomnia |
| [25453732](https://pubmed.ncbi.nlm.nih.gov/25453732/) | 2014 | Observational | Clinical Therapeutics | Benzodiazepine/sedative-hypnotic use among seriously ill older veterans, including inappropriate use for insomnia |
| [40110386](https://pubmed.ncbi.nlm.nih.gov/40110386/) | 2025 | Observational | Alpha Psychiatry | Prescribing trends of benzodiazepines and Z-drugs (incl. lorazepam) in Eastern China, 2015–2021 |
| [15040803](https://pubmed.ncbi.nlm.nih.gov/15040803/) | 2004 | Observational | Health and Quality of Life Outcomes | Sleep quality assessment and sedating drug (incl. benzodiazepines) use among hospitalized adults |
| [19514972](https://pubmed.ncbi.nlm.nih.gov/19514972/) | 2009 | Preclinical | Drug Delivery | Intranasal microemulsion formulation of lorazepam (and other benzodiazepines) evaluated for sleep induction in a rat model |

---

## US Market Information

No Taiwan/US regulatory license records are currently available for lorazepam in this evidence pack (`taiwan_regulatory.market_status`: 未上市 / Not Marketed; 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or DDI data were returned by the current data sources (TFDA label lookup returned no result — flagged as a **Blocking** data gap; DDI query returned `not_found`).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The insomnia indication is supported by a completed Phase 3 comparator trial, multiple Phase 2 studies, and a 1988 RCT showing lorazepam outperforming another hypnotic on sleep parameters — sufficient to justify guarded advancement, but this reflects reinforcement of an existing secondary use rather than a novel discovery. The TxGNN top-ranked candidate (trigeminal nerve neoplasm) and the reflex-epilepsy subtype candidates lack any direct clinical evidence and should remain on Hold/Research-Question status only.

**To proceed, the following is needed:**
- TFDA (or equivalent) product label with warnings/contraindications — currently a **Blocking** gap; safety review (S1) cannot formally begin without it
- Confirmed drug-drug interaction data (current DDI query: not found)
- Structured original-indication/license data, since `taiwan_regulatory.licenses` and `drug.original_indications` are both empty
- Formal relevance grading for the "pending" clinical trial and literature entries to refine the evidence base beyond the manually reviewed subset above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

