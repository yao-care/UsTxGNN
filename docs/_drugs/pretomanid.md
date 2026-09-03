---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 1080
evidence_level: L5
indication_count: 5
---

# Pretomanid
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

# Pretomanid: From Drug-Resistant Tuberculosis to Candidiasis

## One-Sentence Summary

> Pretomanid is a nitroimidazooxazine antimycobacterial, used globally as part of the BPaL regimen (Bedaquiline + Pretomanid + Linezolid) for extensively drug-resistant (XDR) and treatment-intolerant multidrug-resistant (MDR) pulmonary tuberculosis.
> The TxGNN model predicts it may be effective for **Candidiasis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own mechanism of action provides no plausible link to antifungal activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Taiwan regulatory data (drug is not marketed in Taiwan). Based on the drug's evidence records, it is globally approved as part of the **BPaL regimen** for extensively drug-resistant / treatment-intolerant MDR pulmonary tuberculosis. |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | 未上市 (Not marketed in Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Pretomanid is a nitroimidazooxazine prodrug that requires activation by the mycobacteria-specific enzyme **deazaflavin-dependent nitroreductase (Ddn)**. Once activated, it generates reactive nitrogen species that inhibit mycolic acid synthesis under aerobic conditions, or act as a respiratory poison under anaerobic conditions. Both the activating enzyme system and the downstream target are specific to the *Mycobacterium* genus.

*Candida* species are fungi with a fundamentally different cell wall structure and no known Ddn-homologous activation pathway. There is no mechanistic basis connecting pretomanid's mode of action to antifungal activity. The evidence pack's own mechanistic rationale explicitly flags this: the high TxGNN score most likely reflects a generalized "antimicrobial agent" node linkage in the knowledge graph, rather than a target-specific biological relationship.

For context, the same evidence pack also evaluated **leprosy** (*Mycobacterium leprae*) as a candidate — a much more biologically plausible hypothesis given the shared genus. However, direct in-vitro evidence (PMID 17005816) shows *M. leprae* is **naturally resistant** to pretomanid (PA-824), refuting that hypothesis as well. This suggests the model's high-ranking candidates for this drug should be treated with particular caution until mechanism-consistent evidence emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No Taiwan/US market authorization data available — pretomanid is not currently marketed in Taiwan (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Two data gaps were flagged in the evidence pack — TFDA label warnings/contraindications [Blocking severity] and detailed MOA documentation [High severity] — both currently unresolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidiasis prediction has no clinical or literature support (Evidence Level L5) and no plausible mechanistic link — pretomanid's target (mycobacterial Ddn-mediated mycolic acid synthesis/respiratory inhibition) does not exist in fungal pathogens like *Candida*. This looks like a knowledge-graph artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (Blocking data gap, DG001) — required before any safety pre-assessment (S1) can begin
- Confirmed mechanism of action documentation from DrugBank (High priority, DG002)
- Any in-vitro or preclinical antifungal activity data for pretomanid specifically against *Candida* species, to substantiate or refute the TxGNN signal
- Given that the next-ranked candidate (leprosy) has direct **refuting** in-vitro evidence, and the remaining candidates (coronary artery disease, myocardial ischemia, ALCAPA) have no mechanistic rationale at all, **no candidate in this evidence pack currently warrants advancement beyond Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

