---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 608
evidence_level: L5
indication_count: 6
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "obsolete susceptibility to ischemic stroke", "hypoalphalipoproteinemia"]
last_modified_at: 2026-10-14
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Atrial fibrillation"
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Digoxin: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside, originally used to treat atrial fibrillation and digitalis poisoning.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but there are currently **0 clinical trials** and only **1 indirect publication** (a review on antihypertensive chronopharmacology) supporting this direction. This is a model prediction without clinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation; digitalis poisoning |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 11 authorizations in total (2 NDAs, 9 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacological knowledge, digoxin inhibits Na+/K+-ATPase, which raises intracellular calcium, increases myocardial contractility and slows atrioventricular conduction. This underlies its use in atrial fibrillation rate control.

The link to Prinzmetal (vasospastic) angina is weak. This condition is driven by coronary artery vasospasm. Higher intracellular calcium in vascular smooth muscle could, in theory, worsen rather than relieve vasospasm. The only retrieved publication is a review of chronopharmacology in antihypertensive treatment, which does not address digoxin in vasospastic angina.

The high TxGNN score (0.998) most likely reflects proximity in the knowledge graph (shared cardiovascular context) rather than demonstrated biology. A potential safety concern cannot be excluded.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | Chronopharmacology and its impact on antihypertensive treatment. Indirect; does not address digoxin in vasospastic angina |

## US Market Information

All 11 authorizations are listed as cancelled; approved indication text was not available in the compiled data. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020405 | LANOXIN (Advanz Pharma) | Tablet | Not available |
| NDA009330 | LANOXIN (Covis Pharma) | Injection, solution | Not available |
| ANDA083391 | Digoxin (Hikma) | Injection | Not available |
| ANDA040481 | Digoxin (Sandoz) | Injection, solution | Not available |
| ANDA215209 | Digoxin (Amici Pharma) | Solution | Not available |

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text)**: Digoxin is linked to contraindication or caution signals in several conditions. Notable ones include:
  - Cardiac: myocardial infarction, Wolff-Parkinson-White syndrome, sick sinus syndrome, atrioventricular block, ventricular fibrillation, hypertrophic and restrictive cardiomyopathy, myocarditis, constrictive pericarditis, cor pulmonale
  - Metabolic and renal: kidney disease, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, hypothyroidism and myxedema
- **Drug Interactions**: 100 interactions were identified (DDInter). Examples at Moderate level include acarbose, rabeprazole, doxycycline, tetracycline, epinephrine, metformin, bupropion, amphotericin B, acetylsalicylic acid, cholecalciferol, calcium phosphate and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone). Minor interactions include atropine, hyoscyamine, glycopyrronium and albiglutide.

Please refer to the package insert for full warnings and contraindications, as label text was not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials and no relevant literature. The known pharmacology (raised intracellular calcium) may even be unfavorable in vasospastic angina. All US authorizations are cancelled, and label safety data is missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- Preclinical or mechanistic evidence on digoxin in coronary vasospasm, including safety assessment
- Systematic literature search specific to digoxin and vasospastic angina
- Clarification of current US marketing status, given that all authorizations are listed as cancelled

**Other predictions reviewed (all L5, Hold):** duodenal obstruction, duodenal ulcer, duodenogastric reflux, obsolete susceptibility to ischemic stroke and hypoalphalipoproteinemia. None has clinical trials or a plausible supporting mechanism, and the stroke entry is an obsolete ontology term that should be excluded.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

