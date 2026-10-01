---
layout: default
title: Fomepizole
parent: Model Prediction Only (L5)
nav_order: 734
evidence_level: L5
indication_count: 1
---

# Fomepizole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Fomepizole: From Poisoning Antidote to Sclerosing Cholangitis

## One-Sentence Summary

Fomepizole is a marketed injectable drug that is generally known as an antidote for methanol and ethylene glycol poisoning (the US license records provided contain no indication text).
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but this rests on the model score alone: **0 clinical trials** and **0 publications** support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records provided (generally known use: antidote for methanol and ethylene glycol poisoning) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.28% (model rank 16015) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (all are generic ANDA-type authorizations) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Fomepizole is generally known as a competitive alcohol dehydrogenase inhibitor. Its established use is in toxic alcohol poisoning, which is unrelated to bile duct disease.

No plausible pathway from fomepizole to sclerosing cholangitis has been established in the provided data. Speculative links, such as effects on hepatic alcohol or aldehyde metabolism or on oxidative stress, are unverified. The high score (0.993) may reflect knowledge-graph topology rather than real biology, so it should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The license records list no approved indication text, so that column is replaced by the manufacturer.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA078537 | Fomepizole | Injection, solution | Navinta LLC |
| ANDA078368 | Fomepizole | Injection, solution | American Regent, Inc. |
| ANDA216791 | Fomepizole | Injection | Gland Pharma Limited |
| ANDA216791 | Fomepizole | Injection | Sagent Pharmaceuticals |
| ANDA078639 | Fomepizole | Injection, solution | Mylan Institutional LLC |

All products are injectables. Only 5 of the 6 licenses are listed in the input.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no trials, no literature, and no established mechanism linking fomepizole to sclerosing cholangitis. The safety data are also missing, so safety screening cannot start.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking; obtain from the FDA label)
- Mechanism of action data (for example, from DrugBank)
- A systematic search of PubMed, ClinicalTrials.gov and ICTRP for fomepizole in cholestatic or biliary disease
- A testable mechanistic hypothesis, ideally supported by preclinical data, that connects alcohol dehydrogenase inhibition to bile duct injury or fibrosis
- Route and regimen compatibility assessment: the product is injectable only, while sclerosing cholangitis is a chronic condition

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

