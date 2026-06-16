---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK-Positive Non-Small Cell Lung Cancer to Lung Germ Cell Tumor

## One-Sentence Summary

Crizotinib is a first-generation, oral ATP-competitive inhibitor of ALK, ROS1, and MET receptor tyrosine kinases, originally approved for treatment of ALK-positive and ROS1-positive advanced non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may also be applicable to **Lung Germ Cell Tumor** (rank 7 of 10 predicted indications; prediction score 99.73%), based on the hypothesis that ALK rearrangements or MET amplification — known oncogenic drivers across diverse tumor types — may occasionally occur in this rare histology.
Currently **4 clinical trials** (primarily broad ALK-positive basket studies) and **20 publications** provide indirect mechanistic and clinical context supporting this prediction, which carries the highest actionability level (S2, Proceed with Guardrails) among all predictions in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive or ROS1-positive advanced non-small cell lung cancer |
| Predicted New Indication | Lung Germ Cell Tumor |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed (per evidence pack; NDA data likely requires re-query — Xalkori® is commercially available) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known published information, Crizotinib (Xalkori®) is a small-molecule inhibitor that competitively blocks ATP binding at the kinase domains of ALK, ROS1, and c-MET receptor tyrosine kinases, thereby suppressing downstream proliferative and survival signaling cascades (including RAS-MAPK and PI3K-AKT pathways). Its efficacy in EML4-ALK rearranged and ROS1 fusion-positive NSCLC has been robustly established in Phase 3 trials, with FDA approval granted in 2011 (ALK-positive NSCLC) and 2016 (ROS1-positive NSCLC).

Primary lung germ cell tumors are exceedingly rare, and their molecular landscape is not well-characterized. However, ALK rearrangements have been described across a broader spectrum of lung neoplasms beyond classical adenocarcinoma — including inflammatory myofibroblastic tumor (IMT), large-cell neuroendocrine carcinoma (PMID 32651063), and atypical carcinoid — with documented crizotinib sensitivity in ALK-positive cases. The TxGNN graph neural network likely captures structural proximity in the disease knowledge graph between lung germ cell tumors and other ALK-driven lung malignancies, generating this prediction through topological inference rather than direct disease-specific evidence.

The mechanistic rationale is plausible but contingent on biomarker confirmation. A biomarker-unselected lung germ cell tumor would have no biological basis for crizotinib sensitivity; however, a case confirmed to harbor ALK rearrangement or MET amplification by next-generation sequencing would carry a clear therapeutic hypothesis. The MATCH platform trial (NCT02465060) provides the most appropriate existing clinical framework to evaluate such a hypothesis prospectively across rare histologies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, Not Recruiting | 6,452 | NCI-MATCH molecular platform: assigns patients with refractory solid tumors to targeted therapy arms based on genomic profiling; ALK inhibitor sub-trial may capture rare ALK-positive tumors including germ cell histologies — largest available molecular-matching framework |
| [NCT01121588](https://clinicaltrials.gov/study/NCT01121588) | Phase 1B | Terminated | 44 | Crizotinib in non-NSCLC ALK-positive solid tumors; basket design enrolling diverse ALK+ histologies; terminated but with 44 enrolled patients providing indirect safety and activity signal for rare ALK-driven tumors |
| [NCT02223819](https://clinicaltrials.gov/study/NCT02223819) | Phase 2 | Completed | 34 | Adjuvant crizotinib in high-risk uveal melanoma following definitive therapy; demonstrates tolerability of crizotinib as adjuvant strategy in a non-NSCLC solid tumor (indirect, MET-pathway rationale) |
| [NCT02568267](https://clinicaltrials.gov/study/NCT02568267) | Phase 2 | Active, Not Recruiting | 534 | STARTRK-2: Entrectinib (ALK/ROS1/NTRK inhibitor) basket study in ALK/ROS1 fusion-positive solid tumors; not crizotinib, but validates the cross-histology ALK/ROS1 basket approach and provides comparator context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37012551](https://pubmed.ncbi.nlm.nih.gov/37012551/) | 2023 | Phase 1 RCT | Nature Medicine | Lorlatinib (3rd-gen ALK inhibitor) with/without chemotherapy in relapsed/refractory ALK-driven neuroblastoma; confirms role of ALK-targeted therapy in pediatric non-NSCLC ALK-positive tumors and highlights limitations of crizotinib (insufficient potency) in this setting |
| [28183697](https://pubmed.ncbi.nlm.nih.gov/28183697/) | 2017 | Phase 1/2 | Cancer Discovery | Entrectinib (ALK/ROS1/NTRK inhibitor) in advanced solid tumors with gene fusions; antitumor activity demonstrated across multiple histologies — provides cross-histology ALK/ROS1 inhibitor rationale |
| [32651063](https://pubmed.ncbi.nlm.nih.gov/32651063/) | 2021 | Case Report | Clinical Lung Cancer | Novel PLB1-ALK rearrangement identified by NGS in lung large-cell neuroendocrine carcinoma with crizotinib sensitivity; most directly relevant case for rare ALK-positive lung histologies beyond NSCLC |
| [31559892](https://pubmed.ncbi.nlm.nih.gov/31559892/) | 2020 | Case Report | Cancer Biology & Therapy | Primary pulmonary atypical carcinoid with EML4-ALK rearrangement; demonstrates ALK-driven neuroendocrine lung neoplasms exist and may be targetable — relevant precedent for rare lung tumor ALK biology |
| [27573755](https://pubmed.ncbi.nlm.nih.gov/27573755/) | 2016 | Review | Annals of Oncology | Comprehensive review of ALK gene alterations across tumor types (point mutations, fusions, amplifications); supports ALK as a pan-histology oncogenic driver and framework for biomarker-driven crizotinib use |
| [22968692](https://pubmed.ncbi.nlm.nih.gov/22968692/) | 2012 | Review | Targeted Oncology | ALK as a therapeutic target in NSCLC, ALCL, and neuroblastoma; establishes cross-histology rationale for crizotinib beyond its original approval |
| [30790327](https://pubmed.ncbi.nlm.nih.gov/30790327/) | 2019 | Observational | Histopathology | ALK expression characterized in treatment-naive small-cell lung cancer; demonstrates ALK status can be present in non-NSCLC lung tumors and supports broad lung tumor biomarker screening |
| [37561984](https://pubmed.ncbi.nlm.nih.gov/37561984/) | 2023 | Review | JCO Precision Oncology | ALK inhibitors in adult-onset neuroblastoma enriched for somatic ALK mutations; highlights response limitations of crizotinib and rationale for next-generation ALK inhibitors in ALK-driven non-lung tumors |
| [28960893](https://pubmed.ncbi.nlm.nih.gov/28960893/) | 2017 | Preclinical | Cancer Medicine | Crizotinib targets ALK, ROS1, and MET in glioblastoma stem cells; demonstrates crizotinib activity in non-NSCLC, non-hematologic malignancies and MET/ALK co-targeting potential |
| [26122839](https://pubmed.ncbi.nlm.nih.gov/26122839/) | 2015 | Translational Review | Cancer Research | Development pathway of crizotinib resistance in neuroblastoma and rationale for next-generation ALK inhibitors; informs realistic expectations for crizotinib efficacy in ALK-positive tumors with point mutations versus fusions |

---

## US Market Information

No FDA license records were retrieved in the current evidence pack (0 NDAs, market status recorded as not marketed). This appears to be a data gap — Crizotinib is commercially available as **Xalkori®** (Pfizer Inc.) with FDA approval for ALK-positive metastatic NSCLC (2011), ROS1-positive metastatic NSCLC (2016), and ALK-positive pediatric NSCLC (2021). A re-query of FDA's drug database (Drugs@FDA) is recommended to populate this section with complete NDA records and approved labeling.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — ALK/ROS1/MET tyrosine kinase inhibitor (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low to Moderate — neutropenia and lymphopenia reported; not the primary dose-limiting toxicity |
| Emetogenicity Classification | Low to Moderate — nausea and vomiting are common (CTCAE Grade 1–2) but rarely dose-limiting |
| Monitoring Items | CBC with differential (neutropenia monitoring), LFTs/ALT/AST/total bilirubin (hepatotoxicity — including risk of fatal fulminant liver failure, PMID 26898609), ECG (QTc prolongation and bradycardia), ophthalmologic assessment (vision disorders in ~60% of patients), chest imaging/respiratory symptoms (interstitial lung disease/pneumonitis) |
| Handling Protection | Standard precautions for oral targeted therapy apply; institutional cytotoxic drug handling protocols recommended given antineoplastic classification |

---

## Safety Considerations

Please refer to the package insert for safety information. Based on published literature, clinically significant toxicities known to require active monitoring include:

- **Hepatotoxicity**: Fatal fulminant liver failure has been reported (case report PMID 26898609); LFT elevation is common and may require dose interruption
- **Cardiotoxicity**: Simultaneous QT prolongation, bradycardia, and ventricular arrhythmia have been reported (PMID 29717400); ECG monitoring is essential
- **Interstitial Lung Disease / Pneumonitis**: Drug-induced organizing pneumonia reported in ROS1-positive NSCLC (PMID 37062732); requires early recognition and corticosteroid management
- **Dermatologic reactions**: Erythema multiforme reported (PMID 25994067); monitor for skin changes

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lung germ cell tumor with confirmed ALK rearrangement or MET amplification represents a biologically coherent but extremely rare target population; the MATCH platform trial (NCT02465060) and a prior ALK-positive basket Phase 1B study (NCT01121588) provide the closest available clinical evidence framework, and the cross-histology ALK inhibitor literature establishes a mechanistic basis for biomarker-selected investigation.

**To proceed, the following is needed:**

- **Biomarker profiling**: Mandatory ALK FISH/IHC, ROS1 FISH, and MET amplification by NGS on tumor tissue before any crizotinib use — no biomarker confirmation means no treatment rationale
- **MOA data retrieval**: Query DrugBank API (DB08865) to populate the currently missing mechanism of action data
- **Package insert / safety data**: Retrieve FDA-approved Xalkori® labeling (currently absent from evidence pack) and complete the safety section before clinical decision-making
- **MATCH trial sub-group review**: Determine whether ALK-positive germ cell or rare non-NSCLC lung histology patients have been enrolled and what outcomes data are available (NCT02465060 results database)
- **Next-generation ALK inhibitor consideration**: Given that crizotinib resistance develops within ~12 months in NSCLC and crizotinib has insufficient ALK kinase potency in some tumor contexts (neuroblastoma), alectinib or lorlatinib may be superior options if a case is confirmed ALK-positive — a comparative rationale statement should be prepared
- **Compassionate use / expanded access pathway**: If a confirmed ALK-positive lung germ cell tumor case is identified, initiate contact with Pfizer for expanded access or identify an active basket trial with available ALK inhibitor slots
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

