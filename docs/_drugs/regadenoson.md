---
layout: default
title: Regadenoson
parent: 僅模型預測 (L5)
nav_order: 1114
evidence_level: L5
indication_count: 4
---

# Regadenoson
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Regadenoson: From Pharmacologic Cardiac Stress Agent to Predicted Anaphylaxis Indication

## One-Sentence Summary

> Regadenoson is a selective A2A adenosine receptor agonist most commonly used clinically as a pharmacologic stress agent for cardiac perfusion imaging; no disease-treatment indication is on file for this drug in the current dataset.
> The TxGNN model predicts it may be effective for **Anaphylaxis**, but this is supported by **0 directly relevant clinical trials** and **0 publications** — the single retrieved trial is unrelated to this hypothesis, and the underlying mechanism actually contradicts regadenoson's known clinical adverse-effect profile.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available data (drug not marketed; clinically used as a pharmacologic cardiac stress-testing agent, not as a disease treatment) |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for regadenoson is not available in this dataset (flagged as a High-severity data gap, DG002). Based on the repurposing rationale supplied with this candidate, regadenoson is a **selective A2A adenosine receptor agonist**. In theory, A2A receptor activation can suppress mast cell degranulation, which provides a plausible pharmacological pathway toward anti-inflammatory or anti-allergic effects — this is the basis for the TxGNN association with anaphylaxis.

However, this mechanistic hypothesis runs directly counter to regadenoson's established clinical safety profile: regadenoson is itself a **known trigger of allergic-type and anaphylactoid reactions**, including rare cases of severe anaphylactic shock, when used in its approved diagnostic setting. In other words, the adverse effect the drug is predicted to *treat* is the same reaction the drug is documented to *cause*. This directional conflict substantially weakens the biological plausibility of the prediction and should be treated as a significant red flag rather than supporting evidence.

No original indication is recorded for this drug in Taiwan (market status: not marketed, 0 licenses), so there is also no approved-indication analog to compare against the predicted new indication — unlike typical repurposing cases where the original and new indications share a disease-area rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | NA | Recruiting | 1000 | Multicenter stress cardiac MRI perfusion imaging study; regadenoson is used here purely as a pharmacologic stress agent to simulate exercise for coronary blood-flow assessment. **Relevance to anaphylaxis treatment: Grade C (low)** — anaphylaxis, if captured at all, would only appear as a safety-monitoring event, not as a treatment endpoint. This trial does not test or support the anaphylaxis hypothesis. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Regadenoson is **not currently marketed** in this jurisdiction. No license/NDA records are available (total licenses: 0).

---

## Other Predicted Indications Also Reviewed (Same Candidate Set)

Three additional TxGNN-predicted indications for regadenoson were reviewed alongside anaphylaxis. All carry the same evidence tier and recommendation:

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|
| Food-dependent exercise-induced anaphylaxis | 99.74% | L5 | Hold | No clinical or literature support; relies on the same unproven mast-cell hypothesis as above |
| Esotropia | 99.12% | L5 | Hold | No known biological link between A2A adenosine signaling and extraocular muscle imbalance; likely reflects a spurious knowledge-graph connection |
| Pseudoallergy | 99.12% | L5 | Hold | Same mechanistic contradiction as anaphylaxis — regadenoson is a known cause of pseudoallergic reactions, not a treatment for them |

---

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug–drug interaction data are not yet available in this dataset (TFDA label data is a Blocking-severity gap, DG001).

**Important context from the repurposing rationale itself:** regadenoson is documented to be capable of inducing allergic-type and anaphylactoid reactions, including rare severe anaphylactic shock, in its current diagnostic use. This should be treated as a safety signal directly relevant to evaluating the anaphylaxis-related predictions above, independent of the still-missing formal label data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications sit at Evidence Level L5 (model prediction only), decision stage S0. The one retrieved clinical trial is mechanistically unrelated to any of the predicted indications, and no supporting literature exists. Most importantly, the anaphylaxis and pseudoallergy hypotheses conflict with regadenoson's own known adverse-effect profile, which undermines rather than supports biological plausibility.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any S1 safety screening
- Confirmed mechanism-of-action data from DrugBank (DG002) to properly assess the A2A-agonist/mast-cell hypothesis
- Preclinical or pharmacological studies directly testing regadenoson's effect on mast cell degranulation/anaphylactic response, ideally resolving the direction-of-effect contradiction
- Any real-world adverse event data on regadenoson-associated allergic reactions, to contextualize risk before considering further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

