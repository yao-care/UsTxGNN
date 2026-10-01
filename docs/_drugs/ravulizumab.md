---
layout: default
title: Ravulizumab
parent: Model Prediction Only (L5)
nav_order: 1112
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From Complement-Mediated Disease (PNH) to Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency

## One-Sentence Summary

Ravulizumab is a C5 complement inhibitor, marketed in the US as Ultomiris. The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**, but there are **0 clinical trials** and **0 publications** supporting this direction. The prediction is purely graph-based, and no mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complement-mediated disease (PNH is cited in the mechanism review; the approved indication text was not provided in the Evidence Pack) |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 records (all BLA761108) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Based on known information, ravulizumab is a terminal complement (C5) inhibitor. Its efficacy in complement-mediated hemolysis, as in PNH, is established, but that mechanism does not obviously extend to the predicted indication.

**The prediction is weak mechanistically.** G6PC3 deficiency causes neutrophil apoptosis and ER stress through accumulation of 1,5-anhydroglucitol-6-phosphate. This is not a complement-driven process, so blocking C5 has no clear rationale. The high TxGNN score reflects graph-based similarity only, with no supporting clinical or mechanistic data.

**The other top-10 predictions are similarly unsupported.** All have Evidence Level L5, with no clinical trials or literature:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Assessment |
|------|------|------|------|
| 2 | Cyclic hematopoiesis | 99.94% | No plausible link (ELANE-driven precursor maturation defect) |
| 3 | Primary hyperoxaluria | 99.90% | Speculative, indirect link only (secondary complement activation from oxalate crystals); the primary defect is hepatic oxalate overproduction |
| 4 | Severe congenital neutropenia | 99.87% | No link; C5 inhibition raises infection risk in neutropenic patients |
| 5 | Severe congenital neutropenia due to CXCR2 deficiency | 99.86% | Distant conceptual overlap via C5a/neutrophil recruitment; no supporting data |
| 6 | Primary immunodeficiency due to p14 deficiency | 99.83% | No rationale; complement inhibition would further compromise immune defense |
| 7 | Pseudo-von Willebrand disease | 99.82% | No plausible link (GP1BA gain-of-function) |
| 8 | X-linked severe congenital neutropenia | 99.82% | No link (WAS gain-of-function) |
| 9 | Primary release disorder of platelets | 99.81% | No plausible link (platelet granule secretion defect) |
| 10 | Megaloblastic anemia | 99.80% | Weak and indirect; cause is B12/folate deficiency, treated by replacement |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA761108 | Ultomiris | Solution, concentrate | Alexion Pharmaceuticals Inc. |

The Evidence Pack contains 3 identical records for this BLA. The approved indication text was empty in all of them.

---

## Safety Considerations

- **Infection risk**: Complement C5 inhibition increases susceptibility to infections with encapsulated bacteria. This is a particular concern in neutropenia and primary immunodeficiency, where the predicted indications already carry high infection risk.
- **Drug Interactions**: No interaction records were found.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone (Evidence Level L5). There are no trials or publications, and no plausible mechanistic link between C5 inhibition and the predicted diseases. For the neutropenia and immunodeficiency predictions, complement blockade may cause harm rather than benefit.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the original indication
- Any preclinical or clinical evidence linking complement C5 to the predicted disease pathophysiology
- A benefit-risk assessment of infection risk in neutropenic or immunodeficient populations

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

