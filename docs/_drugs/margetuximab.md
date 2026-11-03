---
layout: default
title: Margetuximab
parent: Model Prediction Only (L5)
nav_order: 888
evidence_level: L5
indication_count: 1
monitor_inn: "MARGETUXIMAB"
predicted_indications: ["drug-induced osteoporosis"]
last_modified_at: 2026-11-03
description: "Margetuximab: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Margetuximab
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

## Margetuximab: Drug-induced osteoporosis
{: .text-alpha }

## One-Sentence Summary

Margetuximab is an Fc-engineered anti-HER2 monoclonal antibody that enhances immune-cell killing (ADCC).
The TxGNN model predicts it may be relevant to **drug-induced osteoporosis**, but **no clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9929 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Margetuximab binds HER2 (ERBB2) and has an engineered Fc region that increases binding to CD16A, which strengthens antibody-dependent cell-mediated cytotoxicity. Detailed mechanism-of-action data are not available in the data compiled for this report, which limits how far the link can be checked.

The model's score is very high (0.9929), but no known biological pathway connects HER2 targeting to the prevention or treatment of drug-induced bone loss. The prediction most likely reflects network proximity in the model's training data rather than a real mechanism. At this stage it should be treated as a hypothesis only, and no similarity to the drug's existing use or route compatibility has been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761150 | MARGENZA (MacroGenics, Inc) | Injection, solution, concentrate | Indication text not available in the data compiled; status listed as valid |

The product is a single-ingredient biologic from MacroGenics, Inc, and the licence is currently valid.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody with enhanced immune-effector function) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The only recorded item is a pharmacological target relationship with HER2 (ERBB2); no drug–drug interaction with a severity level is recorded.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is high, but there is no clinical or published evidence for drug-induced osteoporosis, and no plausible mechanism links HER2 targeting to bone loss. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing
- Mechanism-of-action data
- Preclinical bone-biology evidence (for example, bone density or osteoclast/osteoblast models) showing a plausible link
- Any clinical or observational data on bone outcomes in patients treated with margetuximab

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

