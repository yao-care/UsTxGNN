---
layout: default
title: Sonidegib
parent: 僅模型預測 (L5)
nav_order: 1174
evidence_level: L5
indication_count: 10
---

# Sonidegib
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

# Sonidegib: From Basal Cell Carcinoma to Broader Skin Cancer Indications

## One-Sentence Summary

Sonidegib is an oral Smoothened (SMO)/Hedgehog-pathway inhibitor whose approved use for advanced basal cell carcinoma (BCC) is documented in the literature evidence collected here, though structured regulatory license data is not present in this dataset. TxGNN's highest-*evidenced* prediction extends this into the broader **Skin Cancer** category, backed by **10 clinical trials** (including the pivotal BOLT study) and **20 publications**. Nine additional candidates were also predicted by the model, but only one — Xeroderma Pigmentosum-associated BCC — has any supporting evidence (a single case report); the rest are score-only (L5) and should be treated as hypotheses, not findings.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced Basal Cell Carcinoma (per literature evidence, e.g. PMID 26323341, 31545507; no structured regulatory record available in this dataset) |
| Predicted New Indication | Skin Cancer (broader NMSC category, encompassing locally advanced/metastatic BCC) |
| TxGNN Prediction Score | 99.76% (rank 6553/full candidate list) |
| Evidence Level | L2 (multiple completed Phase 2 RCTs, including the registrational BOLT trial; no completed Phase 3) |
| US Market Status | Not Marketed (per this dataset; no license record captured) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`). However, the literature evidence collected under this candidate independently confirms the mechanism: sonidegib is described as "an orally bioavailable, small molecule, Smoothened (SMO) receptor antagonist" that blocks Hedgehog pathway signalling (PMID 26323341), and multiple reviews confirm its established role in locally advanced and metastatic BCC via this mechanism (PMID 31545507 — BOLT study, PMID 27636236, PMID 33888008).

Because BCC *is* a form of skin cancer, TxGNN's prediction of "skin cancer" as a repurposing target largely reflects and extends an indication the drug already addresses, rather than identifying a mechanistically distant new disease. This is analogous to a fluoropyrimidine predicted to work in a related GI tumour type: the underlying pathway (aberrant Hedgehog/SMO signalling) is shared across BCC and other cutaneous malignancies with similar oncogenic drivers, which is why multiple trials have also explored sonidegib combinations (with buparlisib, pembrolizumab, photodynamic therapy) across a wider range of advanced solid/skin tumours (NCT02303041, NCT06623201, NCT04007744).

A second, more genuinely novel signal in this dataset is **Xeroderma Pigmentosum (XP)** (rank 2, score 99.87%). XP patients have defective DNA repair and develop multiple BCC lesions; a 2026 case report (PMID 41862093) describes sonidegib successfully treating multiple BCCs in an XP patient. The mechanistic link here is indirect — sonidegib treats the BCC complication of XP, not the underlying DNA-repair defect — but it represents a plausible, evidence-anchored label-extension use case within a rare, high-need population.

---

## Clinical Trial Evidence
*(for the primary predicted indication: Skin Cancer)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01327053](https://clinicaltrials.gov/study/NCT01327053) | Phase 2 | Completed | 230 | BOLT study — efficacy/safety of two sonidegib doses in locally advanced or metastatic BCC; basis for regulatory approval |
| [NCT00961896](https://clinicaltrials.gov/study/NCT00961896) | Phase 2 | Completed | 18 | Topical LDE225 (sonidegib) in Gorlin syndrome-associated BCC; PoC safety/PK/PD |
| [NCT03534947](https://clinicaltrials.gov/study/NCT03534947) | Phase 2 | Completed | 16 | Neoadjuvant sonidegib before surgery/imiquimod for BCC in cosmetically sensitive sites |
| [NCT01576666](https://clinicaltrials.gov/study/NCT01576666) | Phase 1 | Completed | 120 | Dose-escalation of sonidegib + buparlisib in advanced solid tumours (breast, pancreatic, colorectal, glioblastoma) |
| [NCT01033019](https://clinicaltrials.gov/study/NCT01033019) | Phase 2 | Terminated | 25 | Topical sonidegib cream in sporadic superficial/nodular BCC |
| [NCT02303041](https://clinicaltrials.gov/study/NCT02303041) | Phase 2 | Terminated | 10 | Sonidegib + buparlisib in metastatic/advanced BCC |
| [NCT04007744](https://clinicaltrials.gov/study/NCT04007744) | Phase 1 | Active, not recruiting | 36 | Sonidegib + pembrolizumab in advanced solid tumours |
| [NCT06623201](https://clinicaltrials.gov/study/NCT06623201) | Phase 1 | Recruiting | 20 | Sonidegib combined with blue-light photodynamic therapy for multiple BCC lesions |
| [NCT05463757](https://clinicaltrials.gov/study/NCT05463757) | N/A (registry) | Recruiting | 80 | Real-world Netherlands registry comparing vismodegib vs. sonidegib in advanced/multiple BCC |
| [NCT01757327](https://clinicaltrials.gov/study/NCT01757327) | Phase 2 | Withdrawn | 0 | Planned study of Hedgehog inhibitor on disseminated tumour cells in ER-negative/HER2-negative breast cancer (never enrolled) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31545507](https://pubmed.ncbi.nlm.nih.gov/31545507/) | 2020 | RCT (long-term follow-up) | Br J Dermatol | 42-month BOLT study analysis confirming durable efficacy/safety of sonidegib in advanced BCC |
| [37604067](https://pubmed.ncbi.nlm.nih.gov/37604067/) | 2023 | Guideline | Eur J Cancer | European interdisciplinary consensus guideline on BCC diagnosis/treatment (2023 update) |
| [31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/) | 2019 | Guideline | Eur J Cancer | European consensus-based guidelines on BCC diagnosis and treatment |
| [37326221](https://pubmed.ncbi.nlm.nih.gov/37326221/) | 2023 | Drug safety review | Expert Opin Drug Saf | Efficacy and safety evaluation of sonidegib for BCC management |
| [26323341](https://pubmed.ncbi.nlm.nih.gov/26323341/) | 2015 | Drug profile | Drugs | "Sonidegib: First Global Approval" — SMO antagonist mechanism, Swiss approval for advanced BCC |
| [33888008](https://pubmed.ncbi.nlm.nih.gov/33888008/) | 2021 | Expert opinion | Expert Opin Drug Saf | Sonidegib efficacy, safety and tolerability review |
| [27636236](https://pubmed.ncbi.nlm.nih.gov/27636236/) | 2016 | Review | Expert Rev Anticancer Ther | Safety and efficacy of sonidegib in locally advanced BCC |
| [32759706](https://pubmed.ncbi.nlm.nih.gov/32759706/) | 2020 | Review | Int J Mol Sci | Comprehensive review of BCC biology and treatment resistance mechanisms |
| [33725197](https://pubmed.ncbi.nlm.nih.gov/33725197/) | 2021 | Review | Curr Treat Options Oncol | Neoadjuvant sonic hedgehog inhibitor use in locally advanced/multiple BCC |
| [26566923](https://pubmed.ncbi.nlm.nih.gov/26566923/) | 2016 | Review | Int J Dermatol | Oral hedgehog inhibitors (vismodegib, sonidegib) for advanced non-melanoma skin cancer |

---

## Other TxGNN-Predicted Candidates (Exploratory, Low Evidence)

This evidence pack contained 10 predicted indications in total. Aside from Skin Cancer above, only one has any literature support:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|---|
| 2 | Xeroderma Pigmentosum | 99.87% | L4 | Research Question | Single 2026 case report (PMID 41862093) treating XP-associated multiple BCC with sonidegib |
| 1 | Medulloblastoma with extensive nodularity | 99.90% | L5 | Hold | Strong mechanistic rationale (SHH-driven medulloblastoma) but zero sonidegib-specific trials/literature in this pack |
| 3 | Annular epidermolytic ichthyosis | 99.83% | L5 | Hold | Keratin-gene disorder; no known Hedgehog-pathway link |
| 4 | Epidermolysis bullosa simplex w/ mottled pigmentation | 99.79% | L5 | Hold | No mechanistic or evidentiary link identified |
| 5 | Trichothiodystrophy, photosensitive | 99.77% | L5 | Hold | Theoretical link via shared photosensitivity/DNA-repair biology with XP; unproven |
| 7 | Cutaneous adenocystic carcinoma | 99.75% | L5 | Hold | No supporting data |
| 8 | Benign neoplasm of sweat gland | 99.74% | L5 | Hold | No supporting data |
| 9 | Eccrine carcinoma | 99.72% | L5 | Hold | No supporting data |
| 10 | "Obsolete" cataract–microcephaly–failure to thrive–kyphoscoliosis syndrome | 99.71% | L5 | Hold | Obsolete disease ontology term; recommend excluding from further review |

These L5 candidates should not be advanced without new evidence — high TxGNN scores here likely reflect topological/embedding similarity rather than validated pharmacology.

---

## US Market Information

No license records are present in this dataset (`total_licenses: 0`). Sonidegib's known first global approval (Switzerland, per PMID 26323341) and subsequent BCC indications elsewhere are documented only through the literature evidence above, not through a structured regulatory record in this pack. This is itself a data gap that should be closed before any regulatory-facing decision (see Next Steps).

---

## Cytotoxicity

Sonidegib qualifies as antineoplastic based on its established use in advanced/metastatic basal cell carcinoma (per literature evidence) and its classification as a Hedgehog-pathway/Smoothened inhibitor.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Smoothened/Hedgehog pathway inhibitor) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Low — SMO inhibitors are not characteristically myelosuppressive; no hematologic toxicity data present in this pack |
| Emetogenicity Classification | Low, consistent with the targeted-therapy drug class |
| Monitoring Items | Creatine kinase (musculoskeletal adverse effects are class-characteristic), renal function, pregnancy status (embryo-fetal toxicity is a known class warning for Hedgehog inhibitors) |
| Handling Protection | No cytotoxic-handling data in this pack; as a class, Hedgehog pathway inhibitors carry embryo-fetal toxicity warnings requiring exposure precautions for pregnant staff/patients — confirm against the actual package insert before implementing handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Skin Cancer prediction is supported by a robust body of completed Phase 2 clinical trials (including the pivotal BOLT study) and 20 publications, but this largely confirms/extends an already-known mechanism of action (BCC treatment) rather than revealing a mechanistically novel indication. The remaining 9 predicted indications lack sufficient evidence (8 are L5, score-only; 1 is a single case report) and must remain in a research/monitoring status.

**To proceed, the following is needed:**
- Structured regulatory data (FDA/EMA license records) to resolve the "Not Marketed" data gap, since literature evidence indicates the drug does have approvals elsewhere
- Structured DrugBank MOA field to replace the current data gap
- TFDA/FDA package insert warnings and contraindications (currently a Blocking data gap per `DG001`)
- For Xeroderma Pigmentosum: additional case reports or a small case series before elevating beyond "Research Question"
- For all L5 candidates: no action beyond periodic literature monitoring until new evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

