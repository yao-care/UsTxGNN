---
layout: default
title: Ethambutol
parent: 僅模型預測 (L5)
nav_order: 681
evidence_level: L5
indication_count: 5
---

# Ethambutol
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

# Ethambutol: From Tuberculosis to Epiglottitis

## One-Sentence Summary

> Ethambutol is a first-line antituberculosis agent, used as part of standard combination therapy for tuberculosis (evidence for this original use appears within the literature attached to this evidence pack, though no formal TFDA/FDA license record exists in the dataset).
> The TxGNN model predicts it may be effective for **Epiglottitis**,
> but currently **0 clinical trials** and **0 publications** support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (inferred from literature within this evidence pack — no formal license/MOA record available; see note below) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | Not marketed (0 license records in dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on information contained elsewhere in this evidence pack — specifically the mechanistic rationale attached to other candidate indications for this drug — ethambutol inhibits mycobacterial arabinosyl transferase, blocking arabinogalactan synthesis in the mycobacterial cell wall. This activity is specific to the *Mycobacterium* genus and is the basis of its established role in standard four-drug antituberculosis therapy (isoniazid, rifampicin, pyrazinamide, ethambutol).

Epiglottitis, however, is predominantly caused by *Haemophilus influenzae* type b, *Streptococcus pyogenes*, and other non-mycobacterial pathogens. Ethambutol has no antibacterial activity against these organisms, and the evidence pack's own rationale for this candidate explicitly states there is no plausible mechanistic link.

The TxGNN score is high (99.9th+ percentile), but the model's own decision-stage assignment (S0) and evidence level (L5) reflect that this is a pure knowledge-graph signal with zero supporting clinical trials or literature — likely an artifact of graph proximity (e.g., shared "infectious disease of the airway" nodes) rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No approval records found in the current dataset (0 licenses; market status: not marketed). This drug's US regulatory/label data is flagged as a Blocking data gap (DG001) pending retrieval from the FDA label source.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (epiglottitis) has no mechanistic plausibility — the causative pathogens fall outside ethambutol's antimycobacterial spectrum — and no clinical trial or literature evidence exists to counter this. The TxGNN score alone (L5, S0) is insufficient to advance this candidate.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: TFDA/FDA label warnings and contraindications
- Resolve High-severity data gap DG002: confirmed mechanism of action
- Re-check whether the TxGNN disease node for "epiglottitis" is being conflated with tuberculosis-related upper airway involvement, as appears to be happening with the related candidates "laryngitis" (rank 2, L3 evidence, largely driven by laryngeal TB literature) and "peritonitis" (rank 4, L3 evidence, driven by tuberculous peritonitis literature) — those two candidates carry meaningfully stronger evidence and may warrant separate evaluation
- If the above graph-mapping concern is unresolved, deprioritize this candidate over the two S1-stage candidates in the same pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

