---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
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

Using the `txgnn-pipeline` skill — no additional constraints beyond the system prompt for report generation. Proceeding to produce the evaluation report.

---

**Report scope decision:** The Evidence Pack contains 7 predicted indications. Predictions ranked 1–3 and 5 are all **Hold / L5** with no clinical evidence. The most actionable finding is **Infectious Otitis Media** (array index 3; TxGNN rank 4), which carries L1 evidence, 3 clinical trials, and 19 publications with a "Proceed with Guardrails" recommendation. This indication is selected as the primary focus of the report, with a full prediction summary provided in the Conclusion.

---

# Ceftriaxone: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic broadly used to treat serious bacterial infections — including meningitis, sepsis, pneumonia, and gonococcal infections — via parenteral administration.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**, the highest-quality prediction among seven candidates in this analysis, with **3 clinical trials** and **19 publications** currently supporting this direction.
Although TxGNN ranks this indication 4th by raw model score, it is the only prediction with sufficient clinical evidence (Level L1) and carries a **Proceed with Guardrails** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (meningitis, sepsis, pneumonia, gonococcal infections) — *based on known pharmacology; no regulatory records in current dataset* |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| US Market Status | No records in current dataset (data gap — see note below) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

> ⚠️ **Market Status Note:** The dataset returns `market_status: "未上市"` with zero licenses for Ceftriaxone. This is almost certainly a data pipeline gap — Ceftriaxone is widely available as a generic product in the United States under multiple FDA approvals. Manual verification via the FDA Orange Book is required before drawing any regulatory conclusions from this field.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset (Data Gap DG002). Based on well-established pharmacological knowledge, Ceftriaxone is a **third-generation cephalosporin** that acts by binding to penicillin-binding proteins (PBPs) on the bacterial cell membrane, inhibiting peptidoglycan cross-linking, disrupting cell wall synthesis, and ultimately triggering bacterial autolysis. Its plasma half-life of approximately 8 hours enables once-daily (or even single-dose) intramuscular administration — a distinct clinical advantage in pediatric outpatient settings where intravenous access is impractical.

The mechanistic connection to infectious otitis media (AOM) is direct and well-established. The three primary bacterial pathogens of AOM — *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis* — are all within Ceftriaxone's antimicrobial sensitivity spectrum, including many penicillin-resistant strains of *S. pneumoniae*. This coverage is precisely why intramuscular Ceftriaxone became a clinical alternative for AOM cases unresponsive to first-line amoxicillin therapy.

It is important to note that this TxGNN prediction is not a novel repurposing discovery — it is a **validation of existing clinical practice**. Ceftriaxone's single-dose and three-day IM regimens for AOM are already referenced in US treatment consensus guidelines and have been evaluated in multiple prospective RCTs dating back to the 1990s. The model's high prediction score (99.26%) reflects strong biological plausibility encoded in the underlying knowledge graph, consistent with decades of clinical use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicenter double-blind RCT in children aged 6–23 months comparing 5-day vs 10-day antibiotic courses for AOM, designed to assess whether shorter treatment duration reduces antimicrobial resistance without compromising clinical outcomes. **Terminated early** — the reason for termination should be clarified before drawing efficacy conclusions; if administrative/funding-related (not safety), partial data may still be informative. |
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A | Completed | 391 | Post-marketing observational study of Prevnar 13 (PCV13) impact on otitis media incidence in children. Focuses on vaccine-mediated prevention rather than antibiotic treatment; Ceftriaxone is not the primary intervention. Useful as background context on shifting pneumococcal serotype epidemiology. |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completed | 250 | RCT comparing tympanostomy tube placement vs non-surgical management for recurrent AOM over a 2-year follow-up period. Surgical intervention study — Ceftriaxone is not directly evaluated. Provides context on management of treatment-refractory recurrent AOM. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Prospective, randomized, single-blind trial: single IM dose of Ceftriaxone vs 10-day oral TMP-SMZ for AOM. Established Ceftriaxone single-dose IM as a clinically effective AOM treatment — a landmark study in the field. |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | Clinical Trial | *Pediatric Infect Dis J* | Compared 1-day vs 3-day IM Ceftriaxone regimens in children with nonresponsive AOM. Found the 3-day regimen bacteriologically and clinically superior, especially against penicillin-resistant *S. pneumoniae*. |
| [12237596](https://pubmed.ncbi.nlm.nih.gov/12237596/) | 2002 | Prospective Cohort | *Pediatric Infect Dis J* | Studied dynamics of pneumococcal nasopharyngeal carriage during/after 1-day vs 3-day IM Ceftriaxone therapy for nonresponsive AOM; 3-day regimen more effective at clearing resistant strains. |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Retrospective Cohort | *Int J Pediatric Otorhinolaryngol* | Real-world analysis of Ceftriaxone use patterns for AOM in a large US primary care academic population; identifies increasing IM Ceftriaxone use, particularly for otitis-conjunctivitis syndrome, as an antimicrobial stewardship concern. |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Clinical Practice Guideline | *JAMA Network Open* | National review of pediatric outpatient antibiotic appropriateness in the US; addresses Ceftriaxone as a second-line option for AOM and highlights prescribing patterns requiring stewardship oversight. |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review | *Otology & Neurotology* | Recommendations for AOM prevention and treatment in children with cochlear implants (high-risk population); Ceftriaxone endorsed as a key treatment option for complicated or nonresponsive AOM cases. |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Review | *Pediatrics* | AAP clinical report on cochlear implant-associated infections; endorses Ceftriaxone for AOM with complications or at-risk children due to its parenteral route and broad-spectrum coverage. |
| [38368849](https://pubmed.ncbi.nlm.nih.gov/38368849/) | 2024 | Review | *Am J Emergency Medicine* | Reviews acute mastoiditis (a suppurative complication of AOM); Ceftriaxone cited as standard first-line IV/IM empirical therapy for mastoiditis, reinforcing its role in the AOM severity spectrum. |
| [30279114](https://pubmed.ncbi.nlm.nih.gov/30279114/) | 2019 | Observational | *J Infect Chemother* | Japanese surveillance of antimicrobial susceptibility of *S. pneumoniae*, *H. influenzae*, and *M. catarrhalis* isolated from children with AOM (2014–2017); Ceftriaxone susceptibility data for Japanese pediatric AOM pathogens. |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Review | *Clinical Therapeutics* | Consolidated review of AOM antimicrobial treatment recommendations; synthesizes three published guideline sets and discusses the role of Ceftriaxone for treatment-refractory AOM. |

---

## US Market Information

No authorization records were found for Ceftriaxone in the current regulatory dataset (0 licenses, market status: not marketed). This is a known **data pipeline gap (DG001)** — Ceftriaxone is a well-established generic antibiotic with multiple FDA-approved products in the United States. The package insert and full prescribing information should be obtained directly from the FDA Orange Book or manufacturer labeling.

---

## Safety Considerations

Please refer to the package insert for complete safety information (full warnings and contraindications not available in current dataset — Data Gap DG001).

**Pharmacokinetic safety alert relevant to this prediction set:**
Ceftriaxone has approximately 95% plasma protein binding (predominantly albumin). This has direct implications for two other predictions in this analysis:
- **Congenital analbuminemia** (ranked 3rd by TxGNN): The near-complete absence of serum albumin would dramatically increase free Ceftriaxone concentrations, raising the risk of neurotoxicity and nephrotoxicity. This indication should be classified as a **pharmacokinetic contraindication** and removed from the repurposing candidates list.

---

## Full Prediction Landscape Summary

| Rank | Indication | TxGNN Score | Evidence | Recommendation | Notes |
|------|-----------|-------------|----------|---------------|-------|
| 1 | Polyclonal Hyperviscosity Syndrome | 99.39% | L5 | Hold | No mechanistic link; KG algorithmic artefact |
| 2 | Hyperamylasemia | 99.39% | L4 | Hold | 3 indirectly related case reports; no treatment mechanism |
| 3 | Congenital Analbuminemia | 99.37% | L5 | Hold | ⚠️ Safety concern — high free-drug toxicity risk |
| **4** | **Infectious Otitis Media** | **99.26%** | **L1** | **Proceed with Guardrails** | **Primary report focus** |
| 5 | Blood Group Incompatibility | 99.12% | L5 | Hold | No treatment mechanism; KG algorithmic artefact |
| 6 | Suppurative Otitis Media | 99.02% | L3 | Research Question | Biologically plausible; no direct clinical trials; limited by *P. aeruginosa* coverage gap |
| 7 | Chronic Otitis Media | 99.01% | L3 | Research Question | Similar to above; biofilm and coverage issues limit clinical utility |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ceftriaxone's use in infectious (acute) otitis media is supported by multiple prospective RCTs, cohort studies, and current treatment guidelines. This TxGNN prediction confirms an established clinical practice rather than uncovering a novel indication — making regulatory registration the primary remaining barrier rather than proof-of-concept. The evidence base is sufficient to advance, provided key safety documentation gaps are resolved first.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001:** Obtain the complete package insert (warnings, contraindications, drug interactions) from the FDA Orange Book or manufacturer — required before any safety review can be completed
- **Verify US market authorization:** Manually confirm current FDA approval status and approved indications for Ceftriaxone via the Orange Book; correct the data pipeline that is returning 0 records
- **Clarify NCT01511107 termination reason:** If terminated for safety reasons, this must be disclosed; if administrative, partial data may still be usable for evidence review
- **Scope the indication precisely:** Claims should be limited to **acute** infectious otitis media (AOM) caused by susceptible organisms — *S. pneumoniae*, *H. influenzae*, *M. catarrhalis*. Chronic and suppurative otitis media require separate evaluation due to *P. aeruginosa* coverage gaps and biofilm-related treatment challenges
- **Antimicrobial stewardship review:** Given rising concern about Ceftriaxone overuse in AOM (PMID 35841649, PMID 39361280), any formal indication expansion should include an antibiotic stewardship component addressing appropriate vs. inappropriate use criteria
- **Flag and deprioritize Congenital Analbuminemia (rank 3):** Reclassify as a pharmacokinetic safety contraindication rather than a repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

