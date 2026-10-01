---
layout: default
title: Eculizumab
parent: Model Prediction Only (L5)
nav_order: 640
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Complement-Mediated Diseases (PNH, aHUS) to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab is a C5 complement inhibitor, used for complement-mediated diseases such as paroxysmal nocturnal hemoglobinuria (PNH), atypical hemolytic uremic syndrome (aHUS) and myasthenia gravis.
The TxGNN model predicts it may be effective for **cyclic hematopoiesis** (cyclic neutropenia), but there are **0 clinical trials** and **0 publications** for this indication, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | PNH, aHUS and myasthenia gravis (inferred from the drug's literature, because the approved-indication text in the US license records is blank) |
| Predicted New Indication | Cyclic hematopoiesis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all BLAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record. Eculizumab is known to be a monoclonal antibody that inhibits complement component C5, blocking terminal complement activation. This is the basis of its use in PNH, aHUS and other complement-driven diseases.

The mechanistic link to the predicted indication is weak. Cyclic neutropenia is driven by ELANE mutations affecting neutrophil production and is not complement-mediated. The same problem applies to the other nine predictions, which are mostly neutropenia subtypes (JAGN1, WAS, CXCR2 and CSF3R defects, and idiopathic or severe congenital neutropenia). None has a known complement component. The cluster suggests the model is propagating from a disease-class neighborhood in the knowledge graph rather than from a drug-specific mechanism. The high score should therefore be read as a hypothesis-generation signal, not as support for efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

Some lower-ranked predictions (for example, congenital neutropenia-myelofibrosis-nephromegaly syndrome) returned literature hits. All of these papers concern eculizumab's established uses (PNH, aHUS/TMA, myasthenia gravis, CD59 deficiency). They do not address neutropenia, so they are drug-keyword matches and not disease evidence.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125166 | SOLIRIS | Injection, solution, concentrate | Alexion Pharmaceuticals Inc. |
| BLA761333 | BKEMV | Injection, solution, concentrate | Amgen Inc |
| BLA761340 | EPYSQLI | Injection, solution | Teva Pharmaceuticals USA, Inc. |

All three products are injectables. The source data does not include approved-indication text.

---

## Safety Considerations

- **Infection risk**: Terminal complement blockade raises the risk of serious meningococcal infection. This is a particular concern in neutropenic or immunodeficient patients, which is the population targeted by all ten predicted indications.
- **Drug interactions**: No interactions were found in the DDI query.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no trials or disease-specific publications, and there is no plausible complement-mediated mechanism in cyclic neutropenia. Adding C5 blockade to neutropenic patients would also add serious infection risk.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Preclinical or genetic evidence that complement activation contributes to cyclic neutropenia
- A benefit-risk assessment of meningococcal infection in neutropenic patients

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

