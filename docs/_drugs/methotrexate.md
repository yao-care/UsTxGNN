---
layout: default
title: Methotrexate
parent: Model Prediction Only (L5)
nav_order: 911
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methotrexate: predicted new indication Pulmonary blastoma (evidence level L5). Approved use: Acute lymphoblastic leukemia, non-Hodgkin lymphoma, mycosis fungoides…"
monitor_inn: "METHOTREXATE"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Methotrexate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Methotrexate: From Acute Lymphoblastic Leukemia to Pulmonary Blastoma
{: .text-alpha }

## One-Sentence Summary

Methotrexate is an antifolate chemotherapy and immunosuppressant, originally used for acute lymphoblastic leukemia, lymphomas, rheumatoid arthritis and psoriasis.
The TxGNN model predicts it may be effective for **pulmonary blastoma**, a rare lung tumor, but **no clinical trials and no publications** were found to support this prediction. It is a graph-based hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia, non-Hodgkin lymphoma, mycosis fungoides, rheumatoid arthritis, psoriasis (the US license records compiled here contain no indication text, so these come from the TxGNN knowledge graph) |
| Predicted New Indication | Pulmonary blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (all 13 authorizations are cancelled; none currently valid in the compiled records) |
| Number of NDAs | 13 authorizations in total (3 NDAs and 10 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Methotrexate is widely known as an antifolate that inhibits dihydrofolate reductase (DHFR). This suppresses purine and thymidine synthesis, which is why it acts on rapidly dividing cells such as leukemic and lymphoid cells. Its efficacy in blood cancers, particularly leukemia and lymphoma, is well established.

Pulmonary blastoma is a rare, fast-growing lung tumor with embryonic-like (blastomatous) cells. In principle, an agent that attacks DNA synthesis in proliferating cells could act on such a tumor. This reasoning is speculative, though. The high TxGNN score reflects a pattern in the knowledge graph, not any retrieved clinical or laboratory result, and no methotrexate data specific to this tumor was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

All 13 authorizations are cancelled, and the compiled records contain no approved indication text. The five main ones are listed below, with NDAs first.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA208400 | Xatmep (Azurity Pharmaceuticals) | Solution | Cancelled |
| NDA205776 | Rasuvo (Medexus Pharma) | Injection, solution | Cancelled |
| NDA011719 | Methotrexate (Hospira) | Injection, solution | Cancelled |
| ANDA040385 | Trexall (Teva Women's Health) | Tablet, film coated | Cancelled |
| ANDA040716 | Methotrexate (Accord Healthcare) | Injection | Cancelled |

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
The prediction for pulmonary blastoma rests solely on the model score, with no trials or publications behind it. Methotrexate also carries substantial toxicity, and none of its US authorizations are currently valid.

For context, two other predictions in the same run have somewhat more support, both at evidence level L3:
- **Hodgkin lymphoma:** the vinblastine-bleomycin-methotrexate (VBM) regimen has been studied in early-stage disease.
- **Rhabdomyosarcoma:** a Phase 2 trial of high-dose methotrexate was run in children with advanced disease.

Neither has a Phase 3 RCT directly supporting it.

**To proceed, the following is needed:**
- A systematic search for case reports or series on methotrexate-containing regimens in pulmonary blastoma, including related pleuropulmonary blastoma
- Detailed mechanism of action data (MOA) and FDA package insert warnings and contraindications
- Confirmation of current US marketing status and a suitable available formulation
- A safety and dosing plan covering myelosuppression, hepatic and renal function, and pulmonary toxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

