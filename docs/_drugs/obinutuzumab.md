---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 980
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Obinutuzumab: From CD20+ B-Cell Malignancies (Not Yet Marketed in Taiwan) to Follicular Lymphoma

## One-Sentence Summary

> Obinutuzumab is a glycoengineered type II anti-CD20 monoclonal antibody with no marketing authorization currently on file in Taiwan (0 licenses).
> The TxGNN model's strongest-evidence signal points to **Follicular Lymphoma**, a globally established anti-CD20 antibody indication,
> with **46 clinical trials** and **20 publications** in this evidence pack — including two completed Phase 3 RCTs (GALLIUM, GADOLIN) — supporting the mechanism.
> Two additional model outputs (pregerminal-center CLL/SLL and IGHV-hypermutated CLL/SLL) scored equally high but returned **zero matched trials or literature**, likely reflecting disease-label granularity rather than a new signal — see note below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not currently marketed in Taiwan; drug class is targeted at CD20+ B-cell malignancies (chronic lymphocytic leukemia/small lymphocytic lymphoma) per the model's own rationale text |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.18% (rank 3 candidate; see note on two higher-listed but evidence-free candidates below) |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on the top-ranked candidates:** The two highest-ranked predictions (score ≈99.2%) — "pregerminal center CLL/SLL" and "CLL/SLL with IGHV somatic hypermutation" — returned **no matched clinical trials or literature** in this evidence pack. The model's own rationale flags this as a probable disease-term matching artifact: these are molecular subtypes of CLL/SLL, not distinct disease entities, and CLL/SLL as a whole already has a large body of approved-drug evidence (e.g., CLL14, iLLUMINATE) that simply isn't indexed under these precise subtype labels. They are classified L4/"Research Question" and are not decision-ready. This report therefore focuses on the third-ranked, evidence-rich candidate — **Follicular Lymphoma** — which is the only one of the three reaching a Guardrails-level recommendation.

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data is flagged as a gap in this evidence pack (DG002). Based on the information available in the model's rationale, however, obinutuzumab is a type II, glycoengineered, humanized anti-CD20 IgG1 monoclonal antibody. Compared with first-generation anti-CD20 agents such as rituximab, it produces stronger antibody-dependent cellular cytotoxicity (ADCC) and greater direct/non-apoptotic cell death, while inducing less complement-dependent cytotoxicity.

CD20 is expressed on malignant B-cells across the indolent and aggressive non-Hodgkin lymphoma spectrum, including both CLL/SLL and follicular lymphoma. The mechanistic rationale is therefore not a stretch: obinutuzumab already carries international marketing approval for follicular lymphoma (approved by FDA in 2016 as Gazyva, based on the GALLIUM and GADOLIN trials), so this "prediction" is best understood as the model correctly re-identifying an already-validated pharmacological pathway rather than proposing a novel hypothesis. Its practical relevance for this evidence pack is that Taiwan currently has **zero** marketing authorizations on file for this drug — so the decision in front of stakeholders is a market-entry/registration question, not a scientific-plausibility question.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Phase 3 | Recruiting | 1095 | Epcoritamab + rituximab/lenalidomide vs. chemoimmunotherapy in previously untreated FL |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Phase 2 | Completed | 96 | Obinutuzumab + lenalidomide in previously untreated FL |
| [NCT01582776](https://clinicaltrials.gov/study/NCT01582776) | Phase 1/2 | Completed | 317 | Obinutuzumab + lenalidomide across untreated and R/R FL cohorts |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Completed | 217 | Zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in R/R FL |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Completed | 114 | Post-marketing study of obinutuzumab short-duration infusion in untreated advanced FL |
| [NCT03492775](https://clinicaltrials.gov/study/NCT03492775) | Phase 2 | Completed | 46 | Obinutuzumab monotherapy vs. obinutuzumab + bendamustine in compromised/elderly patients |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Phase 3 | Recruiting | 190 | GAZEBO trial: radiotherapy alone vs. + obinutuzumab in early-stage FL |
| [NCT04450173](https://clinicaltrials.gov/study/NCT04450173) | Phase 2 | Active, not recruiting | 40 | Obinutuzumab + ibrutinib + venetoclax in untreated FL |
| [NCT06108232](https://clinicaltrials.gov/study/NCT06108232) | Phase 2 | Active, not recruiting | 33 | Obinutuzumab + CC-99282 in high tumor burden, untreated FL |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | N/A | Recruiting | 332 | Real-world efficacy/safety of obinutuzumab-based therapy in untreated FL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | N Engl J Med | GALLIUM primary analysis: obinutuzumab-chemo vs. rituximab-chemo in untreated advanced FL |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | J Clin Oncol | GALLIUM: influence of chemotherapy backbone on obinutuzumab efficacy/safety |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | J Clin Oncol | ROSEWOOD: zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in R/R FL |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM final analysis: obinutuzumab- vs. rituximab-based immunochemotherapy in untreated iNHL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | Lancet Haematol | GALEN: obinutuzumab + lenalidomide in R/R follicular B-cell lymphoma |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Targeted Oncol | Review incl. pivotal GADOLIN Phase 3 data (obinutuzumab + bendamustine in rituximab-refractory FL) |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | Cohort | Haematologica | Phase Ib/II: polatuzumab vedotin + bendamustine/obinutuzumab or rituximab in R/R FL |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood Lymphat Cancer | Overview of obinutuzumab alone and in combination for FL |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turk J Haematol | Comprehensive review of FL management incl. anti-CD20 antibody options |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review | Front Pharmacol | Rapid review of efficacy, safety, and cost-effectiveness of obinutuzumab in FL |

---

## Taiwan Market Information

No marketing authorizations are on file. `taiwan_regulatory.total_licenses = 0` and the licenses array is empty — obinutuzumab currently has no registered product in this jurisdiction.

---

## Cytotoxicity

Obinutuzumab is an antineoplastic agent (indicated for B-cell lymphoid malignancies); this section is included per that classification.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted immunotherapy — type II, glycoengineered anti-CD20 monoclonal antibody (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as gaps in this evidence pack; TFDA label retrieval is listed as a blocking data gap — DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Follicular Lymphoma)

**Rationale:**
- Two completed Phase 3 RCTs (GALLIUM, GADOLIN) plus 46 supporting trials and 20 publications establish obinutuzumab's efficacy in FL as an internationally validated, not merely hypothetical, indication — this is an L1-level evidence base.
- The drug has zero Taiwan marketing authorizations, so the practical decision is one of local registration/market entry rather than novel mechanism validation.
- The two higher-scoring CLL/SLL subtype predictions remain at "Research Question" (L4/S1) status and should not be advanced without first cross-checking against the existing CLL/SLL evidence base under standard (non-subtype) disease terms.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications data (DG001 — currently blocking full safety review)
- Formal DrugBank MOA record (DG002)
- Confirmation of Taiwan NDA/registration pathway status for obinutuzumab
- Re-run evidence retrieval for CLL/SLL under standard disease terminology to resolve the rank 1/2 label-matching gap before treating them as independent candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

