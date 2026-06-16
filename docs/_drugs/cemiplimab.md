---
layout: default
title: Cemiplimab
parent: 僅模型預測 (L5)
nav_order: 511
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

Using the `txgnn-pipeline` skill to confirm context. Now generating the report based on the Evidence Pack.

---

# Cemiplimab: From Cutaneous Squamous Cell Carcinoma to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab (Libtayo) is a PD-1 immune checkpoint inhibitor with established FDA approvals for cutaneous squamous cell carcinoma (CSCC), basal cell carcinoma (BCC), and non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Gallbladder Adenosquamous Carcinoma** as the top-ranked indication among 10 predicted targets, with **0 clinical trials** and **0 publications** currently supporting this specific disease; the most actionable finding in this multi-indication pack is **External Ear Basal Cell Carcinoma (Rank 4)**, backed by a published case report and cemiplimab's existing BCC approval.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cutaneous squamous cell carcinoma; basal cell carcinoma; NSCLC *(known from public record; not captured in current US dataset)* |
| Predicted New Indication (Top) | Gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 — model prediction only, no supporting studies |
| US Market Status | Not found in dataset *(Note: Libtayo® is FDA-approved; likely a data collection gap)* |
| Number of NDAs | 0 (in dataset) |
| Recommended Decision | Hold (top indication); Proceed with Guardrails (Rank 4 — External Ear BCC) |

---

## Why is This Prediction Reasonable?

Cemiplimab is a fully human monoclonal antibody that selectively targets PD-1 (Programmed Death-1) on T cells, blocking its interaction with the ligands PD-L1 and PD-L2. This prevents tumor-mediated T-cell exhaustion and reactivates cytotoxic anti-tumor immunity. The drug has demonstrated clinical efficacy across multiple squamous cell carcinoma subtypes — CSCC (approved 2018), BCC (approved 2021), and squamous-predominant NSCLC (approved 2021) — establishing a strong class signal for SCC-related malignancies.

Gallbladder adenosquamous carcinoma is an extremely rare mixed-histology tumor combining both adenocarcinoma and squamous cell carcinoma components. In theory, PD-1 inhibitors possess mechanistic rationale against both components. The TxGNN model likely infers this from cemiplimab's demonstrated breadth of SCC activity. However, gallbladder adenosquamous carcinoma accounts for only a tiny fraction of biliary tract cancers, PD-L1 expression data for this specific subtype is virtually absent from the literature, and the biliary tract immunosuppressive microenvironment further complicates extrapolation.

For the broader set of 10 predictions, the mechanistic logic is most compelling for squamous cell carcinoma subtypes within the head-neck (HNSCC) spectrum — including glottis SCC, supraglottis SCC, sinonasal SCC, and lung occult SCC — where class-level evidence from pembrolizumab and nivolumab provides indirect support. The external ear BCC prediction (Rank 4) is particularly well-grounded: cemiplimab is already approved for BCC regardless of anatomic site, and a published case report documents lasting response in locally advanced BCC.

---

## All Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Gallbladder adenosquamous carcinoma | 99.99% | L5 | Hold |
| 2 | Glottis squamous cell carcinoma | 99.99% | L4 | Research Question |
| 3 | Rectal cloacogenic carcinoma | 99.99% | L5 | Hold |
| **4** | **External ear basal cell carcinoma** | **99.99%** | **L3** | **Proceed with Guardrails** |
| 5 | Adenosquamous prostate carcinoma | 99.99% | L5 | Hold |
| 6 | Urethral verrucous carcinoma | 99.99% | L5 | Hold |
| 7 | Lung occult squamous cell carcinoma | 99.99% | L4 | Research Question |
| 8 | Pancreatic adenosquamous carcinoma | 99.99% | L5 | Hold |
| 9 | Non-keratinizing sinonasal squamous cell carcinoma | 99.99% | L4 | Research Question |
| 10 | Supraglottis squamous cell carcinoma | 99.99% | L4 | Research Question |

> **Most actionable: Rank 4 — External ear basal cell carcinoma.** Cemiplimab is already FDA-approved for BCC; this is a site-specific subtype covered by the existing indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for **gallbladder adenosquamous carcinoma** with cemiplimab.

No clinical trials were identified for any of the 10 predicted indications in the current dataset.

---

## Literature Evidence

No literature found for the top-ranked indication (gallbladder adenosquamous carcinoma).

**Most relevant literature identified in this pack — Rank 4 (External Ear BCC):**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34157152](https://pubmed.ncbi.nlm.nih.gov/34157152/) | 2021 | Case Report | Clinical and Experimental Dermatology | Reports lasting response after cemiplimab discontinuation in a patient with locally advanced BCC, supporting durable PD-1 blockade effects in this histology |

---

## US Market Information

No authorization records found in the current dataset (0 NDAs).

> **Data Discrepancy Notice**: Cemiplimab (Libtayo®, Regeneron/Sanofi) holds confirmed FDA approvals for CSCC (September 2018), BCC (February 2021), and NSCLC (February 2021). The absence of records in this dataset reflects a known data collection gap (DG001/DG002) rather than the actual US regulatory status. US prescribing information should be retrieved directly from FDA.gov before proceeding with any clinical decision.

---

## Cytotoxicity

Cemiplimab is an antineoplastic agent (cancer treatment); this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Anti-PD-1 monoclonal antibody (not conventional cytotoxic) |
| Myelosuppression Risk | Low; immune-mediated hematologic events (e.g., immune thrombocytopenia, hemolytic anemia) are possible but uncommon |
| Emetogenicity Classification | Minimal — not a direct cytotoxic mechanism; nausea is uncommon |
| Monitoring Items | LFTs, thyroid function (TSH/FT4), fasting glucose, cortisol, creatinine, CBC with differential; monitor for signs of immune-related adverse events (irAEs) at each cycle |
| Handling Protection | Standard biologic/monoclonal antibody handling procedures; dedicated cytotoxic chemotherapy containment protocols are not required |

---

## Safety Considerations

Please refer to the package insert for complete safety information.

> As a PD-1 checkpoint inhibitor, cemiplimab carries a class risk of **immune-related adverse events (irAEs)**, which can affect any organ system. Clinically significant irAEs include immune-mediated pneumonitis, colitis, hepatitis, endocrinopathies (hypothyroidism, hyperthyroidism, adrenal insufficiency, type 1 diabetes), nephritis, and severe dermatologic reactions. Specific contraindications, warnings, and management algorithms should be confirmed via the current FDA prescribing information (Libtayo® label), which could not be retrieved in the current data run.

---

## Conclusion and Next Steps

### Primary Decision (Rank 1 — Gallbladder Adenosquamous Carcinoma)

**Decision: Hold**

**Rationale:**
Gallbladder adenosquamous carcinoma is an extremely rare malignancy with no available PD-L1 expression characterization and no clinical experience with checkpoint inhibitors in this specific subtype. The TxGNN prediction is a computational hypothesis; advancing it without preclinical validation would not be justified.

---

### Highest-Priority Actionable Opportunity (Rank 4 — External Ear BCC)

**Decision: Proceed with Guardrails**

**Rationale:**
Cemiplimab is already FDA-approved for BCC; the external ear is an anatomic subtype within the existing approved indication. A published case report (PMID 34157152) documents lasting response in locally advanced BCC, directly relevant to this prediction.

---

### To proceed with the full repurposing pipeline, the following is needed:

- **Resolve US market data gap**: Populate FDA approval records for Libtayo® (CSCC, BCC, NSCLC) to enable accurate regulatory context in future reports
- **Retrieve MOA data from DrugBank** (DG002): Required for mechanism-level repurposing analysis
- **Retrieve TFDA/FDA prescribing information** (DG001): Required for S1 safety screening
- **L4 Research Questions** (Ranks 2, 7, 9, 10 — HNSCC-spectrum SCC subtypes): Evaluate feasibility as exploratory cohorts within existing HNSCC basket trial protocols; search for pembrolizumab/nivolumab data as class-level surrogates
- **L5 Hold predictions** (Ranks 1, 3, 5, 6, 8 — rare/mixed histologies): Require PD-L1 IHC, TMB profiling, and immune microenvironment characterization from tissue biobanks before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

