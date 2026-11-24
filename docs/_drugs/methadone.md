---
layout: default
title: Methadone
parent: Moderate Evidence (L3-L4)
nav_order: 906
evidence_level: L4
indication_count: 7
monitor_inn: "METHADONE"
predicted_indications: ["Tourette syndrome", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "headache disorder", "manic bipolar affective disorder", "trigeminal autonomic cephalalgia", "common cold"]
last_modified_at: 2026-11-20
description: "Methadone: predicted new indication Tourette syndrome (evidence level L4). In the US: 34 FDA applications (26 active)"
---

# Methadone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

## Methadone: Tourette syndrome
{: .text-alpha }

## One-Sentence Summary

Methadone is a long-acting opioid agonist used for opioid dependence and pain management, though the US regulatory data compiled for this report contain no approved-indication text.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but there are currently **0 registered clinical trials** and only **4 publications**, of which only one is a directly relevant 1992 case report or small series.
This direction rests mainly on a computational prediction, and the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L4 |
| US Market Status | Marketed (active FDA-approved applications: 26 of 34) |
| Number of FDA Applications | 34 (active: 26) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Methadone is a mu-opioid receptor agonist and also an NMDA receptor antagonist. According to the Mechanism of Action section of the FDA-approved prescribing information for methadone: "Methadone hydrochloride is a mu-agonist; a synthetic opioid with multiple actions qualitatively similar to those of morphine, the most prominent of which involves the central nervous system and organs composed of smooth muscle. The methadone withdrawal syndrome, although qualitatively similar to that of morphine, differs in that the onset is slower, the course is more prolonged, and the symptoms are less severe." ([DailyMed: Methadose Dispersible (methadone hydrochloride) prescribing information, SpecGx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=544483e6-6f9d-4371-9e93-313e54e0ea05), label version 2026-08-04; accessed 2026-11-19.) Based on known pharmacology, opioid signalling can modulate dopaminergic and striatal circuits, which are thought to be involved in tic expression.

The literature offers some indirect support. A 2007 preclinical review notes that opiate drugs have been reported to be effective in treatment-refractory obsessive-compulsive disorder and Tourette syndrome. A 1992 report in the *American Journal of Psychiatry* describes methadone treatment of Tourette's disorder. However, this is a very old, small observation with no modern replication.

The very high TxGNN score (0.9976) is a computational prediction only. It should not be read as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1728167](https://pubmed.ncbi.nlm.nih.gov/1728167/) | 1992 | Case report / small clinical series | Am J Psychiatry | Reports methadone treatment of Tourette's disorder (no abstract available) |
| [17102981](https://pubmed.ncbi.nlm.nih.gov/17102981/) | 2007 | Preclinical / experimental | Psychopharmacology | Atypical opiates in OCD via 5-HT2A/C receptor-mediated behaviour; notes opiates are effective in treatment-refractory OCD and Tourette syndrome |
| [15247538](https://pubmed.ncbi.nlm.nih.gov/15247538/) | 2004 | Review | Curr Opin Neurol | Review of non-genetic causes of chorea; only indirectly related |
| [39086469](https://pubmed.ncbi.nlm.nih.gov/39086469/) | 2024 | Review | Palliat Care Soc Pract | Novel drugs for neuropathic pain in advanced cancer; not disease-specific |

---

## US Market Information

Five representative licenses are listed below.

<!-- review:begin us-lic-20261105-methadone-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All 16 licenses are valid, and no approved-indication text is recorded. Five representative licenses are listed below." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-methadone-1 -->

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017058 | DISKETS (Hikma) | Tablet | Not available (valid) |
| ANDA074184 | METHADOSE DISPERSIBLE (SpecGx) | Tablet | Not available (valid) |
| ANDA218609 | Methadone Hydrochloride (Hikma) | Injection | Not available (valid) |
| ANDA089897 | Methadone Hydrochloride (Hikma) | Concentrate | Not available (valid) |
| ANDA087393 | Methadone Hydrochloride (Precision Dose) | Solution | Not available (valid) |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for label safety information.

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, respiratory failure, epilepsy, asthma, kidney disease, liver disease, gallbladder disease, hypothyroidism, inflammatory bowel disease, paralytic ileus, intestinal obstruction, hypotensive disorder, intracranial hypertension, benign prostatic hyperplasia, substance-related disorder, and others.
- **Drug Interactions**: 100 interactions were identified. Major interactions among those reviewed include alvimopan, bupropion, morphine, dexamethasone, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes), and cisapride. Moderate interactions include famotidine, hyoscyamine, loperamide, aprepitant, atropine, cimetidine, and several anticholinergics and laxatives.
- **Literature signals**: methadone-induced bradycardia has been reported, and the cardiac (QT) risk is consistent with the TxGNN model (deep learning) signals above, which may reflect similarities the model learned between related diseases, not biological evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction has a high model score but little real-world support: no registered trials, and only a 1992 small report with no modern replication.

**To proceed, the following is needed:**
- Complete FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- Confirmation of the original approved indications and current US marketing status
- Review of the 1992 report and any newer clinical data in Tourette syndrome, then a feasibility assessment for a well-designed controlled study
- A cardiac (QT) and respiratory safety plan, and an assessment of dependence and abuse risk in a young Tourette population

---

*Note on other predicted indications:* nephrogenic syndrome of inappropriate antidiuresis (score 0.9973) and trichotillomania (0.9967) have no supporting evidence. Headache disorder (0.9935) and trigeminal autonomic cephalalgia (0.9905) have literature suggesting that opioids are discouraged or may worsen headache. Manic bipolar affective disorder (0.9932) has only a small 1982 study and indirect literature. For common cold (0.9902), the literature matches came from the "cold pressor" pain test rather than the infection, so it has no real support. All of these remain at **Hold**.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All 16 licenses are valid, and no approved-indication text is recorded" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Methadose Dispersible (methadone hydrochloride) prescribing information, SpecGx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=544483e6-6f9d-4371-9e93-313e54e0ea05) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

