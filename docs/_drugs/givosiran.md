---
layout: default
title: Givosiran
parent: Model Prediction Only (L5)
nav_order: 751
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Givosiran: predicted new indication Hepatoportal sclerosis (evidence level L5). Approved use: Hepatic porphyria"
monitor_inn: "GIVOSIRAN"
predicted_indications: ["hepatoportal sclerosis", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "chronic hepatitis C virus infection", "glycogen storage disease due to hepatic glycogen synthase deficiency", "chronic hepatitis B virus infection", "disorder of phenylalanine metabolism"]
---

# Givosiran
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Givosiran: From Hepatic Porphyria to Hepatoportal Sclerosis
{: .text-alpha }

## One-Sentence Summary

Givosiran is a liver-targeted siRNA therapy, originally used to treat hepatic porphyria.
The TxGNN model predicts it may be effective for **Hepatoportal Sclerosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic porphyria |
| Predicted New Indication | Hepatoportal sclerosis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, givosiran is a GalNAc-conjugated siRNA that silences hepatic ALAS1, the first enzyme in heme biosynthesis. This lowers production of the neurotoxic intermediates ALA and PBG, which drive attacks in acute hepatic porphyria.

For hepatoportal sclerosis (non-cirrhotic portal hypertension with obliterative portal venopathy), no plausible link to ALAS1 suppression is established. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Several other predictions share an identical score (1.0000), including primitive portal vein thrombosis, hepatopulmonary syndrome, idiopathic copper-associated cirrhosis and early-onset familial noncirrhotic portal hypertension. This points to a shared model artifact rather than disease-specific signals.

**Other predictions reviewed.** The other predictions, including chronic hepatitis B and C, glycogen storage disease and phenylalanine metabolism disorder, have no supporting data and no evident mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hepatoportal sclerosis.

---

## Literature Evidence

Currently no related literature available for hepatoportal sclerosis.

For reference, the only prediction with literature is ADP porphyria (rank 9):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | Case report | Front Genet | Lack of response to givosiran in a patient with ALAD porphyria |
| [42443962](https://pubmed.ncbi.nlm.nih.gov/42443962/) | 2026 | Case report | Orphanet J Rare Dis | Hepatic-only ALA suppression had limited effect in an ADP patient; treatment targeting both hepatic and erythroid ALA production was used |
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | RCT post-hoc analysis | Orphanet J Rare Dis | Disease burden in acute hepatic porphyria from the Phase 3 ENVISION trial (indirect for ADP) |
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | Review / trial analysis | J Intern Med | Givosiran significantly reduces attack rates in acute intermittent porphyria |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Clinical study | Sci Rep | Efficacy and safety of givosiran in 10 Japanese patients with AHP (expanded access, open-label) |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Review | Blood | RNA interference therapy in acute hepatic porphyrias |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Review | Drug Des Devel Ther | Givosiran design, development and place in therapy for adult AHP |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | PK/PD modeling | CPT Pharmacometrics Syst Pharmacol | Model of urinary ALA reduction after givosiran in AHP |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | Review | Rev Clin Esp | Therapeutic approach to acute crises of hepatic porphyrias |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212194 (cancelled) | GIVLAARI | Injection, solution | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Drug Interactions**: 87 interactions were identified. The only one rated Major is **eliglustat**. The others shown are rated Moderate, including aminoglycosides (kanamycin, neomycin, streptomycin), vancomycin, amphotericin B formulations, aminosalicylates (mesalazine, balsalazide, olsalazine, sulfasalazine), alosetron, metoclopramide, naltrexone, exenatide, fenfluramine, dexfenfluramine and caffeine.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Hepatoportal sclerosis is supported only by a model score, with no trials, no literature and no plausible mechanistic link to ALAS1 silencing. The US NDA is also listed as cancelled. The one prediction with literature, ADP porphyria, is essentially an extension of the approved indication, and its evidence is limited to mixed case reports.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A mechanistic hypothesis linking ALAS1 suppression to obliterative portal venopathy, with preclinical support
- Clarification of the cancelled NDA status and the current availability of the product
- If the team wants to pursue the best-supported prediction instead, a focused review of ADP porphyria cases, given the mixed responses reported
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

