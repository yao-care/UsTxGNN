---
layout: default
title: Nifurtimox
parent: Model Prediction Only (L5)
nav_order: 965
evidence_level: L5
indication_count: 7
monitor_inn: "NIFURTIMOX"
predicted_indications: ["congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "blood group incompatibility", "monoclonal gammopathy", "premalignant hematological system disease", "hematological disease associated with an acquired peripheral neuropathy"]
last_modified_at: 2026-10-14
description: "Nifurtimox: predicted new indication Congenital analbuminemia (evidence level L5). Approved use: Chagas disease"
---

# Nifurtimox
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

## Nifurtimox: From Chagas Disease to Congenital Analbuminemia
{: .text-alpha }

## One-Sentence Summary

Nifurtimox is a nitrofuran antiprotozoal, originally used to treat Chagas disease.
The TxGNN model predicts it may be effective for **Congenital Analbuminemia**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only prediction with no mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chagas disease |
| Predicted New Indication | Congenital analbuminemia |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, nifurtimox is a nitrofuran antiprotozoal that generates reactive oxygen species and nitro-radical metabolites in *Trypanosoma cruzi*. Its efficacy in Chagas disease is the basis for its original use.

This mechanism does not appear applicable to congenital analbuminemia. That disorder is a rare monogenic condition caused by loss-of-function variants in the *ALB* gene, and an antiparasitic prodrug has no plausible way to correct it. The high TxGNN score (0.9958) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predicted indications show the same pattern, with scores between 0.9906 and 0.9947, and none has supporting trials or literature:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Polyclonal hyperviscosity syndrome | 0.9947 | Nifurtimox has no known immunomodulatory or protein-lowering activity |
| 3 | Hyperamylasemia | 0.9947 | A laboratory finding with many causes; for nifurtimox, gastrointestinal adverse effects are the more relevant question |
| 4 | Blood group incompatibility | 0.9924 | An alloimmune process that nitrofurans do not target |
| 5 | Monoclonal gammopathy | 0.9916 | Only preclinical oxidative-stress work in some malignancies; nothing links it to plasma cell disorders |
| 6 | Premalignant hematological system disease | 0.9911 | A broad category not tied to a specific target |
| 7 | Hematological disease associated with an acquired peripheral neuropathy | 0.9906 | Nifurtimox is known to cause peripheral neuropathy, which runs counter to any benefit |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213464 (cancelled) | LAMPIT (Bayer Healthcare Pharmaceuticals Inc.) | Film-coated tablet (oral) | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions** (5 interactions identified):
  - **Major:** Ethanol
  - **Moderate:** Ritonavir, Tipranavir, *Bifidobacterium longum infantis*, *Lactobacillus acidophilus*
- **Additional safety signal:** Nifurtimox is known to cause peripheral neuropathy and gastrointestinal adverse effects. This matters especially for the neuropathy-associated and gastrointestinal-related predicted indications.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. No clinical trials or publications support it, and no plausible biological link exists between a nitrofuran antiprotozoal and a monogenic albumin deficiency. The only US authorization is cancelled. Evidence Level L5 does not justify advancing.

**To proceed, the following is needed:**
- Mechanism of action data for nifurtimox
- Package insert warnings and contraindications, needed for any safety screening
- A clear biological rationale linking nifurtimox to the predicted indication, supported by preclinical evidence
- A review of whether any of the predicted indications is better framed as a safety signal than as a therapeutic opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

