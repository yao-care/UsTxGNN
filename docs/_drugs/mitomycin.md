---
layout: default
title: Mitomycin
parent: Model Prediction Only (L5)
nav_order: 936
evidence_level: L5
indication_count: 10
monitor_inn: "MITOMYCIN"
predicted_indications: ["solid pseudopapillary carcinoma of pancreas", "osteoclastic giant cell tumor of pancreas", "pancreatic carcinoma with mixed differentiation", "pancreatic intraductal papillary-mucinous carcinoma", "mixed ductal-endocrine carcinoma of pancreas", "pancreatic signet ring cell adenocarcinoma", "undifferentiated pancreatic carcinoma", "malignant exocrine pancreas neoplasm", "pancreatic intraductal papillary-mucinous neoplasm", "pancreatic acinar cell cystadenocarcinoma"]
last_modified_at: 2026-10-14
description: "Mitomycin: predicted new indication Solid pseudopapillary carcinoma of the pancreas (evidence level L5). Approved use: Pancreatic adenocarcinoma"
---

# Mitomycin
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

# Mitomycin: From Pancreatic Adenocarcinoma to Solid Pseudopapillary Carcinoma of the Pancreas

## One-Sentence Summary

Mitomycin is a DNA cross-linking cytotoxic agent, originally associated with the treatment of pancreatic adenocarcinoma.
The TxGNN model predicts it may be effective for **solid pseudopapillary carcinoma of the pancreas**,
but the data compiled for this report contain **0 clinical trials** and **0 publications** for this specific indication, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pancreatic adenocarcinoma (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Solid pseudopapillary carcinoma of the pancreas |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 8 (all cancelled; all are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on general pharmacology, mitomycin is a DNA cross-linking alkylating agent. Its efficacy in pancreatic adenocarcinoma is the basis of the original indication, so a general cytotoxic rationale may extend to other pancreatic tumours.

The predicted disease is a pancreatic neoplasm, so the model likely links it to the original indication through shared pancreatic tumour context. However, solid pseudopapillary neoplasms of the pancreas are generally low-grade and are typically treated by surgery. The benefit of a cytotoxic agent is therefore uncertain, and no disease-specific rationale or clinical data were provided.

Nine other pancreatic tumour predictions scored similarly (99.82–99.86%). Among them, only a few have any indirect literature, and none has clinical trials:

- **Pancreatic carcinoma with mixed differentiation, mixed ductal-endocrine carcinoma and pancreatic signet ring cell adenocarcinoma:** these share ductal or adenocarcinoma components with the original indication, but have no supporting studies.
- **Pancreatic intraductal papillary-mucinous carcinoma and neoplasm:** only a case report and a review of radiochemotherapy in ductal pancreatic carcinoma exist, and neither shows a mitomycin benefit.
- **Malignant exocrine pancreas neoplasm:** this largely overlaps with the original indication as a parent term, so it is not a true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication or for the other nine predictions.

## Literature Evidence

Currently no related literature available for solid pseudopapillary carcinoma of the pancreas.

For other predicted pancreatic indications, only indirect literature was found. None of it demonstrates a mitomycin treatment effect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/) | 2005 | Case report | Pancreatology | Pseudomyxoma peritonei managed with intraperitoneal hyperthermic chemoperfusion in a patient who also had pancreatic IPMN (relevant to IPMN predictions) |
| [10897253](https://pubmed.ncbi.nlm.nih.gov/10897253/) | 2000 | Review | Strahlenther Onkol | Adjuvant and neoadjuvant radiochemotherapy in ductal pancreatic carcinoma (relevant to the original indication) |
| [8361472](https://pubmed.ncbi.nlm.nih.gov/8361472/) | 1993 | Clinical study | Nihon Geka Gakkai Zasshi | Tamoxifen added to immuno-chemotherapy (including mitomycin) after resection of pancreatic carcinoma; estrogen receptors found in 21 of 27 tumours |
| [2695183](https://pubmed.ncbi.nlm.nih.gov/2695183/) | 1989 | Review | Bulletin du Cancer | General review of diagnosis and treatment of unknown primary tumours; not specific to mitomycin |

## US Market Information

All eight US authorizations are generic applications (ANDAs) for a lyophilized powder for injection, and all are cancelled. No approved indication text is available for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA215687 | Mitomycin (Fresenius Kabi USA) | Injection, powder, lyophilized, for solution | Not available |
| ANDA216732 | Mitomycin (BluePoint Laboratories) | Injection, powder, lyophilized, for solution | Not available |
| ANDA202670 | Mitomycin (Bryant Ranch Prepack) | Injection, powder, lyophilized, for solution | Not available |
| ANDA064144 | Mitomycin (BluePoint Laboratories) | Injection, powder, lyophilized, for solution | Not available |
| ANDA064117 | Mitomycin (Hikma Pharmaceuticals USA) | Injection, powder, lyophilized, for solution | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA cross-linking alkylating-type antitumour antibiotic) |
| Myelosuppression Risk | High. Myelosuppression, including thrombocytopenia and leukopenia, is a recognised concern, and the knowledge graph lists these blood disorders among its contraindication links. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential and platelet count, renal function (kidney disease and haemolytic-uremic syndrome are flagged), and signs of heart failure |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindications (knowledge graph links, not label text):** kidney disease, pyoureter, thrombocytopenia, blood coagulation disease, anaemia (including macrocytic anaemia), leukopenia, haemolytic-uremic syndrome (including the typical form), congestive heart failure, heart failure and stomatitis.
- **Drug Interactions:** 100 interactions were found in total. The main ones listed are below.
  - **Major:** deferiprone and samarium (153Sm) lexidronam.
  - **Moderate:** palifermin, strontium chloride Sr-89 and fostamatinib.
  - **Minor:** levofloxacin.
  - Many others, such as warfarin, dexamethasone, prednisone and ondansetron, have an unclassified severity.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.86%), but there are no clinical trials or literature for the predicted indication, so the evidence level is L5. Solid pseudopapillary neoplasms are usually low-grade and surgically treated, which weakens the case for a cytotoxic agent. In addition, all US licenses are cancelled and the safety data are limited.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (this blocks safety screening)
- Mechanism of action data, such as from DrugBank
- Disease-specific preclinical or clinical evidence for solid pseudopapillary carcinoma of the pancreas
- Clarification of whether a current supply or marketed product exists, since all US licenses are cancelled
- Route compatibility assessment (currently pending; only the injectable form is on record)
- A review of other predicted pancreatic indications that may have stronger biological or clinical rationale, such as pancreatic signet ring cell adenocarcinoma or pancreatic carcinoma with mixed differentiation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

