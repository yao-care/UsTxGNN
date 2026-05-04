---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 2
---

# Baclofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist classically established for the treatment of muscle spasticity and spasms.
The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**,
currently supported by **0 registered clinical trials** and **10 publications** (primarily animal studies and reviews focused on comorbid conditions).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not found in dataset (established pharmacological use: muscle spasticity) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 |
| US Market Status | Not found in dataset (may reflect a data gap) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Baclofen is a selective GABA-B receptor agonist. The repurposing rationale proposes that by activating GABA-B receptors in the prefrontal cortex and ventral tegmental area, Baclofen indirectly modulates dopamine and norepinephrine signaling — the two neurotransmitter systems central to ADHD pathophysiology. Animal studies in spontaneously hypertensive rats (SHR), a validated ADHD model, have shown that GABA-B agonism alters cortical and hippocampal EEG patterns in ways that partially resemble ADHD neurophysiology (PMID 21300040), providing limited but mechanistically plausible preclinical support.

However, this link remains indirect and speculative. Established ADHD pharmacotherapy (methylphenidate, amphetamines, atomoxetine) targets dopamine and norepinephrine directly, whereas Baclofen's route is inhibitory modulation via GABAergic pathways. The mechanistic leap from spasticity treatment to ADHD is substantial and lacks human clinical validation.

It is important to note that the TxGNN model's high score (99.32%) likely reflects knowledge graph edges connecting Baclofen to Tourette syndrome — a condition highly comorbid with ADHD — rather than direct evidence of efficacy in ADHD itself. Several literature entries in this Evidence Pack discuss Baclofen explicitly for tic suppression in Tourette syndrome, and the ADHD connection appears to be inherited through this comorbidity relationship rather than through independent study of ADHD as a primary indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Baclofen in ADHD.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review | Cureus | Systematic review of treatments for tics in Tourette syndrome (frequently comorbid with ADHD); behavioral interventions, antipsychotics, and alpha agonists reviewed — Baclofen discussed as a supportive option for tic management |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Review | Clinical Neuropharmacology | Review of mood stabilizers in children/adolescents with autism spectrum disorders; attention-deficit symptoms addressed as a behavioral comorbidity target |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | International Review of Neurobiology | Emerging therapies for Tourette syndrome; Baclofen discussed in context of tic suppression within a disorder that carries high ADHD comorbidity rates |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | Journal of Child Neurology | Uncontrolled study of 450 patients with tics/Tourette syndrome treated with baclofen and botulinum toxin A; symptoms rated via Yale Global Tic Severity Scale — largest clinical dataset involving Baclofen in this comorbid population |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal Study | Brain Research | EEG responses to neurotransmitter agonists in SHR (ADHD model) vs. kainate-treated and normotensive rats; GABA-B agonism shown to alter cortical/hippocampal EEG — the most mechanistically relevant preclinical entry for this indication |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatric Drugs | Clinical management of Tourette syndrome; Baclofen listed as a pharmacological option for tic suppression alongside clonidine and dopamine antagonists |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Clinical Review | L'Encéphale | Review of supervised off-label methylphenidate prescribing in adult ADHD; contextualizes the off-label prescribing landscape relevant to any new candidate for this indication |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal Study | Psychopharmacology | Noradrenergic α2A stimulation in ventral hippocampus reduces impulsive decision-making in rats; relevant to understanding neurotransmitter modulation approaches for ADHD-like impulsivity |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Animal Study | Neuropsychopharmacology | Anterior cingulate cortex and amygdala contributions to cognitive effort decision-making; deficits in this domain are characteristic of ADHD, schizophrenia, and depression |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Animal Study | European Journal of Neuroscience | Habenular integrity and social play in rats; monoaminergic modulation context — indirect mechanistic background for neurodevelopmental disorders |

---

## US Market Information

No FDA authorizations were found in the current dataset for Baclofen.

> **Note:** Baclofen is a well-established pharmaceutical compound with a long history of clinical use. The absence of records in this Evidence Pack most likely reflects a data gap in the current pipeline rather than actual non-approval status. Independent verification via the FDA Orange Book is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN high-confidence prediction for ADHD appears to be driven primarily by Baclofen's knowledge graph proximity to Tourette syndrome (a comorbid condition) rather than by direct clinical evidence in ADHD. With zero registered clinical trials and only animal/indirect literature support, the current evidence base is insufficient to justify advancing this repurposing candidate without foundational data generation.

> **Secondary Signal Worth Noting:** Baclofen's rank-2 prediction — **nicotine dependence** — carries substantially stronger evidence (L2: 3 Phase 2 clinical trials, 20 publications) and a mechanistically direct rationale (VTA GABA-B → dopamine suppression in reward circuitry). If resources for this drug are to be prioritized, the nicotine dependence indication represents a more tractable near-term opportunity.

**To proceed with the ADHD indication, the following is needed:**

- **MOA data**: Confirm whether Baclofen's GABAergic mechanism produces measurable prefrontal dopamine/norepinephrine modulation in humans at clinically tolerated doses
- **Exploratory clinical study**: At minimum a Phase 1/2 proof-of-concept trial in ADHD patients (adults or pediatric) with validated ADHD rating scales as endpoints
- **Knowledge graph audit**: Clarify whether the TxGNN score derives from direct ADHD edges or from Tourette comorbidity paths — this affects interpretation of model confidence
- **Regulatory verification**: Confirm US FDA approval status via the Orange Book; retrieve full prescribing information including warnings, contraindications, and DDI profile
- **Safety package**: Obtain full package insert data before any clinical or regulatory submission — currently no safety data is available in this Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

