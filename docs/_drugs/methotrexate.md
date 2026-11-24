---
layout: default
title: Methotrexate
parent: Model Prediction Only (L5)
nav_order: 911
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "METHOTREXATE"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Methotrexate: predicted new indication Pulmonary blastoma (evidence level L5). In the US: 66 FDA applications (29 active)"
---

# Methotrexate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Methotrexate: Pulmonary blastoma
{: .text-alpha }

## One-Sentence Summary

Methotrexate is an antifolate chemotherapy and immunosuppressant, originally used for acute lymphoblastic leukemia, lymphomas, rheumatoid arthritis and psoriasis.
The TxGNN model predicts it may be effective for **pulmonary blastoma**, a rare lung tumor, but **no clinical trials and no publications** were found to support this prediction. It is a model-based hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pulmonary blastoma |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Marketed (active FDA-approved applications: 29 of 66) |
| Number of FDA Applications | 66 (active: 29) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for methotrexate: "Methotrexate inhibits dihydrofolic acid reductase. Dihydrofolates must be reduced to tetrahydrofolates by this enzyme before they can be utilized as carriers of one-carbon groups in the synthesis of purine nucleotides and thymidylate." ([DailyMed: Jylamvo (methotrexate) prescribing information, SHORLA ONCOLOGY INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96e931f5-51ae-4bdf-a441-bb0dd26d4c0e), label version 2026-11-05; accessed 2026-11-19.) Methotrexate is widely known as an antifolate that inhibits dihydrofolate reductase (DHFR). This suppresses purine and thymidine synthesis, which is why it acts on rapidly dividing cells such as leukemic and lymphoid cells. Its efficacy in blood cancers, particularly leukemia and lymphoma, is well established.

Pulmonary blastoma is a rare, fast-growing lung tumor with embryonic-like (blastomatous) cells. In principle, an agent that attacks DNA synthesis in proliferating cells could act on such a tumor. This reasoning is speculative, though. The high TxGNN score (0.9945) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No retrieved clinical or laboratory result supports it, and no methotrexate data specific to this tumor was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The drug is marketed, and the compiled records contain no approved indication text. The five main ones are listed below, with NDAs first.

<!-- review:begin us-lic-20261106-methotrexate-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed, with 13 valid authorizations, and the compiled records contain no approved indication text." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-methotrexate-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA040054 | METHOTREXATE SODIUM | HIKMA | Tablet; oral | Valid |
| ANDA040263 | METHOTREXATE SODIUM | FRESENIUS KABI USA | Injectable; injection | Valid |
| ANDA040266 | METHOTREXATE PRESERVATIVE FREE | FRESENIUS KABI USA | Injectable; injection | Valid |
| ANDA040385 | TREXALL | BARR | Tablet; oral | Valid |
| ANDA040632 | METHOTREXATE SODIUM PRESERVATIVE FREE | HIKMA | Injectable; injection | Valid |

Showing 5 of 66 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

The records also include tablet, solution and lyophilized-powder generics from other manufacturers.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, antifolate class) |
| Myelosuppression Risk | High, especially at higher doses (leukopenia, thrombocytopenia and anemia appear among the knowledge-graph contraindications) |
| Emetogenicity Classification | Low to moderate, dose-dependent |
| Monitoring Items | CBC with differential, liver and renal function, pulmonary symptoms, mucositis/stomatitis |
| Handling Protection | Must follow cytotoxic drug handling regulations. Please refer to the package insert warnings and precautions for details. |

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** liver failure and liver disease, kidney disease, thrombocytopenia, leukopenia, anemia (including macrocytic anemia), interstitial lung disease, pulmonary fibrosis, stomatitis, peptic and gastric ulcer disease, ulcerative colitis and inflammatory bowel disease, gallbladder disease, pyoureter, substance abuse/dependence, and immune system disease.
- **Drug Interactions:** 100 interactions were recorded. The **major** ones include:
  - rabeprazole
  - amoxicillin
  - acetylsalicylic acid (aspirin)

  Many **moderate** ones were also listed, including:
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - tetracyclines (doxycycline, tetracycline)
  - clarithromycin
  - amphotericin B
  - mesalazine and balsalazide
  - pioglitazone
  - bupropion

Please refer to the package insert for the full official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for pulmonary blastoma rests solely on the model score, with no trials or publications behind it.

For context, two other predictions in the same run have somewhat more support, both at evidence level L3:
- **Hodgkin lymphoma:** the vinblastine-bleomycin-methotrexate (VBM) regimen has been studied in early-stage disease.
- **Rhabdomyosarcoma:** a Phase 2 trial of high-dose methotrexate was run in children with advanced disease.

Neither has a Phase 3 RCT directly supporting it.

**To proceed, the following is needed:**
- A systematic search for case reports or series on methotrexate-containing regimens in pulmonary blastoma, including related pleuropulmonary blastoma
- Detailed mechanism of action data (MOA) and FDA package insert warnings and contraindications
- Confirmation of current US marketing status and a suitable available formulation
- A safety and dosing plan covering myelosuppression, hepatic and renal function, and pulmonary toxicity

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "with 13 valid authorizations" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Jylamvo (methotrexate) prescribing information, SHORLA ONCOLOGY INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96e931f5-51ae-4bdf-a441-bb0dd26d4c0e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

