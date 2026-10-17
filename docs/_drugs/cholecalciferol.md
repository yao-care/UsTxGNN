---
layout: default
title: Cholecalciferol
parent: Model Prediction Only (L5)
nav_order: 526
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Cholecalciferol: predicted new indication Renal osteodystrophy (evidence level L5). Approved use: Osteoporosis, vitamin D deficiency, rickets, osteomalacia…"
monitor_inn: "CHOLECALCIFEROL"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "renal tubular acidosis"]
---

# Cholecalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cholecalciferol: From Osteoporosis and Vitamin D Deficiency to Renal Osteodystrophy

## One-Sentence Summary

Cholecalciferol (vitamin D3) is a vitamin D supplement originally used for conditions such as osteoporosis, vitamin D deficiency, rickets, osteomalacia and hypoparathyroidism.
The TxGNN model's top-ranked prediction is **familial isolated hypoparathyroidism due to impaired PTH secretion**, but that prediction has no supporting studies. The best-supported prediction in the data compiled for this report is **renal osteodystrophy**, with **2 clinical trials** and **20 publications**.
This report therefore covers the top-ranked prediction briefly and focuses on renal osteodystrophy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis, vitamin D deficiency, rickets, osteomalacia, hypoparathyroidism (from the knowledge graph; no approved indication text is available for the US licenses) |
| Predicted New Indication | Renal osteodystrophy (the rank 1 prediction, familial isolated hypoparathyroidism due to impaired PTH secretion, is on Hold with no evidence) |
| TxGNN Prediction Score | 99.11% (renal osteodystrophy); 99.79% (rank 1 prediction) |
| Evidence Level | L2 (renal osteodystrophy); L5 (rank 1 prediction) |
| US Market Status | Cancelled only |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Proceed with Guardrails (renal osteodystrophy); Hold (rank 1 prediction) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, cholecalciferol is a pro-hormone. It is converted in the liver to 25-hydroxyvitamin D and then in the kidney to the active form, calcitriol. Calcitriol regulates calcium and phosphate absorption and parathyroid hormone (PTH) production.

In chronic kidney disease–mineral and bone disorder (CKD-MBD), 25-hydroxyvitamin D deficiency is common and contributes to secondary hyperparathyroidism. Renal osteodystrophy is the bone component of this disorder. Replenishing native vitamin D with cholecalciferol can raise 25(OH)D and lower PTH in some patients, which fits cholecalciferol's known role in calcium and bone homeostasis.

The other predictions are weaker:
- **Familial isolated hypoparathyroidism (rank 1):** Cholecalciferol is already associated with hypoparathyroidism in general, so the biology is plausible. However, no trial or publication addresses this subtype. The high score likely reflects its closeness to the known indication in the knowledge graph.
- **Acromesomelic dysplasia, craniofacial conodysplasia, Dahlberg-Borer-Newcomer syndrome (ranks 2–4):** No mechanistic link was identified. The retrieved publications for rank 4 are general vitamin D papers unrelated to the syndrome.
- **Hypophosphatemic rickets and renal tubular acidosis (ranks 5 and 7):** Vitamin D can only play a supportive role. Standard care relies on phosphate plus active vitamin D analogs or burosumab (hypophosphatemic rickets), or on alkali therapy (renal tubular acidosis).

---

## Clinical Trial Evidence

Trials for renal osteodystrophy:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Phase 3 | Unknown | 200 | VITA-D: placebo-controlled trial of cholecalciferol in vitamin D-deficient kidney transplant recipients, assessing graft function, rejection, infections and CRP in the first year. The population is adjacent to, not the same as, renal osteodystrophy. |
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | Not applicable | Completed | 55 | Cholecalciferol versus doxercalciferol for secondary hyperparathyroidism in CKD stages 3–4, a core component of renal osteodystrophy. Small sample. |

No clinical trials are registered for the other predicted indications.

---

## Literature Evidence

Publications for renal osteodystrophy (selected):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34747516](https://pubmed.ncbi.nlm.nih.gov/34747516/) | 2022 | RCT (secondary analysis) | J Bone Miner Res | Cholecalciferol supplementation attenuated bone loss in 193 incident kidney transplant recipients |
| [35200136](https://pubmed.ncbi.nlm.nih.gov/35200136/) | 2022 | Prospective controlled study | Clin Nephrol | Effect of vitamin D sterols on bone histology in pre-dialysis CKD |
| [38397979](https://pubmed.ncbi.nlm.nih.gov/38397979/) | 2024 | Observational study | Biomedicines | Efficacy and safety of high-dose cholecalciferol in hemodialysis patients with 25(OH)D deficiency |
| [39597015](https://pubmed.ncbi.nlm.nih.gov/39597015/) | 2024 | Observational study | Medicina (Kaunas) | Hemodialysis patients may benefit from cholecalciferol targeting a high 25(OH)D level |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | Role of native vitamin D in pre-dialysis CKD remains unclear |
| [33922902](https://pubmed.ncbi.nlm.nih.gov/33922902/) | 2021 | Review | Nutrients | Vitamin D effects on bone and the cardiovascular system in CKD and transplant recipients |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | Workshop report | Am J Kidney Dis | National Kidney Foundation report on vitamin D in CKD stages 3–4; management remains controversial |
| [20671739](https://pubmed.ncbi.nlm.nih.gov/20671739/) | 2010 | Review | Kidney Int Suppl | Kidney bone disease and mortality in CKD: vitamin D, calcimimetics, alkaline phosphatase and minerals |
| [21947120](https://pubmed.ncbi.nlm.nih.gov/21947120/) | 2011 | Review | Nat Rev Nephrol | Mineral and bone disorders in children with CKD |
| [6264838](https://pubmed.ncbi.nlm.nih.gov/6264838/) | 1981 | Review | Ann Clin Lab Sci | Secondary hyperparathyroidism in chronic renal failure |

Evidence for the other predictions is limited to reviews and case reports. For hypophosphatemic rickets, one case report describes premature cranial synostosis possibly linked to intoxication with 1-alpha-hydroxylated vitamin D. For renal tubular acidosis, one case report describes vitamin D3 overdose in a child with distal RTA after a hasty rickets diagnosis.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021762 | FOSAMAX PLUS D (Organon LLC) | Tablet | Not available (cancelled) |
| Not available | GROWTH SUPPORTPATCH, HAUTUKI (CUSTICS) | Patch | Not available (cancelled) |

---

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text):** Cholecalciferol is linked to contraindications or cautions in conditions including hypercalcemia, nephrocalcinosis, hyperparathyroidism, sarcoidosis, kidney disease, liver disease, hypertension, diabetes mellitus, atrial fibrillation, primary hyperoxaluria and Wilson disease. These are graph-derived and should be confirmed against the package insert.
- **Drug Interactions:** 56 interactions are recorded. The main ones are:
  - **Major:** calcifediol, calcitriol, dihydrotachysterol, doxercalciferol (additive vitamin D effects, risk of hypercalcemia).
  - **Moderate:** thiazide diuretics (bendroflumethiazide, benzthiazide, chlorothiazide, chlorthalidone), barbiturates (amobarbital, butabarbital, butalbital), carbamazepine, bile acid sequestrants (cholestyramine, colesevelam, colestipol), digoxin and digitoxin, and topical calcipotriol and calcitriol.
  - **Minor:** cimetidine.
- **Indication-specific safety signals:** Vitamin D overdose or intoxication has been reported in children with renal tubular acidosis and X-linked hypophosphatemic rickets.

Please refer to the package insert for label warnings and contraindications. These were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (renal osteodystrophy); Hold (familial isolated hypoparathyroidism and the other predictions)**

**Rationale:**
- Renal osteodystrophy has a coherent mechanism and supporting trials: a Phase 3 RCT in transplant recipients and a completed comparison with doxercalciferol in CKD secondary hyperparathyroidism. The Phase 3 trial's indirect population and unknown status cap the evidence at L2 rather than L1.
- The rank 1 prediction and ranks 2–4 have no disease-specific evidence and rest on the model score alone, so they stay on Hold. Hypophosphatemic rickets and renal tubular acidosis (L4) are research questions only, with vitamin D in a supportive role.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently missing and a blocking gap for safety screening).
- Mechanism of action data for cholecalciferol.
- Disease-specific trials in renal osteodystrophy or CKD-MBD with bone outcomes (histology, fracture, bone density) rather than surrogate markers alone.
- A monitoring plan for calcium, phosphate and PTH to avoid hypercalcemia and vascular calcification, with dosing individualized by CKD stage.
- A review of interactions with active vitamin D analogs, thiazides and digoxin, which are common in CKD patients.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

