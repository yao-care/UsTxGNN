---
layout: default
title: Soybean Oil
parent: Model Prediction Only (L5)
nav_order: 1179
evidence_level: L5
indication_count: 1
---

# Soybean Oil
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

# Soybean Oil: From Parenteral Nutrition (Lipid Source) to Amenorrhea

## One-Sentence Summary

Soybean oil is mainly used as a caloric and essential fatty acid source in parenteral nutrition lipid emulsions (such as Intralipid), and as a pharmaceutical excipient.
The TxGNN model predicts it may be effective for **Amenorrhea**, but this rests on a model score alone: **0 clinical trials** and **0 publications** currently support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the regulatory records (used as a lipid source in parenteral nutrition) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, soybean oil is a nutritional lipid source and excipient rather than a drug with a defined pharmacological target. Its role in parenteral nutrition is to supply calories and essential fatty acids, so it has no proven efficacy in a reproductive condition.

One possible link is that soybean-derived phytoestrogens (isoflavones), or changes in lipid and energy status, could influence the hypothalamic-pituitary-ovarian axis, which controls menstruation. This link is weak. Refined soybean oil contains negligible isoflavones, so the phytoestrogen route is unlikely to apply.

The high score may instead reflect knowledge-graph connectivity artifacts, such as soy-related nodes linked to reproductive endocrine phenotypes, rather than a real pharmacological effect. This prediction should be treated as a hypothesis only.

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
| NDA020248 | Intralipid (Fresenius Kabi USA, LLC) | Emulsion | Not listed in the record |
| NDA018449 | Intralipid (Fresenius Kabi USA, LLC) | Emulsion | Not listed in the record |
| BLA103888 | Food - Plant Source, Soybean Glycine soja (Jubilant HollisterStier LLC) | Injection, solution | Not listed in the record |
| NDA020248 | Intralipid (Baxter Healthcare Corporation) | Emulsion | Not listed in the record |
| NDA018449 | Intralipid (ProPharma Distribution) | Emulsion | Not listed in the record |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). There are no registered trials or publications, no mechanism of action data, and no plausible pharmacological link, since refined soybean oil has negligible isoflavone content. The score may be a knowledge-graph artifact.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank (DB09422)
- A systematic literature search for soy-derived lipids or isoflavones and menstrual or ovarian function
- A check of whether the TxGNN score comes from generic soy-related graph connectivity rather than drug-specific evidence
- Route and formulation compatibility assessment (parenteral emulsion versus any oral or dietary use for amenorrhea)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

