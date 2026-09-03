---
layout: default
title: Sodium Oxybate
parent: 僅模型預測 (L5)
nav_order: 1171
evidence_level: L5
indication_count: 6
---

# Sodium Oxybate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Sodium Oxybate: From Narcolepsy with Cataplexy to Insomnia

## One-Sentence Summary

Sodium oxybate (marketed as Xyrem/Xywav) is a GABA‑B/GHB receptor agonist currently used to treat narcolepsy with cataplexy and excessive daytime sleepiness, per trial descriptions found in the evidence pack.
The TxGNN model predicts it may also be effective for **Insomnia**, with **13 clinical trials** and **13 publications** currently associated with this indication —
though only **one trial** (a completed, head‑to‑head Phase 2 RCT vs. zolpidem) is graded as directly and strongly relevant.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy with cataplexy (per clinical trial descriptions in the evidence pack; not confirmed in local regulatory licensing data — data gap) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.99% (model rank 201) |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently a data gap for this candidate. Based on information available within the evidence pack itself, sodium oxybate is a GABA‑B and GHB (gamma‑hydroxybutyrate) receptor agonist that is well documented to significantly increase slow‑wave sleep (SWS) and consolidate sleep architecture — this is the same pharmacological property underlying its approved use in narcolepsy (reducing nocturnal sleep fragmentation and daytime sleepiness).

This SWS‑enhancing, sleep‑consolidating mechanism is biologically plausible for insomnia, particularly sleep‑maintenance insomnia, since deepening and stabilizing nighttime sleep addresses the core pathophysiology of the condition. This is directly supported by a completed Phase 2 RCT (NCT00383643) that compared sodium oxybate head‑to‑head with zolpidem (Ambien) in chronic insomnia patients. However, sodium oxybate is a Schedule‑controlled CNS depressant with known risks of respiratory depression, dependence, and nocturnal arousal/parasomnia-type events, so any repurposing case must be weighed against these risks relative to established first‑line hypnotics.

It is also worth noting that of the six diseases TxGNN predicted for this drug, four were assessed as low‑value or misleading signals rather than genuine therapeutic hypotheses: "neurogenic bladder" and "cauda equina syndrome" appear to be false positives with no mechanistic or literature support, while "restless legs syndrome" and "Wernicke‑Korsakoff syndrome" are actually documented **adverse effects/toxicity signals** of sodium oxybate/GHB in the literature, not treatment opportunities. Only the insomnia and (closely overlapping) "sleep disorder, initiating and maintaining sleep" predictions have genuine mechanistic and evidentiary backing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00383643](https://clinicaltrials.gov/study/NCT00383643) | Phase 2 | Completed | 48 | Randomized, double-blind, double-dummy, placebo-controlled comparison of sodium oxybate vs. zolpidem for chronic insomnia — the single most directly relevant trial. |
| [NCT00641186](https://clinicaltrials.gov/study/NCT00641186) | Phase 2 | Completed | 30 | Open-label trial of sodium oxybate for excessive daytime sleepiness and nocturnal sleep disturbance in mild-to-moderate Parkinson's disease. |
| [NCT00594256](https://clinicaltrials.gov/study/NCT00594256) | Phase 2 | Completed | 8 | Open-label pilot of adjunctive sodium oxybate for schizophrenia-associated sleep disturbances and persistent symptoms. |
| [NCT02637648](https://clinicaltrials.gov/study/NCT02637648) | Phase 3 | Unknown | 60 | Randomized, placebo-controlled trial of sodium oxybate for prophylaxis of headache and associated sleep disturbances in chronic/episodic cluster headache. |
| [NCT04508166](https://clinicaltrials.gov/study/NCT04508166) | N/A | Completed | 27 | Cross-over study testing whether deepening sleep (via drug interventions) reduces post-traumatic intrusive memories after trauma exposure. |
| [NCT01041495](https://clinicaltrials.gov/study/NCT01041495) | Phase 4 | Terminated | 37 | Cyclobenzaprine ER augmentation study for fibromyalgia fatigue/pain; sodium oxybate not the primary intervention. |
| [NCT04803786](https://clinicaltrials.gov/study/NCT04803786) | N/A | Completed | 110 | Real-world observational study (TENOR) on patients with narcolepsy transitioning from Xyrem to low-sodium oxybate (Xywav). |
| [NCT06421532](https://clinicaltrials.gov/study/NCT06421532) | Phase 2 | Enrolling by Invitation | 60 | Investigates whether deepening sleep with low-sodium oxybate enhances glymphatic clearance of amyloid-β in cerebral amyloid angiopathy. |
| [NCT00330291](https://clinicaltrials.gov/study/NCT00330291) | Phase 2 | Withdrawn (n=0) | 0 | Planned trial of Xyrem for treatment-refractory insomnia due to PTSD; withdrawn before enrollment. |
| [NCT01584934](https://clinicaltrials.gov/study/NCT01584934) | Phase 4 | Withdrawn (n=0) | 0 | Planned double-blind, placebo-controlled crossover trial of sodium oxybate for chronic fatigue syndrome; withdrawn before enrollment. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40120323](https://pubmed.ncbi.nlm.nih.gov/40120323/) | 2025 | Cohort | J Clin Neurosci | Propensity-matched cohort characterizing treatment patterns and comorbidities of narcolepsy patients treated with immediate-release sodium oxybate. |
| [18852348](https://pubmed.ncbi.nlm.nih.gov/18852348/) | 2008 | Cohort | Arch Neurol | Open-label polysomnographic study of sodium oxybate for excessive daytime sleepiness in Parkinson's disease, showing effects on sleep architecture. |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Review | Expert Opin Emerging Drugs | Reviews emerging pharmacological treatments for narcolepsy and related disorders, including sodium oxybate's mechanism. |
| [26171909](https://pubmed.ncbi.nlm.nih.gov/26171909/) | 2015 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of effects of opioid, hypnotic and sedating medications (including GABA-ergic agents) on sleep-disordered breathing. |
| [11174231](https://pubmed.ncbi.nlm.nih.gov/11174231/) | 2001 | Case Report | Ann Emerg Med | Describes the GHB (sodium oxybate active moiety) withdrawal syndrome — relevant safety signal for dependence risk. |
| [37590830](https://pubmed.ncbi.nlm.nih.gov/37590830/) | 2023 | Review | Continuum (Minneap Minn) | Comprehensive review of pediatric sleep disorders including insomnia, narcolepsy, and treatment approaches. |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | Rev Neurol | Review of narcolepsy with cataplexy, including associated sleep-maintenance insomnia and pharmacological management. |
| [31526967](https://pubmed.ncbi.nlm.nih.gov/31526967/) | 2019 | Case Report | Sleep Medicine | Case report of sodium oxybate used to treat severe sleep initiation failure in a child with EBV encephalitis affecting the sleep-wake regulation system. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Reviews pitolisant's place in narcolepsy therapy, contextualizing sodium oxybate as an alternative treatment for sleep disturbance. |
| [21815499](https://pubmed.ncbi.nlm.nih.gov/21815499/) | 2011 | Review | Rev Med Suisse | Discusses the bidirectional relationship between chronic pain and sleep disorders, referencing hypnotic treatment strategies. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only directly relevant evidence is a single completed Phase 2 RCT (n=48, 2006–2009) against zolpidem — supportive but not sufficient on its own (L2), and most other trials in the evidence pack are indirect (Parkinson's, schizophrenia, fibromyalgia, PTSD) rather than primary-insomnia populations.
- A **Blocking** data gap exists for local regulatory warning/contraindication information (DG001), which prevents completion of even a preliminary safety assessment (S1) — this alone precludes advancing past Hold.
- Sodium oxybate is a controlled CNS depressant with documented dependence, respiratory depression, and paradoxical sleep-disturbance risks (e.g., restless legs syndrome as a reported side effect), which must be weighed against existing first-line insomnia therapies before any advancement.

**To proceed, the following is needed:**
- Local drug label / regulatory warning and contraindication data (DG001, blocking)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A larger, confirmatory, insomnia-specific RCT (the existing trial is small, dated, and single-site in design characteristics)
- A formal risk–benefit/safety review addressing abuse potential, dependence, and comparative safety vs. standard hypnotics (e.g., zolpidem, eszopiclone) given the drug's controlled-substance status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

