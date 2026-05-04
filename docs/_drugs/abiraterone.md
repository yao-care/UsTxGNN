---
layout: default
title: Abiraterone
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 0
---

# Abiraterone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Abiraterone: Evaluation Incomplete — TxGNN Predictions Pending

## One-Sentence Summary

Abiraterone (DB05812) is a well-established CYP17A1 inhibitor used for metastatic castration-resistant prostate cancer, approved by the US FDA under the brand name Zytiga.
However, **no TxGNN repurposing predictions were generated** in this Evidence Pack, and the Taiwan TFDA query returned zero results.
This report reflects a data-limited evaluation and serves primarily as a gap analysis and triage document.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in this Evidence Pack (known: prostate cancer from US FDA approval) |
| Predicted New Indication | None — TxGNN predictions not available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction not yet generated; no supporting studies via this pipeline) |
| Taiwan Market Status | ✗ Not marketed (TFDA query returned 0 results) |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The `predicted_indications` array in this Evidence Pack is empty, indicating one of the following conditions:

1. **Pipeline incomplete**: The KG and DL prediction steps did not complete for this drug in the current run.
2. **Mapping failure**: Abiraterone (DB05812) may not have been successfully matched to the TxGNN knowledge graph node, preventing score generation.
3. **Filtered out**: Scores fell below the minimum threshold and were excluded from output.

Without a predicted indication, the core analysis sections (mechanism applicability, clinical trial evidence, literature evidence) cannot be meaningfully constructed from this Evidence Pack alone.

> ⚠️ Note: From public pharmaceutical knowledge, Abiraterone acetate (Zytiga) is a US FDA-approved CYP17A1 inhibitor for metastatic castration-resistant prostate cancer (mCRPC) and metastatic high-risk castration-sensitive prostate cancer (mCSPC). It is broadly marketed internationally. The Taiwan TFDA returning 0 results is likely a query issue (possible brand/salt name mismatch) rather than true absence from the Taiwan market.

---

## Taiwan Market Information

No Taiwan TFDA licenses were retrieved. This is likely a data quality issue:

| Query Source | Query Date | Status | Records Found |
|-------------|------------|--------|---------------|
| TFDA | 2026-03-24 | Success | 0 |

**Suggested remediation**: Re-query TFDA using the brand name "Zytiga" or the acetate salt form "Abiraterone Acetate" (醋酸阿比特龍) to capture any registered licenses.

---

## Cytotoxicity

Abiraterone is classified as an antineoplastic agent (prostate cancer) and warrants a cytotoxicity entry, though it is not a conventional cytotoxic drug.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted hormonal therapy (CYP17A1 androgen biosynthesis inhibitor) — not a conventional cytotoxic |
| Myelosuppression Risk | Low (not myelosuppressive; not a chemotherapy agent) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (ALT/AST), blood pressure, serum potassium, fluid retention; adrenocortical function if used without prednisone |
| Handling Protection | Standard oral hazardous drug precautions apply (NIOSH list); no cytotoxic IV handling requirements |

---

## Safety Considerations

All safety fields in this Evidence Pack are marked as data gaps. No DDI records were found.

> Please refer to the US FDA-approved package insert for Zytiga (abiraterone acetate) for complete warnings, contraindications, and drug interaction information. Key known safety concerns include hepatotoxicity, hypertension, hypokalemia, and adrenocortical insufficiency, particularly when co-administered with prednisone.

---

## Data Gaps Requiring Resolution

| Gap ID | Item | Severity | Remediation |
|--------|------|----------|-------------|
| DG001 | Taiwan TFDA package insert (warnings/contraindications) | Blocking | Re-query TFDA using "Zytiga" or "醋酸阿比特龍"; download and parse PDF |
| DG002 | Mechanism of action (MOA) | High | Query DrugBank API for DB05812 |
| — | TxGNN predicted indications | Critical | Re-run KG + DL prediction pipeline; verify DB05812 is mapped in `drugbank_vocab.csv` |
| — | TFDA license records | High | Re-query with alternate drug names/salt forms |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is incomplete — no TxGNN predictions were generated and all safety data is unavailable. There is insufficient structured data to evaluate any repurposing hypothesis for Abiraterone at this time.

**To proceed, the following is needed:**

- Verify that Abiraterone (DB05812) is correctly mapped in the TxGNN knowledge graph (`drugbank_vocab.csv`) and re-run the prediction pipeline
- Re-query TFDA using alternate names ("Zytiga", "醋酸阿比特龍") to retrieve Taiwan license records and package insert safety data
- Retrieve MOA from DrugBank API (DB05812) to enable mechanism applicability analysis
- Once predictions are generated, re-issue this Evidence Pack as v5 for full evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

