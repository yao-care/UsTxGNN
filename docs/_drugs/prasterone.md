---
layout: default
title: Prasterone
parent: Model Prediction Only (L5)
nav_order: 1074
evidence_level: L5
indication_count: 10
monitor_inn: "PRASTERONE"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "severe nonproliferative diabetic retinopathy", "thrombophilia due to protein S deficiency, autosomal recessive", "scleroderma (disease)", "complement component 4a deficiency", "pseudo-von Willebrand disease", "primary release disorder of platelets"]
last_modified_at: 2026-10-14
description: "Prasterone: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Systemic lupus erythematosus"
---

# Prasterone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Prasterone: From Systemic Lupus Erythematosus to Heparin Cofactor 2 Deficiency
{: .text-alpha }

## One-Sentence Summary

Prasterone (DHEA) is a sex-steroid precursor whose original indications in the data compiled for this report are systemic lupus erythematosus, pediatric systemic lupus erythematosus, and psychologic dyspareunia. The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but this is a model-only prediction with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic lupus erythematosus; pediatric systemic lupus erythematosus; psychologic dyspareunia (US labeling for the vaginal insert covers dyspareunia due to vulvar and vaginal atrophy) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, prasterone (DHEA) is an endogenous steroid precursor that is converted in the body into androgens and estrogens. It has reported immunomodulatory properties, which is consistent with its use in lupus.

For heparin cofactor 2 deficiency, no mechanistic link has been established. This is a rare inherited serpin deficiency, and prasterone has no known effect on heparin cofactor II levels or function. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The high score therefore should not be read as biological support. Sex steroids may raise rather than lower thrombotic risk, so the prediction is of doubtful plausibility and carries a safety caveat.

Other top predictions show the same pattern. Most are coagulation or platelet disorders (factor V excess, antithrombin type 2 deficiency, thrombophilia, protein S deficiency, pseudo-von Willebrand disease, platelet release disorder), none with supporting evidence. Two have a loose indirect rationale:
- **Scleroderma:** an autoimmune connective tissue disease like lupus, and DHEA has immunomodulatory properties.
- **Complement C4A deficiency:** linked to lupus susceptibility.
- **Severe nonproliferative diabetic retinopathy:** only a speculative link through DHEA's anti-inflammatory and metabolic effects in preclinical models.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208470 | Intrarosa (Millicent US, Inc.) | Insert | Status: valid |
| Not available | DHEA (Deseret Biologicals, Inc.) | Liquid | Status: cancelled |

Pharmacology data indicate that prasterone (Intrarosa) was FDA approved for moderate to severe pain during sexual intercourse (dyspareunia) as a symptom of vulvar and vaginal atrophy in women. Both authorizations are now cancelled.

## Safety Considerations

- **Thrombotic risk:** Prasterone is converted to androgens and estrogens, and sex steroids may raise thrombotic risk and can lower free protein S. This is a concern for the predicted coagulation-related indications.
- **Pharmacological target:** Pharmacology data list the glycine receptor (all subtypes) as a target of DHEA. No other interaction data are available.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature, and no plausible mechanism. The coagulation-related predictions also raise a safety concern, since sex-steroid precursors may increase rather than reduce thrombotic risk. Both US authorizations are cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (FDA label)
- Mechanism of action data (e.g., from DrugBank)
- Preclinical or mechanistic evidence linking prasterone to heparin cofactor II function
- Thrombotic risk assessment for sex-steroid precursors in patients with coagulation disorders
- Route and formulation compatibility analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

