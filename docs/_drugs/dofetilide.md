---
layout: default
title: Dofetilide
parent: Model Prediction Only (L5)
nav_order: 619
evidence_level: L5
indication_count: 9
monitor_inn: "DOFETILIDE"
predicted_indications: ["stroke disorder", "ABri amyloidosis", "sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "duodenal obstruction", "brain stem infarction", "macrocephaly, dysmorphic facies, and psychomotor retardation", "cerebrovascular disorder"]
last_modified_at: 2026-11-12
description: "Dofetilide: predicted new indication Stroke disorder (evidence level L5). Approved use: Atrial fibrillation"
---

# Dofetilide
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

## Dofetilide: From Atrial Fibrillation to Stroke Disorder
{: .text-alpha }

## One-Sentence Summary

Dofetilide is an antiarrhythmic drug originally used to treat atrial fibrillation.
The TxGNN model predicts it may be effective for **stroke disorder**, but there are currently **0 registered clinical trials** and **7 publications** (all about atrial fibrillation management, none testing stroke as an outcome), so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 10 of 15) |
| Number of FDA Applications | 15 (active: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dofetilide is a selective blocker of the IKr potassium current (Kv11.1/hERG) and is used for rhythm control in atrial fibrillation.

The link between the two conditions is indirect. Stroke is a downstream complication of atrial fibrillation, so maintaining sinus rhythm might lower the risk of clot formation and embolism. However, the retrieved literature covers rhythm management and comparisons of antiarrhythmic drugs. None of it shows that dofetilide prevents stroke. Rhythm control also does not replace anticoagulation.

The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases such as atrial fibrillation and stroke, not biological evidence or a new mechanism of action.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26233885](https://pubmed.ncbi.nlm.nih.gov/26233885/) | 2016 | Systematic review / Meta-analysis | Journal of Cardiology | Comparative effectiveness of antiarrhythmic drugs for rhythm control of atrial fibrillation; little comparative data exists to guide drug choice |
| [32538135](https://pubmed.ncbi.nlm.nih.gov/32538135/) | 2020 | Cohort | Circulation: Arrhythmia and Electrophysiology | Dofetilide in AF patients with LVEF ≤35%; assessed LVEF improvement, safety and outcomes |
| [21955243](https://pubmed.ncbi.nlm.nih.gov/21955243/) | 2012 | Cohort | Journal of Cardiovascular Electrophysiology | Dofetilide reduced ventricular arrhythmias and ICD therapies in patients with implanted defibrillators |
| [11174354](https://pubmed.ncbi.nlm.nih.gov/11174354/) | 2001 | Review | American Heart Journal | Pharmacologic strategies for AF, which carries a risk of embolic complications |
| [11445058](https://pubmed.ncbi.nlm.nih.gov/11445058/) | 2001 | Review | Current Treatment Options in Cardiovascular Medicine | Treatment of atrial flutter |
| [20638626](https://pubmed.ncbi.nlm.nih.gov/20638626/) | 2010 | Review | Gender Medicine | Gender differences in atrial fibrillation |
| [32435191](https://pubmed.ncbi.nlm.nih.gov/32435191/) | 2020 | Preclinical (animal) | Frontiers in Pharmacology | KCa2 and Kv11.1 channel inhibition in pigs with left ventricular dysfunction |

None of these studies uses stroke as an endpoint.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020931 | Tikosyn (Pfizer) | Capsule | Not listed (valid) |
| ANDA210466 | Dofetilide (Sun Pharmaceutical) | Capsule | Not listed (valid) |
| ANDA207058 | Dofetilide (Dr. Reddy's) | Capsule | Not listed (valid) |
| ANDA213220 | Dofetilide (Novadoz) | Capsule | Not listed (valid) |
| ANDA210740 | Dofetilide (Aurobindo) | Capsule | Not listed (valid) |

Four more ANDAs (Accord, Bionpharma, Sigmapharm, Exelan) are also valid.

<!-- review:begin us-lic-20261106-dofetilide-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Four more ANDAs (Accord, Bionpharma, Sigmapharm, Exelan) are also valid. All 9 authorizations are in valid status." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 15 FDA applications or NDC listings for this drug, 10 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-dofetilide-2 -->

## Safety Considerations

- **Disease-level cautions from the knowledge graph** (these come from knowledge-graph contraindication links, not from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, kidney disease, liver disease, gallbladder disease, potassium deficiency, pyoureter and anorexia nervosa.
- **Known class concern**: Dofetilide's most concerning adverse effect is QT prolongation with polymorphic ventricular tachycardia (reported in the literature).
- **Case report**: One report (PMID 30700466) describes facial paralysis after cardioversion in a dofetilide-treated patient, initially mistaken for stroke. This is a safety signal or diagnostic confounder, not evidence of benefit.
- **Drug Interactions**: The interaction query returned 100 entries; the first 20 reviewed include many **Major** ones:
  - Hydrocortisone
  - Cimetidine
  - Clarithromycin
  - Cisapride
  - Dolasetron
  - Eliglustat
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)
  - Moderate interactions include famotidine, metformin, loperamide, aprepitant, bisacodyl, castor oil and clotrimazole. Dexamethasone is Minor.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The stroke prediction comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases such as atrial fibrillation, not biological evidence. No trials exist, the literature contains no stroke-outcome data, and the drug carries a serious proarrhythmic risk. The drug is marketed. The other nine predicted indications are either unsupported by any evidence (L5) or biologically implausible, so none is a better candidate.

<!-- review:begin us-lic-20261106-dofetilide-3 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed, with 9 valid US authorizations." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 15 FDA applications or NDC listings for this drug, 10 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-dofetilide-3 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a current blocking gap)
- Mechanism of action data to support a mechanistic-link analysis
- Evidence that dofetilide-based rhythm control reduces stroke or cerebrovascular events beyond anticoagulation

<!-- review:begin us-lic-20261106-dofetilide-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Evidence that dofetilide-based rhythm control reduces stroke or cerebrovascular events beyond anticoagulation / A review of whether the cancelled US market status limits practical development" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 15 FDA applications or NDC listings for this drug, 10 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-dofetilide-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "A review of whether the cancelled US market status limits practical development" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "All 9 authorizations are in valid status" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 9 valid US authorizations" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

