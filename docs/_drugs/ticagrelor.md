---
layout: default
title: Ticagrelor
parent: Model Prediction Only (L5)
nav_order: 1227
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "fibrocartilaginous embolism"]
description: "Ticagrelor: predicted new indication Intracranial arteriosclerosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ticagrelor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ticagrelor: Intracranial arteriosclerosis
{: .text-alpha }

## One-Sentence Summary

Ticagrelor is an oral antiplatelet drug (a reversible P2Y12 inhibitor), originally used for acute coronary syndrome and peripheral arterial disease.
The TxGNN model predicts it may be effective for **intracranial arteriosclerosis**,
with **2 clinical trials** (one Phase 3) and **2 publications** currently supporting this direction. Neither trial has reported results yet, so the evidence is by design rather than demonstrated efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Intracranial arteriosclerosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (by trial design; the Phase 3 trial has no results yet) |
| US Market Status | Marketed (active FDA-approved applications: 21 of 22) |
| Number of FDA Applications | 22 (active: 21) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on known pharmacology, ticagrelor is a reversible P2Y12 receptor antagonist that inhibits platelet aggregation. Its efficacy in acute coronary syndrome, a platelet-driven thrombotic condition, is established.

Intracranial atherosclerotic stenosis causes stroke through platelet-rich thrombus formation and artery-to-artery embolism, so antiplatelet therapy is mechanistically plausible. Ticagrelor is already used in dual antiplatelet regimens for neurointerventional procedures such as intracranial stenting.

The evidence is still pending. The Phase 3 CAPTIVA trial is active but not recruiting, and no results have been confirmed. The lower-dose regimen paper is a cohort report, not a pivotal efficacy study.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1683 | CAPTIVA: tests whether rivaroxaban, ticagrelor, or both beat clopidogrel for 1-year ischemic stroke, intracerebral hemorrhage, or vascular death in intracranial atherostenosis. Ticagrelor is not the sole experimental arm. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recruiting | 100 | Pilot study of genotype-guided P2Y12 inhibitor selection (including ticagrelor) vs clopidogrel in symptomatic intracranial atherosclerotic disease. Low-powered. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | Journal of NeuroInterventional Surgery | Ticagrelor 60 mg twice daily plus aspirin 81 mg compared with standard aspirin and clopidogrel for intracranial stenting |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Review (trial design) | International Journal of Stroke | Design and early progress of CAPTIVA; standard treatment for symptomatic intracranial stenosis carries a high recurrent stroke risk up to 12 months |

## US Market Information

The drug is marketed.

<!-- review:begin us-lic-20261106-ticagrelor-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed, with 13 valid licenses, and none has approved-indication text on file." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 22 FDA applications or NDC listings for this drug, 21 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-ticagrelor-2 -->

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022433 | BRILINTA (AstraZeneca) | Tablet | Not listed |
| ANDA208597 | Ticagrelor (Mylan) | Tablet, film coated | Not listed |
| ANDA217679 | Ticagrelor (Lifestar Pharma) | Tablet, film coated | Not listed |
| ANDA208596 | Ticagrelor (Novadoz) | Tablet | Not listed |
| ANDA208390 | Ticagrelor (Teva) | Tablet, film coated | Not listed |

## Safety Considerations

- **Contraindication-related conditions** (from knowledge-graph drug-disease links, not label text): liver failure, liver disease, gallbladder disease, intracranial hemorrhage. Intracranial hemorrhage is especially relevant to an intracranial vascular indication.
- **Drug Interactions**: 100 interactions were found. Examples from the first 20 reviewed:
  - **Major**: clarithromycin
  - **Moderate**: acetylsalicylic acid (aspirin), simvastatin, morphine, dexamethasone, budesonide, aprepitant, miconazole, saxagliptin, among others
  - **Minor**: naloxegol, prucalopride

<!-- review:begin us-lic-20261106-ticagrelor-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Eight further ANDAs are on file, all cancelled." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 22 FDA applications or NDC listings for this drug, 21 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-ticagrelor-1 -->

Please refer to the package insert for key warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible, and a large Phase 3 trial (CAPTIVA, n=1683) directly addresses this indication. No results are available, and ticagrelor is not the only experimental arm, so the support is by design rather than proven efficacy. Bleeding risk, particularly intracranial hemorrhage, is the central safety concern.

**To proceed, the following is needed:**
- CAPTIVA results (expected completion January 2027) and the ticagrelor-specific arm outcomes
- FDA package insert warnings and contraindications (currently unavailable and blocking for safety screening)
- Detailed mechanism-of-action data
- Clarification of US regulatory status, since the drug is marketed
- A bleeding-risk management plan, including patient selection and treatment duration

<!-- review:begin us-lic-20261106-ticagrelor-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of US regulatory status, since the drug is marketed with 13 valid licenses" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 22 FDA applications or NDC listings for this drug, 21 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-ticagrelor-3 -->

## Other Predicted Indications (Brief)

| Rank | Predicted Indication | Score | Evidence Level | Decision | Note |
|------|------|------|------|------|------|
| 4 | Ischemic disease | 0.9964 | L1 | Proceed with Guardrails | Largely overlaps the existing acute coronary syndrome use (e.g., TWILIGHT, PEGASUS, and 2021 stroke/TIA RCTs), so it confirms an existing use rather than novel repurposing |
| 8 | Vascular ectasia | 0.9947 | L5 | Research Question | Only an indirect review on coronary ectasia; bleeding concern |

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Eight further ANDAs are on file, all cancelled" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 13 valid licenses, and none has approved-indication text on file" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 13 valid licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

