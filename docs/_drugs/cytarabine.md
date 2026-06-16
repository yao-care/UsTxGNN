---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 562
evidence_level: L5
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cytarabine: From Acute Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (Ara-C, cytosine arabinoside) is a classic antimetabolite used for decades in the treatment of acute leukemia and lymphoma, where it acts as an S-phase–specific DNA synthesis inhibitor by incorporating into replicating DNA and causing chain termination.
The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma (SCLC)**,
with **3 clinical trials** and **20 publications** currently identified — though the most directly relevant evidence comes from historical prospective pilot studies (1979–1988), predating the modern etoposide-platinum era.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute leukemia / lymphoma (based on pharmacological background; no US regulatory record found in current dataset) |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| US Market Status | Not found in dataset (data gap — cytarabine is globally marketed as Cytosar-U® / DepoCyt®) |
| Number of NDAs | 0 (data gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cytarabine is a pyrimidine nucleoside analog that must be phosphorylated intracellularly to its active form, cytarabine triphosphate (Ara-CTP). Ara-CTP competes with the natural substrate deoxycytidine triphosphate (dCTP) for incorporation into replicating DNA, inhibiting DNA polymerase alpha and causing chain termination. Because this mechanism is strictly dependent on active DNA replication, cytarabine preferentially kills rapidly dividing cells — a property known as **S-phase specificity**. This is the same mechanism that makes cytarabine a cornerstone of acute myeloid leukemia (AML) and other hematologic malignancies. *(Note: formal MOA data from the DrugBank query was flagged as a data gap in this evidence pack; the above reflects well-established published pharmacology.)*

SCLC is among the most rapidly proliferating of all human solid tumors — with a very high growth fraction and a cell doubling time of 25–75 days — making it biologically susceptible to S-phase cytotoxic agents. Before the etoposide-platinum (EP) era became standard of care in the 1980s, cytarabine-containing regimens were actively explored in SCLC. A 1979 prospective pilot study (PMID 232239) combined cyclophosphamide, doxorubicin, and cytarabine (20 mg/m² q12h subcutaneously, days 5–9) with thoracic and whole-brain radiotherapy in 20 treatment-naive SCLC patients. A 1984 study (PMID 6095640) evaluated continuous-infusion Ara-C directly in SCLC — confirming activity in chemotherapy-naive extensive-stage patients when combined with the CAV regimen. A 1988 study (PMID 2841844) further demonstrated cytarabine activity in the relapsed/refractory SCLC salvage setting.

The TxGNN model's 99.78% prediction score reflects strong network-level evidence linking cytarabine's pharmacological profile to SCLC biology. While modern SCLC treatment has migrated to EP/IP doublets plus immunotherapy, the unmet need in **relapsed/refractory SCLC** — an area with very few active salvage options — may justify revisiting cytarabine-containing regimens or liposomal cytarabine for CNS/leptomeningeal SCLC involvement, a niche where intrathecal Ara-C is already used empirically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for recurrent leptomeningeal metastasis from NSCLC; cytarabine is mentioned as the current standard for intrathecal chemotherapy, providing indirect context for IT route feasibility in lung cancer CNS involvement |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal pemetrexed combined with involved-field radiotherapy for leptomeningeal metastasis from solid tumors (NSCLC predominant); demonstrates safety and feasibility of combined IT chemotherapy + RT for lung cancer CNS metastases |
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy (vinorelbine, cisplatin, pemetrexed) vs. observation in early-stage NSCLC; terminated prematurely (only 34/planned enrolled); disease is NSCLC not SCLC — indirect reference only |

> **Important note:** No currently registered clinical trials directly evaluate cytarabine in SCLC. All 3 retrieved trials have only **indirect relevance (Grade C)**. The primary evidence base is historical prospective literature (1979–1992).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Prospective Cohort | Am J Clin Oncol | **Most directly relevant:** Continuous-infusion Ara-C 100 mg/m²/d in SCLC. In 10 heavily pretreated patients — no response and severe toxicity with Ara-C monotherapy. In 25 chemo-naive extensive-stage SCLC patients — Ara-C added to CAV (cyclophosphamide/doxorubicin/vincristine) showed meaningful activity |
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Prospective Cohort/Pilot | Med Pediatr Oncol | Earliest prospective study: Ara-C (20 mg/m² q12h SC, days 5–9) combined with cyclophosphamide + doxorubicin + thoracic and whole-brain RT in 20 treatment-naive SCLC patients; established initial tolerability and efficacy signals for Ara-C in SCLC |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Prospective Cohort | Am J Clin Oncol | VP-16 (etoposide) + continuous-infusion Ara-C (45 mg/m²/d × 72h) in 17 refractory/relapsed SCLC patients; confirmed salvage activity; 3 early deaths from tumor progression underscored poor baseline prognosis in this population |
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | RCT | J Clin Oncol | CALGB randomized trial evaluating warfarin addition to chemoradiation in limited-stage SCLC; establishes the chemoradiotherapy standard-of-care context in which Ara-C-containing regimens were evaluated during the same era |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case Series | Am J Med | 60 evaluable SCLC patients with meningeal/cerebral metastases; intensive systemic chemotherapy without prophylactic cranial irradiation yielded 78% CR+PR rate; documents high CNS involvement frequency in SCLC where intrathecal Ara-C is clinically relevant |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Case Report | Gan To Kagaku Ryoho | Stage IV SCLC (cT4N2M1b) with subsequent meningeal carcinomatosis managed with systemic chemotherapy, whole-brain irradiation, and IT chemotherapy including cytarabine; illustrates the clinical scenario where IT Ara-C is deployed in SCLC |
| [11331076](https://pubmed.ncbi.nlm.nih.gov/11331076/) | 2001 | Basic Science | Biochem Pharmacol | MDR SCLC cell lines (daunorubicin- and VM-26-resistant) showed **collateral sensitivity** to cytarabine and gemcitabine — key finding suggesting cytarabine may specifically overcome certain acquired resistance mechanisms in SCLC |
| [1360876](https://pubmed.ncbi.nlm.nih.gov/1360876/) | 1992 | Basic Science | Cancer Chemother Pharmacol | Doxorubicin sensitivity profiling across a panel of SCLC cell lines including MDR variants; cytarabine sensitivity characterized in the same panel, providing in vitro rationale for its activity in SCLC |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiotics Chemother | Overview of Ara-C analogs and resistance mechanisms (cytidine deaminase inactivation); foundational for understanding cytarabine's pharmacological limitations and strategies to extend its activity to solid tumors |
| [75105](https://pubmed.ncbi.nlm.nih.gov/75105/) | 1978 | Phase 2 | Eur J Cancer | EORTC Phase II trial of anhydro-ara-5-fluorocytidine (Ara-C structural analog) across multiple tumor types including **small cell anaplastic carcinoma of the lung**; early evidence that the Ara-C pharmacophore has activity in SCLC |

---

## US Market Information

The current dataset reports **no US FDA marketing authorizations** for cytarabine (market status: not found in dataset). This is a **data gap**, not a reflection of actual regulatory status. Cytarabine is an established FDA-approved chemotherapy agent. Please verify the following directly via the FDA Drugs@FDA portal:

- **Cytosar-U®** (cytarabine injection) — conventional IV/SC formulation for AML, ALL, CML, meningeal leukemia
- **DepoCyt®** (liposomal cytarabine) — intrathecal formulation for lymphomatous meningitis

No authorization table can be generated from the current dataset due to missing regulatory records.

---

## Cytotoxicity

Cytarabine is a **conventional cytotoxic antineoplastic agent** belonging to the antimetabolite class.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Antimetabolite (Pyrimidine nucleoside analog, S-phase specific) |
| Myelosuppression Risk | **High** — Dose-limiting toxicity; leukopenia, thrombocytopenia, and anemia are expected and dose-dependent. Nadir typically at days 7–14; recovery by day 21–28. High-dose Ara-C (HD-Ara-C ≥1 g/m²) carries risk of severe, prolonged myelosuppression requiring hematopoietic support |
| Emetogenicity Classification | Low to Moderate (standard-dose Ara-C); Moderate to High (high-dose Ara-C ≥1 g/m²) |
| Monitoring Items | CBC with differential and platelet count (at least twice weekly during therapy); serum creatinine and hepatic function (AST/ALT/bilirubin); neurological assessment for HD-Ara-C cerebellar toxicity; ophthalmologic examination for HD-Ara-C conjunctivitis; body weight and fluid balance |
| Handling Protection | Must follow cytotoxic drug handling regulations (NIOSH Hazardous Drug List); PPE (gown, gloves, face protection) required during preparation and administration; closed-system drug transfer devices (CSTDs) recommended |

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, drug-drug interactions) was not retrieved in this evidence pack due to data gaps. Based on established pharmacological class, the following is known from published literature:

- **Key Warnings**: Ara-C syndrome (fever, myalgia, bone pain, rash, conjunctivitis — typically 6–12h post-dose, may be corticosteroid-responsive); severe cerebellar toxicity with high-dose regimens (ataxia, dysarthria, somnolence — irreversible in some cases); pulmonary edema/ARDS reported with high-dose regimens; myelosuppression (see Cytotoxicity section)
- **Drug Interactions**: Concomitant flucytosine — cytarabine may reduce antifungal efficacy (competitive inhibition at the cellular level); oral digoxin absorption reduced when co-administered with cytarabine-containing chemotherapy regimens

> Please refer to the **official Cytosar-U® and DepoCyt® package inserts** for complete, up-to-date safety information, contraindications, and drug interaction data before any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Historical clinical studies from 1979–1988 directly demonstrate that cytarabine has cytotoxic activity in SCLC — both as a component of induction regimens in chemo-naive patients and as a salvage agent in relapsed/refractory disease. The mechanistic basis (S-phase cytotoxicity against a highly proliferative neuroendocrine tumor) is pharmacologically sound. However, no modern prospective trials specifically evaluating cytarabine in SCLC exist, and current standard-of-care has advanced significantly beyond these historical regimens.

**To proceed, the following is needed:**
- Retrieve complete FDA package insert for Cytosar-U® and DepoCyt® to confirm approved indications, contraindications, and boxed warnings
- Conduct a systematic literature review specifically targeting cytarabine salvage use in post-EP/IP relapsed SCLC (2000–present) to determine whether any modern regimens have revisited this approach
- Evaluate **liposomal cytarabine (DepoCyt®)** for intrathecal use in **leptomeningeal SCLC** as the highest-priority niche — an area of genuine unmet need where IT Ara-C has established precedent
- Conduct preclinical validation using contemporary EP-resistant SCLC organoid or PDX models to quantify Ara-C sensitivity in the modern resistance context
- Assess combination potential with topoisomerase inhibitors (topotecan, irinotecan) or BCL-2 inhibitors (venetoclax) based on the collateral sensitivity finding in MDR SCLC cell lines (PMID 11331076)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

