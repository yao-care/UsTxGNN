---
layout: default
title: Oxybutynin
parent: Model Prediction Only (L5)
nav_order: 1004
evidence_level: L5
indication_count: 3
monitor_inn: "OXYBUTYNIN"
predicted_indications: ["restless legs syndrome", "gastroduodenitis", "peptic ulcer disease"]
last_modified_at: 2026-11-24
description: "Oxybutynin: predicted new indication Restless legs syndrome (evidence level L5). In the US: 43 FDA applications (25 active)"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Oxybutynin: Restless legs syndrome
{: .text-alpha }

## One-Sentence Summary

Oxybutynin is an antimuscarinic, antispasmodic drug originally used to treat overactive bladder and neurogenic bladder.
The TxGNN model predicts it may be effective for **Restless Legs Syndrome**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 25 of 43) |
| Number of FDA Applications | 43 (active: 25) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for oxybutynin: "Oxybutynin relaxes bladder smooth muscle. Oxybutynin chloride exerts a direct antispasmodic effect on smooth muscle and inhibits the muscarinic action of acetylcholine on smooth muscle. No blocking effects occur at skeletal neuromuscular junctions or autonomic ganglia (antinicotinic effects)." ([DailyMed: Oxybutynin Chloride Extended Release (oxybutynin chloride) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5653b7e-1e3b-4da3-b3a2-33318f448c67), label version 2026-11-11; accessed 2026-11-19.) Based on known information, oxybutynin is a muscarinic antagonist with musculotropic antispasmodic activity. Its efficacy in overactive bladder comes from relaxing bladder smooth muscle.

The link to restless legs syndrome is weak. This condition is mainly associated with dopaminergic dysfunction and brain iron deficiency. Anticholinergics are not an established treatment and may worsen sleep and cognition. The high TxGNN score is a computational prediction only and is not supported by a mechanistic or clinical rationale.

Two other predictions were also generated, both at Hold and with no registered trials:
- **Gastroduodenitis** (score 0.9962, L5): there is a plausible but unverified link through reduced gastrointestinal spasm and secretions. No literature was found.
- **Peptic ulcer disease** (score 0.9931, L4): the evidence is limited to a 1964 uncontrolled clinical evaluation in GI disease, a 1965 pharmacology paper, and a 1990 case report of oxybutynin-induced reflux esophagitis, which points to a possible adverse GI effect. Modern standard care (PPIs, H. pylori eradication) makes anticholinergic therapy unlikely to be competitive.

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

The drug is marketed in the US. No approved indication text is available.

<!-- review:begin us-lic-20261106-oxybutynin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US with 9 valid licenses." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-oxybutynin-2 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA071655 | OXYBUTYNIN CHLORIDE | TEVA PHARMS USA | Tablet; oral | Valid |
| ANDA074520 | OXYBUTYNIN CHLORIDE | LANNETT CO INC | Syrup; oral | Valid |
| ANDA074625 | OXYBUTYNIN CHLORIDE | AIPING PHARM INC | Tablet; oral | Valid |
| ANDA075039 | OXYBUTYNIN CHLORIDE | CHARTWELL RX | Syrup; oral | Valid |
| ANDA075079 | OXYBUTYNIN CHLORIDE | STRIDES PHARMA INTL | Tablet; oral | Valid |

Showing 5 of 43 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

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
The restless legs syndrome prediction has no registered trials or literature (Evidence Level L5) and no supporting mechanism. The drug has a known anticholinergic burden, and it is marketed in the US. The high TxGNN score (0.9974) alone is not sufficient to justify advancement.

<!-- review:begin us-lic-20261106-oxybutynin-3 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug has a known anticholinergic burden, and it is marketed in the US with 9 valid licenses." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-oxybutynin-3 -->

**To proceed, the following is needed:**
- Mechanism of action data, and a plausible biological rationale linking antimuscarinic activity to restless legs syndrome
- Package insert warnings and contraindications (currently a blocking data gap for safety screening)
- Preclinical or clinical signals in restless legs syndrome from literature or trial searches
- Clarification of any available formulations for a new indication
- A review of whether the anticholinergic effects on sleep and cognition would be acceptable in this population

<!-- review:begin us-lic-20261106-oxybutynin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the cancelled US market status and any available formulations for a new indication" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-oxybutynin-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "the cancelled US market status and" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 9 valid licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 9 valid licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Oxybutynin Chloride Extended Release (oxybutynin chloride) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5653b7e-1e3b-4da3-b3a2-33318f448c67) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

