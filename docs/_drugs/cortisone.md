---
layout: default
title: Cortisone
parent: Model Prediction Only (L5)
nav_order: 550
evidence_level: L5
indication_count: 9
monitor_inn: "CORTISONE"
predicted_indications: ["primary cutaneous T-cell lymphoma", "adrenocortical insufficiency", "myelodysplastic syndrome", "lymphosarcoma", "candidiasis", "Crohn's colitis", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5"]
last_modified_at: 2026-10-28
description: "Cortisone: predicted new indication primary cutaneous T-cell lymphoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Cortisone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Cortisone: glucocorticoid prodrug (converted to cortisol) → primary cutaneous T-cell lymphoma
{: .text-alpha }

## One-Sentence Summary

Cortisone is a corticosteroid prodrug that the body converts into active cortisol.
The TxGNN model predicts it may be relevant to **primary cutaneous T-cell lymphoma**.
Support is very thin: the data compiled for this report contain **no clinical trial that studies this disease** and **5 publications**, all case reports or reviews from 1951–1964.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the compiled data. Cortisone is known to be a prodrug that requires conversion to cortisol by 11-beta-HSD1.

Glucocorticoids can induce apoptosis in lymphoid cells through the glucocorticoid receptor. This gives a plausible, class-level rationale for activity in T-cell lymphomas.

The only supporting literature is anecdotal. These are mid-20th-century case reports of cortisone given to patients with mycosis fungoides, the most common form of cutaneous T-cell lymphoma. Current practice relies on topical corticosteroids for early-stage disease and other systemic agents for advanced disease. The prediction is therefore mechanistically plausible but clinically unsupported for cortisone itself.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04799275](https://clinicaltrials.gov/study/NCT04799275) | Phase 2/3 | Active, not recruiting | 422 | R-miniCHOP with or without oral azacitidine in adults aged 75 or older with diffuse large B-cell lymphoma. It is not a cutaneous T-cell lymphoma study and does not test cortisone; prednisone is only part of the chemotherapy backbone. |

No registered trial tests cortisone in primary cutaneous T-cell lymphoma. The single trial above is listed only for completeness.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14896727](https://pubmed.ncbi.nlm.nih.gov/14896727/) | 1951 | Case report | Dermatologica | Effects of cortisone in two cases of mycosis fungoides |
| [14884116](https://pubmed.ncbi.nlm.nih.gov/14884116/) | 1951 | Case report | Svenska lakartidningen | Combined ACTH and cortisone therapy in a patient with mycosis fungoides, among other skin conditions |
| [13612293](https://pubmed.ncbi.nlm.nih.gov/13612293/) | 1958 | Case report | Lyon medical | Two mycosis cases treated with delta-cortisone; a terminal ulceronecrotic process was probably linked to the medication |
| [13536705](https://pubmed.ncbi.nlm.nih.gov/13536705/) | 1957 | Case report | Bulletin de la Societe francaise de dermatologie et de syphiligraphie | Two cases of bronchial epithelioma in patients with mycosis fungoides treated with cortisone |
| [14169182](https://pubmed.ncbi.nlm.nih.gov/14169182/) | 1964 | Review | Journal de medecine et de chirurgie pratiques | General review of mycosis fungoides |

These reports have no abstracts available, and none provides controlled evidence. One reports a possible harmful effect of the medication.

## US Market Information

The local data show cortisone as marketed in the United States, with two records covering a pellet and an oral tablet. The compiled data do not carry approved indication text for these products.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score rests on a plausible class-level glucocorticoid mechanism. The clinical support is limited to decades-old case reports, with no trial testing cortisone in this disease. Cortisone also needs hepatic activation, and modern practice favours other agents.

**To proceed, the following is needed:**
- Parsed package insert warnings and contraindications
- Mechanism of action data from DrugBank
- A comparison against current standard therapy for cutaneous T-cell lymphoma, including topical corticosteroids and other glucocorticoids
- Any modern prospective data on glucocorticoids in this disease before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

