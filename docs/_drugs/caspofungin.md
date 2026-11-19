---
layout: default
title: Caspofungin
parent: Model Prediction Only (L5)
nav_order: 503
evidence_level: L5
indication_count: 1
monitor_inn: "CASPOFUNGIN"
predicted_indications: ["gastrin secretion abnormality"]
last_modified_at: 2026-11-20
description: "Caspofungin: predicted new indication gastrin secretion abnormality (evidence level L5). In the US: 9 FDA applications (4 active)"
---

# Caspofungin
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

## Caspofungin: Echinocandin antifungal (beta-(1,3)-D-glucan synthase inhibitor) → gastrin secretion abnormality
{: .text-alpha }

## One-Sentence Summary

Caspofungin is an echinocandin antifungal drug marketed in the United States as injectable products.
The TxGNN model predicts it may be related to **gastrin secretion abnormality**, with a score of **0.9944**.
Currently there are **no clinical trials** and **no publications** in the compiled data supporting this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | gastrin secretion abnormality |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 4 of 9) |
| Number of FDA Applications | 9 (active: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the FDA-approved prescribing information for caspofungin: "Caspofungin is an echinocandin antifungal drug. […] Caspofungin, an echinocandin, inhibits the synthesis of beta (1,3)-D-glucan, an essential component of the cell wall of susceptible Aspergillus species and Candida species. Beta (1,3)-D-glucan is not present in mammalian cells." ([DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c), label version 2024-10-11; accessed 2026-11-19.) Caspofungin belongs to the echinocandin class, which is generally understood to inhibit beta-(1,3)-D-glucan synthase in the fungal cell wall.

No known pathway connects glucan synthase inhibition to gastrin regulation, G-cell function or gastric acid physiology. The high prediction score reflects a pattern found by the model, not a demonstrated biological link. Any connection, for example an indirect effect through changes in fungal or gut microbiota, would be speculative and would need independent validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021227 | CANCIDAS | Lyophilized powder for injection | Not recorded in the local data |
| NDA206110 | Caspofungin Acetate | Lyophilized powder for injection | Not recorded in the local data |
| ANDA200833 | Caspofungin Acetate | Lyophilized powder for injection | Not recorded in the local data |
| ANDA207092 | Caspofungin Acetate | Lyophilized powder for injection | Not recorded in the local data |
| ANDA216506 | Caspofungin Acetate | Lyophilized powder for injection | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: 81 interactions were recorded. The main ones are:
  - **Major**: Dexamethasone
  - **Moderate**: Naltrexone
  - Other recorded interactions have an unclassified severity level, including calcitriol, pantoprazole, doxycycline, morphine, omeprazole, vancomycin, simvastatin, amphotericin B, prednisone, hydrocortisone and potassium chloride.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9944), but there are no clinical trials, no publications and no supported mechanistic link to gastrin secretion. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis connecting caspofungin to gastrin regulation, supported by preclinical data
- Mechanism of action data for the drug
- Package insert warnings and contraindications
- A literature and trial search to find any direct study of gastrin secretion abnormality
- Clarification of how the drug's injectable-only route fits a possible new use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

