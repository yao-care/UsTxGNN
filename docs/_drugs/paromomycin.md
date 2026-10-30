---
layout: default
title: Paromomycin
parent: Model Prediction Only (L5)
nav_order: 1016
evidence_level: L5
indication_count: 8
monitor_inn: "PAROMOMYCIN"
predicted_indications: ["idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatic porphyria", "acute urate nephropathy", "peritonitis"]
last_modified_at: 2026-10-30
description: "Paromomycin: predicted new indication Idiopathic copper-associated cirrhosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Paromomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Paromomycin: Idiopathic copper-associated cirrhosis
{: .text-alpha }

## One-Sentence Summary

Paromomycin is an oral, poorly absorbed aminoglycoside antibiotic, originally linked to the treatment of hepatic coma and hepatic encephalopathy.
The TxGNN model predicts it may be effective for **idiopathic copper-associated cirrhosis**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
This is a computational prediction only, with no direct supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Idiopathic copper-associated cirrhosis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, paromomycin is an aminoglycoside that is poorly absorbed from the gut, so it acts mainly by reducing intestinal bacteria. This gut-decontaminating effect is the basis of its use in hepatic encephalopathy, where gut-derived toxins such as ammonia contribute to disease.

The predicted indication, idiopathic copper-associated cirrhosis, is a chronic liver disease. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No direct mechanistic connection to copper accumulation or copper-driven liver injury has been established. Any rationale would depend on speculative gut-liver axis modulation in chronic liver disease.

The same score (0.9990) was assigned to several other liver and portal conditions, such as hepatoportal sclerosis, hepatopulmonary syndrome, and portal vein thrombosis. This suggests the scores reflect network proximity to the original liver indications and are not specific to this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for idiopathic copper-associated cirrhosis.

For context, the next-ranked prediction, peritonitis, has 16 associated publications. They cover amebiasis and Leishmania in vitro or formulation work, and none study peritonitis treatment, so they are not evidence for any liver indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA065173 (cancelled) | Humatin | Capsule (oral) | Not available |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): kidney disease, pyoureter, hearing loss disorder, and X-linked mixed deafness with perilymphatic gusher. These are consistent with the known nephrotoxicity and ototoxicity of aminoglycosides.
- **Drug Interactions**: 36 interactions were identified, including:
  - **Major**: neuromuscular blockers (cisatracurium, atracurium, doxacurium, metocurine, mivacurium) and live cholera vaccine (*Vibrio cholerae* CVD 103-HgR).
  - **Moderate**: proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, rabeprazole), estrogens (ethinylestradiol, estradiol, mestranol), methotrexate, mycophenolate mofetil, picosulfuric acid, enflurane, and indium In-111 oxyquinoline.
  - **Minor**: digoxin.

Please refer to the package insert for the full warnings and contraindications. Label data was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature, and no established mechanistic link to copper-associated cirrhosis. The only US license is cancelled, and the label safety information is missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Preclinical or mechanistic evidence linking gut decontamination or the gut-liver axis to copper-associated liver injury
- Review of renal and hearing safety for any chronic liver disease population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

