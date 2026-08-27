---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 807
evidence_level: L5
indication_count: 10
---

# Ioversol
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

# Ioversol: From Diagnostic Contrast Imaging to Osteoarthritis (Low-Confidence Signal)

## One-Sentence Summary

Ioversol (DrugBank DB09134) is an iodinated contrast medium used for diagnostic imaging (angiography, CT, urography); no formal original-indication or mechanism-of-action record is present in this evidence pack. TxGNN's top-ranked prediction, **osteoarthritis susceptibility**, is a genetic susceptibility label rather than a treatable disease and is excluded from consideration. The next candidate, **osteoarthritis**, has **4 clinical trials** and **1 publication**, but all of them study endovascular embolization (Lipiodol/genicular artery embolization) for knee/hand OA pain — ioversol, if present at all, would only serve as the intraprocedural angiography contrast agent, not the tested therapeutic. This is assessed as a mechanistic mismatch, not a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug not marketed in Taiwan; generically known as a low-osmolar iodinated radiographic contrast medium) |
| Predicted New Indication | Osteoarthritis (rank 2; rank-1 "osteoarthritis susceptibility" excluded — see rationale below) |
| TxGNN Prediction Score | 99.63% (osteoarthritis, rank 9427/full list) |
| Evidence Level | L4 |
| Market Status (Taiwan) | 未上市 (Not marketed) |
| Number of Licenses (Taiwan) | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for ioversol in this evidence pack. Based on general pharmacological knowledge, ioversol belongs to the class of non-ionic, low-osmolar iodinated contrast media used for angiography, CT, and urographic imaging — it has no established pharmacodynamic action on joint or immune tissue.

The evidence pack itself flags the top TxGNN hit, "osteoarthritis susceptibility," as inapplicable: it is a genetic-susceptibility label (not a disease entity), and no trial or literature evidence supports it — the repurposing rationale for this rank explicitly states the logic does not apply.

The second-ranked candidate, osteoarthritis, initially looks more substantive because it has both trial and literature support. However, close reading shows all four associated clinical trials and the one associated publication (PMID 38102013, the LipioJoint-1 trial) investigate **transarterial embolization** (using Lipiodol, an iodized-oil embolic agent) as a treatment for knee/hand OA pain. Ioversol is not the embolic or therapeutic agent under study in any of these trials — at most it could appear as the angiographic contrast agent used to guide the procedure. TxGNN most likely picked up a co-occurrence pattern ("contrast agent" + "vascular intervention for OA") rather than a genuine treatment relationship. This is judged a mechanistic mismatch rather than a credible repurposing hypothesis.

---

## Clinical Trial Evidence

*(shown for "osteoarthritis," the highest-evidence candidate; note all trials below test embolization procedures, not ioversol itself)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06497140](https://clinicaltrials.gov/study/NCT06497140) | Phase 3 | Recruiting | 130 | Sham-controlled trial of genicular artery embolization (GAE) for knee OA pain; tests the embolization procedure, not ioversol |
| [NCT06611007](https://clinicaltrials.gov/study/NCT06611007) | Phase 1/2 | Recruiting | 15 | Safety pilot of Lipiodol® arterial embolization for refractory digital (hand) OA |
| [NCT04733092](https://clinicaltrials.gov/study/NCT04733092) | Phase 1 | Completed | 22 | Lipiodol emulsion embolization for inflammatory hypervascularization in knee OA/joint pain |
| [NCT06859164](https://clinicaltrials.gov/study/NCT06859164) | Phase 2 | Recruiting | 50 | NIH-NIAMS-funded pilot sham-controlled trial of genicular artery embolization for knee OA pain (KOOS pain subscore) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | RCT | Diagnostic and Interventional Imaging | LipioJoint-1 trial: safety/efficacy of genicular artery embolization with an ethiodized oil-based emulsion for knee OA; ioversol not the studied agent |

---

## US Market Information

Currently no marketing authorization records are available — ioversol is not marketed in Taiwan under this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are available in this evidence pack, and TFDA label data is flagged as a **blocking data gap** (see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only candidate with any trial/literature support (osteoarthritis) shows a mechanistic mismatch — the underlying studies test embolization procedures and embolic agents (Lipiodol), not ioversol as a therapeutic. The top-ranked TxGNN hit (osteoarthritis susceptibility) is not a valid repurposing target. Combined with the absence of MOA data and TFDA labeling, there is no basis to advance this candidate past initial screening.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (currently a **blocking** data gap — required before any S1 safety screen)
- DrugBank/API-sourced mechanism-of-action data (currently a **high-severity** gap affecting mechanistic-link analysis)
- Confirmation of ioversol's actual role (if any) in the cited OA embolization trials, or new evidence in which ioversol itself is the tested therapeutic agent
- Reassessment if future evidence separates ioversol's specific pharmacology from the embolic agents it happens to co-occur with in these studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

