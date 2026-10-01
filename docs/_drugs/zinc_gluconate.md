---
layout: default
title: Zinc Gluconate
parent: Model Prediction Only (L5)
nav_order: 1307
evidence_level: L5
indication_count: 10
---

# Zinc Gluconate
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

# Zinc Gluconate: From Cold Remedy (Marketed Labeling) to Anemia of Prematurity

## One-Sentence Summary

Zinc gluconate is marketed in the US mainly as an over-the-counter zinc cold remedy (lozenge and tablet products). The TxGNN model predicts it may be effective for **anemia of prematurity** with a very high score, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data (product names suggest common cold remedies) |
| Predicted New Indication | Anemia of prematurity |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, zinc gluconate is a zinc salt sold in oral and lozenge products. The license records do not give an approved indication, so the original indication cannot be confirmed from this dataset.

Zinc plays a general role in heme synthesis and erythropoiesis, so a link to anemia in preterm infants is plausible. This is an inference only. No trials or publications in the dataset address it, and without MOA data the link cannot be verified. The high score reflects model output, not clinical evidence.

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
| Not listed | Zinc Cold Therapy (Better Living Brands LLC) | Chewable tablet | Not listed |
| Not listed | Zinc Cold Therapy (Raritan Pharmaceuticals Inc) | Chewable tablet | Not listed |
| Not listed | Zinc Cold Therapy (Cardinal Health) | Tablet | Not listed |
| Not listed | CVS Health Cold Remedy (CVS Pharmacy, Inc) | Tablet | Not listed |
| Not listed | TopCare Zinc Cold Remedy (Topco Associates LLC) | Tablet | Not listed |

20 licenses are recorded in total; the five above are shown. Available forms are oral tablets, chewable tablets and lozenges.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.94%), but there are no clinical trials or publications for anemia of prematurity, so the evidence level is L5. Mechanism of action and safety data are also missing, so the prediction cannot be assessed further.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Search for studies on zinc and anemia or erythropoiesis in preterm infants
- Route and dose compatibility assessment for neonatal use, since current products are oral tablets and lozenges for general consumers

**Other predicted indications:** The second-ranked prediction, "injury," reaches L4 (preclinical studies only). Those studies are mixed across tissues and species, and none shows clinical benefit of zinc gluconate for a defined injury type.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

