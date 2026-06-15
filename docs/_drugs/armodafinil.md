---
layout: default
title: Armodafinil
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 1
---

# Armodafinil
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

The `txgnn-pipeline` skill covers pipeline operations — the report writing instructions are fully defined in the system prompt. Proceeding directly with the evaluation report.

---

# Armodafinil: From Narcolepsy to Insomnia

## One-Sentence Summary

Armodafinil is the R-enantiomer of modafinil, approved in the United States as a wakefulness-promoting agent for excessive sleepiness associated with narcolepsy, obstructive sleep apnea (OSA), and shift work disorder (SWD).
The TxGNN model predicts it may be effective for **Insomnia**, with **12 clinical trials** and **19 publications** currently touching this direction — though the mechanistic connection is indirect and potentially paradoxical, as the drug's core action promotes wakefulness rather than sleep.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Excessive sleepiness associated with narcolepsy, obstructive sleep apnea, and shift work disorder |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| US Market Status | Not found in database (0 records returned) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacology, Armodafinil is the R-enantiomer of modafinil — a wakefulness-promoting agent that primarily works through dopamine transporter (DAT) inhibition, increasing dopaminergic tone in arousal-related brain circuits (hypothalamic histamine pathways, noradrenergic locus coeruleus). Its core pharmacological effect is to sustain alertness and reduce excessive daytime sleepiness, not to facilitate sleep onset or sleep continuity.

The mechanistic connection to insomnia is, at best, counterintuitive. Insomnia treatment generally requires promoting sleep initiation or maintenance, whereas armodafinil acts in the opposite direction. The clinical trials captured in this evidence pack link armodafinil to "insomnia" through three indirect pathways: (1) oncology patients simultaneously experiencing insomnia and cancer-related fatigue, where armodafinil targets fatigue while CBT-I addresses insomnia; (2) sleep-disordered breathing (OSA/SDB) comorbid with insomnia, where armodafinil treats residual daytime sleepiness rather than insomnia itself; and (3) Phase 3 trials for the drug's approved indications (narcolepsy, OSA), where insomnia appears as a safety monitoring variable, not a treatment outcome.

One narrow scenario where armodafinil might theoretically help: patients with circadian rhythm disruption (e.g., shift work disorder) who experience insomnia as a component of schedule misalignment — but this represents a highly specific subgroup, and even then, the primary effect would be on alertness during work hours, not sleep quality during off-hours. The TxGNN model's high score (99.89%) most likely reflects co-occurrence of insomnia-related terminology across the knowledge graph rather than a validated therapeutic relationship. Prescribing armodafinil for primary insomnia without further mechanistic evidence carries a meaningful risk of worsening the condition.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | Completed | 226 | CBT with or without armodafinil for insomnia and fatigue in cancer survivors post-chemotherapy; armodafinil primarily targets fatigue, CBT-I targets insomnia |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot RCT of brief behavioral therapy (BBT-I or CBT-I) ± armodafinil 150 mg/day for insomnia management in breast cancer patients |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm RCT of CBT-I ± armodafinil in breast cancer patients with sleep disturbances after chemotherapy completion |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | Phase NA | Completed | 39 | Armodafinil and/or CBT-I for insomnia comorbid with sleep-disordered breathing; armodafinil role is treating OSA residual sleepiness, not insomnia |
| [NCT01080807](https://clinicaltrials.gov/study/NCT01080807) | Phase 4 | Completed | 385 | Armodafinil 150 mg for excessive sleepiness in shift work disorder; insomnia is a co-morbidity of SWD, not the primary endpoint |
| [NCT01072630](https://clinicaltrials.gov/study/NCT01072630) | Phase 3 | Completed | 492 | Adjunctive armodafinil (150 and 200 mg/day) vs placebo for major depression in Bipolar I disorder; sleep assessed as secondary outcome |
| [NCT01072929](https://clinicaltrials.gov/study/NCT01072929) | Phase 3 | Completed | 433 | Fixed-dose adjunctive armodafinil for Bipolar I major depression; parallel-group DB/PC design |
| [NCT01305408](https://clinicaltrials.gov/study/NCT01305408) | Phase 3 | Completed | 399 | Adjunctive armodafinil 150 mg/day for Bipolar I major depressive episodes alongside mood stabilizers |
| [NCT00481195](https://clinicaltrials.gov/study/NCT00481195) | Phase 2 | Completed | 257 | 8-week fixed-dose armodafinil 150 mg as adjunctive therapy for Bipolar I major depressive episodes |
| [NCT00772005](https://clinicaltrials.gov/study/NCT00772005) | Phase 2 | Completed | 287 | 24-week DB/PC armodafinil adjunctive therapy for negative symptoms of schizophrenia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review | Parkinsonism & Related Disorders | Meta-analysis of pharmacological interventions for daytime sleepiness and sleep disorders in Parkinson's disease; modafinil/armodafinil class evaluated |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | EBM Review | Movement Disorders | MDS Task Force evidence-based review of non-motor symptom treatments in PD including sleep disorders; wakefulness agents assessed |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Evidence-Based Review | Drugs | Comprehensive review of approved and off-label uses of modafinil (parent compound); covers narcolepsy, OSA, SWD, fatigue, and cognitive applications |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic Review & Meta-analysis | PloS One | Modafinil efficacy for fatigue and excessive daytime sleepiness in neurological disorders; confirms class-wide wakefulness effect, not sleep-promoting |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Narrative Review | Expert Opinion on Pharmacotherapy | Pharmacological and non-pharmacological management of sleep disturbances in Parkinson's disease; wakefulness agents reviewed in context of broader sleep dysfunction |
| [24272458](https://pubmed.ncbi.nlm.nih.gov/24272458/) | 2014 | Review | Neurotherapeutics | Treatment of sleep disorders in Parkinson's disease including insomnia, REM sleep behavior disorder; role of wakefulness-promoting agents discussed |
| [21904092](https://pubmed.ncbi.nlm.nih.gov/21904092/) | 2011 | Review | Postgraduate Medicine | Shift work disorder pathophysiology and management; armodafinil cited for SWD-related excessive sleepiness; insomnia as component of SWD |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | Drugs | Shift work sleep disorder — burden of illness and management; wake-promoting agents' role in reducing sleepiness during shifts, not treating sleep-onset insomnia |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | Revue Neurologique | Narcolepsy with cataplexy; sleep maintenance insomnia noted as an associated narcolepsy symptom; armodafinil class used for EDS, not the insomnia component |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Review | Expert Opinion on Emerging Drugs | Emerging treatments for narcolepsy and related disorders; armodafinil reviewed alongside novel wake-promoting agents |

---

## US Market Information

No FDA authorization records were returned from the regulatory database for Armodafinil.

> **⚠ Data Note**: Armodafinil (brand name **Nuvigil**, Teva Pharmaceuticals) received FDA approval in June 2007 for narcolepsy, OSA-related excessive sleepiness, and shift work disorder. The database returning 0 records indicates a data gap in the current query system. **Manual verification of the full FDA label — including approved indications, boxed warnings, and contraindications — is required before any clinical or regulatory decision-making.**

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap**: The regulatory database query returned no warnings, contraindications, or drug interaction records for Armodafinil. Given that armodafinil is a Schedule IV controlled substance in the United States, obtaining the complete FDA-approved prescribing information is a **blocking prerequisite** (DG001) before safety review can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Armodafinil's core pharmacological action — promoting wakefulness via dopamine reuptake inhibition — is directionally opposite to what insomnia treatment requires. All clinical trial evidence linking armodafinil to insomnia is indirect (cancer-related fatigue management, OSA co-morbidity, or approved-indication safety monitoring), and no trial has evaluated it as a primary treatment for primary insomnia in the general population. Proceeding without resolving the mechanistic paradox and the regulatory data gaps would be premature.

**To proceed, the following is needed:**
- Obtain and parse the FDA-approved full prescribing information (Nuvigil label) — required to complete safety review (DG001, Blocking)
- Retrieve complete mechanism of action data from DrugBank (DB06413) to determine whether any downstream effects (e.g., circadian entrainment, rebound sleep) could offer mechanistic rationale (DG002, High)
- Define a specific target patient subgroup where a wakefulness-promoting effect could paradoxically benefit sleep (e.g., hypersomnia-insomnia phenotype in circadian rhythm disorder, or cancer-related fatigue-insomnia overlap)
- Commission a dedicated literature search for armodafinil specifically in primary insomnia populations, separate from comorbid fatigue or SDB contexts
- Assess risk of insomnia worsening as a primary safety concern if repurposing is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

