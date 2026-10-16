---
layout: default
title: Liothyronine
parent: Model Prediction Only (L5)
nav_order: 863
evidence_level: L5
indication_count: 10
monitor_inn: "LIOTHYRONINE"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "nodular goiter (disease)", "Carney complex", "peripheral dysostosis", "Potter sequence", "acrodysostosis with or without hormone resistance", "myxoma", "angiomyxoma", "hypotrichosis simplex of the scalp"]
last_modified_at: 2026-10-14
description: "Liothyronine: predicted new indication Renal hypodysplasia/aplasia (evidence level L5). Approved use: Hypothyroidism (also myxedema, congenital hypothyroidism, goiter…"
---

# Liothyronine
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

# Liothyronine: From Hypothyroidism to Renal Hypodysplasia/Aplasia

## One-Sentence Summary

Liothyronine is a synthetic form of the thyroid hormone T3, originally used to treat hypothyroidism and other thyroid conditions such as goiter and thyroid cancer.
The TxGNN model predicts it may be effective for **renal hypodysplasia/aplasia**, but the prediction is graph-based only, with **0 clinical trials** and **0 publications** supporting it.
No plausible mechanism links thyroid hormone replacement to this congenital kidney malformation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism (also myxedema, congenital hypothyroidism, goiter, thyroid cancer) |
| Predicted New Indication | Renal hypodysplasia/aplasia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 5 authorizations cancelled) |
| Number of NDAs | 5 (all ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, liothyronine is the active form of thyroid hormone (T3). Its efficacy in hypothyroidism is well established, since it replaces the missing hormone. Its mechanistic applicability to renal hypodysplasia/aplasia is not supported.

Renal hypodysplasia/aplasia is a developmental malformation in which the kidneys form incompletely or not at all. Hormone replacement cannot restore missing or malformed organs. The very high TxGNN score (99.95%) most likely reflects shared gene or phenotype associations in the knowledge graph rather than a true therapeutic relationship.

The other top-ranked predictions show the same pattern. Bilateral renal agenesis, Potter sequence, myxoma, and angiomyxoma are likely graph or name-similarity artifacts. Nodular goiter is biologically plausible but is already covered by existing labeled uses, so it is not true repurposing. Acrodysostosis has an indirect link through hormone resistance and associated hypothyroidism, and it is the only prediction with a modest body of literature (graded L4, "Research Question"). That literature is mostly generic thyroid hormone research, and none of it appears to study acrodysostosis directly.

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
| ANDA091382 | liothyronine sodium | Tablet | Sun Pharmaceutical Industries, Inc. | Cancelled |
| ANDA214803 | Liothyronine sodium | Tablet | A-S Medication Solutions | Cancelled |
| ANDA200295 | Liomny | Tablet | SIGMAPHARM LABORATORIES, LLC | Cancelled |
| ANDA211510 | Liothyronine Sodium | Tablet | Teva Pharmaceuticals USA, Inc. | Cancelled |
| ANDA090097 | Liothyronine Sodium | Tablet | Golden State Medical Supply, Inc. | Cancelled |

Approved indication text is not available for these authorizations. All five are cancelled, and there is no currently valid single-ingredient or combination authorization.

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
The prediction rests only on a knowledge-graph score. There are no clinical trials and no literature, and no credible biological mechanism for thyroid hormone replacement to correct a congenital kidney malformation. All US authorizations are also cancelled.

**To proceed, the following is needed:**
- A plausible mechanistic rationale, which requires the drug's mechanism of action data
- Preclinical or clinical evidence specific to renal hypodysplasia/aplasia
- Package insert warnings and contraindications to complete the safety review
- If a repurposing direction is pursued, a better-supported alternative such as acrodysostosis with hormone resistance, which would need direct studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

