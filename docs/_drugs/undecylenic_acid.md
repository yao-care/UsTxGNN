---
layout: default
title: Undecylenic Acid
parent: 僅模型預測 (L5)
nav_order: 1275
evidence_level: L5
indication_count: 7
---

# Undecylenic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Undecylenic Acid: From Traditional Antifungal Use to Dermatophytosis of the Groin and Perianal Area

## One-Sentence Summary

> Undecylenic acid is a long-chain unsaturated fatty acid historically used as an OTC topical antifungal (e.g., in older US products such as Desenex/Cruex) for superficial dermatophyte infections; a formal original-indication record is not present in this evidence pack.
> The TxGNN model predicts it may be effective for **Dermatophytosis of Groin and Perianal Area (tinea cruris)**,
> but currently **no clinical trials** and **no published literature** support this specific prediction — the evidence rests on mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the current dataset (rationale notes historical OTC topical use for tinea corporis/cruris) |
| Predicted New Indication | Dermatophytosis of groin and perianal area (tinea cruris) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocked by data gap DG002). Based on the information present in this evidence pack, undecylenic acid is a long-chain unsaturated fatty acid with a known dermatophyte membrane-disrupting effect, and was historically marketed as an OTC topical antifungal for tinea corporis and tinea cruris. Its efficacy in superficial dermatophyte infections has been documented in older formulations, and mechanistically this activity would plausibly extend to dermatophytosis of the groin and perianal area, since this condition is caused by the same class of organisms.

An important caveat flagged directly in the evidence pack's own rationale: this top-ranked prediction largely overlaps with the drug's **already-known traditional use** rather than representing a genuinely novel repurposing opportunity. The high TxGNN score likely reflects the model recognizing an established pharmacological pattern rather than uncovering new therapeutic potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Currently no marketing authorization records are available — the drug is not marketed (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/FDA label warnings and contraindications are recorded as a blocking data gap (DG001) — this must be resolved before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication carries only mechanism-level evidence (L4, decision stage S1 "Research Question") with zero supporting clinical trials or literature, the drug is not currently marketed, and a blocking safety data gap (TFDA/FDA warnings and contraindications) prevents even an initial S1 safety screen. The prediction also appears to substantially overlap with the drug's known traditional antifungal use rather than reflecting a novel therapeutic direction.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) to resolve blocking gap DG001
- Confirmed mechanism of action via DrugBank API (DG002)
- Documentation of the drug's actual original/approved indication(s), currently absent from this record
- Prospective clinical or observational evidence specific to dermatophytosis of the groin and perianal area
- Confirmation of current market/licensing status before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

