---
layout: default
title: Palbociclib
parent: Model Prediction Only (L5)
nav_order: 1008
evidence_level: L5
indication_count: 4
monitor_inn: "PALBOCICLIB"
predicted_indications: ["hyperthyroidism", "rheumatoid arthritis", "thrombotic disease", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta"]
last_modified_at: 2026-10-14
description: "Palbociclib: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available in the compiled data"
---

# Palbociclib
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

# Palbociclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Palbociclib is a CDK4/6 inhibitor used in HR-positive, HER2-negative breast cancer. Its labeled indication is not captured in the data compiled for this report. The TxGNN model predicts several new indications, and the best-supported one is **Rheumatoid Arthritis**, which has **0 clinical trials** and **4 publications** (one case report, one observational study, two preclinical studies). The top-ranked prediction by score, hyperthyroidism, has no supporting evidence at all.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the FDA license records have empty indication text) |
| Predicted New Indication | Rheumatoid arthritis (best-supported of the top 4 predictions; the top-scoring prediction, hyperthyroidism, has no evidence) |
| TxGNN Prediction Score | 99.36% (rheumatoid arthritis); hyperthyroidism 99.44% |
| Evidence Level | L4 (rheumatoid arthritis) |
| US Market Status | Cancelled only |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

**Note on the other predictions:** hyperthyroidism (99.44%), thrombotic disease (99.32%), and resistance to thyroid hormone due to a THRB mutation (99.30%) are all rated Hold. Thrombotic disease is a safety concern, not a therapeutic opportunity (see below).

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general knowledge, palbociclib is a CDK4/6 inhibitor that blocks G1-to-S cell cycle progression and so suppresses cell proliferation.

For rheumatoid arthritis, the link is plausible but indirect. Synovial fibroblasts proliferate abnormally in the RA joint, and preclinical work suggests CDK inhibition can reduce this:
- Cell cycle inhibition of synovial fibroblasts with CDK inhibitors ameliorated disease in animal models of RA without weakening acquired immunity (PMID 25165034).
- Synovial hyperplasia in arthritic mice and TNF-α-driven synovial fibroblast proliferation depend on CDK6 (PMID 39940918).
- A case report describes improvement of RA in a breast cancer patient treated with palbociclib (PMID 33587021).

This evidence is preclinical or anecdotal. No registered trial tests palbociclib in RA.

For the other predictions, the data does not support a mechanistic link:
- **Hyperthyroidism** and **thyroid hormone resistance (THRB mutation)**: no trials or publications. The high scores are knowledge-graph predictions only, and a link would be speculative.
- **Thrombotic disease**: the literature shows a safety signal. Pharmacovigilance studies report thromboembolism associated with CDK4/6 inhibitors, so treating thrombosis with palbociclib is not supported and may be harmful.

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis or for any of the other top predicted indications.

## Literature Evidence

**Rheumatoid arthritis**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case report | Modern Rheumatology Case Reports | A breast cancer patient with pre-existing RA, previously treated with methotrexate, showed RA improvement while on palbociclib |
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Observational cohort | The Oncologist | Examines pre-existing and emerging immune-mediated diseases in HR+/HER2- breast cancer patients on CDK4/6 inhibitors plus endocrine therapy; the abstract available is too brief to state its findings |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclinical (animal) | Annals of the Rheumatic Diseases | CDK inhibition of synovial fibroblasts, combined with cytokine blockade, enhanced antiarthritic effects without increasing immune suppression |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclinical | International Journal of Molecular Sciences | Synovial hyperplasia in arthritic mice and TNF-α-induced synovial fibroblast proliferation are CDK6-dependent and CDK4-independent; palbociclib has been explored in RA |

**Thrombotic disease** (safety-related literature, not evidence of benefit)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36794339](https://pubmed.ncbi.nlm.nih.gov/36794339/) | 2023 | Pharmacovigilance and systematic review | Expert Opinion on Drug Safety | Examines the association between CDK4/6 inhibitors and thrombosis |
| [39123221](https://pubmed.ncbi.nlm.nih.gov/39123221/) | 2024 | Pharmacovigilance (FAERS) | BMC Pharmacology & Toxicology | Compares adverse event profiles of palbociclib, abemaciclib, and ribociclib |
| [39083396](https://pubmed.ncbi.nlm.nih.gov/39083396/) | 2025 | Pharmacovigilance (FAERS) | Expert Opinion on Drug Safety | Disproportionality analysis of CDK4/6 inhibitor adverse events |
| [35300061](https://pubmed.ncbi.nlm.nih.gov/35300061/) | 2022 | Observational cohort | Cancer Management and Research | Real-world thromboembolic events with ribociclib in metastatic breast cancer |

Several other retrieved papers on thrombosis are tangential or unrelated and are not listed.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212436 | Ibrance (Pfizer) | Film-coated tablet | Not available; status: cancelled |
| NDA207103 | Ibrance (Pfizer) | Capsule | Not available; status: cancelled |

Both listed NDAs are marked as cancelled, so no currently valid US authorization appears in the compiled data.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. Preclinical work reports palbociclib-induced myelosuppression (PMID 39940918), and bone marrow suppression is a recognized common adverse event of the class (PMID 37994878) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count is the key parameter; otherwise refer to the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Label warnings and contraindications were not available in the compiled data, so please refer to the package insert for them.

Safety signals from the literature:
- **Thromboembolism**: reported with CDK4/6 inhibitors in pharmacovigilance and real-world studies.
- **Interstitial lung disease / pulmonary toxicity**: described as less common but potentially severe class adverse events (PMIDs 37994878, 39894782).
- **Bone marrow suppression and gastrointestinal toxicity**: common class adverse events (PMID 37994878).

**Drug interactions:** 100 interactions were recorded in total, and the first 20 were provided. Major-level interactions in that set:
- Clarithromycin
- Cobicistat
- Deferiprone
- Samarium (153Sm) lexidronam

Moderate-level interactions include aprepitant, dexamethasone, cimetidine, saxagliptin, simvastatin, cilostazol, and several azole antifungals (miconazole, clotrimazole). Prucalopride is Minor. The full list should be reviewed before any clinical use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All four predictions rest mainly on knowledge-graph scores. Rheumatoid arthritis has the most support (L4: preclinical studies, one case report, one observational study) but no registered trial. Hyperthyroidism and thyroid hormone resistance have no evidence, and thrombotic disease points to a safety risk. Both US NDAs are cancelled, and label safety data is missing.
- Rheumatoid arthritis can be treated as a research question to pursue, not a candidate ready to advance.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- The original approved indication text
- For rheumatoid arthritis: review of the full findings of PMID 40504547, and a case for a controlled study that weighs the myelosuppression and thromboembolism risks of palbociclib against existing RA therapies
- Clarification of why the US NDAs are cancelled and of the current regulatory status of the product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

