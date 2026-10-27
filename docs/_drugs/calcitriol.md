---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 487
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Calcitriol: predicted new indication Hereditary hypophosphatemic rickets (evidence level L5). Approved use: Hypercalcemia disease, nephrocalcinosis…"
monitor_inn: "CALCITRIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hereditary hypophosphatemic rickets"]
---

# Calcitriol
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

## Calcitriol: From Hypercalcemia and Mineral Metabolism Disorders to Hereditary Hypophosphatemic Rickets
{: .text-alpha }

## One-Sentence Summary

Calcitriol is the active form of vitamin D, originally used for mineral metabolism disorders such as hypoparathyroidism, hypophosphatemia, renal osteodystrophy and related calcium/phosphorus conditions.
The TxGNN model predicts it may be effective for **Hereditary Hypophosphatemic Rickets**, the best-supported of the top predictions, with **2 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercalcemia disease, nephrocalcinosis, phosphorus metabolism disease, hypophosphatemia, hypoparathyroidism, renal osteodystrophy (from the knowledge graph; no approved indication text is available in the US licence records) |
| Predicted New Indication | Hereditary hypophosphatemic rickets (the best-supported candidate among the top 7 predictions; the top-ranked prediction by score is "obsolete vitamin D deficiency") |
| TxGNN Prediction Score | 99.28% (hereditary hypophosphatemic rickets); 99.96% for the top-ranked "obsolete vitamin D deficiency" |
| Evidence Level | L2 (conservative placement) |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 10 (all cancelled; 2 NDAs and 8 ANDAs) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, calcitriol is the active hormonal form of vitamin D. It bypasses the renal 1-alpha-hydroxylation step and promotes intestinal absorption of calcium and phosphate.

In X-linked hypophosphatemia (XLH) and related FGF23-excess disorders, excess FGF23 suppresses renal 1-alpha-hydroxylase and phosphate reabsorption, which lowers endogenous calcitriol and wastes phosphate. Calcitriol, usually with phosphate supplements, replaces the deficient active vitamin D and improves intestinal phosphate absorption. It is a long-standing conventional therapy. This is closely related to calcitriol's original indications in hypophosphatemia and phosphorus metabolism disorders, so the prediction is a natural extension of its existing use. Burosumab is now an alternative for many patients.

Other predictions were weaker:
- **Obsolete vitamin D deficiency** (score 99.96%): biologically plausible, but the disease term is obsolete and no trials or literature were found (L5, Hold).
- **Renal tubular acidosis** (99.93%): only indirect physiology studies, case reports and one review (L4, Hold).
- **Familial isolated hypoparathyroidism** (99.81%): an extension of an existing indication, with no subtype-specific evidence (L5, Hold).
- **Acromesomelic dysplasia Campailla-Martinelli type, craniofacial conodysplasia, and Dahlberg-Borer-Newcomer syndrome**: no clear mechanistic link, prediction only (L5, Hold).

---

## Clinical Trial Evidence

Trials for hereditary hypophosphatemic rickets:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Completed | 16 | Calcitriol alone (no phosphate) for one year in children and adults with XLH, assessing mineral ions, growth, skeletal mineralization and kidney calcification |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | High vs low dose active vitamin D with neutral phosphate in children with XLH |

No clinical trials were registered for the other six predicted indications.

---

## Literature Evidence

Selected publications for hereditary hypophosphatemic rickets:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | Lancet | XLH is caused by PHEX defects, with FGF23 excess, renal phosphate wasting and reduced calcitriol synthesis |
| [35484227](https://pubmed.ncbi.nlm.nih.gov/35484227/) | 2022 | Consensus Statement | Nat Rev Endocrinol | Evaluation, diagnosis and care of XLH patients |
| [31863781](https://pubmed.ncbi.nlm.nih.gov/31863781/) | 2020 | Review/Guidance | Metabolism | Management of XLH in adults |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Review | Calcif Tissue Int | Diagnosis and therapy of XLH |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Rickets types and treatment with vitamin D and analogues, including calcitriol |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | Horm Res Paediatr | Rickets, vitamin D and calcium/phosphate metabolism |
| [38044258](https://pubmed.ncbi.nlm.nih.gov/38044258/) | 2024 | Review | Best Pract Res Clin Endocrinol Metab | Inherited FGF23-excess syndromes |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Clinical study | Calcif Tissue Int | Bone mass in 17 children with familial hypophosphatemic rickets after calcitriol plus phosphate |
| [32504139](https://pubmed.ncbi.nlm.nih.gov/32504139/) | 2021 | Review | Calcif Tissue Int | New therapies for FGF23-related hypophosphatemia |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Retrospective cohort | J Endocrinol Invest | Growth and body proportions from birth to adulthood in hereditary hypophosphatemic rickets |

The evidence is mostly reviews and guidance; no confirmed Phase 3 RCT was found.

---

## US Market Information

All 10 US licences are cancelled; none are currently valid. No approved indication text is available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021068 | Calcitriol (Sun Pharmaceutical) | Solution | Not available |
| NDA022087 | Calcitrol (Mayne Pharma) | Ointment | Not available |
| ANDA211030 | Calcitriol (Gland Pharma) | Injection | Not available |
| ANDA091356 | Calcitriol (Strides Pharma) | Capsule | Not available |
| ANDA203289 | Calcitriol (Amneal) | Capsule | Not available |

Five more ANDAs, all cancelled, cover capsule and solution forms.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): kidney disease, sarcoidosis, hypercalcemia, nephrocalcinosis, nephrolithiasis, acute urate nephropathy, hyperphosphatemia, hypervitaminosis, pyoureter, arteriosclerosis obliterans.
- **Condition-specific risks** in XLH: hypercalciuria, nephrocalcinosis, and secondary or tertiary hyperparathyroidism, which require monitoring.
- **Drug interactions** (100 recorded):
  - **Major:** cholecalciferol, calcifediol, burosumab.
  - **Moderate:** thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone, bendroflumethiazide), enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butabarbital, butalbital), bile acid sequestrants (cholestyramine, colesevelam, colestipol), digoxin and digitoxin, aluminum hydroxide, and topical calcipotriol.

Please refer to the package insert for full warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for hereditary hypophosphatemic rickets). The other six predictions remain at **Hold**.

**Rationale:**
Calcitriol plus phosphate is a long-standing conventional therapy for XLH. One completed early Phase 1 study and one Phase 4 trial of unknown status, backed by consensus and review literature, support this use. The evidence is short of two completed Phase 3 RCTs, so the L2 placement is conservative. Only mineral-metabolism risks need guardrails.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking data gap for safety screening)
- Detailed mechanism of action data
- Comparison against burosumab and current standard of care
- Monitoring plan for serum calcium, phosphate, PTH, urinary calcium and renal ultrasound for nephrocalcinosis
- Clarification of current US availability, since all licences are cancelled
- Higher-quality controlled trial data, ideally a completed Phase 3 RCT
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

