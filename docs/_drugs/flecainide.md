---
layout: default
title: Flecainide
parent: Model Prediction Only (L5)
nav_order: 710
evidence_level: L5
indication_count: 9
monitor_inn: "FLECAINIDE"
predicted_indications: ["stroke disorder", "sick sinus syndrome 2, autosomal dominant", "ABri amyloidosis", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "duodenal obstruction", "cerebrovascular disorder", "nephrogenic syndrome of inappropriate antidiuresis"]
last_modified_at: 2026-11-12
description: "Flecainide: predicted new indication Stroke disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Flecainide
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

## Flecainide: Stroke disorder
{: .text-alpha }

## One-Sentence Summary

Flecainide is a class 1C sodium channel blocker used as an oral tablet antiarrhythmic.
The TxGNN model predicts it may be relevant to **stroke disorder**, but the evidence level is **L5**: no study has tested flecainide for stroke itself. The data compiled for this report contain **1 related clinical trial** (with an arrhythmia endpoint) and **literature that addresses atrial fibrillation management rather than stroke treatment**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 8 of 11) |
| Number of FDA Applications | 11 (active: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known information, flecainide is a class 1C sodium channel blocker that suppresses cardiac conduction and is used to control heart rhythm.

The link to stroke is indirect. Stroke is a major downstream consequence of atrial fibrillation, so a drug that reduces atrial arrhythmia burden could in theory lower cardioembolic risk. However, no study shows that flecainide itself prevents stroke. The high TxGNN score probably reflects this disease association rather than a direct therapeutic effect.

Practical limits also apply: flecainide is generally avoided in structural or ischaemic heart disease, which describes many stroke patients.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | Active, not recruiting | 186 | Tests flecainide to lower the risk of atrial arrhythmia after patent foramen ovale (PFO) closure in a population treated for cryptogenic stroke. The primary endpoint is arrhythmia, not stroke, so the evidence is indirect. |

## Literature Evidence

None of the publications below tests flecainide for stroke treatment or prevention.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | Cohort | Europace | EAST-AFNET 4 analysis of the safety of long-term sodium channel blocker (flecainide, propafenone) therapy for early rhythm control; concerns proarrhythmic risk |
| [41954064](https://pubmed.ncbi.nlm.nih.gov/41954064/) | 2026 | Cohort | J Am Heart Assoc | Long-term outcomes of class 1C antiarrhythmic drugs in atrial fibrillation; cardiovascular benefit over rate control still unclear |
| [38551548](https://pubmed.ncbi.nlm.nih.gov/38551548/) | 2024 | Cohort | JACC Clin Electrophysiol | Class 1C drugs for premature ventricular complex suppression in nonischaemic cardiomyopathy |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Review | BMJ Clin Evid | Acute-onset atrial fibrillation; notes that it raises stroke risk |
| [39077579](https://pubmed.ncbi.nlm.nih.gov/39077579/) | 2023 | Review | Rev Cardiovasc Med | Managing atrial fibrillation in pregnancy, including thromboembolic risk |
| [19265095](https://pubmed.ncbi.nlm.nih.gov/19265095/) | 2009 | Review | Chest | Acute management of atrial fibrillation, rate versus rhythm control |
| [35114252](https://pubmed.ncbi.nlm.nih.gov/35114252/) | 2022 | Mechanistic study | J Mol Cell Cardiol | Atrial sodium channel properties explain flecainide's atrial effectiveness |
| [37109225](https://pubmed.ncbi.nlm.nih.gov/37109225/) | 2023 | RCT (pilot) | J Clin Med | Carvedilol versus flecainide for idiopathic outflow-tract premature ventricular complexes |

## US Market Information

The licences below are single-ingredient flecainide acetate tablets. No indication text is recorded in the local data.

<!-- review:begin us-lic-20261106-flecainide-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The licences below are single-ingredient flecainide acetate tablets. The list may be partial." Removed: it conflicted with the FDA application data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 11 FDA applications or NDC listings for this drug, 8 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-flecainide-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA075442 | FLECAINIDE ACETATE | AMNEAL PHARM | Tablet; oral | Valid |
| ANDA075882 | FLECAINIDE ACETATE | ANI PHARMS | Tablet; oral | Valid |
| ANDA076278 | FLECAINIDE ACETATE | HIKMA | Tablet; oral | Valid |
| ANDA076421 | FLECAINIDE ACETATE | SUN PHARM INDS LTD | Tablet; oral | Valid |
| ANDA202821 | FLECAINIDE ACETATE | AUROBINDO PHARMA LTD | Tablet; oral | Valid |

Showing 5 of 11 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions** (100 interactions recorded; examples):
  - Major: dolasetron, eliglustat
  - Moderate: famotidine, cimetidine, bupropion, clarithromycin, levofloxacin, loperamide, lorcaserin, palonosetron, trospium
  - Minor: ascorbic acid, metronidazole, potassium citrate
- **Other concerns from the literature**: Class 1C agents carry proarrhythmic risk, especially in structural heart disease or ischaemia (PMIDs 38702961, 40800559).

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 because no study tests flecainide for stroke. The only related trial (NCT05213104) measures atrial arrhythmia after PFO closure, and the literature concerns rhythm control in atrial fibrillation. The proarrhythmic risk in structural and ischaemic heart disease further limits use in stroke populations.

**To proceed, the following is needed:**
- A study with stroke or cerebrovascular events as the endpoint
- Results of NCT05213104, to see whether arrhythmia reduction translates into fewer cerebrovascular events
- Detailed mechanism-of-action data
- Review of full package insert warnings and contraindications
- A safety plan for patients with structural or ischaemic heart disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The list may be partial" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

