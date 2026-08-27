---
layout: default
title: Lomustine
parent: 僅模型預測 (L5)
nav_order: 867
evidence_level: L5
indication_count: 10
---

# Lomustine
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

# Lomustine: From Undocumented Original Indication to Lymphosarcoma

## One-Sentence Summary

Lomustine (CCNU, DrugBank DB01206) is a nitrosourea alkylating-agent chemotherapy drug; its original approved indication is not documented in the current evidence pack, and the drug is not currently marketed in this jurisdiction. The TxGNN model predicts strong relevance to **Lymphosarcoma**, and this pairing is already supported by **17 clinical trials** and **20 publications**, much of which reflects lomustine's long-established international use in lymphoma-directed chemotherapy regimens rather than a purely novel signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available data (drug not currently marketed in this jurisdiction) |
| Predicted New Indication | Lymphosarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lomustine is not available in this evidence pack (data gap DG002). Based on the literature retrieved within this pack itself, lomustine (CCNU) is a **nitrosourea alkylating agent** — the same pharmacologic class as BCNU and methyl-CCNU — noted for its lipophilicity and ability to cross the blood-brain and hemo-meningeal barriers, which historically made it a mainstay for CNS-penetrant chemotherapy (PMID 782694, PMID 1470749).

This class-level mechanism is directly relevant to lymphosarcoma: alkylating agents damage DNA in rapidly dividing lymphoid cells, and nitrosoureas in particular have been used for decades in Hodgkin's disease and non-Hodgkin lymphoma (NHL) regimens — including LOPP, LEMP, CAMP, PACET, and CIBO-P — several of which are represented in the literature and trial evidence below. The predicted indication therefore does not represent a mechanistically novel hypothesis so much as a **re-confirmation of a well-documented, if not currently regulatory-filed, clinical use pattern**.

Because original indication and regulatory history are undocumented in this jurisdiction (market status: 未上市, 0 licenses), the primary uncertainty is not mechanistic plausibility but **local regulatory and safety documentation** — this is captured as a Blocking-severity data gap (DG001) below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01775475](https://clinicaltrials.gov/study/NCT01775475) | Phase 2 (Randomized) | Completed | 7 | RCT comparing IV CHOP vs. oral chemotherapy (incl. lomustine, etoposide, procarbazine) in HIV-associated NHL, Sub-Saharan Africa |
| [NCT00049439](https://clinicaltrials.gov/study/NCT00049439) | Phase 2 | Completed | 54 | Dose-modified oral lomustine + etoposide + cyclophosphamide + procarbazine in AIDS-related non-Hodgkin lymphoma (US and Africa) |
| [NCT00074191](https://clinicaltrials.gov/study/NCT00074191) | Phase 2 | Completed | 1 | Methotrexate, procarbazine, lomustine (MPC) ± intraventricular/intra-ocular chemo for primary CNS lymphoma |
| [NCT00003114](https://clinicaltrials.gov/study/NCT00003114) | Phase 2 | Completed | 5 | Oral lomustine, etoposide, cyclophosphamide, procarbazine for stage IIB–IV AIDS-related Hodgkin's disease |
| [NCT00989352](https://clinicaltrials.gov/study/NCT00989352) | Phase 2 | Unknown | 56 | Rituximab + high-dose methotrexate + lomustine + procarbazine, then maintenance, in elderly primary CNS lymphoma |
| [NCT00003113](https://clinicaltrials.gov/study/NCT00003113) | Phase 2 | Terminated | 6 | Oral combination chemotherapy + G-CSF in elderly intermediate/high-grade NHL |
| [NCT00003929](https://clinicaltrials.gov/study/NCT00003929) | Phase 2 | Withdrawn | 0 | Lomustine, procarbazine, filgrastim + radiation for AIDS-related and immunocompetent primary CNS lymphoma |
| [NCT00317408](https://clinicaltrials.gov/study/NCT00317408) | N/A | Unknown | 96 | Combination chemotherapy + total-body irradiation + stem cell transplant for relapsed anaplastic large cell lymphoma (childhood) |
| [NCT05518383](https://clinicaltrials.gov/study/NCT05518383) | Phase 4 | Recruiting | 300 | B-cell mature NHL treatment protocol for pediatric/adolescent patients, evaluating MRD and risk stratification |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [348294](https://pubmed.ncbi.nlm.nih.gov/348294/) | 1978 | RCT (CALGB) | Cancer | Randomized comparison of CCNU vs. methyl-CCNU in advanced Hodgkin's disease, lymphosarcoma, and reticulum cell sarcoma |
| [21303800](https://pubmed.ncbi.nlm.nih.gov/21303800/) | 2011 | Pilot Trial | Annals of Oncology | Rituximab + methotrexate + procarbazine + lomustine (R-MCP) for primary CNS lymphoma in elderly patients |
| [15803492](https://pubmed.ncbi.nlm.nih.gov/15803492/) | 2005 | Clinical Trial | Cancer | Lomustine + ifosfamide + bleomycin + vincristine + cisplatin (CIBO-P) for refractory/recurrent aggressive NHL |
| [2259920](https://pubmed.ncbi.nlm.nih.gov/2259920/) | 1990 | Phase II Study | Seminars in Oncology | Lomustine, cytarabine, mitoxantrone, prednisone (CAMP) for doxorubicin-resistant intermediate/high-grade NHL |
| [8422281](https://pubmed.ncbi.nlm.nih.gov/8422281/) | 1993 | Clinical Study | European J of Cancer | Prednisolone, cytarabine, lomustine, etoposide, thioguanine (PACET) for relapsed/refractory NHL |
| [8436213](https://pubmed.ncbi.nlm.nih.gov/8436213/) | 1993 | Clinical Study | European J of Haematology | Lomustine, etoposide, methotrexate, prednisone (LEMP) for relapsed/refractory NHL |
| [10711848](https://pubmed.ncbi.nlm.nih.gov/10711848/) | 1999 | Clinical Study | Drugs | Oral lomustine, etoposide, cyclophosphamide, procarbazine regimen in AIDS-related lymphoproliferative malignancies (38 patients) |
| [30197327](https://pubmed.ncbi.nlm.nih.gov/30197327/) | 2018 | Retrospective | J of Cancer Research and Therapeutics | Lomustine-containing LACE conditioning regimen before autologous HSCT in refractory/relapsed lymphoma |
| [35999255](https://pubmed.ncbi.nlm.nih.gov/35999255/) | 2022 | Retrospective | Scientific Reports | Comparison of lomustine-containing CEAC vs. BEAM vs. IEAC conditioning before ASCT in peripheral T-cell lymphoma |
| [33336792](https://pubmed.ncbi.nlm.nih.gov/33336792/) | 2021 | Case Series | British J of Haematology | DECC (dexamethasone, etoposide, chlorambucil, lomustine) oral regimen in relapsed/refractory diffuse large B-cell lymphoma |

---

## US Market Information

Currently no marketing authorization is on file for this jurisdiction (Market status: **未上市 / Not Marketed**; total licenses: **0**).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Nitrosourea alkylating agent) |
| Myelosuppression Risk | High — nitrosoureas cause delayed, cumulative, dose-limiting myelosuppression; the evidence pack itself includes a case of hemorrhagic diathesis and bone marrow aplasia following lomustine overdose (PMID 31062418) |
| Emetogenicity Classification | Moderate to High (single oral alkylating-agent dosing) |
| Monitoring Items | CBC with differential (delayed nadir, typically 4–6 weeks post-dose), pulmonary function (nitrosourea-associated lung toxicity is described in the retrieved literature, PMID 1470749), renal and hepatic function |
| Handling Protection | Cytotoxic drug handling precautions required per standard oral chemotherapy protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the drug-disease pairing has reasonable supporting evidence (L2 — one completed randomized Phase 2 trial plus a substantial body of historical lymphoma-chemotherapy literature), the evidence pack has a **Blocking-severity data gap (DG001)**: TFDA label warnings and contraindications are entirely undocumented, which by definition prevents even a preliminary (S1) safety assessment. The drug also has no marketing history in this jurisdiction, so local safety and dosing precedent cannot be assumed.

**To proceed, the following is needed:**
- TFDA/local label PDF for lomustine, including warnings and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action and original-indication data from DrugBank or an equivalent regulatory source (DG002, High)
- A formal drug-drug interaction (DDI) review, since the current DDI query returned no results
- Given the high myelosuppression risk of this drug class, a hematological monitoring plan before any S1 safety evaluation can be completed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

