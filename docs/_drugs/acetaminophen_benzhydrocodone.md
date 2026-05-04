---
layout: default
title: Acetaminophen Benzhydrocodone
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 0
---

# Acetaminophen Benzhydrocodone
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

# Acetaminophen/Benzhydrocodone: Drug Repurposing Evaluation Report

## One-Sentence Summary

Acetaminophen/Benzhydrocodone is a fixed-dose combination analgesic; benzhydrocodone is a prodrug of hydrocodone (an opioid), paired with acetaminophen (a non-opioid antipyretic/analgesic) for acute pain management.
The TxGNN model returned **no predicted repurposing indications** for this compound pair, likely because the combination molecule is not represented in the current knowledge graph.
This report documents the data gaps and recommends remediation steps before any repurposing analysis can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute pain (based on known pharmacology; no TFDA license on record) |
| Predicted New Indication | — (No TxGNN predictions available) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 — Model prediction only; no actual studies linked |
| US Market Status | Not marketed in Taiwan (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no TxGNN predictions were generated for this drug entry. This is most likely because:

1. **Knowledge graph coverage**: TxGNN's underlying knowledge graph maps individual drug entities (DrugBank nodes). The combination entry "ACETAMINOPHEN; BENZHYDROCODONE" was not resolved to a DrugBank ID, meaning neither the combination nor its prodrug component (benzhydrocodone → hydrocodone) was matched to a graph node that could produce scored disease associations.

2. **Prodrug complexity**: Benzhydrocodone is a prodrug that is converted in vivo to hydrocodone. A repurposing query would need to be re-run under the active moiety (hydrocodone, DrugBank: DB00956) and independently under acetaminophen (DrugBank: DB00316) to surface meaningful predictions.

3. **MOA data unavailable**: Detailed mechanism of action data was not retrieved. Based on known pharmacology, acetaminophen inhibits cyclooxygenase centrally and benzhydrocodone acts via µ-opioid receptor agonism after conversion to hydrocodone. These mechanisms could be queried separately for repurposing signals (e.g., hydrocodone in cough suppression, acetaminophen in fever of unknown aetiology).

Until the DrugBank mapping gap is resolved and the active moiety is queried, repurposing analysis cannot be completed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered under this combination for any repurposed indication.

---

## Literature Evidence

Currently no related literature available (no predicted indication to query against).

---

## US Market Information

This drug combination is not currently licensed in Taiwan. For reference, the US FDA approved Apadaz® (benzhydrocodone/acetaminophen) in 2018 for short-term management of acute pain severe enough to require an opioid. No NDA equivalent is on file with the TFDA.

---

## Cytotoxicity

This section is not applicable. Acetaminophen/benzhydrocodone is an opioid analgesic combination, not an antineoplastic agent.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: All safety fields (key warnings, contraindications, drug interactions) returned as data gaps or were not found in this query cycle. Given that this product contains an opioid component, the following categories are known to carry class-level regulatory warnings and should be verified before any clinical use or repurposing study design:
> - Opioid addiction, abuse, and misuse risk
> - Life-threatening respiratory depression
> - Neonatal opioid withdrawal syndrome
> - Acetaminophen hepatotoxicity (dose-dependent)
> - CNS depressant drug interactions (benzodiazepines, alcohol)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced zero predicted indications because the drug combination could not be mapped to a DrugBank knowledge graph node. Without predictions, there is no repurposing hypothesis to evaluate, and all safety data fields remain unresolved.

**To proceed, the following is needed:**

- [ ] **Resolve DrugBank mapping** (DG001 blocker): Re-query using the active moiety — hydrocodone (DB00956) and acetaminophen (DB00316) — as separate entities to generate TxGNN scores
- [ ] **Retrieve MOA data** (DG002 high): Query DrugBank API for mechanism of action for both components; document µ-opioid receptor agonism and COX inhibition pathways
- [ ] **Download TFDA package insert** (DG001 blocker): Retrieve PDF from TFDA official website to extract warnings, contraindications, and approved indication text
- [ ] **Re-run evidence collection** after DrugBank mapping is resolved: Query ClinicalTrials.gov and PubMed under hydrocodone + candidate disease pairings
- [ ] **Confirm US market context**: Apadaz® (FDA NDA 210730) is the reference product; verify if any ANDA or 505(b)(2) pathway is relevant for Taiwan regulatory strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

