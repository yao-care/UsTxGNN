---
layout: default
title: Acetaminophen Butalbital Caffeine Codeine
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 0
---

# Acetaminophen Butalbital Caffeine Codeine
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

# Acetaminophen / Butalbital / Caffeine / Codeine: Combination Analgesic — No Repurposing Prediction Available

## One-Sentence Summary

Acetaminophen / Butalbital / Caffeine / Codeine is a multi-component analgesic combination, commonly used for tension-type headaches refractory to simple analgesics.
The TxGNN model returned **no predicted new indications** for this combination, likely because it is queried as a fixed-dose combination rather than individual active ingredients.
Due to the absence of predictions, clinical trial evidence, and US market authorization data in this Evidence Pack, a substantive repurposing evaluation cannot be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only; in this case, no prediction available |
| US Market Status | Not found in regulatory data |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mechanism of action data for this combination is not available in the current Evidence Pack. Based on general pharmacological knowledge, this combination consists of four components with complementary roles: **acetaminophen** (analgesic/antipyretic), **butalbital** (barbiturate sedative/muscle relaxant), **caffeine** (CNS stimulant, enhances analgesic effect), and **codeine** (opioid analgesic). The combination is recognized as indicated for tension-type headaches and mild-to-moderate pain unresponsive to single-agent therapy.

The absence of TxGNN predictions is most likely a query-level issue: the TxGNN knowledge graph operates on individual drug nodes (mapped via DrugBank IDs), and this combination has no DrugBank ID assigned in the Evidence Pack. Querying the combination string as a single entity would fail to match any node in the graph, resulting in zero predictions.

To unlock repurposing insights, this combination should be decomposed and each active ingredient — particularly **codeine** and **butalbital** — evaluated individually through the TxGNN pipeline.

---

## Clinical Trial Evidence

Currently no related clinical trials registered under this combination entry.

---

## Literature Evidence

Currently no related literature available under this combination entry.

---

## US Market Information

No US regulatory authorization records are available in this Evidence Pack.

> **Note:** Products containing acetaminophen + butalbital + caffeine + codeine (e.g., Fioricet® with Codeine) are known to be marketed in the United States as Schedule III controlled substances. The absence of records here reflects a data retrieval gap, not confirmed non-approval status. Manual verification against the FDA Orange Book is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Given the opioid component (codeine) and barbiturate component (butalbital), this combination carries known risks including respiratory depression, dependence, and CNS depression, particularly in CYP2D6 ultra-rapid metabolizers. These considerations should be incorporated into any safety review once package insert data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no predicted indications, no US regulatory records, and no safety data, making a repurposing evaluation impossible at this stage. The root cause is that TxGNN was queried with a combination string rather than individual DrugBank-mapped components.

**To proceed, the following is needed:**

- **Decompose the query:** Run TxGNN separately for each active ingredient — acetaminophen (`DB00316`), butalbital (`DB00241`), caffeine (`DB00201`), and codeine (`DB00318`) — to retrieve individual repurposing predictions.
- **Obtain MOA data:** Query DrugBank API for each component to populate mechanism of action fields.
- **Retrieve US regulatory data:** Manually search the FDA Orange Book and DailyMed for NDA records for fixed-dose combination products containing these four ingredients.
- **Safety review:** Download and parse the FDA-approved package insert (available on DailyMed) to populate key warnings, contraindications, and drug interaction data.
- **Re-run Evidence Pack generation** once the above gaps are resolved, then re-evaluate at the individual component level before assessing the combination.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

