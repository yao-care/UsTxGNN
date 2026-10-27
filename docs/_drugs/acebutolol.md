---
layout: default
title: Acebutolol
parent: Model Prediction Only (L5)
nav_order: 64
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Acebutolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "ACEBUTOLOL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Acebutolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Acebutolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Acebutolol is an oral beta-blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. The evidence rests on model prediction alone.

(For the second-ranked prediction, malignant renovascular hypertension, there are 0 clinical trials and 1 older, indirect publication from 1975.)

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active marketing) |
| Number of NDAs | 2 (both cancelled ANDA generic approvals) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acebutolol is a cardioselective beta-1 blocker with intrinsic sympathomimetic activity. Its efficacy in hypertension is established, and it lowers blood pressure by reducing heart rate, cardiac output, and renin release. Mechanistically, this could plausibly apply to hypertension with kidney involvement.

The high TxGNN score (99.10%) mainly reflects how closely the new indication sits to the approved hypertension indication in the knowledge graph. It is not disease-specific evidence.

There are also practical limits. Malignant hypertension with renal injury is a hypertensive emergency, usually managed with intravenous agents (such as labetalol or nicardipine) and therapy targeting the renin-angiotensin system. An oral beta-blocker is unlikely to be first-line.

The second prediction, **malignant renovascular hypertension** (score 99.10%), has a stronger mechanistic rationale because this condition is strongly renin-dependent and beta-1 blockade reduces renin release. However, the only available evidence is indirect (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked prediction. For the second-ranked prediction (malignant renovascular hypertension), one record was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [768911](https://pubmed.ncbi.nlm.nih.gov/768911/) | 1975 | Clinical study (open-label) | La Nouvelle Presse Medicale | 50 hypertensive patients received acebutolol alone or with other antihypertensives for one year. Results were good or moderate in 74% and treatment failed in 26%. The drug was very well tolerated. The study covers arterial hypertension in general, so it is only indirect evidence for the renovascular subtype. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074007 | Acebutolol Hydrochloride (Golden State Medical Supply, Inc.) | Capsule | Not stated; status cancelled |
| ANDA075047 | Acebutolol Hydrochloride (AvKARE) | Capsule | Not stated; status cancelled |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for these.

- **Contraindication-related conditions (from a knowledge graph, not label text)**: The following conditions are linked to acebutolol as contraindications in the knowledge graph:
  - Cardiac and vascular: atrioventricular block, sick sinus syndrome, peripheral vascular disease (including intermittent claudication and peripheral arterial disease), pheochromocytoma and related adrenal or sympathetic tumours
  - Respiratory: asthma (intrinsic and allergic), pulmonary emphysema
  - Metabolic and organ disease: diabetes mellitus, diabetic ketoacidosis, kidney disease, liver disease, gallbladder disease
  - Neuromuscular: myasthenia gravis and neuromuscular junction disease
  - Other: psoriasis, anxiety and related mood disorders, and several cancer-related entries

  Kidney disease appearing on this list is particularly relevant to a renal indication and needs careful review.
- **Drug Interactions**: 100 interactions were identified in the database. Examples from the first 20 returned entries:
  - Moderate: acetohexamide, chlorpropamide, canagliflozin, dapagliflozin (antidiabetic agents); atropine, clidinium; betamethasone, budesonide; bupropion; cimetidine; and several calcium salts (acetate, carbonate, citrate, gluconate, lactate, phosphate)
  - Minor: aluminum hydroxide, acetylsalicylic acid, attapulgite

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no registered trials and no direct literature for malignant hypertensive renal disease. The only available record is a 1975 general hypertension study, and the product has no active US marketing status. Established parenteral therapies are also the standard for hypertensive emergencies.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening), especially regarding use in kidney disease
- Mechanism of action data from DrugBank
- Controlled clinical data in malignant or renovascular hypertension
- Comparison against current standard-of-care agents
- Assessment of the regulatory pathway given the cancelled-only market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

