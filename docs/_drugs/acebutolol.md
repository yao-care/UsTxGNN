---
layout: default
title: Acebutolol
parent: Model Prediction Only (L5)
nav_order: 64
evidence_level: L5
indication_count: 1
monitor_inn: "ACEBUTOLOL"
predicted_indications: ["malignant hypertensive renal disease"]
last_modified_at: 2026-11-20
description: "Acebutolol: predicted new indication malignant hypertensive renal disease (evidence level L5). In the US: 4 FDA applications (2 active)"
---

# Acebutolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Acebutolol: cardioselective beta-1 blocker → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Acebutolol is a cardioselective beta-1 blocker with intrinsic sympathomimetic activity, used as an oral antihypertensive drug. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials and no publications** were found to support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9910 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 4) |
| Number of FDA Applications | 4 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the FDA-approved prescribing information for acebutolol: "Acebutolol is a cardioselective, β-adrenoreceptor blocking agent, which possesses mild intrinsic sympathomimetic activity (ISA) in its therapeutically effective dose range." ([DailyMed: acebutolol hydrochloride prescribing information, AvKARE](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fa40a564-a579-15c1-e053-6294a90ad8e9), label version 2026-01-13; accessed 2026-11-19.) Based on its known drug class, acebutolol blocks beta-1 adrenergic receptors in the heart. This lowers heart rate and cardiac output and reduces renin release, all of which can lower blood pressure.

Malignant hypertension with kidney involvement is a state of severely raised blood pressure with kidney injury. In principle, a blood-pressure-lowering drug that also reduces renin release could be relevant. The high TxGNN score (0.9910) reflects the model's pattern of association with hypertension-related conditions. It is not evidence specific to this disease.

There are important practical limits. Malignant hypertension with kidney injury is a hypertensive emergency, usually managed with intravenous agents and with therapy that targets the renin-angiotensin system. An oral beta-blocker is unlikely to be a first-line choice. No disease-specific data supports its use here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074007 | Acebutolol Hydrochloride | Capsule | Not recorded |
| ANDA075047 | Acebutolol Hydrochloride | Capsule | Not recorded |

## Safety Considerations

- **Drug Interactions**: The interaction search returned 100 records. Examples include:
  - Moderate: acetohexamide, atropine, betamethasone, budesonide, bupropion, canagliflozin, chlorpropamide, cimetidine, clidinium, dapagliflozin, and several calcium salts (acetate, carbonate, citrate, gluconate, lactate, phosphate).
  - Minor: aluminum hydroxide, acetylsalicylic acid, attapulgite.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (evidence level L5). The clinical setting, a hypertensive emergency, is usually treated with other drug classes and routes of administration.

**To proceed, the following is needed:**
- Obtain and review the package insert for warnings and contraindications
- Obtain detailed mechanism of action data
- Run a systematic literature search on beta-blockers in malignant hypertension with kidney involvement
- Compare acebutolol against current standard treatments for this condition, including route of administration
- Confirm the current regulatory status of the marketed products

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: acebutolol hydrochloride prescribing information, AvKARE](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fa40a564-a579-15c1-e053-6294a90ad8e9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

