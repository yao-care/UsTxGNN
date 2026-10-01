---
layout: default
title: Vitamin A
parent: Model Prediction Only (L5)
nav_order: 1295
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamin A: From Marketed Vitamin Products (No Indication Listed) to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vitamin A (DrugBank DB00162) is marketed in the US in injectable, oral and topical products, but the record lists no approved indication text.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but the prediction is not supported by any actual study: **5 retrieved clinical trials** were all graded unrelated, and **0 publications** were retrieved.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.97% (model rank 1182) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record. Vitamin A is a fat-soluble vitamin that acts mainly through retinoid signaling. It is marketed as a nutritional and topical product, and no approved indication text is listed.

The link to the predicted indication is weak. Prothrombin synthesis depends on vitamin K (gamma-carboxylation), and the congenital form is a genetic defect in the F2 gene. Vitamin A has no known role in this pathway.

The very high TxGNN score is most likely a knowledge-graph artifact from shared vitamin or nutrient neighbors. It should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Recruiting | 480 | Bone loss in haemophilia (factor VIII/IX deficiency). No vitamin A intervention. |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completed | 25 | Combination dietary supplement for endothelial function in hypertension. Unrelated disease. |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Phase 3 | Completed | 40 | Prothrombin complex concentrate (Beriplex) for acquired factor II/VII/IX/X deficiency. Not vitamin A, so the Phase 3 label does not transfer. |
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Phase 2 | Completed | 90 | Double-blind RCT of "Vitalliver" in decompensated cirrhosis. The agent cannot be confirmed as vitamin A and is not tied to prothrombin deficiency. Manual check needed. |
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Completed | 220 | Retrospective descriptive cohort of adult inborn errors of metabolism. No vitamin A intervention. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA006823 | AQUASOL A | Injection, solution | Casper Pharma LLC |
| M016 | SKINEEZ | Cloth | Cause for Change LLC |
| M016 | Skineez | Cloth | Cause for Change LLC |
| M016 | EvennessBrighteningBodyOil | Emulsion | Guangzhou Kadiya Biotechnology Co., Ltd. |
| Not specified | Tri-Vite Drops with Fluoride | Solution | Method Pharmaceuticals, LLC |

Other dosage forms in the 20 licenses include spray, cream, tablet, chewable tablet and liquid. Approved indication text is empty for all listed products.

---

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records.
- **Other signals in this evidence pack** (from other predicted indications, not from a package insert):
  - A systematic review and meta-analysis links higher vitamin A intake to increased fracture risk.
  - High-dose vitamin A is teratogenic, so maternal or periconceptional use needs strict dosing caution.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no mechanistic basis, since prothrombin depends on vitamin K, and no vitamin A study was found for this disease. It is a model prediction only (L5).

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any direct evidence linking vitamin A to prothrombin deficiency, which would first have to be shown to exist

**Note on other candidates in this pack:** "Perinatal disease" (rank 7) has the strongest support. It has a Phase 3 placebo-controlled RCT (NCT00211341, n=100,000, outcome not provided) and serial Cochrane reviews in very low birth weight infants, and it is rated L1 with "Proceed with Guardrails". Its evidence is strongest for the narrow VLBW/BPD use case rather than the broad label. If this drug is prioritized, evaluate that candidate rather than rank 1.

---
*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

