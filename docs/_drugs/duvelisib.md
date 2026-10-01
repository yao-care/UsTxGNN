---
layout: default
title: Duvelisib
parent: Model Prediction Only (L5)
nav_order: 637
evidence_level: L5
indication_count: 10
---

# Duvelisib
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

# Duvelisib: From Relapsed/Refractory CLL/SLL to Hodgkin Lymphoma

## One-Sentence Summary

Duvelisib (COPIKTRA) is an oral dual PI3K-delta/gamma inhibitor. The literature in the Evidence Pack documents its US approval for relapsed/refractory chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL).
The TxGNN model predicts it may be effective for **Hodgkin lymphoma**, but the supporting **10 clinical trials** and **16 publications** all address non-Hodgkin lymphoma or other blood cancers, and **none is specific to Hodgkin lymphoma**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license data. The literature reports approval for relapsed/refractory CLL/SLL (PMID 30430368). |
| Predicted New Indication | Hodgkin lymphoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (no Hodgkin-specific clinical data; only indirect NHL and mechanism evidence) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 records (both NDA211155) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Duvelisib blocks the PI3K-delta and PI3K-gamma enzymes. PI3K-delta supports B-cell receptor signaling and B-cell survival. PI3K-gamma affects the tumor microenvironment and T-cell/macrophage function. This dual action is the basis for its use in B-cell and T-cell malignancies.

Hodgkin lymphoma is also a lymphoid malignancy, so the model's high score probably reflects how close it sits to other lymphomas in the knowledge graph. One preclinical paper (PMID 29522278) studied duvelisib in Epstein-Barr virus-associated lymphoma cells. It notes that PI3K/Akt signaling is active in such lymphomas, including Hodgkin lymphoma. The abstract shown does not confirm that Hodgkin cells were tested.

The trials and papers supplied cover indolent NHL, follicular, mantle cell and T-cell lymphomas, and CLL/SLL, not classical Hodgkin lymphoma. The mechanistic link is plausible but unproven for this disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04038359](https://clinicaltrials.gov/study/NCT04038359) | Phase 2 | Completed | 103 | Randomized comparison of two intermittent duvelisib dosing schedules (2-week dose holidays) in indolent NHL. Indirect for Hodgkin lymphoma. |
| [NCT01882803](https://clinicaltrials.gov/study/NCT01882803) | Phase 2 | Completed | 129 | Duvelisib monotherapy in refractory indolent NHL (follicular, marginal zone, small lymphocytic). Relevance not yet graded. |
| [NCT04379167](https://clinicaltrials.gov/study/NCT04379167) | Phase 2 | Unknown | 140 | Single-arm study of YY-20394 (a different PI3K inhibitor) in relapsed/refractory follicular NHL. Indirect only. |
| [NCT04803201](https://clinicaltrials.gov/study/NCT04803201) | Phase 2 | Suspended | 170 | Duvelisib plus CHOEP chemotherapy in untreated peripheral T-cell lymphoma. Different disease. |
| [NCT01871675](https://clinicaltrials.gov/study/NCT01871675) | Phase 1 | Completed | 48 | Duvelisib plus rituximab or bendamustine/rituximab in relapsed/refractory lymphoma or CLL. Indirect. |
| [NCT05065866](https://clinicaltrials.gov/study/NCT05065866) | Phase 1 | Completed | 14 | Safe dose of duvelisib plus BMS-986345 in lymphoid malignancy. Not Hodgkin-specific. |
| [NCT05044039](https://clinicaltrials.gov/study/NCT05044039) | Phase 1 | Active, not recruiting | 42 | Duvelisib after CAR T-cell therapy, to improve CAR T-cell persistence. Not Hodgkin-specific. |
| [NCT05923502](https://clinicaltrials.gov/study/NCT05923502) | N/A | Not yet recruiting | 200 | Real-world observational study of duvelisib in NHL. No data yet. |
| [NCT02576275](https://clinicaltrials.gov/study/NCT02576275) | Phase 3 | Withdrawn | 0 | Duvelisib plus bendamustine/rituximab vs placebo in indolent NHL. Never enrolled, so no data. |
| [NCT04836832](https://clinicaltrials.gov/study/NCT04836832) | Phase 1 | Withdrawn | 0 | Duvelisib plus acalabrutinib in indolent NHL. Never enrolled, so no data. |

Only the first two trials produced completed results in any lymphoma population, and both are in indolent NHL, not Hodgkin lymphoma.

---

## Literature Evidence

No randomized controlled trial specific to Hodgkin lymphoma was found. The publications below are the most relevant, ranked by study type.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36685572](https://pubmed.ncbi.nlm.nih.gov/36685572/) | 2022 | Systematic review / meta-analysis | Front Immunol | Evaluates duvelisib safety and efficacy across relapsed/refractory lymphoid neoplasms. |
| [31490009](https://pubmed.ncbi.nlm.nih.gov/31490009/) | 2019 | Phase 1b trial | Am J Hematol | Duvelisib with rituximab or bendamustine/rituximab in relapsed/refractory NHL and CLL. |
| [29191916](https://pubmed.ncbi.nlm.nih.gov/29191916/) | 2018 | Phase 1 trial | Blood | 210 patients with advanced hematologic malignancies. Maximum tolerated dose was 75 mg twice daily, and the drug was clinically active. |
| [30799261](https://pubmed.ncbi.nlm.nih.gov/30799261/) | 2019 | Commentary on clinical study | Lancet Oncol | Discussion of duvelisib in indolent NHL (no abstract available). |
| [32356174](https://pubmed.ncbi.nlm.nih.gov/32356174/) | 2020 | Review | Curr Treat Options Oncol | PI3K inhibitors as targeted lymphoma therapy, including the rationale and on-target side effects. |
| [33132100](https://pubmed.ncbi.nlm.nih.gov/33132100/) | 2021 | Review | Clin Lymphoma Myeloma Leuk | Next-generation PI3K inhibitors in B-cell lymphoma. |
| [31580408](https://pubmed.ncbi.nlm.nih.gov/31580408/) | 2019 | Review | Am J Health Syst Pharm | Approved targeted therapies for B- and T-cell lymphomas. |
| [33616890](https://pubmed.ncbi.nlm.nih.gov/33616890/) | 2021 | Review | Drugs | New therapy approaches in follicular lymphoma. |
| [36882482](https://pubmed.ncbi.nlm.nih.gov/36882482/) | 2023 | Preclinical | Sci Rep | PI3K-gamma and PI3K-delta drive mantle cell lymphoma proliferation and migration, supporting duvelisib efficacy. |
| [28017967](https://pubmed.ncbi.nlm.nih.gov/28017967/) | 2017 | Preclinical / correlative | Leukemia | Duvelisib changes apoptotic regulators and sensitizes CLL cells to venetoclax. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211155 | COPIKTRA (Secura Bio, Inc) | Capsule (oral) | Not provided in the license data |

The Evidence Pack lists this NDA twice with identical content, so it is shown once here.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral dual PI3K-delta/gamma inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

The Evidence Pack contains no warnings, contraindications or drug interaction data for this drug. As a class-level note from the supplied analysis, PI3K inhibitors carry risks of serious infection, diarrhea/colitis, cutaneous reactions and pneumonitis. Literature also notes that toxicity has limited use of first-generation PI3K inhibitors in CLL (PMID 35899388).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.94% TxGNN score is not backed by any Hodgkin lymphoma trial or publication. The trials and papers supplied address NHL, T-cell lymphoma and CLL/SLL. Three of the ten listed trials are withdrawn, and the only Phase 3 among them (NCT02576275) enrolled no one. The class carries known serious toxicities, and the package insert safety data has not been obtained.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (data gap DG001, blocking) to complete safety screening
- Detailed mechanism of action data from DrugBank (data gap DG002)
- Hodgkin-specific evidence, such as preclinical data in Hodgkin cell lines or an early-phase trial in relapsed/refractory classical Hodgkin lymphoma
- Confirmation of the current approved indication text, since the license data is empty
- A comparison against existing Hodgkin lymphoma treatments to assess unmet need

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

