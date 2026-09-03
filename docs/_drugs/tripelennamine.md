---
layout: default
title: Tripelennamine
parent: 僅模型預測 (L5)
nav_order: 1265
evidence_level: L5
indication_count: 5
---

# Tripelennamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Tripelennamine: From Antihistamine to Allergic Urticaria

## One-Sentence Summary

Tripelennamine (pyribenzamine) is a first-generation H1 antihistamine with no formally recorded original indication in this evidence pack. The TxGNN model predicts it may be effective for **Allergic Urticaria**, but this is mechanistically expected rather than novel, and is currently supported only by older, low-tier literature with **no clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license/indication data recorded) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in structured form, but based on known pharmacology, Tripelennamine is a classic first-generation H1 antihistamine. It blocks histamine H1 receptors, thereby inhibiting histamine-driven vasodilation, increased vascular permeability, and pruritus — the core pathological pathway of allergic urticaria.

This is not a novel repurposing hypothesis in the traditional sense: H1 antihistamines have long been used for histamine-mediated urticaria, so the TxGNN prediction largely reproduces a well-established pharmacological class effect rather than identifying an unexpected new use.

The mechanism plausibly applies because allergic and cold urticaria are both mast cell/histamine-mediated conditions, directly matching the drug's known receptor-blocking action. However, supporting evidence is limited to case reports and reviews from the 1950s, with no modern clinical trials confirming efficacy or safety in this specific context.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15414437](https://pubmed.ncbi.nlm.nih.gov/15414437/) | 1950 | Review | California medicine | Describes histamine's role in tissue/anaphylactic reactions and how antihistaminic drugs block (rather than antagonize) histamine action |
| [13195608](https://pubmed.ncbi.nlm.nih.gov/13195608/) | 1954 | Case series/Uncontrolled | Schweizerische medizinische Wochenschrift | Reports experience with a new antiallergic combination preparation (abstract unavailable) |

---

## US Market Information

No US market license/NDA data is available; the drug is currently recorded as not marketed (未上市) with 0 licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link to allergic urticaria is pharmacologically sound but represents a well-known class effect rather than a novel repurposing opportunity, and current evidence is limited to L4-tier literature from the 1950s with no clinical trials.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank (currently a Blocking/High-severity data gap)
- TFDA package insert warnings/contraindications (currently a Blocking data gap — required before any S1 safety review)
- Modern clinical evidence (trials or contemporary studies) evaluating antihistamine efficacy specifically in allergic/cold urticaria populations
- Clarification of original approved indication(s), since none are currently on record
- Route of administration and dosage form availability data, currently marked "pending"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

