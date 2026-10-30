---
layout: default
title: Sodium Fluoride
parent: Model Prediction Only (L5)
nav_order: 1170
evidence_level: L5
indication_count: 7
monitor_inn: "SODIUM FLUORIDE"
predicted_indications: ["epiglottitis", "urinary tract infection (disease)", "Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "laryngitis"]
last_modified_at: 2026-10-30
description: "Sodium Fluoride: predicted new indication Epiglottitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Sodium Fluoride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Sodium Fluoride: Epiglottitis
{: .text-alpha }

## One-Sentence Summary

Sodium fluoride is a fluoride salt, listed in the data compiled for this report under the original indication of vitamin deficiency disorder. It is marketed in the US mainly as oral and dental products.
The TxGNN model predicts it may be effective for **epiglottitis**, but this rests on the model score alone: **0 clinical trials** and **0 publications** support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of FDA Applications | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sodium fluoride is best known as a topical and dietary dental-caries preventive. Its predicted relationship to vitamin deficiency disorder comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Epiglottitis is an acute airway infection, typically caused by *Haemophilus influenzae* type b or other bacteria. It is treated with systemic antibiotics and airway management. Nothing in the data compiled for this report shows an antibacterial or anti-inflammatory mechanism of sodium fluoride relevant to this condition. The very high score (0.999) is most likely a TxGNN model (deep learning) artifact, not a mechanistic signal.

The other top predictions show the same pattern. They are urinary tract infection, Ureaplasma urethritis, gonococcal urethritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis and laryngitis. All score above 0.99, and none has clinical-trial evidence. Ureaplasma and gonococcal urethritis have identical scores, which may reflect similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for epiglottitis.

For the closely related prediction, laryngitis (rank 7), four papers were retrieved. None supports a therapeutic role, because they are keyword matches:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29245332](https://pubmed.ncbi.nlm.nih.gov/29245332/) | 2017 | Case report | Medicine | Elevated 18F-NaF uptake in the cricoid cartilage of a patient with laryngeal carcinoma (diagnostic imaging, not treatment) |
| [42721223](https://pubmed.ncbi.nlm.nih.gov/42721223/) | 2026 | Imaging study | Cartilage | [18F]NaF and [18F]FDG PET/CT used to assess calcification and glucose metabolism in thyroid cartilage with age |
| [24178785](https://pubmed.ncbi.nlm.nih.gov/24178785/) | 2013 | Animal toxicity study | Biol Trace Elem Res | High dietary fluorine suppressed intestinal development in broilers |
| [235491](https://pubmed.ncbi.nlm.nih.gov/235491/) | 1975 | In vitro | Infect Immun | Ammonium chloride blocked diphtheria toxin action in cultured cells (not directly about fluoride therapy) |

## US Market Information

All three US authorizations in the data are valid, and none carries approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M021 | Anticavity fluoride rinse | Mouthwash | Not available |
| M022 | Sensodyne Pronamel | Paste | Not available |
| Not available | Acclean Foam Fluoride 60 Second Application | Aerosol, foam | Not available |

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not available. No drug interactions were found in the interaction query.

- **Knowledge-graph contraindication signals** (these come from graph relationships, not label text): kidney disease, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, hyperparathyroidism, osteitis fibrosa, hypercalcemia, phosphorus metabolism disease, sarcoidosis, pyoureter, constipation disorder, lytic metastatic bone lesion, and dental fluorosis.

Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or relevant publications (Evidence Level L5). No plausible mechanism links sodium fluoride to epiglottitis, which is already managed with established antibiotic therapy. The drug is marketed, with 3 valid US authorizations, and the safety package is incomplete.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Any preclinical evidence of antibacterial or anti-inflammatory activity relevant to epiglottitis
- An assessment of route compatibility, since current products are dental or topical, while epiglottitis is an acute airway infection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

