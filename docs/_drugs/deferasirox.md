---
layout: default
title: Deferasirox
parent: 僅模型預測 (L5)
nav_order: 577
evidence_level: L5
indication_count: 5
---

# Deferasirox
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Deferasirox: From Iron Overload to HIV Infectious Disease

## One-Sentence Summary

Deferasirox is an oral iron chelator used to treat chronic iron overload caused by repeated blood transfusions (transfusional hemosiderosis) and non-transfusion-dependent thalassemia.
The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with **0 clinical trials** and **2 publications** currently supporting this direction — limited to in vitro mechanistic and narrative review evidence only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic iron overload (transfusional hemosiderosis; non-transfusion-dependent thalassemia) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L4 |
| US Market Status | Not marketed (no licenses on file in this dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Deferasirox is a tridentate oral iron chelator that selectively binds ferric iron (Fe³⁺) with high affinity, reducing systemic and tissue iron burden. Its proven role is in managing iron overload states — conditions in which excess iron drives oxidative stress and organ damage.

The mechanistic bridge to HIV lies in the iron-dependence of viral replication. HIV-1 relies on iron-requiring enzymes — including ribonucleotide reductase and reverse transcriptase — for productive infection. A 2021 in vitro study (PMID 34550543) demonstrated that restricting iron within endolysosomes increases HIV-1 Tat protein oligomerization, which in turn suppresses Tat-mediated LTR promoter transactivation and reduces viral replication. Because Deferasirox reduces the intracellular labile iron pool, it could theoretically recreate this iron-restricted environment and attenuate HIV-1 transcriptional activity.

However, this entire mechanistic chain rests solely on cell-culture data. There is no animal model evidence, no pharmacokinetic analysis of whether Deferasirox achieves relevant intracellular iron reduction at the CNS or lymphoid compartments relevant to HIV, and no clinical data of any kind. The prediction's plausibility is real, but the evidence base is insufficient for clinical translation without substantial additional research.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Deferasirox in HIV Infectious Disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Basic Science (in vitro) | Journal of Neurovirology | Demonstrated that elevated endolysosomal iron increases HIV-1 Tat oligomerization and suppresses Tat-LTR transactivation, reducing HIV-1 replication in cell culture; mechanistically supports iron chelation as a potential antiviral strategy |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Narrative Review | Journal of the American Pharmacists Association | Overview of newly approved drugs including Deferasirox at the time of its initial FDA approval; not specific to HIV; provides general drug characterization context only |

---

## US Market Information

No US market authorizations are recorded for Deferasirox in this dataset (0 licenses on file).

> **Note:** Deferasirox market status should be verified directly against FDA Orange Book records, as this dataset may reflect incomplete regulatory capture.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis — that iron chelation can restrict HIV-1 replication by reducing Tat-mediated LTR transactivation — is scientifically coherent, but all supporting evidence is limited to a single in vitro study. There are no animal models, no clinical trials, and no pharmacokinetic data establishing that Deferasirox achieves the necessary intracellular iron reduction in HIV-relevant tissues.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve full DrugBank record (DB01609) to document Deferasirox's iron-chelation mechanism and known pharmacokinetic profile for the evidence pack
- **Safety data**: Download and parse the FDA package insert (Exjade / Jadenu) to populate key warnings, contraindications, and drug interactions — currently blocking the S1 safety assessment
- **Preclinical validation**: Identify or commission animal model studies (e.g., HIV-1 infected humanized mouse models) measuring viral load changes under iron depletion by Deferasirox
- **CNS/lymphoid PK data**: Confirm whether Deferasirox achieves meaningful iron reduction in lymph nodes and CNS compartments (key HIV reservoirs), given its known limited CNS penetration
- **Comparative mechanism review**: Assess whether other iron chelators (deferoxamine, deferiprone) have more HIV-relevant in vivo or clinical data that could de-risk or inform a Deferasirox strategy
- **Regulatory clarification**: Reconcile the "0 licenses / not marketed" status with known FDA approvals; confirm whether this reflects a data gap or a deliberate scope exclusion in the dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

