---
layout: default
title: Paroxetine
parent: 僅模型預測 (L5)
nav_order: 1017
evidence_level: L5
indication_count: 1
---

# Paroxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Paroxetine: From SSRI Antidepressant Use to Ohdo Syndrome and Variants

## One-Sentence Summary

Paroxetine (DB00715) is a selective serotonin reuptake inhibitor (SSRI); the evidence pack does not record its specific approved indication, and the drug is currently **not marketed** under this record.
The TxGNN model predicts a possible link to **Ohdo Syndrome and Variants**, a rare genetic disorder,
but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record (drug class: SSRI antidepressant; specific indication text unavailable) |
| Predicted New Indication | Ohdo Syndrome and Variants |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug record is not available. Based on known pharmacology, paroxetine is an SSRI that inhibits the serotonin transporter (SERT) to increase synaptic serotonin concentration — this classification is noted in the evidence pack's own rationale field, though the specific original indication text was not captured in this record.

Ohdo syndrome and its variants are rare autosomal dominant developmental disorders caused by pathogenic mutations in chromatin-modifying/transcriptional regulator genes (e.g., *KAT6B*, *MED12*, *KAT6A*, *SETBP1*), presenting with characteristic blepharophimosis facies, intellectual disability, and skeletal/genitourinary anomalies. This is a developmental genetic syndrome, not a disorder of neurotransmitter imbalance.

The evidence pack's own mechanistic assessment concludes there is **no known or inferable biological link** between SSRI pharmacology (SERT inhibition) and the chromatin-regulation pathology underlying Ohdo syndrome. Given the extremely sparse evidence (rank 19,305, no trials, no literature) and the rarity of the target disease in the knowledge graph, this high score is most plausibly a **false positive arising from sparse-node bias** in TxGNN rather than a biologically grounded signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

This drug record is currently **not marketed** (0 authorizations on file). No NDA/license information is available for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has no clinical trial or literature support (Evidence Level L5), and the mechanistic review included in the evidence pack itself identifies no plausible biological link between SSRI pharmacology and Ohdo syndrome's chromatin-regulation pathology — most consistent with a sparse-data false positive rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) — currently a **Blocking** data gap
- Confirmed mechanism of action (MOA) and original approved indication for this drug record
- Any preclinical or case-level evidence specifically linking SSRIs to Ohdo syndrome symptom management before advancing past S0
- Given the genetic/rare-disease nature of the target condition, expert clinical genetics review before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

