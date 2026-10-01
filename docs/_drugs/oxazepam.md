---
layout: default
title: Oxazepam
parent: Model Prediction Only (L5)
nav_order: 1001
evidence_level: L5
indication_count: 1
---

# Oxazepam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Oxazepam: From an Unlisted Original Indication to Insomnia

## One-Sentence Summary

Oxazepam is a benzodiazepine sold as generic oral capsules in the US, but the record lists no approved indication text.
The TxGNN model predicts it may be effective for **insomnia**.
Support is limited: **0 registered clinical trials** and **11 publications**, of which only **2 are RCTs**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source record (all license entries have empty indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 (as scored in the Evidence Pack; the phase of the two RCTs is not confirmed, so this is a generous reading) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 13 (all listed entries are ANDA072253 generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on class pharmacology, oxazepam is a short-to-intermediate-acting benzodiazepine. It is a positive allosteric modulator of GABA-A receptors, which enhances inhibitory neurotransmission. Its sedative-hypnotic effect is biologically consistent with treating insomnia.

The very high TxGNN score matches this class-level mechanism, but it is a model prediction, not clinical evidence. Because the drug record has no curated original indications or MOA, the mechanistic link rests on class knowledge rather than drug-level data.

Oxazepam has no active metabolites and is cleared by glucuronidation. That is relevant to its safety in older adults and in liver disease, but it is not a reason in itself to recommend it for insomnia.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | RCT | Am J Psychiatry | In 14 chronic insomnia patients, oxazepam and flurazepam both improved some polysomnographic sleep measures. Flurazepam caused substantial daytime sleepiness and oxazepam did not. Oxazepam produced some rebound effects. |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | RCT | Ann Pharmacother | Compared melatonin with oxazepam for anxiety and sleep quality in STEMI patients after primary PCI. Benzodiazepines are effective here but carry adverse effects and interaction risks. Results are not included in the available abstract. |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Review | Arch Gerontol Geriatr | Studied 60 elderly patients (over 70) with insomnia and comorbid depression, dementia or behavioral disturbances, looking at the effectiveness and safety of hypnotics. |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Cohort | JAMA | Two patients developed withdrawal syndrome after switching from a long-acting to a short-acting benzodiazepine (oxazepam replaced diazepam in one case). Symptoms lasted at least one month. |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Cohort | PeerJ | Analyzed factors linked to long-term benzodiazepine and z-drug use in older people. Older age, female sex and psychological or somatic burden are associated with long-term use. |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Reviews the pharmacokinetics of anxiolytic drugs, the most prescribed psychoactive drugs in Western countries. |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Review | J Clin Exp Hepatol | Reviews alcohol withdrawal syndrome management in alcoholic liver disease. Insomnia appears as one of its symptoms, so this is only indirectly relevant. |

Four other retrieved papers (agomelatine case report, paroxetine in panic disorder, dementia behavioral symptoms, informed refusal) were judged not relevant to oxazepam for insomnia and are not listed.

## US Market Information

Five of the 13 licenses are shown, all under the same ANDA number. None includes indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA072253 (American Health Packaging) | Oxazepam | Capsule, gelatin coated | Not listed |
| ANDA072253 (Actavis Pharma, Inc.) | Oxazepam | Capsule, gelatin coated | Not listed |
| ANDA072253 (Actavis Pharma, Inc.) | Oxazepam | Capsule, gelatin coated | Not listed |
| ANDA072253 (Actavis Pharma, Inc.) | Oxazepam | Capsule, gelatin coated | Not listed |
| ANDA072253 (American Health Packaging) | Oxazepam | Capsule, gelatin coated | Not listed |

The only route is oral (capsule).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score and a plausible class mechanism. There are no registered trials, and the two RCTs are small or do not clearly test insomnia. The package insert warnings and contraindications are missing, which blocks safety screening. The pack scores this as a research question, not a candidate for advancement.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking), plus the approved indication text
- Curated mechanism of action data from DrugBank
- Phase and outcome details of the two RCTs, to confirm the evidence level
- Safety review for older adults and patients with liver disease, and for withdrawal and dependence risk
- Comparison against currently approved insomnia therapies, and a check of route compatibility

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

