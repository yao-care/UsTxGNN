---
layout: default
title: Dacarbazine
parent: Moderate Evidence (L3-L4)
nav_order: 563
evidence_level: L4
indication_count: 1
monitor_inn: "DACARBAZINE"
predicted_indications: ["upper aerodigestive tract neoplasm"]
last_modified_at: 2026-10-14
description: "Dacarbazine: predicted new indication Upper aerodigestive tract neoplasm (evidence level L4). Approved use: Hodgkin lymphoma and metastatic melanoma"
---

# Dacarbazine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Dacarbazine: From Hodgkin Lymphoma and Metastatic Melanoma to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Dacarbazine is an alkylating chemotherapy drug originally used for Hodgkin lymphoma and metastatic melanoma.
The TxGNN model predicts it may be effective for **upper aerodigestive tract neoplasm**,
but there are **0 registered clinical trials** and only indirect literature (**20 publications**, none showing direct efficacy in this indication) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma and metastatic melanoma (approved indication text is not available in the US license records) |
| Predicted New Indication | Upper aerodigestive tract neoplasm |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of the drug class, dacarbazine is an alkylating agent. Its active metabolite (MTIC) methylates DNA and is cytotoxic to rapidly dividing tumour cells. This gives a plausible but generic link to head and neck and upper aerodigestive tract malignancies.

The retrieved literature does not show direct evidence in squamous cell carcinoma of the upper aerodigestive tract. It instead covers tumour types where dacarbazine has been used: melanoma (including mucosal disease), Hodgkin lymphoma involving head and neck sites, medullary thyroid carcinoma (dacarbazine plus 5-FU), and head and neck paragangliomas. The very high TxGNN score most likely reflects these related-tumour associations and not validated efficacy in this indication. The prediction should therefore be treated as a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomised trial directly tests dacarbazine in this indication. The most relevant publications are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | RCT (Phase 3) | JAMA Oncol | Toripalimab vs dacarbazine as first-line therapy in advanced acral melanoma; dacarbazine was the comparator, so the evidence is indirect |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Clinical study | Ann Oncol | Small series of dacarbazine plus 5-FU in advanced medullary thyroid cancer |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | Cohort | Cancer | Characteristics and outcomes of Hodgkin lymphoma involving head and neck sites |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Cohort | Ear Nose Throat J | Single-institution experience with six head and neck malignant paragangliomas |
| [31621203](https://pubmed.ncbi.nlm.nih.gov/31621203/) | 2019 | Prospective observational | Cancer Med | Carbon-ion radiotherapy plus DAV chemotherapy (dacarbazine, nimustine, vincristine) in 21 patients with head and neck mucosal melanoma |
| [11815960](https://pubmed.ncbi.nlm.nih.gov/11815960/) | 2002 | Preclinical | Cancer | Dacarbazine combined with radioimmunotherapy in medullary thyroid carcinoma xenografts in mice |
| [12845209](https://pubmed.ncbi.nlm.nih.gov/12845209/) | 2003 | Case report | Onkologie | Mucosal metastases of malignant melanoma in the oesophagus, stomach, bladder and tonsil |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | Review | Am J Clin Dermatol | Current concepts in melanoma management |
| [20138008](https://pubmed.ncbi.nlm.nih.gov/20138008/) | 2010 | Review | Transfus Apher Sci | Hodgkin lymphoma in HIV-infected patients |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | Clin Oncol | Medullary thyroid carcinoma overview |

## US Market Information

All three US authorisations for single-agent dacarbazine are cancelled. Approved indication text is not available in the records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075259 (Meitheal Pharmaceuticals) | Dacarbazine | Injection, powder, for solution | Not available |
| ANDA075371 (Fresenius Kabi USA) | Dacarbazine | Injection, powder, for solution | Not available |
| ANDA075812 (Hikma Pharmaceuticals USA) | Dacarbazine | Injection, powder, lyophilised, for solution | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph links the drug to leukopenia, thrombocytopenia and anaemia as contraindicated conditions, which suggests haematological toxicity is a concern |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count, liver function and renal function (the knowledge graph flags kidney and liver disease) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindicated conditions (from the knowledge graph, not label text)**: kidney disease, pyoureter, liver disease, gallbladder disease, thrombocytopenia, anaemia, macrocytic anaemia, leukopenia, hepatic vein thrombosis, Budd-Chiari syndrome.
- **Drug Interactions**: 100 interactions were found. Of those shown, naltrexone is rated Moderate and levofloxacin Minor. The remainder, including pantoprazole, morphine, metformin, omeprazole, palonosetron, prednisone, simvastatin, aprepitant and ondansetron, have no severity rating.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and indirect literature from other tumour types. There are no registered trials, no direct evidence in upper aerodigestive tract neoplasm, and no valid US marketing authorisation. Evidence is at L4.

**To proceed, the following is needed:**
- Review of the current FDA package insert for warnings and contraindications, since this safety data is missing
- Detailed mechanism of action data
- Direct preclinical or clinical evidence in upper aerodigestive tract tumours, in particular squamous cell carcinoma
- Clarification of the regulatory pathway, since all US licences are cancelled
- Comparison with current standard therapies for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

