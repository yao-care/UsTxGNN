---
layout: default
title: Isavuconazonium
parent: Model Prediction Only (L5)
nav_order: 812
evidence_level: L5
indication_count: 2
monitor_inn: "ISAVUCONAZONIUM"
predicted_indications: ["pneumocystosis", "mycetoma"]
last_modified_at: 2026-10-30
description: "Isavuconazonium: predicted new indication Pneumocystosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Isavuconazonium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Isavuconazonium: Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Isavuconazonium is a triazole antifungal prodrug (of isavuconazole), originally used for invasive fungal infections such as aspergillosis and mucormycosis (zygomycosis).
The TxGNN model predicts it may be effective for **pneumocystosis**, but the mechanistic rationale is weak, and **0 clinical trials** and **0 publications** currently support this prediction.
The second-ranked prediction, **mycetoma**, is biologically more plausible, but its only support is **1 indirect review**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9956 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, isavuconazonium is a prodrug of isavuconazole, a triazole that inhibits fungal lanosterol 14-alpha-demethylase (CYP51) and blocks ergosterol synthesis. This mechanism is the basis of its activity in aspergillosis and other mold and yeast infections.

For **pneumocystosis**, the mechanistic link is weak. *Pneumocystis jirovecii* has little or no ergosterol in its cell membrane and uses cholesterol and other sterols instead, so azoles are generally considered poorly active against it. The very high TxGNN score (0.9956) probably reflects a general antifungal class association rather than a validated mechanism.

The second prediction, **mycetoma** (score 0.9934), is more plausible. Eumycetoma is caused by ergosterol-containing fungi such as *Madurella mycetomatis*, which are susceptible in principle to azole inhibition of CYP51, and other azoles (itraconazole, and fosravuconazole in recent trials) are used or studied for it. Actinomycetoma, however, is bacterial and would not respond to an antifungal. This is a research question, not a basis for recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (for pneumocystosis or mycetoma).

---

## Literature Evidence

For pneumocystosis, currently no related literature available.

For the second prediction, mycetoma, one indirect item was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/) | 2023 | Review | Parasites & Vectors | Review of the pipeline of oral anti-infective drugs for off-label use against neglected tropical diseases. It is indirect, pipeline-level information and not a study of isavuconazonium in mycetoma. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA207500 | CRESEMBA (Astellas Pharma US, Inc.) | Capsule | Not available (status: valid) |
| NDA207501 | CRESEMBA (Astellas Pharma US, Inc.) | Lyophilized powder for injection solution | Not available (status: valid) |


---

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 interacting drugs (the data compiled for this report lists 20 of them). Most are Moderate. Major interactions include:
- Clarithromycin
- Eliglustat
- Cisapride

Examples of Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, pioglitazone, saxagliptin, linagliptin, empagliflozin, loperamide, bupropion, aprepitant, cimetidine, and clotrimazole. Fidaxomicin is a Minor interaction.

Please refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pneumocystosis prediction rests on model score alone (L5). There are no clinical trials or literature, and the biology argues against it because *Pneumocystis* lacks ergosterol. The mycetoma prediction is mechanistically plausible but supported only by an indirect review (L4), so it is a research question rather than an actionable recommendation.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For mycetoma: in vitro susceptibility data for *Madurella mycetomatis* and other eumycetoma pathogens, and animal or clinical studies of isavuconazole
- For pneumocystosis: independent evidence of activity against *Pneumocystis*, otherwise deprioritize
- Confirmation of current US regulatory status and the approved indications of the cancelled NDAs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

