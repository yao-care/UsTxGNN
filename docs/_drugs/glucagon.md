---
layout: default
title: Glucagon
parent: Model Prediction Only (L5)
nav_order: 754
evidence_level: L5
indication_count: 1
monitor_inn: "GLUCAGON"
predicted_indications: ["irritable bowel syndrome"]
last_modified_at: 2026-11-04
description: "Glucagon: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Glucagon
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Glucagon: Irritable bowel syndrome
{: .text-alpha }

## One-Sentence Summary

Glucagon is a proglucagon-derived peptide hormone that is also used as a gastrointestinal smooth muscle relaxant.
The TxGNN model predicts it may be useful for **irritable bowel syndrome**, but the evidence level is **L5**: the **2 clinical trials** and **20 publications** compiled for this report study GLP-1 or GLP-1 receptor agonists, not glucagon itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 4 of 5) |
| Number of FDA Applications | 5 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glucagon is not available in the data compiled for this report. Based on known biology, glucagon comes from the same precursor (proglucagon) as GLP-1 and GLP-2, and glucagon has long been used to relax gastrointestinal smooth muscle during diagnostic procedures.

This suggests a plausible link to irritable bowel syndrome (IBS) through inhibition of gut motility, with possible effects on visceral hypersensitivity and the brain-gut axis.

This link is indirect. The clinical and literature evidence concerns GLP-1 receptor agonists and the GLP-1 analogue ROSE-010, which are different drugs from glucagon. No study found tests glucagon in IBS. The high TxGNN score (0.9924) is a computational prediction and does not replace clinical evidence for glucagon.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a GLP-1 analogue) on gastrointestinal motor function in women with constipation-predominant IBS; relevant population, but not glucagon |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 vs analogue ROSE-010 on stomach and small-bowel motility in humans; no glucagon arm, IBS population not specified |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review | Front Endocrinol | GLP-1 receptor agonists and IBS; GLP-1 and ROSE-010 inhibit gut motility in IBS patients |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic Review | J Headache Pain | GLP-1 receptor agonists in headache and pain disorders |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Clinical cross-analysis | Scand J Gastroenterol | Pain relief with ROSE-010 in IBS, by patient subgroup |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Ann Gastroenterol | Prescription and discontinuation patterns of GLP-1 receptor agonists in IBS patients |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Exp Physiol | Role of GLP-1 in IBS pathophysiology |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Adv Exp Med Biol | Aerosolized GLP-1 for diabetes and IBS |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Review | Cell Mol Gastroenterol Hepatol | Brain-gut-microbiome axis interactions |
| [31121089](https://pubmed.ncbi.nlm.nih.gov/31121089/) | 2019 | Preclinical | Neurogastroenterol Motil | GLP-1 activation of rat colonic myenteric neurons |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA201849 | Glucagon (Fresenius Kabi USA) | Lyophilized powder for injection | Not available (valid) |
| NDA212097 | Gvoke HypoPen (Xeris) | Injection, solution | Not available (valid) |
| NDA214231 | Zegalogue (Novo Nordisk) | Injection, solution | Not available (valid) |
| NDA210134 | Baqsimi (Amphastar) | Powder | Not available (valid) |
| Not numbered | Glucagon (Professional Complementary Health Formulas) | Liquid | Not available (cancelled) |

Of the 5 licence records, 4 are valid and 1 is cancelled.

---

## Safety Considerations

- **Drug Interactions**: 25 interactions were recorded, all of the Minor level among those listed. They include warfarin and a range of beta-blockers (for example atenolol, metoprolol, propranolol, carvedilol, and labetalol).

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study tests glucagon in irritable bowel syndrome. The supporting trials and publications concern GLP-1 and its analogues, which are different drugs, so the evidence level is L5. The high model score alone is not enough to advance.

**To proceed, the following is needed:**
- Direct preclinical or clinical data on glucagon in IBS
- Mechanism-of-action data for glucagon in gut motility and visceral pain
- Review of the package insert for warnings and contraindications
- Assessment of whether the available routes of administration suit a chronic condition like IBS

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

