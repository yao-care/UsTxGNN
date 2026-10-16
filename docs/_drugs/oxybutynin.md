---
layout: default
title: Oxybutynin
parent: Model Prediction Only (L5)
nav_order: 1004
evidence_level: L5
indication_count: 3
monitor_inn: "OXYBUTYNIN"
predicted_indications: ["restless legs syndrome", "gastroduodenitis", "peptic ulcer disease"]
last_modified_at: 2026-10-14
description: "Oxybutynin: predicted new indication Restless legs syndrome (evidence level L5). Approved use: Overactive bladder"
---

# Oxybutynin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Oxybutynin: From Overactive Bladder to Restless Legs Syndrome

## One-Sentence Summary

Oxybutynin is an antimuscarinic, antispasmodic drug originally used to treat overactive bladder and neurogenic bladder.
The TxGNN model predicts it may be effective for **Restless Legs Syndrome**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder (also neurogenic bladder and cauda equina syndrome, per the knowledge graph) |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 9 (all cancelled; these are ANDA generic approvals) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, oxybutynin is a muscarinic antagonist with musculotropic antispasmodic activity. Its efficacy in overactive bladder comes from relaxing bladder smooth muscle.

The link to restless legs syndrome is weak. This condition is mainly associated with dopaminergic dysfunction and brain iron deficiency. Anticholinergics are not an established treatment and may worsen sleep and cognition. The high TxGNN score is a computational prediction only and is not supported by a mechanistic or clinical rationale.

Two other predictions were also generated, both at Hold and with no registered trials:
- **Gastroduodenitis** (score 99.62%, L5): there is a plausible but unverified link through reduced gastrointestinal spasm and secretions. No literature was found.
- **Peptic ulcer disease** (score 99.31%, L4): the evidence is limited to a 1964 uncontrolled clinical evaluation in GI disease, a 1965 pharmacology paper, and a 1990 case report of oxybutynin-induced reflux esophagitis, which points to a possible adverse GI effect. Modern standard care (PPIs, H. pylori eradication) makes anticholinergic therapy unlikely to be competitive.

## Clinical Trial Evidence

Currently no related clinical trials registered for restless legs syndrome.

## Literature Evidence

Currently no related literature available for restless legs syndrome.

For reference, the literature found for the third-ranked prediction (peptic ulcer disease) is:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | Case report | DICP: The Annals of Pharmacotherapy | Oxybutynin-induced reflux esophagitis, probably from reduced lower esophageal sphincter tone; a management approach is outlined |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | Pharmacology review | Archives Internationales de Pharmacodynamie et de Therapie | Describes oxybutynin as a musculotropic antispasmodic with moderate anticholinergic action |
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | Clinical evaluation (uncontrolled) | Current Therapeutic Research | Historical clinical evaluation of oxybutynin chloride in gastrointestinal disease |

## US Market Information

All nine authorizations are generic (ANDA) approvals and all are cancelled. No approved indication text is available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202332 | Oxybutynin (Zydus Lifesciences) | Film-coated extended-release tablet | Not available |
| ANDA209025 | Oxybutynin Chloride (A-S Medication Solutions) | Tablet | Not available |
| ANDA209335 | Oxybutynin Chloride (Bryant Ranch Prepack) | Tablet | Not available |
| ANDA206121 | Oxybutynin Chloride (A-S Medication Solutions) | Extended-release tablet | Not available |
| ANDA207138 | Oxybutynin Chloride (Direct Rx) | Extended-release tablet | Not available |

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for safety information.

- **Knowledge-graph contraindications** (from the drug-disease network, not label text): conditions flagged include angle-closure glaucoma, myasthenia gravis, paralytic ileus, intestinal obstruction, toxic megacolon, bladder neck obstruction, benign prostatic hyperplasia, ulcerative colitis, hyperthyroidism, coronary artery disease, heart conduction disease, hypertension, kidney disease, liver disease, gallbladder disease, hiatus hernia, and gastroesophageal reflux disease with esophagitis.
- **Drug Interactions**: 100 interactions were recorded. Major-level interactions:
  - Potassium citrate
  - Potassium chloride

  Moderate-level interactions are mostly with other anticholinergic or antimuscarinic agents (e.g., atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium, propantheline), opioids (morphine, opium, loperamide), and others such as aprepitant, metoclopramide, eluxadoline, and pramlintide.
- **Relevance of the GI findings**: the 1990 case report of reflux esophagitis fits the knowledge-graph flags for gastrointestinal conditions, which argues against use in upper GI disease.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The restless legs syndrome prediction has no registered trials or literature (Evidence Level L5) and no supporting mechanism. The drug has a known anticholinergic burden, and all US licenses are cancelled. The high TxGNN score alone is not sufficient to justify advancement.

**To proceed, the following is needed:**
- Mechanism of action data, and a plausible biological rationale linking antimuscarinic activity to restless legs syndrome
- Package insert warnings and contraindications (currently a blocking data gap for safety screening)
- Preclinical or clinical signals in restless legs syndrome from literature or trial searches
- Clarification of the cancelled US market status and any available formulations for a new indication
- A review of whether the anticholinergic effects on sleep and cognition would be acceptable in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

