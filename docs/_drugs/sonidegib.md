---
layout: default
title: Sonidegib
parent: Model Prediction Only (L5)
nav_order: 1174
evidence_level: L5
indication_count: 10
monitor_inn: "SONIDEGIB"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "trichothiodystrophy photosensitive", "skin cancer", "cutaneous adenocystic carcinoma", "benign neoplasm of sweat gland", "eccrine carcinoma", "obsolete cataract, microcephaly, failure to thrive, kyphoscoliosis syndrome"]
last_modified_at: 2026-10-14
description: "Sonidegib: predicted new indication Medulloblastoma with extensive nodularity (evidence level L5). Approved use: Basal cell carcinoma (skin carcinoma)"
---

# Sonidegib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Sonidegib: From Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

Sonidegib is an oral Hedgehog pathway inhibitor, originally used to treat basal cell carcinoma (a skin cancer).
The TxGNN model predicts it may be effective for **medulloblastoma with extensive nodularity**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
The prediction is biologically plausible but remains purely computational.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Basal cell carcinoma (skin carcinoma) |
| Predicted New Indication | Medulloblastoma with extensive nodularity |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active authorization) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sonidegib is a Smoothened (SMO) inhibitor. SMO is a key signal transducer of the Hedgehog pathway, and sonidegib suppresses aberrant Hedgehog signaling, the main driver of basal cell carcinoma. The data compiled for this report do not include a formal mechanism-of-action entry, so this description comes from the mechanistic analysis of the prediction.

Medulloblastoma, particularly the SHH subgroup and the nodular/desmoplastic variant, is also driven by Hedgehog signaling. This shared pathway makes the TxGNN prediction biologically reasonable.

Several concerns remain open:
- **Blood-brain barrier penetration:** it is unclear whether sonidegib reaches therapeutic levels in the brain.
- **Pediatric safety:** premature growth plate closure is a concern, and medulloblastoma often occurs in children.
- **Resistance:** downstream mutations (e.g., SUFU, GLI2) would make an SMO inhibitor ineffective.

Other predictions for this drug are mostly related to skin cancer. The "skin cancer" prediction is supported by a Phase 2 randomized trial (NCT01327053, n=230), but it largely restates the existing basal cell carcinoma indication rather than a true repurposing finding. Other predictions, such as xeroderma pigmentosum, have only a single case report. They are not the focus of this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for medulloblastoma with extensive nodularity.

---

## Literature Evidence

Currently no related literature available for medulloblastoma with extensive nodularity.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205266 (cancelled) | Odomzo (Sun Pharmaceutical Industries, Inc.) | Capsule | Not specified in the compiled data |

The only US authorization is cancelled, so product availability would need to be verified before any development work.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog/SMO inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Musculoskeletal toxicity and creatine kinase (CK) elevation; other parameters per package insert |
| Handling Protection | Embryo-fetal toxicity precautions are required; otherwise refer to the package insert |

---

## Safety Considerations

- **Drug Interactions:** The interaction screening found 100 interacting drugs in total. The first 20 returned are summarized below.
  - **Major:** aprepitant, dexamethasone, clarithromycin, clotrimazole, cobicistat
  - **Moderate:** cimetidine, metreleptin, miconazole, troglitazone, deferasirox
  - **Minor:** acid-suppressing agents such as famotidine, ranitidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole
- **Class concerns noted in the analysis:** musculoskeletal toxicity with CK elevation, embryo-fetal toxicity, and, for pediatric use, premature growth plate closure.

Please refer to the package insert for the full warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible because medulloblastoma is Hedgehog-driven. However, there is no clinical or published evidence for this indication (Evidence Level L5). The US authorization is cancelled, and the pediatric safety and brain-penetration concerns are significant.

**To proceed, the following is needed:**
- Preclinical or clinical evidence of sonidegib activity in SHH-subgroup and nodular/desmoplastic medulloblastoma
- Data on blood-brain barrier penetration
- Assessment of resistance risk from downstream mutations (SUFU, GLI2)
- A pediatric safety assessment, especially for growth plate effects
- FDA package insert warnings and contraindications
- Verification of current product availability, since the only US NDA is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

