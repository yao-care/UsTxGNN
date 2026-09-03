---
layout: default
title: Treprostinil
parent: 僅模型預測 (L5)
nav_order: 1256
evidence_level: L5
indication_count: 10
---

# Treprostinil
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

Using no specific skill — this is a direct content-generation task per the explicit report template already provided in your instructions; proceeding straight to the report.

---

# Treprostinil: From Idiopathic Pulmonary Arterial Hypertension to Related PAH Subtypes

## One-Sentence Summary

Treprostinil is a synthetic prostacyclin (IP-receptor) analog already established for treating pulmonary arterial hypertension (PAH). This Evidence Pack screened **10 TxGNN-predicted indications**; the two most credible predictions — **connective tissue disease-associated PAH (CTD-PAH)** and **congenital heart disease-associated PAH (CHD-PAH)** — are well supported (L1/L2 evidence, including a subgroup RCT and a direct treprostinil Phase 2 trial), while **7 of the 10 predictions** (e.g., hypotrichosis, congenital malformation syndromes) have zero supporting trials or literature and are most likely knowledge-graph noise.

## Quick Overview

*(Featured candidate: highest-evidence prediction, CTD-associated PAH)*

| Item | Content |
|------|------|
| Original Indication | Not stated in regulatory data (treprostinil is a marketed prostacyclin analog whose core approved use, per the evidence context, is idiopathic/heritable PAH) |
| Predicted New Indication | Pulmonary arterial hypertension associated with connective tissue disease (CTD-PAH) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed (0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails (applies to CTD-PAH and CHD-PAH only — see full ranking below) |

### All 10 Predicted Indications (Full Ranking)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Pulmonary arteriovenous malformation | 99.70% | L5 | S0 | Hold |
| 2 | PAH associated with congenital heart disease (CHD-PAH) | 99.60% | L2 | S2 | Proceed with Guardrails |
| 3 | PAH associated with chronic hemolytic anemia | 99.55% | L5 | S0 | Hold |
| 4 | PAH associated with schistosomiasis | 99.55% | L5 | S0 | Hold |
| 5 | PAH associated with connective tissue disease (CTD-PAH) | 99.55% | L1 | S3 | Proceed with Guardrails |
| 6 | PAH associated with HIV infection | 99.55% | L3 | S1 | Research Question |
| 7 | Hypotrichosis simplex of the scalp | 99.48% | L5 | S0 | Hold |
| 8 | Congenital hypotrichosis milia | 99.30% | L5 | S0 | Hold |
| 9 | Malformation syndrome with odontal/periodontal component | 99.21% | L5 | S0 | Hold |
| 10 | Ambras type hypertrichosis universalis congenita | 99.17% | L5 | S0 | Hold |

## Why is This Prediction Reasonable?

Treprostinil is a stable synthetic analog of prostacyclin (PGI2). It activates the **IP receptor** on pulmonary vascular smooth muscle and platelets, producing pulmonary vasodilation, inhibition of platelet aggregation, and anti-proliferative effects that counteract vascular remodeling. This mechanism is the pharmacological basis for its established use in PAH (WHO Group 1).

CTD-PAH, CHD-PAH, and HIV-PAH are all recognized **WHO Group 1 PAH subtypes** that share the same core pulmonary vascular remodeling pathophysiology as idiopathic PAH — the population in which treprostinil's efficacy is best established. This shared mechanism explains why the CTD-PAH prediction is backed by a **dedicated subgroup RCT (PMID 15302727)** and why a Phase 2 trial of IV treprostinil was specifically run in CHD-PAH neonates (NCT02261883). PAH associated with chronic hemolytic anemia and schistosomiasis fall under WHO Group 5/1 with more heterogeneous, less prostacyclin-responsive pathophysiology, which is consistent with the complete absence of supporting trials or literature for those two candidates.

In contrast, predictions such as hypotrichosis simplex, congenital hypotrichosis milia, Ambras-type hypertrichosis, and the periodontal/odontal malformation syndrome have **no mechanistic link** to vascular smooth muscle or platelet biology. For the periodontal-component prediction, all 20 retrieved literature hits discuss periodontitis pathophysiology with no mention of treprostinil or prostacyclin pathways — a strong indicator of **keyword-coincidence false positives** in the knowledge graph rather than genuine drug-disease relevance.

## Clinical Trial Evidence

### CHD-Associated PAH (Rank 2, L2)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02261883](https://clinicaltrials.gov/study/NCT02261883) | Phase 2 | Terminated | 42 | IV Remodulin (treprostinil) as add-on therapy in neonates with CHD-related persistent pulmonary hypertension; direct drug evidence but trial was terminated early. |
| [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | Unknown | 42 | Iloprost (a related prostacyclin analog, not treprostinil) in adult Eisenmenger-physiology PAH-CHD; indirect class-level support only. |

### CTD-Associated PAH (Rank 5, L1)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02663895](https://clinicaltrials.gov/study/NCT02663895) | Phase 2 | Completed | 12 | Oral treprostinil in systemic sclerosis; primary endpoint was calcinosis reduction, not PAH itself — indirect safety/tolerability evidence in the same CTD population. |

### HIV-Associated PAH (Rank 6, L3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00494533](https://clinicaltrials.gov/study/NCT00494533) | Phase 4 | Terminated | 45 | RCT of IV Remodulin (treprostinil) vs placebo in PAH including HIV- and collagen vascular disease-associated subgroups; terminated, HIV-specific enrollment criteria unconfirmed. |

### All Other Predictions (Ranks 1, 3, 4, 7, 8, 9, 10)

Currently no related clinical trials registered.

## Literature Evidence

### CHD-Associated PAH (Rank 2)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29436381](https://pubmed.ncbi.nlm.nih.gov/29436381/) | 2018 | Cohort | Heart | Subcutaneous treprostinil in adult CHD-PAH: efficacy/safety after 12 months of treatment — most directly relevant evidence. |
| [35000655](https://pubmed.ncbi.nlm.nih.gov/35000655/) | 2022 | Case Report | Cardiology in the Young | Trisomy 21 + CHD-PAH: hemodynamics and exercise capacity improved after switching from oral selexipag to SC treprostinil. |
| [23890862](https://pubmed.ncbi.nlm.nih.gov/23890862/) | 2013 | Cohort | Int J Cardiol | Long-term continuous prostacyclin therapy (incl. treprostinil) in adults with CHD-PAH. |
| [18473715](https://pubmed.ncbi.nlm.nih.gov/18473715/) | 2008 | Review | Expert Opin Pharmacother | Treprostinil for PH treatment, including CHD-associated etiology. |
| [22872790](https://pubmed.ncbi.nlm.nih.gov/22872790/) | 2012 | Review | Clin Med Insights Circ Respir Pulm Med | Clinical utility of treprostinil across PAH etiologies including CHD. |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | General PAH diagnosis/treatment review (background). |
| [21852894](https://pubmed.ncbi.nlm.nih.gov/21852894/) | 2009 | Cohort | Prog Pediatr Cardiol | Non-CHD pediatric PAH context — background/comparator only. |

### CTD-Associated PAH (Rank 5)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15302727](https://pubmed.ncbi.nlm.nih.gov/15302727/) | 2004 | RCT (subgroup) | Chest | SC treprostinil efficacy/safety specifically in CTD-associated PAH — strongest direct evidence. |
| [11897647](https://pubmed.ncbi.nlm.nih.gov/11897647/) | 2002 | RCT | Am J Respir Crit Care Med | Foundational double-blind, placebo-controlled RCT of continuous SC treprostinil in PAH (includes CTD subgroup). |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review/Meta-analysis | Intern Emerg Med | CTD-PAH treatment outcomes across RCT subgroup/post-hoc analyses. |
| [34462153](https://pubmed.ncbi.nlm.nih.gov/34462153/) | 2021 | Retrospective Multicenter | Rev Med Interne | Characteristics/outcomes of CTD-PAH patients treated with prostanoids. |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals | Recent advances in CTD-PAH treatment. |
| [41594679](https://pubmed.ncbi.nlm.nih.gov/41594679/) | 2026 | Review | Biomolecules | Current therapeutic strategies and future prospects in CTD-PAH. |
| [40005302](https://pubmed.ncbi.nlm.nih.gov/40005302/) | 2025 | Case Report | Medicina | Inhaled treprostinil efficacy in systemic sclerosis-associated PH refractory to IV epoprostenol. |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | PAH associated with connective tissue diseases — pathophysiology overview. |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | Treatment of PAH in connective tissue disease. |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | General PAH diagnosis/treatment review (background). |

### HIV-Associated PAH (Rank 6)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Review | Am J Respir Med | Prostanoids for PAH, including HIV-associated subgroup. |
| [18473715](https://pubmed.ncbi.nlm.nih.gov/18473715/) | 2008 | Review | Expert Opin Pharmacother | Treprostinil for PH, including HIV-associated etiology. |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | Prostanoids in PAH treatment across etiologies including HIV infection. |

### Low-Confidence Predictions (Ranks 1, 3, 4, 7, 8, 9, 10)

Currently no related literature available, **except** the malformation-syndrome candidate (Rank 9), where 20 literature hits were retrieved — all exclusively about periodontitis pathophysiology/treatment with **no mention of treprostinil or prostacyclin pathways**. This is assessed as keyword-coincidence noise, not genuine supporting evidence.

## US Market Information

Treprostinil currently has **0 marketing licenses on file** and is **not marketed** in this jurisdiction. No approved-indication label text is available for comparison against the predicted indications.

## Safety Considerations

Please refer to the package insert for safety information.

**Critical data gap:** Detailed labeled warnings and contraindications (TFDA label PDF) have not yet been retrieved (Blocking severity). This gap must be closed before any indication in this pack can proceed past initial safety screening (S1).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for CTD-PAH and CHD-PAH only) / **Hold** (for the remaining 7 low-evidence candidates)

**Rationale:**
- CTD-PAH is backed by a dedicated subgroup RCT plus a 2024 systematic review/meta-analysis and mechanistically fits treprostinil's established WHO Group 1 PAH indication (L1).
- CHD-PAH has a direct (though terminated) Phase 2 treprostinil trial and coherent mechanistic rationale (L2).
- HIV-PAH has only review-level, non-drug-specific literature (L3) — flagged for further research rather than progression.
- The remaining 6 candidates (pulmonary arteriovenous malformation, hemolytic anemia-PAH, schistosomiasis-PAH, hypotrichosis simplex, congenital hypotrichosis milia, Ambras hypertrichosis) and the periodontal malformation-syndrome candidate have no genuine supporting evidence and should not be pursued.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/manufacturer package insert for full warnings, contraindications, and DDI data (Blocking gap, DG001)
- Confirm original approved indication and MOA directly from DrugBank/regulatory source rather than inference (DG002)
- For CHD-PAH: obtain termination reason and any interim data from NCT02261883
- For HIV-PAH: verify actual enrollment criteria of NCT00494533 to confirm HIV-specific subgroup data exists
- Route/formulation compatibility assessment (SC/IV/inhaled/oral) against each target population's clinical practicality
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

