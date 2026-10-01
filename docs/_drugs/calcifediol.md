---
layout: default
title: Calcifediol
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 4
---

# Calcifediol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Calcifediol: From Its Labeled Use to Vitamin D Deficiency (Obsolete Term)

## One-Sentence Summary

Calcifediol (25-hydroxyvitamin D3) is a vitamin D metabolite marketed in the US as the extended-release capsule Rayaldee, but its original indication is not recorded in the supplied data.
The TxGNN model predicts it may be effective for **vitamin D deficiency** (listed under an obsolete disease term).
**No clinical trials and no publications** currently support this specific prediction, so it rests on model output and biological plausibility alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (NDA208010, appearing as 2 duplicate license records) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied data. Calcifediol is 25-hydroxyvitamin D3, the main circulating form of vitamin D. Raising its level is a biologically plausible way to correct vitamin D deficiency. The very high TxGNN score most likely reflects this direct relationship between the compound and the vitamin D pathway.

Several caveats limit how far this prediction can be trusted:
- The disease term is flagged as **obsolete**, so the prediction should be re-mapped to the current vitamin D deficiency term in the ontology.
- The drug's original indications are not recorded, so the similarity between the original and new indication cannot be assessed.
- There are no trials or literature for this prediction in the supplied data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA208010 | Rayaldee | Capsule, extended release (oral) | OPKO Pharmaceuticals LLC |

The data lists NDA208010 twice as identical records; it is shown once here. No approved indication text was supplied.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, but it has no supporting trials or literature. It also uses an obsolete disease term, and the drug's original indications, mechanism and safety data are all missing, so it is not ready for further assessment.

**To proceed, the following is needed:**
- Re-map the prediction to the current vitamin D deficiency ontology term and verify it against the labeled indication.
- Obtain the package insert (warnings, contraindications, approved indication). This is a blocking gap.
- Obtain mechanism of action data, for example from DrugBank.
- Search for trials and literature on calcifediol in vitamin D deficiency.
- Among the other predictions for this drug, vitamin D-dependent rickets has the most defensible mechanism (calcifediol bypasses the block in type 1B, CYP2R1 25-hydroxylase deficiency). Its evidence is still only L4, so it remains a research question rather than a recommendation.

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

