---
layout: default
title: Collagenase Clostridium Histolyticum
parent: Model Prediction Only (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
monitor_inn: "COLLAGENASE CLOSTRIDIUM HISTOLYTICUM"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "Ledderhose disease", "infantile digital fibromatosis", "palmar fibromatosis", "hemorrhagic disorder due to a constitutional thrombocytopenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "posterior leukoencephalopathy syndrome"]
last_modified_at: 2026-10-28
description: "Collagenase Clostridium Histolyticum: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Peyronie disease, penile fibromatosis, balanitis xerotica oblit…"
---

# Collagenase Clostridium Histolyticum
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Collagenase Clostridium Histolyticum: From Peyronie Disease to primary release disorder of platelets
{: .text-alpha }

## One-Sentence Summary

Collagenase Clostridium histolyticum is an enzyme originally used to treat Peyronie disease and related penile fibrotic conditions.
The TxGNN model predicts it may be effective for **palmar fibromatosis (Dupuytren's disease)**,
with **13 clinical trials** and **20 publications** currently supporting this direction. This is closer to confirmation of a known use than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peyronie disease, penile fibromatosis, balanitis xerotica obliterans |
| Predicted New Indication | Primary release disorder of platelets (rank 1 by score); the best-supported prediction is palmar fibromatosis (rank 6) |
| TxGNN Prediction Score | 1.0000 (rank 1, primary release disorder of platelets); 0.9995 (palmar fibromatosis) |
| Evidence Level | L5 (palmar fibromatosis); L5 for the top-ranked platelet disorders |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails (palmar fibromatosis only); Hold for the other predictions |

The top-ranked predictions (platelet function and bleeding disorders) have no clinical or literature support and no plausible mechanism. This report therefore focuses on **palmar fibromatosis**, the only prediction with substantial evidence. Ledderhose disease (plantar fibromatosis) is a secondary research question supported only by case reports.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, collagenase Clostridium histolyticum is a mixture of microbial collagenases that break down collagen types I and III. Its efficacy in collagen-rich fibrotic plaques (Peyronie disease) has been established, and mechanistically it is applicable to other collagen-driven fibrotic conditions.

Dupuytren's disease is a fibroproliferative disorder of the palmar fascia. Collagen-rich cords form and cause fixed finger contracture. Injecting the enzyme directly into the cord lyses the collagen, which is the same mechanism as in Peyronie plaques. Both are localized connective-tissue fibroses, and Dupuytren's contracture is a recognized risk factor for Peyronie disease.

The evidence pack notes that this use (Xiaflex/Xiapex for Dupuytren's contracture with a palpable cord) has already been approved, so the result validates a known use rather than revealing a new one.

By contrast, the highest-scoring predictions (primary release disorder of platelets, Glanzmann thrombasthenia, pseudo-von Willebrand disease, and others) are platelet or bleeding disorders. They have no plausible mechanistic link. The high scores likely reflect network proximity through collagen-platelet interactions, and collagenase could plausibly worsen bleeding. They should be treated as TxGNN model (deep learning) artifacts.

## Clinical Trial Evidence

Trials for palmar fibromatosis (Dupuytren's disease):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00528606](https://clinicaltrials.gov/study/NCT00528606) | Phase 3 | Completed | 308 | Double-blind, randomized, placebo-controlled pivotal study of AA4500 0.58 mg vs placebo (2:1) in Dupuytren's contracture |
| [NCT01674634](https://clinicaltrials.gov/study/NCT01674634) | Phase 3b | Completed | 715 | Open-label, historically controlled study of two concurrent injections; large safety dataset (tendon rupture, anaphylaxis) |
| [NCT00260429](https://clinicaltrials.gov/study/NCT00260429) | Phase 3 | Completed | 38 | Double-blind, placebo-controlled study in residual-type Dupuytren's disease |
| [NCT01407068](https://clinicaltrials.gov/study/NCT01407068) | Phase 3 | Completed | 60 | Open-label study of two concurrent injections into the same hand |
| [NCT01588353](https://clinicaltrials.gov/study/NCT01588353) | Phase 3 | Completed | 104 | Efficacy, safety, and plasma concentration of AK160 in Dupuytren's contracture |
| [NCT04874870](https://clinicaltrials.gov/study/NCT04874870) | Phase 3 | Completed | 80 | Splinting after collagenase injection (post-treatment management) |
| [NCT02725528](https://clinicaltrials.gov/study/NCT02725528) | Phase 3 | Completed | 22 | Randomized comparison of clinical and cost-effectiveness of collagenase vs limited palmar fasciectomy (small sample) |
| [NCT03000114](https://clinicaltrials.gov/study/NCT03000114) | Phase 4 | Unknown | 334 | Collagenase injection vs percutaneous needle aponeurotomy |
| [NCT03192020](https://clinicaltrials.gov/study/NCT03192020) | Phase 4 | Active, not recruiting | 302 | DETECT: needle fasciotomy vs surgery vs collagenase; completion expected 2031 |
| [NCT01498640](https://clinicaltrials.gov/study/NCT01498640) | Phase 4 | Completed | 52 | Retreatment of recurrent contractures previously treated with AA4500 |

No clinical trials are registered for the other nine predicted indications.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28854973](https://pubmed.ncbi.nlm.nih.gov/28854973/) | 2017 | RCT | BMC Musculoskelet Disord | Safety and efficacy of collagenase injection for palmar Dupuytren nodules |
| [26524616](https://pubmed.ncbi.nlm.nih.gov/26524616/) | 2015 | Systematic review | Health Technol Assess | Systematic review and economic evaluation of collagenase for Dupuytren's contracture |
| [27151958](https://pubmed.ncbi.nlm.nih.gov/27151958/) | 2016 | Systematic review | Br Med Bull | Enzymatic fasciectomy described as non-invasive, safe, and fast |
| [40003669](https://pubmed.ncbi.nlm.nih.gov/40003669/) | 2025 | Meta-analysis | Life (Basel) | Collagenase vs percutaneous needle fasciotomy: complications, satisfaction, outcomes, recurrence |
| [37665353](https://pubmed.ncbi.nlm.nih.gov/37665353/) | 2024 | Meta-analysis | Arch Orthop Trauma Surg | Collagenase injection vs limited fasciectomy in comparative studies |
| [32484064](https://pubmed.ncbi.nlm.nih.gov/32484064/) | 2020 | Meta-analysis | J Orthop Surg (Hong Kong) | Efficacy and limitations of fasciectomy vs collagenase; recurrence and complications |
| [24698851](https://pubmed.ncbi.nlm.nih.gov/24698851/) | 2015 | Safety study | J Hand Surg Eur | 11 trials (N=1082): adverse events numerically lower with collagenase than with fasciectomy |
| [24397625](https://pubmed.ncbi.nlm.nih.gov/24397625/) | 2014 | Pooled trial analysis | Curr Med Res Opin | Efficacy and safety in moderate Dupuytren's contracture, from the CORD I and II pivotal trials |
| [36928340](https://pubmed.ncbi.nlm.nih.gov/36928340/) | 2023 | Cohort | Mil Med | Recurrence and subsequent treatment after collagenase in a veteran population |
| [26491251](https://pubmed.ncbi.nlm.nih.gov/26491251/) | 2015 | Review | Biologics | Role of collagenase in Peyronie's disease (original indication) |

For Ledderhose disease (plantar fibromatosis), only three small reports exist: [25158740](https://pubmed.ncbi.nlm.nih.gov/25158740/) (2014), [31679681](https://pubmed.ncbi.nlm.nih.gov/31679681/) (2019), and [37869482](https://pubmed.ncbi.nlm.nih.gov/37869482/) (2023), all case reports or case studies.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA101995 | COLLAGENASE SANTYL (Smith & Nephew) | Ointment | Not stated; status valid |

The only US record in the data compiled for this report is cancelled. It is a topical ointment, not the injectable form used for Dupuytren's contracture, so regulatory and supply status of the injectable product should be verified separately.

## Safety Considerations

- **Drug Interactions**: 49 interactions were identified; the 20 listed in the data are all Moderate level. Main groups:
  - Tetracycline antibiotics: doxycycline, minocycline, tetracycline
  - Antiplatelet agents: acetylsalicylic acid, clopidogrel, cilostazol, cangrelor, abciximab
  - Anticoagulants: apixaban, betrixaban, fondaparinux, dalteparin, danaparoid, argatroban, bivalirudin, antithrombin III
  - Thrombolytics and related agents: alteplase, anistreplase, caplacizumab, defibrotide
- The bleeding-related interactions are particularly relevant for the platelet and bleeding disorders predicted by the model, and further argue against those uses.
- Published safety data for Dupuytren's contracture report fewer adverse events than fasciectomy (nerve injury, neurapraxia, complex regional pain syndrome). The pivotal programs specifically tracked tendon rupture/ligament injury and anaphylaxis.
- Pediatric safety is an additional concern for infantile digital fibromatosis.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (palmar fibromatosis only). **Hold** for the platelet, bleeding, and other predictions.

**Rationale:**
Palmar fibromatosis is supported by multiple completed Phase 3 trials, including a large placebo-controlled pivotal study, and by systematic reviews and meta-analyses. It is nonetheless a previously approved use rather than a new discovery. The nine remaining predictions have no clinical evidence, and the platelet and bleeding disorders have no plausible mechanism and a potential bleeding risk.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Verification of the regulatory and supply status of the injectable product in the US, since the only record listed is a cancelled ointment
- Monitoring plan for tendon rupture, ligament injury, and anaphylaxis
- For Ledderhose disease: controlled studies beyond the existing case reports, as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

