---
layout: default
title: Belimumab
parent: Model Prediction Only (L5)
nav_order: 440
evidence_level: L5
indication_count: 6
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
last_modified_at: 2026-10-14
description: "Belimumab: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Systemic lupus erythematosus"
---

# Belimumab
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

## Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Belimumab is a monoclonal antibody that was originally used to treat systemic lupus erythematosus (including the pediatric form).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**,
but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on a computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic lupus erythematosus; pediatric systemic lupus erythematosus |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (both BLAs are cancelled) |
| Number of NDAs | 2 (BLA125370, BLA761043) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, belimumab is a monoclonal antibody that inhibits soluble BLyS (BAFF), which reduces B-cell survival and autoantibody production. This is why it is used in systemic lupus erythematosus, an autoantibody-driven disease.

Primary release disorder of platelets, however, is an intrinsic platelet function defect (inherited or acquired). It is not driven by B-cell activity. No plausible mechanistic link to BLyS inhibition was identified. The very high TxGNN score (99.96%) is a graph-based prediction only and is not backed by any clinical or literature evidence. The score should therefore be treated as a hypothesis, not as support for efficacy.

### Other Predicted Indications

The model also generated five further predictions. None has clinical trial or literature evidence, and all are Evidence Level L5 with a Hold recommendation.

| Rank | Predicted Indication | TxGNN Score | Mechanistic Assessment |
|------|------|------|------|
| 2 | Pseudo-von Willebrand disease | 99.96% | Caused by gain-of-function variants in platelet GPIbα, a genetic receptor defect. No rationale for BLyS inhibition. |
| 3 | Glanzmann thrombasthenia | 99.88% | Inherited integrin αIIbβ3 defect that belimumab does not correct. Only a speculative link to alloantibodies after platelet transfusion. |
| 4 | Fetal and neonatal alloimmune thrombocytopenia | 99.59% | Most mechanistically plausible: maternal alloantibodies destroy fetal platelets, so B-cell and BAFF-driven antibody production is relevant in principle. Use in pregnancy is limited by safety and placental transfer concerns, and current care relies on IVIG with or without corticosteroids. |
| 5 | Severe nonproliferative diabetic retinopathy | 99.05% | Driven by microvascular damage, VEGF signaling and inflammation, not B cells or BAFF. |
| 6 | Autosomal dominant macrothrombocytopenia | 99.04% | Inherited disorder of megakaryopoiesis and platelet formation, not immune-mediated. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125370 | BENLYSTA | Injection, powder, lyophilized, for solution | Not listed (status: cancelled) |
| BLA761043 | BENLYSTA | Solution | Not listed (status: cancelled) |

Both authorizations are held by GlaxoSmithKline LLC and are recorded as cancelled in the data compiled for this report.

## Safety Considerations

- **Drug Interactions**: 69 interactions were identified. Examples include:
  - **Major**: adalimumab, baricitinib, certolizumab pegol, and BCG live vaccine (Tice strain). These mostly reflect additive immunosuppression or infection risk.
  - **Moderate**: roflumilast, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, and several vaccines or live antigens (e.g., tetanus toxoid, anthrax vaccine, cholera vaccine).
  - **Minor**: zinc salts (acetate, gluconate, sulfate, chloride).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six predictions rest on model scores alone, with no clinical trials or literature, and the stated mechanistic links are weak or absent. The leading prediction (primary release disorder of platelets) has no plausible BLyS-related mechanism. Package-insert safety data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Preclinical or mechanistic evidence for any predicted indication. Fetal and neonatal alloimmune thrombocytopenia is the most plausible one to examine first, together with an assessment of pregnancy safety and placental transfer.
- Clarification of why both US BLAs are recorded as cancelled, since this affects feasibility of development
- Route compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

