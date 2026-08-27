---
layout: default
title: Linaclotide
parent: 僅模型預測 (L5)
nav_order: 861
evidence_level: L5
indication_count: 3
---

# Linaclotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Linaclotide: From Chronic Constipation to Cauda Equina Syndrome

## One-Sentence Summary

Linaclotide is a locally-acting gut peptide, established for treating IBS-C and chronic idiopathic constipation (based on general pharmacological knowledge; not captured in this evidence pack). The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but **no clinical trials and no literature** currently support this direction, and the model's own mechanistic review flags the link as likely spurious.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in evidence pack (generally known as IBS-C / chronic idiopathic constipation) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data is not available in this evidence pack. Based on the repurposing rationale supplied alongside the prediction, linaclotide is a locally-acting guanylate cyclase-C (GC-C) receptor agonist confined to the intestinal epithelium, with minimal systemic absorption; its action increases chloride/bicarbonate secretion in the gut and has no known effect outside the intestinal lumen.

Cauda equina syndrome is a surgical emergency caused by mechanical compression of nerve roots below the spinal cord — a pathology with no established connection to the GC-C/cGMP signaling pathway linaclotide acts through. The evidence pack itself notes this prediction is most likely a graph artifact: a spurious "gut–nerve" node linkage arising from clinical co-occurrence of constipation and neurogenic bowel symptoms, rather than a genuine pharmacological mechanism.

Given the absence of any mechanistic plausibility, clinical trials, or literature, this prediction should be treated as a hypothesis-generation signal only, not as an actionable repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Linaclotide is currently not marketed under this registry, with no license records available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a raw TxGNN model score (L5) with zero clinical trials, zero literature, and a mechanistic rationale that the evidence pack itself characterizes as likely noise rather than a genuine pharmacological link.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action (MOA) data for linaclotide
- TFDA/label warnings and contraindications (currently blocking safety screening)
- Independent mechanistic or preclinical evidence connecting GC-C agonism to cauda equina pathology before any further evaluation
- Re-screening of lower-ranked candidates (e.g., neurogenic bladder, insomnia) — both also lack supporting evidence and carry similarly weak mechanistic justification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

