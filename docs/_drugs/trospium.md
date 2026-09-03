---
layout: default
title: Trospium
parent: 僅模型預測 (L5)
nav_order: 1270
evidence_level: L5
indication_count: 10
---

# Trospium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Trospium: From Overactive Bladder to Irritable Bowel Syndrome

## One-Sentence Summary

> Trospium is a quaternary ammonium, non-selective muscarinic receptor antagonist whose established drug-class use is overactive bladder (OAB); it is not currently licensed/marketed in this jurisdiction.
> The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome**,
> but currently **0 clinical trials** and only **1 loosely related publication** support this direction, and that publication does not actually address IBS.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive Bladder (OAB) — inferred from mechanism-of-action references in the evidence pack; no formal NDA/license record exists for this drug in this market |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 98.04% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Trospium (flagged as a high-severity data gap). Based on the information embedded in the evidence pack, Trospium is a quaternary ammonium, non-selective muscarinic receptor antagonist; its efficacy for overactive bladder has been established as its drug-class use, and — mechanistically — antimuscarinics of this type are used elsewhere (e.g., dicyclomine, hyoscine) as antispasmodics for irritable bowel syndrome, since blocking muscarinic receptors on intestinal smooth muscle can reduce spasm and cramping.

However, the direct evidentiary support for Trospium specifically in IBS is weak. The single cited publication (PMID 33890538) is a Medicare cohort study on antimuscarinic prescribing patterns in **dementia patients with overactive bladder** — it does not evaluate IBS at all and appears to be a topical mismatch rather than direct supporting evidence. No clinical trials targeting IBS were identified. The rationale for this candidate therefore rests entirely on drug-class analogy (antimuscarinic → GI antispasmodic effect), not on trial or literature data specific to Trospium and IBS.

Given the absence of both direct clinical trial evidence and on-topic literature, this prediction should be treated as a hypothesis generated purely from the knowledge-graph mechanism, consistent with its designated evidence level (L5).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33890538](https://pubmed.ncbi.nlm.nih.gov/33890538/) | 2021 | Cohort | Current Medical Research and Opinion | Examined incidence/predictors of antimuscarinic (including non-selective agents like trospium) use among older adults with dementia and overactive bladder — **does not address IBS**; included here only because it is the closest literature match in the evidence pack |

---

## US Market Information

Trospium currently has no license/NDA records in this market (`total_licenses: 0`, market status: Not Marketed). No approved product or indication text is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Official label warnings and contraindications for Trospium are currently a documented data gap of "Blocking" severity — this must be resolved before any safety-relevant decision can be made.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but there are zero clinical trials and no on-topic literature supporting Trospium specifically for IBS — the only cited publication concerns an unrelated OAB/dementia population. Combined with the lack of any market presence or license record for this drug and a blocking gap in official safety labeling, the evidence does not currently meet the bar to advance beyond a research hypothesis.

**To proceed, the following is needed:**
- Official TFDA/regulatory label with warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism-of-action data from DrugBank (currently a data gap)
- IBS-specific clinical trial or on-topic literature evidence (current literature is a topical mismatch)
- Clarification of market/licensing pathway, since the drug is currently unmarketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

