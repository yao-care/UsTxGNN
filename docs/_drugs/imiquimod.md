---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 793
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From Actinic Keratosis to Pre-Malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topically applied Toll-like receptor 7 (TLR7) agonist, originally used to treat actinic keratosis, superficial basal cell carcinoma, and external genital/perianal warts.
The TxGNN model predicts it may be effective for **Pre-Malignant Neoplasm** (a category spanning cervical, vulvar, and anal intraepithelial neoplasia),
with **19 clinical trials** and **9 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Actinic keratosis, superficial basal cell carcinoma, external genital/perianal warts (established global indications, referenced within collected trial records; no formal license text available in this dataset) |
| Predicted New Indication | Pre-Malignant Neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Market Status (this jurisdiction) | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data from DrugBank is not available in this evidence pack. Based on information embedded in the collected trial and literature evidence, imiquimod is a topically applied TLR7 agonist: local application on skin or mucosa triggers an innate immune response (interferon-α and pro-inflammatory cytokine release) followed by cytotoxic T-cell activation, which together help clear abnormal proliferative epithelial cells.

Imiquimod's established indications — actinic keratosis, superficial basal cell carcinoma, and external genital/perianal warts — are themselves pre-malignant or HPV-driven proliferative lesions. The TxGNN-predicted indication, "pre-malignant neoplasm," overlaps substantially with this existing profile: the supporting trial evidence specifically covers cervical intraepithelial neoplasia (CIN), vulvar intraepithelial neoplasia (VIN), and lentigo maligna — all HPV-associated or UV-associated pre-malignant epithelial lesions.

Because the TLR7-driven local immune activation mechanism targets the host immune response to abnormal epithelium rather than a tumor-specific antigen, extension from AK/BCC to other HPV- or UV-driven pre-malignant epithelial lesions (cervical, vulvar, anal) is mechanistically plausible, and this plausibility is already backed by completed Phase 2/3 RCTs.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod for high-grade cervical intraepithelial neoplasia (CIN 2-3) vs. standard LLETZ excision; stopped early but directly on-target design |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Imiquimod as neo-adjuvant treatment to reduce excision size/margins in lentigo maligna of the face |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | RCT evaluating topical imiquimod efficacy for high-grade cervical intraepithelial lesions |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Immune-escape mechanism study of imiquimod in vulvar intraepithelial neoplasia 2/3 and anogenital warts |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Surgical excision vs. curettage + imiquimod for nodular basal cell carcinoma (non-inferiority) |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Neoadjuvant TLR7 agonist (imiquimod) immunotherapy pilot in early-stage oral squamous cell carcinoma |
| [NCT03057340](https://clinicaltrials.gov/study/NCT03057340) | Phase 1 | Unknown | 30 | DRibble antigen-targeted vaccine study in advanced lung cancer; imiquimod as adjuvant, weak relevance |
| [NCT01792505](https://clinicaltrials.gov/study/NCT01792505) | Phase 1 | Completed | 71 | Surgical resection + dendritic cell/tumor lysate vaccine with imiquimod adjuvant in malignant glioma |
| [NCT03872947](https://clinicaltrials.gov/study/NCT03872947) | Phase 1b | Active, not recruiting | 138 | TRK-950 combination regimens including imiquimod cream in advanced solid tumors; drug identity ambiguous |
| [NCT04072900](https://clinicaltrials.gov/study/NCT04072900) | Phase 1 | Unknown | 30 | Personalized neoantigen vaccine + anti-PD-1 in metastatic melanoma; imiquimod not primary intervention |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Cochrane Systematic Review | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia (AIN), an HPV-related pre-malignant condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Cochrane Systematic Review | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined photodynamic therapy approaches for non-melanoma skin cancer, including imiquimod-adjacent strategies |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, a pre-malignant cutaneous lesion |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical treatment strategies (including imiquimod) for non-melanoma skin cancer and precursor lesions |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | PK/PD (animal) | Urol Oncol | TLR7 agonists used topically for (pre-)malignant skin lesions, investigated for intravesical bladder cancer therapy |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | Int J STD AIDS | Successful treatment of high-grade vulval intraepithelial neoplasia with imiquimod in a renal transplant recipient |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case Report | Hautarzt | OCT imaging of a patient with actinic porokeratosis alongside multiple pre-malignant skin lesions |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | Int J STD AIDS | Bowenoid papulosis of the penis (pre-malignant genital lesion) successfully treated with topical imiquimod |

## US Market Information

Currently not marketed in this jurisdiction; no marketing authorization (license) records are available in this dataset.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by completed Phase 2/3 RCTs directly testing topical imiquimod in cervical and vulvar intraepithelial neoplasia, plus two Cochrane systematic reviews on related pre-malignant HPV lesions — this is meaningfully stronger evidence than a pure model prediction. However, the local regulatory label (warnings/contraindications) and formal MOA documentation are still missing, which blocks a full safety assessment.

**To proceed, the following is needed:**
- TFDA package insert / label data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Formal DrugBank MOA documentation — currently a **High** severity data gap (DG002)
- Drug-drug interaction (DDI) data — current query status is "not found"
- Clarification of the "pre-malignant neoplasm" ontology mapping against the specific lesion types actually studied (CIN, VIN, lentigo maligna) to confirm the indication scope before advancing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

