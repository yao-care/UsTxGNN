---
layout: default
title: Capmatinib
parent: 僅模型預測 (L5)
nav_order: 493
evidence_level: L5
indication_count: 2
---

# Capmatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# CAPMATINIB: From Non-Small Cell Lung Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Capmatinib is a selective MET receptor tyrosine kinase inhibitor, clinically established in oncology for treatment of MET-altered non-small cell lung cancer.
The TxGNN model predicts it may have utility in **Rheumatoid Arthritis** via the HGF/MET signaling axis implicated in synovial inflammation,
with **0 dedicated clinical trials** and **1 peripheral publication** (a broad kinase inhibitor class review) currently available — representing an early-stage mechanistic hypothesis only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-small cell lung cancer (MET-altered) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L4 |
| US Market Status | Not Registered (0 licenses in current database) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on pharmacological class context, Capmatinib belongs to the MET kinase inhibitor family — it selectively targets MET (mesenchymal-epithelial transition factor) receptor tyrosine kinase, blocking HGF (hepatocyte growth factor)-mediated downstream signaling through the PI3K/AKT and RAS/MAPK pathways. Its clinical utility is particularly established in cancers harboring MET exon 14 skipping mutations or MET gene amplification.

The biological rationale for the RA prediction rests on the HGF/MET axis in joint pathology. HGF concentrations are elevated in the synovial fluid of RA patients, and MET receptors are expressed on fibroblast-like synoviocytes (FLS) — the stromal cells responsible for synovial hyperplasia and cartilage destruction in RA. In principle, MET inhibition could attenuate FLS proliferation and invasiveness. Class-level plausibility is additionally supported by the observation that imatinib (a related kinase inhibitor targeting BCR-ABL and c-Kit) has demonstrated anti-inflammatory activity in RA animal models, suggesting kinase inhibitor strategies may have broader anti-inflammatory applicability.

However, this mechanistic connection must be characterized as an indirect class-effect inference, not established evidence. RA is primarily an autoimmune disease driven by T and B cell dysregulation; MET/HGF represents only one peripheral signaling node in a complex inflammatory network. There are currently no capmatinib-specific preclinical or clinical studies in RA, and the structural pathology of RA differs substantially from the tumor microenvironment for which capmatinib was developed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | Comprehensive review of 62 FDA-approved small molecule kinase inhibitors (including capmatinib); covers mechanisms, clinical targets, and approval context across disease areas — does not specifically address RA application or MET inhibition in inflammatory disease |

---

## US Market Information

No regulatory license records found in the current database (0 NDA records). This may indicate a data pipeline gap. Refer to official regulatory sources for current market authorization status before drawing conclusions about market availability.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (MET/HGF-pathway kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.45%), the entire evidentiary base is mechanistic inference (L4) — there are no capmatinib-specific preclinical or clinical data for RA, and two critical data gaps (MOA documentation and package insert safety review) remain unresolved, making it premature to advance this candidate.

**To proceed, the following is needed:**
- **Preclinical validation**: Test capmatinib in FLS cell line proliferation/invasion assays and/or a collagen-induced arthritis (CIA) animal model to establish direct pharmacodynamic evidence
- **MOA documentation**: Retrieve complete mechanism of action data from DrugBank API (resolves DG002) to confirm target specificity relevant to RA pathology
- **Safety review**: Download and parse the official package insert to assess key warnings and contraindications applicable to an RA patient population (resolves DG001 — currently Blocking severity)
- **Class-effect benchmarking**: Systematic review of imatinib, tofacitinib, and baricitinib RA clinical data to contextualize the kinase-inhibitor class hypothesis
- **Regulatory status verification**: Confirm current FDA/TFDA authorization status and obtain full prescribing information to address the 0-license discrepancy in the current database
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

