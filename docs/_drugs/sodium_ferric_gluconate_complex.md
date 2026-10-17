---
layout: default
title: Sodium Ferric Gluconate Complex
parent: Model Prediction Only (L5)
nav_order: 1169
evidence_level: L5
indication_count: 6
monitor_inn: "SODIUM FERRIC GLUCONATE COMPLEX"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "anaphylaxis", "bronchitis", "food-dependent exercise-induced anaphylaxis", "diabetic cataract"]
last_modified_at: 2026-10-14
description: "Sodium Ferric Gluconate Complex: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Iron deficiency anemia in chronic kidney disease"
---

# Sodium Ferric Gluconate Complex
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Sodium Ferric Gluconate Complex: From Iron Deficiency Anemia to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Sodium ferric gluconate complex is an intravenous iron replacement agent (Ferrlecit), used to treat iron deficiency, particularly in patients with chronic kidney disease.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this prediction.
It is a computational prediction only, and a plausible biological rationale is lacking.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia in chronic kidney disease (inferred from the drug class and the linked trials; the US licence records contain no indication text) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 2 (NDA020955 and ANDA078215, both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sodium ferric gluconate complex is an intravenous iron preparation that replenishes iron stores. Its role in iron deficiency anemia is established. Mechanistically, however, there is no known pathway linking it to diabetic retinopathy.

The prediction looks like a graph-based association rather than a pharmacological one. Iron is a pro-oxidant, and iron-catalyzed oxidative stress could plausibly worsen retinal vascular damage rather than improve it. A likely confounder is that many diabetic patients with chronic kidney disease receive IV iron to correct anemia, which could create a statistical link in the knowledge graph without any retinal effect.

Other predictions for this drug (diabetic retinopathy, diabetic cataract) share the same diabetic-complication neighbourhood, which further suggests a graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

Two trials were linked to the lower-ranked bronchitis prediction, but they concern iron deficiency in chronic kidney disease, not retinopathy, and are not evidence for this indication.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020955 (cancelled) | Ferrlecit (sanofi-aventis U.S. LLC) | Injection | Not recorded |
| ANDA078215 (cancelled) | Sodium Ferric Gluconate Complex in Sucrose (Hikma Pharmaceuticals USA Inc.) | Injection | Not recorded |

## Safety Considerations

- **Drug Interactions** (5 found; severity from the DDInter database):
  - **Major**: Dimercaprol
  - **Moderate**: Iron, ferrous fumarate, ferrous gluconate, chloramphenicol

Published reports in the data compiled for this report also describe anaphylactoid and anaphylactic reactions to the drug, including in pregnancy. The risk appears lower than with iron dextran, but hypersensitivity remains a recognised concern.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score, with no trials, no literature, no known mechanism, and a plausible biological argument against benefit. All licences are also cancelled in the US.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Preclinical evidence on whether iron or iron complexes affect retinal vascular pathology
- Assessment of whether the association is confounded by diabetic CKD anemia
- Route and formulation feasibility for an ocular indication (only the injectable form exists, and it is intravenous)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

