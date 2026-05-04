---
layout: default
title: Acetaminophen Butalbital Caffeine
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 0
---

# Acetaminophen Butalbital Caffeine
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

# Acetaminophen / Butalbital / Caffeine: Drug Repurposing Evaluation — No Prediction Available

## One-Sentence Summary

Acetaminophen / Butalbital / Caffeine is a fixed-dose analgesic combination (commonly known as Fioricet) used for tension-type headaches and migraine relief.
The TxGNN model returned **no predicted new indications** for this combination in the current pipeline run.
Without a repurposing candidate, a full evidence-based evaluation cannot be completed — this report documents the data gaps and recommends remediation steps before proceeding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in data pack |
| Predicted New Indication | None (TxGNN returned no candidates) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No prediction returned |
| US Market Status | Not Marketed (per query result) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No repurposing prediction was returned by the TxGNN model for this combination. As a result, no mechanistic rationale or indication bridge can be constructed at this stage.

Currently, detailed mechanism of action data is not available. Based on known information, Acetaminophen / Butalbital / Caffeine is a three-component combination: acetaminophen provides analgesia and antipyresis, butalbital (a short-acting barbiturate) provides muscle relaxation and sedation, and caffeine acts as an adjuvant analgesic by enhancing CNS penetration and promoting cerebrovascular constriction. Its efficacy in tension-type headache has been established in clinical practice, and mechanistically the combination may be applicable to other pain or headache disorders — but this requires a formal TxGNN run with a correctly mapped DrugBank ID.

The most likely reason for the empty prediction is that the `drugbank_id` field is null, which prevents the knowledge graph from anchoring the drug in the TxGNN embedding space. Resolving this mapping gap is the critical prerequisite for any repurposing analysis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(No predicted indication available — trial search requires a target indication.)*

---

## Literature Evidence

Currently no related literature available.

*(No predicted indication available — literature search requires a target indication.)*

---

## US Market Information

No US FDA license records were returned for this drug combination under the queried name `"ACETAMINOPHEN; BUTALBITAL; CAFFEINE"`.

> **Note:** This combination is commercially available in the US under brand names such as Fioricet and Esgic. The zero-result query likely reflects a name formatting mismatch (semicolon-delimited multi-ingredient string vs. individual ingredient queries). It is recommended to requery using the individual active ingredients or the brand name.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack. Butalbital carries well-known risks of dependence and overuse headache; acetaminophen carries hepatotoxicity risk at high doses. A full safety review is required before any repurposing effort proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no predicted indications for this combination, and the DrugBank ID is missing — without a knowledge graph anchor, no repurposing candidates can be generated or evaluated. All safety and regulatory data fields are also absent.

**To proceed, the following is needed:**

1. **Resolve DrugBank mapping** — Query DrugBank API for each individual active ingredient (acetaminophen DB00316, butalbital DB01083, caffeine DB00201) and assign the correct `drugbank_id` to re-run TxGNN prediction.
2. **Fix regulatory query** — Requery the US FDA database using ingredient-level searches or the brand name "Fioricet" to retrieve NDA records and approved indications.
3. **Retrieve MOA data** — Pull mechanism of action from DrugBank for each component to enable mechanistic plausibility scoring.
4. **Retrieve safety data** — Download the prescribing information to populate key warnings and contraindications, which are currently blocking the safety screen (DG001, severity: Blocking).
5. **Re-run pipeline** — After resolving the above gaps, re-execute the full TxGNN pipeline to obtain predicted indications and generate a complete evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

