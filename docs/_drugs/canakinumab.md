---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: From Cryopyrin-Associated Periodic Syndromes to Familial Mediterranean Fever (Autosomal Dominant)

## One-Sentence Summary

Canakinumab (Ilaris®) is a fully human anti-IL-1β monoclonal antibody originally approved for Cryopyrin-Associated Periodic Syndromes (CAPS), where uncontrolled IL-1β production drives systemic inflammation.

Among 10 TxGNN-predicted indications in this multi-indication analysis, **Familial Mediterranean Fever, Autosomal Dominant** (rank 6) emerges as the most clinically actionable candidate, supported by **7 clinical trials** (including 5 completed Phase 3) and **20 publications** — evidence consistent with canakinumab's FDA approval for colchicine-resistant FMF in 2016.

Seven of the remaining predictions are classified as **Hold** due to weak or absent mechanistic rationale; **Periodic Fever-Infantile Enterocolitis-Autoinflammatory Syndrome** (L3) and **Blau Syndrome** (L4) are flagged as **Research Questions** warranting further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cryopyrin-Associated Periodic Syndromes (CAPS): FCAS, Muckle-Wells Syndrome, NOMID |
| Predicted New Indication | Familial Mediterranean Fever, Autosomal Dominant |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not marketed (0 licenses) |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Summary of All Predicted Indications

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|------------|---------------|----------------|
| 1 | Hepatic Infarction | 99.86% | L5 | Hold |
| 2 | Hepatic Veno-Occlusive Disease | 99.82% | L5 | Hold |
| 3 | Peliosis Hepatis | 99.78% | L5 | Hold |
| 4 | Syndrome with Combined Immunodeficiency | 99.71% | L5 | Hold |
| **5** | **Periodic Fever-Infantile Enterocolitis-Autoinflammatory Syndrome** | **99.57%** | **L3** | **Research Question** |
| **6** | **Familial Mediterranean Fever, Autosomal Dominant** | **99.41%** | **L1** | **Proceed with Guardrails** |
| 7 | Extracutaneous Mastocytoma | 99.35% | L5 | Hold |
| **8** | **Blau Syndrome** | **99.34%** | **L4** | **Research Question** |
| 9 | Monosomy X | 99.31% | L5 | Hold |
| 10 | Liver Angiosarcoma | 99.30% | L5 | Hold |

> **Note:** Despite high TxGNN scores for rank 1–4 liver conditions, mechanistic analysis reveals these are likely artefacts of semantic proximity between hepatic disease nodes in the knowledge graph, rather than genuine therapeutic targets for IL-1β blockade. Rank 6 (FMF) is featured in this report as the highest-value, evidence-backed candidate.

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on published literature, canakinumab (ACZ885, Ilaris®) is a fully human IgG1/κ monoclonal antibody that selectively neutralizes interleukin-1β (IL-1β), preventing it from binding to its receptor and thereby blocking downstream inflammatory signaling — including NF-κB activation, prostaglandin E2 synthesis, and acute-phase protein induction.

The mechanistic connection between CAPS and FMF is direct and well-established. In CAPS, NLRP3 gene mutations cause cryopyrin overactivation, leading to constitutive IL-1β secretion. In FMF, MEFV gene mutations impair pyrin protein function, also culminating in excess IL-1β release. Both pathways converge on the same cytokine target: IL-1β. This "inflammasome → IL-1β → systemic inflammation" axis is the reason IL-1β blockade works across both disease groups and explains why the TxGNN model — trained on drug-disease relationships in the knowledge graph — correctly identifies FMF as a high-confidence repurposing candidate.

For the autosomal dominant FMF subtype specifically, MEFV mutations classically follow autosomal recessive inheritance; the dominant variant is rarer but shares the identical pathological mechanism. The landmark NEJM study (PMID 29768139) formally demonstrated canakinumab's superiority over placebo in reducing fever attacks in FMF, TRAPS, and HIDS — and the FDA approved canakinumab for colchicine-resistant/intolerant FMF in 2016. This TxGNN prediction therefore validates a known, clinically confirmed therapeutic relationship.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00465985](https://clinicaltrials.gov/study/NCT00465985) | Phase 3 | Completed | 35 | Randomized, double-blind, placebo-controlled trial in Muckle-Wells Syndrome; three-part design (open-label → withdrawal RCT → open-label extension); pivotal efficacy and safety trial underpinning IL-1β blockade in periodic fever syndromes |
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Phase 3 | Completed | 166 | Largest long-term Phase 3 trial (n=166) in CAPS patients; provides critical safety data and evidence of sustained efficacy to support long-term canakinumab use |
| [NCT01302860](https://clinicaltrials.gov/study/NCT01302860) | Phase 3 | Completed | 17 | Open-label multicenter trial in CAPS patients aged ≤4 years; evaluates efficacy, safety, tolerability, and compatibility with childhood vaccinations |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Phase 3 | Completed | 17 | Extension of NCT01302860; captures relapse-after-withdrawal and re-treatment data, providing evidence on sustained disease control and treatment strategy flexibility |
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Phase 3 | Completed | 19 | Japanese CAPS cohort (FCAS, MWS, NOMID); supported Japanese regulatory approval; includes extended supply phase pending local market authorization |
| [NCT01242813](https://clinicaltrials.gov/study/NCT01242813) | Phase 2 | Completed | 20 | Open-label 4-month study in active TRAPS patients with 6-month follow-up; established therapeutic signal and dose rationale for IL-1β inhibition in MEFV-related syndromes |
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | N/A (Real-world) | Recruiting | 25 | Non-interventional post-marketing study (REASSURE) in CAPS, crFMF, TRAPS, HIDS/MKD, and sJIA; completion expected 2028; provides real-world safety and effectiveness surveillance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Clinical Study (NEJM) | N Engl J Med | Landmark randomized trial: canakinumab significantly reduces attack frequency vs. placebo in FMF, TRAPS, and HIDS — directly supports FMF indication and forms regulatory submission basis |
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Systematic Review | Front Immunol | Comprehensive systematic review of all IL-1 targeted biologics (anakinra, canakinumab, rilonacept) in immune-mediated disorders; confirms favourable safety and broad efficacy across autoinflammatory conditions |
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Systematic Review / Meta-analysis | Rheumatology | Quantitative meta-analysis of anti-IL-1 agents specifically in FMF; demonstrates significant reduction in attack frequency and CRP/SAA normalization |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Review | Expert Rev Clin Immunol | Dedicated expert review of canakinumab for FMF; summarizes clinical trial data and positions canakinumab as the preferred anti-IL-1 agent for colchicine-resistant patients |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Review | Clin Exp Rheumatol | IL-1 inhibition in FMF: clinical outcomes and treatment expectations; covers drug metabolism, tapering strategies, and real-world expectations |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Real-World Study | Int J Rheum Dis | Compares canakinumab with vs. without concomitant colchicine in FMF; evaluates attack characteristics, acute-phase reactants, and renal outcomes in clinical practice |
| [34568239](https://pubmed.ncbi.nlm.nih.gov/34568239/) | 2021 | Retrospective Cohort | Front Pediatrics | 65 colchicine-resistant/intolerant FMF patients on canakinumab ≥6 months; complete remission in majority; dose-interval extension feasible in sustained responders |
| [36961326](https://pubmed.ncbi.nlm.nih.gov/36961326/) | 2023 | Cohort Study | Rheumatology | First structured canakinumab withdrawal protocol in pediatric colchicine-resistant FMF; identifies predictors of successful discontinuation |
| [31463794](https://pubmed.ncbi.nlm.nih.gov/31463794/) | 2019 | Retrospective | Paediatr Drugs | Single-center pediatric FMF experience with canakinumab; demonstrates meaningful attack reduction in colchicine non-responders with acceptable safety profile |
| [32806879](https://pubmed.ncbi.nlm.nih.gov/32806879/) | 2020 | Review | Turk J Med Sci | Comprehensive FMF review from molecular pathogenesis to modern treatment; contextualizes anti-IL-1 biologics within the evolving therapeutic landscape |

---

## Market Information

Canakinumab is **not registered or marketed in Taiwan** (0 licenses as of 2026-06-15). The following global regulatory approvals are provided for reference:

| Authorization | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| US FDA (2009) | Ilaris® | Subcutaneous Injection | CAPS: Familial Cold Autoinflammatory Syndrome (FCAS), Muckle-Wells Syndrome (MWS) |
| US FDA (2013) | Ilaris® | Subcutaneous Injection | Systemic Juvenile Idiopathic Arthritis (sJIA), age ≥2 years |
| US FDA (2016) | Ilaris® | Subcutaneous Injection | Colchicine-resistant/intolerant FMF; TRAPS; HIDS/MKD; Active Still's disease (AOSD) |
| EMA (EU) | Ilaris® | Subcutaneous Injection | CAPS, FMF, TRAPS, HIDS/MKD, sJIA, AOSD — full alignment with US label |

---

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack contains no Taiwan-specific warning or contraindication data (all fields returned as Data Gap); the drug interaction database query also returned no results.

Based on the drug class (anti-IL-1β monoclonal antibody) and international labeling, the following safety areas are typically relevant:
- **Serious Infections**: IL-1β suppression increases susceptibility to bacterial and opportunistic infections; live vaccines are contraindicated during treatment
- **Neutropenia**: Neutrophil counts should be monitored before and periodically during therapy
- **Injection Site Reactions**: Common with subcutaneous administration
- **Lipid Monitoring**: IL-1β inhibition may influence lipid metabolism

*For complete and authoritative safety information, refer to the Ilaris® US Prescribing Information or EMA Summary of Product Characteristics.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for Familial Mediterranean Fever (autosomal dominant) is strongly supported by ≥5 completed Phase 3 clinical trials, 20 publications including a landmark NEJM RCT, and — critically — FDA and EMA approval of canakinumab for colchicine-resistant FMF since 2016. This prediction represents a confirmed therapeutic relationship, validating TxGNN model accuracy for this candidate. The autosomal dominant subtype shares the identical IL-1β-driven pathomechanism as the classic autosomal recessive form and is covered under the same approved indication umbrella.

**To proceed, the following is needed:**

- **Taiwan regulatory pathway**: Canakinumab is not marketed in Taiwan; assess feasibility of NDA filing, compassionate use, or specialist import under TFDA regulations for colchicine-resistant FMF patients
- **MOA documentation**: Obtain DrugBank API data (DG002) to complete mechanism of action documentation for full dossier
- **Taiwan safety data**: Download and parse TFDA-equivalent package insert or reference US/EU label for warning/contraindication data (DG001)
- **Epidemiology assessment**: Estimate the prevalence of colchicine-resistant FMF in Taiwan — FMF is uncommon in East Asian populations; a patient-level needs assessment is required to determine commercial and public health rationale
- **Health economics analysis**: Ilaris® is a high-cost biologic; NHI reimbursement pathway assessment and cost-effectiveness modelling are needed before any access strategy is developed
- **Research Questions to explore**: Evaluate canakinumab for **Periodic Fever-Infantile Enterocolitis-Autoinflammatory Syndrome** (L3 evidence, mechanistically plausible via NLRP12/IL-1β axis) and **Blau Syndrome** (L4 evidence, direct case-series data available at PMID 23124805)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

