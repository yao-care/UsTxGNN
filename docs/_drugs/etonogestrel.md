---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 684
evidence_level: L5
indication_count: 5
monitor_inn: "ETONOGESTREL"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia"]
last_modified_at: 2026-10-14
description: "Etonogestrel: predicted new indication Amenorrhea (evidence level L5). Approved use: Not stated in the available regulatory data (marketed as a hormonal c…"
---

# Etonogestrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a progestin that has been marketed in the US in contraceptive implant and vaginal ring products.
The TxGNN model predicts it may be effective for **amenorrhea**, but **no clinical trials** and **only 1 publication (unrelated to this topic)** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available regulatory data (marketed as a hormonal contraceptive implant and ring) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, etonogestrel is a progestin (the active metabolite of desogestrel) that suppresses ovulation and causes endometrial atrophy.

Amenorrhea is a well-recognised effect of etonogestrel-releasing implants, so a biological link is plausible. However, it is an expected side effect rather than a validated therapeutic goal. The use of etonogestrel for deliberate menstrual suppression has not been formally studied in the data reviewed. The model score is a prediction only.

Other predicted indications are all benign breast conditions (fibrocystic disease, apocrine adenosis, blunt duct adenosis, benign mammary dysplasia). They share a hormonal-pathway rationale, but there are no trials or literature for any of them. Several appear to derive from shared ontology parents, and progestin-only contraceptives can cause breast tenderness, so the direction of effect is uncertain.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT protocol (unrelated topic) | Trials | Study protocol for BIO101 in COVID-19 pneumonia; not relevant to etonogestrel or amenorrhea |

No relevant literature on etonogestrel for amenorrhea was identified.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021529 | Nexplanon | Implant | Not available (status: cancelled) |
| ANDA211157 | EnilloRing | Ring | Not available (status: cancelled) |
| NDA021187 | Etonogestrel/Ethinyl Estradiol | Extended-release insert | Not available (status: cancelled) |
| ANDA210830 | EluRyng | Ring | Not available (status: cancelled) |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: The TxGNN knowledge graph lists contraindication links with the following conditions:
  - Cardiovascular and metabolic: hypertension, coronary artery disease, thrombophlebitis, diabetes mellitus and diabetic ketoacidosis, hyperlipidemia, hypertriglyceridemia, obesity
  - Hepatic, renal and biliary: liver disease, gallbladder disease, kidney disease
  - Neurological and psychiatric: epilepsy, migraine, anxiety disorder, neurotic disorder, dysthymic disorder
  - Other: female breast carcinoma, systemic lupus erythematosus, asthma, porphyria
- **Drug Interactions**: 100 interactions were found, with the 20 shown in the data all rated Moderate. The main ones fall into these groups:
  - Antidiabetic agents (e.g., acarbose, metformin, glimepiride, chlorpropamide, canagliflozin, dapagliflozin, empagliflozin, alogliptin, saxagliptin, semaglutide, dulaglutide, albiglutide, and several insulins)
  - Others: aprepitant, clarithromycin, linaclotide

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no relevant trials or literature. Amenorrhea is an expected side effect of the drug rather than an established treatment target. All four US licenses are cancelled, and label safety data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (required before any safety screening)
- Mechanism of action data from DrugBank
- Clinical or observational evidence on etonogestrel for therapeutic menstrual suppression
- Review of the knowledge-graph contraindication signals (cardiovascular, metabolic, hepatic, breast cancer) against the intended patient population
- Confirmation of route and product availability, since all current US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

