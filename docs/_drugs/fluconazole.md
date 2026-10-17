---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 713
evidence_level: L5
indication_count: 1
monitor_inn: "FLUCONAZOLE"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-14
description: "Fluconazole: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Oral candidiasis, candidiasis, vulvovaginal candidiasis…"
---

# Fluconazole
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

# Fluconazole: From Candidiasis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is an azole antifungal originally used for candidiasis (oral, esophageal, vulvovaginal, disseminated) and cryptococcal meningitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral candidiasis, candidiasis, vulvovaginal candidiasis, esophageal candidiasis, cryptococcal meningitis, candidemia, disseminated candidiasis |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 authorizations in total (1 NDA, 9 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, fluconazole is an azole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51), blocking ergosterol synthesis. Its efficacy in candidiasis and cryptococcal infection is well established.

A plausible link to the new indication would be a fungal cause or fungal co-infection of the ocular surface. However, punctate epithelial keratoconjunctivitis is most often caused by viral (e.g., adenoviral), bacterial, toxic or dry-eye-related mechanisms. An antifungal rationale is therefore not established, and any link is speculative.

The high model score (0.992) is not clinical evidence. One way to test the prediction would be to check whether it is driven by a related node, such as fungal keratitis, in the knowledge graph.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All authorizations listed below are cancelled; none is currently valid. Only 5 of the 10 are shown. Approved indication text was not available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020090 | Fluconazole (Mylan Pharmaceuticals Inc.) | Powder, for suspension | Not available |
| ANDA078764 | Fluconazole (Hikma Pharmaceuticals USA Inc.) | Injection | Not available |
| ANDA076658 | Fluconazole (Cardinal Health 107, LLC) | Tablet | Not available |
| ANDA208963 | Fluconazole (Zydus Pharmaceuticals (USA) Inc.) | Tablet | Not available |
| ANDA079104 | Fluconazole (Sagent Pharmaceuticals) | Injection, solution | Not available |

Dosage forms across all authorizations: injectable (injection, injection solution), oral (tablet), and powder for suspension. Route compatibility with an ocular indication has not been assessed.

## Safety Considerations

**Contraindication-related diseases (from knowledge graph, not label text):** long QT syndrome, familial long QT syndrome, kidney disease, pyoureter, liver disease, gallbladder disease.

**Drug Interactions:** 100 interactions were found in total. The first 20 returned include:
- **Major:** chlorpropamide
- **Moderate:** famotidine, rabeprazole, omeprazole, dexlansoprazole, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide (including nasal), loperamide, aprepitant, bisacodyl, picosulfuric acid, polyethylene glycol 3350 with electrolytes, saxagliptin
- **Minor:** amphotericin B (including lipid complex), clarithromycin

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, the mechanistic link to a mainly viral, bacterial, toxic or dry-eye-related condition is weak, and all US authorizations are cancelled.

**To proceed, the following is needed:**
- Review the knowledge-graph paths behind the prediction (e.g., a fungal keratitis link)
- Literature and trial searches for fluconazole in ocular surface disease
- Mechanism of action data and a clearer rationale for this indication
- Assessment of route compatibility (systemic vs. ocular delivery)
- Package insert warnings and contraindications, including QT prolongation and hepatic/renal risk
- Clarification of the current US regulatory status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

