---
layout: default
title: Liothyronine
parent: Model Prediction Only (L5)
nav_order: 863
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "LIOTHYRONINE"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Carney complex", "peripheral dysostosis", "Potter sequence", "acrodysostosis with or without hormone resistance", "myxoma", "angiomyxoma", "hypotrichosis simplex of the scalp"]
description: "Liothyronine: predicted new indication Renal hypodysplasia/aplasia (evidence level L5). Approved use: Not recorded in the local data"
---

# Liothyronine
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

## Liothyronine: Renal hypodysplasia/aplasia
{: .text-alpha }

## One-Sentence Summary

Liothyronine is a synthetic form of the thyroid hormone T3, originally used to treat hypothyroidism and other thyroid conditions such as goiter and thyroid cancer.
The TxGNN model (deep learning) predicts it may be effective for **renal hypodysplasia/aplasia**, but the prediction rests only on the model score, with **0 clinical trials** and **0 publications** supporting it.
No plausible mechanism links thyroid hormone replacement to this congenital kidney malformation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal hypodysplasia/aplasia |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 5) |
| Number of NDAs | 5 (all ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, liothyronine is the active form of thyroid hormone (T3). Its efficacy in hypothyroidism is well established, since it replaces the missing hormone. Its mechanistic applicability to renal hypodysplasia/aplasia is not supported.

Renal hypodysplasia/aplasia is a developmental malformation in which the kidneys form incompletely or not at all. Hormone replacement cannot restore missing or malformed organs. The very high TxGNN score (0.9995) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions show the same pattern. Bilateral renal agenesis, Potter sequence, myxoma, and angiomyxoma likely reflect similarities the model learned between related diseases or names. Acrodysostosis has an indirect link through hormone resistance and associated hypothyroidism, and it is the only prediction with a modest body of literature (graded L4, "Research Question"). That literature is mostly generic thyroid hormone research, and none of it appears to study acrodysostosis directly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|-----------|
| ANDA091382 | liothyronine sodium | Tablet | Sun Pharmaceutical Industries, Inc. | Valid |
| ANDA214803 | Liothyronine sodium | Tablet | A-S Medication Solutions | Valid |
| ANDA200295 | Liomny | Tablet | SIGMAPHARM LABORATORIES, LLC | Valid |
| ANDA211510 | Liothyronine Sodium | Tablet | Teva Pharmaceuticals USA, Inc. | Valid |
| ANDA090097 | Liothyronine Sodium | Tablet | Golden State Medical Supply, Inc. | Valid |

Approved indication text is not available for these authorizations.

---

## Safety Considerations

- **Disease contraindications (from the knowledge graph, not label text):**
  - Hypertension and hypertensive disorders
  - Pituitary hormone deficiency conditions, including hypopituitarism, growth hormone deficiency, hypogonadotropic hypogonadism, Kallmann syndrome, and Sheehan syndrome
  - Osteoporosis and postmenopausal osteoporosis
  - Diabetes mellitus and diabetic ketoacidosis
  - Coronary artery disease and myocardial infarction
  - Thymus gland disease
- **Drug Interactions:** 100 interactions were found, and all 20 listed are Moderate severity.
  - Antidiabetic agents: acarbose, alogliptin, albiglutide, dulaglutide, linagliptin, metformin, pioglitazone, chlorpropamide, and the SGLT2 inhibitors canagliflozin, dapagliflozin, and empagliflozin
  - Acid suppressants: omeprazole, rabeprazole, and dexlansoprazole
  - Sympathomimetics: epinephrine, isometheptene, and diethylpropion
  - Minerals and antacids: calcium phosphate, calcium acetate, and magnesium oxide

Label warnings and contraindications were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. There are no clinical trials and no literature, and no credible biological mechanism for thyroid hormone replacement to correct a congenital kidney malformation. The drug is currently marketed in the US, with 5 valid licenses.

**To proceed, the following is needed:**
- A plausible mechanistic rationale, which requires the drug's mechanism of action data
- Preclinical or clinical evidence specific to renal hypodysplasia/aplasia
- Package insert warnings and contraindications to complete the safety review
- If a repurposing direction is pursued, a better-supported alternative such as acrodysostosis with hormone resistance, which would need direct studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

