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

Pitolisant is a histamine H3 receptor inverse agonist, marketed in the US as Wakix and used to treat excessive daytime sleepiness in narcolepsy.
The TxGNN model predicts it may be effective for **insomnia**, but only **1 clinical trial** (withdrawn, 0 participants, and not in insomnia) and **7 publications** (none showing benefit in insomnia) are linked to this prediction.
The mechanism points the opposite way, so this prediction is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Excessive daytime sleepiness in narcolepsy (per the literature; the US label text was not provided) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both entries are the same NDA211150) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pitolisant is a selective histamine H3 receptor inverse agonist. Blocking H3 autoreceptors increases histamine release in the brain and promotes wakefulness. The provided data do not include a formal mechanism-of-action entry, but the literature consistently describes this mechanism.

The original use is to reduce excessive sleepiness in narcolepsy. Insomnia is the reverse problem: too little sleep, not too much. A wake-promoting drug should not be expected to treat it, and insomnia is a known adverse effect of pitolisant. The high TxGNN score most likely reflects a knowledge-graph link between sleep-wake disorders in general, not a therapeutic relationship.

All supporting literature concerns excessive daytime sleepiness (narcolepsy, obstructive sleep apnea), not insomnia. The one listed clinical trial was withdrawn and targets alcohol use disorder. The evidence is indirect and mechanistically contradictory.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Withdrawn | 0 | Placebo-controlled trial of pitolisant in alcohol use disorder (primary endpoint: heavy drinking days). Withdrawn with no participants, so no efficacy or safety data exist. Not an insomnia trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | Lancet Neurol | Phase 3 trial of pitolisant in children aged 6 or older with narcolepsy, with or without cataplexy. Indirect to insomnia. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Pitolisant for residual excessive daytime sleepiness in OSA patients adhering to CPAP. Indirect to insomnia. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | Pitolisant for daytime sleepiness in OSA patients who refuse CPAP. Indirect to insomnia. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort | Rev Neurol | Real-life study of pitolisant in type 1 narcolepsy patients unresponsive to prior treatments. Indirect to insomnia. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Curr Neuropharmacol | Histaminergic changes in neuropsychiatric disorders. Notes pitolisant for sleepiness in narcolepsy and the H1 antagonist doxepin for insomnia. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handb Clin Neurol | Overview of histamine receptors, agonists and antagonists in health and disease. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Profile of pitolisant in narcolepsy: design, development and place in therapy. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211150 | Wakix (Harmony Biosciences, LLC) | Film-coated tablet (oral) | Indication text not provided in the data |

The data list this NDA twice with identical details; it is shown once here.

---

## Safety Considerations

- **Known adverse effect relevant to this prediction**: Insomnia is a recognized adverse effect of pitolisant, so treating insomnia with it would work against its own safety profile.
- **Drug Interactions**: No interaction records were found in the queried data.

Please refer to the package insert for full safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted benefit in insomnia contradicts pitolisant's wake-promoting mechanism, and insomnia is a known adverse effect. The only linked trial was withdrawn and was not in insomnia, and the supporting literature addresses daytime sleepiness rather than insomnia.

**Other predictions in this pack (for context):**
- **Attention deficit-hyperactivity disorder** (score 99.36%, L4): plausible through H3-mediated increases in dopamine, acetylcholine and norepinephrine, but supported only by reviews and preclinical discussion, with no clinical trial or human efficacy data. This is a research question, not a clinical recommendation.
- **Faciodigitogenital syndrome** (score 99.29%, L5): no mechanistic rationale, trials or literature. Hold.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications and approved indication text) to complete safety screening
- A formal mechanism-of-action entry (e.g., from DrugBank)
- Any direct clinical evidence of pitolisant in insomnia. If none exists, deprioritize this indication.

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

