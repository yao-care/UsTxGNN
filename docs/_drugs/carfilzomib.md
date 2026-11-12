---
layout: default
title: Carfilzomib
parent: Model Prediction Only (L5)
nav_order: 499
evidence_level: L5
indication_count: 5
monitor_inn: "CARFILZOMIB"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma"]
last_modified_at: 2026-11-12
description: "Carfilzomib: predicted new indication CMM7 (a melanoma-related subtype) (evidence level L5). Approved use: Plasma cell myeloma"
---

# Carfilzomib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Carfilzomib: From Plasma Cell Myeloma to CMM7
{: .text-alpha }

## One-Sentence Summary

Carfilzomib is a proteasome inhibitor, originally used to treat plasma cell myeloma (multiple myeloma).
The TxGNN model predicts it may be effective for **melanoma** (and several melanoma subtypes), but the evidence is limited to **0 clinical trials** and **4 publications**, all preclinical or computational.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasma cell myeloma |
| Predicted New Indication | CMM7 |
| TxGNN Prediction Score | 0.9937 (CMM7); melanoma: 0.9903 |
| Evidence Level | L5 for CMM7; L4 for melanoma |
| US Market Status | Marketed (active FDA-approved applications: 4 of 7) |
| Number of FDA Applications | 7 (active: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, carfilzomib is a proteasome inhibitor. It is used in plasma cell myeloma, and proteasome inhibition disrupts protein homeostasis and can induce apoptosis in cancer cells. This mechanism may in theory also apply to melanoma.

The only direct supporting finding is preclinical. A 2021 study showed that carfilzomib combined with bortezomib increased apoptotic cell death in B16-F1 mouse melanoma cells. The other retrieved papers are computational docking work or indirect mechanistic studies, and they provide only weak support.

Several of the predicted subtypes carry additional biological concerns:
- **Pediatric leptomeningeal melanoma:** Carfilzomib is expected to penetrate the central nervous system poorly, so activity against leptomeningeal disease is doubtful.
- **Epithelioid cell uveal melanoma:** Uveal melanoma is biologically distinct from cutaneous melanoma (GNAQ/GNA11-driven), so cutaneous findings cannot be extrapolated.
- **Vulvar melanoma:** Mucosal melanoma differs biologically from cutaneous melanoma, and no direct data exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The table below covers melanoma (the only prediction with literature). The other predicted subtypes have no retrieved publications.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro preclinical study | Biology | Carfilzomib plus bortezomib induced apoptosis in B16-F1 melanoma cells, with activation of caspases 3, 8, 9 and 12 |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational study | J Biomol Struct Dyn | Docking and dynamics simulations for repurposing clinical drugs against kinase targets across ten cancer types, including melanoma |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclinical mechanistic study (indirect) | Mol Cancer Res | ZAN2a gene regulates cell survival in human melanoma via the E3 ligase cIAP2; indirect relevance |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical mechanistic study (indirect) | Matrix Biol | Bortezomib and carfilzomib activate NF-κB and induce heparanase expression, which is linked to a more aggressive tumour phenotype |

---

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA209422 | CARFILZOMIB | DR REDDYS | Powder; intravenous | Valid |
| ANDA209526 | CARFILZOMIB | MSN | Powder; intravenous | Valid |
| NDA202714 | KYPROLIS | ONYX PHARMS AMGEN | Powder; intravenous | Valid |
| NDA220712 | KITPROZY | AMNEAL PHARMS NY | Vial; single-use | Valid |
| ANDA209330 | CARFILZOMIB | BRECKENRIDGE | Powder; intravenous | Discontinued in Drugs@FDA |

Showing 5 of 7 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; routine monitoring would typically include CBC, and liver and renal function |
| Handling Protection | Please refer to the package insert; follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

- **Drug Interactions:** The interaction screen returned 100 interactions in total. The 20 retrieved entries include the following.
  - **Major:** oxandrolone, oxymetholone, stanozolol, deferiprone, samarium (153Sm) lexidronam, avatrombopag, aminocaproic acid, recombinant antihemophilic factor, von Willebrand factor, human C1-esterase inhibitor, conestat alfa, recombinant coagulation factor VIIa, and human coagulation factor X.
  - **Moderate:** metronidazole, tinidazole, naltrexone, rosuvastatin, simvastatin, palifermin, and strontium chloride Sr-89.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions are supported only by a very high model score. For melanoma, the evidence is limited to preclinical and computational studies (L4), and there are no human efficacy or safety data. The drug interaction burden is large.

<!-- review:begin us-lic-20261106-carfilzomib-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The registered product is also cancelled in the US, and the drug interaction burden is large." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 7 FDA applications or NDC listings for this drug, 4 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-carfilzomib-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Dedicated preclinical studies in the specific melanoma subtype (cutaneous, uveal, mucosal), including in vivo models
- For the leptomeningeal indication, data on CNS penetration
- Clarification of the availability of current products

<!-- review:begin us-lic-20261106-carfilzomib-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the cancelled US market status and the availability of current products" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 7 FDA applications or NDC listings for this drug, 4 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-carfilzomib-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "he registered product is also cancelled in the US, and t" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "the cancelled US market status and" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

