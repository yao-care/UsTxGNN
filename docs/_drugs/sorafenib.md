---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 1175
evidence_level: L5
indication_count: 10
---

# Sorafenib
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

# Sorafenib: From Hepatocellular Carcinoma to Liposarcoma

## One-Sentence Summary

> Sorafenib is a multikinase inhibitor whose established indications (per literature within this evidence pack) include hepatocellular carcinoma and renal cell carcinoma.
> The TxGNN model predicts it may be effective for **Liposarcoma**,
> with **2 clinical trials** and **8 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatocellular Carcinoma *(no `taiwan_regulatory.licenses` or `drug.original_indications` entries in this evidence pack; inferred from literature evidence, e.g. PMID 40716153, PMID 31118247)* |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The `drug.original_moa` field in this evidence pack is not populated. However, literature captured elsewhere in the pack (e.g. PMID 15466206, Wilhelm et al. 2004) directly characterizes sorafenib (BAY 43-9006) as a bi-aryl urea multikinase inhibitor that suppresses the RAF/MEK/ERK signaling pathway and blocks receptor tyrosine kinases involved in tumor progression and angiogenesis — including VEGFR and PDGFR-β.

Soft tissue sarcomas, including liposarcoma, frequently exhibit PDGFR pathway activation and are angiogenesis-dependent, giving a plausible mechanistic bridge from sorafenib's known anti-VEGFR/PDGFR activity in hepatocellular and renal cancers to liposarcoma. This is not purely theoretical: the SWOG-directed intergroup trial S0505 (PMID 21751200, a completed Phase 2 RCT) directly tested sorafenib in advanced soft tissue sarcomas, and a dedicated Phase 2 trial (NCT00217620, BAY-9006/sorafenib) enrolled 51 patients with advanced soft tissue sarcomas — a category that includes liposarcoma subtypes.

One caveat: the other clinical trial linked to this prediction (NCT02048371, SARC024) actually tested **regorafenib**, not sorafenib, and appears to be a data-linkage artifact rather than direct evidence (flagged as Grade C relevance in the pack). The liposarcoma-specific signal therefore rests on broader soft-tissue-sarcoma trial data rather than a liposarcoma-dedicated trial, which is why the evidence level is capped at L2 rather than L1.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | BAY-9006 (sorafenib) tested in advanced soft tissue sarcomas, a category encompassing liposarcoma; sorafenib may block enzymes needed for cell growth and blood flow to tumors. (Relevance: B — direct but broad histology trial) |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 studied oral **regorafenib** (not sorafenib) in selected sarcoma subtypes. Drug mismatch — likely a data-linkage artifact; low direct relevance. (Relevance: C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | RCT (Phase 2) | Cancer | SWOG-directed intergroup trial S0505: sorafenib evaluated in advanced soft tissue sarcomas; sorafenib targets RAF, VEGFR1-3, PDGFR-B, FLT3, and c-KIT, pathways relevant to STS. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven therapy for soft tissue sarcomas; notes trabectedin's high activity in myxoid liposarcoma and discusses targeted agent rationale by subtype. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Medical treatment of soft tissue sarcomas by histological subtype, covering targeted therapy options including kinase inhibitors. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | Reviews sarcoma patient-derived orthotopic xenograft (PDOX) models identifying effective combination therapies including CDK inhibitors, relevant to targeted therapy rationale in sarcoma. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 | Annals of Surgical Oncology | Neoadjuvant conformal radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma, based on preclinical synergy between antiangiogenic therapy and radiotherapy. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Molecular Cancer Therapeutics | Sorafenib inhibits growth and MAPK signaling in malignant peripheral nerve sheath tumor cells and dedifferentiated liposarcoma cell lines (LS141, DDLS). |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical (xenograft) | American Journal of Pathology | Dedifferentiated liposarcoma xenograft models reveal PTEN down-regulation as a malignant signature and response to PI3K pathway inhibition — informs combination targeted-therapy rationale. |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case report | Anti-Cancer Drugs | Case report of response to trabectedin in synovial sarcoma with lung metastases — supportive of targeted/non-cytotoxic agent activity in sarcoma family, though not sorafenib-specific. |

---

## US Market Information

No marketing authorization records are present in this evidence pack for the target market region (`taiwan_regulatory.total_licenses = 0`, `market_status = 未上市 / Not Marketed`, `licenses = []`). Sorafenib is marketed internationally (e.g., as Nexavar) for other indications per the clinical trial literature above, but no local license data is available to summarize here.

---

## Cytotoxicity

**This drug is antineoplastic** — all predicted new indications are cancers, and cited literature repeatedly characterizes sorafenib as a multikinase inhibitor used in first-line treatment of hepatocellular carcinoma.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor: RAF/MEK/ERK pathway, VEGFR, PDGFR-β) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this evidence pack flags TFDA/local package insert warnings and contraindications as a **Blocking** data gap (DG001) — this must be resolved before any Stage 1 safety review.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT (SWOG S0505) and a dedicated Phase 2 trial directly evaluated sorafenib in advanced soft tissue sarcoma populations that include liposarcoma, and the PDGFR-β/VEGFR mechanistic rationale is well supported by preclinical liposarcoma-specific data (PMID 18413802, 23416162). However, no liposarcoma-dedicated Phase 2/3 trial exists, and one linked trial (NCT02048371) is a drug mismatch, so evidence should be treated as guardrailed rather than definitive.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action documentation directly attributed to `drug.original_moa` (High priority gap, DG002)
- Liposarcoma-subtype-specific trial data (current evidence is largely at the broader soft-tissue-sarcoma level)
- Local market/licensing data, since this drug is currently unlicensed/not marketed in the target jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

