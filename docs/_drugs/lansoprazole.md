---
layout: default
title: Lansoprazole
parent: Moderate Evidence (L3-L4)
nav_order: 835
evidence_level: L4
indication_count: 2
---

# Lansoprazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Lansoprazole: From Acid-Related Upper GI Disease to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor, a drug class used mainly for acid-related upper gastrointestinal conditions such as peptic ulcer and gastro-oesophageal reflux disease.
The TxGNN model predicts it may be effective for **duodenogastric reflux**, but there are **0 clinical trials** and only **2 publications** (one rat study, one general review) for this direction.
The only disease-specific study is an animal study that raises a safety concern rather than supporting efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acid-related upper GI disease (general PPI class use; the US license records supplied contain no indication text) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not supplied with this record. Lansoprazole is generally known as a proton pump inhibitor (H+/K+ ATPase inhibitor) that suppresses gastric acid secretion. The general review in the evidence (Shi & Klotz, 2008) describes PPIs as first-choice drugs for peptic ulcer, *Helicobacter pylori* infection, gastro-oesophageal reflux disease, NSAID-related GI injury and Zollinger-Ellison syndrome.

Duodenogastric reflux is the backflow of duodenal contents (bile and pancreatic juice) into the stomach. Acid suppression could plausibly reduce the acid part of the mucosal injury. It does not treat the reflux itself, because it has no effect on pyloric function or gastric motility. The very high TxGNN score most likely reflects proximity to acid-related diseases in the knowledge graph, not proof of a treatment effect.

The only disease-specific study is a 2004 rat study reporting that lansoprazole promoted gastric carcinogenesis in the setting of duodenogastric reflux. This is a preclinical safety signal that would need to be resolved before any repurposing effort.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | Update on PPI clinical use and pharmacokinetics; PPIs are first-choice drugs for peptic ulcer, *H. pylori* infection, GERD, NSAID-related GI lesions and Zollinger-Ellison syndrome. It does not address duodenogastric reflux specifically. |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal study (rat) | Gastric Cancer | Examined the combined effect of duodenogastric reflux and acid inhibition on gastric cancer development; the title reports that lansoprazole promoted gastric carcinogenesis in rats with reflux. |

## US Market Information

The license records supplied contain no approved-indication text. The table below lists 5 of the 20 authorizations.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021428 | Prevacid SoluTab | Tablet, orally disintegrating, delayed release | Takeda Pharmaceuticals America, Inc. |
| ANDA202366 | Lansoprazole | Capsule, delayed release pellets | Bryant Ranch Prepack |
| ANDA200816 | Lansoprazole | Tablet, orally disintegrating | Zydus Pharmaceuticals USA Inc. |
| ANDA205868 | Lansoprazole | Capsule, delayed release | Preferred Pharmaceuticals, Inc. |
| ANDA205868 | Lansoprazole | Capsule, delayed release | NuCare Pharmaceuticals, Inc. |

## Safety Considerations

- **Preclinical signal**: A rat study (PMID 15052437) reported that lansoprazole promoted gastric carcinogenesis in the presence of duodenogastric reflux. Its relevance to humans is unknown.
- **Drug interactions**: The interaction query returned no records, which does not confirm the absence of interactions.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is at the model-prediction and preclinical level (L4), with no registered clinical trials for this indication. Acid suppression does not address the underlying reflux, and the only disease-specific study is an animal safety signal.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, to allow safety screening
- Mechanism-of-action data from DrugBank to support a mechanistic-link analysis
- Review of the rat study's full text and its relevance to human risk
- Full-record review of NCT00175032, whose target condition is unconfirmed, before any weight is placed on it
- A clinical rationale showing a benefit of PPIs in duodenogastric reflux (for example, symptom or mucosal injury endpoints) beyond general acid suppression

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

