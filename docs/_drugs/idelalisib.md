---
layout: default
title: Idelalisib
parent: 僅模型預測 (L5)
nav_order: 787
evidence_level: L5
indication_count: 10
---

# Idelalisib
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

# IDELALISIB: From B-cell Hematologic Malignancies to Mantle Cell Lymphoma

## One-Sentence Summary

Idelalisib is a selective PI3Kδ inhibitor originally developed for B-cell hematologic malignancies such as chronic lymphocytic leukemia (CLL), follicular lymphoma, and small lymphocytic lymphoma (SLL), based on literature evidence in this dataset (structured license/indication fields are not populated for this jurisdiction). The TxGNN model predicts it may also be effective for **Mantle Cell Lymphoma (MCL)**, with **9 clinical trials** and **19 publications** currently supporting this direction, though the strongest single trial in this set (NCT01796470) was terminated.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured license data (0 licenses on file); literature evidence in this pack consistently describes idelalisib (Zydelig®) as approved for relapsed CLL, follicular lymphoma, and SLL |
| Predicted New Indication | Mantle Cell Lymphoma |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available for this drug (data gap DG002). Based on evidence within the literature corpus, idelalisib is a first-in-class, orally administered, selective inhibitor of the delta isoform of phosphatidylinositol 3-kinase (PI3Kδ). PI3Kδ is expressed predominantly in hematopoietic cells and sits downstream of the B-cell receptor (BCR), where it drives proliferation and survival signaling in B-cell malignancies.

Idelalisib's established efficacy in CLL, follicular lymphoma, and SLL stems from blocking this BCR/PI3Kδ survival pathway, which is broadly active across B-cell derived neoplasms — including MCL. This provides a plausible mechanistic bridge to MCL, since MCL is also a B-cell lymphoproliferative disorder in which PI3K pathway activation contributes to pathogenesis (as reflected in several of the MCL-specific publications below).

However, the mechanistic case for MCL specifically is weaker than for CLL/iNHL: MCL's clinical response has historically been driven more strongly by BTK inhibition (e.g., ibrutinib) than by PI3Kδ inhibition, and idelalisib has shown intrinsic resistance in MCL in some preclinical models. The most directly relevant combination trial in this indication (NCT01796470, entospletinib + idelalisib) was terminated, while the strongest positive signal comes from a smaller Phase 1/randomized Phase 2 study of idelalisib + lenalidomide (NCT01838434) specifically in relapsed/refractory MCL.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1 / Randomized Phase 2 | Completed | 106 | Idelalisib + lenalidomide in relapsed/refractory MCL — direct, most relevant trial for this population |
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Safety of idelalisib combined with anti-CD20 mAb, chemotherapy, or other agents in relapsed indolent NHL, MCL, or CLL |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib + idelalisib in relapsed/refractory hematologic malignancies incl. MCL; terminated |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1b | Completed | 20 | BCL201 + idelalisib safety/tolerability in follicular lymphoma and MCL |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib as post-allogeneic HSCT maintenance in B-cell derived malignancies |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A | Completed | 121 | Real-world association of idelalisib/ibrutinib plasma concentration with side effects in hematologic malignancies including MCL |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Phase 1 | Terminated | 203 | Tirabrutinib combined with targeted anti-cancer therapies in relapsed/refractory B-cell lymphoproliferative malignancies |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Phase 1/2 | Completed | 803 | Oral pirtobrutinib in CLL/SLL/NHL; idelalisib not the study drug, indirect relevance |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A | Unknown | 464 | Quality-of-life assessment of lymphoma patients treated with oral therapies including idelalisib |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Review (Tier 1) | Cancer Discovery | The PI3Kδ inhibitor idelalisib was effective in heavily pretreated patients with MCL |
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Phase 1 clinical study | Blood | Phase 1 study of idelalisib (50–350 mg) in 40 patients with relapsed/refractory MCL; evaluated safety, DLT, ORR, PFS |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Cohort (Tier 2) | Clin Cancer Res | Idelalisib impacts MCL cell growth by disrupting translation-regulatory mechanisms |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Review (Tier 2) | Acta Pharmacol Sin | P300/CBP inhibition sensitizes MCL to idelalisib, overcoming intrinsic resistance |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Review (Tier 2) | Phytomedicine | CBX5 loss drives PI3Kδ inhibitor resistance in MCL; propolis restores sensitivity |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | — | Cancer Letters | Idelalisib enhances anti-tumor effects of CDK4/6 inhibitor palbociclib via PLK1 in B-cell lymphoma incl. MCL |
| [22361516](https://pubmed.ncbi.nlm.nih.gov/22361516/) | 2012 | — | Oncotarget | Novel targeted therapies for MCL, including PI3K/Akt pathway inhibition |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | — | Br J Haematol | Current regimens and novel agents for MCL |
| [23512567](https://pubmed.ncbi.nlm.nih.gov/23512567/) | 2013 | — | Curr Treat Options Oncol | Current and emerging therapies in MCL |
| [26360791](https://pubmed.ncbi.nlm.nih.gov/26360791/) | 2015 | — | Expert Opin Pharmacother | Overview of standard and novel treatment options for MCL |

---

## US Market Information

Idelalisib currently holds **no active marketing authorization on file** in this dataset — 0 licenses recorded and market status "Not Marketed." No product/dosage-form/indication records are available to tabulate.

---

## Cytotoxicity

Idelalisib is an antineoplastic agent (oncology indication class evident throughout the literature evidence — CLL, SLL, follicular lymphoma, MCL), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — selective PI3Kδ (phosphatidylinositol 3-kinase delta) inhibitor, not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Standard monitoring for this drug class as referenced in the literature includes CBC with differential, liver function tests, and infection surveillance; specific institutional protocols should follow the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic rationale (PI3Kδ/BCR pathway relevance to B-cell malignancies) is plausible for MCL, and one directly relevant Phase 1/randomized Phase 2 trial (NCT01838434) was completed, supporting an L2 evidence level. However, the most disease-specific combination trial (NCT01796470) was terminated, and MCL's clinical dependency is more strongly tied to BTK than PI3Kδ inhibition, so the signal is not yet strong enough for a Go or Guardrails decision.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) to close data gap DG001 before any safety evaluation
- DrugBank-confirmed mechanism of action to close data gap DG002
- Detailed efficacy outcomes (ORR, PFS) from NCT01838434 and the completed Phase 1 study (PMID 24615778)
- Clarification on why NCT01796470 was terminated (efficacy vs. safety vs. business reasons) before weighting it further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

