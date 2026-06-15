---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Amiodarone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Amiodarone: From Ventricular Arrhythmias to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is a multi-channel antiarrhythmic agent (Class III, with Class I/II/IV properties) with over 40 years of clinical use for life-threatening ventricular arrhythmias and atrial fibrillation.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, a rare inherited channelopathy causing exercise-triggered ventricular arrhythmias,
with **0 clinical trials** and **10 publications** currently supporting this direction — all consisting of case reports and observational studies rather than dedicated trials.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory records found in current data pipeline (amiodarone is globally established for ventricular tachycardia / ventricular fibrillation / atrial fibrillation) |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Market Status | No records found in current data pipeline |
| Number of NDAs | 0 (data pipeline did not retrieve records; likely a collection gap) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved in this evidence pack. Based on established pharmacological knowledge and the mechanistic annotations in the prediction rationale, amiodarone is a Vaughan Williams Class III antiarrhythmic that uniquely combines properties of all four classes: it blocks Na⁺, K⁺, and Ca²⁺ channels, and exerts non-competitive β-adrenergic receptor blocking activity. Together, these effects prolong the cardiac action potential duration and refractory period, suppress re-entrant circuits, and attenuate the adrenergic triggers that initiate ventricular arrhythmias.

CPVT is a rare inherited channelopathy caused by gain-of-function mutations in RYR2 (ryanodine receptor type 2) or loss-of-function mutations in CASQ2 (calsequestrin-2). Under catecholamine stimulation such as exercise or emotional stress, these mutations cause pathological calcium release from the sarcoplasmic reticulum, triggering delayed afterdepolarizations (DADs) that degenerate into bidirectional or polymorphic ventricular tachycardia. Amiodarone's β-adrenergic blocking component can partially suppress these catecholamine-driven triggers, which explains the mechanistic link the TxGNN model likely detected.

However, amiodarone does not directly stabilize RYR2 channels — the key mechanism that makes flecainide (current preferred add-on therapy per guidelines) effective in CPVT. The available literature consists exclusively of case reports in which amiodarone was used as a last-resort adjunct in patients refractory to beta-blockers and flecainide, not as a primary CPVT therapy. The TxGNN prediction reflects a plausible but incomplete mechanistic overlap, rather than evidence-based CPVT-specific efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Advances in pharmacologic treatment of ventricular arrhythmias; amiodarone discussed for acute termination and chronic VT prevention across multiple substrates |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Retrospective Cohort | Life (Basel) | Systematic review of CPVT patients from China; characterizes genetic basis (RYR2/CASQ2) and arrhythmic outcomes; notes differences from Western populations |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Retrospective Cohort | Rev Cardiovasc Med | CPVT clinical profile and healthcare utilization from a Chinese city cohort; contextualizes overall treatment landscape and resource burden |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case Series | Pacing Clin Electrophysiol | 14-year-old with CPVT (CASQ2 mutation) developed ICD-induced arrhythmic storm; flecainide added to background therapy (amiodarone) to suppress storming — highlights amiodarone's adjunctive role |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case Report | BMJ Case Rep | Child with out-of-hospital cardiac arrest received 40 defibrillation shocks; amiodarone used as part of multi-drug resuscitation protocol; CPVT ultimately identified as underlying cause |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case Report | Front Cardiovasc Med | CPVT in teenager resolved via bilateral cardiac sympathetic denervation after failure of drug therapy including amiodarone; illustrates amiodarone as a step before surgical escalation |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case Report | Anesth Analg | Neonate with Long QT and refractory polymorphic VT; multimodal therapy with lidocaine, esmolol, and amiodarone plus ventricular pacing; relevant to inherited arrhythmia management in neonates |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case Report | Turk Pediatri Arsivi | 2-year-old presented with sudden cardiac arrest later diagnosed as CPVT; treatment course documented including antiarrhythmic escalation |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | 6-year delayed CPVT diagnosis in a 9-year-old with RYR2 c.7580T>G mutation; highlights challenges in pediatric CPVT recognition and the role of antiarrhythmic therapy during diagnostic delay |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case Report | Rev Esp Cardiol | Arrhythmic storm triggered by ICD discharge in a CPVT patient; amiodarone documented as part of management to break the storm cycle |

---

## US Market Information

No regulatory license records were retrieved for amiodarone in the current data pipeline (0 records found). This likely reflects a data collection gap rather than a true absence of approval — amiodarone (brand names include Nexterone®, Pacerone®) has a well-established US FDA approval history for hemodynamically unstable ventricular tachycardia and ventricular fibrillation, first approved intravenously in 1995. Downstream pipeline steps (DrugBank API query, TFDA package insert retrieval) are required to resolve this gap.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** This evidence pack contains no retrieved safety data (warnings, contraindications, or drug-drug interaction records). Before any clinical use or trial design, the following sources should be consulted: TFDA or US FDA package insert (amiodarone carries Black Box Warnings for pulmonary toxicity, hepatotoxicity, and pro-arrhythmia), DrugBank interaction database, and prescribing information for the specific formulation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All available evidence for amiodarone in CPVT consists of case reports and secondary observational mentions (Evidence Level L4), with zero dedicated clinical trials. Amiodarone lacks the direct RYR2-stabilizing mechanism that defines first-line CPVT augmentation therapy (flecainide), and current arrhythmia guidelines position beta-blockers and flecainide as standard-of-care — amiodarone's role in CPVT is limited to refractory cases as a last-resort adjunct.

**To proceed, the following is needed:**
- Retrieve amiodarone MOA data from DrugBank API (DG002 remediation)
- Download and parse the TFDA/FDA package insert for complete warning and contraindication data (DG001 remediation — currently blocking safety evaluation)
- Confirm regulatory approval status: verify amiodarone's US FDA NDA records are properly ingested in the pipeline
- Conduct a focused literature search specifically for amiodarone + CPVT (current retrieval appears to rely on broad CPVT searches; amiodarone-specific CPVT studies may exist but were not retrieved)
- If evidence from the above steps is sufficient, consider designing a small prospective registry study in CPVT patients who have failed beta-blocker + flecainide therapy, using amiodarone as the escalation arm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

