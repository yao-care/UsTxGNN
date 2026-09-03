---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 911
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Antineoplastic/Antirheumatic Therapy to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate (DrugBank DB00563) is a long-established antifolate agent used broadly across oncology and autoimmune disease; specific original-indication records were not available in this evidence pack. The TxGNN model's top-ranked prediction is **Pulmonary Blastoma**, but currently **0 clinical trials** and **0 publications** support this specific link — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory records (no TFDA/market license data returned); methotrexate is broadly known as an antineoplastic/antirheumatic agent |
| Predicted New Indication | Pulmonary Blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on generally known pharmacology, methotrexate belongs to the antifolate (dihydrofolate reductase inhibitor) class of antimetabolite chemotherapy agents, which broadly inhibits DNA/RNA synthesis in rapidly dividing cells.

Pulmonary blastoma is an extremely rare, aggressive pulmonary malignancy with mixed epithelial and mesenchymal components. In principle, an antimetabolite chemotherapy agent could have some theoretical activity against such a rapidly proliferating tumor, consistent with methotrexate's general use in other malignancies. However, this rationale is purely mechanistic extrapolation — there is no direct or indirect clinical evidence (trial or literature) connecting methotrexate specifically to pulmonary blastoma in the data available here.

Notably, this is the highest-scoring candidate in the TxGNN output but also the one with the weakest evidentiary support among the 10 candidates in this evidence pack — other predicted indications for methotrexate (e.g., Hodgkin's lymphoma, ranked #5) carry substantially more clinical trial and literature backing (see Conclusion below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Cytotoxicity

Methotrexate is a conventional cytotoxic agent (antimetabolite / folate antagonist class), consistent with its long-standing use in oncology.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antimetabolite, folate antagonist) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications data is flagged as a Blocking data gap (DG001) — this prevents the candidate from entering the S1 safety pre-assessment stage.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a TxGNN model score (L5 evidence level) with no clinical trials or literature identified for methotrexate in pulmonary blastoma, and no TFDA safety data is currently available to support even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA label/insert data (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action data via DrugBank API — currently a High-severity data gap
- Any preclinical or case-level evidence specific to pulmonary blastoma to move beyond L5
- Consider reprioritizing evaluation toward the higher-evidence candidates in this same evidence pack — notably Hodgkin's lymphoma (L2, decision stage S2, "Proceed with Guardrails"), which has direct historical trial evidence (e.g., VBM regimen) and substantially more supporting literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

