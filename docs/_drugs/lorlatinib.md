---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 871
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor whose established use — evident from literature attached to other candidates in this evidence pack — is ALK-positive non-small cell lung cancer (NSCLC). The TxGNN model's top-ranked prediction for this drug is **Gingival Fibromatosis**, but this prediction is supported by **0 clinical trials** and **0 publications** — it rests on the model score alone, with no biological rationale identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) — inferred from literature evidence attached to other ranked candidates in this pack; no formal license record exists in the evidence pack itself |
| Predicted New Indication | Gingival Fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lorlatinib in this evidence pack (flagged as a High-severity data gap, DG002). Based on literature evidence collected elsewhere in this pack (e.g., PMID 38554546, 35534623), lorlatinib is known to be a brain-penetrant, third-generation ALK/ROS1 tyrosine kinase inhibitor, with proven efficacy in ALK-positive NSCLC (CROWN trial, phase 3 RCT).

For this specific top-ranked prediction, however, the model itself provides no supporting clinical trial or literature evidence, and the accompanying rationale explicitly states: *"no clinical or mechanistic evidence exists; this is a TxGNN score alone, with no plausible biological link that can be inferred."* Gingival fibromatosis is a benign, largely genetic/fibrotic gum condition with no known relationship to ALK signaling. There is therefore no mechanistic bridge connecting lorlatinib's known pharmacology to this predicted indication — the prediction should be treated as an unvalidated model output, not a repurposing hypothesis with biological grounding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

*(Lorlatinib is an antineoplastic/targeted oncology agent; original indication — ALK+ NSCLC — is a malignancy per literature evidence in this pack.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Formal DrugBank/label toxicity data not available in this evidence pack. Literature attached to other ranked candidates (PMID 40287137, 39537504, 33789526, 31985497) reports hyperlipidemia, weight gain, edema, and rare pulmonary toxicity (ARDS) as recognized adverse events; myelosuppression is not a prominent reported signal — likely Low, but unconfirmed by primary label data |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Based on literature-reported adverse events: lipid panel (cholesterol, triglycerides), weight/BMI, renal function, pulmonary symptoms; CBC and liver function per standard oncology monitoring practice |
| Handling Protection | Oral antineoplastic — handle per institutional hazardous drug protocols; specific handling classification not confirmed in this evidence pack, refer to package insert/SDS |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Gingival Fibromatosis) has zero supporting clinical trials or publications and no identifiable mechanistic link to lorlatinib's known pharmacology — it is a model score with no corroborating evidence (L5/S0).

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism of action data (currently a High-severity data gap, DG002)
- Independent biological or preclinical rationale connecting ALK inhibition to gingival fibromatosis, if this candidate is to be pursued further
- Note for the review team: several lower-ranked candidates in this evidence pack (ranks 4, 5, 7, 10) show literature that does not match their assigned `disease_name` — these appear to be TxGNN disease-ontology mapping errors (e.g., rank 7's literature is entirely about ALK-driven neuroblastoma, not "lung germ cell tumor"; rank 5's literature is entirely about the already-approved ALK+ NSCLC indication, not "lung benign neoplasm"). These mislabeled candidates should be re-triaged with corrected disease labels before being scored, as they may contain more clinically meaningful signal than the current top-ranked, evidence-free prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

