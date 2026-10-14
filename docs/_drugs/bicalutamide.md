---
layout: default
title: Bicalutamide
parent: Model Prediction Only (L5)
nav_order: 458
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is a non-steroidal androgen receptor antagonist. The data compiled for this report do not list an approved indication, but the drug is known as an anti-androgen used in prostate cancer.
The TxGNN model ranks **Hypertrichosis** as its top prediction, but the supporting evidence is thin: **0 clinical trials** and **1 publication** (a comment letter).
The best-supported prediction in this list is actually **Female Breast Carcinoma**, with **1 Phase 2 trial** and **20 publications**, mostly preclinical or review articles.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the data compiled for this report (approval text is blank) |
| Predicted New Indication | Hypertrichosis (top-ranked prediction) |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 (for hypertrichosis) |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 4 (1 NDA and 3 ANDAs, all cancelled) |
| Recommended Decision | Hold |

> Among the top 10 predictions, **Female Breast Carcinoma** (score 99.11%, evidence level L2) has the strongest evidence and is the most practical candidate for follow-up. Its recommended handling is "Research Question".

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known information, bicalutamide is a non-steroidal androgen receptor (AR) antagonist. It blocks androgen signaling in tissues that depend on it.

**Hypertrichosis (top prediction):** Androgen signaling drives hair follicle activity, so AR blockade is biologically plausible for conditions of excess hair. The only literature item is a comment on a retrospective study of bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss. This is indirect evidence and does not cover congenital or generalized hypertrichosis.

**Female breast carcinoma (best-supported prediction):** AR is expressed in a substantial fraction of breast cancers, especially the luminal androgen receptor (LAR) subtype of triple-negative breast cancer and apocrine carcinoma. Preclinical work shows bicalutamide has antiproliferative and anti-invasive effects in TNBC models, including combinations with curcumin and with ERK inhibitors. Patient selection (AR-positive tumors) and the efficacy of bicalutamide alone remain open questions.

**Other predictions (ranks 2–10)** mostly lack a plausible mechanistic link. Examples are malformation syndromes, leprosy, and nephrogenic syndrome of inappropriate antidiuresis. They rest on the model score alone. The Ambras-type hypertrichosis and hair shaft abnormality predictions have only a weak link through hair follicle biology, because these conditions are genetically driven rather than androgen-mediated.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication (hypertrichosis). Trials found for other predictions are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) | Phase 2 | Active, not recruiting | 30 | Nivolumab + ipilimumab + bicalutamide in metastatic HER2-negative breast cancer; tests AR blockade combined with checkpoint therapy; no results reported; the combination design makes the contribution of bicalutamide hard to isolate |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME precision oncology trial (linked to multiple endocrine neoplasia); not specific to the disease; no interpretable efficacy data |
| [NCT02615223](https://clinicaltrials.gov/study/NCT02615223) | Not applicable | Unknown | 120 | Endocrine therapy with or without cryoablation in stage IV prostate cancer (linked to multiple endocrine neoplasia); quality-of-life and tumor-control study; not relevant to the predicted disease |

---

## Literature Evidence

**Hypertrichosis**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Comment/Letter | J Am Acad Dermatol | Comment on a retrospective review of 35 patients using bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss; indirect evidence |

**Female breast carcinoma (selected from 20 publications)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31434793](https://pubmed.ncbi.nlm.nih.gov/31434793/) | 2020 | Phase 2 single-arm study | Oncologist | Bicalutamide plus aromatase inhibitor in ER+/AR+ advanced breast cancer showed no synergy; clinical benefit rate 16.7% and objective response rate 0% at 6 months; study terminated |
| [40974527](https://pubmed.ncbi.nlm.nih.gov/40974527/) | 2026 | Preclinical | Sci China Life Sci | AR/ERK co-targeting (bicalutamide + GDC-0994) triggers ferroptosis via FOXC2 in TNBC |
| [31917699](https://pubmed.ncbi.nlm.nih.gov/31917699/) | 2020 | Preclinical | Anti-Cancer Drugs | Bicalutamide plus curcumin has a strong effect in AR-positive TNBC |
| [32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | 2020 | Preclinical (cell line) | Medicine | Bicalutamide inhibits proliferation and invasion of MDA-MB-231 TNBC cells |
| [39063165](https://pubmed.ncbi.nlm.nih.gov/39063165/) | 2024 | Preclinical | Int J Mol Sci | Bicalutamide enhances doxorubicin and docetaxel in human and canine inflammatory mammary cancer models |
| [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 | Review | Curr Med Sci | Overview of anti-androgen therapy for TNBC, including bicalutamide and combination strategies |
| [29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) | 2018 | Review | Cancer Treat Rev | AR as a potential target in the LAR subtype of TNBC |
| [35027319](https://pubmed.ncbi.nlm.nih.gov/35027319/) | 2022 | Review | Clin Breast Cancer | Molecular and clinical features of apocrine carcinoma (ER-negative, AR-positive) |
| [24740738](https://pubmed.ncbi.nlm.nih.gov/24740738/) | 2014 | Review | J Mol Endocrinol | Revisits the role of AR in breast cancer |
| [29069648](https://pubmed.ncbi.nlm.nih.gov/29069648/) | 2017 | Mechanistic study | Cell Physiol Biochem | Bicalutamide inhibits the β-catenin transcription complex in ER-negative breast cancer; refers to a phase II trial in AR+/ER- disease |

---

## US Market Information

All four US authorizations are cancelled, and the approval text for each is blank in the compiled data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020498 | Bicalutamide (ANI Pharmaceuticals) | Tablet | Not available |
| ANDA078917 | Bicalutamide (Proficient Rx) | Tablet | Not available |
| ANDA079110 | Bicalutamide (Sun Pharmaceutical) | Tablet, film coated | Not available |
| ANDA079089 | Bicalutamide (Pinnacle Life Science) | Tablet | Not available |

---

## Cytotoxicity

Bicalutamide is an anti-androgen used in oncology, so a limited cytotoxicity profile is given. It is a hormonal (targeted) agent, not a conventional cytotoxic chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (AR antagonist) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (the knowledge graph links the drug to liver disease and drug-induced liver injury); blood glucose and blood count are also relevant given the graph-based associations below |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** liver disease, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, anemia, macrocytic anemia, interstitial lung disease, and drug-induced liver injury. These come from a knowledge-graph contraindication relationship and need verification against the official label.
- **Drug interactions:** 100 interactions were found in total; the 20 reviewed include:
  - **Major:** cisapride, dolasetron
  - **Moderate:** famotidine, loperamide, aprepitant, bisacodyl, budesonide, castor oil, clarithromycin, eliglustat, glycerin, granisetron, lactitol, lactulose, levofloxacin, magnesium citrate, magnesium hydroxide, mineral oil
  - **Minor:** metronidazole

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, hypertrichosis, is supported only by one comment letter and no registered trials. The remaining predictions are mostly model output without a plausible mechanism.
- Female breast carcinoma is the one prediction with a coherent mechanism and clinical activity, but the evidence is early: one Phase 2 combination trial without results, a terminated Phase 2 single-arm study with no objective responses, and mostly preclinical literature. It is worth pursuing as a research question, not as a decision to proceed.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, to complete safety screening
- Mechanism-of-action data from DrugBank
- Original approved indication text, which is blank in the compiled license data
- For hypertrichosis: the full retrospective study of bicalutamide for minoxidil-induced hypertrichosis, and a prospective trial design
- For breast cancer: results of NCT03650894, and an AR-positive selection strategy with monotherapy data in LAR TNBC
- A route and formulation compatibility assessment, which is still pending for all predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

