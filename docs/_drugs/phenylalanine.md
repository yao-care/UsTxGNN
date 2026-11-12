---
layout: default
title: Phenylalanine
parent: Moderate Evidence (L3-L4)
nav_order: 1041
evidence_level: L4
indication_count: 2
monitor_inn: "PHENYLALANINE"
predicted_indications: ["sclerosing cholangitis", "congenital prothrombin deficiency"]
last_modified_at: 2026-11-12
description: "Phenylalanine: predicted new indication Sclerosing cholangitis (evidence level L4). Approved use: Not available (the approved indication text is empty)"
---

# Phenylalanine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

## Phenylalanine: From an Unspecified Original Indication to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Phenylalanine is an essential amino acid. Its only US authorization in the data compiled for this report is a cancelled liquid product, and no approved indication is recorded.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are **0 clinical trials** and only **3 publications** that are indirectly related, so the prediction is essentially unsupported by clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved indication text is empty) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9943 |
| Evidence Level | L4 |
| US Market Status | Marketed (no FDA-approved application; OTC monograph / unapproved listings: 13) |
| Number of FDA Applications | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenylalanine is an essential aromatic amino acid, and a metabolite of it, tyrosine, has been studied in liver disease. Its original indication is not recorded, so a direct link to the predicted indication cannot be drawn.

The only mechanistic hint in the retrieved literature is a cohort study of plasma tyrosine in primary biliary cirrhosis and primary sclerosing cholangitis. It suggests altered aromatic amino acid metabolism in cholestatic liver disease. This is an association with fatigue, not evidence that phenylalanine treats the disease.

The high TxGNN score (0.9943) is a computational prediction only. No therapeutic rationale has been established, so the prediction should be treated as a hypothesis, not a finding.

A second prediction, **congenital prothrombin deficiency** (score 0.9926), has no clinical trials, no literature, and no known mechanistic link. Phenylalanine is not known to affect prothrombin synthesis or activity. Its evidence level is L5.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined the relation between plasma tyrosine (a phenylalanine metabolite) and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis; it identified amino acid abnormalities but showed no therapeutic benefit |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort | Journal of Clinical and Experimental Hepatology | Serum metabolomic profiling in cholangiocarcinoma versus benign hepatobiliary disease, aimed at pathogenesis and early biomarkers; not a treatment study |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Basic/Other | Journal of Gastroenterology and Hepatology | Radioimmunoassay for a bacterial chemotactic peptide containing phenylalanine, showing enterohepatic circulation; unrelated to phenylalanine therapy |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available (cancelled) | Phenylalanine Phenolic (Energique, Inc.) | Liquid | Not recorded |

---

## Safety Considerations

Package insert warnings and contraindications were not available. No drug interactions were found in the data compiled for this report.

The TxGNN knowledge graph lists the following diseases as contraindication-related to phenylalanine. This is knowledge-graph data, not label text:

- **Phenylketonuria** and other **disorders of phenylalanine metabolism**. Phenylalanine is directly harmful in these conditions.
- **Kidney disease**: chronic kidney disease, chronic renal failure, end-stage renal failure, acute urate nephropathy, nephrolithiasis (including the SLC26A1-related form), nephrocalcinosis and pyoureter.
- **Heart and cardiovascular disease**, including ventricular fibrillation and digitalis poisoning.
- **Calcium and phosphorus disorders**: hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis and phosphorus metabolism disease.

Please refer to the package insert for confirmed safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, the literature is only indirectly related, and no mechanistic rationale exists.

<!-- review:begin us-lic-20261031-phenylalanine-1 -->

> **Review correction (2026-10-31)**: Originally stated: "There are no clinical trials, the literature is only indirectly related, and no mechanistic rationale exists. The only US authorization is cancelled, and package insert safety data are missing, which blocks safety screening." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-10-31). The FDA data list 0 FDA applications or NDC listings for this drug, 0 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261031-phenylalanine-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank, to assess any link to cholestatic liver disease
- Preclinical or clinical studies testing phenylalanine in sclerosing cholangitis
- Review of the knowledge-graph contraindications, especially kidney and cardiovascular disease, against the likely patient population
- Clarification of the original approved indication and the current regulatory and route-of-administration status

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only US authorization is cancelled, and package insert safety data are missing, which blocks safety screening" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

