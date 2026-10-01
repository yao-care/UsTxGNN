---
layout: default
title: Nizatidine
parent: Model Prediction Only (L5)
nav_order: 975
evidence_level: L5
indication_count: 7
---

# Nizatidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Nizatidine: From an Unlisted Original Indication to Active Peptic Ulcer Disease

## One-Sentence Summary

Nizatidine is a marketed H2-receptor antagonist (an acid-suppressing drug), but the supplied data do not state its original approved indication.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, but the supplied Evidence Pack contains **0 clinical trials** and **0 publications** for this specific prediction.
The prediction is model-only, and it may describe an existing labeled use rather than true repurposing. This has not been verified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (all approved-indication text fields are empty) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 (all listed as generic ANDA applications) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, nizatidine is an H2-receptor antagonist that suppresses gastric acid secretion. Because acid suppression is central to ulcer healing, the drug is mechanistically well suited to peptic ulcer disease.

Nizatidine's known use in duodenal and gastric ulcer suggests this prediction may reflect an existing indication rather than a new one. The Evidence Pack does not support or refute this. The original indication and label text are both missing, so the relationship between the original and predicted indications cannot be confirmed from the supplied data. This should be checked against the current US label.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All five listed authorizations are generic (ANDA) applications. Two entries are identical duplicates (ANDA076178), so four unique authorizations are shown. Approved-indication text is empty in the supplied data, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076178 | Nizatidine | Capsule | Epic Pharma, LLC |
| ANDA090576 | Nizatidine | Solution | Amneal Pharmaceuticals LLC |
| ANDA075616 | Nizatidine | Capsule | Actavis Pharma, Inc. |
| ANDA077314 | Nizatidine | Capsule | Dr Reddy's Laboratories Limited |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no trials or literature for this entry, and the original indication and mechanism data are missing. Nizatidine's ulcer use may already be labeled, so it cannot be treated as repurposing until verified.

**Other predictions in this pack (for context):**
- Gastrojejunal ulcer (score 99.94%) and gastroduodenitis (score 99.58%) are rated L4 and Research Question. Their evidence is indirect, drawn from duodenal and gastric ulcer studies and NSAID-related injury studies.
- The remaining predictions (peptic ulcer perforation, duodenal obstruction, duodenogastric reflux, multiple endocrine neoplasia) have weak mechanistic links and stay at Hold.

**To proceed, the following is needed:**
- The current US package insert, to confirm the approved indications and to fill the missing warnings and contraindications
- Detailed mechanism of action data (MOA) from DrugBank
- A targeted literature search for this indication, since the current results for this entry are empty
- A drug-interaction query, which returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

