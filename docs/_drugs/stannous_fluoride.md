---
layout: default
title: Stannous Fluoride
parent: 僅模型預測 (L5)
nav_order: 1181
evidence_level: L5
indication_count: 1
---

# Stannous Fluoride
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

# Stannous Fluoride: From Dental Caries Prevention to Meningococcal Infection

## One-Sentence Summary

Stannous fluoride is a topical dental agent used to prevent tooth decay through enamel remineralization and antibacterial action against oral biofilm.
The TxGNN model predicts it may be effective for **Meningococcal Infection**,
but this prediction is currently **unsupported by any clinical trials or literature evidence**, and the drug is not marketed in Taiwan.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indications on record) |
| Predicted New Indication | Meningococcal Infection |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, stannous fluoride is a topical dental agent whose activity comes from fluoride and stannous (tin) ions, which promote enamel remineralization and inhibit oral bacterial biofilm formation (e.g., *Streptococcus mutans*).

The predicted new indication — meningococcal infection, a systemic bacterial infection caused by *Neisseria meningitidis* — has no established pharmacological relationship to the original topical dental use. Stannous fluoride is not marketed as a systemic drug, and there is no pharmacokinetic data supporting that a topical dental formulation could achieve the systemic exposure required to treat invasive meningococcal disease.

While stannous and fluoride compounds do have some broad-spectrum antibacterial properties, there is currently no in vitro or in vivo evidence of specific activity against *N. meningitidis*. The high TxGNN score (99.66%) most likely reflects topological similarity within the knowledge graph's "antimicrobial agent" category rather than genuine mechanistic evidence — a typical case of a high prediction score without corroborating mechanistic support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Stannous fluoride is not currently marketed in Taiwan (未上市), and no license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based solely on TxGNN model output (L5, no clinical or literature evidence), and the drug has no established systemic pharmacokinetic profile or market presence in Taiwan. There is no plausible mechanistic pathway connecting a topical dental agent to treatment of invasive meningococcal infection.

**To proceed, the following is needed:**
- Original approved indication and MOA data (currently marked as Data Gap)
- TFDA package insert warnings/contraindications (blocking gap per evidence pack)
- In vitro antimicrobial susceptibility data against *N. meningitidis*
- Pharmacokinetic data demonstrating potential for systemic exposure, if a non-topical route were to be explored
- Any preclinical or case-level evidence before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

