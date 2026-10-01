---
layout: default
title: Amiodarone
parent: Model Prediction Only (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Amiodarone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Amiodarone: From Ventricular Arrhythmias to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is a class III antiarrhythmic drug used for ventricular arrhythmias. The license records in the Evidence Pack do not state the approved indication, so this is based on the drug's general use.
The TxGNN model predicts it may be effective for **catecholaminergic polymorphic ventricular tachycardia (CPVT)**. There are **0 clinical trials** and **10 publications** on this indication, and none of the publications tests amiodarone for CPVT.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular arrhythmias (general drug knowledge; not stated in the license records) |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 (no trials; literature is not amiodarone-specific) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Amiodarone is generally described as a class III antiarrhythmic. It blocks potassium channels and prolongs repolarization, with additional sodium-channel, calcium-channel and beta-adrenergic effects.

CPVT is a rare inherited channelopathy. It is driven by RYR2 or CASQ2-related diastolic calcium leak, which causes adrenergic-triggered delayed afterdepolarizations. The predicted indication is a ventricular arrhythmia, so it is superficially close to amiodarone's original use.

Amiodarone's main mechanism does not target this calcium-handling defect. The retrieved literature centers on beta-blockers, flecainide, sympathetic denervation and ICD management, and amiodarone appears only incidentally (for example, in arrhythmic storm). The high TxGNN score is therefore not backed by mechanistic or clinical support.

Among the other predictions for this drug, plain **ventricular tachycardia** (rank 3) has far stronger evidence. It has Phase 3 trials and RCTs, and it is probably an already-established use rather than true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | General review of antiarrhythmic drugs for ventricular arrhythmias; not CPVT-specific |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical features, genetics and arrhythmic outcomes of CPVT patients from China |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Rev Cardiovasc Med | Clinical characteristics, genetics, healthcare use and costs in CPVT patients in a Chinese city |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in a boy with CASQ2-related CPVT |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Front Cardiovasc Med | CPVT in a teenager resolved after right cardiac sympathetic denervation following left denervation |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Arsivi | A 2-year-old with CPVT presenting with sudden cardiac arrest |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Six-year delayed diagnosis of CPVT (RYR2 c.7580T>G) in a 9-year-old |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case report | BMJ Case Rep | Young child survived out-of-hospital cardiac arrest with recurrent VT/VF despite 40 shocks |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case report | Rev Esp Cardiol | Arrhythmic storm induced by ICD discharge in a CPVT patient |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case report | Anesth Analg | Neonate with long QT syndrome and refractory VT treated with lidocaine, esmolol and amiodarone (not CPVT) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA204742 | Amiodarone Hydrochloride (RemedyRepack) | Tablet | Not stated in record |
| ANDA076217 | Amiodarone Hydrochloride (HF Acquisition / HealthFirst) | Injection, solution | Not stated in record |
| ANDA076217 | Amiodarone Hydrochloride (Medical Purchasing Solutions) | Injection, solution | Not stated in record |
| ANDA204742 | Amiodarone Hydrochloride (NCS HealthCare of KY / Vangard Labs) | Tablet | Not stated in record |
| ANDA204550 | Amiodarone Hydrochloride (AuroMedics Pharma) | Injection, solution | Not stated in record |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found. The Evidence Pack's notes flag pulmonary, thyroid, hepatic and QT toxicity, plus interaction monitoring, as key themes for any use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.78%), but there are no registered trials and no literature testing amiodarone in CPVT. Amiodarone's potassium-channel mechanism does not address the RYR2/CASQ2 calcium-leak defect. The literature points to beta-blockers, flecainide and sympathetic denervation as the relevant therapies.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text (currently missing, blocking safety screening)
- Mechanism of action data from DrugBank
- Evidence that amiodarone has any clinical or preclinical effect in CPVT models or patients
- Consider prioritizing the **ventricular tachycardia** prediction (rank 3) instead, after confirming against the label whether it counts as repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

