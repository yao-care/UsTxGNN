---
layout: default
title: Chlorambucil
parent: Model Prediction Only (L5)
nav_order: 518
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-29
monitor_inn: "CHLORAMBUCIL"
predicted_indications: ["chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma"]
description: "Chlorambucil: predicted new indication Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation (evidence level L5)."
---

# Chlorambucil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Chlorambucil: Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation
{: .text-alpha }

## One-Sentence Summary

Chlorambucil is an oral DNA-alkylating agent, originally used for Hodgkin lymphoma, follicular lymphoma, acute lymphoblastic leukemia and related lymphoid malignancies.
The TxGNN model predicts it may be effective for **chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) with immunoglobulin heavy chain variable-region gene somatic hypermutation**.
However, **0 clinical trials** and **0 publications** were found for this specific subtype, so the prediction rests on model proximity to existing indications rather than new evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation |
| TxGNN Prediction Score | 0.9972 |
| Evidence Level | L5 (preclinical/mechanistic only; no trials or subtype-specific literature) |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, chlorambucil is a nitrogen mustard-type DNA-alkylating agent. It cross-links DNA and triggers cell death in rapidly dividing lymphoid cells. It has a long history in CLL and indolent lymphomas.

The predicted entity is a molecular subtype of CLL/SLL, defined by somatic hypermutation of the immunoglobulin heavy chain variable-region genes. This is the same disease family as the established lymphoid indications, so the mechanistic link is plausible but indirect. The high TxGNN score most likely reflects closeness to existing indications rather than new subtype-specific evidence.

Chlorambucil has also largely been replaced in CLL by targeted therapies such as BTK inhibitors and BCL2 inhibitors. For example, a phase 3 comparison (RESONATE-2) showed ibrutinib to be superior to chlorambucil in older untreated CLL/SLL patients. This limits the practical value of the prediction.

Other predictions in the list are also of interest, but their evidence is mostly weaker:
- **Pregerminal center CLL/SLL** (score 0.9972): plausible by the same reasoning, with only a 2003 review as context.
- **Primary pulmonary lymphoma** (score 0.9942): the best-supported of the other predictions (L3), because chlorambucil has been used in indolent extranodal marginal zone/MALT lymphoma. The supporting data are case reports, retrospective series, guidelines and a small 1987 phase II study.
- **Small cell lung carcinoma** (score 0.9924): historical trials were negative or showed no meaningful benefit, and current evidence is mostly preclinical.
- **ALK-positive large B-cell lymphoma, well-differentiated fetal adenocarcinoma of the lung and pulmonary blastoma:** computational prediction only (L5).
- **Acute lymphoblastic leukemia:** already listed among the original indications, so this is not true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication.

For context, the only trial-type evidence found among the other predictions is historical and appears in the literature table below.

## Literature Evidence

No publications were found for the top-ranked subtype. The table below lists the most relevant items for closely related predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Review | Ned Tijdschr Geneeskd | Describes pre-germinal-center (unmutated) vs. post-germinal-center CLL subtypes and argues for risk-adapted treatment (pregerminal center CLL/SLL) |
| [36672456](https://pubmed.ncbi.nlm.nih.gov/36672456/) | 2023 | Cohort | Cancers | Long-term follow-up of RESONATE-2: ibrutinib was superior to chlorambucil in older untreated CLL/SLL |
| [3307632](https://pubmed.ncbi.nlm.nih.gov/3307632/) | 1987 | Phase II trial | Gan To Kagaku Ryoho | 8 patients with hematologic malignancies; partial remission in 2 CLL cases, 1 follicular lymphoma and 1 pulmonary pseudolymphoma; myelosuppression noted |
| [18603558](https://pubmed.ncbi.nlm.nih.gov/18603558/) | 2008 | Guideline | Haematologica | Italian practice guidelines for primary lung and mediastinal lymphomas |
| [19541720](https://pubmed.ncbi.nlm.nih.gov/19541720/) | 2009 | Cohort | Eur Respir J | 63 patients with pulmonary MALT lymphoma; clinical characteristics and prognostic factors |
| [25452791](https://pubmed.ncbi.nlm.nih.gov/25452791/) | 2015 | Case report/Review | Exp Ther Med | Pulmonary MALT lymphoma case in a 19-year-old with literature review |
| [688257](https://pubmed.ncbi.nlm.nih.gov/688257/) | 1978 | Randomized trial | Cancer Treat Rep | Adriamycin plus chlorambucil vs. adriamycin plus thiabendazole in extensive non-small cell lung cancer (pilot study; small cell lung cancer is not the studied entity) |
| [6254684](https://pubmed.ncbi.nlm.nih.gov/6254684/) | 1980 | Phase II trial | Cancer Chemother Pharmacol | Prednimustine (a chlorambucil ester) in small-cell lung cancer: no responses in 19 pretreated patients; 3 brief responses in 9 untreated patients over 70 |
| [3179770](https://pubmed.ncbi.nlm.nih.gov/3179770/) | 1988 | Phase I trial | Cancer Invest | Pulsed chlorambucil in advanced cancers; central nervous system toxicity was dose-limiting |
| [41025286](https://pubmed.ncbi.nlm.nih.gov/41025286/) | 2026 | Preclinical | Int J Cancer | Chlorambucil-conjugated pyrrole-imidazole polyamide targeting STMN1 in small cell lung cancer (early-stage) |
| [2825510](https://pubmed.ncbi.nlm.nih.gov/2825510/) | 1987 | Phase II trial | Am J Clin Oncol | High-dose chlorambucil in non-small cell lung cancer: no objective responses; significant toxicity including seizures (off-target indication) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA010669 | LEUKERAN (Waylis Therapeutics LLC) | Film-coated tablet (oral) | Not specified in the record; status valid |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrogen mustard alkylating agent) |
| Myelosuppression Risk | High (myelosuppression is reported in the supplied clinical literature; knowledge-graph contraindications include neutropenia, leukopenia, thrombocytopenia, anemia and lymphopenia) |
| Emetogenicity Classification | Low to moderate at usual oral doses; nausea and vomiting were prominent at high doses in older trials |
| Monitoring Items | Complete blood count with differential, liver and renal function; neurological status (seizures were reported at high doses) |
| Handling Protection | Follow cytotoxic drug handling regulations. Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text):** epilepsy, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, lymphopenia, anemia, nephrotic syndrome, interstitial lung disease, pulmonary fibrosis, drug-induced liver injury, and acute leukemia (including mixed phenotype and biphenotypic forms).
- **Drug Interactions:** 100 interactions were recorded. Major-level interactions include **deferiprone** and **samarium (153Sm) lexidronam**. Moderate-level interactions include amphotericin B (all formulations), palifermin, strontium chloride Sr-89, mercaptopurine, roflumilast and chloramphenicol. Minor: levofloxacin. Several others (e.g., warfarin, prednisone, omeprazole) are of unknown severity.
- **Literature-reported risks:** CNS toxicity and seizures at high doses, myelosuppression, and an increased risk of second malignancies (including acute leukemia) in patients treated for Hodgkin disease.

Please refer to the package insert for full safety information, as label warnings and contraindications were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials and no subtype-specific literature, and chlorambucil has largely been replaced by BTK and BCL2 inhibitors in CLL/SLL. The US license is cancelled, and the safety profile includes significant myelosuppression and second-malignancy risk. Primary pulmonary lymphoma (indolent MALT type) is the most promising secondary lead (L3), but even there the evidence is retrospective or case-level.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- For the top prediction: evidence that chlorambucil offers a benefit in IGHV-mutated CLL/SLL over current targeted therapies, such as a comparative analysis of existing CLL trial data by IGHV status
- For primary pulmonary lymphoma: a structured review of chlorambucil use in MALT/marginal zone lymphoma, and a decision on whether a prospective study is justified
- A clear regulatory and availability assessment, given that the US NDA is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

