---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 63
evidence_level: L5
indication_count: 9
monitor_inn: "ACARBOSE"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-11-12
description: "Acarbose: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Acarbose
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

## Acarbose: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Acarbose is an oral alpha-glucosidase inhibitor, originally used to treat type 2 diabetes mellitus.
The TxGNN model (deep learning) predicts it may be effective for **classic stiff person syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 5 of 9) |
| Number of FDA Applications | 9 (active: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acarbose is an alpha-glucosidase inhibitor that acts in the gut to slow carbohydrate digestion and lower postprandial blood glucose. Its efficacy in type 2 diabetes is established.

For stiff person syndrome, no clear mechanistic link exists. The condition is an autoimmune disorder of GABAergic neurotransmission, typically involving anti-GAD65 antibodies. The high score probably reflects network proximity through autoimmune diabetes and GAD autoimmunity, not a direct pharmacological rationale. Acarbose has no known action on the nervous system or on the autoimmune process.

The second-ranked prediction, focal stiff limb syndrome (score 0.9965), is a focal variant of the same spectrum and likely reflects the same similarities the model learned between related diseases. Other lower-ranked predictions (thiamine-responsive dysfunction syndrome, opsismodysplasia, several localized lipodystrophies, and pancreatic agenesis) also have no clinical evidence, and their links to acarbose are at best indirect (a shared diabetes or metabolic phenotype).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

For reference, the literature retrieved for the lower-ranked prediction of pancreatic agenesis concerns type 2 diabetes, insulin autoimmune syndrome, and animal models, and does not address that condition directly. One animal study (PMID 10094112, 1999) showed that acarbose prevented and reversed metabolic abnormalities in a diabetic rat model, which supports its established antidiabetic use rather than any new indication.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA077532 | ACARBOSE | WATSON LABS | Tablet; oral | Valid |
| ANDA078441 | ACARBOSE | IMPAX LABS | Tablet; oral | Valid |
| ANDA078470 | ACARBOSE | HIKMA | Tablet; oral | Valid |
| ANDA090912 | ACARBOSE | STRIDES PHARMA | Tablet; oral | Valid |
| ANDA091343 | ACARBOSE | SOMERSET THERAPS LLC | Tablet; oral | Valid |

Showing 5 of 9 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, pyoureter, liver disease, gallbladder disease, cirrhosis of liver, inflammatory bowel disease, hypoglycemia, injury.
- **Drug Interactions**: 100 interactions were identified. Examples of moderate-level interactions include acetazolamide, salbutamol, aloe vera leaf, alpelisib, amprenavir, aripiprazole, asenapine, asparaginase, atazanavir, bedaquiline, bendroflumethiazide, benzphetamine, benzthiazide, and betamethasone. Minor-level examples include albiglutide, alclometasone (topical), lipoic acid, amcinonide, and anisindione.

Please refer to the package insert for label warnings and contraindications, as this information has not yet been compiled.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5), with no clinical trials or literature. There is no plausible pharmacological link between an intestinal alpha-glucosidase inhibitor and an autoimmune neurological disorder.

<!-- review:begin us-lic-20261105-acarbose-1 -->

> **Review correction (2026-11-05)**: Originally stated: "There is no plausible pharmacological link between an intestinal alpha-glucosidase inhibitor and an autoimmune neurological disorder. The drug is marketed in the US, and all 3 licenses are valid." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The FDA data list 9 FDA applications or NDC listings for this drug, 5 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-acarbose-1 -->

**To proceed, the following is needed:**
- Mechanism of action data, and a plausible mechanistic hypothesis for stiff person syndrome
- FDA package insert warnings and contraindications, to enable safety screening
- Any preclinical or clinical evidence in stiff person syndrome or related conditions
- Clarification of current US market and supply status

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "The drug is marketed in the US, and all 3 licenses are valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

