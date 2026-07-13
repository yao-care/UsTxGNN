---
layout: default
title: Tamoxifen
parent: 僅模型預測 (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
---

# Tamoxifen
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

# TAMOXIFEN: From ER-Positive Breast Cancer to Mammary Paget Disease

## One-Sentence Summary

Tamoxifen is a selective estrogen receptor modulator (SERM) long established as a cornerstone hormonal therapy for estrogen receptor-positive (ER+) breast cancer treatment and prevention.
The TxGNN model predicts it may be effective for **Mammary Paget Disease**,
with **1 clinical trial** and **13 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ER-positive breast cancer (adjuvant treatment and prevention) |
| Predicted New Indication | Mammary Paget Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L3 |
| Market Status | 未上市 (No regulatory records in current dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, tamoxifen is a selective estrogen receptor modulator (SERM) that competitively binds to estrogen receptor alpha (ERα), blocking estrogen-driven transcriptional activation in breast tissue. Its efficacy in ER-positive breast cancer has been extensively proven across landmark Phase 3 trials (NSABP B-14, ATAC, BIG 1-98), reducing recurrence by 25–30% over 10 years of adjuvant therapy.

Mammary Paget disease is a rare intraepithelial adenocarcinoma of the nipple-areola complex that, in 80–95% of cases, is accompanied by an underlying ER-positive invasive or in situ carcinoma. This strong biological co-occurrence provides the primary mechanistic bridge: by blocking ERα signaling in the associated underlying tumor, tamoxifen may suppress the carcinogenic milieu that sustains Paget cell populations. A case report of hormone receptor-positive metastatic extramammary Paget disease successfully treated with tamoxifen (PMID 34463889) provides direct proof-of-concept for ER-targeted therapy in Paget histology.

However, the direct responsiveness of Paget cells themselves — as distinct from the co-existing underlying carcinoma — to ERα blockade remains mechanistically uncertain. The TxGNN prediction likely reflects the model's recognition of the strong ER biology shared between ER+ breast cancers and Paget disease, rather than evidence of autonomous Paget cell ER-dependence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | Completed | 313 | Medroxyprogesterone acetate vs. observation to prevent tamoxifen-induced endometrial pathology in postmenopausal women with DCIS, lobular CIS, **Paget's disease of the nipple**, Stage I–II breast cancer. Tamoxifen is the background therapy, not under evaluation; trial is not a direct Paget disease treatment study. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | Case Report | Investigational New Drugs | Successful tamoxifen treatment of HR-positive metastatic **extramammary** Paget disease; supports ER-directed therapy concept for Paget histology |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | Case Report | Breast | Unusually extensive Paget's disease of the nipple concealed for 10 years; response achieved with tamoxifen followed by electron arc radiotherapy; disease-free at 9 months |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | Case Series | British Journal of Surgery | 48-woman series over 13 years; treatment breakdown: 37 mastectomy, 10 cone excision, 1 tamoxifen alone; DCIS found in 45 operative specimens |
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | Meta-analysis | Breast Care | Local recurrence after mastectomy vs. breast-conserving surgery in Paget's disease; total recurrence rate 20–40%; establishes standard-of-care surgical context |
| [29694313](https://pubmed.ncbi.nlm.nih.gov/29694313/) | 2018 | Case Report | Il Giornale di Chirurgia | Male breast Paget disease; rare presentation with no established guidelines; underlying invasive ductal carcinoma common finding |
| [19112575](https://pubmed.ncbi.nlm.nih.gov/19112575/) | 2009 | Case Report | Archives of Gynecology and Obstetrics | Synchronous vulvar and breast Paget disease with underlying adenocarcinoma; illustrates the systemic ER+ oncological context |
| [12924421](https://pubmed.ncbi.nlm.nih.gov/12924421/) | 2003 | Case Report | Surgery Today | Synchronous bilateral breast cancer with Paget disease and invasive ductal carcinoma; demonstrates multifocal ER+ disease presentation |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | Case Series | The American Surgeon | Review of 32 literature cases of male breast Paget's disease; 50% present with palpable mass or positive nodes at diagnosis; tamoxifen noted in systemic therapy discussion |
| [17319355](https://pubmed.ncbi.nlm.nih.gov/17319355/) | 2006 | Case Series | Nigerian Journal of Clinical Practice | 8-case series at Nigerian teaching hospital; all female, mean age 47.6 years; late presentation common; provides epidemiological context |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | Case Report | Clinical Breast Cancer | Paget's disease as ipsilateral local recurrence after breast-conserving treatment in 2,181-patient cohort; highlights management complexity after initial ER+ breast cancer treatment |

---

## Market Authorization Information

No regulatory authorization records are available in the current dataset (0 licenses on file).

> **Data note:** The absence of records reflects a query gap, not actual global unavailability. Tamoxifen (Nolvadex®, generics) holds established approvals in numerous jurisdictions for ER-positive breast cancer treatment and prevention. This dataset did not return matching regulatory records at the time of query.

---

## Cytotoxicity

Tamoxifen meets the antineoplastic classification criteria: it is indicated for breast cancer (malignant condition) and is categorized as a selective estrogen receptor modulator with anti-tumor activity.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted hormonal therapy — Selective Estrogen Receptor Modulator (SERM); non-conventional cytotoxic (not a DNA-damaging chemotherapy agent) |
| Myelosuppression Risk | Low (tamoxifen does not cause clinically significant myelosuppression at standard doses) |
| Emetogenicity Classification | Low |
| Monitoring Items | Endometrial thickness / annual gynecological exam (especially postmenopausal women); liver function tests; coagulation parameters (VTE risk assessment); ophthalmologic exam at high-dose or prolonged use; bone mineral density (premenopausal patients on long-term therapy) |
| Handling Protection | Standard precautions per institutional policy for hormonal antineoplastic agents; not classified as a conventional hazardous cytotoxic requiring full PPE containment, but reproductive toxicity warrants appropriate handling by pregnant staff |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed prescribing information was not retrieved in this dataset (Data Gap DG001). Key known risks based on drug class include: endometrial cancer risk (primarily postmenopausal women), venous thromboembolism, menopausal symptoms (hot flashes, vaginal discharge), and rare retinal toxicity. CYP2D6 poor metabolizer status impairs conversion to active metabolite endoxifen and may reduce efficacy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the biological rationale linking tamoxifen to mammary Paget disease is coherent — given that 80–95% of cases involve an underlying ER-positive carcinoma — direct clinical evidence for tamoxifen in Paget disease itself remains confined to isolated case reports and one Phase 3 trial where Paget's patients were enrolled as a minor subgroup. The evidence does not yet meet the threshold for a formal repurposing designation; this is best framed as an investigational signal warranting prospective evaluation.

**To proceed, the following is needed:**
- Prospective registry study or dedicated pilot trial in mammary Paget disease evaluating tamoxifen response (particularly in patients with confirmed HR-positive underlying carcinoma)
- Histopathological ER/PR receptor characterization of Paget cells directly (not only the underlying carcinoma) to determine autonomous ER-dependence
- Mechanistic clarification of whether tamoxifen suppresses Paget cells via ERα in the epidermal compartment or exclusively through control of the underlying tumor
- Retrieval of detailed MOA data from DrugBank (Data Gap DG002)
- Retrieval of TFDA/FDA package insert warnings and contraindications (Data Gap DG001) to complete safety screening before any clinical protocol design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

