---
layout: default
title: Imiquimod
parent: Model Prediction Only (L5)
nav_order: 793
evidence_level: L5
indication_count: 10
---

# Imiquimod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Imiquimod: From Topical Skin Therapy to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical cream marketed in the US in several products, including the brand Zyclara. The Evidence Pack does not list its labeled indications.
The TxGNN model predicts it may be effective for **pre-malignant neoplasm**, with **18 clinical trials** and **8 publications** retrieved for this direction. Most of the trials are early-phase or only indirectly relevant, and none has posted results in the Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 as assigned in the Evidence Pack. A strict reading of the criteria gives a lower level (see Conclusion). |
| US Market Status | ✓ Marketed |
| Number of NDAs | 13 licenses in total (NDA and ANDA combined) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for imiquimod is not available in the Evidence Pack. It is known to be a Toll-like receptor 7 (TLR7) agonist. Applied to the skin, it triggers local innate and adaptive immune activation (interferon-alpha, TNF-alpha, IL-12, Th1 response). This immune activation can clear dysplastic and HPV-infected epithelium.

That mechanism fits pre-malignant lesions such as cervical, vulvar and anal intraepithelial neoplasia and actinic lesions. These conditions are often HPV-driven and confined to the epithelium, so a topical immune stimulant can reach them. The pack notes that topical imiquimod is already established for actinic keratosis and superficial basal cell carcinoma. Part of this prediction signal may therefore reflect existing labeled use rather than true repurposing.

Two points need checking before relying on the evidence:
- The trial titles are truncated, so the exact lesion type in each trial should be confirmed.
- The pack's data gaps (original indications and MOA) limit how far the mechanistic link can be analysed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomized trial of topical imiquimod versus standard excision (LLETZ) for high-grade cervical intraepithelial neoplasia. Terminated with only 9 participants, so it is underpowered. |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Imiquimod as neoadjuvant treatment in facial lentigo maligna to reduce excision size and the risk of intralesional excision. |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | Randomized trial of topical imiquimod in high-grade cervical intraepithelial lesions. |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Exploratory study of immune escape in HPV-associated lesions (VIN 2/3 and anogenital warts) and of imiquimod's mechanisms. |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Randomized comparison of 5% imiquimod, 0.05% imiquimod and nanoencapsulated 0.05% imiquimod gel in actinic cheilitis. |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Imiquimod 3.75% cream after cryotherapy for hypertrophic actinic keratoses on the hands and forearms. |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream, 1 or 2 treatment cycles, for actinic keratoses on the head. |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Surgical excision versus curettage plus imiquimod for nodular basal cell carcinoma. This is a malignancy, so it is only indirectly relevant. |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Pilot of neoadjuvant imiquimod in early-stage oral squamous cell carcinoma. This is a malignancy, not a pre-malignant lesion. |
| [NCT01792505](https://clinicaltrials.gov/study/NCT01792505) | Phase 1 | Completed | 71 | Dendritic-cell vaccine with imiquimod after resection of malignant glioma. Low relevance. |

Eight further trials were retrieved but are not listed. They are mostly cancer vaccine or combination studies in which imiquimod is at most an adjuvant.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Reviews interventions for anal canal intraepithelial neoplasia, a pre-malignant, HPV-associated condition. |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Reviews medical interventions for high-grade vulval intraepithelial neoplasia, a pre-malignant condition without consensus on optimal management. |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, a pre-malignant lesion that can progress to squamous cell carcinoma. Covers topical field therapies. |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical strategies for non-melanoma skin cancer and precursor lesions, including fluorouracil, diclofenac, imiquimod and photodynamic therapy. |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer. |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical | Urol Oncol | Rat pharmacokinetics and pharmacodynamics of two investigational TLR7 agonists. Notes that TLR7 agonists are used topically for (pre)malignant skin lesions. |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | Successful treatment of high-grade vulval intra-epithelial neoplasia with imiquimod 5% in a renal transplant recipient. |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | Bowenoid papulosis of the penis cleared with topical imiquimod 5%, and well tolerated. |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Imaging/diagnostic study | Hautarzt | OCT imaging of actinic porokeratosis. Little direct bearing on imiquimod efficacy. |

The retrieved literature contains no RCTs. Direct clinical support comes only from case reports.

---

## US Market Information

The Evidence Pack does not provide approved indication text for these licenses.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA078837 | Imiquimod | Cream | Padagis Israel Pharmaceuticals Ltd |
| ANDA078837 | Imiquimod | Cream | Bryant Ranch Prepack |
| ANDA201994 | Imiquimod | Cream | Glenmark Pharmaceuticals Inc., USA |
| NDA022483 | Zyclara | Cream | Bausch Health US, LLC |

The pack reports 13 licenses in total. Only the distinct products above are shown, and the topical cream is the only dosage form listed.

---

## Safety Considerations

The package insert warnings, contraindications and drug interaction data are not available in the Evidence Pack. Please refer to the package insert for safety information.

The retrieved literature raises these signals:
- **Malignant conversion:** One case report describes malignant conversion of florid oral and labial papillomatosis during imiquimod therapy (PMID 12719972).
- **Skin reactions:** Case reports describe erythema multiforme (PMID 29173871) and lichen planopilaris (PMID 24575881) after topical imiquimod.
- **Off-label oral use:** A 2024 review examines the safety of off-label imiquimod in oral lesions (PMID 38867102).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible for HPV-related and actinic pre-malignant lesions. The trials are mainly in cervical intraepithelial neoplasia, vulvar intraepithelial neoplasia, actinic keratosis and lentigo maligna. The Evidence Pack assigns L1, but by strict criteria that level is borderline. Only two Phase 3 trials are completed. One is a single-arm study of 20 patients, and the pivotal cervical trial was terminated at 9 participants. The signal also overlaps with existing labeled uses.

Among the other nine predictions, only benign neoplasm of buccal mucosa reaches L4, as a Research Question. Six are L5 prediction-only, and the two L4 predictions (odontogenic cyst, cystic neoplasm) rest on indirect or single case-report evidence. All of these are Hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are a blocking gap before safety screening.
- Detailed mechanism of action data from DrugBank.
- Confirmation of the lesion type and design for each Phase 3 trial, and the published results of NCT01720407 and NCT03233412.
- A separation of the signal that reflects existing labeled use (actinic keratosis, superficial BCC) from true new indications.
- A safety review of the malignant conversion and immune-mediated skin reaction reports before any use in new lesion types.

*This report is for research reference only and does not constitute medical advice. Predicted repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

