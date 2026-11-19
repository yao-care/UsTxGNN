---
layout: default
title: Letrozole
parent: Model Prediction Only (L5)
nav_order: 848
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-06
monitor_inn: "LETROZOLE"
predicted_indications: ["nipple carcinoma", "Ehrlich tumor carcinoma", "breast fibrocystic disease", "benign mammary dysplasia"]
description: "Letrozole: predicted new indication Nipple carcinoma (evidence level L5). In the US: 23 FDA applications (9 active)"
---

# Letrozole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Letrozole: Nipple carcinoma
{: .text-alpha }

## One-Sentence Summary

Letrozole is an oral aromatase inhibitor that lowers estrogen production.
The TxGNN model predicts it may be useful for **nipple carcinoma**, but the evidence is thin. There are **0 clinical trials** and **8 publications**, and none of the publications tests letrozole in this disease. The evidence level is therefore **L5**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nipple carcinoma |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 9 of 23) |
| Number of FDA Applications | 23 (active: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for letrozole: "The growth of some cancers of the breast is stimulated or maintained by estrogens. Treatment of breast cancer thought to be hormonally responsive (i.e., estrogen and/or progesterone receptor positive or receptor unknown) has included a variety of efforts to decrease estrogen levels (ovariectomy, adrenalectomy, hypophysectomy) or inhibit estrogen effects (antiestrogens and progestational agents). […] Letrozole is a nonsteroidal competitive inhibitor of the aromatase enzyme system; it inhibits the conversion of androgens to estrogens." ([DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406), label version 2026-06-11; accessed 2026-11-19.) Letrozole belongs to the aromatase inhibitor class. These drugs block the conversion of androgens to estrogens, which deprives hormone-dependent tumours of their growth signal.

Nipple carcinoma is a form of breast cancer arising in or near the nipple. If a tumour is hormone receptor-positive, estrogen suppression is mechanistically plausible. This link is an extrapolation from general breast cancer biology. No cited study tested letrozole in nipple carcinoma, so the prediction rests on the model score and mechanistic reasoning alone.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these publications studies letrozole in nipple carcinoma. They are case reports or small series on rare breast tumour presentations. They are listed because the search linked them to this disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33120755](https://pubmed.ncbi.nlm.nih.gov/33120755/) | 2020 | Cohort/case report | Medicine | Neoadjuvant endocrine therapy in poorly differentiated neuroendocrine carcinoma of the breast. This is only indirectly relevant. |
| [41607681](https://pubmed.ncbi.nlm.nih.gov/41607681/) | 2026 | Case report | Clinical Case Reports | Solid papillary carcinoma in situ arising in the nipple of a 73-year-old woman. It highlights the lack of standard diagnostic and treatment guidance. |
| [40395253](https://pubmed.ncbi.nlm.nih.gov/40395253/) | 2025 | Case report | Cureus | Axillary recurrence after breast cancer that presented with bloody nipple discharge. |
| [42040393](https://pubmed.ncbi.nlm.nih.gov/42040393/) | 2026 | Case report | Clinical Case Reports | Tall cell carcinoma of the breast with reverse polarity and an IDH1 R132 mutation. The patient presented with a breast mass and nipple discharge. |
| [42416948](https://pubmed.ncbi.nlm.nih.gov/42416948/) | 2026 | Case report | Cureus | Imaging features of florid lobular carcinoma in situ on ultrasound. |
| [34495428](https://pubmed.ncbi.nlm.nih.gov/34495428/) | 2021 | Case report | Surgical Case Reports | Rare accessory breast cancer in the inframammary region, with literature review. |
| [39682607](https://pubmed.ncbi.nlm.nih.gov/39682607/) | 2024 | Case report | Diagnostics (Basel) | Synchronous metastatic infra-mammary accessory breast cancer and ipsilateral breast cancer. |
| [42305961](https://pubmed.ncbi.nlm.nih.gov/42305961/) | 2026 | Case report | Frontiers in Medicine | Synchronous accessory breast cancer, papillary thyroid carcinoma and nasal papilloma. |

## US Market Information

Letrozole is currently marketed in the United States, and the licence records show valid status. The list below shows five of the licences on record and may be partial. Approved-indication text is not recorded in the local data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020726 | Femara (Novartis) | Tablet, film coated | Not available in compiled data |
| ANDA205869 | Letrozole (Avet Pharmaceuticals) | Tablet, film coated | Not available in compiled data |
| ANDA211717 | Letrozole (Aurobindo Pharma) | Tablet, film coated | Not available in compiled data |
| ANDA090289 | Letrozole (Proficient Rx) | Tablet, film coated | Not available in compiled data |
| ANDA090934 | Letrozole (Bryant Ranch Prepack) | Tablet, film coated | Not available in compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (endocrine) therapy, not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; bone health and liver function are commonly followed with estrogen-lowering therapy |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Package-insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

**Drug Interactions**: The interaction screen returned 100 potentially interacting drugs. The only one with a severity rating is **aprepitant** (Moderate). Others, including calcitriol, glimepiride, lansoprazole, omeprazole, pantoprazole, famotidine, metformin, simvastatin, prednisone and morphine, are flagged with an unknown severity level and need review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9976), but no clinical trial exists and no publication tests letrozole in nipple carcinoma. The evidence level is L5. Any benefit would be extrapolated from general hormone receptor-positive breast cancer data.

**To proceed, the following is needed:**
- Studies or case series that directly evaluate letrozole in nipple carcinoma, including hormone receptor status of the tumours
- Detailed mechanism of action data
- Package insert warnings and contraindications to complete the safety review
- Review of the flagged drug interactions, especially those with unknown severity

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data were not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

