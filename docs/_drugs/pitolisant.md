---
layout: default
title: Pitolisant
parent: Moderate Evidence (L3-L4)
nav_order: 1052
evidence_level: L4
indication_count: 3
---

# Pitolisant
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pitolisant: From Narcolepsy to Insomnia

## One-Sentence Summary

Pitolisant is a histamine H3 receptor inverse agonist, originally used to treat narcolepsy (with or without cataplexy).
The TxGNN model predicts it may be effective for **Insomnia**, but there are **0 registered clinical trials** and **no publications that directly address insomnia treatment**. The prediction rests on model scoring alone, and the mechanism points the opposite way (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy (the US licence record lists no indication text; this is taken from the knowledge-graph indications) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. From the literature, pitolisant is a selective histamine H3 receptor antagonist/inverse agonist. It increases histaminergic neurotransmission in the brain and promotes wakefulness, which is why it is used for excessive daytime sleepiness in narcolepsy.

This is where the prediction becomes doubtful. Insomnia treatment aims to promote sleep, whereas pitolisant promotes wakefulness. Blocking H3 receptors could plausibly worsen insomnia, and insomnia is a known adverse effect of the drug. The high TxGNN score (0.997) most likely reflects a graph-based association between pitolisant and sleep-wake disorders in general, rather than a true therapeutic signal.

The available literature concerns narcolepsy and residual daytime sleepiness in obstructive sleep apnoea, not insomnia treatment. The prediction should therefore be regarded as a likely false positive until shown otherwise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications studies pitolisant as a treatment for insomnia. They are listed because they are the closest available sleep-medicine evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT (Phase 3) | The Lancet. Neurology | Double-blind, placebo-controlled trial of safety and efficacy in children aged 6 years or older with narcolepsy, with or without cataplexy |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Residual excessive daytime sleepiness in OSA patients adhering to CPAP (not insomnia) |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | Daytime sleepiness in OSA patients who refuse CPAP (not insomnia) |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Real-world study | Revista de Neurologia | Effectiveness and safety in type 1 narcolepsy patients unresponsive to or intolerant of previous treatments |
| [41588264](https://pubmed.ncbi.nlm.nih.gov/41588264/) | 2026 | Real-world study | Neurological Sciences | Retrospective study of 40 Chinese paediatric narcolepsy patients treated with pitolisant |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Profile of pitolisant in narcolepsy: design, development and place in therapy |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | Histaminergic changes in neuropsychiatric disorders; mentions pitolisant for narcolepsy sleepiness and doxepin (an H1 antagonist) for insomnia |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | Histamine receptors, agonists and antagonists in health and disease |
| [42525367](https://pubmed.ncbi.nlm.nih.gov/42525367/) | 2026 | Review | Neurology and Therapy | Current and emerging therapies for paediatric sleep disorders |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review | Clinical Neuropharmacology | Pitolisant as an alternative stimulant for narcolepsy-cataplexy in teenagers with refractory sleepiness |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211150 (cancelled) | Wakix (Harmony Biosciences, LLC) | Film-coated tablet (oral) | Not listed in the licence record |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. Two of the 20 shown are rated **Major**: **bupropion** and **dolasetron**. The others shown are rated Moderate, including famotidine, hydrocortisone, metformin, loperamide, triamcinolone, morphine, acetylsalicylic acid, dexamethasone, betamethasone, bisacodyl, budesonide, cimetidine, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes), eliglustat, empagliflozin and methylnaltrexone.
- **Adverse effect relevant to this prediction**: insomnia is a known adverse effect of pitolisant (noted in the literature review).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials and no insomnia-specific literature. The wake-promoting mechanism runs opposite to what insomnia treatment requires, and insomnia is a recognised side effect of the drug. The evidence level is L4.

**To proceed, the following is needed:**
- A clear mechanistic rationale showing why H3 inverse agonism could help insomnia, or confirmation that the prediction is an artefact of the knowledge graph
- Any preclinical or clinical data on pitolisant in insomnia populations
- The FDA package insert warnings and contraindications, to complete safety screening
- Detailed mechanism-of-action data from DrugBank
- Clarification of why the US Wakix licence (NDA211150) is recorded as cancelled

---

## Other Predicted Indications (for reference)

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|------|
| 2 | Attention deficit-hyperactivity disorder | 99.36% | L4 | Research Question | H3 antagonism increases histamine, acetylcholine, dopamine and norepinephrine release in cortical circuits, which gives a plausible basis for effects on attention. No ADHD-specific trials exist, and the literature is review-level. A dedicated proof-of-concept trial would be needed, with attention to insomnia, anxiety and QT considerations. |
| 3 | Faciodigitogenital syndrome (Aarskog-Scott syndrome) | 99.29% | L5 | Hold | No plausible mechanistic link, no trials and no literature. This is a computational prediction only. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

