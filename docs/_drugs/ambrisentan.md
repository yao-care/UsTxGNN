---
layout: default
title: Ambrisentan
parent: Model Prediction Only (L5)
nav_order: 322
evidence_level: L5
indication_count: 5
monitor_inn: "AMBRISENTAN"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "malformation syndrome with odontal and/or periodontal component", "hypotrichosis simplex of the scalp", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature"]
last_modified_at: 2026-11-06
description: "Ambrisentan: predicted new indication pulmonary arteriovenous malformation (disease) (evidence level L5). In the US: 10 FDA applications (8 active)"
---

# Ambrisentan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ambrisentan: endothelin receptor type A antagonist → pulmonary arteriovenous malformation (pulmonary arteriovenous malformation (disease))
{: .text-alpha }

## One-Sentence Summary

Ambrisentan is an oral endothelin receptor type A antagonist that is marketed in the United States.
The TxGNN model predicts it may be effective for **pulmonary arteriovenous malformation (disease)**, but there are **no registered clinical trials** and only **1 publication** (a case report on a related condition), so the evidence is limited to a computational prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | pulmonary arteriovenous malformation (disease) |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 8 of 10) |
| Number of FDA Applications | 10 (active: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for ambrisentan: "Endothelin-1 (ET-1) is a potent autocrine and paracrine peptide. Two receptor subtypes, ET A and ET B, mediate the effects of ET-1 in the vascular smooth muscle and endothelium. […] Ambrisentan is a high-affinity (K i =0.011 nM) ET A receptor antagonist with a high selectivity for the ET A versus ET B receptor (>4000-fold)." ([DailyMed: Letairis (ambrisentan) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=725d4e73-6c83-477a-adc6-0ae4a133a844), label version 2026-06-22; accessed 2026-11-19.) Ambrisentan is known as an endothelin receptor type A antagonist. Endothelin drives blood vessel constriction and vascular remodeling, so blocking this pathway could plausibly matter in some pulmonary vascular conditions.

The only related publication describes pulmonary arterial hypertension (PAH) in a patient with hereditary hemorrhagic telangiectasia (HHT), a disease in which pulmonary arteriovenous malformations can occur. That report concerns PAH occurring in an HHT patient, not pulmonary arteriovenous malformation itself. The mechanistic link is therefore indirect, and the high TxGNN score should be read as a computational prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case report | World journal of clinical cases | A patient with hereditary hemorrhagic telangiectasia who also had pulmonary arterial hypertension; the report reviews the clinical course, treatment and family gene analysis to raise awareness of this combination. |

---

## US Market Information

At least 9 licence records are listed in the local data, and the list may be partial. All 9 are for single-ingredient oral film-coated tablets. No approved indication text is recorded in these licence records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022081 | Letairis | Tablet, film coated | Not recorded |
| ANDA208354 | Ambrisentan | Tablet, film coated | Not recorded |
| ANDA208441 | Ambrisentan | Tablet, film coated | Not recorded |
| ANDA210701 | Ambrisentan | Tablet, film coated | Not recorded |
| ANDA210058 | Ambrisentan | Tablet, film coated | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database. Examples with a Moderate level include canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, eliglustat and naltrexone. Examples with a Minor level include clarithromycin, miconazole and omeprazole.
- **Other considerations**: Ambrisentan is known to be teratogenic, which matters for any new use in women of reproductive age.

Please refer to the package insert for warnings and contraindications, as label text was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and one case report about a related condition (PAH in HHT). No study directly addresses pulmonary arteriovenous malformation, so the evidence level is L5.

**To proceed, the following is needed:**
- Studies that directly examine ambrisentan in pulmonary arteriovenous malformation, including HHT-associated disease
- Detailed mechanism of action data
- FDA package insert warnings and contraindications for a full safety review, including teratogenicity
- Clarification of the original approved indication from the licence records

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Letairis (ambrisentan) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=725d4e73-6c83-477a-adc6-0ae4a133a844) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

