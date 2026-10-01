---
layout: default
title: Bremelanotide
parent: Model Prediction Only (L5)
nav_order: 466
evidence_level: L5
indication_count: 10
---

# Bremelanotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Bremelanotide: From Hypoactive Sexual Desire Disorder (HSDD) to Acne

## One-Sentence Summary

Bremelanotide (Vyleesi) is a melanocortin receptor agonist given by injection. The Evidence Pack does not state its approved indication; the title uses HSDD in premenopausal women from general knowledge of the US label, which should be checked against the package insert.
The TxGNN model predicts it may be effective for **acne**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (the approved indication text is empty); HSDD per general knowledge of the US label |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 100.00% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bremelanotide is a melanocortin receptor agonist, acting mainly on MC4R with activity at other melanocortin receptors. Detailed mechanism-of-action data is not available in the source record, so this description comes from the analysis of the predicted indication.

Melanocortin signaling, including MC1R and MC5R, has been reported in sebocytes and in skin inflammation. That makes a link to acne biologically plausible. The link is indirect and unverified. MC5R is the main receptor on sebaceous glands, and bremelanotide is not selective for it. Bremelanotide is also known to cause skin hyperpigmentation, which is a concern for a skin indication.

The relationship between the original indication and acne is still pending analysis. The 100% score should be read as a model output, not as evidence of efficacy.

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
| NDA210557 | Vyleesi (Cosette Pharmaceuticals, Inc.) | Injection | Not listed in source data |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records.
- **Skin effects**: Bremelanotide is known to cause skin hyperpigmentation, which matters for a dermatologic use.
- **Blood pressure**: Bremelanotide is known to raise blood pressure.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, registry, or literature support (L5). The mechanistic link to acne is weak and indirect, and known skin pigmentation and blood pressure effects add concerns. The other nine predicted indications, including mitochondrial oxidative phosphorylation disorder, exocrine pancreatic insufficiency, and retinopathy of prematurity, are also L5 and Hold, with weaker mechanistic links.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- The approved indication text and mechanism-of-action data from DrugBank
- Preclinical evidence on melanocortin receptors (especially MC5R) in sebocytes and acne models
- A literature and trial search for melanocortin agonists in acne
- An assessment of injectable delivery against the needs of an acne treatment, including a comparison with topical options
- A safety assessment of pigmentation and blood pressure effects in an acne population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

