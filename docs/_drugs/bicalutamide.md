---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 458
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is a non-steroidal androgen receptor (AR) antagonist, widely used for prostate cancer treatment by competitively blocking testosterone and DHT binding to AR. The TxGNN model predicts it may be effective for **Hypertrichosis**, with **0 clinical trials** and **1 publication** currently supporting this specific direction. Separately, among all 10 predicted indications, the highest-evidence signal is **female breast carcinoma (AR+ Triple-Negative Breast Cancer)** at Evidence Level L2, which warrants a dedicated evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (androgen receptor–positive) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| US Market Status | Not marketed (no FDA approvals recorded in dataset — see note) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

> **Data note:** This dataset records bicalutamide as unlisted in the US market, which is inconsistent with the known existence of Casodex® (bicalutamide 50 mg, NDA 020498). Please cross-verify with the current FDA Orange Book before drawing regulatory conclusions.

---

## Why is This Prediction Reasonable?

Bicalutamide is a competitive AR antagonist that blocks testosterone and dihydrotestosterone (DHT) from binding to the androgen receptor. Since androgens—particularly DHT—stimulate hair follicle growth and can drive unwanted hypertrichosis in androgen-sensitive tissues, AR blockade provides a mechanistically coherent rationale for reducing androgen-driven hair excess.

The most concrete supporting evidence comes from drug-induced hypertrichosis: minoxidil, commonly used for androgenetic alopecia, can trigger unwanted facial and body hair as a side effect. The lone publication in this Evidence Pack (Trüeb et al., *JAAD*, 2022) is a letter commenting on a retrospective review of 35 female pattern hair loss patients in whom bicalutamide was used to manage minoxidil-induced hypertrichosis. This represents a **side-effect management application** rather than a primary therapeutic indication for hypertrichosis per se.

Currently, detailed mechanism of action data from DrugBank is not available in this Evidence Pack. Based on established pharmacology, bicalutamide's AR antagonism is biologically relevant only to **androgen-driven subtypes** of hypertrichosis (e.g., androgen excess in PCOS-related hirsutism, or drug-induced cases). The mechanistic link to hereditary or non-androgen-mediated hypertrichosis subtypes—such as Ambras syndrome (rank 3, chromosomal 8q22.1 rearrangement) or isolated genetic hair shaft abnormalities (rank 5)—is weak to absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bicalutamide in hypertrichosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Letter/Comment | Journal of the American Academy of Dermatology | Commentary on a retrospective study of 35 female pattern hair loss patients; authors discuss whether bicalutamide's AR-antagonism explains its benefit in reducing minoxidil-induced hypertrichosis |

---

## US Market Information

No FDA-licensed products for bicalutamide are recorded in this dataset. As noted above, this likely reflects a data collection gap rather than true US market absence. Once verified, the known product profile is:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| NDA 020498 *(verify)* | Casodex® | Tablet, 50 mg | Prostate cancer (stage D2 metastatic, in combination with LHRH analog) |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (Non-steroidal antiandrogen / AR antagonist — not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (not myelosuppressive; mild anemia may occur with long-term use) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT/AST at baseline and periodically), CBC, blood glucose |
| Handling Protection | Standard antineoplastic handling precautions apply as an antiandrogen agent |

---

## Safety Considerations

No TFDA or FDA label warnings, contraindications, or drug interaction data were available in this Evidence Pack. Please refer to the Casodex® US prescribing information for full safety details, particularly regarding hepatotoxicity (rare but serious), glucose intolerance, and QT-interval considerations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole supporting literature is a clinical commentary discussing bicalutamide as an incidental management strategy for a drug side effect (minoxidil-induced hypertrichosis), not as a primary treatment for hypertrichosis. No clinical trials exist for this indication, and the mechanistic link is confined to androgen-excess subtypes. Evidence is insufficient to advance beyond hypothesis generation at this stage.

**To proceed, the following is needed:**
- Define the hypertrichosis subtype of interest: androgen-driven (e.g., PCOS hirsutism, drug-induced) vs. hereditary/non-androgenic forms—only the former is mechanistically tractable
- Retrieve the full retrospective study that Trüeb et al. commented on, to assess the 35-patient dataset directly (PMID of the original article is not provided in this pack)
- Design a prospective pilot study or case series for androgen-excess–related hypertrichosis
- Obtain bicalutamide MOA/DrugBank data (Data Gap DG002) to complete the mechanism rationale
- Obtain FDA/TFDA label safety data (Data Gap DG001) before any clinical protocol can proceed

---

> **⚠️ High-Priority Secondary Finding**
>
> Among all 10 TxGNN-predicted indications, **female breast carcinoma** (AR-positive / Triple-Negative Breast Cancer, rank 9) carries substantially stronger clinical evidence (Evidence Level **L2**) despite its lower TxGNN rank. An active Phase II trial ([NCT03650894](https://clinicaltrials.gov/study/NCT03650894)) is evaluating bicalutamide + nivolumab + ipilimumab in metastatic HER2-negative breast cancer (enrollment 30, active not recruiting), supported by 20 publications spanning in vitro studies, retrospective series, and a complete response case report. The mechanistic basis is well-established: ~20–35% of TNBC tumors express AR (the LAR subtype), and bicalutamide suppresses AR-driven Wnt/β-catenin and PI3K/AKT proliferative signaling. This indication should be evaluated in a **separate, full-depth repurposing report** with a recommended decision of **Proceed with Guardrails**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

