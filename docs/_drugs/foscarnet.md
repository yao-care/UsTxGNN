---
layout: default
title: Foscarnet
parent: Model Prediction Only (L5)
nav_order: 736
evidence_level: L5
indication_count: 4
monitor_inn: "FOSCARNET"
predicted_indications: ["autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "rheumatoid arthritis", "diabetic nephropathy"]
last_modified_at: 2026-10-14
description: "Foscarnet: predicted new indication autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome (evidence level L5). Approved use: Not stated in the available data (approved-indication tex…"
---

# Foscarnet
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

## Foscarnet: From Cytomegalovirus Infection to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome
{: .text-alpha }

## One-Sentence Summary

Foscarnet is an injectable antiviral that inhibits viral DNA polymerase. The data compiled for this report do not list its original approved indication.
The TxGNN model (deep learning) predicts it may be effective for **autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome**, but **no clinical trials and no publications** support this prediction. The score comes from the TxGNN model alone and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available data (approved-indication text is blank in all authorizations) |
| Predicted New Indication | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome |
| TxGNN Prediction Score | 0.9956 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 6 of 6) |
| Number of NDAs | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general pharmacology, foscarnet is a pyrophosphate analog that inhibits viral DNA polymerase and reverse transcriptase, so its activity is antiviral.

The predicted condition is a rare inherited vascular and basement-membrane disorder (COL4A1-related) with no known viral cause. No mechanistic link between foscarnet and this syndrome was identified. The high TxGNN score (0.9956) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. With no supporting trials or literature, the prediction should be treated as a hypothesis only.

Other top-ranked predictions are equally weak:
- **Brain small vessel disease 1 with or without ocular anomalies**: a COL4A1-related genetic disorder with no viral component. Four retrieved papers concern CMV retinitis and appear only through ocular keyword overlap.
- **Rheumatoid arthritis**: foscarnet has no known immunomodulatory effect. The literature concerns CMV/EBV infections, with RA appearing only incidentally.
- **Diabetic nephropathy**: foscarnet is nephrotoxic, so this is a safety concern rather than a therapeutic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020068 | Foscavir (Clinigen Limited) | Injection, solution | Not stated (valid) |
| ANDA216602 | Foscarnet Sodium (Amneal) | Injection | Not stated (valid) |
| ANDA212483 | Foscarnet (Fresenius Kabi USA) | Injection, solution | Not stated (valid) |
| ANDA213001 | Foscarnet Sodium (Gland Pharma) | Injection, solution | Not stated (valid) |
| ANDA213987 | Foscarnet Sodium (Hikma) | Injection, solution | Not stated (valid) |

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for these.

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): long QT syndrome and torsades de pointes, epilepsy, kidney disease, neutropenia and related congenital neutropenias, anemia, and electrolyte or mineral disorders (potassium deficiency, hypercalcemia, nephrocalcinosis, hyperphosphatemia, hypophosphatemia, phosphorus metabolism disease).
- **Drug Interactions**: 100 interactions were recorded. Major-level interactions include:
  - Amphotericin B (including the lipid complex)
  - Dolasetron
  - Bupropion

  Moderate-level examples include famotidine, omeprazole, rabeprazole, dexamethasone, hydrocortisone, clarithromycin, and loperamide.
- **Nephrotoxicity and electrolyte disturbance**: the compiled assessment notes dose-limiting renal impairment and electrolyte disturbances (hypomagnesemia, hypocalcemia, hypokalemia). This is especially relevant for the kidney-related predicted indications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials, no relevant literature, and no plausible mechanism. Foscarnet is an antiviral, and the predicted condition is a non-viral genetic disorder. The drug is marketed in the US, with 6 of 6 licenses valid, and it carries significant renal and electrolyte toxicity.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- FDA package insert warnings and contraindications, which block safety screening
- Original approved indication text
- A biological hypothesis linking foscarnet to COL4A1-related disease, supported by preclinical evidence
- Review of the other top-ranked predictions, none of which currently has supporting evidence either
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

