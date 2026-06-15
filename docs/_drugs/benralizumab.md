---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 445
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

以下是根據 Evidence Pack 生成的完整評估報告：

---

# Benralizumab: From Severe Eosinophilic Asthma to Dermatitis

## One-Sentence Summary

Benralizumab is an anti-IL-5 receptor α (IL-5Rα) monoclonal antibody proven effective in severe eosinophilic asthma, acting by depleting eosinophils and basophils via antibody-dependent cell-mediated cytotoxicity (ADCC).
The TxGNN model predicts it may be effective for **Dermatitis**, with **6 clinical trials** and **20 publications** currently supporting this direction.
However, the pivotal Phase 2 RCT (HILLIER, NCT04605094, n=194) was terminated early with negative results for broad atopic dermatitis, suggesting any remaining opportunity is restricted to eosinophil-predominant subtypes such as DRESS/DiHS.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma (globally approved; not found in current dataset) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L2 |
| US Market Status | Not Marketed (0 records in current registry) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benralizumab binds directly to IL-5Rα on eosinophils and basophils, triggering ADCC-mediated near-complete depletion of these cells. This mechanism was validated in severe eosinophilic asthma, where excessive eosinophil-driven airway inflammation drives disease. Because IL-5Rα is expressed broadly wherever eosinophils accumulate — not just in the lung — the biological rationale for extending benralizumab to other eosinophilic conditions is sound in principle.

Dermatitis, particularly atopic dermatitis (AD) and drug reaction with eosinophilia and systemic symptoms (DRESS/DiHS), shares key pathophysiological features with eosinophilic asthma: tissue eosinophilia, type 2 innate lymphoid cell (ILC2) activation, and IL-5 overproduction driving eosinophil recruitment and prolonged survival in affected tissue. A 2025 translational study (PMID 40781582) directly confirmed that benralizumab depletes IL-5Rα-bearing cells in AD skin lesions, establishing that the drug does reach and engage its target at the disease site.

Despite this biologically coherent hypothesis, the HILLIER trial (NCT04605094) — a randomized, double-blind, placebo-controlled study enrolling 194 patients with moderate-to-severe AD — was terminated early due to lack of efficacy (PMID 37178404). This outcome highlights that for most AD patients, where the dominant inflammatory drivers are IL-4 and IL-13 rather than IL-5, depleting eosinophils alone is insufficient. The remaining mechanistically justified niche lies in diseases where eosinophilia is a defining — not incidental — feature: DRESS/DiHS is the clearest candidate, and an active Phase 2 trial (NCT06734884) is currently addressing this question.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Not Yet Recruiting | 96 | Evaluating benralizumab in DRESS (Drug Reaction with Eosinophilia and Systemic Symptoms) — eosinophils are a defining feature of DRESS pathology, making IL-5Rα depletion mechanistically compelling; highest-priority active study for this indication |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Completed | 20 | Exploratory study of benralizumab in atopic dermatitis — confirmed eosinophil and basophil depletion in skin (target engagement proven), but limited clinical response; small sample size; provides critical biomarker data for patient selection in future trials |
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | Terminated | 194 | **HILLIER Study** — randomized, double-blind, placebo-controlled RCT in moderate-to-severe AD; terminated early due to lack of efficacy; combined with PMID 37178404, this constitutes the principal negative evidence against broad AD indication |
| [NCT06477653](https://clinicaltrials.gov/study/NCT06477653) | Phase 2 | Recruiting | 30 | Dupilumab add-on therapy in hypereosinophilic syndrome (HES) patients with partial response to eosinophil-depleting biologics — indirect evidence relevant to eosinophilic skin overlap; supports the residual-eosinophil hypothesis in refractory cases |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | N/A | Completed | 28 | Observational retrospective study of benralizumab in severe eosinophilic asthma in Spain — real-world safety profile and responder phenotype characterization; provides supporting safety context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | Phase 2 RCT | JEADV | **KEY NEGATIVE**: HILLIER primary results — benralizumab showed no significant effect on signs or symptoms of moderate-to-severe AD; critical evidence against pursuing broad atopic dermatitis indication |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | Phase 2 RCT | Immunotherapy | HILLIER plain language summary — confirms early termination and negative outcome; underscores the need for eosinophil-enriched patient selection in any future dermatitis trials |
| [40781582](https://pubmed.ncbi.nlm.nih.gov/40781582/) | 2025 | Mechanistic Study | Clin Transl Allergy | Benralizumab depletes IL-5Rα-bearing cells in AD skin lesions — validates target engagement in skin tissue; distinguishes pharmacological activity from clinical efficacy |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Narrative Review | Allergologie select | Comprehensive update on biologics for atopic diseases and urticaria including benralizumab; positions anti-IL-5Rα within the evolving type 2 biologics landscape |
| [36355314](https://pubmed.ncbi.nlm.nih.gov/36355314/) | 2023 | Review | Dermatology and Therapy | Dupilumab combination strategies — contextualizes scenarios where add-on benralizumab may be considered for AD patients with concomitant eosinophilic conditions |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Review | Immunol Allergy Clin N Am | Biologics (including benralizumab) during pregnancy and lactation — key reference for safety profiling in women of childbearing age presenting with dermatitis |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Review | J Allergy Clin Immunol Pract | Safety review of 7 FDA-approved biologics including benralizumab during pregnancy — summarizes maternal and fetal outcomes relevant to special population counselling |
| [33236428](https://pubmed.ncbi.nlm.nih.gov/33236428/) | 2020 | Review | Pediatr Allergy Immunol | Anti-IL-5 biologics in pediatric allergic diseases — background on the IL-5 axis in childhood atopic dermatitis and rationale for eosinophil-targeting approaches |
| [34642091](https://pubmed.ncbi.nlm.nih.gov/34642091/) | 2021 | Review | Ann Allergy Asthma Immunol | Practical guide for biologic selection across asthma, urticaria, nasal polyps, and atopic dermatitis — includes benralizumab positioning and emerging indications |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Narrative Review | Allergy Asthma Proc | Review of anti-IL-5 biologics (mepolizumab, reslizumab, benralizumab) for severe asthma, atopic dermatitis, and chronic urticaria — foundational reference for the eosinophil-dermatitis hypothesis |

---

## US Market Information

No authorization records were found in the current regulatory dataset (0 NDAs on file). The registry query returned no approved indications for benralizumab in this dataset.

> **Note:** Benralizumab is marketed globally as **Fasenra** (AstraZeneca) and is FDA-approved in the United States for severe eosinophilic asthma. The absence of records above likely reflects a data gap in the current registry rather than actual non-approval status. Please verify against the official FDA Drugs@FDA database for US authorization details.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No warnings, contraindications, or drug interaction data were available in the current dataset. As a biologic monoclonal antibody, benralizumab carries class-level considerations including hypersensitivity reactions and potential effects on vaccine responses (see PMID 38878020 for reduced post-vaccination SARS-CoV-2 immunity observed with benralizumab and related biologics).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-quality direct evidence — the HILLIER Phase 2 RCT (NCT04605094, n=194) — demonstrated no efficacy for benralizumab in broad moderate-to-severe atopic dermatitis and was terminated early, making a general "dermatitis" indication untenable under current evidence. The mechanistic rationale remains valid only for eosinophil-predominant disease subtypes, principally DRESS/DiHS, which is still under active investigation.

**To proceed, the following is needed:**
- **Await DRESS trial results**: NCT06734884 (Phase 2, n=96) is the pivotal next data point; monitor for recruitment initiation and interim data
- **Biomarker-driven patient selection**: Define minimum blood/tissue eosinophil thresholds (e.g., blood eosinophils ≥300 cells/μL, tissue eosinophil density in biopsy) as enrollment criteria for any new dermatitis study
- **Safety data**: Obtain full package insert warnings and contraindications to enable regulatory-compliant benefit-risk assessment
- **Mechanistic gap fill**: Clarify why target engagement (PMID 40781582) did not translate to clinical response in HILLIER — explore whether IL-4/IL-13 pathway compensates in broad AD
- **MOA documentation**: Retrieve complete DrugBank pharmacology record (DrugBank ID: DB12023) to support regulatory submissions and clinician communications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

