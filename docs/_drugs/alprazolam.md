---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 3
---

# Alprazolam
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

# Alprazolam: From Anxiety Disorder to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine widely used for anxiety disorders and panic disorder, exerting its effects through positive modulation of GABA-A receptors to produce central nervous system depression.
The TxGNN model predicts it may be effective for **Insomnia**, with **7 clinical trials** and **18 publications** currently supporting this direction.
While the mechanistic bridge from anxiolysis to sedation is pharmacologically coherent, the evidence base consists primarily of observational and indirect studies rather than dedicated large-scale RCTs for insomnia as a primary indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety Disorder / Panic Disorder |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed |
| Number of Taiwan Approvals | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alprazolam is a triazolo-benzodiazepine that acts by positively modulating GABA-A receptors, enhancing chloride ion influx and producing dose-dependent central nervous system depression. This mechanism shortens sleep onset latency and increases time in early slow-wave sleep stages — the same pharmacological targets exploited by dedicated sedative-hypnotic agents. The mechanistic overlap with insomnia pathophysiology is therefore direct and well-established, which likely drives the high TxGNN prediction score.

The original indication (anxiety and panic disorder) and insomnia are closely intertwined clinically. Anxiety-driven hyperarousal is among the most common precipitants of insomnia, and GABAergic suppression of this hyperarousal directly addresses the disorder's pathophysiology. In real-world practice, alprazolam is already used off-label for sleep difficulties in patients with comorbid anxiety, as reflected in the attached comparative study in hemodialysis patients (PMID 33403184) and the integrative therapy trial in coronary heart disease patients with insomnia (PMID 39183410).

However, alprazolam is not considered a first-line treatment for insomnia under current clinical guidelines (which favor cognitive behavioral therapy for insomnia, z-drugs, or low-dose doxepin). The key limitations are REM sleep suppression, pharmacodynamic tolerance development, and physical dependence risk with chronic use — all of which are particularly problematic in the long-term management that insomnia requires. The TxGNN prediction most likely captures the established anxiolytic-to-hypnotic pharmacological bridge rather than identifying a truly novel therapeutic opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | Observational | Unknown | 1,400 | Large prospective cohort at a Taiwanese academic center examining medication use patterns, safety outcomes, and pharmacokinetic/pharmacogenetic characteristics of hypnotics — including benzodiazepines — in elderly patients with sleep disorders. Most directly relevant real-world dataset in a Taiwan population. |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | Multicenter open-label trial comparing Niravam™ (alprazolam XR) combined with a newly prescribed SSRI/SNRI versus SSRI/SNRI alone in patients with GAD or Panic Disorder. Completed in 8 weeks with 848 total subjects across 212 sites; confirms alprazolam's rapid CNS sedation effect in anxious patients who frequently present with sleep difficulties. |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | Randomized comparison of hypnosis versus alprazolam premedication for perioperative anxiety in gynecological laparoscopic surgery. Alprazolam used as the active comparator for pre-procedure sedation — not chronic insomnia, but confirms its role as a benchmark sedative-anxiolytic agent. |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | Double-blind RCT evaluating AVP-923 (dextromethorphan/quinidine) for agitation in Alzheimer's Disease. Benzodiazepines may have appeared as background or rescue medications; indirect evidence only. |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Electronically-delivered self-management intervention to promote benzodiazepine (alprazolam, lorazepam) cessation in Veterans prescribed BZDs mainly for anxiety and sleep difficulties. Context is discontinuation rather than treatment efficacy, but highlights the real-world overlap between insomnia and BZD prescribing. |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Clarithromycin for central hypersomnia — clarithromycin is the study drug, not alprazolam. Informative for understanding GABA system involvement in sleep architecture (the proposed mechanism of action) but does not provide direct evidence for alprazolam in insomnia. |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin for benzodiazepine dependence — terminated prematurely with only 2 enrolled patients. No interpretable data; included for completeness only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | RCT/Comparative | Cureus | Direct head-to-head comparison of alprazolam versus melatonin for sleep disturbances in hemodialysis (end-stage renal disease) patients. Alprazolam is used as the active control arm, confirming established clinical use for sleep disorders in a high-comorbidity population and providing comparative safety and efficacy data. |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Clinical Trial | Medicine | Retrospective observational study of 116 patients with coronary heart disease and comorbid insomnia: alprazolam-only control group vs. integrative Du Meridian moxibustion + ear acupuncture group. Demonstrates alprazolam as an active current standard of care for insomnia in this specific comorbid population. |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Systematic review of RCTs, case-controls, and cohort studies on tranquilizers (including benzodiazepines) for elderly patients with chronic non-communicable diseases, evaluating dose, efficacy outcomes, and adverse effects. Relevant to alprazolam's benefit-risk profile in insomnia. |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical Study | Aging | Proteomic analysis in mice showing 24-day repeated alprazolam administration causes mitochondrial dysfunction and impairs hippocampus-dependent memory consolidation. Raises an important mechanistic safety concern for chronic insomnia use, where long-term administration is expected. |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Retrospective/Real-world | China Journal of Chinese Materia Medica | Real-world analysis of 1,067 insomnia patients from 20 hospitals' HIS databases; benzodiazepines among the most commonly co-prescribed agents alongside TCM. Provides epidemiological context for alprazolam-class drug use in clinical insomnia management in East Asian populations. |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | Medicine | Single-center study on insomnia among COVID-19 survivors (Dec 2022–Feb 2023), using ISI scale. Quantifies the post-pandemic burden of insomnia and explores risk factors — contextualizes the growing unmet medical need that makes insomnia repurposing candidates relevant. |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohort | JHEP Reports | Retrospective cohort showing that deprescribing zolpidem (a non-BZD hypnotic) in cirrhosis patients significantly reduces falls and fractures. Although focused on zolpidem, findings apply to BZD class sedative-hypnotics: underscores the hazard of long-term hypnotic prescribing in vulnerable populations relevant to the insomnia indication. |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Epidemiological Model | Value in Health Regional Issues | Ten-year predictive model of benzodiazepine prescribing trends in Croatia — BZDs commonly used for anxiety, insomnia, and mood disorders. Long-term use associated with memory loss, Alzheimer's risk, dependence, falls, and traffic accidents. Provides risk-quantification context for alprazolam in the insomnia indication. |
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | RCT | Brain and Behavior | RCT of eszopiclone (a non-BZD GABA-A positive modulator) in elderly Alzheimer's patients with sleep disorders; eszopiclone improved sleep quality and partially preserved cognitive function. Serves as a benchmark for the sedative-hypnotic drug class — alprazolam targets the same receptor family but with less sleep-architecture selectivity. |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Observational | Sleep Medicine | Analysis of hypnotic prescription patterns in a large managed-care population, showing a decline in classic hypnotic use and a rise in non-hypnotic (including BZD anxiolytic) prescriptions for insomnia over the preceding decade. Documents the off-label prescribing trend that underpins the insomnia repurposing hypothesis for alprazolam. |

---

## Safety Considerations

Please refer to the package insert for safety information.

Based on known benzodiazepine class pharmacology, the following safety considerations are clinically relevant in the insomnia context and should be addressed in any formal repurposing plan:

- **Dependence and tolerance**: Physical dependence and pharmacodynamic tolerance develop with repeated use — particularly concerning for chronic insomnia management.
- **REM sleep suppression**: Alprazolam suppresses REM sleep, potentially worsening sleep quality despite reducing sleep latency.
- **Withdrawal syndrome**: Abrupt discontinuation risks rebound insomnia and withdrawal seizures.
- **CNS depression and falls**: Sedation, cognitive impairment, and psychomotor slowing increase fall risk, especially in elderly patients.
- **Cognitive effects**: Repeated administration is associated with anterograde amnesia and, in preclinical models, hippocampal mitochondrial dysfunction (PMID 37801512).

Full Taiwan FDA package insert data (DG001) is currently unavailable — this is a blocking gap that prevents formal safety screening completion.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score of 99.81% reflects a well-established pharmacological connection: alprazolam's GABAergic mechanism directly reduces sleep onset latency, and clinical evidence (PMID 33403184, 39183410) confirms real-world use of alprazolam for insomnia in comorbid populations. However, alprazolam is not recommended as a first-line insomnia agent in current guidelines due to its dependence liability and REM-suppressive effects, limiting the repurposing opportunity to specific subpopulations (e.g., insomnia driven by comorbid anxiety, short-term use) rather than a broad label expansion.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking)**: Download and parse the TFDA package insert to complete the S1 safety screening — without this, formal risk classification cannot proceed.
- **Resolve DG002 (High)**: Retrieve full DrugBank MOA data to support a rigorous mechanistic justification section and regulatory dossier.
- **Define target patient population**: Clarify whether the repurposing target is general insomnia or a specific comorbid subgroup (e.g., anxiety-comorbid insomnia, ESRD insomnia) where the risk-benefit ratio is more favorable.
- **Comparative evidence review**: Commission a systematic review specifically comparing alprazolam against first-line insomnia treatments (CBT-I, eszopiclone, z-drugs, low-dose doxepin) to establish the incremental value and identify the patient segments most likely to benefit.
- **Risk management framework**: Develop a structured risk mitigation plan addressing dependence monitoring, maximum treatment duration, and discontinuation taper protocols — required for any regulatory submission in the insomnia indication.
- **Taiwan regulatory pathway assessment**: Given that alprazolam has no current Taiwan approvals, determine whether a full NDA submission or a bridging strategy from existing foreign approvals (US Xanax/Niravam) is the appropriate regulatory path.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

