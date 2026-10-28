---
layout: default
title: Alprazolam
parent: Model Prediction Only (L5)
nav_order: 268
evidence_level: L5
indication_count: 3
monitor_inn: "ALPRAZOLAM"
predicted_indications: ["insomnia (disease)", "benign paroxysmal torticollis of infancy", "agoraphobia"]
last_modified_at: 2026-10-27
description: "Alprazolam: predicted new indication insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Alprazolam
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

## Alprazolam: Benzodiazepine (GABA-A receptor modulator) → insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Alprazolam is a benzodiazepine that has been used mainly in anxiety-related conditions.
The TxGNN model predicts it may be effective for **insomnia (disease)**,
but there are currently **0 registered clinical trials** and no publication that directly tests alprazolam for insomnia, so the support is mostly computational.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | insomnia (disease) |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 7) |
| Number of NDAs | at least 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general benzodiazepine pharmacology, alprazolam enhances GABA-A receptor signaling, which produces sedative and hypnotic effects. This is a plausible route to improving sleep, especially when insomnia occurs together with anxiety.

However, this link rests on general class knowledge rather than supplied data. The literature gathered is mostly indirect: panic disorder reviews, benzodiazepine prescribing and cost analyses, pharmacokinetics, and a cross-sectional survey of insomnia in COVID-19 survivors. One 2024 study used alprazolam in the control arm against acupuncture-based therapy in patients with coronary heart disease and insomnia, but it cannot isolate the effect of the drug. Because no cited study directly evaluates alprazolam for insomnia, the evidence level is L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Retrospective observational study | Medicine | Alprazolam control group vs. moxibustion plus ear acupuncture in coronary heart disease with insomnia; the combination design cannot isolate the drug effect |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | Medicine | Survey of insomnia and its influencing factors among COVID-19 survivors; not a drug study |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Tranquilizer therapy in elderly patients with chronic non-communicable diseases: dose and adverse effects |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Predictive model / economic analysis | Value in Health Regional Issues | Benzodiazepine use trends and economic burden; long-term use linked to memory loss, dependence and falls |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs |
| [7484706](https://pubmed.ncbi.nlm.nih.gov/7484706/) | 1995 | Review | American Family Physician | Overview of panic disorder |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Prescription pattern study | Sleep Medicine | Hypnotic prescribing patterns in a managed-care population |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohort | JHEP Reports | Zolpidem deprescribing reduced falls and fractures in cirrhosis (not alprazolam) |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical (mouse) | Aging | Repeated alprazolam administration caused mitochondrial dysfunction and impaired memory consolidation |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074342 | Alprazolam | Tablet | Not recorded |
| ANDA203346 | Alprazolam | Tablet | Not recorded |
| NDA018276 | Alprazolam | Tablet | Not recorded |
| ANDA090871 | Alprazolam | Extended-release tablet | Not recorded |
| ANDA200739 | Alprazolam | Tablet | Not recorded |

The licence list may be partial.

## Safety Considerations

- **Class risks seen in the supplied literature**: dependence, falls, cognitive and memory impairment with benzodiazepine hypnotic use; deprescribing is discussed in the literature.
- **Drug Interactions**: 100 interactions were found in total. Major interactions include **morphine** and **liposomal morphine**. Moderate interactions include aprepitant, bupropion, cimetidine, clarithromycin, clotrimazole, dronabinol, eliglustat, glycerol phenylbutyrate, metoclopramide and miconazole. Antacids (aluminum hydroxide, calcium carbonate, magnesium salts) and corticosteroids such as dexamethasone and betamethasone are minor.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no registered trial and no cited study directly tests alprazolam for insomnia. The known risks of benzodiazepine hypnotics (dependence, falls, cognitive effects) add to the concern.

**To proceed, the following is needed:**
- Controlled clinical studies of alprazolam specifically in insomnia (with or without comorbid anxiety)
- Detailed mechanism of action data
- Package insert warnings and contraindications
- Benefit–risk comparison with existing insomnia treatments, and a safety plan for older adults and patients taking opioids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

