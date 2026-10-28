---
layout: default
title: Temozolomide
parent: Model Prediction Only (L5)
nav_order: 1209
evidence_level: L5
indication_count: 1
monitor_inn: "TEMOZOLOMIDE"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-23
description: "Temozolomide: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Anaplastic astrocytoma"
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Temozolomide: From Anaplastic Astrocytoma to Cauda Equina Neoplasm
{: .text-alpha }

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy drug. The knowledge graph records it for anaplastic astrocytoma, astrocytoma (excluding glioblastoma) and brain glioblastoma.
The TxGNN model predicts it may be useful for **cauda equina neoplasm**, but the supporting evidence is limited to **0 clinical trials** and **1 directly relevant case report** (3 publications were retrieved in total).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaplastic astrocytoma; astrocytoma (excluding glioblastoma); brain glioblastoma (relations recorded in the knowledge graph) |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 6) |
| Number of NDAs | at least 6 |
| Number of approvals | At least 6 (1 NDA and 5 ANDAs; the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, temozolomide is an oral alkylating agent that methylates DNA (O6-guanine, N7-guanine, N3-adenine). This causes cytotoxic lesions and apoptosis in tumor cells. It crosses the blood-brain barrier and is used in glial tumors of the brain.

Cauda equina neoplasms are mostly myxopapillary ependymomas, which are glial-lineage tumors of the spinal axis. This gives a plausible biological link to the glial tumors in the original indications. Efficacy likely depends on MGMT promoter methylation status (low MGMT expression predicts sensitivity), which is not reported in the available data.

The high TxGNN score is a computational prediction and does not replace clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Case report | Eur Spine J | Remarkable response to temozolomide in a relapsed spinal myxopapillary ependymoma with multiple recurrences and cerebrospinal dissemination |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Case report | Medicine | Nasal NUT carcinoma managed with multimodal treatment including radiotherapy; not about cauda equina neoplasm |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Case report | Neuro-Chirurgie | Neuromeningeal cryptococcosis in a child treated for pontine glioma; not about cauda equina neoplasm |

Only the first report is closely related to the predicted disease. It describes a single spinal myxopapillary ependymoma, a tumor type that commonly arises in the cauda equina region, and is not a study of cauda equina neoplasm itself. The other two are not relevant to this indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021029 | TEMODAR (Merck Sharp & Dohme LLC) | Capsule | Not stated in the compiled data |
| ANDA207658 | Temozolomide (Devatis, Inc.) | Capsule | Not stated in the compiled data |
| ANDA201742 | Temozolomide (Sun Pharmaceutical Industries, Inc.) | Capsule | Not stated in the compiled data |
| ANDA206309 | Temozolomide (Rising Pharma Holdings, Inc.) | Capsule | Not stated in the compiled data |
| ANDA203691 | Temozolomide (Amneal Pharmaceuticals LLC) | Capsule | Not stated in the compiled data |

At least 6 approvals are on record (the sixth is ANDA213328, Nivagen Pharmaceuticals), and the list may be partial. All are single-ingredient oral capsules.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph links the drug to contraindication relations with several blood disorders (see below). |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication relations in the knowledge graph (not label text):** liver failure, thrombocytopenia, neutropenia, agranulocytosis, anemia, macrocytic anemia, pancytopenia, lymphopenia, myelodysplastic syndrome, idiopathic aplastic anemia, aplastic anemia, pneumocystosis.
- **Drug interactions:** 100 interactions were found in total. Naltrexone is rated Moderate and levofloxacin Minor. The others shown (for example pantoprazole, omeprazole, lansoprazole, morphine, metformin, prednisone, hydrocortisone, doxycycline and amphotericin B) have an unknown severity level.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial is registered for this indication, and the only closely related publication is a single case report on spinal myxopapillary ependymoma. The evidence therefore remains at the model-prediction level (L5), and the high TxGNN score alone is not sufficient to proceed.

**To proceed, the following is needed:**
- Clinical studies directly addressing cauda equina neoplasm or myxopapillary ependymoma treated with temozolomide
- MGMT promoter methylation data for these tumors
- Mechanism-of-action data from DrugBank
- FDA package insert warnings and contraindications for safety screening
- A review of the blood-disorder contraindication relations and a monitoring plan for patients with spinal tumors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

