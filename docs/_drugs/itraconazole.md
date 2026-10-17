---
layout: default
title: Itraconazole
parent: Model Prediction Only (L5)
nav_order: 819
evidence_level: L5
indication_count: 1
monitor_inn: "ITRACONAZOLE"
predicted_indications: ["pneumocystosis"]
last_modified_at: 2026-10-14
description: "Itraconazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Systemic fungal infections"
---

# Itraconazole
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

# Itraconazole: From Systemic Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is an azole antifungal originally used for systemic fungal infections such as candidiasis, histoplasmosis, aspergillosis, blastomycosis and sporotrichosis.
The TxGNN model predicts it may be effective for **Pneumocystosis**, but the data compiled for this report show **0 registered clinical trials** and **20 publications**, none of which directly tests itraconazole as a Pneumocystis treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic fungal infections (esophageal candidiasis, candidemia, histoplasmosis, aspergillosis, blastomycosis, and others; listed in the knowledge graph, as US label text is not available) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 9 licenses cancelled) |
| Number of NDAs | 9 (9 cancelled; includes NDA and ANDA licenses) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. From general pharmacology, itraconazole is an azole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51), blocking ergosterol synthesis. Its efficacy across many systemic fungal infections is well established.

The mechanistic link to pneumocystosis is weak, however. *Pneumocystis jirovecii* has a cell membrane in which cholesterol, rather than ergosterol, is the dominant sterol, so the azole target is largely absent. The high TxGNN score (0.993) therefore likely reflects network proximity to other fungal diseases rather than a true mechanistic fit.

The supplied literature points the same way. Most articles are general reviews of prophylaxis and opportunistic infections in transplant, HIV and neutropenic patients, or reports of histoplasmosis and aspergillosis. They appear to have been retrieved because itraconazole is discussed alongside other fungal infections, not because it was studied for Pneumocystis. Pneumocystosis is also not among the drug's listed original indications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No study listed below tests itraconazole for Pneumocystis treatment. Study types are those assigned in the compiled data; "Not classified" means no type was assigned.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | Randomized, double-blind, placebo-controlled phase III trial (per title) | HIV Medicine | Itraconazole capsules for preventing deep fungal infections in HIV patients; the abstract excerpt does not report Pneumocystis outcomes |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including *P. carinii* |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Primary and secondary prophylaxis of opportunistic infections in HIV |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Review | Clinical Infectious Diseases | Antimicrobial prophylaxis in febrile neutropenia; trimethoprim-sulfamethoxazole is highly effective against Pneumocystis pneumonia |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Infection after lung transplantation |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Prophylaxis and treatment of infection in bone marrow transplant recipients |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Case series/Review | Medicine | Disseminated histoplasmosis in AIDS: clinical findings, diagnosis and treatment |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | Single-center experience with invasive fungal infections after kidney transplantation |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report and literature review | Frontiers in Immunology | *Talaromyces marneffei* and *P. jirovecii* coinfection in a child with a STAT1 mutation |

## US Market Information

All 9 US licenses are cancelled, and no approved-indication text is available for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208901 | Tolsura (Mayne Pharma) | Capsule, gelatin coated | Not available |
| NDA020083 | Itraconazole (Patriot Pharmaceuticals) | Capsule | Not available |
| ANDA208591 | Itraconazole (Ascend Laboratories) | Capsule, coated pellets | Not available |
| ANDA212239 | Itraconazole (Camber Pharmaceuticals) | Solution | Not available |
| ANDA206741 | Itraconazole (Alembic Pharmaceuticals) | Capsule | Not available |

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for safety information.

The following come from the knowledge graph (not label text) and from drug-interaction databases:

- **Knowledge-graph contraindicated conditions** (30 in total, main groups):
  - Cardiac: long QT syndrome, torsades de pointes, congestive heart failure, heart failure, cardiomyopathy, coronary artery disease, myocardial ischemia, heart valve disease
  - Liver and kidney: liver disease, drug-induced liver injury, kidney disease, impaired renal function
  - Respiratory: chronic obstructive pulmonary disease
  - Nervous system: peripheral neuropathy
  - Sensory: hearing loss, vision disorder
  - Metabolic: potassium deficiency, hypercalcemia
- **Drug interactions** (100 recorded; examples from the 20 retrieved):
  - Major: loperamide, triamcinolone, budesonide
  - Moderate: famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, dexamethasone, hydrocortisone, betamethasone, aprepitant, alosetron
  - Minor: metformin, pioglitazone, amphotericin B, chlorpropamide

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no registered clinical trials and no literature testing itraconazole against Pneumocystis. *Pneumocystis* lacks the ergosterol target of azoles, so the mechanistic rationale is weak. Evidence stays at L5 (model prediction only), and all US licenses are cancelled.

**To proceed, the following is needed:**
- Direct evidence of itraconazole activity against *Pneumocystis* (in vitro, animal, or clinical), with a plausible non-ergosterol mechanism
- Mechanism-of-action data for itraconazole
- US package insert warnings and contraindications for a safety screen, given the cardiac, hepatic and interaction concerns above
- Comparison against established Pneumocystis therapy and prophylaxis (e.g. trimethoprim-sulfamethoxazole)
- Review of the cancelled US market status and route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

