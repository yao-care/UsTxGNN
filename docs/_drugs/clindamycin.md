---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 535
evidence_level: L5
indication_count: 6
---

# Clindamycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

以下是根據 Evidence Pack 產生的評估報告：

---

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic with established clinical use in bacterial infections (including skin and soft tissue infections, anaerobic infections, bacterial vaginosis, and ocular toxoplasmosis), with no US NDA data available in this dataset.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No US NDA data available |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on established pharmacological knowledge, Clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit. It is active primarily against Gram-positive organisms and anaerobes, and holds a well-recognised clinical role in ocular toxoplasmosis — an indication that touches on ophthalmic use and may have influenced the TxGNN graph structure.

Punctate epithelial keratoconjunctivitis (PEK) is, however, predominantly caused by non-bacterial etiologies: adenoviral infection, dry eye syndrome, or chemical/toxic irritation. Clindamycin's antibacterial mechanism has no established direct relevance to these pathways. While secondary bacterial superinfection of a compromised ocular surface is theoretically possible, there is no evidence that clindamycin plays a primary therapeutic role in PEK.

The TxGNN model assigned a high prediction score (99.97%), but this likely reflects graph-based proximity among ophthalmic disease nodes in the knowledge graph rather than a genuine pharmacological connection. The mechanistic rationale is considered very low, and this prediction is most probably a false positive driven by disease-class clustering within the model.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 prediction — model output only, with zero supporting clinical trials or literature. Critically, Clindamycin's antibacterial mechanism of action is biologically misaligned with punctate epithelial keratoconjunctivitis, a condition driven primarily by viral and non-infectious etiologies. The high TxGNN score is likely an artefact of ophthalmic disease-node proximity in the knowledge graph, not a reflection of true pharmacological relevance.

**To proceed, the following is needed:**
- Retrieval of US package insert to confirm approved indications, contraindications, and key warnings (currently all listed as data gaps)
- Formal MOA documentation from DrugBank to enable mechanistic link analysis
- Any preclinical evidence (in vitro or animal model) demonstrating Clindamycin activity relevant to PEK pathophysiology — none currently identified
- Review of whether the TxGNN prediction may reflect the known ocular toxoplasmosis use of Clindamycin leaking into adjacent ophthalmic disease nodes, and if graph re-weighting is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

