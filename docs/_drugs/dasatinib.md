---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is a potent oral multi-targeted tyrosine kinase inhibitor approved globally for chronic myeloid leukemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukemia (Ph+ ALL), though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **2 directly relevant clinical trials** (including 1 completed Phase 2 multi-sarcoma basket trial, n=366) and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan registration; globally approved for CML and Ph+ ALL |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the primary data source (TFDA/DrugBank query returned no MOA entry). Based on the published scientific literature cited in the evidence pack, dasatinib is a small-molecule oral kinase inhibitor that potently suppresses BCR-ABL (at 325-fold the potency of imatinib), Src family kinases, c-KIT, PDGFR-α/β, and ephrin A receptors at nanomolar concentrations. Its established clinical use is in BCR-ABL-driven hematologic malignancies. The Src family kinase inhibition profile is what makes Ewing sarcoma a biologically plausible target.

Ewing sarcoma cells are highly dependent on Src kinase activity for invasive behavior. Micro-environmental stressors (hypoxia, nutrient deprivation) activate Src signaling to drive invadopodia formation and cell migration in Ewing sarcoma (PMID 27566104). The matricellular protein tenascin C further cooperates with Src to promote metastatic spread (PMID 31521948). At the molecular complex level, the FAK-Src axis has been identified as a core targetable pathway in Ewing sarcoma alongside desmoplastic small round cell tumors (PMID 35655525). Importantly, direct in vitro experiments have demonstrated that dasatinib inhibits proliferation and migration of Ewing sarcoma cell lines by suppressing c-KIT and PDGFR in addition to Src (PMID 18202781, 17363602).

The mechanistic case is supported by a completed Phase 2 basket trial in advanced sarcomas (NCT00464620, n=366) that provides the strongest available clinical signal. However, Ewing sarcoma-specific response data from this trial have not been independently confirmed in published subgroup analyses. A dedicated pediatric Phase 1/2 study (NCT00788125) was terminated after enrolling only 7 patients, leaving the clinical evidence for this specific population incomplete. The prediction is biologically coherent but requires prospective validation in a Ewing sarcoma-specific cohort before clinical deployment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Basket trial of dasatinib in advanced sarcomas; examines response rate and 6-month progression-free survival across sarcoma subtypes — Ewing sarcoma likely included, but Ewing-specific subgroup results require confirmation from published reports |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric trial of dasatinib combined with ifosfamide, carboplatin, and etoposide (ICE chemotherapy) in relapsed/refractory sarcomas including Ewing sarcoma; terminated early due to extremely low enrollment, limiting any clinical interpretation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | In vitro preclinical | Oncology Reports | Dasatinib inhibits proliferation and migration in Ewing sarcoma and neuroblastoma cell lines by blocking c-KIT and PDGFR; first direct evidence of dasatinib activity in ES cells |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | In vitro preclinical | Cancer Research | Dasatinib inhibits migration and invasion in diverse human sarcoma cell lines; induces apoptosis in bone sarcoma cells dependent on Src kinase for survival |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Preclinical mechanistic | Sarcoma | FAK-Src complex is a targetable axis in Ewing sarcoma; dasatinib single-agent showed limited clinical activity, highlighting the need for FAK-Src combination inhibition strategies |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical mechanistic | Neoplasia | Tenascin C and Src cooperate to drive invadopodia formation and metastasis in Ewing sarcoma; microenvironmental Src activation is a rational therapeutic target |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical mechanistic | Neoplasia | Micro-environmental stress induces Src-dependent activation of invadopodia and cell migration in Ewing sarcoma; Src inhibition attenuates this invasive phenotype |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Comprehensive review of Src signaling in sarcoma biology; discusses Src as a potential drug target across sarcoma subtypes and the rationale for Src inhibitors including dasatinib |

---

## Taiwan Market Information

Dasatinib is **not currently registered in Taiwan** (TFDA). There are no active licenses, approved indications, or dosage form authorizations in the Taiwan regulatory database. The drug is marketed globally as **Sprycel®** (Bristol Myers Squibb) for CML and Ph+ ALL; a Taiwan-specific NDA has not been identified in the current evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — BCR-ABL / Src / PDGFR-α/β / c-KIT multi-kinase inhibitor (second-generation TKI) |
| Myelosuppression Risk | Moderate — neutropenia, thrombocytopenia, and anemia are well-documented class effects; specific grades depend on indication and dose regimen |
| Emetogenicity Classification | Low to moderate (consistent with oral targeted kinase inhibitors) |
| Monitoring Items | Complete blood count with differential (CBC-diff), liver function tests (ALT/AST), renal function, pleural effusion surveillance (chest X-ray or CT), QTc interval monitoring |
| Handling Protection | Oral targeted therapy; classify and handle per institutional cytotoxic drug handling policies; standard PPE for preparation and dispensing |

---

## Safety Considerations

Taiwan TFDA package insert data (warnings and contraindications) is not available in the current evidence pack. Please refer to the global Sprycel® (dasatinib) prescribing information for the full safety profile.

The following safety signals are reported in the published literature included in this evidence pack:

- **Pleural effusion**: Reported in approximately one-third of patients on long-term dasatinib therapy; dasatinib-associated interstitial pneumonitis has also been described (PMID 36346055)
- **Chylothorax**: Rare complication from thoracic lymphatic leakage into the pleural space (PMID 36448074)
- **Skin and soft tissue infections**: Reported in adolescent CML patients on long-term dasatinib treatment (PMID 35441424)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological rationale for dasatinib in Ewing sarcoma is mechanistically sound — Src/FAK-axis dependency has been well-characterized and dasatinib's direct in vitro activity in Ewing sarcoma cell lines is demonstrated — but clinical evidence is limited to an indirect basket-trial signal (NCT00464620, mixed sarcoma population) and a terminated pediatric study (NCT00788125, n=7). Ewing sarcoma-specific efficacy data have not been confirmed in a prospective, dedicated trial, and the evidence does not yet meet the threshold for clinical deployment.

**To proceed, the following is needed:**
- Published subgroup analysis from the completed Phase 2 basket trial (NCT00464620) confirming Ewing sarcoma-specific response rate and progression-free survival data
- A prospective, Ewing sarcoma-dedicated Phase 2 study of dasatinib alone or in combination with standard-of-care chemotherapy (e.g., ICE or VDC/IE regimens)
- Preclinical validation of FAK-Src combination inhibition strategies to address the known limitations of single-agent Src inhibitor activity (as noted in PMID 35655525)
- Taiwan TFDA registration and package insert retrieval for complete domestic safety assessment (currently a Blocking data gap)
- DrugBank MOA data retrieval to enable formal mechanistic linkage scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

