---
layout: default
title: Atropine
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 2
---

# Atropine
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

Using the `txgnn-pipeline` skill — this task involves generating a drug repurposing evaluation report from a TxGNN evidence pack.

---

# Atropine: From Anticholinergic Agent to Migraine Disorder

## One-Sentence Summary

Atropine is a classic muscarinic receptor antagonist, historically established for reversing bradycardia, treating organophosphate poisoning, and reducing presurgical secretions.
The TxGNN model predicts it may be effective for **migraine disorder** (score: 99.56%), supported by **0 clinical trials** and **13 publications** that explore the cholinergic system's role in migraine pathophysiology.
However, the mechanistic evidence points in two opposing directions — peripheral parasympathetic blockade may reduce neurogenic inflammation, while central muscarinic blockade may paradoxically impair endogenous pain relief — leaving the net clinical effect in humans unresolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bradycardia; Organophosphate Poisoning (per known pharmacology; no regulatory records in this dataset) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 — Preclinical and mechanistic studies only |
| Taiwan Market Status | ✗ 未上市 (Not Marketed) |
| Number of Approved Products | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atropine competitively blocks acetylcholine at muscarinic receptors (M1–M5) across both the peripheral and central nervous systems. Its established clinical utility stems from this mechanism: it reverses parasympathetic-mediated bradycardia, counteracts organophosphate-induced cholinergic excess, and reduces glandular secretions. Detailed MOA data is not available in this evidence pack, so the mechanistic analysis below draws on published pharmacology and the provided literature.

The hypothesized therapeutic pathway centers on the autonomic nervous system's role in migraine. The sphenopalatine ganglion (SPG) is a major parasympathetic relay in the cranial region whose activation drives meningeal vasodilation, mast cell degranulation, and plasma protein extravasation in the dura mater — core events in trigeminal pain sensitization. Atropine's blockade of muscarinic receptors could theoretically suppress this SPG-driven neuroinflammatory cascade, reducing the nociceptive input that initiates migraine headache (PMID 9344563, PMID 36485173). Clinical support for autonomic involvement appears in observations that systemic atropine markedly reduced attack-related autonomic features (sweating, tearing, nasal secretion) in patients with chronic paroxysmal hemicrania (PMID 2943405).

Critically, a competing mechanism constrains enthusiasm. The central cholinergic system actively mediates endogenous antinociception: studies show the antimigraine drug sumatriptan elevates extracellular acetylcholine in the hippocampus, and its antinociceptive effect is fully abolished by atropine pretreatment (PMID 8930196). This means atropine could paradoxically worsen central pain processing by silencing a natural analgesic pathway. The second predicted indication — **migraine with brainstem aura** — carries an additional concern: cholinergic activation suppresses cortical spreading depression (CSD), the electrophysiological event underlying migraine aura (PMID 31945385). Blocking this cholinergic brake with atropine may facilitate CSD propagation, which is particularly hazardous in brainstem aura. Until the net balance between these peripheral and central effects is quantified in an appropriate human or validated animal model, the repurposing hypothesis for migraine remains scientifically open but clinically uncommittable.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Atropine in migraine disorder or migraine with brainstem aura.

---

## Literature Evidence

*Ranked by relevance to the Atropine × Migraine repurposing hypothesis.*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Basic Science (In vivo/In vitro) | European Journal of Neuroscience | Muscarinic antagonism modulates meningeal mast cell activation and neurogenic dural inflammation in a nitroglycerin-induced rat migraine model; directly implicates the cholinergic/muscarinic axis as a mechanistic lever in migraine |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Animal Study (In vivo Rat) | Experimental Neurology | SPG parasympathetic stimulation induces plasma protein extravasation in rat dura mater, establishing the parasympathetic→neuroinflammation pathway that atropine could theoretically suppress |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical Case Series | Cephalalgia | In 4 chronic paroxysmal hemicrania patients, systemic atropine markedly reduced attack-related autonomic features (sweating, tearing, nasal secretion), providing rare direct human evidence of cholinergic involvement in headache attacks |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Animal Study | J Pharmacol Exp Ther | Sumatriptan's antinociceptive effect is mediated via central cholinergic activation; atropine pretreatment abolished this effect — key evidence that blocking muscarinic receptors undermines pain relief in migraine pharmacology |
| [31945385](https://pubmed.ncbi.nlm.nih.gov/31945385/) | 2020 | Animal Study (Mouse In vivo Electrophysiology) | Neuropharmacology | Cholinergic activation via mAChR suppresses cortical spreading depression (CSD) in mouse neocortex; atropine (mAChR blocker) would remove this brake, potentially promoting CSD and worsening migraine aura |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | In vitro (Isolated Vessel Preparation) | British Journal of Pharmacology | Atropine (3 µM) used to isolate nicotinic effects in guinea-pig basilar artery; reveals complex cholinergic-vasomotor interplay relevant to migraine cerebrovascular changes |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Pharmacology Study | Neuroscience Letters | Centrally evoked facial blood flow changes involve CGRP and nicotinic receptor activation; distinguishes nicotinic from muscarinic pathways and contextualises where atropine would and would not act in the trigeminal circuit |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | Journal of Applied Toxicology | Pharmacological review of anisodamine, a naturally occurring atropine derivative with the same anticholinergic spectrum but less potency and lower CNS toxicity; useful comparator for assessing whether a less CNS-penetrant analogue might have a more favourable therapeutic window for migraine |

---

## Taiwan Market Information

No approved drug products for Atropine were found in the Taiwan regulatory database (TFDA).

**Taiwan market status: 未上市 (Not Marketed)** — 0 approved product licences on record.

> Note: Atropine has well-established regulatory approval in other markets (e.g., the United States and the European Union) for bradycardia, organophosphate poisoning, and related anticholinergic indications. This section reflects only data from the Taiwan regulatory query conducted for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No Taiwan-specific warnings, contraindications, or drug interaction data were available in this evidence pack. Formal safety review of the full prescribing information is a prerequisite before any further development steps.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Atropine's peripheral anticholinergic mechanism offers a biologically plausible but unproven pathway for migraine relief (SPG blockade → reduced dural neuroinflammation); however, this is directly counterbalanced by evidence that central muscarinic blockade impairs endogenous antinociception and may facilitate the cortical spreading depression that drives migraine aura. With zero clinical trials, only L4-level preclinical and mechanistic literature, and no validated net-effect data in a human-relevant system, proceeding to any clinical stage would be premature.

**To proceed, the following is needed:**

- **Preclinical go/no-go experiment**: Run atropine vs. vehicle in a validated migraine animal model (e.g., nitroglycerin-induced allodynia model) with quantitative pain endpoints to determine whether the peripheral anti-inflammatory or central pro-nociceptive effect dominates
- **Route-of-administration strategy**: Evaluate whether peripheral-restricted delivery (e.g., intranasal SPG-targeted administration) could deliver parasympathetic blockade while limiting CNS penetration and preserving central antinociceptive tone
- **Receptor subtype mapping**: Clarify which muscarinic subtypes (M1/M3 in meningeal tissue vs. M2/M4 centrally) are most functionally relevant to each side of the bidirectional hypothesis
- **Safety review**: Obtain and formally review the full atropine package insert (warnings, contraindications, DDI profile) before any progression decision — currently a blocking data gap
- **Brainstem aura sub-indication (Rank 2)**: Rated **Hold (S0)** separately; the CSD-promoting risk from muscarinic blockade requires explicit mechanistic resolution before this sub-indication can be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

