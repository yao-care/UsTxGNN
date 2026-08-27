---
layout: default
title: Lenvatinib
parent: 僅模型預測 (L5)
nav_order: 846
evidence_level: L5
indication_count: 10
---

# Lenvatinib
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

Using the report as specified in the v5 prompt — all fields are extracted directly from the Evidence Pack JSON below.

# Lenvatinib: From Thyroid Cancer to Liposarcoma

## One-Sentence Summary

> Lenvatinib is a multi-target tyrosine kinase inhibitor originally developed for radioactive-iodine-refractory differentiated thyroid cancer, and later expanded to hepatocellular carcinoma and renal cell carcinoma (in combination regimens).
> The TxGNN model's top-ranked new-indication signal for this drug is **Liposarcoma**, supported currently by **1 completed clinical trial** and **4 publications**.
> Evidence is still early-stage (single-arm Phase Ib/II data only, no randomized confirmation yet), so this candidate sits at a research-question stage rather than a ready-to-advance one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack — `original_indications` and `taiwan_regulatory.licenses` are both empty (see data gap DG001/DG002 below). Based on generally known drug information, lenvatinib's first approved indication was radioactive-iodine-refractory differentiated thyroid cancer. |
| Predicted New Indication | Liposarcoma (advanced adipocytic sarcoma) |
| TxGNN Prediction Score | 99.51% (0.9950719475746156) |
| Evidence Level | L2 |
| US Market Status | Not Marketed (0 licenses on record) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for lenvatinib is flagged as a data gap in this evidence pack (`original_moa: "[Data Gap]"`, item DG002). However, other entries within this same evidence pack (repurposing rationale for the renal cell carcinoma prediction, rank 7) document that lenvatinib is a multi-target tyrosine kinase inhibitor acting on VEGFR1–3, FGFR1–4, PDGFRα, KIT, and RET — a mechanism centered on blocking tumor angiogenesis. This is consistent with lenvatinib's known clinical use as an anti-angiogenic agent across several solid-tumor indications.

For liposarcoma specifically, the mechanistic rationale is combinatorial rather than monotherapy-based: the completed LEADER study (NCT03526679) paired lenvatinib's anti-angiogenic activity with eribulin, a microtubule-targeting chemotherapy already used in liposarcoma and leiomyosarcoma. The evidence pack's own rationale states that this combination "showed antiproliferative/anti-angiogenic synergy in soft-tissue sarcoma models, including dedifferentiated liposarcoma," and separately notes that CDK4 expression may serve as a prognostic/predictive biomarker for combination treatment response in this histotype.

Liposarcoma and dedifferentiated/well-differentiated subtypes are difficult-to-treat soft-tissue sarcomas with few approved systemic options, which is consistent with why an anti-angiogenic add-on to existing chemotherapy (eribulin) would be mechanistically plausible — but this remains a hypothesis supported by a single completed early-phase trial rather than confirmatory randomized data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | Completed | 30 | Single-arm study of lenvatinib + eribulin in inoperable/metastatic adipocytic sarcoma (incl. liposarcoma) and leiomyosarcoma, evaluating safety and efficacy of combining anti-angiogenic and anti-mitotic mechanisms. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase 1/2 Trial (single-arm) | Clinical Cancer Research | Primary publication of the LEADER study (NCT03526679): lenvatinib + eribulin evaluated in advanced leiomyosarcoma and liposarcoma given limited treatment options. |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical/Translational | Experimental Hematology & Oncology | CDK4 explored as a prognostic biomarker in soft tissue sarcoma, with synergistic effect of CDK4 inhibition noted in sequential treatment of dedifferentiated liposarcoma. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Research | Broad-spectrum preclinical study of eribulin combined with mechanistically distinct anticancer agents; eribulin itself has established use in liposarcoma. |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case Report | Case Reports in Oncology | Individualized treatment (targeting + surgery + chemotherapy) achieved notable tumor size reduction in a dedifferentiated liposarcoma patient with lung/abdominal metastasis. |

---

## US Market Information

Currently not marketed under this evidence pack's tracked jurisdiction — `taiwan_regulatory.total_licenses = 0` and no license records are present. This is listed as a Blocking data gap (DG001): the formal package insert/label (warnings, contraindications, approved indication text) has not yet been retrieved from the regulatory source and must be obtained before a safety pre-assessment (S1) can proceed.

---

## Cytotoxicity

*(Included because lenvatinib is an antineoplastic agent — all ten TxGNN-predicted indications in this pack are oncologic, and its mechanism, per the evidence pack's own rationale text, is a multi-target tyrosine kinase inhibitor used across cancer indications.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor — VEGFR1–3/FGFR1–4/PDGFRα/KIT/RET), not a conventional cytotoxic agent |
| Myelosuppression Risk | Not directly characterized in this evidence pack. Monotherapy myelosuppression risk is typically low for TKIs, but risk may increase when combined with cytotoxic partners such as eribulin (as used in the LEADER liposarcoma trial) — please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Not specified in this evidence pack; TKIs are generally considered low-to-moderate emetogenic risk — please confirm via package insert |
| Monitoring Items | Blood pressure (hypertension is a documented class effect for lenvatinib and other multikinase inhibitors per literature retrieved elsewhere in this pack, e.g., PMID 28796163, PMID 31547602), thyroid function, urine protein/renal function, liver function, and CBC when combined with cytotoxic agents (e.g., eribulin) |
| Handling Protection | Not specified in this evidence pack (blocked by DG001 pending TFDA/FDA label retrieval); follow institutional hazardous-drug handling policy for oral antineoplastic agents until label data is confirmed |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug–drug interaction data are all marked as data gaps or "not found" in this evidence pack — DG001 is flagged as a Blocking severity item preventing initial safety assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The liposarcoma prediction is supported only by a single completed single-arm Phase 1/2 trial (n=30) plus preclinical/case-report literature — evidence level L2, decision stage S2 ("Research Question"). This is promising as a hypothesis but not yet sufficient to proceed with guardrails.
- For context, this same evidence pack shows the TxGNN model also (re)identifies renal cell carcinoma as a lenvatinib indication with L1-level evidence (multiple completed Phase 3 RCTs, e.g., the CLEAR trial) — but that is already a globally approved use of lenvatinib, not a genuinely new repurposing candidate; it serves mainly as a sanity check on model validity. Several other ranked predictions (Xp11.2-translocation RCC, neuroblastoma-associated RCC, ovarian myxoid liposarcoma, angiolipoma, childhood kidney carcinoma, familial spontaneous pneumothorax, endocrine-cerebro-osteodysplasia syndrome) are scored L5/S0 ("Hold") due to absent clinical/mechanistic evidence and are likely knowledge-graph proximity artifacts rather than real signals.

**To proceed, the following is needed:**
- TFDA/FDA package insert extraction to resolve the Blocking data gap (DG001) before any safety pre-assessment (S1)
- DrugBank-sourced mechanism-of-action confirmation (DG002)
- A randomized or larger controlled trial in liposarcoma/soft-tissue sarcoma confirming the lenvatinib + eribulin signal from NCT03526679
- Completion of the pending drug–drug interaction (DDI) query, currently returned "not_found"
- Route/dosage-form compatibility assessment (currently marked "pending" for all ranked indications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

