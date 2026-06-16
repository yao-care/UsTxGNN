---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 487
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Calcitriol: From Calcium Metabolic Disorders to Hereditary Hypophosphatemic Rickets

## One-Sentence Summary

Calcitriol (1,25-dihydroxyvitamin D₃) is the biologically active form of vitamin D, established globally for treating hypocalcemia in chronic renal failure and hypoparathyroidism, though no registrations were found in the queried dataset.
The TxGNN model identifies multiple applications across phosphate metabolism disorders; **Hereditary Hypophosphatemic Rickets** carries the strongest clinical evidence among all predictions, with **7 clinical trials** and **20 publications** currently supporting this direction.
Evidence is rated **L2**, and the recommendation is **Proceed with Guardrails**.

> **Note on prediction ranking**: TxGNN Rank 1 ("obsolete vitamin D deficiency", score 99.96%) represents the drug's own pharmacological mechanism — calcitriol *is* the active form of vitamin D — and uses a MONDO term already marked as obsolete. This report therefore focuses on Rank 7 (Hereditary Hypophosphatemic Rickets), which carries the highest clinical evidence level (L2) and the only actionable recommendation in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not found in dataset; globally established for hypocalcemia in chronic renal failure and hypoparathyroidism |
| Predicted New Indication | Hereditary Hypophosphatemic Rickets |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L2 |
| US Market Status | Not found in dataset (0 licenses); Rocaltrol / Calcijex globally available |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Calcitriol is the terminal active metabolite of vitamin D, produced in renal proximal tubule cells via the CYP27B1 enzyme (1α-hydroxylase). Although formal mechanism-of-action data is not available in this Evidence Pack, calcitriol's pharmacology is extensively characterized in the literature: it binds the vitamin D receptor (VDR), a nuclear receptor that controls gene transcription governing intestinal calcium and phosphate absorption, renal calcium reabsorption, suppression of parathyroid hormone (PTH), and bone mineralization.

Hereditary Hypophosphatemic Rickets — most commonly X-linked hypophosphatemia (XLH), caused by loss-of-function mutations in the *PHEX* gene — represents a direct mechanistic target for calcitriol. PHEX deficiency leads to excess production of fibroblast growth factor 23 (FGF23), which simultaneously drives renal phosphate wasting (causing chronic hypophosphatemia) and suppresses 1α-hydroxylase activity, resulting in inappropriately low calcitriol levels. This dual deficiency of phosphate and active vitamin D prevents normal bone mineralization, producing rickets in children and osteomalacia in adults. Supplementing exogenous calcitriol directly bypasses FGF23-mediated enzyme inhibition, restoring 1,25(OH)₂D₃ signaling to the gut and skeleton.

Combined calcitriol + oral phosphate has been the standard of care for XLH for over four decades, supported by foundational clinical studies (NEJM 1980, J Clin Investigation 1985) and contemporary consensus reviews (Lancet 2024, Calcified Tissue International 2025). It served as the historical comparator arm before burosumab (anti-FGF23 monoclonal antibody) became available. NCT03748966 is now actively examining whether calcitriol monotherapy alone — without phosphate — can achieve therapeutic benefit without the nephrocalcinosis risk associated with the combination regimen. The high TxGNN score (99.28%) faithfully reflects the strong topological connection between calcitriol and the hypophosphatemic rickets disease cluster in the biomedical knowledge graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | **Direct calcitriol monotherapy study in XLH**: children and adults treated with escalating calcitriol doses (without supplemental phosphate) over 1 year; primary hypothesis — calcitriol alone can improve serum phosphate and skeletal mineralization without increasing nephrocalcinosis |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | **Dose-optimization RCT in XLH**: head-to-head comparison of high-dose vs. low-dose active vitamin D combined with neutral phosphate in children; objective is to establish evidence-based weight-based dosing |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completed | 260 | Systematic observational study of inappropriate FGF23 hypersecretion across hypophosphatemia subtypes; completed April 2022; provides mechanistic context establishing calcitriol deficiency as a key consequence of FGF23 excess |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, Not Recruiting | 27 | ENERGY 3 Study: evaluating INZ-701 (recombinant ENPP1) in ENPP1 deficiency-related hypophosphatemia; disease background overlaps with phosphate-wasting rickets spectrum; indirect comparator context |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not Yet Recruiting | 65 | Phosphorus-31 MR spectroscopy to quantify tissue ATP in phosphate diabetes (XLH and acquired forms); biomarker/diagnostic study; contextualizes severity of phosphate depletion treatable with calcitriol |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Unknown | 150 | Cross-sectional study of FGF23, Klotho, and Sclerostin in kidney stone formers; explores the FGF23–calcitriol axis in a related calcium-phosphate disorder |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Withdrawn | 0 | Cinacalcet for familial hypophosphatemic rickets; withdrawn before any enrollment; no usable data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | Lancet | Authoritative XLH review; defines FGF23 excess → suppressed 1α-hydroxylase → calcitriol deficiency as central pathophysiology; establishes calcitriol + phosphate as the pre-burosumab standard of care |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Review | Calcified Tissue International | Current comprehensive review of XLH diagnosis and therapy; reaffirms calcitriol combination approach and contextualizes its role in the burosumab era |
| [38044258](https://pubmed.ncbi.nlm.nih.gov/38044258/) | 2024 | Review | Best Practice & Research: Clinical Endocrinology & Metabolism | Reviews the full spectrum of inherited FGF23 excess (XLH, ADHR, ARHR, syndromic forms); maps calcitriol-based therapy across genetic subtypes |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | Hormone Research in Paediatrics | Broad historical and mechanistic overview of rickets subtypes; covers evolution of calcitriol use from vitamin D-resistant rickets through modern targeted therapy |
| [31863781](https://pubmed.ncbi.nlm.nih.gov/31863781/) | 2020 | Review | Metabolism | Adult XLH management review; documents ongoing disease burden (pain, pseudofractures, enthesopathy) and discusses calcitriol's role in adult long-term management |
| [31392510](https://pubmed.ncbi.nlm.nih.gov/31392510/) | 2020 | Review | Pediatric Nephrology | Details bone, growth plate, and dental pathology in hypophosphatemic rickets; explains mechanistic rationale for why both calcitriol and phosphate supplementation are needed |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical Study | N Engl J Med | Foundational comparative study: 11 children with vitamin D-resistant rickets treated with phosphate alone, ergocalciferol, or calcitriol; calcitriol combination increased intestinal phosphate absorption and reduced required phosphate doses |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical Study | J Clinical Investigation | Landmark high-dose calcitriol study: conventional therapy (vitamin D + phosphate) healed rickets but not osteomalacia; high-dose calcitriol (68.2 ng/kg/day) + phosphate healed both rachitic bone lesion AND osteomalacia in XLH patients |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Cohort | J Endocrinological Investigation | Retrospective cohort study tracking growth from birth to adulthood in hereditary hypophosphatemic rickets; documents disproportionate short stature and limb bowing as treatment endpoints |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Review | Pediatric Endocrinology Reviews | Height data from 127 untreated XLH patients across 49 centers; analyzes effect of early calcitriol + phosphate therapy initiation on spontaneous growth trajectories |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinical caution from established pharmacology**: Calcitriol's primary adverse effects include hypercalcemia and hypercalciuria, which are of particular concern in the XLH treatment context. Long-term high-dose calcitriol + phosphate carries a well-documented risk of nephrocalcinosis — one of the key safety signals that NCT03748966 (calcitriol monotherapy study) is specifically designed to evaluate. Serum calcium, urinary calcium, and renal function should be monitored throughout treatment. Formal warnings, contraindications, and drug interaction data were not available in this Evidence Pack (data gaps DG001 and DG002 remain unresolved).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Calcitriol + oral phosphate supplementation is a pharmacologically sound and clinically validated strategy for hereditary hypophosphatemic rickets (XLH), supported by over 40 years of clinical experience, foundational studies in NEJM and J Clin Investigation, and consensus reviews published in Lancet (2024) and Calcified Tissue International (2025). The FGF23-mediated suppression of 1α-hydroxylase directly explains why calcitriol supplementation is mechanistically appropriate, and NCT03820518 (Phase 4) and NCT03748966 (Early Phase 1) are actively refining dosing and evaluating monotherapy feasibility.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking)**: Download and parse the calcitriol package insert (Rocaltrol/Calcijex) from the prescribing authority to complete safety screening and enable S1 safety evaluation
- **Resolve DG002 (High)**: Query DrugBank API to formalize mechanism-of-action documentation for the evaluation record
- **Confirm local market availability**: Dataset shows 0 licenses, but calcitriol (Rocaltrol) is globally registered; verify current availability and regulatory status for the target jurisdiction
- **Establish safety monitoring protocol**: Define baseline and follow-up schedule for serum calcium, urinary calcium, serum phosphate, creatinine, and renal ultrasound (nephrocalcinosis screening) before initiating therapy
- **Monitor NCT03820518 results**: Phase 4 dose-comparison data will inform whether high- or low-dose calcitriol is preferred in XLH; plan to update this evaluation once trial results are published
- **Consider burosumab positioning**: Document how calcitriol + phosphate compares to the current anti-FGF23 standard in the target patient population, and whether it addresses any unmet need in burosumab-ineligible or resource-constrained settings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

