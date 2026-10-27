---
layout: default
title: Bupivacaine
parent: Model Prediction Only (L5)
nav_order: 477
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Bupivacaine: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Dermatitis"
monitor_inn: "BUPIVACAINE"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
---

# Bupivacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Bupivacaine: From Dermatitis to Acrodermatitis Chronica Atrophicans
{: .text-alpha }

## One-Sentence Summary

Bupivacaine is an amide local anesthetic. In the knowledge graph used for this analysis, its original indication is recorded as dermatitis.
The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 13 (all cancelled; 2 NDAs and 11 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, bupivacaine is an amide local anesthetic that blocks voltage-gated sodium channels.

Acrodermatitis chronica atrophicans is a late skin manifestation of *Borrelia* infection (Lyme disease) and is treated with antibiotics. A local anesthetic has no plausible antimicrobial or disease-modifying role. The high TxGNN score (0.992) is a model output only. It most likely reflects the drug's link to dermatitis in the knowledge graph rather than a biological rationale.

The other top predictions face the same problem:
- **Neonatal dermatomyositis** (99.15%): an immune-mediated muscle and skin disease. Bupivacaine can at most give local pain relief and is myotoxic at high concentrations, which is a concern in muscle inflammation and in neonates.
- **Secondary childhood interstitial lung disease associated with a connective tissue disease** (99.11%): driven by immune inflammation and fibrosis, which sodium channel blockade does not address.
- **Amyopathic dermatomyositis** (99.03%): driven by immune dysregulation. Bupivacaine has no known immunomodulatory role.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 13 US authorizations are cancelled. The first five are listed below. The data compiled for this report contain no approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA204842 | Bupivacaine Hydrochloride | Injection, solution | Asclemed USA, Inc. | Cancelled |
| NDA016964 | Marcaine | Injection, solution | Hospira, Inc. | Cancelled |
| ANDA091487 | Bupivacaine Hydrochloride | Injection, solution | Fosun Pharma USA Inc. | Cancelled |
| ANDA070590 | 0.25% Bupivacaine HCl | Injection, solution | HF Acquisition Co LLC, DBA HealthFirst | Cancelled |
| ANDA207183 | Bupivacaine Hydrochloride | Injection, solution | A-S Medication Solutions | Cancelled |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): hypertension, liver failure and liver disease, kidney disease, epilepsy, COPD and respiratory failure, diabetes and diabetic ketoacidosis, hypothyroidism and myxedema, coronary artery disease, myocardial infarction, atrial fibrillation, heart conduction disease, sudden cardiac arrest, hypotensive disorder, inflammatory bowel disease, benign prostatic hyperplasia, angle-closure glaucoma, hemoglobinopathy, potassium deficiency, substance abuse/dependence, and others. These come from graph relationships and should be verified against the package insert.
- **Drug interactions**: 56 interactions are recorded. Two are rated Moderate: **aprepitant** and **liposomal morphine**. Others, such as atropine, dexamethasone, prednisone, simvastatin, ondansetron, and vancomycin, have an unrated severity.
- Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no clinical trials or publications, and no plausible mechanism links a local anesthetic to *Borrelia*-related skin atrophy. The drug also has no valid US authorization, and the safety data are incomplete.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data to evaluate any biological link
- Preclinical or clinical evidence for the predicted indication (none exists in the compiled data)
- Clarification of why the knowledge graph links bupivacaine to dermatitis, and whether the other predicted indications are better candidates
- Review of route and formulation compatibility (not yet assessed; only injectable forms exist)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

