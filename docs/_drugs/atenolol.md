---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 422
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

The txgnn-pipeline skill is noted. The current task is report generation from an Evidence Pack — I'll now produce the evaluation report following the system prompt format.

---

# Atenolol: From Hypertension and Angina to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Atenolol is a cardioselective β1-adrenergic receptor blocker, widely recognized for the treatment of hypertension and angina pectoris, with beta-blockers as a class forming a cornerstone of post-myocardial infarction (post-MI) standard care.
The TxGNN model predicts it may be specifically effective for **Posteroinferior Myocardial Infarction**,
with **0 registered clinical trials** and **1 publication** (a 1985 crossover single-blind RCT) directly addressing this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, angina pectoris (no US license record found in dataset) |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L3 |
| US Market Status | No records found (0 NDAs retrieved; possible data gap) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, atenolol is a selective β1-adrenergic receptor blocker (beta-blocker). By competitively blocking β1-adrenergic receptors in cardiac tissue, atenolol reduces heart rate, myocardial contractility, and oxygen consumption — the three key drivers of ischemic injury. It also suppresses sympathetic nervous system activation, which is critically elevated in the acute MI setting and contributes to arrhythmia and extension of infarction.

Beta-blockers as a class are already embedded in international post-MI guidelines, and atenolol in particular has been one of the most studied agents in this setting. The TxGNN model's prediction focuses specifically on the **posteroinferior** MI subtype — an anatomical variant primarily involving the territory of the right coronary artery, affecting the inferior and posterior left ventricular walls. This subtype is clinically distinct: it frequently co-occurs with right ventricular infarction and carries a heightened risk of sinus bradycardia and AV block, making the application of a negative chronotropic agent like atenolol a high-stakes individualized decision.

The mechanistic rationale is therefore strong — atenolol's β1-selective blockade reduces myocardial oxygen demand and may suppress post-infarction arrhythmias. The key clinical caveat is that in posteroinferior MI with right ventricular involvement or conduction system compromise, beta-blockers must be used with extra caution, requiring pre-treatment assessment of right ventricular function, heart rate, and AV conduction status.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for atenolol in posteroinferior myocardial infarction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Crossover Single-blind RCT | La Revue de medecine interne | Compared atenolol 200 mg vs diltiazem 240 mg in 23 post-MI patients (posteroinferior or anterior) with residual ischemia at 4 weeks. Computerized bicycle ergometer stress testing used to quantify anti-ischemic efficacy, providing direct comparative evidence for atenolol in the posteroinferior MI recovery setting. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atenolol's β1-selective mechanism provides a well-grounded theoretical basis for use in posteroinferior MI — beta-blockers are guideline-recommended post-MI therapy — but the posteroinferior subtype carries specific hemodynamic risks (right ventricular infarction, bradycardia, AV block) that demand individualized clinical evaluation before initiating therapy.

**To proceed, the following is needed:**

- **Verify US FDA NDA/ANDA records** directly from the FDA Orange Book — the pipeline retrieved 0 records for atenolol, which is likely a data retrieval gap given atenolol's (Tenormin®) historical availability in the US market
- **Retrieve MOA data** from DrugBank (DB00335) to formally document the β1-selective mechanism for regulatory-level reporting
- **Retrieve package insert warnings and contraindications** from the FDA-approved label (priority: bradycardia, AV block, right ventricular failure — all clinically critical for this MI subtype)
- **Conduct a targeted systematic review** specifically examining beta-blocker use in the posteroinferior MI subtype, with attention to right ventricular involvement as an effect modifier
- **Establish pre-treatment assessment criteria**: right ventricular function, baseline heart rate, and AV conduction status should be mandatory gating conditions before atenolol initiation in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

