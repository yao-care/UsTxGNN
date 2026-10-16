---
layout: default
title: Cortisone
parent: Model Prediction Only (L5)
nav_order: 550
evidence_level: L5
indication_count: 9
monitor_inn: "CORTISONE"
predicted_indications: ["primary cutaneous T-cell lymphoma", "adrenocortical insufficiency", "myelodysplastic syndrome", "lymphosarcoma", "candidiasis", "Crohn's colitis", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5"]
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Cortisone: From Unspecified Labeled Indication to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Cortisone is a corticosteroid (glucocorticoid) prodrug. Its US labeled indication text is not available in the data compiled for this report, though it has historically been used as a replacement and anti-inflammatory steroid.
The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma**, but **no relevant clinical trial** tests cortisone for this disease, and the only literature is **5 publications**, mostly 1950s-1960s case reports.
Evidence for this top prediction is weak. The best-supported alternative among the predictions is adrenocortical insufficiency, and that support is class-level only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (indication text blank on both licenses) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 (no cortisone trials, only historical case reports) |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From general pharmacology, cortisone is an inactive prodrug converted to cortisol by 11-beta-hydroxysteroid dehydrogenase type 1 (11-beta-HSD1). Cortisol acts on the glucocorticoid receptor.

Glucocorticoids induce apoptosis in lymphoid cells through this receptor, which gives a plausible mechanism for activity in T-cell lymphomas. However, the supporting literature consists only of 1950s-1960s case reports in mycosis fungoides, which are anecdotal. Modern practice uses topical corticosteroids for early-stage disease and other systemic agents for advanced disease. The prediction is therefore mechanistically plausible at the class level but not supported by cortisone-specific modern evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04799275](https://clinicaltrials.gov/study/NCT04799275) | Phase 2/3 | Active, not recruiting | 422 | R-miniCHOP with or without oral azacitidine in patients ≥75 years with diffuse large B-cell lymphoma. Not a cutaneous T-cell lymphoma study and does not test cortisone (prednisone is part of the CHOP backbone). |

The only trial retrieved has low relevance to the predicted indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14896727](https://pubmed.ncbi.nlm.nih.gov/14896727/) | 1951 | Case report | Dermatologica | Effects of cortisone in two cases of mycosis fungoides |
| [14884116](https://pubmed.ncbi.nlm.nih.gov/14884116/) | 1951 | Case report | Svenska lakartidningen | Combined ACTH and cortisone therapy in impetigo herpetiformis, mycosis fungoides and erythroderma psoriatica |
| [13612293](https://pubmed.ncbi.nlm.nih.gov/13612293/) | 1958 | Case report | Lyon medical | Two mycosis cases treated with delta-cortisone; terminal ulceronecrotic process probably related to the medication |
| [13536705](https://pubmed.ncbi.nlm.nih.gov/13536705/) | 1957 | Case report | Bull Soc Fr Dermatol Syphiligr | Two cases of bronchial epithelioma in mycosis fungoides patients treated with cortisone |
| [14169182](https://pubmed.ncbi.nlm.nih.gov/14169182/) | 1964 | Review | J Med Chir Prat | General review of mycosis fungoides (no abstract available) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA080694 (cancelled) | Cortisone Acetate (Chartwell RX, LLC) | Tablet | Not available |
| Number not available (cancelled) | Cortisone aceticum (Boiron) | Pellet | Not available |

## Safety Considerations

Please refer to the package insert for safety information. Package insert warnings and contraindications are not available in the data compiled for this report, and no drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has only historical case reports and no relevant trials. Cortisone has no currently valid US license, and modern practice uses other agents for cutaneous T-cell lymphoma. The glucocorticoid mechanism is plausible, but it is a class-level argument.

**Context from other predictions:**
- **Adrenocortical insufficiency** has the strongest supporting evidence among the predictions (two completed Phase 3/4 RCTs). Both compare dual-release hydrocortisone with conventional glucocorticoids, not cortisone itself. It supports the glucocorticoid-replacement class and would be a class-evidence conclusion (Proceed with Guardrails), since hydrocortisone is now preferred and cortisone is no longer marketed.
- **Lymphosarcoma**, **Crohn's colitis**: class-level plausibility only, with no cortisone-specific trials. Hold.
- **Myelodysplastic syndrome** and related predictions (refractory cytopenia of childhood, unclassified MDS, del(5q)): no mechanistic rationale or evidence. Hold.
- **Candidiasis**: cortisone is used to induce Candida infection in animal models, so the signal suggests harm, not benefit.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications (currently missing; blocks safety screening)
- Detailed mechanism of action data from DrugBank
- Cortisone-specific clinical data, or a decision to use a modern glucocorticoid (e.g., hydrocortisone, prednisone) as the repurposing candidate instead
- Route and formulation compatibility assessment for the target indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

