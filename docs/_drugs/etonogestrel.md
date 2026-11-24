---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 684
evidence_level: L5
indication_count: 5
monitor_inn: "ETONOGESTREL"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia"]
last_modified_at: 2026-11-24
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Etonogestrel: From Contraception to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Etonogestrel is a progestin that has been marketed in the US in contraceptive implant and vaginal ring products.
The TxGNN model predicts it may be effective for **amenorrhea**, but **no clinical trials** and **only 1 publication (unrelated to this topic)** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available regulatory data (marketed as a hormonal contraceptive implant and ring) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 6 of 7) |
| Number of FDA Applications | 7 (active: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for etonogestrel: "The contraceptive effect of NEXPLANON is achieved by suppression of ovulation, increased viscosity of the cervical mucus, and alterations in the endometrium." ([DailyMed: Nexplanon (etonogestrel) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=487f8a62-e142-457c-97cc-2e398fde7594), label version 2026-05-28; accessed 2026-11-19.) Based on known pharmacology, etonogestrel is a progestin (the active metabolite of desogestrel) that suppresses ovulation and causes endometrial atrophy.

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

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA021529 | NEXPLANON | ORGANON | Implant; implantation | Valid |
| ANDA204305 | ETHINYL ESTRADIOL; ETONOGESTREL | TEVA PHARMS USA INC | Ring; vaginal | Valid |
| ANDA210830 | ELURYNG | AMNEAL | Ring; vaginal | Valid |
| ANDA211157 | ENILLORING | XIROMED | Ring; vaginal | Valid |
| ANDA211328 | HALOETTE | DR REDDYS LABS SA | Ring; vaginal | Valid |

Showing 5 of 7 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

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
The prediction is supported only by the model score (L5). There are no relevant trials or literature. Amenorrhea is an expected side effect of the drug rather than an established treatment target.

<!-- review:begin us-lic-20261105-etonogestrel-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Amenorrhea is an expected side effect of the drug rather than an established treatment target. The drug is marketed in the US, with all four licenses valid, and label safety data are missing." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-etonogestrel-1 -->

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (required before any safety screening)
- Mechanism of action data from DrugBank
- Clinical or observational evidence on etonogestrel for therapeutic menstrual suppression
- Review of the knowledge-graph contraindication signals (cardiovascular, metabolic, hepatic, breast cancer) against the intended patient population
- Confirmation of route and product availability

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "The drug is marketed in the US, with all four licenses valid, and label safety data are missing" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nexplanon (etonogestrel) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=487f8a62-e142-457c-97cc-2e398fde7594) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

