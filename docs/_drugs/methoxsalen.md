---
layout: default
title: Methoxsalen
parent: Model Prediction Only (L5)
nav_order: 912
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
monitor_inn: "METHOXSALEN"
predicted_indications: ["localized pagetoid reticulosis", "neoplasm of mature B-cells", "small intestinal Burkitt lymphoma", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "breast mucosa-associated lymphoid tissue lymphoma", "tonsillar lymphoma", "vulvar inverted follicular keratosis"]
description: "Methoxsalen: predicted new indication Localized pagetoid reticulosis (evidence level L5). In the US: 6 FDA applications (3 active)"
---

# Methoxsalen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Methoxsalen: Localized pagetoid reticulosis
{: .text-alpha }

## One-Sentence Summary

Methoxsalen (a psoralen) was originally used to treat primary cutaneous T-cell lymphoma and vitiligo.
The TxGNN model predicts it may be effective for **Localized Pagetoid Reticulosis**, an indolent variant of mycosis fungoides.
Currently there are **0 clinical trials** and **0 publications** specific to this disease, so the support is indirect and rests on class-level extrapolation from the established cutaneous T-cell lymphoma use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Localized pagetoid reticulosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 3 of 6) |
| Number of FDA Applications | 6 (active: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of methoxsalen as: DNA inhibitor ([ChEMBL CHEMBL416 (methoxsalen): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL416), CC BY-SA 3.0; accessed 2026-11-19.) Based on known pharmacology, methoxsalen is a psoralen. When activated by UVA light (PUVA), it crosslinks DNA and induces apoptosis of malignant epidermotropic T cells. It is also used in extracorporeal photopheresis, where blood cells are exposed to the drug and UVA outside the body.

Localized pagetoid reticulosis (Woringer-Kolopp disease) is an indolent, epidermotropic variant of mycosis fungoides, which is a primary cutaneous T-cell lymphoma. Because the original indication is the same disease family and the malignant cells sit in the skin, where UVA can reach them, the prediction is biologically plausible. However, this is an extrapolation from the broader indication. No studies specific to this entity were found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for localized pagetoid reticulosis itself. For the second-ranked prediction, indolent primary cutaneous T-cell lymphoma, one related record was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23074497](https://pubmed.ncbi.nlm.nih.gov/23074497/) | 2006 | Review | Ontario Health Technology Assessment Series | Evidence-based analysis of extracorporeal photopheresis for refractory erythrodermic cutaneous T-cell lymphoma and chronic graft-versus-host disease. It is indirect evidence, not specific to the indolent subtype, and dated. |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA202687 | METHOXSALEN | ONESOURCE | Capsule; oral | Valid |
| NDA019600 | OXSORALEN-ULTRA | BAUSCH | Capsule; oral | Valid |
| NDA020969 | UVADEX | THERAKOS DEVELOPMENT | Injectable; injection | Valid |
| ANDA087781 | METHOXSALEN | ANI PHARMS | Capsule; oral | Discontinued in Drugs@FDA |
| ANDA202603 | METHOXSALEN | ACTAVIS INC | Capsule; oral | Discontinued in Drugs@FDA |

Showing 5 of 6 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

Package insert warnings and contraindications were not available. The following come from knowledge-graph contraindication links and drug interaction screening.

- **Contraindications (knowledge graph, not label text)**: Conditions linked to contraindication include:
  - Photosensitivity conditions: photosensitivity disease, photoparoxysmal response, xeroderma pigmentosum
  - Porphyrias: porphyria, variegate porphyria, porphyria cutanea tarda, erythropoietic protoporphyria
  - Skin cancers and melanoma: melanoma, basal cell carcinoma, squamous cell carcinoma, skin carcinoma
  - Systemic lupus erythematosus
  - Liver disease and gallbladder disease
  - Pigmentary disorders: albinism, piebaldism, Waardenburg syndrome, Griscelli syndrome
- **Drug Interactions**: 100 interactions were found, and the 20 shown are all Moderate level. Main groups:
  - Tetracyclines: doxycycline, tetracycline, minocycline
  - Sulfonylureas: glipizide, glyburide, glimepiride, chlorpropamide, tolbutamide, tolazamide, acetohexamide
  - Fluoroquinolone: levofloxacin
  - NSAIDs: ibuprofen, flurbiprofen
  - Others: sulfasalazine, sulfamethizole, promethazine, alosetron

Many of these interactions likely relate to additive photosensitivity, but the data do not state the mechanism.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible because it lies within the cutaneous T-cell lymphoma family where PUVA is established. The package insert safety data are missing, and the knowledge graph flags multiple contraindications, including skin cancers.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A targeted literature search for PUVA in localized pagetoid reticulosis or mycosis fungoides (case series, guidelines)
- Review of the regulatory pathway
- Assessment of long-term PUVA risks, particularly photocarcinogenicity, in the target population

<!-- review:begin us-lic-20261106-methoxsalen-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Review of the regulatory pathway, since both US authorizations are cancelled" Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-methoxsalen-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "since both US authorizations are cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL416 (methoxsalen): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL416) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

