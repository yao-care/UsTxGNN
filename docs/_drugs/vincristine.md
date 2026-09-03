---
layout: default
title: Vincristine
parent: 僅模型預測 (L5)
nav_order: 1293
evidence_level: L5
indication_count: 3
---

# Vincristine
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

# Vincristine: From Hematologic and Pediatric Solid Tumor Chemotherapy to Ganglioneuroblastoma

## One-Sentence Summary

> Vincristine is a vinca alkaloid chemotherapy agent widely used as a component of combination regimens for leukemia, lymphoma, and pediatric solid tumors.
> The TxGNN model predicts it may be effective for **Ganglioneuroblastoma**,
> with **4 clinical trials** and **6 publications** currently supporting this direction — several of which already show vincristine being used clinically in this exact disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack; vincristine is a well-established component of combination chemotherapy for hematologic malignancies (leukemia, lymphoma) and pediatric solid tumors |
| Predicted New Indication | Ganglioneuroblastoma |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, vincristine is a vinca alkaloid that binds tubulin and inhibits microtubule assembly, arresting tumor cells in the M phase of mitosis. This mitotic-inhibition mechanism underlies its broad activity across rapidly dividing malignant cells and is why it forms the backbone ("V" in VAC, OPEC, and similar regimens) of many pediatric oncology protocols.

Ganglioneuroblastoma is a tumor of the sympathetic nervous system within the neuroblastic tumor family (spanning neuroblastoma to ganglioneuroma), and it is treated with the same combination chemotherapy backbones used for neuroblastoma. Notably, the literature evidence retrieved for this candidate already documents vincristine being used clinically to treat ganglioneuroblastoma (e.g., in combination with cisplatin, doxorubicin, and cyclophosphamide), and the associated Phase 2/3 trials target the broader "high-risk neuroblastoma/ganglioneuroblastoma" disease category. This suggests the TxGNN prediction is recovering an already-established clinical practice pattern rather than proposing a novel mechanistic hypothesis — which strengthens biological plausibility, though it also means the "new indication" framing should be interpreted as formalizing existing off-label/protocol use rather than a genuinely novel therapeutic direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Phase 2 | Active, not recruiting | 42 | Pilot induction regimen adding dinutuximab and sargramostim to chemotherapy for newly diagnosed high-risk neuroblastoma |
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Phase 3 | Recruiting | 750 | 131I-MIBG or ALK inhibitor (lorlatinib) added to intensive standard therapy for newly diagnosed high-risk neuroblastoma/ganglioneuroblastoma |
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Phase 3 | Recruiting | 478 | Dinutuximab added to intensive multimodal therapy (induction chemo, surgery, transplant, immunotherapy) for newly diagnosed high-risk neuroblastoma |
| [NCT01798004](https://clinicaltrials.gov/study/NCT01798004) | Phase 1 | Completed | 150 | Myeloablative busulfan/melphalan consolidation following induction chemotherapy for newly diagnosed high-risk neuroblastoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Case report | Postgraduate Medical Journal | Spinal ganglioneuroblastoma achieved complete response with chemotherapy (including vincristine) alone, without surgery or radiotherapy |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Case report | Journal of Pediatric Hematology/Oncology | Ganglioneuroblastoma presenting with obstructive jaundice, treated with cisplatin/doxorubicin/cyclophosphamide/vincristine regimen |
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Prospective clinical trial | Pediatric Blood & Cancer | Image-defined risk factors used to guide surgical timing in low-risk neuroblastoma disease (Japan Children's Cancer Group) |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Case report | Hinyokika Kiyo | Multimodality treatment of adult adrenal ganglioneuroblastoma with regional lymph node metastasis |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Case report | Journal of Pediatric Hematology/Oncology | Gastric involvement in an infant with multifocal ganglioneuroblastoma |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Case series | Journal of Thoracic and Cardiovascular Surgery | 31 patients with intrathoracic ganglioneuroblastoma treated with resection, radiation, or chemotherapy; long-term follow-up up to 25 years |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid / mitotic spindle inhibitor) |
| Myelosuppression Risk | Low relative to most cytotoxic agents; dose-limiting toxicity is peripheral neuropathy rather than bone marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC, neurological exam (peripheral neuropathy, constipation/ileus), liver function; strict IV-line monitoring for extravasation (vesicant) |
| Handling Protection | Requires cytotoxic drug handling protocols; well-documented risk of fatality if administered intrathecally — for IV administration only, with route clearly labeled |

*Note: The above reflects general pharmacological knowledge of the vinca alkaloid class, as drug-specific MOA/toxicity data (DG002) is not available in this evidence pack.*

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data for this candidate are marked as data gaps — notably DG001, a **Blocking**-severity gap for TFDA label warnings/contraindications, is required before this candidate can proceed to safety initial assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is biologically plausible and partially corroborated by existing literature showing vincristine already used in ganglioneuroblastoma treatment protocols, but a **Blocking** data gap (TFDA warnings/contraindications, DG001) prevents this candidate from entering safety initial assessment (S1). No decision to proceed can be made until this gap is closed.

**To proceed, the following is needed:**
- TFDA (or equivalent regulatory) label PDF for warnings and contraindications (DG001 — Blocking)
- DrugBank-sourced detailed mechanism of action data (DG002 — High)
- Confirmation of current Taiwan/US market/licensing status given "Not Marketed" flag with 0 licenses on file
- Awaiting completion of ongoing Phase 3 trials (NCT03126916, NCT06172296) to upgrade evidence level beyond L3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

