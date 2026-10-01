---
layout: default
title: Acetylcysteine
parent: Model Prediction Only (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
---

# Acetylcysteine
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

# Acetylcysteine: From Approved Mucolytic and Antidote Uses to Thrombotic Disease

## One-Sentence Summary

Acetylcysteine (N-acetylcysteine, NAC) is a marketed drug whose established uses, per the literature in this pack, include acetaminophen overdose, cystic fibrosis and COPD.
The TxGNN model predicts it may be effective for **thrombotic disease**, particularly thrombotic microangiopathies such as transplant-associated TMA (TA-TMA) and thrombotic thrombocytopenic purpura (TTP).
Support comes from **9 clinical trials** (only 1 completed Phase 3; no outcome data in this pack) and **20 publications**, including 1 randomized trial, 1 cohort study, 1 systematic review and several preclinical studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records supplied. Literature in the pack cites acetaminophen overdose, cystic fibrosis and COPD as well-established uses. |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 (one completed Phase 3 trial, but no outcome data provided) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five records shown are all ANDAs) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the DrugBank record. The mechanistic link below comes from the repurposing rationale and the supporting preclinical literature.

NAC can reduce disulfide bonds in ultra-large von Willebrand factor (VWF) multimers. This lowers VWF-platelet binding and microthrombus formation, which is the central lesion in TTP. A 2011 study (PMID 21266777) reported that NAC reduces VWF size and activity in human plasma and in mice. A 2017 study (PMID 28011677) tested NAC in mouse and baboon TTP models.

NAC is also a glutathione precursor and antioxidant. This may limit endothelial injury in thrombotic microangiopathies such as TA-TMA, where endothelial damage drives the disease. It also explains why trials have focused on stem cell transplant patients.

The predicted indication is broad, and the evidence is concentrated in thrombotic microangiopathies (TA-TMA, TTP) rather than thrombosis in general. Data on venous or arterial thrombosis are limited to a diabetes model showing reduced platelet activation and cerebral vessel thrombosis (PMID 28961512) and one Phase 2 trial in renal insufficiency (NCT03636932).

---

## Clinical Trial Evidence

No trial results were included in the pack, so efficacy cannot be confirmed from it. The list is ordered by relevance grade.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Completed | 170 | NAC in transplant-associated TMA. The most direct trial, but no outcome data provided. |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Phase 3 | Unknown | 260 | NAC to prevent thrombotic events after allogeneic HSCT. No results available. |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Active, not recruiting | 44 | Single-arm multicenter trial of NAC for TA-TMA, a setting where plasma exchange response is under 10% and complement inhibitors are costly. |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | Completed | 3 | IV NAC pilot in suspected TTP patients on plasma exchange. Hypothesis-generating only. |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Completed | 40 | Randomized, double-blind, placebo-controlled crossover trial of NAC against the thrombotic phenotype in chronic kidney disease. Related to thrombosis but not the same disease. |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Unknown | 44 | High-dose dexamethasone plus NAC in newly diagnosed immune thrombocytopenia (a platelet disorder, not thrombosis). |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Unknown | 200 | Atorvastatin, NAC and danazol in steroid-resistant or relapsed ITP. Not thrombotic disease. |
| [NCT06518044](https://clinicaltrials.gov/study/NCT06518044) | Phase 2 | Not yet recruiting | 30 | NAC for hematopoietic recovery in severe aplastic anemia after haploidentical transplant. Not thrombosis. |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | Completed | 15 | Atorvastatin plus NAC on platelet count in steroid-resistant or relapsed ITP. Indirect relevance. |

---

## Literature Evidence

Abstracts in the pack are truncated, so only findings visible in them are summarized.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | RCT | Transplantation and Cellular Therapy | Randomized, placebo-controlled, open-label trial of NAC as prophylaxis for TA-TMA in HSCT patients. Outcome data not shown in the excerpt. |
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Systematic review | Journal of Clinical Medicine | Systematic review and critical appraisal of NAC in TTP. Findings not shown in the excerpt. |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Cohort | Annals of Hematology | Retrospective cohort assessing NAC and in-hospital mortality in acquired TTP. The abstract notes NAC use in aTTP is still controversial. |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Review | Expert Review of Hematology | Summarizes repurposed drugs for immune TTP, including NAC alongside rituximab, bortezomib and caplacizumab. |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | Journal of Clinical Medicine | TTP pathophysiology, diagnosis and management. |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclinical | Blood | NAC tested in mouse and baboon TTP models. |
| [21266777](https://pubmed.ncbi.nlm.nih.gov/21266777/) | 2011 | Preclinical | J Clin Invest | NAC reduces the size and activity of VWF in human plasma and mice. |
| [28961512](https://pubmed.ncbi.nlm.nih.gov/28961512/) | 2018 | Preclinical | Redox Biology | NAC attenuated systemic platelet activation and cerebral vessel thrombosis in diabetes. |
| [30871975](https://pubmed.ncbi.nlm.nih.gov/30871975/) | 2019 | Mechanistic study | Biol Blood Marrow Transplant | Circulating heme oxygenase-1 and complement activation in TA-TMA (background pathogenesis). |
| [39737637](https://pubmed.ncbi.nlm.nih.gov/39737637/) | 2025 | Case report | J Pediatr Hematol Oncol | Plasma exchange plus NAC in congenital TTP presenting with acute renal failure. |

---

## US Market Information

Four distinct authorizations are shown (ANDA219194 appears twice in the source data). Approved-indication text is not provided in the records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA072489 (American Regent, Inc.) | Acetylcysteine | Inhalant | Not provided |
| ANDA219194 (Somerset Therapeutics, LLC) | Acetylcysteine | Solution | Not provided |
| ANDA207358 (Eugia US LLC) | Acetylcysteine | Injection, solution | Not provided |
| ANDA213693 (Glenmark Pharmaceuticals Inc., USA) | Acetylcysteine | Injection, solution | Not provided |

Both injectable and non-injectable forms are on the market. The thrombotic microangiopathy trials involve systemic administration, so the injectable and oral routes are the relevant ones.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is a plausible mechanism (VWF disulfide reduction, antioxidant effect), preclinical support in TTP models, and one completed Phase 3 trial plus a published randomized trial in TA-TMA. The pack, however, contains no efficacy outcomes from the clinical trials. Proceeding should be limited to thrombotic microangiopathies (TA-TMA and TTP) as a research question, not general thrombotic disease, and safety review is blocked until package insert data are obtained.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Outcome results from NCT03252925 and the 2022 RCT (PMID 35940529), plus the pending results of NCT05907486
- Review of the systematic review (PMID 41977015) and the aTTP cohort (PMID 37311880) for the efficacy signal and the reported controversy
- Route and formulation compatibility assessment for the intended systemic use in transplant patients

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

