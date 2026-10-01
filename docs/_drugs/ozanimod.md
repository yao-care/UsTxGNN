---
layout: default
title: Ozanimod
parent: Model Prediction Only (L5)
nav_order: 1006
evidence_level: L5
indication_count: 1
---

# Ozanimod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Ozanimod: From Relapsing Multiple Sclerosis to Progressive Relapsing Multiple Sclerosis

## One-Sentence Summary

Ozanimod (ZEPOSIA) is an oral S1P receptor modulator. Published literature reports its US approval for relapsing forms of multiple sclerosis (MS), but the license record supplied here has no indication text.
The TxGNN model predicts it may be effective for **progressive relapsing multiple sclerosis**, with **7 registered trials** and **18 publications** retrieved. Only 1 completed Phase 3 RCT was supplied, and it is in relapsing MS, not in a population defined as progressive relapsing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing forms of MS (from PMID 32385738; the license record's indication field is empty) |
| Predicted New Indication | Progressive relapsing multiple sclerosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L2 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Proceed with Guardrails |

**Evidence level note:** The Evidence Pack labels this L1. Under the grading rules, L1 needs at least 2 completed Phase 3 RCTs, and only 1 (NCT02576717) was supplied, so L2 is the strict grade. That trial is also in relapsing MS.

## Why is This Prediction Reasonable?

Ozanimod is a selective sphingosine-1-phosphate receptor 1 and 5 (S1P1/S1P5) modulator. It keeps lymphocytes in the lymph nodes, which reduces autoreactive lymphocyte infiltration into the central nervous system. This is the basis for its use in relapsing MS. The original MOA field in the record is empty, so this description comes from the literature rather than the supplied drug record.

"Progressive relapsing MS" is an obsolete phenotype label. It is now generally reclassified as primary or secondary progressive MS with activity. The mechanism is therefore plausible mainly for the inflammatory, relapse-driven component of the disease. Direct S1P5 effects on CNS cells are plausible, but they are unproven for neurodegeneration in non-active progression.

Because ozanimod is already labelled for relapsing forms of MS, this is not true repurposing. The prediction mostly reflects the overlap between the relapsing and progressive-with-activity MS phenotypes.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02576717](https://clinicaltrials.gov/study/NCT02576717) | Phase 3 | Completed | 2,494 | Randomized, double-blind, double-dummy, active-controlled study of ozanimod (RPC1063) in relapsing MS. It is the only randomized Phase 3 evidence supplied. The title is truncated, so check the population and arms against the registry. |
| [NCT06396039](https://clinicaltrials.gov/study/NCT06396039) | Phase 4 | Active, not recruiting | 84 | Single-arm, open-label study of ozanimod effectiveness and safety in Chinese adults with relapsing MS. No control arm and a small sample. |
| [NCT05605782](https://clinicaltrials.gov/study/NCT05605782) | N/A | Active, not recruiting | 9,000 | ORION post-authorisation, long-term, non-interventional safety study of ozanimod in RRMS. It compares adverse-event rates against other S1P modulators and DMTs. It provides no efficacy evidence. |
| [NCT05828901](https://clinicaltrials.gov/study/NCT05828901) | N/A | Recruiting | 60 | Observational study of disease activity and rebound risk in MS patients on S1P receptor modulators. Relevant to the class rebound concern, but not specific to ozanimod or progressive disease. |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS: early intensive versus escalation DMT strategies in RRMS. Concerns strategy; ozanimod is not shown to be a specific comparator. |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Active, not recruiting | 900 | Pragmatic trial of early aggressive versus escalation therapy in MS. Concerns strategy, so the link to ozanimod is indirect. |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | Enrolling by invitation | 323 | STATURE: observational study of oral DMT burden and adherence, with ozanimod among six drugs. Adherence focus, not efficacy or safety. |

NCT05688436 (pregnancy outcomes with diroximel fumarate, a different drug) was retrieved but is not relevant to ozanimod, so it is not listed.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | Network meta-analysis (Cochrane) | Cochrane Database Syst Rev | Compares immunomodulators and immunosuppressants in progressive MS. The abstract notes a lack of direct comparison trials. This is the most relevant source for the predicted indication. |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network meta-analysis (Cochrane) | Cochrane Database Syst Rev | Update on relative benefit of immunomodulators and immunosuppressants in RRMS. |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | Review | Neurology International | Comprehensive review of ozanimod in relapsing MS, covering disease, efficacy and side effects. |
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | Review | Drugs | Approval summary. The US FDA approved ozanimod in March 2020 for relapsing forms of MS: clinically isolated syndrome, relapsing-remitting disease and active secondary progressive disease. |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | Review | Expert Opin Pharmacother | Update on S1P receptor modulators (fingolimod, siponimod, ozanimod, ponesimod) in relapsing MS. |
| [33797705](https://pubmed.ncbi.nlm.nih.gov/33797705/) | 2021 | Review | CNS Drugs | Overview of the S1P receptor modulator class in MS. |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | Review | Ther Adv Neurol Disord | Latest therapeutic developments and future directions in progressive MS. |
| [38162670](https://pubmed.ncbi.nlm.nih.gov/38162670/) | 2023 | Review | Front Immunol | Reviews CNS-bioavailable DMTs. Notes that current DMTs have limited efficacy in progressive forms of MS. |
| [41919069](https://pubmed.ncbi.nlm.nih.gov/41919069/) | 2026 | Real-world registry study | Ther Adv Neurol Disord | MSBase comparison of anti-CD20 therapies and S1P receptor modulators in late-onset MS. |
| [37638037](https://pubmed.ncbi.nlm.nih.gov/37638037/) | 2023 | Preclinical | Front Immunol | A different S1PR-1/5 modulator (RP-101074) showed beneficial effects in a model of CNS degeneration. This is mechanistic support only, not ozanimod data. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209899 | ZEPOSIA (Celgene Corporation) | Capsule (oral) | Not listed in the supplied record |

## Safety Considerations

Please refer to the package insert for safety information. The record contains no warnings, contraindications or drug-interaction entries.

Two evidence-derived points are worth noting:
- Rebound risk after discontinuation of S1P receptor modulators is being studied (NCT05828901).
- Long-term real-world adverse-event monitoring of ozanimod is ongoing in the ORION study (NCT05605782).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ozanimod is already marketed in the US, has a completed Phase 3 RCT in relapsing MS, and has a plausible S1P1/S1P5 mechanism for the inflammatory component of MS. However, none of the supplied evidence directly shows benefit in a population defined as progressive relapsing MS, and this is not true repurposing because the relapsing-form indication is already labelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening).
- DrugBank MOA data to replace the literature-derived mechanism.
- Verification of the population, arms and results of NCT02576717 against the registry record.
- Clarification of the target phenotype (active secondary progressive, or primary progressive with activity) in place of the obsolete "progressive relapsing" label.
- Evidence of benefit in non-active progressive MS, or an explicit exclusion of that population.
- A second completed Phase 3 RCT, if an L1 grade is to be claimed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

