---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 1047
evidence_level: L5
indication_count: 9
monitor_inn: "PIOGLITAZONE"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-30
description: "Pioglitazone: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Not recorded in the local data"
---

# Pioglitazone
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

## Pioglitazone: Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Pioglitazone is an oral insulin-sensitizing drug (a PPAR-gamma agonist) originally used to treat type 2 diabetes mellitus.
The TxGNN model (deep learning) predicts it may be effective for **Opsismodysplasia** (score 0.9959), but there are **0 clinical trials** and **0 publications** directly supporting this prediction. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 6) |
| Number of FDA Applications | 6 authorizations in total (1 NDA, 5 ANDAs), all cancelled |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pioglitazone is a PPAR-gamma agonist (thiazolidinedione class), its efficacy in type 2 diabetes is established, and its main effects are insulin sensitization and adipose tissue modulation.

Opsismodysplasia is a rare skeletal dysplasia caused by mutations in INPPL1 (SHIP2, a regulator of the PI3K pathway). Pioglitazone has no established mechanistic connection to this pathway, so any link is speculative. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions show the same pattern:
- **Stiff person syndrome (classic and focal variants, score 0.9950)**: a theoretical anti-inflammatory/immunomodulatory rationale. The identical scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Localized lipodystrophies (scores 0.9918–0.9930)**: PPAR-gamma-driven adipogenesis makes a biological link plausible, but these are local tissue processes with no supporting data for systemic pioglitazone.
- **Thiamine-responsive dysfunction syndrome (0.9948)** and **pancreatic agenesis (0.9918)**: no clear mechanistic link. In pancreatic agenesis, insulin sensitizers depend on endogenous insulin and would not address the core deficit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for opsismodysplasia.

(For the ninth-ranked prediction, pancreatic agenesis, seven publications were retrieved, but they concern PPAR agonists in type 2 diabetes or prediabetes and are indirect, not relevant to that disease.)

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021073 | Actos (Takeda Pharmaceuticals America, Inc.) | Tablet | Valid |
| ANDA200268 | Pioglitazone Hydrochloride (A-S Medication Solutions) | Tablet | Valid |
| ANDA207806 | Pioglitazone (Solco Healthcare LLC) | Tablet | Valid |
| ANDA202467 | Pioglitazone (Macleods Pharmaceuticals Limited) | Tablet | Valid |
| ANDA077210 | Pioglitazone (Bryant Ranch Prepack) | Tablet | Valid |

All six authorizations in the data compiled are listed as cancelled. Indication text was not available.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not label text): kidney disease, liver disease, gallbladder disease, congestive heart failure, adrenocortical insufficiency/Addison disease, thymus gland disease, infectious disease, and a large group of pituitary and gonadal deficiency conditions (hypopituitarism, growth hormone deficiency, hypogonadotropic hypogonadism, Kallmann syndrome, Sheehan syndrome, among others).
- **Drug Interactions**: 100 interactions were found. Examples among the entries reviewed:
  - Moderate: abiraterone, acetazolamide, hydrochlorothiazide, hydrocortisone, epinephrine, phenylephrine, pseudoephedrine, salbutamol, formoterol, alpelisib, ethanol, abametapir (topical), aloe vera leaf
  - Minor: nifedipine, ethinylestradiol, lipoic acid, topical corticosteroids (hydrocortisone, alclometasone, amcinonide), aminoglutethimide

Please refer to the package insert for label warnings, as these were not available in the data compiled.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model (deep learning) score, which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications for opsismodysplasia, no plausible mechanistic link to INPPL1/SHIP2 biology, and the drug is marketed in the US with 6 valid licenses. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a clear mechanistic hypothesis linking PPAR-gamma agonism to the INPPL1/PI3K pathway
- Preclinical evidence (cell or animal models of opsismodysplasia)
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Review of the cancelled licensure status and the current availability of the drug
- Consideration of better-supported alternatives among the other predictions (for example, the lipodystrophy indications), which would still require supporting data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

