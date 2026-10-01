---
layout: default
title: Obinutuzumab
parent: Model Prediction Only (L5)
nav_order: 980
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Obinutuzumab: From an Unspecified Original Indication to Pregerminal Center CLL/SLL

## One-Sentence Summary

Obinutuzumab is a glycoengineered type II anti-CD20 antibody marketed in the US as Gazyva. The supplied data do not state its original indication.
The TxGNN model predicts it may be effective for **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL)**, but this pack contains **0 clinical trials and 0 publications** for that subtype, so the prediction rests on the model alone.
The pack does contain **50 trials and 20 publications** for a lower-ranked prediction, **follicular lymphoma**, which are summarized below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (the approved-indication text is empty) |
| Predicted New Indication | Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L5 (model prediction only). For the lower-ranked follicular lymphoma prediction, the pack assigns L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125486) |
| Recommended Decision | Hold (for the rank-1 CLL/SLL prediction). Follicular lymphoma is Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the pack. Based on its known drug class, obinutuzumab is a glycoengineered type II anti-CD20 antibody.
CLL/SLL cells express CD20, so a CD20-directed antibody has a biologically plausible link to this disease.
The high score (0.992) is consistent with that link.

Two caveats limit how far this prediction can be trusted:
- **This may not be true repurposing.** The original indications are missing, so the prediction may simply reflect an existing labeled CLL use. That cannot be confirmed from this pack.
- **The two CLL/SLL nodes are probably not independent signals.** The rank-2 node (CLL/SLL with IGHV somatic hypermutation) has an identical score of 0.992, which suggests the two are ontology siblings. CD20 targeting is not restricted to the IGHV-mutated subtype. Evidence for the broader CLL/SLL entity would have to be retrieved separately.

## Clinical Trial Evidence

Currently no related clinical trials registered for pregerminal center CLL/SLL.

## Literature Evidence

Currently no related literature available for pregerminal center CLL/SLL.

## Supporting Evidence: Follicular Lymphoma (Rank 3, Score 99.18%)

Follicular lymphoma is a CD20-positive B-cell malignancy. Obinutuzumab acts through enhanced direct cell death, antibody-dependent cellular cytotoxicity and phagocytosis. It has a lower complement-dependent cytotoxicity profile than the type I antibody rituximab.

**Clinical trials (10 of 50 shown)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Phase 2 | Completed | 96 | Obinutuzumab + lenalidomide in previously untreated FL |
| [NCT01582776](https://clinicaltrials.gov/study/NCT01582776) | Phase 1b/2 | Completed | 317 | GALEN: obinutuzumab + lenalidomide in relapsed/refractory FL and aggressive B-cell lymphomas |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Completed | 217 | Zanubrutinib + obinutuzumab vs obinutuzumab alone in relapsed/refractory FL |
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | Recruiting | 780 | Zanubrutinib + obinutuzumab vs lenalidomide + rituximab in relapsed/refractory FL or MZL, primary endpoint PFS |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Phase 3 | Recruiting | 190 | GAZEBO: radiotherapy alone vs radiotherapy + obinutuzumab in early-stage FL |
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Phase 3 | Recruiting | 1095 | EPCORE FL-2: epcoritamab + R2 vs chemoimmunotherapy in untreated FL. Obinutuzumab's role (comparator or backbone) is unverified |
| [NCT06961500](https://clinicaltrials.gov/study/NCT06961500) | Phase 2 | Not yet recruiting | 133 | Obinutuzumab + CHOP vs obinutuzumab + bendamustine in newly diagnosed grade 3A FL |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Completed | 114 | Safety of short-duration (90-minute) obinutuzumab infusion with chemotherapy in untreated advanced FL |
| [NCT04450173](https://clinicaltrials.gov/study/NCT04450173) | Phase 2 | Active, not recruiting | 40 | Obinutuzumab + ibrutinib + venetoclax in previously untreated FL (the FL cohort is not confirmed) |
| [NCT06108232](https://clinicaltrials.gov/study/NCT06108232) | Phase 2 | Active, not recruiting | 33 | Obinutuzumab + CC-99282 in untreated high tumor burden FL |

**Literature (10 of 20 shown)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | N Engl J Med | Obinutuzumab-based vs rituximab-based chemotherapy in previously untreated advanced FL (GALLIUM) |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | J Clin Oncol | GALLIUM: obinutuzumab prolonged PFS vs rituximab; report on the influence of chemotherapy backbone |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | J Clin Oncol | ROSEWOOD: randomized Phase 2 of zanubrutinib + obinutuzumab vs obinutuzumab alone in relapsed/refractory FL |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | Phase 3 final analysis | HemaSphere | Final GALLIUM results, obinutuzumab vs rituximab immunochemotherapy in FL/MZL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | Single-arm Phase 2 | Lancet Haematol | GALEN: activity and safety of lenalidomide + obinutuzumab in relapsed/refractory FL |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Rapid review | Front Pharmacol | Efficacy, safety and cost-effectiveness of obinutuzumab in FL |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood Lymphat Cancer | Impact of obinutuzumab alone and in combination for FL |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Target Oncol | Obinutuzumab in rituximab-refractory or -relapsed FL (GADOLIN) |
| [40355425](https://pubmed.ncbi.nlm.nih.gov/40355425/) | 2025 | Phase 2 | Blood Cancer J | Intermittent venetoclax + obinutuzumab + bendamustine in high-risk untreated FL (PrE0403) |
| [35359000](https://pubmed.ncbi.nlm.nih.gov/35359000/) | 2022 | Phase 1b/2 | Blood Adv | Atezolizumab + obinutuzumab + bendamustine in previously untreated FL |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125486 | Gazyva (Genentech, Inc.) | Injection, solution, concentrate | Not provided in the supplied data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted immunotherapy (anti-CD20 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold** (for the rank-1 CLL/SLL prediction)

**Rationale:**
The CLL/SLL prediction has no trials or publications in this pack, and the two CLL/SLL nodes appear to be a single signal. Original indications and mechanism of action are also missing. The follicular lymphoma prediction (rank 3) is much better supported and is graded **Proceed with Guardrails**. It has GALLIUM and ROSEWOOD RCT publications plus several completed and ongoing Phase 2/3 trials.

**To proceed, the following is needed:**
- Retrieve trials and literature for the broader CLL/SLL entity, not just the pregerminal center and IGHV-mutated subtype nodes
- Download and parse the US package insert (warnings, contraindications, approved indications) to confirm whether CLL and FL are already labeled uses
- Confirm the Phase 3 status of the GALLIUM publications from full text, since the classification currently rests on titles
- Confirm obinutuzumab's role in NCT06191744
- Fill in mechanism-of-action data from DrugBank (DB08935)
- Assess route compatibility, which is still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

