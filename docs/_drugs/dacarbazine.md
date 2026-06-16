---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 563
evidence_level: L5
indication_count: 1
---

# Dacarbazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Dacarbazine: From Melanoma to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Dacarbazine (DTIC) is a classic cytotoxic alkylating agent, long established as a standard chemotherapy backbone for advanced melanoma and soft tissue sarcoma.
The TxGNN model predicts it may be effective for **Upper Aerodigestive Tract (UADT) Neoplasm** — a broad category encompassing oral cavity, pharynx, larynx, sinonasal, thyroid, and esophageal malignancies —
with **1 clinical trial** and **20 publications** currently identified in support of this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced melanoma; soft tissue sarcoma (Hodgkin's disease) |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L3 |
| US Market Status | Not marketed (no licenses found in database) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. However, based on well-established pharmacology, dacarbazine is a triazene alkylating prodrug that undergoes hepatic activation to its active metabolite **MTIC** (monomethyl triazeno imidazole carboxamide). MTIC methylates DNA at the O⁶ position of guanine, triggering mismatch repair (MMR)-mediated cell death. This is precisely the same mechanism as **temozolomide**, its oral second-generation analogue — a relationship directly relevant to the evidence reviewed below.

The link between dacarbazine's established indications and UADT neoplasms is mechanistically coherent: the UADT harbors several tumour subtypes with biological profiles that overlap with dacarbazine's known targets. **Mucosal melanoma** of the oral cavity, nasal cavity, and sinuses shares the same melanocytic origin as cutaneous melanoma, for which dacarbazine remains a registered comparator standard. Similarly, **paragangliomas** and **esthesioneuroblastomas** of the head and neck are neuroendocrine tumours — a family dacarbazine has been used to treat (e.g., Hodgkin's disease, neuroendocrine variants). **Medullary thyroid carcinoma**, anatomically within the UADT region, has also been directly investigated with dacarbazine-based regimens.

The strongest indirect evidence comes from temozolomide's Phase 2 trial in UADT cancers (NCT00423150), which confirms that MGMT-pathway alkylation is biologically actionable in this anatomical space. Because dacarbazine and temozolomide share identical downstream mechanisms, this trial constitutes Grade B indirect support for dacarbazine repurposing in the same indication. The TxGNN model's 99.26% score likely reflects this mechanistic and epidemiological convergence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | Terminated | 86 | Temozolomide (oral analogue of dacarbazine, identical MGMT-alkylating mechanism) in MGMT-methylation–selected patients with advanced aerodigestive tract cancers (head & neck, esophageal, NSCLC) and colorectal cancer. Trial terminated; published results (PMID 23443801) show limited efficacy despite biomarker enrichment, suggesting MGMT methylation alone is insufficient for patient selection in UADT. |

> ⚠️ **Note:** The sole registered trial uses **temozolomide**, not dacarbazine directly. No trials with dacarbazine as the investigational agent specifically for UADT neoplasm were identified. This is classified as indirect (Class B) evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | Phase 3 RCT | JAMA Oncology | Toripalimab vs **dacarbazine** as first-line therapy for advanced acral melanoma. Dacarbazine served as the active comparator arm, confirming its continued use as a clinical benchmark in advanced melanoma — the subtype most directly overlapping with UADT mucosal melanoma. |
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase 2 RCT | Mol Cancer Ther | Phase 2 study of temozolomide in MGMT-methylated aerodigestive tract and colorectal cancers (NCT00423150). Limited responses observed; MGMT methylation alone insufficient for patient selection. Establishes alkylating agent activity in UADT as investigable but not yet confirmed. |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Case Series | Ann Oncol | **Dacarbazine + 5-FU** combination chemotherapy in advanced medullary thyroid carcinoma (a neuroendocrine UADT tumour). Cytotoxic drug combination explored given MTC's neuroendocrine biology; provides direct evidence of dacarbazine use in a UADT-region neoplasm. |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Case Series | Gan To Kagaku Ryoho | CYVADIC regimen (cyclophosphamide, vincristine, doxorubicin, **DTIC/dacarbazine**) for head and neck angiosarcoma (Wilson-Jones type). Dacarbazine included as active component; angiosarcoma of head/neck falls within UADT region. Prognosis poor despite multimodal treatment. |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Retrospective Cohort | Ear Nose Throat J | Six-patient series of malignant head and neck paragangliomas. Characterises genetic mutations and treatment options; identifies systemic chemotherapy as a consideration for this rare UADT neoplasm subtype relevant to dacarbazine's neuroendocrine activity profile. |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Retrospective Case Series | Int J Radiat Oncol | Radiotherapy for esthesioneuroblastoma (olfactory neuroblastoma) — a rare UADT neoplasm. Multi-centre analysis; context for the broader UADT neoplasm treatment landscape. |
| [3153227](https://pubmed.ncbi.nlm.nih.gov/3153227/) | 1986 | Case Report | Pediatr Hematol Oncol | Olfactory neuroblastoma with intracranial extension in a 2-year-old; treated with radiation and combination chemotherapy including **cyclophosphamide** (a related alkylating agent). Historical precedent for alkylating chemotherapy in UADT neuroblastic tumours. |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | Clin Oncol | Comprehensive review of medullary thyroid carcinoma (MTC) biology, RET mutations, and treatment. Describes the limited role of cytotoxic chemotherapy in systemic MTC — relevant context for dacarbazine's potential in this UADT neoplasm. |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | Epidemiological Review | J Cancer Res Clin Oncol | Global burden of EBV-related cancers including nasopharyngeal carcinoma (a major UADT tumour). Epidemiological context; EBV-driven NPC is a dominant UADT malignancy where novel systemic therapies are actively sought. |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | Review | Am J Clin Dermatol | Comprehensive melanoma management review covering dacarbazine's role as standard systemic therapy. Establishes dacarbazine as the reference alkylating agent for melanoma, including mucosal subtypes that arise within UADT anatomical sites. |

---

## US Market Information

No US FDA licenses (NDAs) for dacarbazine were identified in the current database query. The drug is listed as **not marketed** in this dataset.

> ⚠️ **Data Verification Recommended:** Dacarbazine (DTIC-Dome®) has historically held FDA approval for metastatic melanoma and Hodgkin's disease. The absence of records in this dataset likely reflects a database gap rather than true non-approval status. Manual verification against the FDA Orange Book or DailyMed is recommended before drawing regulatory conclusions.

---

## Cytotoxicity

Dacarbazine meets antineoplastic criteria: it is a conventional cytotoxic chemotherapy agent in the triazene/alkylating class, used for melanoma and Hodgkin's disease.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Triazene alkylating agent (DNA O⁶-methylguanine methylation via active metabolite MTIC) |
| Myelosuppression Risk | High — leukopenia and thrombocytopenia are dose-limiting toxicities; nadir typically at 3–4 weeks |
| Emetogenicity Classification | High — dacarbazine is among the most emetogenic IV agents; prophylactic 5-HT₃ antagonist + NK₁ antagonist + dexamethasone required |
| Monitoring Items | CBC with differential (before each cycle and at nadir), hepatic function (ALT, AST, bilirubin), renal function (creatinine); monitor for hepatic veno-occlusive disease |
| Handling Protection | Must follow cytotoxic drug handling regulations — prepare in a biological safety cabinet, personal protective equipment (gloves, gown, eye protection) mandatory; classified as NIOSH hazardous drug |

---

## Safety Considerations

Safety-specific data (package insert warnings, contraindications, drug interactions) was not retrievable for this candidate from the current data sources.

> Please refer to the current package insert and institutional chemotherapy protocols for complete safety information, including hepatotoxicity risk, renal impairment dosing adjustments, photosensitivity precautions, and reproductive toxicity warnings.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for dacarbazine specifically in UADT neoplasms remains indirect (L3): the only clinical trial used temozolomide (an analogue, not dacarbazine itself) and was terminated without meeting endpoints, while literature support consists largely of case series, reviews, and trials using dacarbazine in mechanistically adjacent but anatomically distinct tumour types. The mechanistic rationale is scientifically sound, particularly for UADT mucosal melanoma and neuroendocrine subtypes, but direct efficacy data is absent.

**To proceed, the following is needed:**

- **Direct clinical evidence:** Identify or initiate a pilot study of dacarbazine (or DTIC-containing regimen) specifically in UADT subtypes — particularly **mucosal melanoma of the oral/sinonasal cavity** (highest mechanistic overlap with dacarbazine's approved indication)
- **MOA data confirmation:** Retrieve full DrugBank entry to formally document dacarbazine's mechanism, pharmacokinetics, and DrugBank categories for regulatory submission readiness
- **Safety data retrieval:** Download and parse the FDA package insert (DailyMed) to populate key warnings, contraindications, and drug interactions — currently a blocking data gap
- **UADT subtype stratification:** Disaggregate the broad "upper aerodigestive tract neoplasm" category — dacarbazine's likelihood of benefit differs substantially between mucosal melanoma (high plausibility), paraganglioma (moderate), esthesioneuroblastoma (moderate), and squamous cell carcinoma (low) subtypes
- **Temozolomide cross-referencing:** Analyse why NCT00423150 was terminated and whether patient selection (MGMT methylation) or dose schedule was the limiting factor — this directly informs dacarbazine trial design
- **US regulatory status verification:** Confirm current FDA approval status and labelled indications against FDA Orange Book and DailyMed to correct the apparent database gap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

