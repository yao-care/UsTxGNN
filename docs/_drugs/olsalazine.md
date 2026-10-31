---
layout: default
title: Olsalazine
parent: Model Prediction Only (L5)
nav_order: 990
evidence_level: L5
indication_count: 10
monitor_inn: "OLSALAZINE"
predicted_indications: ["myelodysplastic syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "alopecia", "diffuse alopecia areata", "partial deletion of the long arm of chromosome 5", "unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts"]
last_modified_at: 2026-10-31
description: "Olsalazine: predicted new indication Myelodysplastic syndrome (evidence level L5). Approved use: Not stated in the available US label data"
---

# Olsalazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Olsalazine: From Ulcerative Colitis to Myelodysplastic Syndrome
{: .text-alpha }

## One-Sentence Summary

Olsalazine is a locally acting prodrug of 5-aminosalicylic acid (5-ASA, mesalamine), a drug class used for inflammatory bowel disease. The TxGNN model predicts it may be effective for **myelodysplastic syndrome (MDS)**, but **no clinical trials and no publications** currently support this direction. The prediction is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available US label data |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, olsalazine is a prodrug of 5-ASA that acts mainly locally in the colon, with minimal systemic exposure. Its original indication text is not recorded in the data compiled for this report.

No mechanistic link to MDS is established. A speculative anti-inflammatory or NF-kB-modulating rationale could be proposed, but olsalazine's low systemic absorption argues against meaningful effects on bone marrow. The high TxGNN score (0.9991) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top predictions are related or unrelated conditions, all with the same lack of supporting data:
- MDS-related terms: unclassified MDS, refractory cytopenia of childhood, partial deletion of the long arm of chromosome 5 (del(5q)), aregenerative anemia, and congenital sideroblastic anemia. These likely reflect similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence.
- Hair disorders: hypotrichosis simplex of the scalp, congenital hypotrichosis milia, alopecia and diffuse alopecia areata. Only alopecia areata has a theoretical immune-mediated rationale, and it is unsupported by data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019715 (cancelled) | Dipentum (Viatris Specialty LLC) | Capsule, gelatin coated (oral) | Not available |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database; the first 20 reviewed are mostly Moderate, and several are Major.
  - **Major**: human immunoglobulin G (intravenous), human botulinum neurotoxin A/B immune globulin, cidofovir, iothalamic acid.
  - **Moderate (examples)**: NSAIDs (ketorolac, ibuprofen, celecoxib, diclofenac), azathioprine, aminoglycosides and related nephrotoxic agents (amikacin, amphotericin B, bacitracin, capreomycin, colistimethate), acyclovir, cisplatin, clofarabine, ibandronate, chlorpropamide. Many of these involve potential additive kidney toxicity.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score. There are no trials or publications, no mechanistic data, and olsalazine's minimal systemic absorption makes bone marrow or hair follicle effects implausible.

**To proceed, the following is needed:**
- Mechanism of action data for olsalazine and a plausible biological link to MDS (or to alopecia areata)
- Preclinical evidence (for example, in vitro or animal studies in MDS or hair follicle models)
- Package insert warnings and contraindications from the FDA
- Pharmacokinetic evidence on whether systemic exposure could reach relevant tissues
- Renal safety and interaction review, given the many nephrotoxicity-related interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

