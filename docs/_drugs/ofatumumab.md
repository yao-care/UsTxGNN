---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 983
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Ofatumumab: From Chronic Lymphocytic Leukemia to Follicular Lymphoma

## One-Sentence Summary

> Ofatumumab (DrugBank DB06650) is a fully human anti-CD20 monoclonal antibody whose established use is in chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) — confirmed within this evidence pack by the head-to-head RESONATE and DUO trials (rank 5 candidate).
> Among the TxGNN model's outputs, the strongest **evidence-backed new-indication signal** is **Follicular Lymphoma**,
> supported by **15 clinical trials** (including 2 randomized Phase 2/3 studies) and **20 publications**.
> Note: the model's raw top-ranked outputs (rank 1–2, IGHV-mutation subtype nodes; rank 4, a genetic-susceptibility node; ranks 7–8, CD20-negative tumors) carry no clinical or literature evidence and are flagged in the evidence pack itself as ontology artifacts — Follicular Lymphoma is the highest-evidence *genuinely novel* signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia / Small Lymphocytic Lymphoma (CLL/SLL) — per the RESONATE (NCT01578707) and DUO (NCT02004522) trial evidence in this pack, ofatumumab is used as monotherapy comparator/standard for relapsed-refractory CLL/SLL; no formal license record exists in this dataset |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L2 |
| US Market Status | Not marketed (per this dataset; 0 license records) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action (MOA) field is not available for this drug (flagged as data gap DG002, High severity). However, literature captured within this evidence pack (e.g. PMID 20068404, PMID 18535937, PMID 22830942) consistently describes ofatumumab as a fully human IgG1κ monoclonal antibody that binds a membrane-proximal epitope on CD20, triggering B-cell lysis via complement-dependent cytotoxicity (CDC) and antibody-dependent cell-mediated cytotoxicity (ADCC).

Follicular lymphoma is, like CLL/SLL, a CD20-positive B-cell malignancy. The mechanistic rationale is therefore direct: the same CD20-targeting activity that clears malignant B cells in CLL/SLL applies to FL's malignant B-cell clone. This is reinforced by clinical precedent — rituximab, ofatumumab's same-class predecessor, is already a backbone therapy in FL — and by the trial evidence below, which shows ofatumumab tested across frontline, maintenance, and relapsed/refractory FL settings.

By contrast, several other TxGNN outputs in this pack (IGHV-mutation subtype, pregerminal-center subtype, genetic-susceptibility node, malignant spiradenoma, Langerhans cell histiocytosis) are explicitly annotated in their own `repurposing_rationale` fields as ontology-driven artifacts lacking any CD20-relevant biological basis or supporting evidence — these were excluded from the headline signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Phase 2 | Completed | 51 | Single-agent ofatumumab in previously untreated Stage II–IV follicular NHL |
| [NCT01294579](https://clinicaltrials.gov/study/NCT01294579) | Phase 2 | Completed | 49 | Ofatumumab + bendamustine induction, followed by ofatumumab maintenance, in indolent B-NHL relapsed after rituximab |
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Phase 3 | Terminated | 346 | Ofatumumab + bendamustine vs. bendamustine alone in rituximab-unresponsive indolent B-NHL; terminated before full readout |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Phase 2 | Completed | 110 | Involved-field radiotherapy ± ofatumumab in Stage I/II FL, stratified by Bcl-2 status (MIRO trial) |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Phase 2 | Completed | 59 | Two-dose ofatumumab + CHOP as frontline therapy for untreated FL |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Phase 2 | Completed | 116 | Ofatumumab monotherapy in rituximab-refractory FL |
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2 | Completed | 135 | Ofatumumab + bendamustine ± bortezomib in untreated FL |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Phase 1 | Completed | 6 | Safety/PK of ofatumumab monotherapy in Japanese FL/CLL patients |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Phase 2 | Completed | 43 | Ofatumumab as initial systemic treatment for indolent B-cell lymphoma |
| [NCT00823719](https://clinicaltrials.gov/study/NCT00823719) | Phase 2 | Completed | 61 | Ofatumumab + ICE/DHAP salvage chemotherapy pre-autologous transplant in relapsed/refractory aggressive lymphoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | RCT (Phase 2) | Cancer | CALGB 50904: ofatumumab+bendamustine vs. ofatumumab+bendamustine+bortezomib in untreated high-risk FL |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | RCT (Phase 2) | Br J Haematol | CALGB 50901: single-agent ofatumumab efficacy in untreated low/intermediate-risk FL |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Phase 2 trial | Lancet Haematology | FIL MIRO final results: MRD-driven radiotherapy ± ofatumumab in early-stage FL |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Cohort (multicenter) | Blood | Ofatumumab monotherapy in rituximab-refractory FL; ORR 13%, modest activity in heavily pretreated disease |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Phase 2 cohort | Br J Haematol | O-CHOP (ofatumumab + CHOP) as frontline therapy for FL |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Phase 1/2 | Blood | First clinical use of ofatumumab in relapsed/refractory FL |
| [28983798](https://pubmed.ncbi.nlm.nih.gov/28983798/) | 2017 | Review | Advances in Therapy | 20-year review of rituximab (anti-CD20 class) across B-cell malignancies including FL |
| [21083037](https://pubmed.ncbi.nlm.nih.gov/21083037/) | 2010 | Review | Expert Rev Hematol | Emerging therapeutic strategies in follicular lymphoma |
| [26043777](https://pubmed.ncbi.nlm.nih.gov/26043777/) | 2015 | Review | Expert Opin Biol Ther | Ofatumumab activity across CD20+ B-cell lymphomas |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | Review | Clin Lymphoma Myeloma Leuk | Evidence-based review of anti-CD20 regimens in relapsed/refractory CLL, DLBCL, and FL |

---

## US Market Information

No marketing authorization records are present in this dataset (`total_licenses = 0`, `market_status = 未上市/Not marketed`). This does not necessarily reflect ofatumumab's actual global regulatory history — it reflects a gap in the source registry used to build this evidence pack.

---

## Cytotoxicity

Ofatumumab is an antineoplastic biologic (anti-CD20 monoclonal antibody used in B-cell malignancies), so this section applies — but it is **not** a conventional cytotoxic chemotherapy agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy — CD20-targeted monoclonal antibody (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Not directly reported in this dataset. As a monoclonal antibody, direct myelosuppression is expected to be lower than cytotoxic chemotherapy; however, the combination regimens documented above (e.g., ofatumumab+bendamustine, O-CHOP) carry the conventional myelosuppression risk of their chemotherapy partners |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential; infusion-related reaction monitoring; hepatitis B reactivation screening (standard precaution for anti-CD20 antibody class) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are marked as data gaps in this evidence pack — DG001, Blocking severity, requires TFDA-equivalent label sourcing.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two randomized Phase 2 trials (CALGB 50904, CALGB 50901) plus multiple completed single-arm Phase 2 studies support ofatumumab activity in follicular lymphoma across frontline and relapsed settings, giving L2 evidence strength. However, activity in heavily pretreated/rituximab-refractory FL is modest (ORR 13% per PMID 22389254) and one Phase 3 combination trial (NCT01077518) was terminated early — this is not yet a clear-cut Go.

**To proceed, the following is needed:**
- MOA/DrugBank mechanism-of-action data (DG002)
- Regulatory label warnings and contraindications (DG001, Blocking — required before any safety pre-screen)
- Clarification of ofatumumab's actual marketing status, since this dataset shows 0 licenses despite known historical approvals
- Head-to-head efficacy data vs. rituximab/obinutuzumab in FL to establish differentiated positioning
- Route/dosing compatibility confirmation for the FL population (currently unassessed in this pack)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

