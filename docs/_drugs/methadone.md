---
layout: default
title: Methadone
parent: Moderate Evidence (L3-L4)
nav_order: 906
evidence_level: L4
indication_count: 7
monitor_inn: "METHADONE"
predicted_indications: ["Tourette syndrome", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "headache disorder", "manic bipolar affective disorder", "trigeminal autonomic cephalalgia", "common cold"]
last_modified_at: 2026-10-28
description: "Methadone: predicted new indication Tourette syndrome (evidence level L4). Approved use: Not recorded in the local data"
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
| US Market Status | Marketed (valid licenses on record: at least 16) |
| Number of NDAs | 16 licenses (1 NDA, 15 ANDAs), all cancelled |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Methadone is a mu-opioid receptor agonist and also an NMDA receptor antagonist. Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known pharmacology, opioid signalling can modulate dopaminergic and striatal circuits, which are thought to be involved in tic expression.

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

All 16 licenses are valid, and no approved-indication text is recorded. Five representative licenses are listed below.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

