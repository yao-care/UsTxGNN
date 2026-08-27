---
layout: default
title: Etelcalcetide
parent: 僅模型預測 (L5)
nav_order: 679
evidence_level: L5
indication_count: 4
---

# Etelcalcetide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Etelcalcetide: From Secondary Hyperparathyroidism to Hyperphosphatemia

## One-Sentence Summary

Etelcalcetide is an intravenous calcimimetic originally developed to treat secondary hyperparathyroidism (SHPT) in chronic kidney disease patients on hemodialysis. The TxGNN model predicts it may also be effective for **Hyperphosphatemia**, with **1 clinical trial** and **3 publications** currently supporting this direction, though the evidence base is still early-stage (L2).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Secondary hyperparathyroidism (SHPT) in CKD patients on hemodialysis *(not TFDA-labeled — drug not yet marketed in Taiwan; official indication text unavailable)* |
| Predicted New Indication | Hyperphosphatemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| Market Status (Taiwan) | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this evidence pack (data gap DG002). Based on known pharmacology, etelcalcetide is a calcium-sensing receptor (CaSR) agonist — a calcimimetic — administered intravenously at the end of hemodialysis sessions. It activates parathyroid CaSR to suppress parathyroid hormone (PTH) secretion, which in turn reduces PTH-driven calcium/phosphate release from bone and calcium/phosphate reabsorption in the gut and kidney.

Secondary hyperparathyroidism and hyperphosphatemia are both core components of chronic kidney disease–mineral and bone disorder (CKD-MBD) and are highly co-morbid in the hemodialysis population: elevated PTH drives phosphate release from bone, while reduced renal clearance further raises serum phosphate. Because etelcalcetide's PTH-suppressing mechanism sits upstream of this phosphate-release pathway, a secondary phosphate-lowering effect is mechanistically plausible even though hyperphosphatemia is not etelcalcetide's approved primary indication.

This is best understood as a mechanistically coherent but *indirect* ("adjacent indication") relationship rather than a validated new use. The strongest supporting trial, the DUET trial (PMID 33305109), was designed and powered to evaluate PTH control, not phosphate as a primary endpoint — so the hyperphosphatemia signal should be read as supportive, biomarker-level evidence rather than confirmatory proof of efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | N/A | Completed | 21 | Small mechanistic study evaluating the effect of active vitamin D and etelcalcetide on osteoclast activity in CKD-MBD patients — addresses bone/mineral pathway relevant to hyperphosphatemia rather than phosphate levels as a primary endpoint |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | RCT | Kidney International Reports | The DUET trial: prospective RCT of etelcalcetide in hemodialysis patients with secondary hyperparathyroidism, evaluating multilateral mechanisms including mineral/phosphate control |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | International Journal of Nephrology and Renovascular Disease | Reviews etelcalcetide's role in managing SHPT in hemodialysis, noting its effect on reducing PTH alongside phosphate-lowering strategies |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case Report | Clinical Nephrology | Case of metastatic pulmonary calcification in a dialysis patient with hyperparathyroidism, illustrating downstream consequences of uncontrolled mineral/phosphate metabolism |

## Safety Considerations

Please refer to the package insert for safety information. No TFDA warnings, contraindications, or drug interaction data are currently available for etelcalcetide (DG001, Blocking).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is one supportive RCT (DUET trial) and a coherent CaSR/PTH mechanistic pathway linking etelcalcetide's approved use to phosphate metabolism, but no trial has used phosphate reduction as a primary endpoint, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA package insert / label (warnings, contraindications) — currently a Blocking data gap
- Confirmed DrugBank mechanism-of-action documentation
- Taiwan market entry status for etelcalcetide
- Trial data with hyperphosphatemia (not PTH) as the primary endpoint

**Note on other candidates:** Three additional TxGNN-predicted indications for this drug (esophageal varices with/without bleeding, varicose disease) were also assessed but rated **L5 / Hold** — no clinical trials, no literature, and no plausible mechanistic link to CaSR/PTH biology. These are considered likely knowledge-graph statistical artifacts and are not recommended for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

