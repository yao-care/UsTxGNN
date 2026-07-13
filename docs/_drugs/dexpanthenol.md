---
layout: default
title: Dexpanthenol
parent: 僅模型預測 (L5)
nav_order: 596
evidence_level: L5
indication_count: 7
---

# Dexpanthenol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Dexpanthenol: From Wound Healing and Skin Repair to Anorectal Stricture

## One-Sentence Summary

Dexpanthenol (provitamin B5) is a well-established skin and mucosal healing agent, marketed as Bepanthen® in numerous countries, used for wound care, skin barrier repair, and post-procedure recovery — though it holds no regulatory approval in Taiwan.
The TxGNN model ranks **Anorectal Stricture** as its top predicted new indication, with a prediction score of 99.72%.
However, **no clinical trials or published literature** currently support this specific application, and the mechanistic rationale faces a fundamental challenge: anorectal stricture is a structural/fibrotic condition that cannot be reversed through pharmacological means alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Wound healing, skin barrier repair, mucosal recovery (general use; no regulatory record in Taiwan) |
| Predicted New Indication | Anorectal Stricture |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (0 approved products) |
| Number of Approved Licenses | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Dexpanthenol is the alcohol form of pantothenic acid (vitamin B5). Once absorbed, it is enzymatically converted to pantothenic acid and incorporated into Coenzyme A (CoA) — a central cofactor in fatty acid synthesis, energy metabolism, and cellular repair. Through this pathway, dexpanthenol supports lipid synthesis in the skin barrier, stimulates keratinocyte and epithelial cell proliferation, suppresses pro-inflammatory cytokines such as IL-1α, and accelerates wound and mucosal healing. The Bepanthen® Rectal formulation (containing approximately 2.75% dexpanthenol) is available in several European markets for anorectal discomfort, providing indirect evidence that the drug is tolerated in this anatomical region.

Anorectal stricture, however, is a narrowing of the anal canal caused predominantly by fibrous scarring — typically following anorectal surgery, radiation therapy, or chronic inflammatory disease. Fibrosis involves irreversible collagen deposition and tissue remodeling that dexpanthenol's mucosal-repair mechanism cannot reverse. Standard management is mechanical (graduated dilation) or surgical (anoplasty, flap repair). There is no established pharmacological pathway by which CoA-mediated epithelial healing would address the underlying fibrous architecture.

The TxGNN model likely assigned a high score due to anatomical proximity within the knowledge graph — shared ontological nodes between anorectal conditions where dexpanthenol has recognized activity (mucosal soothing, post-hemorrhoidectomy care) and anorectal stricture. This is a known limitation of graph-based prediction models: anatomical co-location can inflate scores in the absence of mechanistic specificity.

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
Anorectal stricture is fundamentally a structural/fibrotic condition requiring mechanical dilation or surgical reconstruction. Dexpanthenol's established mechanism — epithelial repair via CoA-mediated lipid and energy metabolism — has no established pathway to reverse anal canal fibrosis, and the absence of any supporting preclinical, clinical, or literature evidence at this time does not justify advancement.

**To proceed, the following is needed:**
- Preclinical evidence (animal models of anal canal fibrosis or radiation-induced stricture) demonstrating that dexpanthenol reduces collagen deposition or stricture severity
- Mechanistic data showing anti-fibrotic activity beyond epithelial healing — e.g., CoA pathway influence on TGF-β signaling or myofibroblast activation
- If clinical interest remains, consider reframing the research question as **post-operative mucosal healing to prevent stricture formation** (rather than reversing established stricture), which is more aligned with the drug's known biology
- MOA data from DrugBank to formally characterize anti-fibrotic potential
- Safety profile data (package insert warnings, contraindications) before any clinical research can be initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

