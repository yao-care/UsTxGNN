---
layout: default
title: Lenvatinib
parent: High Evidence (L1-L2)
nav_order: 846
evidence_level: L2
indication_count: 10
monitor_inn: "LENVATINIB"
predicted_indications: ["liposarcoma", "unclassified renal cell carcinoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal cell carcinoma associated with neuroblastoma", "ovarian myxoid liposarcoma", "childhood kidney cell carcinoma", "renal carcinoma", "angiolipoma", "familial spontaneous pneumothorax", "endocrine-cerebro-osteodysplasia syndrome"]
last_modified_at: 2026-10-14
description: "Lenvatinib: predicted new indication Liposarcoma (evidence level L2). Approved use: Renal cell carcinoma and thyroid cancer"
---

# Lenvatinib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Lenvatinib: From Renal Cell Carcinoma and Thyroid Cancer to Liposarcoma

## One-Sentence Summary

Lenvatinib is an oral multi-kinase inhibitor, originally used to treat renal cell carcinoma and thyroid cancer.
The TxGNN model predicts it may be effective for **Liposarcoma**,
with **1 clinical trial** and **4 publications** currently supporting this direction (only 1 of the 4 publications is clinical).

Of the ten predictions, the best-supported is **renal carcinoma**, which is an on-label confirmation rather than true repurposing (see "Other Predictions" below). This report centres on the top-ranked prediction, liposarcoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma and thyroid cancer (the original indication list in the data compiled for this report) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L2 |
| US Market Status | Cancelled only (1 NDA, cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold (treat as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the data compiled for this report. Based on known pharmacology, lenvatinib inhibits VEGFR1-3, FGFR1-4, PDGFRα, RET and KIT. These kinases drive angiogenesis and tumour-stromal signalling, which may also matter in sarcoma.

Its efficacy in renal cell carcinoma and thyroid cancer is established. Liposarcoma is a very different tumour type, so the link is mechanistic rather than based on shared tissue of origin. Eribulin, a microtubule inhibitor, is already established in liposarcoma, and preclinical data suggest it works synergistically with other anticancer agents. A single-arm Phase Ib/II study tested lenvatinib plus eribulin in advanced liposarcoma and leiomyosarcoma.

An important caveat is that there is no randomised comparison. Because lenvatinib was only tested together with eribulin, its own contribution cannot be separated out.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | Completed | 30 | Single-arm LEADER study of lenvatinib plus eribulin in inoperable or metastatic adipocytic sarcoma and leiomyosarcoma; tests safety and efficacy. Non-randomised and combination-based. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase Ib/II single-arm trial | Clin Cancer Res | Lenvatinib plus eribulin in advanced liposarcoma and leiomyosarcoma (LEADER study); the abstract excerpt available describes the study aim, with no results quoted |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical/biomarker | Exp Hematol Oncol | CDK4 as a prognostic biomarker in soft tissue sarcoma; CDK4 inhibition in dedifferentiated liposarcoma (not lenvatinib-specific) |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Res | Eribulin shows broad antitumour activity and combination potential with agents of different mechanisms |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case report | Case Rep Oncol | Tumour shrinkage in dedifferentiated liposarcoma with lung metastasis under individualised treatment |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA206947 | Lenvima (Eisai Inc.) | Capsule | Not listed in the data compiled; status: cancelled |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood pressure, urine protein, liver and renal function, thyroid function, CBC |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. Of those listed, the **Major** ones are **dolasetron** and **cisapride**, which are likely QT-related concerns. Moderate interactions include clarithromycin, levofloxacin, famotidine, loperamide, granisetron, palonosetron, naltrexone, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, sodium sulfate, magnesium citrate and hydroxide, lactulose, lactitol, castor oil, glycerin). Metronidazole is Minor.
- **Known class toxicities** (not from the data compiled, noted for clinical attention): hypertension and proteinuria.

Please refer to the package insert for full warnings and contraindications.

---

## Other Predictions (Brief)

| Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|
| Renal carcinoma | 99.37% | L1 | Supported by the Phase 3 CLEAR trial and a randomised Phase 2 trial. It matches the original indications, so it is an on-label confirmation, not repurposing. Recommendation: Proceed with Guardrails |
| Unclassified renal cell carcinoma | 99.49% | L2 | Phase 2 single-arm trial in non-clear cell RCC plus case reports |
| TFE3-rearranged RCC | 99.49% | L4 | Only a not-yet-recruiting Phase 2 triple-combination trial; no outcome data |
| Ovarian myxoid liposarcoma, childhood kidney cell carcinoma, RCC associated with neuroblastoma, angiolipoma, familial spontaneous pneumothorax, endocrine-cerebro-osteodysplasia syndrome | 99.2%–99.5% | L5 | Computational prediction only; no trials or literature |

---

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
The only direct evidence for liposarcoma is a single-arm Phase Ib/II study of lenvatinib combined with eribulin, so lenvatinib's own contribution is unproven. In addition, the US NDA is listed as cancelled and no package insert safety data are available. This is promising enough to justify further research, but not to proceed.

**To proceed, the following is needed:**
- Efficacy and safety results from the LEADER study, with comparison against eribulin alone (ideally a randomised trial)
- Formal mechanism of action data
- FDA package insert warnings and contraindications, and verification of the cancelled NDA status
- A safety monitoring plan for hypertension, proteinuria and the Major drug interactions (dolasetron, cisapride)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

