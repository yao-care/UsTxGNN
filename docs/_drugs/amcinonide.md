---
layout: default
title: Amcinonide
parent: 僅模型預測 (L5)
nav_order: 323
evidence_level: L5
indication_count: 8
---

# Amcinonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Amcinonide: From Eczematous Dermatitis to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Amcinonide is a Class II high-potency topical corticosteroid with established clinical use in eczematous dermatitis, supported by multiple double-blind RCTs from the 1970s–1980s.
The TxGNN model predicts it may be effective for **Vulvar Inverted Follicular Keratosis (VIFK)**,
however, there are currently **no registered clinical trials** and **no supporting publications** for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication (topical corticosteroid; clinical use established in eczematous dermatitis) |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from DrugBank. Based on known pharmacological class, amcinonide is a synthetic glucocorticoid that binds to intracellular glucocorticoid receptors, suppressing NF-κB–mediated transcription of pro-inflammatory cytokines (IL-4, IL-13, IFN-γ), inhibiting phospholipase A2 to reduce arachidonic acid metabolites, and producing local vasoconstriction. These mechanisms collectively account for its anti-inflammatory, anti-proliferative, and immunosuppressive effects when applied topically. Multiple double-blind RCTs have confirmed its clinical efficacy in eczematous dermatitis.

Vulvar Inverted Follicular Keratosis (VIFK) is a rare benign keratinizing proliferative lesion driven primarily by squamous epithelial hyperproliferation. While corticosteroids do exert anti-proliferative effects on keratinocytes, this mechanism is not well-matched to the pathogenesis of VIFK — which is more closely associated with inverted follicular architecture and endophytic growth rather than immune-mediated inflammation. There is no mechanistic literature linking glucocorticoid receptor signaling to VIFK regression.

The TxGNN prediction likely reflects shared disease-graph proximity between VIFK and other corticosteroid-responsive keratinocyte disorders (e.g., hypertrophic lichen planus, dermatitis). This is a plausible but highly speculative extrapolation. VIFK is an extremely rare condition, and the complete absence of any clinical or preclinical evidence specific to this indication means this prediction cannot advance beyond model output at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Based on literature evidence collected for the dermatitis indication (rank 7), amcinonide carries a documented paradoxical risk: multiple case reports (PMIDs 3816214, 3160532, 2964991, 2144811, 11683835) describe **allergic contact dermatitis caused by amcinonide itself**. Cross-reactivity within the acetonide corticosteroid group (triamcinolone acetonide, budesonide) has also been reported. This safety signal should be considered for any new topical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based solely on TxGNN model output (Evidence Level L5) with no clinical trials, observational studies, or published literature specifically addressing amcinonide in vulvar inverted follicular keratosis. The mechanistic rationale is insufficient — glucocorticoid anti-proliferative effects are not well-aligned with the pathogenesis of this rare benign keratinizing lesion, and the condition is uncommon enough that conventional drug development economics would not support proceeding without at minimum a plausible preclinical signal.

**To proceed, the following is needed:**
- Confirm mechanism of action via DrugBank API (DG002 remediation)
- Retrieve TFDA package insert warnings and contraindications (DG001 remediation, currently blocking S1 safety evaluation)
- Identify at least one published case report or histopathological study linking corticosteroid use to VIFK or morphologically similar inverted keratinizing lesions
- Perform dermatopathology literature review to assess whether anti-proliferative corticosteroid effects can meaningfully modulate inverted follicular keratosis architecture
- Consider whether the dermatitis indication (rank 7, Evidence Level L2, 4 RCTs) represents a more actionable repurposing target within the same drug profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

