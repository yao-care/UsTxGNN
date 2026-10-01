---
layout: default
title: Benralizumab
parent: Model Prediction Only (L5)
nav_order: 445
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Benralizumab: From Its Approved Use to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Benralizumab is an anti-IL-5Rα antibody marketed in the US as FASENRA. The source record does not state its approved indication.
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, but **no clinical trials and no publications** support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source record |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all records are BLA761070) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Benralizumab is an anti-IL-5Rα antibody that depletes eosinophils and basophils. Detailed mechanism-of-action data are not available in the source record.

No clear pathway links this mechanism to antibody-mediated platelet destruction. Immune thrombocytopenia is driven by autoantibodies and clearance of platelets, not by the IL-5/eosinophil axis. The high score most likely reflects proximity in the knowledge graph rather than a proven biological link, so the prediction should be treated as a hypothesis only.

Other predictions for this drug offer context. For dermatitis (rank 2), a placebo-controlled Phase 2 trial in atopic dermatitis (HILLIER) found no clinical benefit, even though biopsy data show the drug depletes IL-5Rα-bearing cells in skin. This is a reminder that target engagement does not guarantee efficacy. The remaining top predictions (acne keloid, neonatal dermatomyositis, amyopathic dermatomyositis) also have no supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761070 | FASENRA (AstraZeneca Pharmaceuticals LP) | Injection, solution | Not stated in the source record |

The three license records in the source record share the same authorization number and product. Only the injectable route is available.

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or publications. There is no plausible mechanistic link between IL-5Rα blockade and immune-mediated platelet destruction. The nearest related prediction, atopic dermatitis, has already shown a negative randomized result despite target engagement.

**To proceed, the following is needed:**
- Mechanism-of-action data and a mechanistic rationale connecting eosinophil or basophil depletion to platelet destruction
- A targeted literature and trial-registry search for benralizumab in immune thrombocytopenia, including case reports
- The FDA package insert (approved indication, warnings, contraindications) to complete safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

