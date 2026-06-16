---
layout: default
title: Caspofungin
parent: 僅模型預測 (L5)
nav_order: 503
evidence_level: L5
indication_count: 1
---

# Caspofungin
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

以下是根據 Evidence Pack 產生的藥師評估報告：

---

# Caspofungin: From Invasive Fungal Infections to Gastrin Secretion Abnormality

## One-Sentence Summary

Caspofungin is an echinocandin antifungal agent that inhibits fungal β-(1,3)-D-glucan synthase, used clinically for invasive aspergillosis and invasive candidiasis.
The TxGNN model predicts it may be effective for **Gastrin Secretion Abnormality**,
however there are currently **0 clinical trials** and **0 publications** supporting this direction — this is a pure model prediction with no empirical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan marketing authorization; internationally indicated for invasive aspergillosis and invasive candidiasis |
| Predicted New Indication | Gastrin Secretion Abnormality |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Caspofungin is an echinocandin antifungal that selectively inhibits β-(1,3)-D-glucan synthase — an enzyme essential for fungal cell wall integrity. This mechanism is highly specific to fungal biology and has no established interaction with the neuroendocrine pathways governing gastric acid regulation.

The predicted indication, gastrin secretion abnormality, involves dysregulation of gastrin release from antral G cells, mediated primarily through GPCR signalling, proton pump feedback, and *Helicobacter pylori* infection. None of these pathways share known mechanistic overlap with β-(1,3)-D-glucan synthase inhibition or any downstream effect of caspofungin.

A speculative indirect hypothesis could invoke gut fungal dysbiosis influencing enteroendocrine signalling; however, this remains entirely without experimental support. Furthermore, caspofungin is administered exclusively by intravenous infusion for systemic infections — a route incompatible with targeted luminal gut action. The TxGNN score of 99.44% (rank 12,995 globally) is strongly suspected to be a **knowledge graph topology artifact** rather than a genuine biological signal, and should not be interpreted as clinical evidence.

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
There is no clinical, preclinical, or mechanistic evidence connecting caspofungin to gastrin secretion abnormality. The high TxGNN score is most consistent with a knowledge graph false positive (topology artifact), not a real drug–disease biological signal.

**To proceed, the following would be needed:**
- Identification of a plausible mechanistic bridge between β-(1,3)-D-glucan synthase inhibition and gastrin / G-cell regulation
- At least one preclinical study (in vitro or animal model) demonstrating any effect on gastrin secretion or gastric neuroendocrine function
- Graph neighbourhood analysis of TxGNN node DB00520 to rule out topology-driven inflation before allocating further research resources
- MOA data from DrugBank (DG002) and safety label data from the regulatory package insert (DG001) to complete a baseline drug characterisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

