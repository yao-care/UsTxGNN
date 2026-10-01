---
layout: default
title: Hydroxyurea
parent: Model Prediction Only (L5)
nav_order: 781
evidence_level: L5
indication_count: 10
---

# Hydroxyurea
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

# Hydroxyurea: From Approved Antineoplastic Use to Female Breast Carcinoma

## One-Sentence Summary

Hydroxyurea is an oral antineoplastic drug that inhibits ribonucleotide reductase. It is marketed in the US as capsules, and the pack lists no approved-indication text.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but **0 clinical trials** are registered for this indication.
The **20 retrieved publications** are mostly preclinical or indirect. Only two older, small clinical regimen reports include hydroxyurea in breast cancer patients.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.97% (model rank 1406) |
| Evidence Level | L4 (preclinical and mechanism studies only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (NDA and ANDA authorizations) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the DrugBank record. The reasoning below is inferred from known pharmacology.

Hydroxyurea inhibits ribonucleotide reductase (RNR). This depletes the dNTP pool needed for DNA synthesis and causes S-phase arrest and replication stress. That is plausible for rapidly proliferating tumors such as breast cancer.

Preclinical work supports the link. Valproic acid sensitizes breast cancer cells to hydroxyurea by blocking RPA2-mediated DNA repair. The RNR inhibitor COH29 inhibits DNA repair in BRCA1-defective breast cancer cells. EYA4 helps breast cancer cells avoid replication stress.

The prediction score is high, but it is a model output and not clinical proof.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No RCTs were retrieved. The table shows the most relevant items, ordered clinical first and then preclinical.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Single-arm clinical study | Bone Marrow Transplant | 26 women with responding metastatic breast cancer received hydroxyurea (18 g/m²) added to cyclophosphamide and thiotepa with autologous stem cell rescue as consolidation |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I | Am J Clin Oncol | 20 patients with advanced GI and breast cancers received allopurinol, 5-FU and leucovorin followed by hydroxyurea. The tumor types are mixed, so breast-specific results are unclear |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico design | Drug Res | Hydroxyurea–lipid conjugates designed to overcome poor lipophilicity, targeting the PI3K/AKT/mTOR pathway in breast cancer |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitized breast cancer cells to hydroxyurea by inhibiting RPA2 hyperphosphorylation-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | 2-hexyl-4-pentynoic acid proposed as a valproic acid alternative that influences RPA2-mediated DNA repair, following the hydroxyurea sensitization work |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclinical | Mol Pharmacol | The RNR inhibitor COH29 inhibited DNA repair in BRCA1-defective breast cancer cells. It targets the same enzyme as hydroxyurea |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | Preclinical | Mol Cancer | EYA4 promotes breast cancer progression and metastasis through replication stress avoidance |
| [34661718](https://pubmed.ncbi.nlm.nih.gov/34661718/) | 2022 | Preclinical | Naunyn Schmiedebergs Arch Pharmacol | Hydroxyurea-loaded Fe3O4/SiO2/chitosan nanoparticles showed pH-dependent release, cell cycle arrest and altered p53 and lincRNA-p21 expression |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Rep Hematol | Management of coexisting breast cancer and essential thrombocythemia. It is a treatment-challenge report, not evidence of breast cancer efficacy |
| [28585003](https://pubmed.ncbi.nlm.nih.gov/28585003/) | 2017 | Case report | Breast Cancer | Secondary breast carcinoma in a patient previously treated with hydroxyurea and imatinib for CML. It is not efficacy evidence |

## US Market Information

Approved indication text is not listed in the supplied data.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA016295 | HYDREA | Capsule | H2-Pharma LLC |
| ANDA075340 | Hydroxyurea | Capsule | Endo USA, Inc. |
| ANDA075340 | Hydroxyurea | Capsule | Major Pharmaceuticals |
| ANDA075143 | Hydroxyurea | Capsule | AvKARE |
| ANDA218021 | Hydroxyurea | Capsule | Qilu Pharmaceutical Co., Ltd. |

Other dosage forms in the market data are oral solution and film-coated tablet.

## Cytotoxicity

The pack contains no toxicity data. The entries below reflect general knowledge of this drug class and should be checked against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | High (dose-limiting toxicity; cytopenias expected) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, renal and liver function |
| Handling Protection | Follow cytotoxic drug handling regulations (e.g., gloves when handling capsules) |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, but there are no registered trials in breast cancer. Clinical data are limited to two older, small studies that include hydroxyurea inside multi-drug regimens. The remaining literature is preclinical or indirect. The high TxGNN score alone does not justify advancing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Breast cancer-specific efficacy data, such as a hydroxyurea combination study (e.g., with a DNA repair inhibitor) or a clinical review of prior regimens
- A comparison against current standard breast cancer therapy to define where hydroxyurea would fit

**Note:** Within this pack, hydroxyurea for sickle cell–hemoglobin C disease has much stronger support. It is rated L2, with Phase 2 trials and a 2025 publication. Two of the three dedicated Phase 2 trials were terminated early, and one enrolled a single participant. It merits a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

