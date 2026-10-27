---
layout: default
title: Revefenacin
parent: Model Prediction Only (L5)
nav_order: 1118
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Revefenacin: predicted new indication Bronchitis (evidence level L5). Approved use: Chronic obstructive pulmonary disease (COPD)"
monitor_inn: "REVEFENACIN"
predicted_indications: ["bronchitis"]
---

# Revefenacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Revefenacin: From COPD to Bronchitis / Obstructive Lung Disease
{: .text-alpha }

## One-Sentence Summary

Revefenacin is a once-daily, nebulized long-acting muscarinic antagonist (LAMA) originally used for the maintenance treatment of chronic obstructive pulmonary disease (COPD).
The TxGNN model predicts it may be effective for **bronchitis** (top-ranked prediction) and **obstructive lung disease** (second-ranked prediction), but both predictions largely reflect disease-classification overlap with COPD rather than true new indications.
For obstructive lung disease, **13 clinical trials** (including several completed Phase 3 RCTs) and **20 publications** are available; for bronchitis, only **1 clinical trial** (COPD population) and no literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic obstructive pulmonary disease (COPD) |
| Predicted New Indication | Bronchitis (rank 1); Obstructive lung disease (rank 2) |
| TxGNN Prediction Score | Bronchitis 99.61%; Obstructive lung disease 99.10% |
| Evidence Level | Bronchitis: L3 (indirect only); Obstructive lung disease: L1 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 |
| Recommended Decision | Proceed with Guardrails (obstructive lung disease); Hold / research question only (bronchitis) |

---

## Why is This Prediction Reasonable?

Revefenacin is a lung-selective, long-acting muscarinic antagonist. It blocks M3 muscarinic receptors on airway smooth muscle, reducing cholinergic tone and producing sustained bronchodilation suitable for once-daily nebulized dosing. Detailed mechanism of action data was not available in the data compiled for this report; the description above is based on the published literature and the drug's known class.

The two predicted indications are closely related to the original one. Chronic bronchitis is a component of COPD, and "obstructive lung disease" is the umbrella category that includes COPD. The very high TxGNN scores most likely reflect this nosological proximity. This is therefore mainly a confirmation of the existing COPD indication, not a novel repurposing. There is no direct evidence in isolated bronchitis (non-COPD) populations, and extension to other obstructive diseases such as asthma is not supported by the available data.

---

## Clinical Trial Evidence

### Bronchitis

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01704404](https://clinicaltrials.gov/study/NCT01704404) | Phase 2 | Completed | 62 | 7-day dose-response, safety and PK study in COPD; indirect support only, no bronchitis-specific efficacy data |

### Obstructive Lung Disease

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02518139](https://clinicaltrials.gov/study/NCT02518139) | Phase 3 | Completed | 1060 | 52-week safety and tolerability of nebulized revefenacin vs tiotropium in moderate to very severe COPD |
| [NCT02459080](https://clinicaltrials.gov/study/NCT02459080) | Phase 3 | Completed | 619 | 12-week placebo-controlled study of effectiveness and safety in moderate to very severe COPD |
| [NCT02512510](https://clinicaltrials.gov/study/NCT02512510) | Phase 3 | Completed | 611 | Replicate 12-week pivotal placebo-controlled efficacy trial in COPD |
| [NCT05165485](https://clinicaltrials.gov/study/NCT05165485) | Phase 4 | Completed | 404 | Revefenacin vs tiotropium (HandiHaler) over 12 weeks in severe to very severe COPD with suboptimal inspiratory flow |
| [NCT02040792](https://clinicaltrials.gov/study/NCT02040792) | Phase 2 | Completed | 355 | 28-day dose-ranging, placebo-controlled study of four doses |
| [NCT05046795](https://clinicaltrials.gov/study/NCT05046795) | Phase 3 | Completed | 258 | 12-week placebo-controlled study of 175 mcg once daily in Chinese patients with COPD |
| [NCT03095456](https://clinicaltrials.gov/study/NCT03095456) | Phase 3 | Completed | 207 | Once-daily nebulized revefenacin vs Spiriva HandiHaler in COPD with low peak inspiratory flow |
| [NCT03573817](https://clinicaltrials.gov/study/NCT03573817) | Phase 3 | Completed | 122 | 42-day safety and tolerability of revefenacin with formoterol (sequential vs combined) |
| [NCT07133880](https://clinicaltrials.gov/study/NCT07133880) | Phase 4 | Recruiting | 72 | Nebulizer vs dry powder inhaler delivery of long-acting bronchodilators in symptomatic COPD |
| [NCT02109172](https://clinicaltrials.gov/study/NCT02109172) | Phase 2 | Completed | 64 | Crossover study of once-daily vs twice-daily nebulized dosing vs placebo |

*Additional trials not listed above include NCT03064113 (Phase 2, n=32), NCT04315558 (RARICO, Phase 2, n=21, acute respiratory failure in COPD) and NCT02772159 (Phase 1 ADME, n=9).*

---

## Literature Evidence

No literature was found specific to bronchitis. The publications below are the most relevant for obstructive lung disease (COPD).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31150963](https://pubmed.ncbi.nlm.nih.gov/31150963/) | 2019 | Phase 3 trial (safety) | Respiratory Medicine | 52-week safety and tolerability of revefenacin 88 and 175 μg in moderate to very severe COPD |
| [29096627](https://pubmed.ncbi.nlm.nih.gov/29096627/) | 2017 | RCT | Respiratory Research | 28-day placebo-controlled study of bronchodilation efficacy and adverse events |
| [32106777](https://pubmed.ncbi.nlm.nih.gov/32106777/) | 2020 | RCT (subgroup) | Ther Adv Respir Dis | Efficacy and safety in patients taking concomitant LABA or ICS/LABA |
| [36681255](https://pubmed.ncbi.nlm.nih.gov/36681255/) | 2023 | RCT (post hoc) | Respiratory Medicine | Improvements in health status (SGRQ, CAT, CCQ) in women and men |
| [34875569](https://pubmed.ncbi.nlm.nih.gov/34875569/) | 2022 | Meta-analysis | Heart & Lung | Safety of revefenacin at the approved dose in COPD |
| [31152911](https://pubmed.ncbi.nlm.nih.gov/31152911/) | 2019 | Phase 3 safety analysis | Pulm Pharmacol Ther | No clinically meaningful ECG changes over up to 52 weeks |
| [28987804](https://pubmed.ncbi.nlm.nih.gov/28987804/) | 2018 | Phase 2 RCTs | Pulm Pharmacol Ther | Pharmacodynamics, PK and safety from two randomized phase 2 studies |
| [39429809](https://pubmed.ncbi.nlm.nih.gov/39429809/) | 2024 | Clinical analysis | Int J COPD | FEV1 area-under-the-curve spirometry in moderate to very severe COPD |
| [30803279](https://pubmed.ncbi.nlm.nih.gov/30803279/) | 2019 | Review | Expert Rev Clin Pharmacol | Overview of revefenacin for COPD |
| [31847629](https://pubmed.ncbi.nlm.nih.gov/31847629/) | 2020 | Review | Expert Rev Respir Med | Role of revefenacin among LAMA/LABA maintenance options and device selection |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210598 | YUPELRI (Viatris Specialty LLC) | Solution | Status: cancelled; indication text not available |

The only US authorization is recorded as cancelled, so commercial availability should be verified before any action.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. All those listed are of Moderate severity. Most are additive anticholinergic effects with other antimuscarinic agents, including hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolate, methscopolamine, propantheline and scopolamine. Other moderate interactions include cobicistat, promethazine, eltrombopag, artesunate, abiraterone, eluxadoline, obeticholic acid and prucalopride.

Please refer to the package insert for warnings and contraindications, as this information was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for obstructive lung disease/COPD); **Hold** for bronchitis as a stand-alone indication (research question only).

**Rationale:**
- For obstructive lung disease, multiple completed Phase 3 RCTs and a Phase 4 trial show improved lung function and an acceptable safety profile. However, this largely confirms the already-approved COPD indication rather than a new one.
- For bronchitis, there is no direct evidence outside COPD, and the high TxGNN score likely reflects disease-classification proximity.

**To proceed, the following is needed:**
- Verify current commercial availability, since the only US NDA is listed as cancelled
- Obtain the FDA package insert warnings and contraindications
- Obtain detailed mechanism of action data from DrugBank
- Bronchitis-specific data in non-COPD populations, if that indication is to be pursued
- Evidence for any extension to non-COPD obstructive diseases such as asthma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

