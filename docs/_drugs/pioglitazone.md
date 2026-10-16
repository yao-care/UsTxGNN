---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 1047
evidence_level: L5
indication_count: 9
monitor_inn: "PIOGLITAZONE"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is an oral insulin-sensitizing drug (a PPAR-gamma agonist) originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Opsismodysplasia** (score 99.59%), but there are **0 clinical trials** and **0 publications** directly supporting this prediction. It is a graph-based prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses in the data compiled) |
| Number of NDAs | 6 authorizations in total (1 NDA, 5 ANDAs), all cancelled |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pioglitazone is a PPAR-gamma agonist (thiazolidinedione class), its efficacy in type 2 diabetes is established, and its main effects are insulin sensitization and adipose tissue modulation.

Opsismodysplasia is a rare skeletal dysplasia caused by mutations in INPPL1 (SHIP2, a regulator of the PI3K pathway). Pioglitazone has no established mechanistic connection to this pathway, so any link is speculative. The high TxGNN score reflects graph-based association rather than independent biological or clinical evidence.

Other top-ranked predictions show the same pattern:
- **Stiff person syndrome (classic and focal variants, score 99.50%)**: a theoretical anti-inflammatory/immunomodulatory rationale, with identical scores suggesting a shared graph neighborhood rather than independent evidence.
- **Localized lipodystrophies (scores 99.18%–99.30%)**: PPAR-gamma-driven adipogenesis makes a biological link plausible, but these are local tissue processes with no supporting data for systemic pioglitazone.
- **Thiamine-responsive dysfunction syndrome (99.48%)** and **pancreatic agenesis (99.18%)**: no clear mechanistic link. In pancreatic agenesis, insulin sensitizers depend on endogenous insulin and would not address the core deficit.

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
| NDA021073 | Actos (Takeda Pharmaceuticals America, Inc.) | Tablet | Cancelled |
| ANDA200268 | Pioglitazone Hydrochloride (A-S Medication Solutions) | Tablet | Cancelled |
| ANDA207806 | Pioglitazone (Solco Healthcare LLC) | Tablet | Cancelled |
| ANDA202467 | Pioglitazone (Macleods Pharmaceuticals Limited) | Tablet | Cancelled |
| ANDA077210 | Pioglitazone (Bryant Ranch Prepack) | Tablet | Cancelled |

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
The prediction is supported only by a graph-based score. There are no clinical trials or publications for opsismodysplasia, no plausible mechanistic link to INPPL1/SHIP2 biology, and all US licenses are cancelled. Evidence level is L5.

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

