---
layout: default
title: Crizotinib
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Crizotinib: predicted new indication Gingival fibromatosis (evidence level L5). Approved use: Non-small cell lung cancer"
monitor_inn: "CRIZOTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Crizotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Crizotinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis
{: .text-alpha }

## One-Sentence Summary

Crizotinib is an oral kinase inhibitor, originally used to treat ALK-positive non-small cell lung cancer (NSCLC) and lung cancer.
The TxGNN model's top-ranked prediction is **Gingival Fibromatosis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.
Among the ten predictions, only **lung germ cell tumor** has linked trials (2) and literature, and even that evidence is non-specific.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer; lung cancer |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the published literature, crizotinib is an ATP-competitive small-molecule inhibitor of the receptor tyrosine kinases ALK, ROS1 and c-MET. Its efficacy in ALK-rearranged and ROS1-rearranged NSCLC is well established.

For the top prediction, gingival fibromatosis, no plausible link to ALK, ROS1 or MET inhibition is evident. The high score (0.998) reflects knowledge-graph association only. Other predictions are more biologically coherent but still weakly supported:

- **Lung germ cell tumor** (rank 7): A rationale exists only if the tumor carries an ALK, ROS1 or MET alteration. Linked trials are tumor-agnostic and biomarker-driven.
- **Fibroma of lung** (rank 2): A theoretical link to ALK-driven mesenchymal tumors is possible but unsupported by data.
- **Lung hilum carcinoma**, **pulmonary sulcus neoplasm** (ranks 4 and 6): These are largely forms of NSCLC, so they fall under the existing indication and are not true repurposing.
- **Lung benign neoplasm** (rank 5): The Phase 3 RCTs retrieved all concern malignant ALK-positive NSCLC and do not transfer to benign lesions. The label appears to be a mapping artifact.

---

## Clinical Trial Evidence

The top-ranked prediction (gingival fibromatosis) has no registered clinical trials. The only predictions with linked trials are shown below (lung germ cell tumor, rank 7).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01121588](https://clinicaltrials.gov/study/NCT01121588) | Phase 1 | Terminated | 44 | Safety and efficacy of crizotinib in ALK-positive tumors other than NSCLC. No germ cell tumor data shown. |
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, not recruiting | 6,452 | NCI-MATCH basket trial of genetically directed therapy in refractory solid tumors, lymphomas and myeloma. Link to lung germ cell tumor is non-specific. |

---

## Literature Evidence

The top-ranked prediction has no linked literature. The table below shows the most relevant publications across the predictions, with their relevance qualified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23724913](https://pubmed.ncbi.nlm.nih.gov/23724913/) | 2013 | RCT (Phase 3) | N Engl J Med | Crizotinib vs chemotherapy in advanced ALK-positive lung cancer (approved indication) |
| [25470694](https://pubmed.ncbi.nlm.nih.gov/25470694/) | 2014 | RCT (Phase 3) | N Engl J Med | First-line crizotinib vs chemotherapy in ALK-positive NSCLC |
| [28586279](https://pubmed.ncbi.nlm.nih.gov/28586279/) | 2017 | RCT (Phase 3) | N Engl J Med | Alectinib vs crizotinib in untreated ALK-positive NSCLC |
| [30280657](https://pubmed.ncbi.nlm.nih.gov/30280657/) | 2018 | RCT (Phase 3) | N Engl J Med | Brigatinib vs crizotinib in ALK-positive NSCLC |
| [33568345](https://pubmed.ncbi.nlm.nih.gov/33568345/) | 2021 | Clinical study | Clin Cancer Res | Crizotinib activity in ALK-aberrant relapsed/refractory neuroblastoma (COG ADVL0912) |
| [37012551](https://pubmed.ncbi.nlm.nih.gov/37012551/) | 2023 | Phase 1 trial | Nat Med | Lorlatinib (not crizotinib) in ALK-driven neuroblastoma |
| [39716454](https://pubmed.ncbi.nlm.nih.gov/39716454/) | 2024 | Case report | Am J Case Rep | Pathological complete response to crizotinib plus chemotherapy in ROS1-positive locally advanced lung adenocarcinoma |
| [34011083](https://pubmed.ncbi.nlm.nih.gov/34011083/) | 2021 | Case report | Medicine | ALK-negative lung inflammatory myofibroblastic tumor; indirect to hamartoma |
| [31559892](https://pubmed.ncbi.nlm.nih.gov/31559892/) | 2020 | Case report | Cancer Biol Ther | Primary pulmonary atypical carcinoid with EML4-ALK rearrangement |

Note that the Phase 3 RCTs all concern the already-approved NSCLC indication and do not support any of the predicted new indications.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA217581 | Xalkori | Capsule, coated pellets | Not available (status: cancelled) |
| NDA202570 | Xalkori | Capsule | Not available (status: cancelled) |

Both authorizations (Pfizer) are cancelled; none is currently valid.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/MET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (case reports of fatal hepatotoxicity), ECG/heart rate (bradycardia, QT prolongation), CBC |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Safety signals from case reports in the retrieved literature:** fatal fulminant liver failure (PMID 26898609), multiple simultaneous cardiac toxicities including bradycardia, QT prolongation and ventricular fibrillation (PMID 29717400), sick sinus syndrome (PMID 25922742), erythema multiforme (PMID 25994067), and erosive esophagitis in a pediatric patient (PMID 29357780).
- **Drug Interactions:** 100 interactions were identified. Major-level interactions in the listed results include **clarithromycin, cisapride, dolasetron, eliglustat and granisetron**. Moderate-level interactions include famotidine, metformin, loperamide, bupropion, aprepitant, dexamethasone and budesonide, among others.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, gingival fibromatosis, rests on a model score alone, with no trials, no literature, and no plausible mechanistic link. Predictions with some supporting material are either already covered by the approved NSCLC indication or backed only by non-specific basket trials. Both US authorizations are cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A mechanistic or molecular rationale (for example, ALK, ROS1 or MET alteration status) for any selected indication
- For lung germ cell tumor (the only candidate with trial linkage, currently a research question), crizotinib-arm outcomes from NCT01121588 and NCT02465060 in that tumor type
- A hepatic and cardiac safety monitoring plan, given the reported toxicities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

