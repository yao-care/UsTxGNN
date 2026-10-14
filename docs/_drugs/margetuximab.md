---
layout: default
title: Margetuximab
parent: Model Prediction Only (L5)
nav_order: 888
evidence_level: L5
indication_count: 2
---

# Margetuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Margetuximab: From HER2-Positive Metastatic Breast Cancer to HER2-Positive Breast Carcinoma (Top Prediction: Drug-Induced Osteoporosis)

## One-Sentence Summary

Margetuximab is an Fc-engineered anti-HER2 monoclonal antibody used with chemotherapy for pretreated HER2-positive metastatic breast cancer.
The TxGNN model's highest-ranked prediction is **drug-induced osteoporosis** (no supporting trials or publications, likely a knowledge-graph artifact). The second-ranked prediction, **HER2 positive breast carcinoma**, is supported by **7 clinical trials** and **20 publications**, but it is essentially the drug's already-approved use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data compiled for this report (literature indicates HER2-positive metastatic breast cancer) |
| Predicted New Indication | Drug-induced osteoporosis (rank 1); HER2 positive breast carcinoma (rank 2, evaluated in detail below) |
| TxGNN Prediction Score | Drug-induced osteoporosis: 99.29%; HER2 positive breast carcinoma: 99.05% |
| Evidence Level | Drug-induced osteoporosis: L5; HER2 positive breast carcinoma: L1 |
| US Market Status | Cancelled only (to be verified, see below) |
| Number of NDAs | 1 (BLA761150) |
| Recommended Decision | Drug-induced osteoporosis: Hold; HER2 positive breast carcinoma: Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

**Drug-induced osteoporosis (rank 1).** The score is very high, but no clinical trials or publications support it. Margetuximab targets HER2 and enhances immune-cell killing of tumour cells. No plausible biological pathway links HER2 targeting to preventing or treating drug-induced bone loss. The prediction is most likely a knowledge-graph artifact driven by network proximity rather than a real mechanism. Detailed mechanism of action data is also unavailable, which limits further verification.

**HER2 positive breast carcinoma (rank 2).** Margetuximab binds the extracellular domain of HER2, as trastuzumab does. Its engineered Fc region binds the activating receptor CD16A (FcγRIIIa) more strongly and the inhibitory receptor CD32B more weakly. This enhances NK-cell-mediated antibody-dependent cellular cytotoxicity (ADCC) against HER2-overexpressing tumour cells. The mechanism is directly relevant to this disease.

This is an already-approved use: the FDA approved margetuximab in December 2020 for pretreated metastatic HER2-positive breast cancer, so it is not a true repurposing finding. Subgroup analyses in the SOPHIA literature suggest benefit is greatest in carriers of the CD16A-158F allele.

---

## Clinical Trial Evidence

No clinical trials are registered for drug-induced osteoporosis. The trials below relate to HER2 positive breast carcinoma.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02492711](https://clinicaltrials.gov/study/NCT02492711) | Phase 3 | Completed | 624 | SOPHIA: margetuximab + chemotherapy vs trastuzumab + chemotherapy in pretreated HER2+ metastatic breast cancer; underpinned FDA approval |
| [NCT04425018](https://clinicaltrials.gov/study/NCT04425018) | Phase 2 | Active, not recruiting | 174 | MARGOT: neoadjuvant paclitaxel/pertuzumab with margetuximab vs trastuzumab in stage II-III HER2+ breast cancer |
| [NCT01148849](https://clinicaltrials.gov/study/NCT01148849) | Phase 1 | Completed | 66 | Dose escalation of MGAH22 (margetuximab) in refractory HER2+ cancers; safety, dosing and early efficacy signals |
| [NCT03133988](https://clinicaltrials.gov/study/NCT03133988) | N/A | Approved for marketing | N/A | Expanded access program for pretreated HER2+ metastatic breast cancer |
| [NCT04398108](https://clinicaltrials.gov/study/NCT04398108) | Phase 1 | Completed | 16 | Pharmacokinetics and safety of margetuximab plus chemotherapy in Chinese patients |
| [NCT03219268](https://clinicaltrials.gov/study/NCT03219268) | Phase 1 | Completed | 277 | Tebotelimab (PD-1/LAG-3 bispecific), including combination with margetuximab; indirect evidence |
| [NCT05227131](https://clinicaltrials.gov/study/NCT05227131) | Phase 2 | Withdrawn | 0 | Margetuximab + tucatinib + capecitabine; no participants enrolled, no evidence |

---

## Literature Evidence

No literature is available for drug-induced osteoporosis. The publications below relate to HER2 positive breast carcinoma.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33480963](https://pubmed.ncbi.nlm.nih.gov/33480963/) | 2021 | RCT | JAMA Oncology | Phase 3 trial of margetuximab vs trastuzumab in pretreated HER2+ advanced breast cancer |
| [36332179](https://pubmed.ncbi.nlm.nih.gov/36332179/) | 2023 | RCT (final analysis) | J Clin Oncol | SOPHIA final overall survival results |
| [34916216](https://pubmed.ncbi.nlm.nih.gov/34916216/) | 2022 | Regulatory review | Clin Cancer Res | FDA approval summary: December 16, 2020 approval with chemotherapy after two or more prior anti-HER2 regimens |
| [37170847](https://pubmed.ncbi.nlm.nih.gov/37170847/) | 2023 | Review | Future Oncol | Development of margetuximab-cmkb for later-line HER2+ metastatic breast cancer |
| [33761116](https://pubmed.ncbi.nlm.nih.gov/33761116/) | 2021 | Review | Drugs | Margetuximab first approval; Fc engineering for CD16A binding |
| [33238772](https://pubmed.ncbi.nlm.nih.gov/33238772/) | 2021 | Review | Expert Opin Biol Ther | Margetuximab slightly improved PFS over trastuzumab in pretreated disease |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2+ breast cancer |
| [36730303](https://pubmed.ncbi.nlm.nih.gov/36730303/) | 2023 | Case report | Anti-Cancer Drugs | Complete response in a patient with liver metastasis after margetuximab |
| [36729856](https://pubmed.ncbi.nlm.nih.gov/36729856/) | 2023 | Case report | Anti-Cancer Drugs | Significant response in a Chinese patient progressing after second-line therapy |
| [36159262](https://pubmed.ncbi.nlm.nih.gov/36159262/) | 2022 | Economic evaluation | Front Public Health | Cost-effectiveness of margetuximab vs trastuzumab in the US and China |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761150 | MARGENZA (MacroGenics, Inc) | Injection, solution, concentrate | Indication text not available in the data compiled; status listed as cancelled |

The "Cancelled only" status appears inconsistent with the literature describing the 2020 FDA approval. The current regulatory and market status should be verified.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody with enhanced ADCC) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (risk is largely driven by the combined chemotherapy) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; HER2-directed agents typically involve cardiac function monitoring (literature on trastuzumab-class cardiotoxicity) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: Only a pharmacology record was found, identifying the drug's target, ERBB2 (HER2); no clinically graded drug-drug interactions were reported.
- **Cardiotoxicity**: HER2-directed therapies are associated with left ventricular dysfunction (per the trastuzumab-focused review, PMID 34115243). This is class context and not specific margetuximab label data.

Please refer to the package insert for full warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold for drug-induced osteoporosis; Proceed with Guardrails for HER2 positive breast carcinoma**

**Rationale:**
- Drug-induced osteoporosis has no trial or literature support and no plausible mechanism (L5), so the high score likely reflects a knowledge-graph artifact.
- HER2 positive breast carcinoma has Phase 3 RCT evidence (SOPHIA) and an FDA approval (L1), but it is an existing indication, not new repurposing.

**To proceed, the following is needed:**
- Verify the current US regulatory and market status (the "Cancelled only" listing conflicts with the approval literature)
- Obtain the FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Obtain detailed mechanism of action data
- Consider the CD16A-158F allele in patient selection
- For drug-induced osteoporosis, no further investment unless independent mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

