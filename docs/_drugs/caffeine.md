---
layout: default
title: Caffeine
parent: Model Prediction Only (L5)
nav_order: 484
evidence_level: L5
indication_count: 10
monitor_inn: "CAFFEINE"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "acute laryngopharyngitis", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "hypnic headache (disease)", "vein disease"]
last_modified_at: 2026-10-14
description: "Caffeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis…"
---

# Caffeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Caffeine: From Headache and Rhinitis Disorders to Nasal Cavity Disease

## One-Sentence Summary

Caffeine was originally used (mainly in combination products) for headache disorders such as migraine and cluster headache, and for upper-respiratory conditions such as allergic rhinitis and the common cold.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, but there are **0 clinical trials** and only **3 publications** (a review, a formulation study and an animal study), so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, migraine, pharyngitis, common cold, nasopharyngitis, headache disorders (cluster headache, paroxysmal hemicrania, hemicrania continua). No approved-indication text is available from the US licence records. |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 8 licence records (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, caffeine is an adenosine receptor antagonist and phosphodiesterase inhibitor. Bitter taste receptors are also expressed in the human nasal cavity and airways, which could offer a pharmacological connection.

The original indications already include nasal conditions (allergic and vasomotor rhinitis). The high score may therefore mostly reflect a known indication class rather than a truly new use. The only intranasal caffeine paper found concerns an in situ gel for cognition after sleep deprivation, not treatment of nasal disease. The link is weakly supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are found in the nasal cavity, lungs and other tissues; their pharmacology and role in human airways are reviewed |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Preclinical formulation study | Current Drug Delivery | Nasal thermo-sensitive caffeine in situ gel for enhanced cognition after sleep deprivation (delivery route, not nasal disease treatment) |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine inhibited lung tumorigenesis in rats given a tobacco-specific carcinogen (not relevant to nasal disease) |

## US Market Information

All eight US licence records are cancelled, and no approved-indication text is available for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020793 | CAFCIT | Injection | Not available |
| ANDA077233 | Caffeine citrate | Injection | Not available |
| ANDA207400 | Caffeine citrate | Injection, solution | Not available |
| ANDA213202 | Caffeine citrate | Solution | Not available |
| part340 | Alert | Tablet, film coated | Not available |

Three further cancelled records (M011 Stay Awake, 505G(a)(3) Stay Awake, and the Caffeinum pellet) are not listed here.

## Safety Considerations

- **Conditions flagged as contraindication-related in the knowledge graph (not label text):** hypertension, orthostatic hypotension and related autonomic disorders, long QT syndrome, epilepsy, insomnia, anxiety disorders, liver failure and liver disease, kidney disease, peptic and gastric ulcer, inflammatory bowel disease, pancreatitis, gallbladder disease, porphyria, hypothyroidism, COPD and thrombocytopenia.
- **Drug Interactions:** 75 interactions were recorded. Major-level interactions were identified with nasal and topical cocaine. Moderate-level interactions include alosetron, obeticholic acid, adenosine, anagrelide, bendamustine, capmatinib, ciprofloxacin, cycloserine, dipyridamole and duloxetine. Minor-level interactions include aspirin, cimetidine, atazanavir and disulfiram.
- Published reviews also raise cardiovascular concerns with stimulants and note an association with medication-overuse headache.

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.999), but it rests on model output alone, with no clinical trials and no literature showing caffeine treats nasal cavity disease. Because rhinitis is already among caffeine's original indications, the prediction adds little new information, and all US licences are currently cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Clarification of which specific nasal conditions are meant by "nasal cavity disease", and how they differ from the existing rhinitis indications
- Preclinical or early clinical evidence of caffeine (including a suitable intranasal formulation) in a nasal disease model
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

