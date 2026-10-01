---
layout: default
title: Etelcalcetide
parent: Moderate Evidence (L3-L4)
nav_order: 679
evidence_level: L4
indication_count: 4
---

# Etelcalcetide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Etelcalcetide: From Secondary Hyperparathyroidism to Hyperphosphatemia

## One-Sentence Summary

Etelcalcetide (US brand PARSABIV) is an intravenous calcimimetic used to treat secondary hyperparathyroidism (SHPT) in hemodialysis patients.
The TxGNN model predicts it may be relevant to **hyperphosphatemia**, but the support is thin: **1 registered clinical trial** (a mechanistic bone-biology study) and **3 publications**, none of which test phosphate lowering as the main endpoint.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Secondary hyperparathyroidism in hemodialysis patients (the US license records provide no indication text; this is taken from the literature and the pack's rationale) |
| Predicted New Indication | Hyperphosphatemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 license entries, all under a single NDA (NDA208325) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Etelcalcetide is a calcimimetic: it activates the calcium-sensing receptor on parathyroid cells and lowers parathyroid hormone (PTH). Its efficacy in SHPT is established, and the link to hyperphosphatemia is mechanistically plausible but has not been checked against the source record.

SHPT and hyperphosphatemia are closely linked parts of chronic kidney disease-mineral and bone disorder (CKD-MBD). Lower PTH reduces bone turnover, which can lower serum phosphate and calcium as a downstream effect. The high TxGNN score likely reflects this close CKD-MBD network association.

The link is indirect. Phosphate lowering here is a secondary pharmacodynamic effect of SHPT treatment, not a separate therapeutic use. In practice, phosphate is managed mainly with oral binders. This prediction is therefore better read as a research question about a secondary effect than as a new indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | N/A | Completed | 21 | Effect of active vitamin D and etelcalcetide on human osteoclasts in CKD patients. This is a mechanistic bone-biology study, not designed around a phosphate endpoint. Relevance grade: C. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | RCT | Kidney Int Rep | DUET trial: prospective randomized study of etelcalcetide for SHPT control in hemodialysis patients. It targets SHPT, not hyperphosphatemia. |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | Int J Nephrol Renovasc Dis | Reviews etelcalcetide in hemodialysis SHPT. Notes that phosphate is usually managed with oral binders and that etelcalcetide effectively lowers PTH with thrice-weekly dosing. |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case report | Clin Nephrol | Temporary metastatic pulmonary calcification in a peritoneal dialysis patient with hyperparathyroidism. Background on ectopic calcification in ESRD only. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208325 | PARSABIV (Amgen Inc) | Injection, solution | Not provided in the license record |

The record lists three identical entries for this NDA; they are shown once here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence is L4. The only trial is a mechanistic study, and the literature does not test phosphate lowering directly. Hyperphosphatemia is also a secondary effect of the approved SHPT use, not a distinct indication. The other predicted indications (esophageal varices with and without bleeding, varicose disease) are L5 model predictions with no plausible mechanism, and they are also on Hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Serum phosphate outcomes from existing etelcalcetide RCTs, such as the DUET data, to show whether the effect is clinically meaningful
- A decision on whether this is a distinct indication or only a secondary benefit of SHPT treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

