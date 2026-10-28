---
layout: default
title: Toremifene
parent: Model Prediction Only (L5)
nav_order: 1244
evidence_level: L5
indication_count: 1
monitor_inn: "TOREMIFENE"
predicted_indications: ["HIV infectious disease"]
last_modified_at: 2026-10-14
description: "Toremifene: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not stated in the compiled data"
---

# Toremifene
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

## Toremifene: From Breast Cancer to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Toremifene is an oral selective estrogen receptor modulator that has been marketed in the United States as a breast cancer drug (this is general knowledge, since the compiled data holds no indication text).
The TxGNN model predicts it may be effective for **HIV infectious disease**, but the support is thin: **0 clinical trials** and **1 publication**, and that publication is a preclinical antifungal study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled data (all license records have empty indication text) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of NDAs | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Toremifene is a known estrogen receptor antagonist related to tamoxifen, and its use in hormone-driven cancer is established. Any mechanistic link to HIV infectious disease therefore has to be inferred from indirect evidence.

The only linked publication (PMID 24520056, 2014) shows that estrogen receptor antagonists related to tamoxifen and toremifene have antifungal activity against *Cryptococcus*. They appear to act by binding EF-hand proteins such as calmodulin, and they synergize with fluconazole and amphotericin B in vitro. Cryptococcal meningitis is a major opportunistic infection in people with HIV/AIDS.

This evidence does **not** show activity against HIV itself. At most, it suggests a possible adjunctive role against an opportunistic infection in people living with HIV. The very high TxGNN score (0.9941) is a computational prediction only and should not be read as clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24520056](https://pubmed.ncbi.nlm.nih.gov/24520056/) | 2014 | Preclinical / in vitro | mBio | Tamoxifen- and toremifene-related estrogen receptor antagonists are fungicidal against *Cryptococcus*, bind EF-hand proteins, and synergize with fluconazole and amphotericin B. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020497 | Fareston (Kyowa Kirin, Inc.) | Tablet | Not available; status valid |
| ANDA208813 | Toremifene citrate (Rising Pharma Holdings, Inc.) | Tablet | Not available; status valid |
| ANDA212818 | Toremifene citrate (Novadoz Pharmaceuticals LLC) | Tablet | Not available; status valid |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (selective estrogen receptor modulator), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; the knowledge-graph contraindications below suggest monitoring of ECG/QT interval, electrolytes (potassium, calcium), and blood counts |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (derived from drug-disease relationships in the TxGNN knowledge graph, not from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, thrombocytopenia, potassium deficiency disease, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, leukopenia, and endometrial hyperplasia.
- **Drug Interactions**: The interaction query returned 100 records. The list below includes only the **Major** interactions among the 20 records shown, which are largely QT-related combinations:
  - Dexamethasone
  - Clarithromycin
  - Levofloxacin
  - Dolasetron
  - Palonosetron
  - Picosulfuric acid
  - Sodium sulfate
  - Polyethylene glycol (3350 with electrolytes)

  Moderate interactions include famotidine, pioglitazone, loperamide, aprepitant, bisacodyl, cimetidine, metreleptin, miconazole, nateglinide, lactitol, and lactulose. Metronidazole is a Minor interaction.

For label-based warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score and a single preclinical antifungal paper that does not show anti-HIV activity. There are no clinical trials, the evidence level is L5, and the drug is marketed in the US with 3 of 3 licenses valid.

**To proceed, the following is needed:**
- Direct evidence of anti-HIV activity, or a clearly defined adjunctive role in cryptococcal infection among people with HIV (in vitro, animal, then clinical studies)
- Mechanism of action data
- FDA package insert warnings and contraindications for formal safety screening, with particular attention to QT prolongation and its interactions with antiretroviral and antifungal drugs
- Clarification of the original approved indication and of the commercial availability of toremifene, which is marketed in the US with 3 of 3 licenses valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

