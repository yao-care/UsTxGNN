---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 1166
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus: From Organ Transplant Rejection to Liposarcoma

## One-Sentence Summary

> Sirolimus (rapamycin) is an mTOR inhibitor originally developed as an immunosuppressant to prevent organ (kidney) transplant rejection.
> The TxGNN model predicts it may be effective for **Liposarcoma**,
> with **5 clinical trials** and **12 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of organ transplant rejection (immunosuppressant) — not formally recorded in this evidence pack; inferred from supporting literature (see below) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for sirolimus is not available in this evidence pack (formal MOA field is a data gap). Based on known drug class information, sirolimus is an mTOR (mammalian target of rapamycin) inhibitor, part of the rapalogue family that also includes temsirolimus and everolimus. Its efficacy as an immunosuppressant for renal transplant rejection prophylaxis has been established for decades.

The bridge between the original indication (transplant immunosuppression) and the predicted new indication (liposarcoma) is unusually well documented within the literature evidence itself. Several publications describe an unexpected observation from the transplant setting: switching transplant patients from calcineurin inhibitors (e.g., cyclosporine) to sirolimus reduces the incidence of *de novo* malignancy (PMID 16434506, PMID 20534289, PMID 26093731). This antineoplastic signal, first observed incidentally in transplant recipients, motivated direct investigation of sirolimus and its analogues in solid tumors, including sarcomas.

Mechanistically, dedifferentiated liposarcoma frequently shows activation of the Akt-mTOR and MAPK signaling pathways (PMID 26518767), providing a direct molecular rationale for mTOR inhibition as an antitumor strategy. This is reinforced by a completed Phase 2 trial (NCT02821507) that directly tested sirolimus in combination with cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma, along with multiple trials of the closely related rapalogues temsirolimus and everolimus in advanced sarcoma populations.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm trial of sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma, based on preclinical evidence that mTOR inhibition prevents tumor growth |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (mTOR inhibitor, AP23573) in advanced sarcoma; large sample size, includes liposarcoma histology |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + temsirolimus (sirolimus analogue) in pediatric recurrent/refractory sarcoma |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus (sirolimus analogue) in advanced dedifferentiated liposarcoma and leiomyosarcoma |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus + liposomal doxorubicin in advanced soft tissue and bone sarcoma; dose-finding and efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT (Phase 2) | Clin Cancer Res | Ribociclib (CDK4/6 inhibitor) + everolimus (mTOR inhibitor) shows synergistic growth inhibition in dedifferentiated liposarcoma and leiomyosarcoma models and patients |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanistic | Tumour Biol | Akt/mTOR and MAPK pathways are activated in dedifferentiated liposarcoma specimens; in vitro mTOR inhibition shows antitumor effect |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma, including targeted and mTOR-pathway agents |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Review of new molecular-targeted agents for advanced sarcomas, including mTOR inhibitors |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical/Cohort | Cancer Genomics Proteomics | Combination of chloroquine and rapamycin (sirolimus) shows synergistic autophagy inhibition and efficacy in well-differentiated liposarcoma |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | Randomized trial: switching renal transplant patients from cyclosporine to sirolimus reduces risk of skin and non-skin malignancy |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Cohort | Transplant Proc | Immunosuppressive drug choice (including sirolimus), cumulative dose, and viral infection affect malignancy development in long-term transplant patients |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical (PDOX model) | In Vivo | Chloroquine + rapamycin arrests tumor growth in a patient-derived orthotopic xenograft model of dedifferentiated liposarcoma |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | MLN0128, an ATP-competitive mTOR kinase inhibitor, shows potent in vitro/in vivo antitumor activity in bone and soft-tissue sarcoma |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Review of targeted treatments for rare connective tissue tumors and sarcomas, including mTOR-pathway-directed therapy |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial (NCT02821507) directly evaluated sirolimus in myxoid liposarcoma, and this is reinforced by a broader body of Phase 2 evidence for closely related mTOR inhibitors (ridaforolimus, temsirolimus, everolimus) in liposarcoma and advanced sarcoma populations, together with a clear mechanistic rationale (Akt-mTOR/MAPK pathway activation in dedifferentiated liposarcoma).

**To proceed, the following is needed:**
- Formal mechanism of action (MOA) documentation from DrugBank or equivalent source
- Regulatory safety data: key warnings, contraindications, and drug-drug interactions (currently all data gaps)
- Confirmation of sirolimus's original approved indication and licensing status (not recorded in this evidence pack)
- Route of administration and dosage form compatibility assessment for a liposarcoma indication
- Comparative analysis against approved rapalogue analogues (temsirolimus, everolimus, nab-sirolimus) already used in related sarcoma/PEComa indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

