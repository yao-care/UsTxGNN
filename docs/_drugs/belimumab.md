---
layout: default
title: Belimumab
parent: Model Prediction Only (L5)
nav_order: 440
evidence_level: L5
indication_count: 6
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
last_modified_at: 2026-11-12
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
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, belimumab is a monoclonal antibody that inhibits soluble BLyS (BAFF), which reduces B-cell survival and autoantibody production. This is why it is used in systemic lupus erythematosus, an autoantibody-driven disease.

Primary release disorder of platelets, however, is an intrinsic platelet function defect (inherited or acquired). It is not driven by B-cell activity. No plausible mechanistic link to BLyS inhibition was identified. The very high TxGNN score (0.9996) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not backed by any clinical or literature evidence. The score should therefore be treated as a hypothesis, not as support for efficacy.

### Other Predicted Indications

The model also generated five further predictions. None has clinical trial or literature evidence, and all are Evidence Level L5 with a Hold recommendation.

| Rank | Predicted Indication | TxGNN Score | Mechanistic Assessment |
|------|------|------|------|
| 2 | Pseudo-von Willebrand disease | 0.9996 | Caused by gain-of-function variants in platelet GPIbα, a genetic receptor defect. No rationale for BLyS inhibition. |
| 3 | Glanzmann thrombasthenia | 0.9988 | Inherited integrin αIIbβ3 defect that belimumab does not correct. Only a speculative link to alloantibodies after platelet transfusion. |
| 4 | Fetal and neonatal alloimmune thrombocytopenia | 0.9959 | Most mechanistically plausible: maternal alloantibodies destroy fetal platelets, so B-cell and BAFF-driven antibody production is relevant in principle. Use in pregnancy is limited by safety and placental transfer concerns, and current care relies on IVIG with or without corticosteroids. |
| 5 | Severe nonproliferative diabetic retinopathy | 0.9905 | Driven by microvascular damage, VEGF signaling and inflammation, not B cells or BAFF. |
| 6 | Autosomal dominant macrothrombocytopenia | 0.9904 | Inherited disorder of megakaryopoiesis and platelet formation, not immune-mediated. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261106-belimumab-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Both authorizations are held by GlaxoSmithKline LLC and are recorded as cancelled in the data compiled for this report." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 2 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-belimumab-1 -->

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125370 | BENLYSTA | Injection, powder, lyophilized, for solution | Not listed (status: valid) |
| BLA761043 | BENLYSTA | Solution | Not listed (status: valid) |

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
- Route compatibility and similarity-to-original-indication assessments, which are still pending

<!-- review:begin us-lic-20261106-belimumab-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of why both US BLAs are recorded as cancelled, since this affects feasibility of development / Route compatibility and similarity-to-original-indication assessments, which are still pending" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 2 FDA applications or NDC listings for this drug, 2 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-belimumab-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Both authorizations are held by GlaxoSmithKline LLC and are recorded as cancelled in the data compiled for this report" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "Clarification of why both US BLAs are recorded as cancelled, since this affects feasibility of development" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

