---
layout: default
title: Atropine
parent: Model Prediction Only (L5)
nav_order: 428
evidence_level: L5
indication_count: 2
monitor_inn: "ATROPINE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
last_modified_at: 2026-10-30
description: "Atropine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available"
---

# Atropine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Atropine: From Anticholinergic Use (Original Indication Not Specified) to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Atropine is a non-selective muscarinic (anticholinergic) antagonist. The data compiled for this report do not list a specific original indication.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 registered clinical trials** and the **10 retrieved publications** are mostly indirect (preclinical, unrelated, or adverse-event reports); none shows that atropine itself treats migraine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is blank in all US license records) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9956 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 13) |
| Number of FDA Applications | 13 (all cancelled) |
| Recommended Decision | Hold |

A second prediction, **migraine with brainstem aura** (score 0.9942, Evidence Level L5, Hold), is covered briefly in the sections below.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, atropine is a non-selective muscarinic cholinergic antagonist, and the link to migraine is mechanistically plausible but unproven.

Preclinical studies suggest that the parasympathetic and cholinergic systems are involved in migraine biology. Cholinergic modulation affects meningeal mast cell-mediated neurogenic inflammation in a rat migraine model. Stimulating the parasympathetic sphenopalatine ganglion causes plasma protein extravasation in rat dura mater. A cholinergic role in antinociception has also been reported in rodents. Blocking muscarinic receptors could therefore, in theory, dampen these pathways in the trigeminovascular system.

The evidence stops there. No study shows that atropine treats or prevents migraine. For the brainstem aura subtype, the only supporting paper is a mouse study in which muscarinic receptor *activation* inhibited cortical spreading depression. A muscarinic antagonist such as atropine could therefore act in the opposite direction, so the direction of effect is unresolved.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Of the 10 publications retrieved for migraine disorder, only the first four rows are relevant to atropine or cholinergic mechanisms; the remainder are unrelated and are omitted from the table.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical (rat) | Eur J Neurosci | Cholinergic modulation and meningeal mast cells contribute to neurogenic inflammation in a nitroglycerin-induced migraine model |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical (rat) | Exp Neurol | Parasympathetic sphenopalatine ganglion stimulation induces dural plasma protein extravasation |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical observation (4 patients) | Cephalalgia | In chronic paroxysmal hemicrania (not migraine), systemic atropine markedly reduced attack-related sweating, tearing and nasal secretion |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Pharmacology of anisodamine, an atropine derivative and non-specific cholinergic antagonist; no migraine efficacy data for atropine |
| [31945385](https://pubmed.ncbi.nlm.nih.gov/31945385/) | 2020 | Preclinical (mouse) | Neuropharmacology | For migraine with brainstem aura: muscarinic receptor activation inhibits cortical spreading depression, a hypothesis-generating finding with an uncertain direction for atropine |

## US Market Information

All 13 US licenses are valid, and none has approved indication text on record. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208151 | Isopto Atropine | Solution | Not available |
| NDA021146 | Atropine Sulfate (Hospira) | Injection, solution | Not available |
| ANDA215342 | Atropine sulfate (Amneal) | Injection, solution | Not available |
| ANDA218148 | Atropine Sulfate (Redpharm) | Solution/drops | Not available |
| ANDA214752 | Atropine (Amneal NY) | Solution/drops | Not available |

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. The sample reviewed includes mostly Moderate-level interactions, with a few Minor. Main ones include:
  - Other anticholinergics and antimuscarinics: aclidinium, hyoscyamine, amitriptyline, chlorpheniramine, acrivastine, phenyltoloxamine (additive anticholinergic effects)
  - Opioids and CNS depressants: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, ethanol
  - Cholinergic agents (opposing effects): acetylcholine, galantamine
  - Others: botulinum toxin type A, acebutolol, amantadine, loperamide
- **Class effects to consider for any chronic use**: antimuscarinic adverse effects such as dry mouth, blurred vision, tachycardia and cognitive effects.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the evidence is model prediction plus indirect preclinical findings, with no clinical trials and no human data for atropine in migraine. The drug is marketed in the US with 13 valid licenses, and the mechanistic direction is uncertain for the aura subtype.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication information
- Preclinical or early clinical studies testing atropine (or a muscarinic antagonist) directly in migraine models
- Assessment of route and formulation feasibility, and of the tolerability of chronic antimuscarinic exposure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

