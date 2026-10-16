---
layout: default
title: Andexanet Alfa
parent: Model Prediction Only (L5)
nav_order: 349
evidence_level: L5
indication_count: 4
monitor_inn: "ANDEXANET ALFA"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "hemophilia"]
---

# Andexanet Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Andexanet Alfa: From FXa-Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

Andexanet alfa is a recombinant factor Xa decoy protein used to reverse the effect of factor Xa inhibitor anticoagulants during life-threatening bleeding. The TxGNN model predicts it may be effective for **Glanzmann thrombasthenia**, but **no clinical trials and no supporting publications** exist for this prediction. The high score appears to be a knowledge-graph artifact rather than a biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the US license record has no indication text) |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single license, BLA125586, is cancelled) |
| Number of NDAs | 1 (a BLA, cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in the compiled record. From the product's known profile, andexanet alfa is a catalytically inactive factor Xa decoy that binds and sequesters factor Xa inhibitors. It also binds TFPI and antithrombin-heparin complexes. Its role is to reverse anticoagulation, not to correct an intrinsic bleeding disorder.

Glanzmann thrombasthenia is an inherited platelet disorder caused by a defect in integrin αIIbβ3 (GPIIb/IIIa), which impairs platelet aggregation. A factor Xa-inhibitor reversal agent does not act on this defect, so **no plausible mechanistic link** is apparent. The very high TxGNN score (0.998) most likely reflects the drug's proximity to other "bleeding/coagulation disorder" nodes in the knowledge graph rather than a true biological relationship.

The other top predictions show the same pattern:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 1 | Glanzmann thrombasthenia | 99.77% | No mechanistic link; platelet aggregation defect |
| 2 | Primary release disorder of platelets | 99.76% | No effect on platelet granule secretion; added thrombotic risk |
| 3 | Pseudo-von Willebrand disease | 99.65% | Does not act on the GPIbα-VWF axis |
| 4 | Hemophilia | 99.10% | FVIII/FIX deficiency is not an FXa-inhibitor effect |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for Glanzmann thrombasthenia. The only predicted indication with publications is hemophilia (rank 4). Those publications are shown below for completeness. None of them evaluates andexanet alfa as a treatment for hemophilia. They concern anticoagulant reversal or laboratory testing. Classification is based on titles and partial abstracts and should be verified against the full text.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38620086](https://pubmed.ncbi.nlm.nih.gov/38620086/) | 2024 | Cohort/Observational | Circulation | ANNEXA-4 subanalysis of andexanet alfa in acute GI bleeding on FXa inhibitors (not hemophilia) |
| [33742436](https://pubmed.ncbi.nlm.nih.gov/33742436/) | 2021 | Guideline | Thromb Haemost | ICSH recommendations for laboratory measurement of direct oral anticoagulants |
| [31962376](https://pubmed.ncbi.nlm.nih.gov/31962376/) | 2020 | Laboratory study | Haemophilia | Andexanet alfa or DOAC Stop used to neutralize rivaroxaban interference in FVIII/FIX assays |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Review | Curr Pharm Des | New hemostatic agents and antidotes in perioperative care |
| [30309890](https://pubmed.ncbi.nlm.nih.gov/30309890/) | 2018 | Review | Blood | Reversing anti-FXa agents and unmet needs in trauma patients |
| [26519420](https://pubmed.ncbi.nlm.nih.gov/26519420/) | 2016 | Review | Drug Saf | Reversal strategies for NOACs |
| [27254626](https://pubmed.ncbi.nlm.nih.gov/27254626/) | 2016 | Review | Dtsch Med Wochenschr | Coagulation disorders in the ICU, including NOAC antidotes |
| [36819179](https://pubmed.ncbi.nlm.nih.gov/36819179/) | 2023 | Review/Protocol survey | EJHaem | Review of UK hospital protocols for andexanet alfa |
| [42033142](https://pubmed.ncbi.nlm.nih.gov/42033142/) | 2026 | Position statement | Br J Haematol | British Society for Haematology position statement on andexanet alfa use |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125586 (cancelled) | ANDEXXA | Injection, powder, lyophilized, for solution | Not listed in the compiled record |

## Safety Considerations

- **Thromboembolic risk**: The approved product carries a boxed warning for thromboembolic events, ischemic events, cardiac arrest and sudden death. Using it in patients with bleeding or platelet disorders, with no mechanistic rationale, would add risk without benefit.
- **Drug Interactions**: No interaction records were found.

Detailed warnings and contraindications from the package insert were not available in the compiled data. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5). There are no clinical trials or relevant literature, and there is no plausible mechanism linking a factor Xa-inhibitor reversal agent to platelet function disorders. The product's license is also cancelled in the US, and it carries a boxed thrombotic warning.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- A credible biological rationale linking the drug to the predicted indication, followed by preclinical evidence
- Clarification of the original approved indication and current regulatory status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

