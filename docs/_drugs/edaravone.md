---
layout: default
title: Edaravone
parent: 僅模型預測 (L5)
nav_order: 641
evidence_level: L5
indication_count: 2
---

# Edaravone
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

# Edaravone: From ALS / Acute Ischemic Stroke to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Edaravone is a free-radical scavenger (antioxidant) whose established clinical uses are amyotrophic lateral sclerosis (ALS) and acute ischemic stroke — though this candidate record has no formally sourced Taiwan license data confirming an original indication (data gap). The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency**, an ultra-rare inherited coagulation disorder, but this prediction is currently supported by **zero clinical trials** and **zero publications**. A second, lower-ranked candidate (Factor V excess with spontaneous thrombosis) shows the same pattern of high model score but no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Taiwan license records (drug is not marketed in Taiwan); per evidence pack rationale, edaravone's known clinical uses are ALS and acute ischemic stroke |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record (flagged as a High-severity data gap). Based on known information, edaravone is a free-radical scavenger/antioxidant, with proven efficacy in ALS and acute ischemic stroke — conditions where oxidative stress contributes to neuronal injury.

Heparin cofactor 2 deficiency, by contrast, is a rare autosomal-dominant coagulation disorder caused by mutations in the *SERPIND1* (HCF2) gene, leading to a prothrombotic tendency through impaired thrombin inhibition — a protein-function defect rather than an oxidative-stress-driven pathology.

The evidence pack's own mechanistic assessment concludes that no known or biologically plausible pathway connects edaravone's antioxidant activity to heparin cofactor deficiency's coagulation-factor pathology. The high TxGNN score (99.47%) should therefore be interpreted as a knowledge-graph similarity signal rather than mechanistic validation. The same caveat applies to the second-ranked candidate, Factor V excess with spontaneous thrombosis (score 99.06%), where no literature or trial evidence links edaravone to thrombosis-pathway modulation either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN knowledge-graph score (L5, model prediction only) — there are no clinical trials, no published literature, and no established mechanistic link between edaravone's antioxidant activity and this rare coagulation disorder. Combined with a Blocking-severity gap in TFDA label/safety data, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA (or originating regulator) label with warnings/contraindications — currently a Blocking data gap
- Confirmed mechanism of action (DrugBank query) — currently a High-severity data gap
- Preclinical or mechanistic studies establishing a biological rationale linking free-radical scavenging to heparin cofactor 2 / coagulation-factor regulation
- Any case reports or observational data in rare coagulation disorders, given the ultra-low prevalence of both target conditions makes RCTs unlikely
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

