---
layout: default
title: Paclitaxel
parent: Model Prediction Only (L5)
nav_order: 1007
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "PACLITAXEL"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Paclitaxel: predicted new indication Parameningeal embryonal rhabdomyosarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Paclitaxel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Paclitaxel: Parameningeal embryonal rhabdomyosarcoma
{: .text-alpha }

## One-Sentence Summary

The data compiled for this report include **40 clinical trials** and **20 publications** for this prediction, but paclitaxel is already an established breast cancer treatment, so this is not true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of NDAs | 12 (3 NDAs and 9 ANDAs) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the source database. From established pharmacology, paclitaxel stabilizes microtubules and blocks disassembly of the mitotic spindle. This causes G2/M cell-cycle arrest and apoptosis in rapidly dividing tumor cells.

Ovarian cancer and breast cancer are both epithelial solid tumors that respond to taxane chemotherapy. Taxane activity does not depend on hormone receptor status. Reviews in the compiled literature describe paclitaxel and docetaxel as evidence-based components of therapy for advanced breast, lung and ovarian carcinomas, and paclitaxel has been approved in the US for adjuvant treatment of node-positive early breast cancer.

The prediction is therefore biologically sound, but it reflects a **well-established use rather than a novel repurposing signal**. Subtype-level predictions show the same pattern. ER-negative, ER-positive and hormone-resistant breast cancer are supported by clinical trials, while rarer or non-human categories are weakly supported (see the conclusion).

---

## Clinical Trial Evidence

The data include 40 trials for female breast carcinoma. The table lists the 10 most relevant, favoring completed, randomized or larger studies with paclitaxel as a core agent.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | Completed | 50 | Weekly 1-hour paclitaxel plus anti-HER2 antibody (trastuzumab) in metastatic breast cancer |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Phase 2 | Unknown | Not reported | Randomized comparison of two schedules of docetaxel or paclitaxel in metastatic breast cancer |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | Not reported | Gemcitabine plus paclitaxel versus paclitaxel alone in unresectable, locally recurrent or metastatic breast cancer |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Phase 3 | Completed | 580 | Lapatinib plus paclitaxel versus paclitaxel alone as first-line therapy in advanced or metastatic breast cancer |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane-based chemotherapy with lapatinib versus trastuzumab in HER2-positive metastatic breast cancer |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Completed | 455 | Neo-ALTTO: neoadjuvant lapatinib, trastuzumab or both plus paclitaxel in HER2-positive breast cancer |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Phase 3 | Completed | 632 | ETNA: neoadjuvant nab-paclitaxel versus solvent-based paclitaxel before anthracycline regimens in HER2-negative high-risk breast cancer |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense adjuvant FE75C followed by docetaxel versus paclitaxel in node-positive breast cancer |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | Completed | 280 | Neoadjuvant FEC then paclitaxel plus trastuzumab versus the reverse sequence in HER2-positive operable breast cancer |
| [NCT00006110](https://clinicaltrials.gov/study/NCT00006110) | Phase 2 | Completed | 82 | AC followed by 12 weeks of paclitaxel with or without trastuzumab in stage IIB–IV breast cancer |

Most of these trials test paclitaxel as the backbone chemotherapy in combination studies, rather than testing paclitaxel itself against a placebo.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | Taxanes stabilize microtubules. Paclitaxel and docetaxel are evidence-based components of therapy for advanced breast, lung and ovarian cancers, and paclitaxel is approved in the US for adjuvant treatment of node-positive early breast cancer |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Paclitaxel and docetaxel in breast and ovarian cancer; licensing extended to first-line ovarian cancer and metastatic breast cancer |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase 2 trial | Cancer | Doxorubicin plus paclitaxel in metastatic breast carcinoma; importance of prior adjuvant anthracycline therapy |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Clinical study | Cancer | Role of paclitaxel in multimodality treatment of inflammatory breast carcinoma |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | Dose-finding study | Ann Oncol | Maximum tolerable doses of 3-hour paclitaxel with cyclophosphamide in advanced breast cancer |
| [10898354](https://pubmed.ncbi.nlm.nih.gov/10898354/) | 2000 | Review | Cancer | Developments in breast cancer chemotherapy |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Preclinical/computational | Chem Biol Drug Des | Paclitaxel combinations against breast carcinoma and in vivo biomarkers |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Translational | Nat Commun | TEKT4 germline variations linked to breast cancer resistance to paclitaxel |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Preclinical | J Cell Physiol | ZD6474 enhances paclitaxel antiproliferative and apoptotic effects in breast carcinoma cells |
| [7904376](https://pubmed.ncbi.nlm.nih.gov/7904376/) | 1993 | Review | Semin Oncol Nurs | Overview of paclitaxel development and its mechanism of action |

The literature for this indication is mostly older reviews and early-phase studies. Several retrieved items are off-topic, such as a cyclosporine anaphylaxis case and breast reconstruction papers.

---

## US Market Information

The table shows five of the main ones.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021660 | ABRAXANE (Abraxis BioScience) | Injection, powder, lyophilized, for suspension | Not available |
| NDA216338 | Paclitaxel (Teva Pharmaceuticals) | Injection, powder, lyophilized, for suspension | Not available |
| NDA211875 | Paclitaxel protein-bound particles, albumin-bound (American Regent) | Injection, powder, lyophilized, for suspension | Not available |
| ANDA075184 | Paclitaxel (Teva Parenteral Medicines) | Injection, solution, concentrate | Not available |
| ANDA076131 | Paclitaxel (Hospira) | Injection, solution | Not available |

All forms are injectable.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane class, microtubule stabilizer) |
| Myelosuppression Risk | High. Neutropenia is the dose-limiting toxicity; the knowledge graph also flags neutropenia, agranulocytosis, thrombocytopenia and anemia as cautions |
| Emetogenicity Classification | Low to moderate, according to general drug-class knowledge |
| Monitoring Items | Complete blood count with differential, liver function (hyperbilirubinemia and liver disease are flagged), renal function, and peripheral neuropathy assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations. Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. This is a blocking gap for safety screening.

- **Disease-level cautions (knowledge graph, not label text)**: The knowledge graph lists contraindication links to these conditions:
  - Hematologic: neutropenia, agranulocytosis, thrombocytopenia, anemia (including macrocytic anemia) and hemoglobinopathy.
  - Hepatic and renal: liver disease, gallbladder disease, hyperbilirubinemia (including Gilbert syndrome) and kidney disease.
  - Neurologic: peripheral neuropathy and peripheral nervous system disease.
  - Cardiovascular: myocardial infarction, coronary thrombosis, sudden cardiac arrest and hypotensive disorder.
  - Metabolic and respiratory: diabetes mellitus, diabetic ketoacidosis and asthma.
  - Skin and psychiatric: psoriasis and parapsoriasis, plus anxiety, neurotic and dysthymic disorders.
- **Drug Interactions**: 100 interactions were found. Those listed (about 20) are mostly moderate:
  - Moderate: aprepitant, cimetidine, clarithromycin, clotrimazole, dexamethasone, eliglustat, metronidazole, miconazole, rolapitant, rosuvastatin, simvastatin, tinidazole and troglitazone.
  - Minor: ascorbic acid and levofloxacin.
  - Unknown severity: glimepiride, doxycycline, morphine, metformin and omeprazole.
  - Many of the moderate interactions likely involve CYP metabolism (for example CYP2C8 and CYP3A4), but this is not stated in the data.

Literature also reports paclitaxel-associated pneumonitis, uveitis, corneal lesions and taxane-induced polyneuropathy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Paclitaxel has multiple completed Phase 2 and Phase 3 trials in breast cancer where it is the chemotherapy backbone, and the mechanism is well understood. This supports L2 evidence (a Phase 3 trial of paclitaxel itself as the investigational agent is not in the supplied data). The recommendation applies to female breast carcinoma and its subtypes with trial support (ER-negative/triple-negative, ER-positive, hormone-resistant), which are established uses rather than novel repurposing.

Other predictions in the data are weaker:
- **Research question**: breast carcinoma by gene expression profile, which is a biomarker category rather than a distinct indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently a blocking gap, to complete safety screening.
- Mechanism of action data from DrugBank.
- Current US label indications.
- Pivotal comparative data for specific settings, such as ER-negative and hormone-resistant disease, rather than combination studies where paclitaxel is only the backbone.
- A monitoring plan for myelosuppression, neuropathy and hypersensitivity, and a review of CYP-related drug interactions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

