---
layout: default
title: Prucalopride
parent: Model Prediction Only (L5)
nav_order: 1097
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride: From Gastrointestinal Prokinetic Use to Hypoalphalipoproteinemia

## One-Sentence Summary

Prucalopride is an oral gut prokinetic that acts on the 5-HT4 receptor. The TxGNN model predicts it may be effective for **hypoalphalipoproteinemia** (low HDL cholesterol), but **no clinical trials and no publications** support this prediction. It is a graph-based model output only and has no known mechanistic basis.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (generic ANDA listings) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacological knowledge, prucalopride is a selective 5-HT4 receptor agonist that stimulates gut motility. This mechanism was assumed rather than taken from the source data.

No plausible link was identified between 5-HT4 agonism and HDL metabolism or lipoprotein regulation. The original indication is not recorded in the Evidence Pack, but a gut prokinetic has no clear relationship to a lipid disorder. The high TxGNN score (rank 5144) reflects patterns in the knowledge graph, not a demonstrated biological connection. Because no supporting data exist, the prediction should be treated as a hypothesis-generation signal only.

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
| ANDA218812 | PRUCALOPRIDE | Film-coated tablet | SKG Pharma Inc. |
| ANDA218847 | Prucalopride | Film-coated tablet | Lupin Pharmaceuticals, Inc. |
| ANDA218177 | PRUCALOPRIDE | Film-coated tablet | Novadoz Pharmaceuticals LLC |
| ANDA219078 | Prucalopride succinate | Tablet | Somerset Therapeutics, LLC |
| ANDA218812 | Prucalopride | Film-coated tablet | Amneal Pharmaceuticals NY LLC |

All listed products are oral tablets. The Evidence Pack contains no approved-indication text for these authorizations, and the number ANDA218812 appears twice under different manufacturers, so the source record may need verification.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it (L5). There are no trials or publications, and no plausible mechanistic link between 5-HT4 agonism and HDL regulation. Package insert safety data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data from DrugBank, and the original approved indication
- Any preclinical or clinical signal linking 5-HT4 agonism to lipoprotein metabolism

**Note on other predictions:** Among the other top-10 predictions, amyloidosis and primary amyloidosis are the only ones with retrieved literature (L4, "Research Question"). The plausible role there is symptomatic relief of gut dysmotility, not treatment of the amyloid disease. The retrieved articles do not report prucalopride efficacy or safety, so the evidence remains very weak.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

