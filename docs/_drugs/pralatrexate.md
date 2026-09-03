---
layout: default
title: Pralatrexate
parent: 僅模型預測 (L5)
nav_order: 1073
evidence_level: L5
indication_count: 10
---

# Pralatrexate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pralatrexate: From Peripheral T-Cell Lymphoma to Pleural Mesothelioma

## One-Sentence Summary

> Pralatrexate is an antifolate (DHFR-inhibitor) chemotherapy originally developed for relapsed/refractory peripheral T-cell lymphoma.
> TxGNN flagged a cluster of 10 mesothelioma/pleural-tumor indications as high-scoring candidates; among them, **Pleural Mesothelioma**
> has by far the strongest support, backed by **1 completed Phase II trial** and **2 supporting reviews/preclinical studies**.
> Evidence remains preliminary (L2, hypothesis-generating), and the drug currently holds no marketing authorization in this jurisdiction.

*Note: TxGNN's single highest-scoring prediction ("pleural adenomatoid tumor," score 99.91%) has zero supporting clinical trials or literature and low biological plausibility — adenomatoid tumors are typically benign, making cytotoxic chemotherapy inappropriate. This report therefore focuses on the best-evidenced candidate within the predicted cluster, Pleural Mesothelioma.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peripheral T-Cell Lymphoma (relapsed/refractory) — per internationally known labeling; not present in the supplied regulatory dataset |
| Predicted New Indication | Pleural Mesothelioma (part of a broader TxGNN-flagged mesothelioma/pleural-tumor cluster) |
| TxGNN Prediction Score | 99.85% (rank 4610) |
| Evidence Level | L2 |
| Market Status | Not marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack (flagged as a data gap). Based on known drug class information, pralatrexate is an antifolate — a dihydrofolate reductase (DHFR) inhibitor that blocks DNA synthesis in rapidly dividing cells, structurally related to methotrexate and the 10-deazaaminopterin class.

The original indication (peripheral T-cell lymphoma) and the predicted new indication (pleural mesothelioma) are mechanistically connected through the antifolate drug class rather than tissue-type similarity: pemetrexed, another antifolate, is already an approved standard-of-care agent for malignant pleural mesothelioma. This provides independent, real-world validation that antifolate mechanisms are clinically active against mesothelioma, lending biological plausibility to the TxGNN signal for pralatrexate.

This plausibility is further supported by early clinical and preclinical data specific to pralatrexate itself: a Phase II trial (PMID 17409804) tested pralatrexate directly in unresectable malignant pleural mesothelioma, and preclinical work (PMID 11595715) demonstrated 25–30 fold greater in vitro cytotoxic potency than methotrexate in mesothelioma cell lines. However, this Phase II study is small, single-arm, from 2007, and was not followed by confirmatory Phase III trials — so the signal should be treated as hypothesis-generating rather than confirmed efficacy. The other mesothelioma subtypes in the TxGNN output (biphasic, epithelioid, sarcomatoid, lymphohistiocytoid, peritoneal, well-differentiated papillary) inherit this rationale only indirectly, as an extrapolation from the general pleural mesothelioma hypothesis, without subtype-specific data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(The Phase II study identified for this indication was captured only as a published-literature record, not as a structured clinical trial registry entry — see Literature Evidence below.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Phase II Clinical Trial (single-arm) | J Thorac Oncol | Pralatrexate tested in unresectable malignant pleural mesothelioma; favorable toxicity profile, primarily stomatitis; prior antifolates already shown to be active in mesothelioma |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Review | Cancer Manag Res | Reviews antifolate mechanism (DHFR/thymidylate synthase inhibition) as an established anticancer strategy, contextualizing pralatrexate within the antifolate drug class |
| [11595715](https://pubmed.ncbi.nlm.nih.gov/11595715/) | 2001 | Preclinical/Experimental Therapeutics | Clin Cancer Res | Pralatrexate (PDX) showed 25–30x greater in vitro cytotoxic potency than methotrexate against human mesothelioma cell lines; enhanced activity when combined with platinum agents |

---

## US Market Information

This drug currently holds no marketing authorization on record in this jurisdiction (0 licenses; market status: Not Marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — antifolate (DHFR inhibitor), same pharmacological class as methotrexate and pemetrexed |
| Myelosuppression Risk | Not quantified in current evidence pack. Per PMID 17409804, the dose-limiting toxicity observed in the mesothelioma trial was primarily stomatitis/mucositis rather than myelosuppression; antifolates as a class do carry cytopenia risk — please refer to the package insert |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, oral mucosa/mucositis assessment, renal and hepatic function, folate/B12 status |
| Handling Protection | Requires cytotoxic/hazardous drug handling precautions per antineoplastic classification |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the pleural mesothelioma indication rests on a single small, 19-year-old Phase II single-arm trial with no subsequent Phase III confirmation, supported only by older preclinical and review literature. The drug is not currently marketed in this jurisdiction, and safety/labeling data are entirely unavailable (blocking data gap). The TxGNN top-ranked candidate (pleural adenomatoid tumor) has no supporting evidence and low clinical plausibility given the typically benign nature of that lesion, and should not be pursued.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert — warnings, contraindications, and DDI data (DG001, blocking)
- Confirmed mechanism of action via DrugBank API (DG002)
- Updated or confirmatory clinical trial data in mesothelioma, ideally subtype-stratified
- Confirmation of current local regulatory/marketing status
- Formal risk–benefit assessment given the drug's cytotoxic chemotherapy class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

