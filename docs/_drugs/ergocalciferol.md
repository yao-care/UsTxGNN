---
layout: default
title: Ergocalciferol
parent: Model Prediction Only (L5)
nav_order: 667
evidence_level: L5
indication_count: 10
monitor_inn: "ERGOCALCIFEROL"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hypophosphatemia (disease)", "renal osteodystrophy", "hypophosphatemic rickets", "calcium-alkali syndrome", "vitamin D-dependent rickets"]
last_modified_at: 2026-10-14
description: "Ergocalciferol: predicted new indication Familial isolated hypoparathyroidism due to impaired PTH secretion (evidence level L5). Approved use: Vitamin D deficiency, rickets, osteomalacia, hypoparathy…"
---

# Ergocalciferol
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

# Ergocalciferol: From Vitamin D Deficiency and Bone Disorders to Renal Osteodystrophy

## One-Sentence Summary

Ergocalciferol (vitamin D2) was originally used for vitamin D deficiency and related bone and calcium-phosphate disorders such as rickets, osteomalacia, osteoporosis, and hypoparathyroidism.
The TxGNN model's top-ranked prediction is **familial isolated hypoparathyroidism due to impaired PTH secretion**, but it has no supporting trials or literature. The best-supported prediction in the data is **renal osteodystrophy**, with **1 clinical trial** (Phase 4, status unknown) and **20 publications**.
Overall, the evidence is limited and mostly indirect, so all predictions remain at the hypothesis stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin D deficiency, rickets, osteomalacia, hypoparathyroidism, osteoporosis (US label indication text is not available; these come from the knowledge graph) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion (rank 1); renal osteodystrophy is the best-supported candidate (rank 7) |
| TxGNN Prediction Score | 99.85% (rank 1); 99.67% (renal osteodystrophy) |
| Evidence Level | L5 (rank 1); L3 (renal osteodystrophy) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 (all cancelled; 4 ANDAs and 1 NDA) |
| Recommended Decision | Hold (rank 1); renal osteodystrophy is a Research Question, best treated as Proceed with Guardrails only if further work is pursued |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ergocalciferol is a nutritional vitamin D form (vitamin D2). It is converted in the liver and kidney to active 1,25-dihydroxyvitamin D, which regulates intestinal calcium and phosphate absorption and bone mineralization. Its efficacy in vitamin D deficiency, rickets, and osteomalacia is long established.

**Rank 1, familial isolated hypoparathyroidism:** Hypoparathyroidism is already among the original indications, and vitamin D can support calcium absorption. However, this is a specific genetic subtype (impaired PTH secretion), and no trials or literature were found for it. The high score is a model prediction only.

**Renal osteodystrophy (rank 7):** In chronic kidney disease, vitamin D deficiency contributes to secondary hyperparathyroidism and mineral bone disorder. Native vitamin D such as ergocalciferol is used to correct low 25-OH vitamin D and help control PTH. This is the most clinically plausible of the better-evidenced predictions, though no completed Phase 3 RCT was identified.

**Other predictions:**
- **Hypophosphatemic rickets** is already an original indication. Calcitriol and burosumab are now preferred in X-linked hypophosphatemia, so ergocalciferol's role is mostly historical or supportive.
- **Hypophosphatemia** and **vitamin D-dependent rickets** have indirect case-level or review evidence only. In type I, calcitriol is needed because ergocalciferol requires activation. In type II, response to standard doses is poor.
- **Renal tubular acidosis** has only two case-level or historical reports, and vitamin D does not correct the acid-base defect.
- **Calcium-alkali syndrome** is likely a spurious association with a possible safety concern, since ergocalciferol increases calcium absorption and could worsen hypercalcemia.
- **Acromesomelic dysplasia, craniofacial conodysplasia, and Dahlberg-Borer-Newcomer syndrome** have no plausible mechanistic link or no disease-specific evidence. The literature linked to Dahlberg-Borer-Newcomer syndrome covers general vitamin D topics and appears to be an indirect match.

---

## Clinical Trial Evidence

Only the renal osteodystrophy prediction has a registered trial. The other nine predictions have none.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01799317](https://clinicaltrials.gov/study/NCT01799317) | Phase 4 | Unknown | 60 | Tests whether ergocalciferol plus doxercalciferol, or doxercalciferol alone, corrects the bone mineralization defect in pediatric peritoneal dialysis patients with secondary hyperparathyroidism (2009-03 to 2014-06). No results provided. |

---

## Literature Evidence

Shown for renal osteodystrophy, the best-supported prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27401037](https://pubmed.ncbi.nlm.nih.gov/27401037/) | 2016 | Randomized controlled trial | Eur J Pharmacol | Ergocalciferol vs calcitriol in 204 patients with stage 3-5 CKD, compared for efficacy and safety in controlling CKD mineral bone disorder over about 33 months |
| [3877585](https://pubmed.ncbi.nlm.nih.gov/3877585/) | 1985 | Clinical study | Clin Nephrol | Childhood renal osteodystrophy treated with calcitriol (8) or ergocalciferol (7); aluminum-related osteomalacia worsened in some patients |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | Role of native vitamin D in pre-dialysis CKD remains unclear |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | Workshop report | Am J Kidney Dis | National Kidney Foundation workshop: vitamin D management in CKD stages 3-4 remains controversial |
| [28873969](https://pubmed.ncbi.nlm.nih.gov/28873969/) | 2017 | Clinical practice recommendations | Nephrol Dial Transplant | Recommendations for native vitamin D therapy in children with CKD stages 2-5 and on dialysis |
| [21947120](https://pubmed.ncbi.nlm.nih.gov/21947120/) | 2011 | Review | Nat Rev Nephrol | Mineral and bone disorders in children with CKD |
| [20671739](https://pubmed.ncbi.nlm.nih.gov/20671739/) | 2010 | Review | Kidney Int Suppl | Kidney bone disease and mortality in CKD, role of vitamin D |
| [16898852](https://pubmed.ncbi.nlm.nih.gov/16898852/) | 2006 | Review | Paediatr Drugs | Minimizing bone abnormalities in children with renal failure |

For hypophosphatemic rickets, a 1980 clinical study ([6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/), N Engl J Med) compared phosphate salts with ergocalciferol or calcitriol in 11 children with vitamin D-resistant rickets. Other predictions are supported mainly by reviews and case reports.

---

## US Market Information

All five US licenses are cancelled, and no approved-indication text is available for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090455 | Vitamin D (RemedyRepack) | Capsule | Not available |
| ANDA040833 | Ergocalciferol (Chartwell RX) | Capsule | Not available |
| ANDA080704 | Ergocalciferol (PD-Rx Pharmaceuticals) | Capsule, liquid filled | Not available |
| ANDA204276 | Ergocalciferol Capsules (Proficient Rx) | Capsule | Not available |
| NDA003444 | Ergocalciferol (Torrent Pharmaceuticals) | Capsule | Not available |

All products are oral formulations.

---

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for them.

- **Disease contraindications from the knowledge graph (not label text):** These include hypercalcemia, nephrocalcinosis, hyperparathyroidism, sarcoidosis, kidney disease, liver disease, gallbladder disease, hypertension, atrial fibrillation, diabetes and diabetic ketoacidosis, primary hyperoxaluria, iron-overload conditions (hemochromatosis, hemosiderosis), Wilson disease, hyperlipidemia, and prostate and breast cancers. These should be verified against the label.
- **Drug interactions:** 55 interactions were recorded; the first 20 are listed in the data compiled for this report.
  - **Major:** other vitamin D products and analogues, namely cholecalciferol, calcifediol, calcitriol, and doxercalciferol (additive hypercalcemia risk).
  - **Moderate:** thiazide-type diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone), barbiturates (amobarbital, butalbital), carbamazepine, rifabutin, bile acid sequestrants (cholestyramine, colesevelam, colestipol), sevelamer, magnesium oxide, digoxin, and topical calcipotriol or calcitriol.
  - **Minor:** cimetidine.
- **Repurposing-specific concern:** For calcium-alkali syndrome, ergocalciferol could worsen hypercalcemia.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (familial isolated hypoparathyroidism) is supported only by the model score, with no trials or literature. The majority of predictions are L4-L5.
- Renal osteodystrophy has the strongest support (L3), including one randomized ergocalciferol vs calcitriol study and a Phase 4 trial of unknown status. No completed Phase 3 RCT was identified, and effects on hard outcomes remain uncertain. It merits further research but not a Go decision.
- All US licenses are cancelled, and label safety data are missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking data gap)
- Mechanism of action data (for example, from DrugBank)
- For renal osteodystrophy: results or status update for NCT01799317, and a review of the 2016 randomized study for hard outcomes (fractures, PTH control, mortality)
- A hypercalcemia monitoring plan, including serum calcium and phosphate, especially in CKD patients and with co-administered vitamin D analogues
- Confirmation of the current US marketing status, since all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

