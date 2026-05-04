---
layout: default
title: Acetaminophen Caffeine Dihydrocodeine Bitartrate
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 0
---

# Acetaminophen Caffeine Dihydrocodeine Bitartrate
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

# Acetaminophen + Caffeine + Dihydrocodeine: Combination Analgesic — No Repurposing Prediction Available

## One-Sentence Summary

Acetaminophen + Caffeine + Dihydrocodeine Bitartrate is a fixed-dose combination analgesic used for moderate to moderately severe pain, combining a non-opioid analgesic, a CNS stimulant adjuvant, and a weak opioid. The TxGNN model returned **no predicted new indications** for this combination, and the drug is currently **not marketed in Taiwan** with **no FDA licenses on record**. Evaluation cannot proceed to evidence-level assessment at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain management (moderate to moderately severe) — inferred from drug class; no formal indication record found in TFDA |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction unavailable; no supporting studies identified |
| US Market Status | 未上市 (Not Marketed in Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction is available for this combination, so a mechanistic repurposing rationale cannot be constructed at this time.

From established pharmacology, this combination works through complementary mechanisms: Acetaminophen inhibits central prostaglandin synthesis to reduce pain and fever; Dihydrocodeine acts on μ-opioid receptors to produce analgesia; and Caffeine enhances analgesic efficacy through adenosine receptor antagonism and CNS stimulation. These mechanisms together target pain signalling at multiple levels.

Detailed MOA data was not retrieved from DrugBank (DrugBank query returned 1 result but no structured data was populated in this Evidence Pack), and no formal indication records exist in the TFDA system. Until TxGNN generates a prediction for this combination and MOA data is populated, mechanistic applicability to new indications cannot be assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a TxGNN-predicted indication (no prediction available).

---

## Literature Evidence

Currently no related literature available for evaluation against a predicted indication.

---

## US Market Information

This drug combination has **0 Taiwan FDA licenses** on record. No authorization table can be produced.

> Note: The combination Acetaminophen + Caffeine + Dihydrocodeine is marketed in other jurisdictions (e.g., UK: Paramol, Solpadol variants) but does not appear in the TFDA database. Verification against US FDA Orange Book and international sources is recommended.

---

## Cytotoxicity

This section is not applicable. Acetaminophen + Caffeine + Dihydrocodeine is a non-oncology analgesic combination and does not meet antineoplastic classification criteria.

---

## Safety Considerations

All safety fields returned as data gaps in this Evidence Pack. Please refer to the package inserts for each individual component for safety information:

- **Acetaminophen**: Hepatotoxicity risk at high doses; contraindicated in severe hepatic impairment
- **Dihydrocodeine**: Opioid class warnings — respiratory depression, dependence potential, contraindicated in respiratory depression and acute asthma
- **Caffeine**: CNS stimulant; avoid in anxiety disorders, arrhythmias

Full DDI assessment was not completed (`query_status: not_found`). Given the opioid component, interactions with CNS depressants, MAOIs, and other opioids are clinically significant and must be evaluated before any repurposing work proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evaluation cannot advance because TxGNN returned no predicted indications for this combination, the drug has no TFDA regulatory history, and all safety data fields are unpopulated. There is no repurposing signal to evaluate at this stage.

**To proceed, the following is needed:**

- **Re-run TxGNN** on each individual active ingredient (Acetaminophen, Caffeine, Dihydrocodeine) separately, as the model may not recognise the multi-component string as a single node
- **Populate MOA data** by querying DrugBank individually for each component (DrugBank IDs: Acetaminophen = DB00316, Caffeine = DB00201, Dihydrocodeine = DB01551)
- **Resolve market status** — confirm whether any Taiwan NDA exists under alternate product names or ingredient spellings
- **Complete DDI assessment** using individual ingredient queries against the DDI database
- **Re-assess** once individual-component TxGNN predictions are available; consider whether the combination's safety profile would support any predicted new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

