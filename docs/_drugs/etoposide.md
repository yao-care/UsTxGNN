---
layout: default
title: Etoposide
parent: Moderate Evidence (L3-L4)
nav_order: 685
evidence_level: L4
indication_count: 10
---

# Etoposide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Etoposide: From Small Cell Lung Cancer and Testicular Tumors to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide is a cytotoxic chemotherapy drug, classically used for small cell lung cancer, germ cell (testicular) tumors and lymphomas.
The TxGNN model predicts it may be effective for **well-differentiated fetal adenocarcinoma of the lung**, a rare low-grade lung tumor.
Support is thin: **0 clinical trials** and **1 publication** (a case report and review), so this is a computational hypothesis, not clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records provided. Literature and general labeling place etoposide in small cell lung cancer, germ cell tumors and lymphomas |
| Predicted New Indication | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the dataset. From general pharmacology, etoposide inhibits topoisomerase II, causing DNA strand breaks in rapidly dividing cells. Its efficacy in lung malignancy, especially small cell lung cancer, is well established.

Well-differentiated fetal adenocarcinoma is a very rare lung tumor. It is one of the three forms grouped under pulmonary blastoma, alongside classic biphasic pulmonary blastoma and pleuropulmonary blastoma. The only supporting paper is a case report and literature review of classic biphasic pulmonary blastoma. It states that no standard treatment guidelines exist because the disease is so rare.

The link is therefore indirect. It rests on etoposide's activity in other lung cancers, not on evidence in this tumor. The 0.999 TxGNN score is a model output and does not measure clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case report / Review | J Int Med Res | A classic biphasic pulmonary blastoma patient had lobe resection, then adjuvant nedaplatin plus paclitaxel. The visible abstract does not mention etoposide, so it does not directly support this drug. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075635 | Etoposide (Mylan) | Capsule | Not listed in the record |
| ANDA074290 | Etoposide (Hikma) | Injection | Not listed in the record |
| ANDA074513 | Etoposide (BluePoint) | Injection | Not listed in the record |
| NDA020457 | ETOPOPHOS (H2-Pharma) | Lyophilized powder for injection | Not listed in the record |
| ANDA074529 | Etoposide (BluePoint) | Concentrate for injection | Not listed in the record |

Both oral (capsule) and injectable forms are available, and 16 authorizations exist in total.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase II inhibitor) |
| Myelosuppression Risk | High (general pharmacology; dose-limiting toxicity). Please refer to the package insert for details |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

This section is based on general drug-class knowledge because the Evidence Pack contains no toxicity data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single case report and review that does not describe etoposide use, and no trials are registered. The evidence supports only a research question, not development.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Case series or reports of etoposide-containing regimens specifically in fetal adenocarcinoma or pulmonary blastoma
- Consider prioritizing other predictions for this drug that have stronger support, such as Ewing sarcoma (L1, randomized phase 3 evidence for adding ifosfamide and etoposide) and rhabdomyosarcoma (L2)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

