---
layout: default
title: Caffeine
parent: Model Prediction Only (L5)
nav_order: 484
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Caffeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis…"
monitor_inn: "CAFFEINE"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
---

# Caffeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Caffeine: From Headache and Rhinitis Disorders to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Caffeine was originally used (mainly in combination products) for headache disorders such as migraine and cluster headache, and for upper-respiratory conditions such as allergic rhinitis and the common cold.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, but there are **0 clinical trials** and only **3 publications** (a review, a formulation study and an animal study), so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis, common cold, nasopharyngitis, headache disorders (cluster headache, paroxysmal hemicrania, hemicrania continua). No approved-indication text is available from the US licence records. |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 46 of 128; OTC monograph / unapproved listings: 334) |
| Number of FDA Applications | 128 (active: 46) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for caffeine: "Caffeine is structurally related to other methylxanthines, theophylline, and theobromine. It is a bronchial smooth muscle relaxant, a CNS stimulant, a cardiac muscle stimulant, and a diuretic. Although the mechanism of action of caffeine in apnea of prematurity is not known, several mechanisms have been hypothesized." ([DailyMed: caffeine citrate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f38c395-0093-4afd-89ec-f96e5dc0934a), label version 2026-07-29; accessed 2026-11-19.) Based on general pharmacology, caffeine is an adenosine receptor antagonist and phosphodiesterase inhibitor. Bitter taste receptors are also expressed in the human nasal cavity and airways, which could offer a pharmacological connection.

The original indications already include nasal conditions (allergic and vasomotor rhinitis). The high score may therefore mostly reflect a known indication class rather than a truly new use. The only intranasal caffeine paper found concerns an in situ gel for cognition after sleep deprivation, not treatment of nasal disease. The link is weakly supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

<!-- review:begin us-lic-20261106-caffeine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Eight US licence records are valid, and no approved-indication text is available for them." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-caffeine-1 -->

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are found in the nasal cavity, lungs and other tissues; their pharmacology and role in human airways are reviewed |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Preclinical formulation study | Current Drug Delivery | Nasal thermo-sensitive caffeine in situ gel for enhanced cognition after sleep deprivation (delivery route, not nasal disease treatment) |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine inhibited lung tumorigenesis in rats given a tobacco-specific carcinogen (not relevant to nasal disease) |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA077233 | CAFFEINE CITRATE | EXELA PHARMA SCIENCE | Solution; intravenous | Valid |
| ANDA077304 | CAFFEINE CITRATE | EXELA PHARMA | Solution; oral | Valid |
| ANDA077906 | CAFFEINE CITRATE | AM REGENT | Solution; intravenous | Valid |
| ANDA077997 | CAFFEINE CITRATE | FRESENIUS KABI USA | Solution; intravenous | Valid |
| ANDA078002 | CAFFEINE CITRATE | FRESENIUS KABI USA | Solution; oral | Valid |

Showing 5 of 462 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

Three further cancelled records (M011 Stay Awake, 505G(a)(3) Stay Awake, and the Caffeinum pellet) are not listed here.

## Safety Considerations

- **Conditions flagged as contraindication-related in the knowledge graph (not label text):** hypertension, orthostatic hypotension and related autonomic disorders, long QT syndrome, epilepsy, insomnia, anxiety disorders, liver failure and liver disease, kidney disease, peptic and gastric ulcer, inflammatory bowel disease, pancreatitis, gallbladder disease, porphyria, hypothyroidism, COPD and thrombocytopenia.
- **Drug Interactions:** 75 interactions were recorded. Major-level interactions were identified with nasal and topical cocaine. Moderate-level interactions include alosetron, obeticholic acid, adenosine, anagrelide, bendamustine, capmatinib, ciprofloxacin, cycloserine, dipyridamole and duloxetine. Minor-level interactions include aspirin, cimetidine, atazanavir and disulfiram.
- Published reviews also raise cardiovascular concerns with stimulants and note an association with medication-overuse headache.

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9991), but it rests on model output alone, with no clinical trials and no literature showing caffeine treats nasal cavity disease. Because rhinitis is already among caffeine's original indications, the prediction adds little new information, and the drug is currently marketed in the US.

<!-- review:begin us-lic-20261106-caffeine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Because rhinitis is already among caffeine's original indications, the prediction adds little new information, and the drug is currently marketed in the US with 8 valid licences." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-caffeine-2 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Clarification of which specific nasal conditions are meant by "nasal cavity disease", and how they differ from the existing rhinitis indications
- Preclinical or early clinical evidence of caffeine (including a suitable intranasal formulation) in a nasal disease model

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Eight US licence records are valid, and no approved-indication text is available for them" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 8 valid licences" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: caffeine citrate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f38c395-0093-4afd-89ec-f96e5dc0934a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

