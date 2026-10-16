---
layout: default
title: Erdafitinib
parent: Model Prediction Only (L5)
nav_order: 665
evidence_level: L5
indication_count: 6
monitor_inn: "ERDAFITINIB"
predicted_indications: ["pulmonary hypertension", "kyphoscoliotic heart disease", "amenorrhea (disease)", "rheumatoid arthritis", "amyotrophic lateral sclerosis", "brachydactyly-syndactyly syndrome"]
last_modified_at: 2026-10-14
description: "Erdafitinib: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Erdafitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Erdafitinib: From an Unspecified Original Indication to Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib is an oral pan-FGFR (FGFR1-4) tyrosine kinase inhibitor sold in the US as BALVERSA, and the data compiled for this report do not state its original approved indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a computational prediction only, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single NDA is listed as cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the compiled data. Erdafitinib is known to be a pan-FGFR tyrosine kinase inhibitor. FGF/FGFR signaling has been implicated in pulmonary vascular remodeling and smooth muscle proliferation, so a biologically plausible link to pulmonary hypertension exists, but it has not been validated.

The original indication text was empty in the compiled data, so the relationship between the original and the predicted indication cannot be assessed. The high TxGNN score (0.994) is a model output and not evidence of efficacy.

There is also a safety concern. FGFR inhibition is associated with hyperphosphatemia and ocular toxicity, and these would need careful evaluation in a vascular disease setting.

Other top-ranked predictions are even weaker: kyphoscoliotic heart disease, amenorrhea, amyotrophic lateral sclerosis and brachydactyly-syndactyly syndrome have no clear mechanistic rationale or supporting studies. Rheumatoid arthritis has a plausible but preclinical-level rationale, and its only retrieved publication is a general kinase inhibitor review with no RA-specific data on erdafitinib.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for pulmonary hypertension.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212018 (cancelled) | BALVERSA (Janssen Products LP) | Tablet, film coated (oral) | Not listed in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Serum phosphate and eye examinations are relevant to the FGFR inhibitor class. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screening completed with 100 interactions recorded. The first 20 are shown in the compiled data, and these include the following.
  - **Major**: cholecalciferol, calcifediol, calcitriol, dexamethasone, clarithromycin, calcium phosphate, calcium acetate, magnesium oxide, magnesium sulfate, magnesium chloride
  - **Moderate**: metformin, loperamide, saxagliptin, linagliptin, empagliflozin, eliglustat, naldemedine, naloxegol, prucalopride, rifaximin

Label warnings and contraindications were not available in the compiled data. Please refer to the package insert for them.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no clinical trials or relevant literature, and the evidence level is L5. The only US license is cancelled, and the label warnings and original indication data are missing. Safety screening cannot proceed without the package insert.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- The original approved indication text
- Preclinical evidence for FGFR inhibition in pulmonary vascular remodeling
- Assessment of the safety risks of FGFR inhibition (hyperphosphatemia, ocular toxicity) in a vascular disease setting
- Clarification of the cancelled US market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

