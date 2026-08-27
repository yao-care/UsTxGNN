---
layout: default
title: Nelarabine
parent: 僅模型預測 (L5)
nav_order: 959
evidence_level: L5
indication_count: 1
---

# Nelarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Nelarabine: From T-cell Acute Lymphoblastic Leukemia/Lymphoma to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine (DrugBank DB01280) is a purine nucleoside analog chemotherapy agent used to treat T-cell acute lymphoblastic leukemia/lymphoma. The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis (RRMS)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph inference with no direct empirical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | T-cell acute lymphoblastic leukemia/lymphoma (known use; not documented in Taiwan regulatory records — drug is not marketed in Taiwan) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data (DrugBank `original_moa`) is not currently available for this drug (data gap DG002). Based on the model's own rationale, nelarabine is a prodrug of ara-G, activated by deoxyguanosine kinase (dGK), and produces highly selective cytotoxicity against T-cells — this is the pharmacological basis for its approved use in T-cell leukemia/lymphoma.

RRMS is a T-cell–mediated (particularly Th17/CD8+) autoimmune demyelinating disease. TxGNN's inference rests on a topological similarity in the knowledge graph — both conditions involve "T-cell" related nodes — rather than on any direct pharmacological or clinical validation of T-cell–selective cytotoxicity as a treatment strategy for MS.

Critically, the evidence pack itself flags a mechanistic contradiction: nelarabine has well-documented, severe, dose-limiting neurotoxicity (peripheral neuropathy, demyelination-like CNS symptoms, and even reversible posterior leukoencephalopathy syndrome). This is directly at odds with the neuroprotective goal of MS therapy, making the biological plausibility of this prediction low despite the high TxGNN score.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Nelarabine is not marketed in Taiwan (0 licenses on record), so no NDA/product information is available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, neurological examination (dose-limiting neurotoxicity has been reported), liver and renal function |
| Handling Protection | Standard cytotoxic/hazardous drug handling protocols apply |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but evidence level is L5 — there are zero clinical trials or publications supporting nelarabine in RRMS, and the drug's known dose-limiting neurotoxicity conflicts mechanistically with the neuroprotective goals of MS treatment.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) retrieval — currently a blocking data gap (DG001)
- DrugBank-sourced mechanism of action confirmation (DG002)
- Preclinical or mechanistic studies specifically evaluating T-cell–selective cytotoxic agents in demyelinating/autoimmune CNS disease models
- Any real-world or case-level safety data addressing whether neurotoxicity risk is compatible with an MS patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

